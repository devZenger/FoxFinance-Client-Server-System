from pydantic import BaseModel

from repository import (insert_one_table,
                        remove_from_one_table,
                        latest_trade_day_entry,
                        watchlist_overview)

from database import update_single_stock_datas


class WatchlistOrder(BaseModel):
    isin: str
    transaction_type: bool


def load_watchlist(customer_id):

    result = watchlist_overview(customer_id)

    return result


def editing_watchlist(customer_id, watchlist_order: WatchlistOrder):

    result = latest_trade_day_entry(watchlist_order.isin)

    to_eddit = {"customer_id": customer_id,
                "isin": watchlist_order.isin}

    if watchlist_order.transaction_type is False:
        remove_from_one_table("watchlist", to_eddit)

    elif watchlist_order.transaction_type:
        to_eddit["price"] = result["close"]

        update_single_stock_datas(to_eddit["isin"])

        insert_one_table("watchlist", to_eddit)

    else:
        raise ValueError("Transaction_type is not bool")


if __name__ == "__main__":

    test = WatchlistOrder(isin="DE000SYM9999", transaction_type=True)

    answer = editing_watchlist(1, test)

    print("answer", answer)
