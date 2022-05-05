#in kivy you will import everything you use
#from smallercase import AfterCase

import kivy 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout


class NumberBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        k = 1
        for i in range(4):
                box = BoxLayout()
                for j in range(i+1):
                    b = Button(text=f"{k}")
                    box.add_widget(b)
                    k=k+1
                    
                self.add_widget(box)
                


#extend App module
class MyApp(App):
    pass
    
MyApp().run() # run app

