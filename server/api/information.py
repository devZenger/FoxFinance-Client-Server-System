from fastapi import APIRouter, HTTPException

from service import all_order_charges

router = APIRouter()


@router.get("/information/")
async def get_information():

        try:
                charges = all_order_charges()
                return {"message": charges}

        except Exception as e:
                print(f"Fehler bei get_information.\nError: {e}\n")
                raise HTTPException(status_code=422, detail=str(e))
