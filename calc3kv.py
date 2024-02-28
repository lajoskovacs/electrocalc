# Electrotechnical calculations
# XL, XC, Ze 
#  R-L    R-C  L-C circuits
# 2024.02.26. - 2024.03.    KL

# import os
# os.environ['KIVY_NO_CONSOLELOG']='1'

from kivy.config import Config 
Config.set('graphics','width','360')
Config.set('graphics','height','800')
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

<PageLabel>:				
	font_size: '18sp'
    foreground_color:1,0,0,1
    background_color:1,1,0,1
    multiline: False
    readonly: True   


<EcalcWidget>:
    do_default_tab: False

    TabbedPanelItem:
        text: 'XL'
        BoxLayout:
            orientation: 'vertical'   
            size_hint: 1, 1/3
            PageLabel:				
                text: 'Induktív reaktancia'	
                size_hint: 1, 1/8

            XL_GridL:
                size_hint: 1, 7/8
 

 

    TabbedPanelItem:
        text: 'XC'
        BoxLayout:           



    TabbedPanelItem:
        text: 'fo'
        BoxLayout:   


<XL_GridL>:
    cols: 2
    padding: '10dp'
    spacing: '20dp'
        
    Button:
        text: 'L'
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
    Button:
        text: 'f'
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
    Button:
        text: 'XL'
    TextInput:				
        text: 'ha'		
		font_size: '16sp'





''')


class PageLabel(TextInput):
    pass


class XL_GridL(GridLayout):
    pass



class EcalcWidget(TabbedPanel):

    def __init__(self):
        super().__init__()

      



class EcalcApp(App):

    def build(self):       
        return EcalcWidget()



if __name__ == '__main__':
    ec= EcalcApp()
    ec.run()


