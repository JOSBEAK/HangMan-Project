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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        figures.hangmanfig3.HangManFig3.win_screen_reference = self

    def on_enter(self):
        WinScreen.widget_reference.start_animation()

    def win_popup(self):
        app_root = MDApp.get_running_app().root
        if getattr(app_root, 'current') == "_main_screen_":
            return

        self.ids.animation_area.clear_widgets([WinScreen.widget_reference])

        return_main = MDFillRoundFlatIconButton(
            text="Back to Main Screen", icon="arrow-left")

        dialog = MDDialog(title="YOU WIN!",
                          text="Go Back to Main Screen",
                          buttons=[return_main],
                          auto_dismiss=False)

        dialog.open()
        tr = app_root.transition
        return_main.bind(
            on_press=lambda *args: setattr(tr, 'direction', "right"))
        return_main.bind(
            on_press=lambda *args: setattr(app_root, 'current', "_main_screen_"))
        return_main.bind(on_press=dialog.dismiss)
