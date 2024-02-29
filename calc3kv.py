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
        on_press: root.f_button_click()
    TextInput:	
        id: f_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Kapacitás, C (nF)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.c_button_click()
    TextInput:	
        id: C_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'XC (ohm)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.xc_button_click()
    TextInput:	
        id: xc_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1


<Fo_GridL>:
    l_textin: L_text
    c_textin: C_text
    f_textin: f_text
    cols: 2
    padding: '10dp'
    spacing: '20dp'
        
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
        text: 'Kapacitás, C (nF)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.c_button_click()
    TextInput:	
        id: C_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Rezonancia fr. fo (Hz)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.f_button_click()
    TextInput:	
        id: f_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1



<RLC_GridL>:
    l_textin: L_text
    c_textin: C_text
    r_textin: R_text
    f_textin: f_text
    ze_textin: Ze_text
    fi_textin: fi_text                
    cols: 2
    padding: '10dp'
    spacing: '10dp'

    Button:
        text: 'Frekvencia, f (Hz)'
        color: 1, 1, 0, 1
    TextInput:		
        id: f_text		
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1    
    Button:
        text: 'Induktivitás, L (mH)'
        color: 1, 1, 0, 1
    TextInput:		
        id: L_text		
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Kapacitás, C (nF)'
        color: 1, 1, 0, 1
    TextInput:		
        id: C_text		
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 1, 1, 0, 1
    TextInput:		
        id: R_text		
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Impedancia, Ze (ohm)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.ze_button_click()            
    TextInput:	
        id: Ze_text          			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
        background_color:1,1,0,1            
        readonly: True
    Button:
        text: 'Fázisszög, fi (fok)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.ze_button_click()            
    TextInput:	
        id: fi_text          			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
        background_color:1,1,0,1            
        readonly: True


<RC_GridL>:
    c_textin: C_text
    r_textin: R_text
    f_textin: f_text
    tr_textin: tr_text
    fi_textin: fi_text 
    fh_textin: fh_text 
    cols: 2
    padding: '10dp'
    spacing: '10dp'

    Button:
        text: 'Frekvencia, f (Hz)'
        color: 1, 1, 0, 1
    TextInput:				
        id: f_text
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1    
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 1, 1, 0, 1
    TextInput:	
        id: R_text    			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Kapacitás, C (nF)'
        color: 1, 1, 0, 1
    TextInput:	
        id: C_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Feszültség átv., Uki/Ube'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    TextInput:
        id: tr_text    				
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
        background_color:1,1,0,1            
        readonly: True
    Button:
        text: 'Fázistolás, ki-be (fok)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    TextInput:	
        id: fi_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
        background_color:1,1,0,1            
        readonly: True
    Button:
        text: 'Határfrekvencia, fh (Hz)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    TextInput:
        id: fh_text   				
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
        background_color:1,1,0,1            
        readonly: True

<CR_GridL>:
    c_textin: C_text
    r_textin: R_text
    f_textin: f_text
    tr_textin: tr_text
    fi_textin: fi_text 
    fh_textin: fh_text 
    cols: 2
    padding: '10dp'
    spacing: '10dp'

    Button:
        text: 'Frekvencia, f (Hz)'
        color: 1, 1, 0, 1
    TextInput:
        id: f_text  				
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1    
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 1, 1, 0, 1
    TextInput:
        id: R_text				
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Kapacitás, C (nF)'
        color: 1, 1, 0, 1
    TextInput:
        id: C_text				
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Feszültség átv., Uki/Ube'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    TextInput:
        id: tr_text				
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
        background_color:1,1,0,1            
        readonly: True
    Button:
        text: 'Fázistolás, ki-be (fok)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    TextInput:
        id: fi_text				
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
        background_color:1,1,0,1            
        readonly: True
    Button:
        text: 'Határfrekvencia, fh (Hz)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    TextInput:
        id: fh_text				
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
        background_color:1,1,0,1            
        readonly: True


