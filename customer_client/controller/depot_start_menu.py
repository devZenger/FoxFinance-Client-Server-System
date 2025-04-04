from view import DisplayMenu


class DepotStartMenu:
    def __init__(self, options):
        self.title = "Willkommen in ihren Depot"
        self.options = options

    def run(self):

        display_menu = DisplayMenu()

        display_menu.display_title(self.title)
        choice = display_menu.display_options(self.options)

        return choice
