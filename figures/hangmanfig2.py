from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('figures/hangmanfig2.kv')

class HangManFig2(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.w = 950
        self.h = 750
