from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

import figures.hangmanfig4

Builder.load_file("screens/losescreen.kv")

class LoseScreen(Screen):
    widget_reference = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        figures.hangmanfig4.HangManFig4.lose_screen_reference = self

    def on_enter(self):
        LoseScreen.widget_reference.start_animation()
