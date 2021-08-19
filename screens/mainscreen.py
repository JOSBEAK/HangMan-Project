from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatIconButton

Builder.load_file('screens/mainscreen.kv')


class MainScreen(Screen):
    def show_confirmation_dialog(self):
        cancel_button = MDFillRoundFlatIconButton(text="Cancel")
        exit_button = MDFillRoundFlatIconButton(text="OK")
        dialog = MDDialog(title="Do you really want to exit?",
                          type="confirmation",
                          buttons=[exit_button, cancel_button], auto_dismiss=False)

        dialog.open()
        cancel_button.bind(on_press=dialog.dismiss)
        exit_button.bind(on_press=MDApp.get_running_app().stop)
