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
        text: 'XL'L
        BoxLayout:
            orientation: 'vertical'   
            size_hint: 1, 1/3
            PageLabel:				
                text: 'Induktív reaktancia'	
                size_hint: 1, 1/5

            XL_GridL:
                size_hint: 1, 4/5
 

    TabbedPanelItem:
        text: 'XC'
        BoxLayout:           
            orientation: 'vertical'   
            size_hint: 1, 1/3
            PageLabel:				
                text: 'Kapacitív reaktancia'	
                size_hint: 1, 1/5

            XC_GridL:
                size_hint: 1, 4/5
 

    TabbedPanelItem:
        text: 'fo'
        BoxLayout:   
            orientation: 'vertical'   
            size_hint: 1, 1/3
            PageLabel:				
                text: 'Rezonancia frekvencia'	
                size_hint: 1, 1/5

            Fo_GridL:
                size_hint: 1, 4/5


    TabbedPanelItem:
        text: 'RLC'
        BoxLayout:           
            orientation: 'vertical'   
            size_hint: 1, 1/2
            PageLabel:				
                text: 'Soros RLC'	
                size_hint: 1, 1/7

            RLC_GridL:
                size_hint: 1, 6/7


    TabbedPanelItem:
        text: 'R'
        BoxLayout:   
            orientation: 'vertical'   
            size_hint: 1, 2/5
            PageLabel:				
                text: 'Vezeték ellenállása'	
                size_hint: 1, 1/5
            R_GridL:
                size_hint: 1, 4/5          




    TabbedPanelItem:
        text: 'RC'
        BoxLayout:   
            orientation: 'vertical'   
            size_hint: 1, 1/2
            PageLabel:				
                text: 'RC szűrő (aluláteresztő)'	
                size_hint: 1, 1/7
            RC_GridL:
                size_hint: 1, 6/7


    TabbedPanelItem:
        text: 'CR'
        BoxLayout:   
            orientation: 'vertical'   
            size_hint: 1, 1/2
            PageLabel:				
                text: 'CR szűrő (felüláteresztő)'	
                size_hint: 1, 1/7
            CR_GridL:
                size_hint: 1, 6/7



<XL_GridL>:
    xl_textin: xl_text
    l_textin: L_text
    f_textin: f_text
    cols: 2
    padding: '10dp'
    spacing: '20dp'
       
    Button:
        text: 'Frekvencia, f (Hz)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.f_button_click()
    TextInput:	
        id: f_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Induktivitás, L (mH)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.l_button_click()
    TextInput:			
        id: L_text	
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'XL (ohm)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.xl_button_click()
    TextInput:		
        id: xl_text		
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1


<XC_GridL>:
    xc_textin: xc_text
    c_textin: C_text
    f_textin: f_text
    cols: 2
    padding: '10dp'
    spacing: '20dp'
        
    Button:
        text: 'Frekvencia, f (Hz)'
        color: 0.5, 0.6, 0.7, 1
        root.f_button_click()
    TextInput:	
        id: f_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Kapacitás, C (nF)'
        color: 0.5, 0.6, 0.7, 1
        root.c_button_click()
    TextInput:	
        id: C_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'XC (ohm)'
        color: 0.5, 0.6, 0.7, 1
        root.xc_button_click()
    TextInput:	
        id: xc_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1


<Fo_GridL>:
    cols: 2
    padding: '10dp'
    spacing: '20dp'
        
    Button:
        text: 'Induktivitás, L (mH)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Kapacitás, C (nF)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Rezonancia fr. fo (Hz)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1


<RLC_GridL>:
    cols: 2
    padding: '10dp'
    spacing: '10dp'

    Button:
        text: 'Frekvencia, f (Hz)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1    
    Button:
        text: 'Induktivitás, L (mH)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Kapacitás, C (nF)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1

    Button:
        text: 'Impedancia, Ze (ohm)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1

    Button:
        text: 'Fázisszög, fi (fok)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1



<RC_GridL>:
    cols: 2
    padding: '10dp'
    spacing: '10dp'

    Button:
        text: 'Frekvencia, f (Hz)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1    
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Kapacitás, C (nF)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Feszültség átv., Uki/Ube'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1

    Button:
        text: 'Fázistolás, ki-be (fok)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1

    Button:
        text: 'Határfrekvencia, fh (Hz)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1


<CR_GridL>:
    cols: 2
    padding: '10dp'
    spacing: '10dp'

    Button:
        text: 'Frekvencia, f (Hz)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1    
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Kapacitás, C (nF)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Feszültség átv., Uki/Ube'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1

    Button:
        text: 'Fázistolás, ki-be (fok)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1

    Button:
        text: 'Határfrekvencia, fh (Hz)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1


<R_GridL>:
    cols: 2
    padding: '10dp'
    spacing: '20dp'

    Button:
        text: 'Hossz, l (m)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1    
    Button:
        text: 'Átmérő, d (mm)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Anyag'
        color: 0.5, 0.6, 0.7, 1
    Spinner: 
        text: "Réz"
		font_size: '16sp'
        foreground_color:1,0,0,1	        
        values:'Réz','Alumínium','Arany','Ezüst'
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 0.5, 0.6, 0.7, 1
    TextInput:				
        text: 'ha'		
		font_size: '16sp'
        foreground_color:1,0,0,1


