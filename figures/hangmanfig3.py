from types import DynamicClassAttribute
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import NumericProperty

Builder.load_file('figures/hangmanfig3.kv')

class HangManFigPart3(Widget):
    angle_a = NumericProperty(-100)
    angle_b = NumericProperty(100)
    angle_c = NumericProperty(-160)
    angle_d = NumericProperty(160)

    x_offset = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.animate_it()

    def animate_it(self):
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

        anim_temp = Animation(x_offset=300, duration=5)
        anim &= anim_temp

        anim.start(self)

class HangManFigPart1(Widget):
    offset_y = NumericProperty(0)
    angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.animate_it()

    def animate_it(self):
        anim = Animation(angle=10, duration=.5)
        anim += Animation(angle=-10)
        anim += Animation(angle=10)
        anim += Animation(angle=-10)
        anim += Animation(angle=0, duration=.5)

        anim += Animation(offset_y = -125, duration=.5)
        anim.start(self)

        anim.bind(on_complete=lambda *args: self.in_transition())

    def clear_screen(self):
        HangManFig3.win_screen_reference.ids.animation_area.clear_widgets([self])

    def in_transition(self):
        self.clear_screen()
        HangManFig3.win_screen_reference.ids.animation_area.add_widget(HangManFigPart2())
        
class HangManFigPart2(Widget):
    head_offset = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.animate_it()
    
    def animate_it(self):
        anim = Animation(head_offset=10, duration=.5)
        anim += Animation(head_offset=-5, duration=.5)
        anim += Animation(head_offset=10, duration=.5)

        anim.start(self)

        anim.bind(on_complete=lambda *args: self.in_transition())

    def clear_screen(self):
        HangManFig3.win_screen_reference.ids.animation_area.clear_widgets([self])
    
    def in_transition(self):
        self.clear_screen()
        HangManFig3.win_screen_reference.ids.animation_area.add_widget(HangManFigPart3())

class HangManFig3(Widget):
    win_screen_reference = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        HangManFig3.win_screen_reference.ids.animation_area.add_widget(HangManFigPart1())