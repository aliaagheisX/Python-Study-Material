#in kivy you will import everything you use
#from smallercase import AfterCase

import kivy 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout


class Tools(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        righTools = ['*', '-', '+']
        for i in range(3,0,-1):
            for j in range(i*3-2,i*3+1):
                b = Button(text = f"{j}", size_hint=[0.25,0.2])
                self.add_widget(b)
                
            self.add_widget(Button(text = righTools[i-1], size_hint=[0.25,0.2]))
            
        toolList = ['C', '0', 'DEL', '/']
        for i in toolList:
            self.add_widget(Button(text = i, size_hint=[0.25,0.2]))
        
        


#extend App module
class MyApp(App):
    pass
    
MyApp().run() # run app

