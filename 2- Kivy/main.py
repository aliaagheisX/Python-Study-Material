#in kivy you will import everything you use
#from smallercase import AfterCase

import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass

#extend App module
class MyApp(App):
    pass
    
MyApp().run() # run app

