# Electrotechnical calculations
# XL, XC, Ze 
#  R-L    R-C  L-C circuits
# 2024.02.26. - 2024.03. 10.   KL

# import os
# os.environ['KIVY_NO_CONSOLELOG']='1'

from kivy.config import Config 
Config.set('graphics','width','400')
Config.set('graphics','height','800')
# Config.set('graphics','resizable','0')

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from math import pi
from math import sqrt
from math import atan
from math import log10
from kivy.uix.button import  Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.graphics import Color, Ellipse, Line, Rectangle, Point, GraphicException



Builder.load_string('''

<PageLabel>:				
	font_size: '18sp'
    foreground_color:1,0,0,1
    background_color:1,1,0,1
    multiline: False
    readonly: True   

<MyTextInput>:				
    text: ''		
	font_size: '16sp'
    foreground_color:1,0,0,1
    multiline: False

<MyTextInputRonly>:				
    text: ''		
	font_size: '16sp'
    foreground_color:1,0,0,1
    multiline: False
    background_color:1,1,0,1            
    readonly: True


<Rcircuit_hor>:
    du: self.size[0]/40 if self.size[0]/2 < self.size[1] else self.size[1]/20
    w: 2
    canvas:
        Color:
            rgb: (1, 0, 0)       
        Line:
            points: (0,10*self.du,8*self.du,10*self.du)
            width: self.w
        Line:
            rectangle: (8*self.du,6*self.du,24*self.du,8*self.du)
            width: self.w
        Line:
            points: (32*self.du,10*self.du,self.size[0],10*self.du)
            width: self.w  


<Lcircuit_hor>:
    du: self.size[0]/40 if self.size[0]/2 < self.size[1] else self.size[1]/20
    w: 2
    canvas:
        Color:
            rgb: (1, 0, 0)       
        Line:
            points: (0,10*self.du,8*self.du,10*self.du)
            width: self.w
        Line:
            circle: (11*self.du,10*self.du,3*self.du,90,-90)
            width: self.w
        Line:
            circle: (17*self.du,10*self.du,3*self.du,90,-90)
            width: self.w
        Line:
            circle: (23*self.du,10*self.du,3*self.du,90,-90)
            width: self.w
        Line:
            circle: (29*self.du,10*self.du,3*self.du,90,-90)
            width: self.w            
        Line:
            points: (32*self.du,10*self.du,self.size[0],10*self.du)
            width: self.w 


<Ccircuit_hor>:
    du: self.size[0]/40 if self.size[0]/2 < self.size[1] else self.size[1]/20
    w: 2
    canvas:
        Color:
            rgb: (1, 0, 0)       
        Line:
            points: (0,10*self.du,16*self.du,10*self.du)
            width: self.w
        Line:
            points: (16*self.du,4*self.du,16*self.du,16*self.du)
            width: self.w
        Line:
            points: (22*self.du,4*self.du,22*self.du,16*self.du)
            width: self.w    
        Line:
            points: (22*self.du,10*self.du,self.size[0],10*self.du)
            width: self.w 
   

<MyCircuit>:
	xe: self.size[0]/50
	ye: self.size[1]/50
	on_size: self.circdraw()
       

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
            size_hint: 1, 6/10
            PageLabel:				
                text: 'Soros RLC'	
                size_hint: 1, 1/10
            RLC_GridL:
                size_hint: 1, 7/10
            BoxLayout:
                pos_hint: {'x': 0.2}
                size_hint: 5/10, 2/10
                Rcircuit_hor
                Lcircuit_hor
                Ccircuit_hor  


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
            size_hint: 1, 3/4
            PageLabel:				
                text: 'RC szűrő (aluláteresztő)'	
                size_hint: 1, 1/10
            RC_GridL:
                size_hint: 1, 6/10
            MyCircuit:
                ctyp: 'RC'
                size_hint: 0.5, 3/10


    TabbedPanelItem:
        text: 'CR'
        BoxLayout:   
            orientation: 'vertical'   
            size_hint: 1, 3/4
            PageLabel:				
                text: 'CR szűrő (felüláteresztő)'	
                size_hint: 1, 1/10
            CR_GridL:
                size_hint: 1, 6/10
            MyCircuit:
                ctyp: 'CR'
                size_hint: 0.5, 3/10


    TabbedPanelItem:
        text: 'RL'
        BoxLayout:   
            orientation: 'vertical'   
            size_hint: 1, 3/4
            PageLabel:				
                text: 'RL szűrő (felűláteresztő)'	
                size_hint: 1, 1/10
            RL_GridL:
                size_hint: 1, 6/10
            MyCircuit:
                ctyp: 'RL'
                size_hint: 0.5, 3/10


    TabbedPanelItem:
        text: 'LR'
        BoxLayout:   
            orientation: 'vertical'   
            size_hint: 1, 3/4
            PageLabel:				
                text: 'LR szűrő (aluláteresztő)'	
                size_hint: 1, 1/10
            LR_GridL:
                size_hint: 1, 6/10
            MyCircuit:
                ctyp: 'LR'
                size_hint: 0.5, 3/10


    TabbedPanelItem:
        text: 'bT'
        BoxLayout:   
            orientation: 'vertical'   
            size_hint: 1, 3/4
            PageLabel:				
                text: 'Áthidalt T csillapító'	
                size_hint: 1, 1/10
            BT_GridL:
                size_hint: 1, 5/10
            BridgedTcircuit:
                size_hint: 1/2, 4/10




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
    MyTextInput:	
        id: f_text			 
    Button:
        text: 'Induktivitás, L (mH)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.l_button_click()
    MyTextInput:			
        id: L_text	
    Button:
        text: 'XL (ohm)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.xl_button_click()
    MyTextInput:		
        id: xl_text		


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
    MyTextInput:	
        id: f_text			
    Button:
        text: 'Kapacitás, C (nF)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.c_button_click()
    MyTextInput:	
        id: C_text			
    Button:
        text: 'XC (ohm)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.xc_button_click()
    MyTextInput:	
        id: xc_text			
 

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
    MyTextInput:	
        id: L_text			
    Button:
        text: 'Kapacitás, C (nF)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.c_button_click()
    MyTextInput:	
        id: C_text			
    Button:
        text: 'Rezonancia fr. fo (Hz)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.f_button_click()
    MyTextInput:	
        id: f_text			


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
    MyTextInput:		
        id: f_text		 
    Button:
        text: 'Induktivitás, L (mH)'
        color: 1, 1, 0, 1
    MyTextInput:		
        id: L_text		
    Button:
        text: 'Kapacitás, C (nF)'
        color: 1, 1, 0, 1
    MyTextInput:		
        id: C_text		
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 1, 1, 0, 1
    MyTextInput:		
        id: R_text		
    Button:
        text: 'Impedancia, Ze (ohm)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.ze_button_click()            
    MyTextInputRonly:	
        id: Ze_text          			
    Button:
        text: 'Fázisszög, fi (fok)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.ze_button_click()            
    MyTextInputRonly:	
        id: fi_text          			


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
    MyTextInput:				
        id: f_text  
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 1, 1, 0, 1
    MyTextInput:	
        id: R_text    			
    Button:
        text: 'Kapacitás, C (nF)'
        color: 1, 1, 0, 1
    MyTextInput:	
        id: C_text			
    Button:
        text: 'Feszültség átv., Uki/Ube'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:
        id: tr_text    				
    Button:
        text: 'Fázistolás, ki-be (fok)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:	
        id: fi_text			
    Button:
        text: 'Határfrekvencia, fh (Hz)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:
        id: fh_text   				

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
    MyTextInput:
        id: f_text  				
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 1, 1, 0, 1
    MyTextInput:
        id: R_text				
    Button:
        text: 'Kapacitás, C (nF)'
        color: 1, 1, 0, 1
    MyTextInput:
        id: C_text				
    Button:
        text: 'Feszültség átv., Uki/Ube'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:
        id: tr_text				
    Button:
        text: 'Fázistolás, ki-be (fok)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:
        id: fi_text				
    Button:
        text: 'Határfrekvencia, fh (Hz)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:
        id: fh_text				
   

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
    MyTextInput:	
        id: l_text			   
    Button:
        text: 'Átmérő, d (mm)'
        color: 1, 1, 0, 1
    MyTextInput:	
        id: d_text			
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
    MyTextInputRonly:		
        id: R_text
    

<RL_GridL>:
    l_textin: L_text
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
    MyTextInput:				
        id: f_text  
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 1, 1, 0, 1
    MyTextInput:	
        id: R_text    			
    Button:
        text: 'Induktivitás, L (mH)'
        color: 1, 1, 0, 1
    MyTextInput:	
        id: L_text			
    Button:
        text: 'Feszültség átv., Uki/Ube'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:
        id: tr_text    				
    Button:
        text: 'Fázistolás, ki-be (fok)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:	
        id: fi_text			
    Button:
        text: 'Határfrekvencia, fh (Hz)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:
        id: fh_text   				


<LR_GridL>:
    l_textin: L_text
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
    MyTextInput:				
        id: f_text  
    Button:
        text: 'Ellenállás, R (ohm)'
        color: 1, 1, 0, 1
    MyTextInput:	
        id: R_text    			
    Button:
        text: 'Induktivitás, L (mH)'
        color: 1, 1, 0, 1
    MyTextInput:	
        id: L_text			
    Button:
        text: 'Feszültség átv., Uki/Ube'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:
        id: tr_text    				
    Button:
        text: 'Fázistolás, ki-be (fok)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:	
        id: fi_text			
    Button:
        text: 'Határfrekvencia, fh (Hz)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:
        id: fh_text   				


<BT_GridL>:
    rs_textin: Rs_text
    ro_textin: Ro_text
    rp_textin: Rp_text
    zo_textin: Z0_text 
    ao_textin: a0_text 
    cols: 2
    padding: '10dp'
    spacing: '10dp'

    Button:
        text: 'Ro (ohm)'
        color: 1, 0, 1, 1
    MyTextInput:				
        id: Ro_text  
    Button:
        text: 'Rs (ohm)'
        color: 0, 1, 0, 1
    MyTextInput:	
        id: Rs_text    			
    Button:
        text: 'Rp (ohm)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:	
        id: Rp_text							
    Button:
        text: 'Hullámimpedan. Z0 (ohm)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:	
        id: Z0_text			
    Button:
        text: 'Hullámcsillapítás a0 (dB)'
        color: 0.5, 0.6, 0.7, 1
        on_press: root.tr_button_click()
    MyTextInputRonly:
        id: a0_text   				



<BridgedTcircuit>:
    du: self.size[0]/100 if self.size[0] < self.size[1] else self.size[1]/100
    w: 2
    canvas:
        Color:
            rgb: (1, 0, 0)       
        Line:
            points: (2*self.du,60*self.du,18*self.du,60*self.du)
            width: self.w
        Line:
            points: (42*self.du,60*self.du,58*self.du,60*self.du)
            width: self.w  
        Line:
            points: (82*self.du,60*self.du,98*self.du,60*self.du)
            width: self.w
        Color:
            rgb: (1, 0, 1) 
        Line:
            rectangle: (18*self.du,56*self.du,24*self.du,8*self.du)
            width: self.w
        Line:
            rectangle: (58*self.du,56*self.du,24*self.du,8*self.du)
            width: self.w
        Color:
            rgb: (1, 0, 0)       
        Line:
            points: (12*self.du,60*self.du,12*self.du,76*self.du,38*self.du,76*self.du)
            width: self.w
        Line:
            points: (88*self.du,60*self.du,88*self.du,76*self.du,62*self.du,76*self.du)
            width: self.w       
        Line:
            points: (50*self.du,60*self.du,50*self.du,50*self.du)
            width: self.w           
        Line:
            points: (50*self.du,26*self.du,50*self.du,16*self.du)
            width: self.w           
        Line:
            points: (2*self.du,16*self.du,98*self.du,16*self.du)
            width: self.w
        Color:
            rgb: (0, 1, 0) 
        Line:
            rectangle: (38*self.du,72*self.du,24*self.du,8*self.du)
            width: self.w
        Color:
            rgb: (1, 0, 0) 
        Line:
            rectangle: (46*self.du,26*self.du,8*self.du,24*self.du)
            width: self.w



''')

