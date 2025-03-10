from view.display_menu_base import DisplayMenuBase


class DisplayMenuInput2(DisplayMenuBase):
    def __init__(self):
        self.title=None
        self.info=None
        super().__init__()
        
    def execute(self, title, info=""):
        
        self.title=title
        self.info=info
        
        self.display_title()
        self.display_info()
    
    def execute_form(self, form_names, to_fill):
        
        self.form_names=form_names
        self.to_fill=to_fill
        
        return self.display_form()    
    
    
    def execute_filled_form(self, form_names):
        self.form_names=form_names
        self.display_filled_form
       
    def excute_options(self, options):
        self.options=options
        return self.display_options()
    
    

        