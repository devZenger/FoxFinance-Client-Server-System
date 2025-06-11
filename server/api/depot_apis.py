from typing import Annotated
from fastapi import Depends, APIRouter

from utilities import excptions_handler, check_not_None_and_empty
from service import (customer_name,
                     depot_overview,
                     get_current_active_user,
                     search_stock,
                     load_watchlist,
                     editing_watchlist,
                     update_settings,
                     search_current_settings)
from schemas import User, WatchlistOrder, Settings

router = APIRouter()


# Overview:
# 1. get(/depot/)
# 2. get("/depot/depotoverview/")
# 3. get(/depot/stocksearch/{search_term})
#
# watchlist
# 4. get("/depot/watchlist/")
# 5. post("/depot/editingwatchlist/")
# 6. delete("/depot/editingwatchlist/")
#
# settings
# 7. get("/depot/settings/")
# 8. patch("/depot/changesettings/")


# 1. get(/depot/)
@router.get("/depot/")
async def get_depot(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        name = customer_name(current_customer["customer_id"])
        return {"message": name}

    except Exception as e:
        excptions_handler(e, "get_depot() (dept_overview_apis.py)")


# 2. /depot/depotoverview/
@router.get("/depot/depotoverview/")
async def get_depot_overview(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        depot = depot_overview(current_customer["customer_id"])
        return {"message": depot}

    except Exception as e:
        excptions_handler(e, "get_depot_overview() (dept_overview_apis.py)")


# 3. get(/depot/stocksearch/{search_term})
@router.get("/depot/stocksearch/{search_term}")
async def get_stock_search(search_term: str, current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        check_not_None_and_empty(search_term)
        result = search_stock(search_term)
        return {"message": result}

    except Exception as e:
        excptions_handler(e, "get_stock_search() (depot_stock_api.py)")


# 4. get("/depot/watchlist/")
@router.get("/depot/watchlist/")
async def get_watchlist(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        result = load_watchlist(current_customer["customer_id"])
        return {"message": result}

    except Exception as e:
        excptions_handler(e, "get_watchlist() (depot_stock_api.py)")


# 5. post("/depot/editingwatchlist/")
@router.post("/depot/editingwatchlist/")
async def post_editing_watchlist(watchlist_order: WatchlistOrder,
                                 current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        wl_order = watchlist_order.model_dump()
        editing_watchlist(current_customer["customer_id"], True, wl_order)

    except Exception as e:
        excptions_handler(e, "post_edditing_watchlist() (depot_stock_api.py)")


# 6. delete("/depot/editingwatchlist/")
@router.delete("/depot/editingwatchlist/")
async def delete_editing_watchlist(watchlist_order: WatchlistOrder,
                                   current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        wl_order = watchlist_order.model_dump()
        editing_watchlist(current_customer["customer_id"], False, wl_order)

    except Exception as e:
        excptions_handler(e, "delete_edditing_watchlist() (depot_stock_api.py)")


# 7. get("/depot/settings/")
@router.get("/depot/settings/")
async def get_settings(current_customer: Annotated[User, Depends(get_current_active_user)]):

    try:
        current_settings = search_current_settings(current_customer["customer_id"])

        return {"message": current_settings}

    except Exception as e:
        excptions_handler(e, "get_settings() (depot_settings_api.py)")


# 8. patch("/depot/changesettings/")
@router.patch("/depot/changesettings/")
async def change_settings(settings: Settings, current_customer: Annotated[User, Depends(get_current_active_user)]):

    new_settings = settings.model_dump(exclude_unset=True)

    try:
        if new_settings == {}:
            raise ValueError("Es wurden keine Datensätze übermittelt.")
        update_settings(current_customer["customer_id"], new_settings)
        return {"message": "Updated"}

    except Exception as e:
        excptions_handler(e, "change_settings() (depot_settings_api.py)")
