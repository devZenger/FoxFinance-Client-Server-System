from .display_menu_form import DisplayMenuForm

class DisplayMenuLogin(DisplayMenuForm):
    def __init__(self, menu_title, menu_points, form_names, to_fill, info=""):
       
        super().__init__(menu_title, menu_points, form_names, to_fill, info)
    
    def execute(self):
        self.display_title()
        
        self.display_info()
        
        self.display_form()
        
        self.display_option()