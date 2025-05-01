from view import Display
from model import BankTransfer


class DepotBankTransfer:
    def __init__(self, token, options):

        self.transfer = BankTransfer(token)
        self.options = options
        self.title = "Überweisung"

        self.options_make_transfer = {"1. Geld überweisen": "make_transfer",
                                      "2. Abrechen": "options"}

    def run(self):

        display_menu = Display()

        self.information = self.transfer.actual_balance()

        form_names = self.transfer.form_names

        display_menu.display_title(self.title)

        choice = "start"
        start = True

        while True:
            match choice:

                case "start":
                    display_menu.display_title_and_infos(
                        self.title, self.transfer.actual_balance())
                    if start:
                        start = False
                        choice = "transfer"
                    else:
                        choice = "options"

                case "transfer":
                    display_menu.display_form(form_names, self.transfer)
                    display_menu.display_filled_form()
                    choice = display_menu.display_options(
                        self.options_make_transfer)

                case "make_transfer":
                    success, result = self.transfer.make_transfer()
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