''')

###########################################################################################


class PageLabel(TextInput):
    pass

###########################################################################################


class XL_GridL(GridLayout):

    def xl_button_click(self):
        #  XL calculation
        
        ok = True
        try:
            L = float(self.l_textin.text)   # read value of 'L' from textinput
            if L <= 0:                   # bad value !
                ok = False
                self.l_textin.text = self.l_textin.text + ' ?'  
        except:                              # bad value !
            ok = False
            self.l_textin.text = self.l_textin.text + ' ?'  
        try:
            f = float(self.f_textin.text)   # read  value of 'f' from textinput
            if f <= 0:                  # bad value !
                ok = False
                self.f_textin.text = self.f_textin.text + ' ?'                  
        except:                              # bad value !
            ok = False
            self.f_textin.text = self.f_textin.text + ' ?'  
        if ok:
            xl = 2*pi*f*L/1000         #  XL  in Ohm !!
            self.xl_textin.text = str(xl)   # write  'XL' 
        else:
            self.xl_textin.text = "hiba!!"  


    def l_button_click(self):
        #  L calculation
        
        ok = True
        try:
            xl = float(self.xl_textin.text)   # read value of 'XL' from textinput
            if xl <= 0:                   # bad value !
                ok = False
                self.xl_textin.text = self.xl_textin.text + ' ?'  
        except:                              # bad value !
            ok = False
            self.xl_textin.text = self.xl_textin.text + ' ?'  
        try:
            f = float(self.f_textin.text)   # read  value of 'f' from textinput
            if f <= 0:                  # bad value !
                ok = False
                self.f_textin.text = self.f_textin.text + ' ?'                  
        except:                              # bad value !
            ok = False
            self.f_textin.text = self.f_textin.text + ' ?'  
        if ok:
            L = 1000*xl/(2*pi*f)         #  L  in mH !!
            self.l_textin.text = str(L)   # write  'L' 
        else:
            self.l_textin.text = "hiba!!"  


    def f_button_click(self):
        #  f calculation
        
        ok = True
        try:
            L = float(self.l_textin.text)   # read value of 'L' from textinput
            if L <= 0:                   # bad value !
                ok = False
                self.l_textin.text = self.l_textin.text + ' ?'  
        except:                              # bad value !
            ok = False
            self.l_textin.text = self.l_textin.text + ' ?'  
        try:
            xl = float(self.xl_textin.text)   # read  value of 'XL' from textinput
            if xl <= 0:                  # bad value !
                ok = False
                self.xl_textin.text = self.xl_textin.text + ' ?'                  
        except:                              # bad value !
            ok = False
            self.xl_textin.text = self.xl_textin.text + ' ?'  
        if ok:
            f = 1000*xl/(2*pi*L)      #  f  in Hz !!
            self.f_textin.text = str(f)   # write  'f' 
        else:
            self.f_textin.text = "hiba!!"  



###########################################################################################



class XC_GridL(GridLayout):

    def xc_button_click(self):
        #  XC calculation
        
        ok = True
        try:
            C = float(self.c_textin.text)   # read value of 'C' from textinput
            if C <= 0:                   # bad value !
                ok = False
                self.c_textin.text = self.c_textin.text + ' ?'  
        except:                              # bad value !
            ok = False
            self.c_textin.text = self.c_textin.text + ' ?'  
        try:
            f = float(self.f_textin.text)   # read  value of 'f' from textinput
            if f <= 0:                  # bad value !
                ok = False
                self.f_textin.text = self.f_textin.text + ' ?'                  
        except:                              # bad value !
            ok = False
            self.f_textin.text = self.f_textin.text + ' ?'  
        if ok:
            xc = 1000000000/(2*pi*f*C)        #  XC  in Ohm !!
            self.xc_textin.text = str(xc)   # write  'XC' 
        else:
            self.xc_textin.text = "hiba!!"  


    def c_button_click(self):
        #  C calculation
        
        ok = True
        try:
            xc = float(self.xc_textin.text)   # read value of 'XC' from textinput
            if xc <= 0:                   # bad value !
                ok = False
                self.xc_textin.text = self.xc_textin.text + ' ?'  
        except:                              # bad value !
            ok = False
            self.xc_textin.text = self.xc_textin.text + ' ?'  
        try:
            f = float(self.f_textin.text)   # read  value of 'f' from textinput
            if f <= 0:                  # bad value !
                ok = False
                self.f_textin.text = self.f_textin.text + ' ?'                  
        except:                              # bad value !
            ok = False
            self.f_textin.text = self.f_textin.text + ' ?'  
        if ok:
            C = 1000000000/(2*pi*f*xc)         #  C  in nF !!
            self.c_textin.text = str(C)   # write  'L' 
        else:
            self.c_textin.text = "hiba!!"  


    def f_button_click(self):
        #  f calculation
        
        ok = True
        try:
            C = float(self.c_textin.text)   # read value of 'C' from textinput
            if C <= 0:                   # bad value !
                ok = False
                self.c_textin.text = self.c_textin.text + ' ?'  
        except:                              # bad value !
            ok = False
            self.c_textin.text = self.c_textin.text + ' ?'  
        try:
            xc = float(self.xc_textin.text)   # read  value of 'XC' from textinput
            if xc <= 0:                  # bad value !
                ok = False
                self.xc_textin.text = self.xc_textin.text + ' ?'                  
        except:                              # bad value !
            ok = False
            self.xc_textin.text = self.xc_textin.text + ' ?'  
        if ok:
            f = 1000000000/(2*pi*C*xc)      #  f  in Hz !!
            self.f_textin.text = str(f)   # write  'f' 
        else:
            self.f_textin.text = "hiba!!"  



###########################################################################################



class Fo_GridL(GridLayout):
    pass


class RLC_GridL(GridLayout):
    pass


class R_GridL(GridLayout):
    pass


class RC_GridL(GridLayout):
    pass


class CR_GridL(GridLayout):
    pass

###########################################################################################


class EcalcWidget(TabbedPanel):

    def __init__(self):
        super().__init__()

 
      
class EcalcApp(App):

    def build(self):       
        return EcalcWidget()



if __name__ == '__main__':
    ec= EcalcApp()
    ec.run()


