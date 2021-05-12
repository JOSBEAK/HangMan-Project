from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import NumericProperty

Builder.load_file('figures/hangmanfig1.kv')

class HangManFig1(Widget):
    angle = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.w = 950
        self.h = 750

        angle = NumericProperty(0)
        anim = Animation(angle=10)
        anim += Animation(angle=-10)
        anim.repeat = True
        anim.start(self)
    
