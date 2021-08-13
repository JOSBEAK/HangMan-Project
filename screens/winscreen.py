from types import WrapperDescriptorType
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

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

    def on_leave(self):
        self.ids.animation_area.clear_widgets([WinScreen.widget_reference])



        