#in kivy you will import everything you use
#from smallercase import AfterCase

import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class WidgetExamples(GridLayout):
    i = 0
    txt = StringProperty(f'{i}')
    def onClickMe(self):
        self.i += 1
        self.txt = f'{self.i}'





#extend App module
class MyApp(App):
    pass
    
MyApp().run() # run app