<R_GridL>:
    l_textin: l_text
    d_textin: d_text
    mat_spin: mat_spin
    r_textin: R_text
    cols: 2
    padding: '10dp'
    spacing: '20dp'

    Button:
        text: 'Hossz, l (m)'
        color: 1, 1, 0, 1
    TextInput:	
        id: l_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1    
    Button:
        text: 'Átmérő, d (mm)'
        color: 1, 1, 0, 1
    TextInput:	
        id: d_text			
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
    Button:
        text: 'Anyag'
        color: 1, 1, 0, 1
    Spinner: 
        id: mat_spin
        text: "Réz"
		font_size: '16sp'
        foreground_color:1,0,0,1	        
        values:'Réz','Alumínium','Arany','Ezüst'
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.r_button_click()
    TextInput:		
        id: R_text
        text: ''		
		font_size: '16sp'
        foreground_color:1,0,0,1
        background_color:1,1,0,1            
        readonly: True


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
            self.c_textin.text = str(C)   # write  'C' 
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

    def l_button_click(self):
        #  L calculation
        
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
            L = 1000000000000/(4*pi*pi*f*f*C)        #  L  in mH !!
            self.l_textin.text = str(L)   # write  'L' 
        else:
            self.l_textin.text = "hiba!!"  


    def c_button_click(self):
        #  C calculation
        
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
            C = 1000000000000/(4*pi*pi*f*f*L)         #  C  in nF !!
            self.c_textin.text = str(C)   # write  'C' 
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
            L = float(self.l_textin.text)   # read  value of 'L' from textinput
            if L <= 0:                  # bad value !
                ok = False
                self.l_textin.text = self.l_textin.text + ' ?'                  
        except:                              # bad value !
            ok = False
            self.l_textin.text = self.l_textin.text + ' ?'  
        if ok:
            f = 1000000/(2*pi*sqrt(C*L))      #  f  in Hz !!
            self.f_textin.text = str(f)   # write  'f' 
        else:
            self.f_textin.text = "hiba!!"  


###########################################################################################

class RLC_GridL(GridLayout):
    
    def ze_button_click(self):
        ok = True  
        try:
            f = float(self.f_textin.text)   # read 'f' 
            if f <= 0:
                ok = False
                self.f_textin.text = self.f_textin.text + ' ?'   # wrong value !               
        except:
            ok = False
            self.f_textin.text = self.f_textin.text + ' ?'   # wrong value !
        try:
            L = float(self.l_textin.text)   # read  'L'
            if L < 0:
                ok = False
                self.l_textin.text = self.l_textin.text + ' ?'   # wrong value !
        except:
            ok = False
            self.l_textin.text = self.l_textin.text + ' ?'   # wrong value ! 
        try:
            C = float(self.c_textin.text)   # read  'C' 
            if C < 0:
                ok = False
                self.c_textin.text = self.c_textin.text + ' ?'   # wrong value !
        except:
            ok = False
            self.c_textin.text = self.c_textin.text + ' ?'   # wrong value !
        try:
            R = float(self.r_textin.text)   # read 'R' beolvasása szövegmezőből
            if R < 0:
                ok = False
                self.r_textin.text = self.r_textin.text + ' ?'   #  wrong value !
        except:
            ok = False
            self.r_textin.text = self.r_textin.text + ' ?'   #  wrong value !                       
        if ok:                          #  all input data are ok
            if L == 0:
                xl = 0
            else:
                xl = 2*pi*f*L/1000         #  XL  in Ohm !!
            if C == 0:
                xc = 0
            else:
                xc = 1000000000/(2*pi*f*C)        #  XC   in Ohm !!
            Ze = sqrt(R**2+(xl-xc)**2)
            if R == 0:
                if xl>xc:
                    fi = 90
                elif xc>xl:
                    fi = -90
                else:
                    fi = ""
            else:
                fi = 180*atan((xl-xc)/R)/pi

            self.ze_textin.text = str(Ze)   # 'Ze' kiírása szövegmezőbe
            self.fi_textin.text = str(fi)   # 'fi' kiírása szövegmezőbe

        else:
            self.ze_textin.text = "hiba!!"     
            self.fi_textin.text = "hiba!!"     

###########################################################################################

