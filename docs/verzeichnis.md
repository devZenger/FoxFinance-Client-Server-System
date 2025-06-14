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
│    │    ├── depot_welcome.py
│    │    ├── financial_historey.py
│    │    ├── information.py
│    │    ├── login_form.py
│    │    ├── model_utilities.py
│    │    ├── registratrtion_form.py
│    │    ├── stock_actions.py
│    │    ├── validation.py
│    │    └── watchlist.py
│    ├── service/
│    │    ├── __init__.py
│    │    └── server_request.py
│    ├── view/
│    │    ├── __init__.py            
│    │    └── display.py
│    └── app.py
├── docs/
│    ├── images/
│    │    └── (enthält .PNG-Bilddateien für die README-Datei)
│    ├── customer_client_classdiagramm.puml
│    ├── relationales_datenbankmodell.pdf
│    ├── relationales_datenbankmodell.dbml
│    ├── server_classdiagramm.puml
│    └── verzweichnis.md
├── server/
│    ├── api/
│    │    ├── __init__.py
│    │    ├── depot_api.py
│    │    ├── depot_trade_and_transfer_apis.py
│    │    ├── information_api.py
│    │    └── registration_and_auth_apis.py
│    ├── database/
│    │    ├── sqlite_scripts/
│    │    │    ├── __init__.py
│    │    │    ├── create_sqlite_db.py
│    │    │    ├── customer_addresses.csv
│    │    │    ├── dax.csv
│    │    │    ├── import_customer_data_to_db.py
│    │    │    ├── import_dax_data_to_db.py
│    │    │    ├── import_stock_data_to_db.py
│    │    │    ├── insert_base_data_to_db.py
│    │    │    ├── max_mustermann.py
│    │    │    └── mustermann_transactions.csv
│    │    ├── __init__.py
│    │    ├── FoxFinanceData.db
│    │    └── update_database.py
│    ├── keys/
│    │    ├── __init__.py
│    │    ├── demo_account_key.py
│    │    ├── demo_token_key.py
│    │    └── key_script.py
│    ├── logger/
│    │    ├── log_files/
│    │    └── (enthält .txt-Dateien)
│    │    ├── __init__.py
│    │    ├── config.json
│    │    └── logger.py
│    ├── repository/
│    │    ├── __init__.py
│    │    ├── authentication_repo.py
│    │    ├── customer_repo.py
│    │    ├── db_operator.py
│    │    ├── financial_repo.py
│    │    ├── insert_remove_repo.py
│    │    ├── order_charges_repo.py
│    │    ├── search_repo.py
│    │    ├── stock_repo.py
│    │    ├── transaction_repo.py
│    │    ├── update_repo.py
│    │    └── watchlist_repo.py
│    ├── schemas/
│    │    ├── __init__.py
│    │    ├── authentication_schemas.py
│    │    ├── form_schemas.py
│    │    └── transaction_schema.py
│    ├── service/
│    │    ├── __init__.py
│    │    ├── authentication_token.py
│    │    ├── depot_service.py
│    │    ├── financiatl_service.py
│    │    ├── information_service.py
│    │    ├── registration_and_settings_service.py
│    │    ├── stock_service.py
│    │    ├── validation_service.py
│    │    └── watchlist_service.py
│    ├── utilities/
│    │    ├── __init__.py
│    │    ├── bamnk_account_encryption.py
│    │    ├── check_and_error_msg.py
│    │    ├── config_loader.py
│    │    ├── exceptions_and_handler.py
│    │    ├── repo_utlities.py
│    │    └── service_utilites.py
│    ├── __init__.py
│    ├── config.json
│    └── main_server.py
├── README.md
└── requirements.txt
</pre>







