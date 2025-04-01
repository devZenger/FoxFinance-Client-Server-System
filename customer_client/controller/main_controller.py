import sys
from view import DisplayMenuOption

from .main_create_account import CreateAccountMenu
from .main_login import LoginMenu
from .depot_controller import DepotControl


class MainControll:
    def __init__(self):
        self.option = {"1. Start": "start",
                       "2. Login": "login",
                       "3. Login erstellen": "a_form",
                       "4. Informationen": "information",
                       "5. Beenden": "exit"}

    def run(self):

        choice = "welcome"

        while True:

            match choice:
                case "welcome":
                    title = "Hauptmenü"
                    info = "Willkommen bei Fox"
                    display_menu = DisplayMenuOption(title, info)
                    choice = display_menu.execute(self.option)

                case "start":
                    title = "Hauptmenü"
                    display_menu = DisplayMenuOption(title, info)
                    choice = display_menu.execute(self.option)

                case "a_form":
                    create_account = CreateAccountMenu()
                    choice = create_account.run()

                case "login":
                    login_menu = LoginMenu()
                    success, token = login_menu.run()
                    if success:
                        depot_controller = DepotControl(token)
                        depot_controller.run()

                        del depot_controller
                        del token

                    choice = "start"

                case "information":
                    title ="Informationen"
                    info = "in Bearbeitung"
                    display_menu = DisplayMenuOption(title, info)
                    choice = display_menu.execute(self.option)

                case "exit":
                    sys.exit(0)
