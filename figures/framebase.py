from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.animation import Animation

import figures.hangmanfig3

Builder.load_file('figures/framebase.kv')


class FrameBase(Widget):
    x_offset = NumericProperty(0)
    w = NumericProperty(950)
    h = NumericProperty(750)

    def animate_it(self):
        anim = Animation(x_offset=-1000, duration=10)
        anim.start(self)

