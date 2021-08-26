from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.dialog import MDDialog

import figures.hangmanfig4

Builder.load_file("screens/losescreen.kv")

class LoseScreen(Screen):
    widget_reference = None
    valid = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        figures.hangmanfig4.HangManFig4.lose_screen_reference = self

    def on_enter(self):
        LoseScreen.widget_reference.start_animation()

    def lose_popup(self, final_fig=None):
        if final_fig != None:
            if LoseScreen.valid == False:
                LoseScreen.valid = True
                return
        else:
            LoseScreen.valid = False

        self.ids.animation_area.clear_widgets()
        app_root = MDApp.get_running_app().root


        return_main = MDFillRoundFlatIconButton(
            text="Back to Main Screen", icon="arrow-left")

        dialog = MDDialog(title="YOU LOSE!",
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


