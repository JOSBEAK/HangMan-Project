from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import NumericProperty

from figures.framebase import FrameBase

Builder.load_file('figures/frame2.kv')

class Frame2(FrameBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        x = NumericProperty(0)
        anim = Animation(x=-800, duration=4)
        anim.start(self)