###########################################################################################

class BridgedTcircuit(RelativeLayout):
    du = NumericProperty(2)	# draw unit
    w = NumericProperty(2)  # width


class PageLabel(TextInput):
    pass


class MyTextInput(TextInput):
    pass

class MyTextInputRonly(TextInput):
    pass

class Rcircuit_hor(RelativeLayout):
    du = NumericProperty(2)	# draw unit
    w = NumericProperty(2)  # width

class Lcircuit_hor(RelativeLayout):
    du = NumericProperty(2)	# draw unit
    w = NumericProperty(2)  # width

class Ccircuit_hor(RelativeLayout):
    du = NumericProperty(2)	# draw unit
    w = NumericProperty(2)  # width   


###########################################################################################

class MyCircuit(RelativeLayout):
    xe = NumericProperty(2)	# x unit
    ye = NumericProperty(2)	# y unit
    ctyp = StringProperty('CR')  # circuit type ->  RC,  CR, 
    
    def __init__(self,**kwargs):
        super(MyCircuit,self).__init__(**kwargs)
        self.circdraw()
		
    def circdraw(self):
        ''' áramkör kirajzoló függvény   '''
        self.canvas.clear()    
        xe = self.xe
        ye = self.ye
        if xe>ye:
            xe=ye
        else:
            ye=xe
        with self.canvas:
            #Color(1, 1, 1)
            #Rectangle(pos=[0,0],size=self.size)
            Color(1, 0, 0)           
            Line(points=[10*xe,16*ye,40*xe,16*ye],width=2)    # alsó vonal
            # felső alkatrész
            if self.ctyp=='RC' or self.ctyp=='RL':                # ellenállás felül
                Line(points=[10*xe,40*ye,16*xe,40*ye],width=2)  # bal kivezetés
                Line(rectangle=(16*xe,38*ye,12*xe,4*ye),width=2)       # R test
                Line(points=[28*xe,40*ye,40*xe,40*ye],width=2)    # jobb kivezetés
            elif self.ctyp=='CR' or self.ctyp=='CL':              # kondi felül
                Line(points=[10*xe,40*ye,20*xe,40*ye],width=2)  # bal kivezetés
                Line(points=[20*xe,43*ye,20*xe,37*ye],width=2)       # C test
                Line(points=[23*xe,43*ye,23*xe,37*ye],width=2)
                Line(points=[23*xe,40*ye,40*xe,40*ye],width=2)    # jobb kivezetés
            elif self.ctyp=='LR' or self.ctyp=='LC':              # tekercs felül    
                Line(points=[10*xe,40*ye,14*xe,40*ye],width=2)  # bal kivezetés
                Line(circle=(16*xe,40*ye,2*xe,90,-90),width=2)       # L test
                Line(circle=(20*xe,40*ye,2*xe,90,-90),width=2)
                Line(circle=(24*xe,40*ye,2*xe,90,-90),width=2)
                Line(circle=(28*xe,40*ye,2*xe,90,-90),width=2)
                Line(points=[30*xe,40*ye,40*xe,40*ye],width=2)    # jobb kivezetés 
                      
             # kimeneti alkatrész
            if self.ctyp=='CR' or self.ctyp=='LR':                # ellenállás a kimeneten
                Line(points=[34*xe,40*ye,34*xe,34*ye],width=2)  # felső kivezetés  
                Line(rectangle=(32*xe,22*ye,4*xe,12*ye),width=2)       # R test
                Line(points=[34*xe,22*ye,34*xe,16*ye],width=2)  # alsó kivezetés 
            elif self.ctyp=='RC' or self.ctyp=='LC':              # kondi a kimeneten
                Line(points=[34*xe,40*ye,34*xe,30*ye],width=2)  # felső kivezetés
                Line(points=[31*xe,30*ye,37*xe,30*ye],width=2)       # C test
                Line(points=[31*xe,27*ye,37*xe,27*ye],width=2)
                Line(points=[34*xe,27*ye,34*xe,16*ye],width=2)    # alsó kivezetés
            elif self.ctyp=='RL' or self.ctyp=='CL':              # tekercs a kimeneten
                Line(points=[34*xe,40*ye,34*xe,36*ye],width=2)  # felső kivezetés
                Line(circle=(34*xe,34*ye,2*xe,0,180),width=2)       # L test
                Line(circle=(34*xe,30*ye,2*xe,0,180),width=2)
                Line(circle=(34*xe,26*ye,2*xe,0,180),width=2)
                Line(circle=(34*xe,22*ye,2*xe,0,180),width=2)
                Line(points=[34*xe,20*ye,34*xe,16*ye],width=2)    # alsó kivezetés    
      
 ###########################################################################################

