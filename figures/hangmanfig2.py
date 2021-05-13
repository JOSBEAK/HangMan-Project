from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import NumericProperty


Builder.load_file('figures/hangmanfig2.kv')

class HangManFig2(Widget):
    angle_a = NumericProperty(0)
    angle_b = NumericProperty(0)
    angle_c = NumericProperty(0)
    angle_d = NumericProperty(0)

    x = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.w = 950
        self.h = 750

        anim = Animation(angle_a=10)
        anim += Animation(angle_a=-100)
        anim.repeat = True

        anim_temp = Animation(angle_b=-10)
        anim_temp += Animation(angle_b=100)
        anim_temp.repeat = True
        anim &= anim_temp

        anim_temp = Animation(angle_c=10)
        anim_temp += Animation(angle_c=-160)
        anim_temp.repeat = True
        anim &= anim_temp

        anim_temp = Animation(angle_d=-10)
        anim_temp += Animation(angle_d=160)
        anim_temp.repeat = True
        anim &= anim_temp

        anim_temp = Animation(x=800, duration=4)
        anim &= anim_temp

        anim.start(self)
    
