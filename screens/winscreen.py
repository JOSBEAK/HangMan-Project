from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.app import MDApp

import figures.hangmanfig3
import figures.framebase

Builder.load_file('screens/winscreen.kv')


class WinScreen(Screen):
    widget_reference = None
    valid = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        figures.hangmanfig3.HangManFig3.win_screen_reference = self

    def on_enter(self):
        WinScreen.widget_reference.start_animation()

    def win_popup(self, final_fig=None):
        self.ids.animation_area.clear_widgets()

        if final_fig != None:
            if WinScreen.valid == False:
                WinScreen.valid = True
                return
            else:
                WinScreen.valid = True
        else:
            WinScreen.valid = False

        app_root = MDApp.get_running_app().root


        return_main = MDFillRoundFlatIconButton(
            text="Back to Main Screen", icon="arrow-left")

        dialog = MDDialog(title="YOU WIN!",
                          text="Go Back to Main Screen",
                          buttons=[return_main],
                          auto_dismiss=False)

        dialog.open()
        tr = app_root.transition

        WinScreen.valid = False
        return_main.bind(
            on_press=lambda *args: setattr(tr, 'direction', "right"))
        return_main.bind(
            on_press=lambda *args: setattr(app_root, 'current', "_main_screen_"))
        return_main.bind(on_press=dialog.dismiss)