class BT_GridL(GridLayout):  

    def tr_button_click(self):
            #  Rp, Z0, a0 calculation  
        ok = True
        try:
            R0 = float(self.ro_textin.text)   # read value of 'R0' from textinput
            if R0 <= 0:                   # bad value !
                ok = False
                self.ro_textin.text = self.ro_textin.text + ' ?'  
        except:                              # bad value !
            ok = False
            self.ro_textin.text = self.ro_textin.text + ' ?'  
        try:
            Rs = float(self.rs_textin.text)   # read  value of 'Rs' from textinput
            if Rs <= 0:                  # bad value !
                ok = False
                self.rs_textin.text = self.rs_textin.text + ' ?'                  
        except:                              # bad value !
            ok = False
            self.rs_textin.text = self.rs_textin.text + ' ?'  
        if ok:                          #  all input data are ok
            Rp = R0*R0/Rs       #  Rp  in  Ohm !!
            Z0 = R0
            a0 = 20*log10(Rs/R0 +1)

            self.rp_textin.text = str(Rp)   # 'Rp' write
            self.zo_textin.text = str(Z0)   # 'Z0' write
            self.ao_textin.text = str(a0)   # 'a0' write

        else:
            self.rp_textin.text = "hiba!!"     
            self.zo_textin.text = "hiba!!"  
            self.ao_textin.text = "hiba!!" 


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
                Tr = 0
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

