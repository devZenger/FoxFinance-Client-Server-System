from fastapi import APIRouter

router = APIRouter()


@router.get("/information/")
async def get_infos():
        return {"message":"Fox Finance offers great service"}