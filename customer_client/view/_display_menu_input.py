from customer_client.view._display_menu_base import DisplayMenuBase


class DisplayMenuInput(DisplayMenuBase):
    def __init__(self, title, info=""):
        self.title=title
        self.info=info
        super().__init__()
        
    
    
    def execute(self, options, form_names, to_fill ):
        self.options=options
        self.form_names=form_names
        self.to_fill=to_fill
        
        self.display_title()
        
        self.display_info()
        
        self.display_form()    
       
        return self.display_options()

        