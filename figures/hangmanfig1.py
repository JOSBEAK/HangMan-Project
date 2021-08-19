from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import NumericProperty

Builder.load_file('figures/hangmanfig1.kv')


class HangManFig1(Widget):
    angle = NumericProperty(-10)
    w = NumericProperty(950)
    h = NumericProperty(750)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animate_it()

    def animate_it(self):
        anim = Animation(angle=10)
        anim += Animation(angle=-10)
        anim.repeat = True
        anim.start(self)
