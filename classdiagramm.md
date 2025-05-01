```mermaid

---
title: Client App
---

classDiagram

    Display <-- DepotOverview 
    Display <-- Settings
    Display <-- AccountOverview
    Display <-- DepotBankTransfer
    Display <-- DepotStockSearch
    Display <-- DepotStockTrade
    Display <-- DepotWatchlist

    MainControl --> CreateAccountMenu
    MainControl --> LoginMenu
    MainControl --> AllInformation
    
    DepotControl <-- MainControl
    
    DepotOverview <-- DepotControl
    Settings <-- DepotControl
    AccountOverview <-- DepotControl
    DepotBankTransfer <-- DepotControl
    DepotStockSearch <-- DepotControl
    DepotStockTrade <-- DepotControl
    DepotWatchlist <-- DepotControl

    CreateAccountMenu --> Display 
    Display <-- LoginMenu
    Display <-- AllInformation

    LoginMenu --> LoginForm
    CreateAccountMenu --> RegistrationForm
    AllInformation --> Information

    Settings --> SettingsForm
    DepotOverview --> DepotHistory
    AccountOverview --> FinancialHistory
    DepotBankTransfer --> BankTransfer
    DepotStockSearch --> StockActions
    DepotStockTrade --> StockActions
    DepotWatchlist --> Watchlist

    LoginForm --> ServerRequest
    DepotHistory --> ServerRequest
    FinancialHistory --> ServerRequest
    RegistrationForm --> ServerRequest
    SettingsForm --> ServerRequest
    Information --> ServerRequest
    BankTransfer --> ServerRequest
    StockActions --> ServerRequest
    Watchlist --> ServerRequest

    SettingsForm --|> RegistrationForm

    class Display {
        + line: str
        + display_title(title: str) void
        + display_info(info: str) void
        + display_title_and_info(title: str, info: str) void
        + display_options(options: str) str
        + display_form(form_names: dict), to_fill: object) void
        + display_filled_form(form_names: dict) void
        + display_table(input: dict, column_names: dict) void
    }

    class MainControl{
        + title: str
        + options: dict
        + init() void
        + run() void
    }
    class CreateAccountMenu {
        + title: str
        + information: str
        + options: dict
        + options_failure : dict
        + init() void
        + run() str
    }

    class LoginMenu {
        + title: str
        + options: dict
        + options_failure: dict
        + init() void
        + run() bool, str
    }
    class AllInformation {
        + title: str
        + options: dict
        + token: str
        + init(options: dict, token: str=None)
        + run() str
    }
    class DepotControl {
        + token: str
        + headers: str
        + options: dict
        + depot_overview: object=None
        + stock_search = object=None
        + stock_trade = object=None
        + watchlist = object=None
        + account_overview = object=None
        + bank_transaction = object=None
        + information = object=None
        + settings = object=None
        + init(token: str)
        + delete_token_instance() void
        + run() void
    }
    class DepotBankTransfer {
        + transfer: object
        + options: dict
        + options_make_transfer: dict
        + init(token:str, options: dict) void
        + run() str
    }
    class AccountOverview {
        + account: object
        + title: str
        + options: dict
        + display_menu: object
        + init(token: str) void
        + run() str
        + show_info(input: bool) void
        + show_table(input: bool) void
    }
    class DepotOverview {
        + depot: object
        + title: str
        + options: dict
        + display_menu: object
        + init(token: str) void
        + run() str
        + show_table(input: bool) void
        + show_table_timespan(input: bool) void
    }
    class Settings {
        + depot: object
        + title: str
        + information: str
        + information_2time: str
        + options: dict
        + options_settings: dict
        + otpions_make_change: dict
        + init(token: str, options: dict) void
        + run() str
    }
    class DepotStockSearch {
    
    }
    class DepotStockTrade {
    }
    class DepotWatchlist {
    
    }




    %% Model:
    class RegistrationForm {
    }
    class LoginForm {
    }
    class StockActions {
    }
    class Information {
    }
    class DepotHistory {
    }
    class FinancialHistory {
    }
    class BankTransfer {
    }
    class SettingsForm {
        + token: str
        + data: dict=None
        + form_names_adress: dict
        + form_names_email_adress: dict
        + form_names_ref_account: dict
        + form_names_password: dict
        + name_settings: dict
        + init(token: str) void
        + transmit_changes(type:str) str
        + current_settings() bool
    }
    class Validation {
    }
    class Watchlist {
    }
    class ServerRequest




