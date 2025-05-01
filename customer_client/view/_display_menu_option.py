from ._display_menu_base import DisplayMenuBase


class DisplayMenuOption(DisplayMenuBase):
    
    line = "-" * 80
    
    def __init__(self, title, info=""):
        self.title= title
        self.info=info
        super().__init__()
        
    def execute(self, options):
        self.options=options
        election = True
        self.display_title()
        
        self.display_info()
        
 
            
        return self.display_options()

    
        
    
                