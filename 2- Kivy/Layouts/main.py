#in kivy you will import everything you use
#from smallercase import AfterCase
import kivy 
from kivy.app import App
from kivy.metrics import dp #*for DP
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
class StackExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(ord('A'), ord('Z') + 1):
            b = Button(text=chr(i), size_hint=[None, None], size=[100,100])
            self.add_widget(b)


class GridExample(GridLayout):
    pass


class AnchorExample(AnchorLayout):
    pass

class BoxExample(BoxLayout):
   """  def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical' # default horizantal
        b1 = Button(text = "A")
        b2 = Button(text = "B")
        b3 = Button(text = "C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3) """

class MainWidget(Widget):
    pass

#extend App module
class MyApp(App):
    pass
    
MyApp().run() # run app