class R_GridL(GridLayout):

    def r_button_click(self):
        materials = {'Réz':0.0175,'Alumínium':0.028,'Arany':0.023,'Ezüst':0.016 }
        ok = True 
        try:
            l = float(self.l_textin.text)   # read  'l'  (wire length)
            if l <= 0:
                ok = False
                self.l_textin.text = self.l_textin.text + ' ?'   # wrong value !
        except:
            ok = False
            self.l_textin.text = self.l_textin.text + ' ?'   # wrong value ! 
        try:
            d = float(self.d_textin.text)   # read  'd' (diameter)
            if d <= 0:
                ok = False
                self.d_textin.text = self.d_textin.text + ' ?'   # wrong value !
        except:
            ok = False
            self.d_textin.text = self.d_textin.text + ' ?'   # wrong value !
        if ok:                              #  all input data are ok
            mat = self.mat_spin.text             # read material
            ro = materials[mat]
            A = d*d*pi/4                    # cross-section  mm2
            R = ro*l/A                      #  resistance   in  ohm !!
            self.r_textin.text = str(R)   # 'R' write
        else:
            self.r_textin.text = "hiba!!"                           
                                 

###########################################################################################

class RC_GridL(GridLayout):

    def tr_button_click(self):
        ok = True 
        try:
            f = float(self.f_textin.text)   # read 'f' 
            if f < 0:
                ok = False
                self.f_textin.text = self.f_textin.text + ' ?'   # wrong value !               
        except:
            ok = False
            self.f_textin.text = self.f_textin.text + ' ?'   # wrong value !
        try:
            R = float(self.r_textin.text)   # read  'R'
            if R <= 0:
                ok = False
                self.r_textin.text = self.r_textin.text + ' ?'   # wrong value !
        except:
            ok = False
            self.r_textin.text = self.r_textin.text + ' ?'   # wrong value ! 
        try:
            C = float(self.c_textin.text)   # read  'C' 
            if C <= 0:
                ok = False
                self.c_textin.text = self.c_textin.text + ' ?'   # wrong value !
        except:
            ok = False
            self.c_textin.text = self.c_textin.text + ' ?'   # wrong value !                      
        if ok:                          #  all input data are ok
            if f==0:
                Tr = 1
                fi = 0
            else:
                xc = 1000000000/(2*pi*f*C)        #  XC  in  Ohm !!
                Ze = sqrt(R**2+xc**2)
                Tr = xc/Ze                  # Uout / Uin
                fi = -180*atan(R/xc)/pi

            fh=1000000000/(2*pi*R*C)

            self.tr_textin.text = str(Tr)   # 'Tr' write
            self.fi_textin.text = str(fi)   # 'fi' write
            self.fh_textin.text = str(fh)   # 'fh' write

        else:
            self.tr_textin.text = "hiba!!"     
            self.fi_textin.text = "hiba!!"  
            self.fh_textin.text = "hiba!!" 


###########################################################################################

class CR_GridL(GridLayout):

    def tr_button_click(self):
        ok = True 
        try:
            f = float(self.f_textin.text)   # read 'f' 
            if f < 0:
                ok = False
                self.f_textin.text = self.f_textin.text + ' ?'   # wrong value !               
        except:
            ok = False
            self.f_textin.text = self.f_textin.text + ' ?'   # wrong value !
        try:
            R = float(self.r_textin.text)   # read  'R'
            if R <= 0:
                ok = False
                self.r_textin.text = self.r_textin.text + ' ?'   # wrong value !
        except:
            ok = False
            self.r_textin.text = self.r_textin.text + ' ?'   # wrong value ! 
        try:
            C = float(self.c_textin.text)   # read  'C' 
            if C <= 0:
                ok = False
                self.c_textin.text = self.c_textin.text + ' ?'   # wrong value !
        except:
            ok = False
            self.c_textin.text = self.c_textin.text + ' ?'   # wrong value !                      
        if ok:                          #  all input data are ok
            if f==0:
                Tr = 1
                fi = 0
            else:
                xc = 1000000000/(2*pi*f*C)        #  XC  in  Ohm !!
                Ze = sqrt(R**2+xc**2)
                Tr = R/Ze                   # Uout / Uin
                fi = 180*atan(xc/R)/pi
              
            fh=1000000000/(2*pi*R*C)
            self.tr_textin.text = str(Tr)   # 'Tr' write
            self.fi_textin.text = str(fi)   # 'fi' write
            self.fh_textin.text = str(fh)   # 'fh' write

        else:
            self.tr_textin.text = "hiba!!"     
            self.fi_textin.text = "hiba!!"  
            self.fh_textin.text = "hiba!!" 

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


