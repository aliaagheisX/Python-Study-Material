#in kivy you will import everything you use
#from smallercase import AfterCase

import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty


class WidgetExample3(GridLayout):
    txt = StringProperty()
    def validateMe(self,inp):
        self.txt = inp.text






















class WidgetExample2(GridLayout):
    pass
        









class WidgetExample1(GridLayout):
    i = 0
    txt = StringProperty(f'{i}')
    
    def onClickMe(self):
        self.i += 1
        self.txt = f'{self.i}'






#extend App module
class MyApp(App):
    pass
    
MyApp().run() # run app

