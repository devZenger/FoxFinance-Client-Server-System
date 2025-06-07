from view import Display
from model import Welcome


class DepotStartMenu:
    def __init__(self, options):
        self.name = None
        self.title = "Willkommen in ihren Depot"
        self.options = options

    def run(self, token):
        succes = False
        self.welcome = Welcome()
        display_menu = Display()
        if self.name is None:
            succes = self.welcome.customer_name(token)
            self.name = self.welcome.response
        if succes:
            self.title = f"{self.title} {self.name}"

        display_menu.display_title(self.title)
        choice = display_menu.display_options(self.options)

        return choice
