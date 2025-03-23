from fastapi import FastAPI
import uvicorn

from api import information, create_customer_accout, customer_depot, authentication, depot_stock_apis, depot_information, depot_history_apis
from api import depot_financial_apis, depot_settings_api

server = FastAPI()



server.include_router(information.router)
server.include_router(create_customer_accout.router)

server.include_router(authentication.router)
server.include_router(customer_depot.router)

server.include_router(depot_stock_apis.router)
server.include_router(depot_financial_apis.router)
server.include_router(depot_history_apis.router)
server.include_router(depot_settings_api.router)
server.include_router(depot_information.router)


@server.get("/")
async def root():
    return {"message": "Welcome to Fox Finance Service"}


def start_server():
    uvicorn.run(
        "main_server:server",
        host="127.0.0.1",
        port=8000,
        log_level="debug",
        reload=True)



if __name__ == "__main__":

    start_server()
    
    