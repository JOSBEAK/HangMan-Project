from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

import figures.hangmanfig3

Builder.load_file('screens/winscreen.kv')


class WinScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        figures.hangmanfig3.HangManFig3.win_screen_reference = self
        