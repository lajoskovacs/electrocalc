# Electrotechnical calculations
# XL, XC, Ze 
#  R-L    R-C  L-C circuits
# 2024.02.26. - 2024.03.    KL

# import os
# os.environ['KIVY_NO_CONSOLELOG']='1'

from kivy.config import Config 
Config.set('graphics','width','520')
Config.set('graphics','height','1100')
# Config.set('graphics','resizable','0')

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from math import pi
from math import sqrt
from math import atan
from kivy.uix.button import  Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
#from kivy.properties import ObjectProperty
#from kivy.graphics import Color, Ellipse, Line, Rectangle, Point, GraphicException



Builder.load_string('''

<EcalcWidget>:
    do_default_tab: False

    TabbedPanelItem:
        text: 'XL'
        BoxLayout:
            orientation: 'vertical'       
            GridLayout:
                cols: 2
                padding: '10dp'
                spacing: '20dp'
                size_hint: 1, 1/2
                TextInput:				
                    text: 'Induktív reaktancia'	
                    size_hint: 1, 1/2
		            font_size: '20sp'
                    foreground_color:1,0,0,1
                    background_color:1,1,0,1
                    multiline: False
                    readonly: True
                TextInput:				
                    text: '??'
                    size_hint: 1, 1/2

                Button:
                    text: 'L'
                TextInput:				
                    text: 'ha'		
		            font_size: '20sp'
                Button:
                    text: 'f'
                TextInput:				
                    text: 'ha'		
		            font_size: '20sp'
                Button:
                    text: 'XL'
                TextInput:				
                    text: 'ha'		
		            font_size: '20sp'


            BoxLayout:
                orientation: 'vertical'  
                size_hint: 1, 1/2        


    TabbedPanelItem:
        text: 'XC'
        BoxLayout:           



    TabbedPanelItem:
        text: 'fo'
        BoxLayout:   




''')



class EcalcWidget(TabbedPanel):
	
    def __init__(self):
        super().__init__()
      



class EcalcApp(App):

    def build(self):       
        return EcalcWidget()



if __name__ == '__main__':
    ec= EcalcApp()
    ec.run()


