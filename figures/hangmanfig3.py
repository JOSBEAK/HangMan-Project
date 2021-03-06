from figures.hangmanfig4 import HangManFig4
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import NumericProperty

import screens.winscreen
import figures.framebase

Builder.load_file('figures/hangmanfig3.kv')


class HangManFigPart3(Widget):
    angle_a = NumericProperty(-100)
    angle_b = NumericProperty(100)
    angle_c = NumericProperty(-160)
    angle_d = NumericProperty(160)

    w = NumericProperty(950)
    h = NumericProperty(750)

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

        anim_temp = Animation(x_offset=1000, duration=7)
        anim &= anim_temp

        HangManFig3.obj.animate_it()
        Clock.schedule_once(
            lambda *args: self.show_popup(), 5)

        anim.start(self)

    def show_popup(self):
        self.clear_screen()
        HangManFig3.win_screen_reference.win_popup(self)

    def clear_screen(self):
        HangManFig3.win_screen_reference.ids.animation_area.clear_widgets([self, HangManFig3.obj])



class HangManFigPart1(Widget):
    offset_y = NumericProperty(0)
    angle = NumericProperty(0)

    w = NumericProperty(950)
    h = NumericProperty(750)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animate_it()


    def animate_it(self):
        anim = Animation(angle=10, duration=.5)
        anim += Animation(angle=-10)
        anim += Animation(angle=0, duration=.5)

        anim += Animation(offset_y=-125, duration=.5)
        anim.start(self)

        anim.bind(on_complete=lambda *args: self.in_transition())

    def clear_screen(self):
        HangManFig3.win_screen_reference.ids.animation_area.clear_widgets([
                                                                          self])

    def in_transition(self):
        self.clear_screen()
        HangManFig3.win_screen_reference.ids.animation_area.add_widget(
            HangManFigPart2())


class HangManFigPart2(Widget):
    head_offset = NumericProperty(0)

    w = NumericProperty(950)
    h = NumericProperty(750)

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
        HangManFig3.win_screen_reference.ids.animation_area.clear_widgets([
                                                                          self])

    def in_transition(self):
        self.clear_screen()
        HangManFig3.win_screen_reference.ids.animation_area.add_widget(
            HangManFigPart3())


class HangManFig3(Widget):
    win_screen_reference = None
    obj = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        screens.winscreen.WinScreen.widget_reference = self

    def start_animation(self):
        HangManFig3.win_screen_reference.ids.animation_area.add_widget(
            HangManFigPart1())
        HangManFig3.obj = figures.framebase.FrameBase()
        HangManFig3.win_screen_reference.ids.animation_area.add_widget(
            HangManFig3.obj)