class RL_GridL(GridLayout):

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
            L = float(self.l_textin.text)   # read  'L' 
            if L <= 0:
                ok = False
                self.l_textin.text = self.l_textin.text + ' ?'   # wrong value !
        except:
            ok = False
            self.l_textin.text = self.l_textin.text + ' ?'   # wrong value !                      
        if ok:                          #  all input data are ok
            if f==0:
                Tr = 0
                fi = 0
            else:
                xl = 2*pi*f*L/1000        #  XL  in  Ohm !!
                Ze = sqrt(R**2+xl**2)
                Tr = xl/Ze                  # Uout / Uin
                fi = 180*atan(R/xl)/pi

            fh=1000*R/(2*pi*L)

            self.tr_textin.text = str(Tr)   # 'Tr' write
            self.fi_textin.text = str(fi)   # 'fi' write
            self.fh_textin.text = str(fh)   # 'fh' write

        else:
            self.tr_textin.text = "hiba!!"     
            self.fi_textin.text = "hiba!!"  
            self.fh_textin.text = "hiba!!" 



###########################################################################################

class LR_GridL(GridLayout):
    
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
            L = float(self.l_textin.text)   # read  'L' 
            if L <= 0:
                ok = False
                self.l_textin.text = self.l_textin.text + ' ?'   # wrong value !
        except:
            ok = False
            self.l_textin.text = self.l_textin.text + ' ?'   # wrong value !                      
        if ok:                          #  all input data are ok
            if f==0:
                Tr = 1
                fi = 0
            else:
                xl = 2*pi*f*L/1000        #  XL  in  Ohm !!
                Ze = sqrt(R**2+xl**2)
                Tr = R/Ze                  # Uout / Uin
                fi = -180*atan(xl/R)/pi

            fh=1000*R/(2*pi*L)

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


