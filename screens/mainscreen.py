from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatIconButton

Builder.load_file('screens/mainscreen.kv')

class MainScreen(Screen):
    def show_confirmation_dialog(self):
        dialog = MDDialog(title="Do you really want to exit?", 
                type="confirmation", 
                buttons=[MDFillRoundFlatIconButton(text="Cancel"), 
                    MDFillRoundFlatIconButton(text="OK")])

        dialog.open()





