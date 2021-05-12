from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('figures/frame.kv')

class Frame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.w = 950
        self.h = 750
