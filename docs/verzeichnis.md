<pre style="font-size:12px; font-family:Consolas;">
FoxFinance/
├── customer_client/
│    ├── controller/
│    │    ├── __init__.py
│    │    ├── depot_bank_transfer.py
│    │    ├── depot_controller.py
│    │    ├── depot_financial_overview.py
│    │    ├── depot_overview.py
│    │    ├── depot_settings.py
│    │    ├── depot_start_menu.py
│    │    ├── depot_stock_search.py
│    │    ├── depot_stock_trade.py
│    │    ├── depot_watchlist.py
│    │    ├── information.py
│    │    ├── main_controller.py
│    │    ├── main_create_account.py
│    │    └── main_login.py
│    ├── model/
│    │    ├── __init__.py
│    │    ├── bank_transfer.py
│    │    ├── depot_history.py
│    │    ├── depot_settings_form.py
│    │    ├── financial_historey.py
│    │    ├── information.py
│    │    ├── login_form.py
│    │    ├── registratrtion_form.py
│    │    ├── stock_actions.py
│    │    ├── time_check.py
│    │    ├── validation.py
│    │    └── watchlist.py
│    ├── service/
│    │    ├── __init__.py
│    │    └── server_request.py
│    ├── view/
│    │    ├── __init__.py            
│    │    ├── display.py
│    │    └── utility.py
│    └── app.py
├── docs/
│    ├── images/
│    │    └── 
│    ├── customer_client_classdiagramm.puml
│    ├── relationales_datenbankmodell.dbml
│    ├── server__classdiagramm.puml
│    └── verzweichnis.md
├── server/
│    ├── api/
│    │    ├── __init__.py
│    │    ├── authentication_apis.py
│    │    ├── create_customer_account.py
│    │    ├── depot_financial_apis.py
│    │    ├── depot_overview_apis.py
│    │    ├── depot_settings_apis.py
│    │    ├── depot_stock_apis.py
│    │    └── information_api.py
│    ├── database/
│    │    ├── sqlite_scripts/
│    │    │    ├── __init__.py
│    │    │    ├── create_sqlite_db.py
│    │    │    ├── customer_adresses.csv
│    │    │    ├── dax.csv
│    │    │    ├── import_customer_data_to_db.py
│    │    │    ├── import_dax_data_to_db.py
│    │    │    ├── import_stock_data_to_db.py
│    │    │    ├── insert_base_data_to_db.py
│    │    │    └──
│    │    ├── __init__.py
│    │    ├── FoxFinanceData.db
│    │    └── update_database.py
│    ├── logger/
│    │    ├── __init__.py
│    │    ├── config.py
│    │    └── logger.py
│    ├── repository/
│    │    ├── __init__.py
│    │    ├── authentication_repo.py
│    │    ├── customer_repo.py
│    │    ├── db_executor.py
│    │    ├── depot_repo.py
│    │    ├── financial_repo.py
│    │    ├── insert_remove_repo.py
│    │    ├── order_charges_repo.py
│    │    ├── repo_utility.py
│    │    ├── search_repo.py
│    │    ├── stock_repo.py
│    │    ├── sun_repo.py?
│    │    ├── transaction_repo.py
│    │    ├── update_repo.py
│    │    └── watchlist_repo.py
│    ├── schemas
│    │    ├── __init__.py
│    │    ├── authentication_schemas.py
│    │    ├── form_schemas.py
│    │    └── transaction_schema.py
│    ├── service
│    │    ├── __init__.py
│    │    ├── authentication_token.py
│    │    ├── customer_registration.py
│    │    ├── depot_service.py
│    │    ├── financiatl_service.py
│    │    ├── information_service.py
│    │    ├── settings_jservice.py
│    │    ├── stock_service.py
│    │    ├── utility.py
│    │    ├── validation_service.py
│    │    └── watchlist_service.py
│    ├── __init__.py
│    └── main_server.py
├── README.md
└── requirements.txt
</pre>







