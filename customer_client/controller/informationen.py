from view import DisplayMenu
from model import Information


class AllInformation:
    def __init__(self, options, token=None):
        self.title = "Informationen"
        self.options = options
        self.token = token

        self.options = {"1. Server anfragen: ": "stock_search"}

    def run(self):
        display_menu = DisplayMenu(self.title)
        information = Information()
        
        choice = "start"
        while True:
            match choice:

                case "start":
                    status = information.get_information()
                    if status:
                        display_menu.display_dic(information.response)
                    else:
                        display_menu.display_info(information.response) 

                    choice = "options"

                case "options":
                    choice = display_menu.display_options(self.options)
                    return choice

                case _:
                    choice = "options"

