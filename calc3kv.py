# Electrotechnical calculations
# XL, XC, Ze 
#  R-L    R-C  L-C circuits
# 2024.02.26. - 2024.03.    KL

# import os
# os.environ['KIVY_NO_CONSOLELOG']='1'

from kivy.config import Config 
Config.set('graphics','width','400')
Config.set('graphics','height','600')
# Config.set('graphics','resizable','0')

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from math import pi
from math import sqrt
from math import atan
#from kivy.uix.button import  Button
#from kivy.uix.textinput import TextInput
#from kivy.uix.label import Label
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.gridlayout import GridLayout
#from kivy.properties import ObjectProperty
#from kivy.graphics import Color, Ellipse, Line, Rectangle, Point, GraphicException



Builder.load_string('''

<EcalcWidget>:


''')



class EcalcWidget(FloatLayout):
	
    def __init__(self):
        super().__init__()
      



class EcalcApp(App):

    def build(self):       
        return EcalcWidget()



if __name__ == '__main__':
    ec= EcalcApp()
    ec.run()


