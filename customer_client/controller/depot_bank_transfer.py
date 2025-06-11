from view import Display
from model import BankTransfer


class DepotBankTransfer:
    def __init__(self, options):
        self.title = "Überweisung"
        self.options = options
        self.options_make_transfer = {"1. Geld überweisen": "make_transfer",
                                      "2. Abbrechen": "options"}

    def run(self, token):
        self.transfer = BankTransfer()
        display_menu = Display()
        form_names = self.transfer.form_names

        choice = "start"
        start = True

        while True:
            match choice:

                case "start":
                    display_menu.display_title_and_infos(self.title, self.transfer.actual_balance(token))
                    if start:
                        start = False
                        choice = "transfer"
                    else:
                        choice = "options"

                case "transfer":
                    form_filled = display_menu.display_form(form_names, self.transfer)
                    if form_filled:
                        display_menu.display_filled_form()
                        choice = display_menu.display_options(self.options_make_transfer)
                    else:
                        "options"

                case "make_transfer":
                    success, result = self.transfer.make_transfer(token)
                    if success:
                        display_menu.display_dic_in_dic(result)
                    else:
                        display_menu.display_info(result)

                    choice = "start"

                case "options":
                    choice = display_menu.display_options(self.options)
                    return choice

                case _:
                    choice = "options"
