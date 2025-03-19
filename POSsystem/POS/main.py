from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'dock')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
import kivy.properties
kivy.require('2.3.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from functools import partial
from kivy.metrics import dp
from kivy.graphics import Rectangle, Color
from kivy.uix.slider import Slider
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
Window.maximize()

import sqlite3
import databases
import math
import printer
from datetime import datetime
from datetime import time
import json
from escpos.printer import Usb
#Kv File

Builder.load_file("Screens.kv")
Builder.load_file("RV.kv")
Builder.load_file("Layouts.kv")

#usb = Usb(0x0FE6, 0x811E, in_ep=0x81, out_ep=0x02)
usb = 1
"""
Layout Function for background colors
with self.(WDIGET).canvas.before:
    Color(rgba=(2, 1, 1, 1))
    self.bg = Rectangle(pos=self.pos, size=self.size)
self.(WDIGET).bind(pos=self.update_bg)
self.(WDIGET).bind(size=self.update_bg)

def update_bg(self, *args):
    self.bg.pos = self.(WDIGET).pos
    self.bg.size = self.(WDIGET).size
"""
#List of items

#Screens
class AppetizersScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(AppetizersScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("appetizer"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
      

    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"
        
class BeefScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(BeefScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("beef"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"

class FavoriteScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(FavoriteScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("favorite"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))
    
    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"

class ChickenScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ChickenScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("chicken"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))
 

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"

class VegetableScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(VegetableScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("vegetable"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))
                  
    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"
        
class CombosScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CombosScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("combos"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"
        
class EggFooScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(EggFooScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("egg foo yong"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"
        
class NoodlesScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(NoodlesScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("noodle"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i)) 

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"
        
class PorkScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PorkScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("pork"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"
        
class RiceScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RiceScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("rice"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"
        
class SeafoodScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SeafoodScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("seafood"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"
        
class SoupScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SoupScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("soup"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"
        
class CurryScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CurryScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("curry"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i)) 

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"
        
class TeriyakiScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TeriyakiScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("teriyaki"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"

class MenuItemsScreen(Screen):
    grid = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(MenuItemsScreen, self).__init__(**kwargs)
        con = sqlite3.connect(f'..\\POSsystem\\Default Databases\\MenuTitles.db')
        cur = con.cursor()
        self.List = list(cur.execute("SELECT * FROM Titles"))
        con.close()
        for i in self.List:
            btn = Button(text = i[0], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release = (self.switch))
        sauceBtn = Button(text = 'Sauce', size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        discountBtn = Button(text = 'Cash Discount', size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(sauceBtn)
        sauceBtn.bind(on_release = (self.sauce))
        self.grid.add_widget(discountBtn)
        discountBtn.bind(on_release = (self.discount))

    def switch(self, instance):
        self.manager.transition = SlideTransition(direction = 'left')
        self.manager.current = instance.text

    def discount(self, *args):
        counter = 0
        for i in recycle_view.data:
            if "Cash Discount" in i.values():
                return
            counter += 1
        recycle_view.data.extend([{'QTY' : f"1", 'NAME' : f"Cash Discount", 'Price' : f"10%", "NOTES": ""}])
        Total().Update()       
        Total().Calculate() 

    def sauce(self, *args):
        PopUpClass().Confirmation([[0, "['Meme']", "Sauce", 2.00]])

class DrinksScreen(Screen):
    grid = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DrinksScreen, self).__init__(**kwargs)
        backBtn = Button(text = "< Back", size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
        self.grid.add_widget(backBtn)
        backBtn.bind(on_release = (self.BackClicked))

        for i in Items().Item("drinks"):
            btn = Button(text = i[2], size = (164.5, 100), size_hint = (None, None), text_size = (80, None))
            self.grid.add_widget(btn)
            btn.bind(on_release =  partial(self.Clicked, i))

    def Clicked(self, *args):
        PopUpClass().Confirmation(args)
        
    def BackClicked(self, *args):
        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = "MainMenu"

#Layouts
class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)  
        self.add_widget(CustomAmountDisplay())
        self.add_widget(MenuWindows())
        self.add_widget(ItemsLayout())

class CustomAmountDisplay(BoxLayout):
    def __init__(self, **kwargs):
        self.CustomList  = []
        super(CustomAmountDisplay, self).__init__(**kwargs)
        self.Layout = GridLayout(cols = 1)
        self.CustomNumber = Label(font_size = 25, color = 'black', text = "$0.00" , size = (600, 50), size_hint = (None, None), valign = "middle", halign = "center")
        self.Name = TextInput(text = 'Custom...', font_size = 25, size = (600, 50), size_hint = (None, None))
        self.Name.bind(focus = self.on_focus)
        self.Layout.add_widget(self.CustomNumber)
        self.Layout.add_widget(self.Name)
        self.add_widget(self.Layout)
        self.CustomAmountPads = StackLayout(orientation = 'lr-tb', size = (600, 300), size_hint = (None, None))
        Add = Button(text = "Add" , size = (200, 100), size_hint = (None, None))
        Clear = Button(text = "C" , size = (200, 100), size_hint = (None, None))
        Back = Button(text = "<" , size = (200, 100), size_hint = (None, None))
        for i in range(1, 10):
            btn = Button(text = str(i), size = (200, 100), size_hint = (None, None))
            self.CustomAmountPads.add_widget(btn)
            btn.bind(on_release = (self.NumberPressed))
        Zero = Button(text = "0" , size = (200, 100), size_hint = (None, None))
        self.CustomAmountPads.add_widget(Back)
        self.CustomAmountPads.add_widget(Zero)
        self.CustomAmountPads.add_widget(Clear)
        self.CustomAmountPads.add_widget(Label( size = (200, 100), size_hint = (None, None)))
        self.CustomAmountPads.add_widget(Add)
        Back.bind(on_release = (self.NumberDelete))
        Zero.bind(on_release = (self.NumberPressed))
        Clear.bind(on_release = (self.ClearNumber))
        Add.bind(on_release = (self.CustomAddition))
        self.Layout.add_widget(self.CustomAmountPads)

        self.TDetails = GridLayout(cols = 2, rows = 1, size = (600, 50), size_hint =(None, None))
        global databasename
        databasename = Label(text = '', color = 'black')

        self.Tickets = GridLayout(cols = 2, rows = 1, size = (600, 50), size_hint =(None, None))
        self.Ticketwindow = Button(text = "Tickets")
        self.Transactions = Button(text = "Transactions")
        self.Ticketwindow.bind(on_release = self.TicketsTab)
        self.Transactions.bind(on_release = self.TransactionsTab)


        self.TDetails.add_widget(databasename)
        self.Tickets.add_widget(self.Ticketwindow)
        self.Tickets.add_widget(self.Transactions)


        global databaseid
        databaseid = Label(text = '')
        self.add_widget(databaseid)
        self.add_widget(self.TDetails)
        self.add_widget(self.Tickets)

    def on_focus(self, instance, value):
        if value:
            if self.Name.text and self.Name.text != "Custom...":
                return
            else:
                self.Name.text = ''
        else:
            if self.Name.text:
                return
            else:
                self.Name.text = 'Custom...'


    def NumberPressed(self, instance):
        self.CustomList.append(instance.text)
        if len(self.CustomList) == 1:
            self.CustomNumber.text = ('$0.0' + self.CustomList[0])
        elif len(self.CustomList) == 2:
            self.CustomNumber.text = ('$0.' + self.CustomList[0] + self.CustomList[1])
        else:
            self.CustomNumber.text = ('$' + ''.join(self.CustomList[:-2]) + '.' + ''.join(self.CustomList[-2:]))

    def NumberDelete(self, instance):
        self.CustomList = self.CustomList[:-1]
        if len(self.CustomList) == 0:
            self.CustomNumber.text = '$0.00'
        elif len(self.CustomList) == 1:
            self.CustomNumber.text = ('$0.0' + self.CustomList[0])
        elif len(self.CustomList) == 2:
            self.CustomNumber.text = ('$0.' + self.CustomList[0] + self.CustomList[1])
        else:
            self.CustomNumber.text = ('$' + ''.join(self.CustomList[:-2]) + '.' + ''.join(self.CustomList[-2:]))

    def CustomAddition(self, instance):
        if self.CustomNumber.text == '$0.00':
            return
        else:
            if self.Name.text == '' or self.Name.text == 'Custom...':
                recycle_view.data.extend([{'QTY' : "1", 'NAME' : f"Custom", 'Price' : f"{self.CustomNumber.text[1:]}", 'NOTES': ""}])
            else:
                recycle_view.data.extend([{'QTY' : "1", 'NAME' : f"{self.Name.text}", 'Price' : f"{self.CustomNumber.text[1:]}", 'NOTES': ""}])
        self.ClearNumber(instance)
        Total().Calculate()

    def ClearNumber(self, instance):
        self.CustomList.clear()
        self.Name.text = 'Custom...'
        self.CustomNumber.text = '$0.00'

    def TicketsTab(self, instance):
        PopUpTicketWindow().Window()

    def TransactionsTab(self, instance):
        PopUpTransactions().Window()

    
class MenuWindows(BoxLayout):
    def __init__(self, **kwargs):
        super(MenuWindows, self).__init__(**kwargs)  
        self.Menu = ScreenManager(transition= NoTransition())
        search = Button(text = "search", height = 50, width = 658, size_hint_x = None, size_hint_y = None)
        search.bind(on_release = self.Clicked)
        clockoutbtn = Button(text = "Sales", height = 50, width = 658, size_hint_x = None, size_hint_y = None)
        self.add_widget(search)
        self.add_widget(self.Menu)
        self.add_widget(clockoutbtn)
        clockoutbtn.bind(on_release = self.Clockout)
        
        self.Menu.add_widget(MenuItemsScreen(name = "MainMenu"))
        self.Menu.add_widget(AppetizersScreen(name ="Appetizers"))
        self.Menu.add_widget(BeefScreen(name ="Beef"))
        self.Menu.add_widget(FavoriteScreen(name ="Favorite"))
        self.Menu.add_widget(ChickenScreen(name ="Chicken"))
        self.Menu.add_widget(VegetableScreen(name ="Vegetable"))
        self.Menu.add_widget(CombosScreen(name ="Combos"))
        self.Menu.add_widget(EggFooScreen(name ="Egg Foo Yong"))
        self.Menu.add_widget(RiceScreen(name ="Rice"))
        self.Menu.add_widget(NoodlesScreen(name ="Noodles"))
        self.Menu.add_widget(PorkScreen(name ="Pork"))
        self.Menu.add_widget(SeafoodScreen(name ="Seafood"))
        self.Menu.add_widget(SoupScreen(name ="Soup"))
        self.Menu.add_widget(CurryScreen(name ="Curry"))
        self.Menu.add_widget(TeriyakiScreen(name ="Teriyaki"))
        self.Menu.add_widget(DrinksScreen(name ="Drinks"))
    
    def Clicked(self, *args):
        PopUpSearch().Search()

    def Clockout(self, *args):
        ReportPopUp().Display()

class ItemsLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ItemsLayout, self).__init__(**kwargs)  
        global recycle_view
        #Recycleview
        recycle_box_layout = RecycleBoxLayout(size=(660, 1680), size_hint=(1, None), orientation='vertical')
        recycle_box_layout.bind(minimum_height=recycle_box_layout.setter("height"))
        recycle_view = RecycleView()
        recycle_view.add_widget(recycle_box_layout)
        recycle_view.viewclass = ItemsClass

        global Notesinput
        Notesinput = TextInput(text =  "Notes...", height = 32, size_hint_y = None)
        Notesinput.bind(focus = self.on_focus)

        global clearBtn
        clearBtn = Button(text = "Clear Items", height = 50, size_hint_y = None)
        clearBtn.bind(on_release = self.clearall)
        self.add_widget(clearBtn)
        self.add_widget(Notesinput)
        self.add_widget(recycle_view)

        
        #SendLayout = BoxLayout(orientation = 'vertical', size = (660, 50), size_hint =(None, None))
        SubTotalBox = BoxLayout(orientation = 'horizontal',size = (660, 50), size_hint =(None, None))
        #self.add_widget(SendLayout)

        global SubTotalVar
        global FeesVar
        global GSTVar
        global TotalVar
        SubTotalVar = Label(text = '$0.00', color = 'black')
        SubTotalBox.add_widget(Label(text = 'Subtotal', color = 'black'))
        SubTotalBox.add_widget(SubTotalVar)


        FeesVar = Label(text = '$0.00', color = 'black')
        FeesBox = BoxLayout(orientation = 'horizontal',size = (660, 50), size_hint =(None, None))
        FeesBox.add_widget(Label(text = 'Discount', color = 'black'))
        FeesBox.add_widget(FeesVar)


        GSTVar = Label(text = '$0.00', color = 'black')
        GSTBox = BoxLayout(orientation = 'horizontal',size = (660, 50), size_hint =(None, None))
        GSTBox.add_widget(Label(text = 'GST/PST', color = 'black'))
        GSTBox.add_widget(GSTVar)


        TotalVar = Label(text = '$0.00', color = 'black')
        TotalBox = BoxLayout(orientation = 'horizontal',size = (660, 50), size_hint =(None, None))
        TotalBox.add_widget(Label(text = 'Total', color = 'black'))
        TotalBox.add_widget(TotalVar)

        self.Send = BoxLayout(orientation = 'horizontal',size = (660, 50), size_hint =(None, None))


        SaveButton = Button(text = 'Save')
        SaveButton.bind(on_release = (self.save))
        self.Send.add_widget(SaveButton)
        PayButton = Button(text = 'Pay')
        PayButton.bind(on_release = (self.pay))
        self.Send.add_widget(PayButton)


        self.Line = BoxLayout(size = (660, 25), size_hint =(None, None))

        self.add_widget(SubTotalBox)
        self.add_widget(GSTBox)
        self.add_widget(FeesBox)
        self.add_widget(TotalBox)
        self.add_widget(self.Send)

    def on_focus(self, instance, value):
        if value:
            if Notesinput.text and Notesinput.text != "Notes...":
                return
            else:
                Notesinput.text = ''
        else:
            if Notesinput.text:
                return
            else:
                Notesinput.text = "Notes..."

    def clearall(self, *args):
        Notesinput.text = "Notes..."
        if recycle_view.data:
            recycle_view.data.clear()
            Total().Update()
            Total().Calculate()

    def save(self, *args):
        if recycle_view.data:

            PopUpTicket(False).confirmation()
            
            Total().Calculate()
        else:
            return

    def pay(self, *args):
        if recycle_view.data:
            if float(TotalVar.text[1:]) <= 0:
                PopUpPay(TotalVar.text, "default", "meme").Initialize()

            else:
                PopUpPay(TotalVar.text, "default", "meme").Initialize()
        else:
            return

#Recycleview
class ItemsClass(BoxLayout):
    QTY = StringProperty()
    NAME = StringProperty()
    Price = StringProperty()
    NOTES = StringProperty()

    def Edit(self, *Item):
        layout = GridLayout(cols = 1)
        if self.NOTES:
            notes = self.NOTES
        else:
            notes = "Notes..."
        self.input = TextInput(text =  notes, height = 32, size_hint_y = None)
        self.input.bind(focus = self.on_focus)
        Incrementbuttons = GridLayout(cols = 4, rows = 1, size = (300, 50), size_hint = (None, None))
        confirmbuttons = GridLayout(cols = 3, rows = 1)
        title = Label(text='Quantity', color = 'black', font_size = 25)
        placeholder = Label()
        placeholder3 = Label(width = 10)

        increase = Button(text = "+")
        decrease = Button(text = "-")
        self.Quantity = Label(text = self.QTY, color = 'black', font_size = 20)
        Incrementbuttons.add_widget(placeholder3)
        Incrementbuttons.add_widget(decrease)
        Incrementbuttons.add_widget(self.Quantity)
        Incrementbuttons.add_widget(increase)

        cancel = Button(text = "cancel", height = 50, size_hint_y = None)
        add = Button(text = "done", height = 50, size_hint_y = None)
        delete = Button(text = "delete", height = 50, size_hint_y = None)

        confirmbuttons.add_widget(cancel)
        confirmbuttons.add_widget(delete)
        confirmbuttons.add_widget(add)
        layout.add_widget(title)
        layout.add_widget(Incrementbuttons)
        layout.add_widget(Label(height = 15, size_hint_y = None))
        layout.add_widget(self.input)
        layout.add_widget(Label(height = 15, size_hint_y = None))
        layout.add_widget(confirmbuttons)

        self.popup = Popup(title=str(self.NAME), content=layout, size_hint=(None, None), size=(400, 350), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey', pos_hint={'righ': 1, 'top': 0.87})
        self.popup.open()
        cancel.bind(on_release = self.popup.dismiss)
        increase.bind(on_release = lambda *args: self.Increment())
        decrease.bind(on_release = lambda *args: self.Decrement())
        delete.bind(on_release = lambda *args: self.DeleteItem())
        add.bind(on_release = lambda *args: self.add())

    def on_focus(self, instance, value):
        if value:
            if self.input.text and self.input.text != "Notes...":
                return
            else:
                self.input.text = ''
        else:
            if self.input.text:
                return
            else:
                self.input.text = "Notes..."
            
    def Increment(self):
        self.Quantity.text = str(int(self.Quantity.text) + 1)
        if self.Quantity.text == '0':
            self.Quantity.text = str(int(self.Quantity.text) + 1)

    def Decrement(self):
        self.Quantity.text = str(int(self.Quantity.text) - 1)
        if self.Quantity.text == '0':
            self.Quantity.text = str(int(self.Quantity.text) - 1)

    def add(self):
        if self.NAME == "Cash Discount":
            return
        notes = ''
        if self.input.text and self.input.text != "Notes...":
            notes = str(self.input.text)
        index = recycle_view.data.index({'QTY' : f"{self.QTY}", 'NAME' : f"{self.NAME}", 'Price' : f"{"%.2f" %float(self.Price)}", "NOTES": f"{self.NOTES}"})
        recycle_view.data[index]['QTY'] = self.Quantity.text
        recycle_view.data[index]['Price'] = str("%.2f" % round(((float(self.Price) / float(self.QTY)) * float(self.Quantity.text)), 2))
        recycle_view.data[index]['NOTES'] = notes
        Total().Update()       
        Total().Calculate()
        self.popup.dismiss()
        
    def DeleteItem(self):
        if self.NAME == "Cash Discount":
            recycle_view.data.remove({'QTY' : f"{self.QTY}", 'NAME' : f"{self.NAME}", 'Price' : f"10%", 'NOTES' : ""})
        else:
            recycle_view.data.remove({'QTY' : f"{self.QTY}", 'NAME' : f"{self.NAME}", 'Price' : f"{"%.2f" % float(self.Price)}", "NOTES": f"{self.NOTES}"})
        Total().Calculate()
        self.popup.dismiss()
      
class ItemsList(BoxLayout):
    NAME = StringProperty()
    ID = StringProperty()
    PRICE = StringProperty()
    WINDOW = ObjectProperty()
    Placeholder = ""
    Placeholder2 = []

    def add(self):
        args = [[self.Placeholder, self.Placeholder, self.NAME, self.PRICE], self.Placeholder2]
        self.WINDOW.dismiss()
        PopUpClass().Confirmation(args)
             
class TicketsList(BoxLayout):
    DATA = ObjectProperty()
    NAME = StringProperty()
    WINDOW = ObjectProperty()
    IDNo = StringProperty()

    def view(self):
        modifier = 0
        confirmbuttons = GridLayout(cols = 4, rows = 1)
        layout = GridLayout(cols = 1, row_force_default=True, row_default_height=40)

        items = Label(text = "Items:", color = 'black', halign = 'left') 
        items.bind(size=items.setter('text_size'))   
        layout.add_widget(items)
        for i in json.loads(self.DATA[2]):
            if i['NOTES']:
                x = Label(text = f"{i['QTY']} x {i['NAME']}\nNotes:{i['NOTES']}", color = 'black', halign = 'left')
            else:
                x = Label(text = f"{i['QTY']} x {i['NAME']}", color = 'black', halign = 'left')
            x.bind(size=x.setter('text_size'))   
            layout.add_widget(x)
            modifier+= 50
        if self.DATA[13] != "Notes...":
            notesstring = Label(text = f"Notes: {self.DATA[13]}", color = 'black', halign = 'left')
            notesstring.bind(size=notesstring.setter('text_size'))
            layout.add_widget(notesstring)
            modifier += 50
        SubString = Label(text = f"SubTotal: ${"%.2f" %self.DATA[9]}", color = 'black', halign = 'left')
        SubString.bind(size=SubString.setter('text_size'))
        TaxesString = Label(text = f"GST: ${"%.2f" %self.DATA[7]}", color = 'black', halign = 'left')
        TaxesString.bind(size=TaxesString.setter('text_size'))
        TotalString = Label(text = f"Total: ${"%.2f" % round((self.DATA[10] + float(self.DATA[6])), 2)}", color = 'black', halign = 'left')
        TotalString.bind(size=TotalString.setter('text_size'))
        layout.add_widget(SubString)
        layout.add_widget(TaxesString)


        if self.DATA[8]:
            DiscountString = Label(text = f"Discount: -${"%.2f" %self.DATA[8]}", color = 'black', halign = 'left')
            DiscountString.bind(size=DiscountString.setter('text_size'))
            layout.add_widget(DiscountString)
            modifier += 50
        layout.add_widget(TotalString)

       
        layout.add_widget(Label(height = 5, size_hint_y = None))
        leave = Button(text = 'Close', height = 40, size_hint_y = None)
        pay = Button(text = 'Pay', height = 40, size_hint_y = None)
        Bill = Button(text = "Print Bill", height = 40, size_hint_y = None)
        Delete = Button(text = "Delete", height = 40, size_hint_y = None)
        Edit = Button(text = "Edit", height = 40, size_hint_y = None)
        confirmbuttons.add_widget(pay)
        confirmbuttons.add_widget(Delete)
        confirmbuttons.add_widget(Edit)
        confirmbuttons.add_widget(Bill)
        layout.add_widget(confirmbuttons)
        layout.add_widget(leave)
        self.popup = Popup(title= f'{self.DATA[1]}', content = layout, size_hint=(None, None), size=(400, (layout.height + 275 + modifier)), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey')
        leave.bind(on_release = self.popup.dismiss)
        Bill.bind(on_release = lambda *args: self.PrintPaper())
        Edit.bind(on_release = lambda *args: self.edit())
        Delete.bind(on_release = lambda *args: self.DeleteData(self.NAME, self.IDNo, self.WINDOW, self.popup))
        pay.bind(on_release = lambda *args: self.Payment())
        self.popup.open()
    
    def PrintPaper(self):
        printer.Printer([self.DATA[1:]], "Bill", usb).Print()

    def Payment(self):
        PopUpPay(f"${"%.2f" % round((self.DATA[10] + float(self.DATA[5])), 2)}", self.DATA[0], self.DATA).Initialize()
        self.WINDOW.dismiss()
        self.popup.dismiss()

    def edit(self):
        Total().Update()
        recycle_view.data.clear()
        Total().Update()
        for i in json.loads(self.DATA[2]):
            recycle_view.data.extend([{'QTY': i['QTY'], 'NAME': i['NAME'], 'Price': i['Price'], 'NOTES': i['NOTES']}])
        Total().Calculate()
        databaseid.text = (self.IDNo)
        databasename.text = (self.NAME)
        Notesinput.text = (self.DATA[13])
        self.WINDOW.dismiss()
        self.popup.dismiss()

    def DeleteData(self, NAME, IDNo, WINDOW, popup):
        PopUpDelete(NAME, IDNo, WINDOW, popup).Window()
        
class TransactionsList(BoxLayout):
    DATA = ObjectProperty()
    NAME = StringProperty()
    WINDOW = ObjectProperty()
    IDNo = StringProperty()

    def view(self):
        modifier = 0
        confirmbuttons = GridLayout(cols = 3, rows = 1)
        layout = GridLayout(cols = 1, row_force_default=True, row_default_height=40)
        items = Label(text = "Items:", color = 'black', halign = 'left')
        items.bind(size=items.setter('text_size'))   
        layout.add_widget(items)
        time = Label(text = f"Completed at: {self.DATA[14]}" , color = 'black', halign = 'left')
        time.bind(size=time.setter('text_size'))   
        layout.add_widget(time)
        for i in json.loads(self.DATA[2]):
            if i['NOTES']:
                x = Label(text = f"{i['QTY']} x {i['NAME']}\nNotes:{i['NOTES']}", color = 'black', halign = 'left')
            else:
                x = Label(text = f"{i['QTY']} x {i['NAME']}", color = 'black', halign = 'left')
            x.bind(size=x.setter('text_size'))   
            layout.add_widget(x)
            modifier+= 50
        if self.DATA[13] != "Notes...":
            notesstring = Label(text = f"Notes: {self.DATA[13]}", color = 'black', halign = 'left')
            notesstring.bind(size=notesstring.setter('text_size'))
            layout.add_widget(notesstring)
            modifier += 50
        SubString = Label(text = f"SubTotal: ${"%.2f" %self.DATA[9]}", color = 'black', halign = 'left')
        SubString.bind(size=SubString.setter('text_size'))
        TaxesString = Label(text = f"GST: ${"%.2f" %self.DATA[7]}", color = 'black', halign = 'left')
        TaxesString.bind(size=TaxesString.setter('text_size'))
        TotalString = Label(text = f"Total: ${"%.2f" % round((self.DATA[10] + float(self.DATA[6])), 2)}", color = 'black', halign = 'left')
        TotalString.bind(size=TotalString.setter('text_size'))
        layout.add_widget(SubString)
        layout.add_widget(TaxesString)


        if self.DATA[8]:
            DiscountString = Label(text = f"Discount: -${"%.2f" %self.DATA[7]}", color = 'black', halign = 'left')
            DiscountString.bind(size=DiscountString.setter('text_size'))
            layout.add_widget(DiscountString)
            modifier += 50
        
        if self.DATA[4]:
            CashString = Label(text = f"Cash: ${"%.2f" %self.DATA[4]}", color = 'black', halign = 'left')
            CashString.bind(size=CashString.setter('text_size'))
            layout.add_widget(CashString)
            modifier += 50
        if self.DATA[5]:
            CreditString = Label(text = f"Credit: ${"%.2f" %self.DATA[5]}", color = 'black', halign = 'left')
            CreditString.bind(size=CreditString.setter('text_size'))
            layout.add_widget(CreditString)
            modifier += 50
        if self.DATA[6]:
            TipsString = Label(text = f"Tips: ${"%.2f" %self.DATA[6]}", color = 'black', halign = 'left')
            TipsString.bind(size=TipsString.setter('text_size'))
            layout.add_widget(TipsString)
            modifier += 50
        layout.add_widget(TotalString)
        if self.DATA[11]:
            ChangeString = Label(text = f"Change: -${"%.2f" %self.DATA[11]}", color = 'black', halign = 'left')
            ChangeString.bind(size=ChangeString.setter('text_size'))
            layout.add_widget(ChangeString)
            modifier += 50

       
        layout.add_widget(Label(height = 5, size_hint_y = None))
        leave = Button(text = 'Close', height = 40, size_hint_y = None, valign = 'bottom', pos_hint ={'x':.2, 'y':.2})
        Bill = Button(text = "Print Reciept", height = 40, size_hint_y = None, valign = 'bottom', pos_hint ={'x':.2, 'y':.2})
        edit = Button(text = "Edit", height = 40, size_hint_y = None, valign = 'bottom', pos_hint ={'x':.2, 'y':.2})
        confirmbuttons.add_widget(leave)
        confirmbuttons.add_widget(edit)
        confirmbuttons.add_widget(Bill)
        layout.add_widget(confirmbuttons)
        self.popup = Popup(title= f'{self.DATA[1]}', content = layout, size_hint=(None, None), size=(400, (layout.height + 250 + modifier)), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey')
        leave.bind(on_release = self.popup.dismiss)
        Bill.bind(on_release = lambda *args: self.PrintPaper())
        edit.bind(on_release = lambda *args: self.EditBill())
        self.popup.open()
    
    def PrintPaper(self):
        printer.Printer([self.DATA[1:]], "Reciept", usb).Print()

    def EditBill(self):
        printer.Printer([self.DATA[1:]], "Reciept", usb).Print()
        print(self.DATA[0])
        databases.Database.EditPaid(1, self.DATA[0])
        Total().Update()
        recycle_view.data.clear()
        Total().Update()
        for i in json.loads(self.DATA[2]):
            recycle_view.data.extend([{'QTY': i['QTY'], 'NAME': i['NAME'], 'Price': i['Price'], 'NOTES': i['NOTES']}])
        Total().Calculate()
        databaseid.text = (self.IDNo)
        databasename.text = (self.NAME)
        Notesinput.text = (self.DATA[13])
        self.popup.dismiss()
        self.WINDOW.dismiss()


    

#Popup
class PopUpClass(Popup):
    def __init__(self, **kwargs):
        self.quantity = Label(text = '1', color = 'black', font_size = 20)

    def Confirmation(self, *Item):
        layout = GridLayout(cols = 1)
        self.input = TextInput(text =  "Notes...", height = 32, size_hint_y = None)
        self.input.bind(focus = self.on_focus)
        Incrementbuttons = GridLayout(cols = 4, rows = 1, size = (300, 50), size_hint = (None, None))
        confirmbuttons = GridLayout(cols = 3, rows = 1)
        title = Label(text='Quantity', color = 'black', font_size = 25)
        placeholder = Label()
        placeholder2 = Label()
        placeholder3 = Label(width = 10)

        increase = Button(text = "+")
        decrease = Button(text = "-")

        Incrementbuttons.add_widget(placeholder3)
        Incrementbuttons.add_widget(decrease)
        Incrementbuttons.add_widget(self.quantity)
        Incrementbuttons.add_widget(increase)

        cancel = Button(text = "cancel", height = 50, size_hint_y = None)
        add = Button(text = "add", height = 50, size_hint_y = None)

        confirmbuttons.add_widget(cancel)
        confirmbuttons.add_widget(placeholder)
        confirmbuttons.add_widget(add)
        layout.add_widget(title)
        layout.add_widget(Incrementbuttons)
        layout.add_widget(Label(height = 15, size_hint_y = None))
        layout.add_widget(self.input)
        layout.add_widget(Label(height = 15, size_hint_y = None))
        layout.add_widget(confirmbuttons)

        self.popup = Popup(title=str(Item[0][0][2]), content=layout, size_hint=(None, None), size=(400, 350), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey', pos_hint={'righ': 1, 'top': 0.87})
        self.popup.open()
        cancel.bind(on_release = self.popup.dismiss)
        increase.bind(on_release = lambda *args: self.Increment())
        decrease.bind(on_release = lambda *args: self.Decrement())
        add.bind(on_release = lambda *args: self.add(Item))

    def on_focus(self, instance, value):
        if value:
            if self.input.text and self.input.text != "Notes...":
                return
            else:
                self.input.text = ''
        else:
            if self.input.text:
                return
            else:
                self.input.text = "Notes..."
            
    def Increment(self):
        self.quantity.text = str(int(self.quantity.text) + 1)
        if self.quantity.text == '0':
            self.quantity.text = str(int(self.quantity.text) + 1)

    def Decrement(self):
        self.quantity.text = str(int(self.quantity.text) - 1)
        if self.quantity.text == '0':
            self.quantity.text = str(int(self.quantity.text) - 1)

    def add(self, args):
        notes = ''
        if self.input.text and self.input.text != "Notes...":
            notes = str(self.input.text)
        args = args[0]
        if int(self.quantity.text) > 0:
            counter = 0
            for i in (recycle_view.data):
                if args[0][2] in i.values() and notes in i.values():
                    recycle_view.data[counter]['QTY'] = str(int(i['QTY']) + int(self.quantity.text))
                    recycle_view.data[counter]['Price'] = str("%.2f" % round((float(args[0][3]) * float(self.quantity.text)) + float(recycle_view.data[counter]['Price']), 2))
                    Total().Update()       
                    Total().Calculate()
                    self.popup.dismiss()
                    return
                counter += 1
            recycle_view.data.extend([{'QTY' : f"{self.quantity.text}", 'NAME' : f"{args[0][2]}", 'Price' : f"{str("%.2f" % round( float(args[0][3]) * float(self.quantity.text), 2))}" , "NOTES": f"{notes}" }])
            Total().Calculate()
            self.popup.dismiss()
            return
        elif int(self.quantity.text) < 0:
            counter = 0
            for i in (recycle_view.data):
                if args[0][2] in i.values() and notes in i.values():
                    recycle_view.data[counter]['QTY'] = str(int(i['QTY']) + int(self.quantity.text))
                    recycle_view.data[counter]['Price'] = str("%.2f" % round((float(args[0][3]) * (float(self.quantity.text))) + float(recycle_view.data[counter]['Price']), 2))
                    Total().Update()
                    Total().Calculate()
                    self.popup.dismiss()
                    return
                counter += 1
            recycle_view.data.extend([{'QTY' : f"{self.quantity.text}", 'NAME' : f"{args[0][2]}", 'Price' : f"{str("%.2f" % round( float(args[0][3]) * float(self.quantity.text), 2))}", "NOTES": f"{notes}"}])
            Total().Calculate()
            self.popup.dismiss()
            return
        else:
            return

class PopUpSearch():
    def __init__(self, **kwargs):
        con = sqlite3.connect(f'..\\POSsystem\\Default Databases\\MenuItems.db')
        cur = con.cursor()
        self.items = []
        for i in cur.execute("SELECT * FROM Items ORDER BY name"):
            self.items.append(i)
        con.close()

    def Search(self):
        layout = GridLayout(cols = 1)

        self.input = TextInput(text = "Search...",height = 32, size_hint_y = None)
        self.input.bind(text = lambda *args: self.on_text())
        self.input.bind(focus = self.on_focus)
        layout.add_widget(self.input)
        
        recycle_box_layout = RecycleBoxLayout(size=(100, 50), size_hint=(1, None), orientation='vertical')
        recycle_box_layout.bind(minimum_height=recycle_box_layout.setter("height"))
        self.dropdownview = RecycleView()
        self.dropdownview.add_widget(recycle_box_layout)
        self.dropdownview.viewclass = ItemsList
        layout.add_widget(self.dropdownview)
        self.leave = Button(text = 'Close', height = 64, size_hint_y = None)

        with self.leave.canvas.before:
            Color(rgba=(0, 0, 0, 1))
            self.leave.bg = Rectangle(pos=self.leave.pos, size=self.leave.size)
        self.leave.bind(pos=self.update_bg)
        self.leave.bind(size=self.update_bg)


        layout.add_widget(self.leave)

        self.popup = Popup(title= "search", content = layout, size_hint=(None, None), size=(750, 750), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey')
        for row in self.items:
            self.dropdownview.data.extend([{'NAME' : row[2], 'PRICE' : str(row[3]), 'WINDOW' : self.popup, 'ID': str(row[0])}])
        self.leave.bind(on_release = self.popup.dismiss)
        self.popup.open()

    def on_focus(self, instance, value):
        if value:
            if self.input.text and self.input.text != "Search...":
                return
            else:
                self.input.text = ''
        else:
            if self.input.text:
                return
            else:
                self.input.text = 'Search...'

    def on_text(self):
        if self.input.text == 'Search...':
            return
        temp = []
        for item in (self.items):
            if self.input.text.lower() in item[2].lower() or self.input.text.lower() in str(item[0]).lower():
                temp.append({'NAME' : item[2], 'PRICE' : str(item[3]), 'WINDOW' : self.popup, 'ID': str(item[0])})
        self.dropdownview.data = temp
        Total().Update()
        return

    def update_bg(self, *args):
        self.leave.bg.pos = self.leave.pos
        self.leave.bg.size = self.leave.size

class PopUpTicket():
    def __init__(self, status, **kwargs):
        self.status = status

    def confirmation(self):
        layout = GridLayout(cols = 1, row_force_default=True, row_default_height=50)
        if databaseid.text:
            self.input = TextInput(text =  databasename.text, height = 32, size_hint_y = None)
        else:
            self.input = TextInput(text =  "Enter Ticket Name...", height = 32, size_hint_y = None)
        self.input.bind(focus = self.on_focus)
        layout.add_widget(self.input)
        Buttons = GridLayout(cols = 3, rows = 1)
        leave = Button(text = 'Close', height = 64, size_hint_y = None)
        Buttons.add_widget(leave)
        Buttons.add_widget(Label())
        confirm = Button(text = 'Save', height = 64, size_hint_y = None)
        confirm.bind(on_release = lambda *args: self.confirm())
        Buttons.add_widget(confirm)
        layout.add_widget(Label())
        layout.add_widget(Buttons)
        self.popup = Popup(title= "Save Ticket", content = layout, size_hint=(None, None), size=(400, 250), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey', pos_hint={'righ': 1, 'top': 0.75})
        leave.bind(on_release = self.popup.dismiss)
        self.popup.open()

    def on_focus(self, instance, value):
        if value:
            if self.input.text and self.input.text != "Enter Ticket Name...":
                return
            else:
                self.input.text = ''
        else:
            if self.input.text:
                return
            else:
                self.input.text = "Enter Ticket Name..."

    def confirm(self, *args):
        if self.input.text == '' or self.input.text == "Enter Ticket Name...":
            return
        else:
            if databaseid.text:
                self.popup.dismiss()
                con = sqlite3.connect(f'..\\POSsystem\\Datas\\{str(datetime.now().date())}.db')
                cur = con.cursor()
                databases.Database().Update(recycle_view.data, GSTVar.text[1:], FeesVar.text[2:], SubTotalVar.text[1:], TotalVar.text[1:], Notesinput.text, databaseid.text, self.input.text)
                data = list(cur.execute(f'SELECT * FROM tickets WHERE rowid = {(databaseid.text)}'))
                con.close()
                PrintBill(databaseid.text, "Bill").window()
                Total().Reset()
                recycle_view.data.clear()
                Total().Update()
                Total().Calculate()
                
            else:
                self.popup.dismiss()
                databases.Database().add(self.input.text, recycle_view.data, self.status, 0.0, 0.0, 0.0, GSTVar.text[1:],FeesVar.text[2:], SubTotalVar.text[1:], TotalVar.text[1:], 0.0, 0.0, Notesinput.text, "")
                PrintBill("Last", "Bill").window()
                recycle_view.data.clear()
                Total().Reset()
                Total().Calculate()
                Total().Update()

class PopUpTicketWindow():
    def __init__(self, **kwargs):
        con = sqlite3.connect(f'..\\POSsystem\\Datas\\{str(datetime.now().date())}.db')
        cur = con.cursor()
        try:
            cur.execute("CREATE TABLE tickets(id, items, completed, cash, credit, tips, taxes, discounts, subtotal, total, change, roundedchange, notes, time)")
        except Exception as i:
            pass

        self.List = list(cur.execute("SELECT rowid, * FROM tickets WHERE completed=False"))
        con.close()
        
        
    
    def Window(self):
        layout = GridLayout(cols = 1)
        
        recycle_box_layout = RecycleBoxLayout(size=(100, 50), size_hint=(1, None), orientation='vertical')
        recycle_box_layout.bind(minimum_height=recycle_box_layout.setter("height"))
        self.dropdownview = RecycleView()
        self.dropdownview.add_widget(recycle_box_layout)
        self.dropdownview.viewclass = TicketsList
        layout.add_widget(self.dropdownview)
        self.leave = Button(text = 'Close', height = 40, size_hint_y = None)



        layout.add_widget(self.leave)

        self.popup = Popup(title= "Tickets", content = layout, size_hint=(None, None), size=(400, 900), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey')
        self.leave.bind(on_release = self.popup.dismiss)
        for i in self.List:
            if i[3] == False:
                self.dropdownview.data.extend([{'DATA': i, 'NAME': i[1], 'WINDOW': self.popup, 'IDNo': str(i[0])}])
        self.popup.open()

class PopUpTransactions():
    def __init__(self, **kwargs):
        con = sqlite3.connect(f'..\\POSsystem\\Datas\\{str(datetime.now().date())}.db')
        #con = sqlite3.connect(f'..\\POSsystem\\Datas\\2024-09-10.db')
        cur = con.cursor()
        try:
            cur.execute("CREATE TABLE tickets(id, items, completed, cash, credit, tips, taxes, discounts, subtotal, total, change, roundedchange, notes, time)")
        except Exception as i:
            pass

        self.List = list(cur.execute("SELECT rowid, * FROM tickets WHERE completed=True"))
        con.close()
        self.List.sort(key= lambda x:x[14])
        self.List.reverse()
    
    def Window(self):
        layout = GridLayout(cols = 1)
        
        recycle_box_layout = RecycleBoxLayout(size=(100, 50), size_hint=(1, None), orientation='vertical')
        recycle_box_layout.bind(minimum_height=recycle_box_layout.setter("height"))
        self.dropdownview = RecycleView()
        self.dropdownview.add_widget(recycle_box_layout)
        self.dropdownview.viewclass = TransactionsList
        layout.add_widget(self.dropdownview)
        self.leave = Button(text = 'Close', height = 40, size_hint_y = None)



        layout.add_widget(self.leave)

        self.popup = Popup(title= "Transactions", content = layout, size_hint=(None, None), size=(400, 600), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey')
        self.leave.bind(on_release = self.popup.dismiss)
        for i in self.List:
            if i[3] == True:
                self.dropdownview.data.extend([{'DATA': i, 'NAME': i[1], 'WINDOW': self.popup, 'IDNo': str(i[0])}])
        self.popup.open()

class PopUpDelete():
    def __init__(self, Name, IDNo, Window, Popup):
        self.Name = Name
        self.Id = IDNo
        self.window = Window
        self.LastPop = Popup
    def Window(self):
        layout = GridLayout(cols = 1)
        confirmbuttons = GridLayout(cols = 3, rows = 1)
        title = Label(text= f'Delete {self.Name}?', color = 'black', font_size = 25)
        placeholder = Label()

        cancel = Button(text = "Cancel", height = 50, size_hint_y = None)
        delete = Button(text = "Delete", height = 50, size_hint_y = None)

        confirmbuttons.add_widget(cancel)
        confirmbuttons.add_widget(placeholder)
        confirmbuttons.add_widget(delete)
        layout.add_widget(title)
        layout.add_widget(confirmbuttons)

        self.popup = Popup(title="Delete", content=layout, size_hint=(None, None), size=(400, 300), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey')
        self.popup.open()
        cancel.bind(on_release = self.popup.dismiss)
        delete.bind(on_release = lambda *args: self.delete())
        
    def delete(self):
        self.popup.dismiss()
        databases.Database().Delete(self.Id)
        self.LastPop.dismiss()
        self.window.dismiss()
        if self.Id == databaseid.text:
            Total().Reset()
            recycle_view.data.clear()
            Total().Update()
            Total().Calculate()

class PrintBill():
    def __init__(self, id, type,**kwargs):
        self.id = id
        self.type = type

    def window(self):
        layout = GridLayout(cols = 1)
        confirmbuttons = GridLayout(cols = 3, rows = 1)
        title = Label(text= f'Print {self.type}?', color = 'black', font_size = 25)
        placeholder = Label()

        cancel = Button(text = "close", height = 50, size_hint_y = None)
        delete = Button(text = "print", height = 50, size_hint_y = None)

        confirmbuttons.add_widget(cancel)
        confirmbuttons.add_widget(placeholder)
        confirmbuttons.add_widget(delete)
        layout.add_widget(title)
        layout.add_widget(confirmbuttons)

        self.popup = Popup(title=f"{self.type}", content=layout, size_hint=(None, None), size=(400, 300), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey')
        self.popup.open()
        cancel.bind(on_release = self.popup.dismiss)
        delete.bind(on_release = lambda *args: self.PrintBills(args))

    def PrintBills(self, args):
        data = 0
        con = sqlite3.connect(f'..\\POSsystem\\Datas\\{str(datetime.now().date())}.db')
        cur = con.cursor()
        if self.id == "Last":
            data = list(cur.execute('SELECT * FROM tickets WHERE rowid = (SELECT MAX(rowid) FROM Tickets)'))
        else:
            data = list(cur.execute(f'SELECT * FROM tickets WHERE rowid = {(self.id)}'))
        con.close()
        try:
            printer.Printer(list(data), self.type, usb).Print()
        except Exception as e:
            print(e)

        
class PopUpPay():
    def __init__(self, total, tunnel, data, **kwargs):
        self.tips = 0.0
        self.cash = 0.0
        self.credit = 0.0
        self.change = 0.0
        self.CustomList  = []
        self.amount = Label(text = total, color = 'black')
        self.amountentered = Label(text = '$0.00', color = 'black', font_size = 20)
        self.method = Label(text = '', color = 'black', font_size = 20)
        self.tunnel = tunnel
        self.data = data

    def Initialize(self):
        self.Window()
        self.Payment()
        self.popup.open()

    def Window(self):
        layout = GridLayout(cols = 1)
        confirmbuttons = GridLayout(cols = 4, rows = 1)
        title = Label(text='Payment Method', color = 'black', font_size = 25)
        placeholder = Label()
        placeholder2 = Label()
        creditbtn = Button(text = 'Credit')
        cashbtn = Button(text = 'Cash')
        creditbtn.bind(on_release = lambda *args: self.SwitchPayment(args))
        creditbtn.bind(on_press = lambda *args: self.ChangePayment(args, "Credit"))
        cashbtn.bind(on_release = lambda *args: self.SwitchPayment(args))
        cashbtn.bind(on_press = lambda *args: self.ChangePayment(args, "Cash"))

        cancel = Button(text = "Cancel", height = 50, size_hint_y = None)
        
        layout.add_widget(title)
        layout.add_widget(self.amount)
        layout.add_widget(creditbtn)
        layout.add_widget(cashbtn)
        confirmbuttons.add_widget(cancel)
        confirmbuttons.add_widget(placeholder)

        layout.add_widget(placeholder2)
        layout.add_widget(confirmbuttons)

        self.popup = Popup(title='Payment', content=layout, size_hint=(None, None), size=(400, 350), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey', auto_dismiss=False)
        cancel.bind(on_release = self.popup.dismiss)

    def ChangePayment(self, args, method):
        self.method.text = method

    def Payment(self):
        self.popup.dismiss()
        layout = GridLayout(cols = 1)
        self.CustomAmountPads = GridLayout(cols = 3, rows = 5, size = (150, 225), size_hint = (None, None))
        MegaGrid = GridLayout(cols = 2)

        Pay = Button(text = "Pay" , size = (150, 75), size_hint = (None, None))
        Clear = Button(text = "C" , size = (150, 75), size_hint = (None, None))
        Back = Button(text = "<" , size = (150, 75), size_hint = (None, None))
        for i in range(1, 10):
            btn = Button(text = str(i), size = (150, 75), size_hint = (None, None))
            self.CustomAmountPads.add_widget(btn)
            btn.bind(on_release = (self.NumberPressed))
        Zero = Button(text = "0" , size = (150, 75), size_hint = (None, None))

        self.CustomAmountPads.add_widget(Back)
        self.CustomAmountPads.add_widget(Zero)
        self.CustomAmountPads.add_widget(Clear)
        self.CustomAmountPads.add_widget(Label( size = (150, 75), size_hint = (None, None)))
        self.CustomAmountPads.add_widget(Pay)
        Back.bind(on_release = (self.NumberDelete))
        Zero.bind(on_release = (self.NumberPressed))
        Clear.bind(on_release = (self.ClearNumber))
        Pay.bind(on_release = lambda *args: self.PAY(args))

        MegaGrid.add_widget(Label(width = 15, size_hint_x = None))
        MegaGrid.add_widget(self.CustomAmountPads)
        layout.add_widget(self.method)
        layout.add_widget(Label(text = "Enter amount", color = 'black'))
        layout.add_widget(self.amountentered)
        layout.add_widget(MegaGrid)
        
        Closebtn = (Button(text = "Cancel", on_release = lambda *args: self.SwtichOptions(args), height = 50))
        for i in range(6):
            layout.add_widget(Label())
        layout.add_widget(Closebtn)
        self.Paymentpopup = Popup(title=self.amount.text, content=layout, size_hint=(None, None), size=(500, 700), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey', auto_dismiss=False)
  
    def NumberPressed(self, instance):
        self.CustomList.append(instance.text)
        if len(self.CustomList) == 1:
            self.amountentered.text = ('$0.0' + self.CustomList[0])
        elif len(self.CustomList) == 2:
            self.amountentered.text = ('$0.' + self.CustomList[0] + self.CustomList[1])
        else:
            self.amountentered.text = ('$' + ''.join(self.CustomList[:-2]) + '.' + ''.join(self.CustomList[-2:]))
    
    def NumberDelete(self, instance):
        self.CustomList = self.CustomList[:-1]
        if len(self.CustomList) == 0:
            self.amountentered.text = '$0.00'
        elif len(self.CustomList) == 1:
            self.amountentered.text = ('$0.0' + self.CustomList[0])
        elif len(self.CustomList) == 2:
            self.amountentered.text = ('$0.' + self.CustomList[0] + self.CustomList[1])
        else:
            self.amountentered.text = ('$' + ''.join(self.CustomList[:-2]) + '.' + ''.join(self.CustomList[-2:]))
    
    def ClearNumber(self, instance):
        self.CustomList.clear()
        self.amountentered.text = '$0.00'

    def PAY(self, instance):
        if self.amountentered.text == '$0.00':
            if self.method.text == "Credit":
                PopPayResults("%.2f" % self.cash, "%.2f" % Total().round_nearest2(self.change), "%.2f" % self.change ,"%.2f" % float(self.amount.text[1:]), "%.2f" % self.tips, self.tunnel,self.data).results()
                self.Paymentpopup.dismiss()
            else:
                return
        else:
            if float(self.amountentered.text[1:]) < float(self.amount.text[1:]):
                self.amount.text = f'${str("%.2f" %round(float(self.amount.text[1:]) - float(self.amountentered.text[1:]), 2))}'
                if self.method.text == "Credit":
                    self.credit += float(self.amountentered.text[1:])
                elif self.method.text == "Cash":
                    self.cash += float(self.amountentered.text[1:])
                self.Paymentpopup.dismiss()
                self.ClearNumber(instance)
                self.popup.open()
            else:                
                if self.method.text == "Credit":
                    if float(self.amountentered.text[1:]) > float(self.amount.text[1:]):
                        self.tips = round(float(self.amountentered.text[1:]) - (float(self.amount.text[1:])), 2)
                        self.credit += (float(self.amount.text[1:]))
                    else:
                        self.credit += (float(self.amount.text[1:]))
                elif self.method.text == "Cash":
                    if float(self.amountentered.text[1:]) > float(self.amount.text[1:]):
                        self.change =  round(float(self.amountentered.text[1:]) - (float(self.amount.text[1:])), 2)
                        self.cash += (float(self.amount.text[1:]))
                    else:
                        self.cash +=  (float(self.amount.text[1:]))
                self.Paymentpopup.dismiss()
                PopPayResults("%.2f" % self.cash, "%.2f" % Total().round_nearest2(self.change), "%.2f" % self.change ,"%.2f" % self.credit, "%.2f" % self.tips, self.tunnel,self.data).results()

    def SwtichOptions(self, instance):
        self.Paymentpopup.dismiss()
        self.popup.open()

    def SwitchPayment(self, args):
        if float(TotalVar.text[1:]) < 0:
            RefundPopup().refund(self.method.text)
        else:
            self.Paymentpopup.title = self.amount.text
            self.Paymentpopup.open()
        self.popup.dismiss()
        
class PopPayResults():
    def __init__(self, cash, roundedchange, change, credit, tips, tunnel, data):
        self.cash = (cash)
        self.roundedchange = roundedchange
        self.change = (change)
        self.credit = (credit)
        self.tips = (tips)
        self.dataid = databaseid.text
        self.tunnel = tunnel
        self.data = data

    def results(self):
        layout = GridLayout(cols = 1)
        title = Label(text= '', color = 'black', font_size = 25)
        leftovers = Label(text = '', color = 'black', font_size = 25)
        confirmbuttons = GridLayout(cols = 3, rows = 1)
        if self.change == 0 and self.tips == 0:
            pass
        elif float(self.tips):
            title.text = "Tips"
            leftovers.text = f'${str(self.tips)}'
            layout.add_widget(title)
            layout.add_widget(leftovers)
        elif float(self.roundedchange):
            title.text = "Change"
            leftovers.text = f'${str(self.roundedchange)}'
            layout.add_widget(title)
            layout.add_widget(leftovers)

        Finish = Button(text = "Exit", height = 50, size_hint_y = None)
        Print = Button(text = "Print", height = 50, size_hint_y = None)
        confirmbuttons.add_widget(Finish)
        confirmbuttons.add_widget(Label())
        confirmbuttons.add_widget(Print)

        layout.add_widget(Label(text = "Print Reciept?", color = 'black'))
        layout.add_widget(confirmbuttons)

        self.popup = Popup(title="Finalized", content=layout, size_hint=(None, None), size=(400, 300), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey')
        self.Payment()

        self.popup.open()
        Finish.bind(on_release = self.popup.dismiss)
        Print.bind(on_release = lambda *args: self.PrintReciept())
    
    def Payment(self):

        if self.tunnel != "default":
            databases.Database().Paid(json.loads(self.data[2]), self.cash, self.credit, self.tips, self.data[7], self.data[8], self.data[9], self.data[10], self.change, self.tunnel, self.roundedchange, datetime.now().strftime("%X"))
        elif databaseid.text:
            databases.Database().Paid(recycle_view.data, self.cash, self.credit, self.tips, GSTVar.text[1:], FeesVar.text[2:], SubTotalVar.text[1:], TotalVar.text[1:], self.change, databaseid.text, self.roundedchange, datetime.now().strftime("%X"))
        
        else:
            databases.Database().add("Paid", recycle_view.data, True, self.cash, self.credit, self.tips, GSTVar.text[1:], FeesVar.text[2:], SubTotalVar.text[1:], TotalVar.text[1:], self.change, self.roundedchange, Notesinput.text, datetime.now().strftime("%X"))
        if self.tunnel == "default":
            recycle_view.data.clear()
            Total().Update()
            Total().Reset()
            Total().Calculate()
        else:
            if str(self.tunnel) == databaseid.text:
                recycle_view.data.clear()
                Total().Update()
                Total().Reset()
                Total().Calculate()
        self.popup.dismiss()
        


    def PrintReciept(self):
        data = 0
        con = sqlite3.connect(f'..\\POSsystem\\Datas\\{str(datetime.now().date())}.db')
        cur = con.cursor()

        if self.tunnel != "default":
            data = list(cur.execute(f'SELECT * FROM tickets WHERE rowid = {(self.tunnel)}'))
        elif self.dataid:
            data = list(cur.execute(f'SELECT * FROM tickets WHERE rowid = {(self.dataid)}'))
        else:
            data = list(cur.execute('SELECT * FROM tickets WHERE rowid = (SELECT MAX(rowid) FROM Tickets)'))
        con.close()
        printer.Printer(list(data), "Reciept", usb).Print()

class RefundPopup():
    def refund(self, method):
        layout = GridLayout(cols = 1)
        title = Label(text= SubTotalVar.text, color = 'black', font_size = 25)  
        layout.add_widget(title)
        x = Button(text = "Close")
        layout.add_widget(x)
        self.popup = Popup(title="Refund", content=layout, size_hint=(None, None), size=(400, 300), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey')
        self.popup.open()
        x.bind(on_release = self.popup.dismiss)
        if databaseid.text:
            if method == "Cash":
                databases.Database().Paid(recycle_view.data, float(TotalVar.text[1:]), 0.0, 0.0, GSTVar.text[1:], FeesVar.text[2:], SubTotalVar.text[1:], TotalVar.text[1:], 0.0, databaseid.text, 0.0)
            if method == "Credit":
                databases.Database().Paid(recycle_view.data, 0.0, float(TotalVar.text[1:]), 0.0, GSTVar.text[1:], FeesVar.text[2:], SubTotalVar.text[1:], TotalVar.text[1:], 0.0, databaseid.text, 0.0)
        else:
            if method == "Cash":
                databases.Database().add("Refunded", recycle_view.data, True, float(TotalVar.text[1:]), 0.0, 0.0, GSTVar.text[1:], FeesVar.text[2:], SubTotalVar.text[1:], TotalVar.text[1:], 0.0, 0.0, Notesinput.text, datetime.now().strftime("%X"))
            if method == "Credit":
                databases.Database().add("Refunded", recycle_view.data, True, 0.0, float(TotalVar.text[1:]), 0.0, GSTVar.text[1:], FeesVar.text[2:], SubTotalVar.text[1:], TotalVar.text[1:], 0.0, 0.0, Notesinput.text, datetime.now().strftime("%X"))
        recycle_view.data.clear()
        Total().Update()
        Total().Reset()
        Total().Calculate()

class ReportPopUp():
    def __init__(self):
            self.cash = 0
            self.credit = 0
            self.tips = 0
            self.taxes = 0
            self.discounts = 0
            self.subtotal = 0
            self.total = 0
            self.change = 0
            self.roundedchange = 0
            self.cashrefunds = 0
            self.creditrefunds = 0
            self.subrefunds = 0
            self.creditCounter = 0
            self.cashCounter = 0
            con = sqlite3.connect(f'..\\POSsystem\\Datas\\{str(datetime.now().date())}.db')
            
            cur = con.cursor()
            try:
                cur.execute("CREATE TABLE tickets(id, items, completed, cash, credit, tips, taxes, discounts, subtotal, total, change, roundedchange, notes, time)")
            except Exception as i:
                pass
            List = list(cur.execute("SELECT * FROM tickets"))
            con.close()
            if not List:
                return
            else:
                for i in List:
                    if i[2]:
                        self.cash += i[3]
                        if i[0] == "Refunded":
                            self.creditrefunds += i[4]
                            self.cashrefunds += i[3]
                            self.subrefunds += i[8]
                        self.credit += i[4] + i[5]
                        self.subtotal += i[8]
                        self.total += i[9]
                        self.tips += i[5]
                        self.taxes += i[6]
                        self.discounts += i[7]
                        self.change += i[10]
                        self.roundedchange += (i[11])
                        if i[3] > 0:
                            self.cashCounter += 1
                        if i[4] > 0:
                            self.creditCounter += 1

    def Display(self):
        confirmbuttons = GridLayout(cols = 3, rows = 1)
        placeholder = Label()
        cancel = Button(text = "close", height = 50, size_hint_y = None)
        delete = Button(text = "print", height = 50, size_hint_y = None)
        confirmbuttons.add_widget(cancel)
        confirmbuttons.add_widget(placeholder)
        confirmbuttons.add_widget(delete)
        layout = GridLayout(cols = 1, row_force_default=True, row_default_height=40)
        layout.add_widget(Label(text = str(datetime.now().date()), color = 'black'))


        GrossString = Label(text = f"Gross Sales: ${"%.2f" % (self.subtotal - self.subrefunds)}", color = 'black', halign = 'left')
        GrossString.bind(size=GrossString.setter('text_size'))   
        layout.add_widget(GrossString)

        RefundString = Label(text = f"Refunds: $({"%.2f" % (self.subrefunds * -1)})", color = 'black', halign = 'left')
        RefundString.bind(size=RefundString.setter('text_size'))   
        layout.add_widget(RefundString)

        DiscountsString = Label(text = f"Discounts: $({"%.2f" % (self.discounts)})", color = 'black', halign = 'left')
        DiscountsString.bind(size=DiscountsString.setter('text_size'))   
        layout.add_widget(DiscountsString)

        layout.add_widget(Label())

        NetString = Label(text = f"Net Sales: ${"%.2f" % (self.subtotal - self.discounts)}", color = 'black', halign = 'left')
        NetString.bind(size=NetString.setter('text_size'))   
        layout.add_widget(NetString)

        TaxesString = Label(text = f"Taxes: ${"%.2f" % (self.taxes)}", color = 'black', halign = 'left')
        TaxesString.bind(size=TaxesString.setter('text_size'))   
        layout.add_widget(TaxesString)

        TipsString = Label(text = f"Tips: ${"%.2f" % (self.tips)}", color = 'black', halign = 'left')
        TipsString.bind(size=TipsString.setter('text_size'))   
        layout.add_widget(TipsString)

        CashroundString = Label(text = f"Cash Rounding: ${"%.2f" % (self.change-self.roundedchange)}", color = 'black', halign = 'left')
        CashroundString.bind(size=CashroundString.setter('text_size'))   
        layout.add_widget(CashroundString)

        layout.add_widget(Label())

        TotalString = Label(text = f"Total: ${"%.2f" % (self.total + self.tips + self.change-self.roundedchange)}", color = 'black', halign = 'left')
        TotalString.bind(size=TotalString.setter('text_size'))   
        layout.add_widget(TotalString)

        layout.add_widget(Label())

        salesCredit = Label(text = f"No. of Credit Sales: {(self.creditCounter)}", color = 'black', halign = 'left')
        salesCredit.bind(size=salesCredit.setter('text_size'))   
        layout.add_widget(salesCredit)     

        salesCash = Label(text = f"No. of Cash Sales: {(self.cashCounter)}", color = 'black', halign = 'left')
        salesCash.bind(size=salesCash.setter('text_size'))   
        layout.add_widget(salesCash)      

        layout.add_widget(Label())


        payments = Label(text = "Payments", color = 'black', halign = 'left')
        payments.bind(size=payments.setter('text_size'))  
        layout.add_widget(payments)

        cashString = Label(text = f"Cash: ${"%.2f" % (self.cash)}", color = 'black', halign = 'left')
        cashString.bind(size=cashString.setter('text_size'))   
        layout.add_widget(cashString)       

        creditString = Label(text = f"Credit: ${"%.2f" % (self.credit)}", color = 'black', halign = 'left')
        creditString.bind(size=creditString.setter('text_size'))   
        layout.add_widget(creditString)   

        layout.add_widget(Label())   

        
        delete.bind(on_release = lambda *args: self.Clockout(args))
        layout.add_widget(confirmbuttons)
        self.popup = Popup(title="Daily Report", content=layout, size_hint=(None, None), size=(500, 900), title_size = 30 , title_align = 'center' , background = 'white', title_color = 'black', separator_color = 'grey')
        cancel.bind(on_release = self.popup.dismiss)
        self.popup.open()
    
    def Clockout(self, *args):
        printer.Printer("yeet", "Gross", usb).GrossPaper()

#Global Classes
class Items():
    def Item(Type, *args):
        List = []
        con = sqlite3.connect(f'..\\POSsystem\\Default Databases\\MenuItems.db')
        cur = con.cursor()
        for i in list(cur.execute("SELECT * FROM Items ORDER BY name")):
            if (args[0]) in i[1].lower():
                List.append(i)
        con.close()
        if List:
            return List

class Total():
    def __init__(self, **kwargs):
        self.subtotal = 0.00
        self.gst = 0.00
        self.discounts = 0.00
        self.total = 0.00
        self.discounted = 0.00
        self.amountdiscounts = 0.0

    def Calculate(self):
        if recycle_view.data:
            for i in recycle_view.data:
                if i["NAME"] == "Cash Discount":
                    self.discounts += (float(i["Price"][:2])/100)
                elif i["NAME"] == "dis":
                    self.amountdiscounts += abs(float((i["Price"])))
                else:
                    self.subtotal += (float(i['Price']))
    
        self.discounted = round(((self.subtotal * self.discounts) + self.amountdiscounts), 2)
        self.gst = round((round((self.subtotal - self.discounted), 2) * 0.05), 2)
        
        self.total = round((self.subtotal - self.discounted + self.gst), 2)

        FeesVar.text = f'-${str("%.2f" % (self.discounted))}'
        SubTotalVar.text = (f'${str("%.2f" % round(self.subtotal, 2))}')
        GSTVar.text = (f'${str("%.2f" % (self.gst))}')
        TotalVar.text = (f'${str("%.2f" % (self.total))}')
        

    def Update(self):
        recycle_view.data.extend([{'QTY' : "Test", 'NAME' : "Test", 'Price' : "test"}])
        recycle_view.data.remove({'QTY' : "Test", 'NAME' : "Test", 'Price' : "test"})

    def Reset(self):
        databaseid.text = ''
        databasename.text = ''
        Notesinput.text = "Notes..."

    
    def round_nearest2(self, change):
        return round(round(change / 0.05) * 0.05, -int(math.floor(math.log10(0.05))))

#Main Class
class Main(App):
    def build(self):
        #Defualt Values
        Window.size = (1920, 1080)
        #Window.size = (1000, 600)
        return MainLayout()

#Main Function
if __name__ == "__main__":
    POS = Main()
    POS.run()