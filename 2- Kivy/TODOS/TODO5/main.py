#in kivy you will import everything you use
#from smallercase import AfterCase

import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty

class WidgetExamples(GridLayout):
    count_enable = BooleanProperty(True)
    i = 0
    txt = StringProperty(f'{i}')
    def onToggleMe(self, toggle):
        toggle.text = 'ON' if toggle.state == 'down' else 'OFF'
        self.count_enable = False if toggle.state == 'down' else True
    
    def onClickMe(self):
        self.i += 1
        self.txt = f'{self.i}'















#extend App module
class MyApp(App):
    pass
    
MyApp().run() # run app

