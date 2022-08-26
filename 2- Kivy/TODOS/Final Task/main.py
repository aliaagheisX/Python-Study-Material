#in kivy you will import everything you use
#from smallercase import AfterCase

import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget



 
class WidgetExample2(GridLayout):
    clicked = []
    cells = []
    def onClick(self, cell):
        pass
        """ if cell.state == 'normal':
            self.clicked.remove(cell)
        elif len(self.clicked) >= 2:
            cell.state = 'normal'
        else :
            self.clicked.append(cell)
            
        if len(self.clicked) == 2:
            pass """
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        for i in range(16):
            self.cells.append(ToggleButton())
            ToggleButton().add_widget(widget)
            self.cells[i].bind(on_press=self.onClick)
            self.add_widget(self.cells[i])

#extend App module
class MyApp(App):
    pass
    
MyApp().run() # run app

