from view import Display
from model import Information


class AllInformation:
    def __init__(self, options, token=None):
        self.title = "Informationen"
        self.options = options
        self.token = token

    def run(self):
        display_menu = Display()
        information = Information()

        choice = "start"
        while True:
            match choice:

                case "start":
                    display_menu.display_title(self.title)
                    information.get_information()
                    display_menu.display_info(information.response)
                    choice = "options"

                case "options":
                    choice = display_menu.display_options(self.options)
                    return choice

                case _:
                    choice = "options"
