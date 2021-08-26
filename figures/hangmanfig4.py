from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.animation import Animation
from kivy.lang import Builder

Builder.load_file("figures/hangmanfig4.kv")

import screens.losescreen
import figures.framebase

class HangManFig4Part1(Widget):
    w = NumericProperty(950)
    h = NumericProperty(750)

    angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animate_it()
    
    def animate_it(self):
        anim = Animation(angle=10, duration=.5)
        anim += Animation(angle=-10)
        anim += Animation(angle=0, duration=.5)

        anim.start(self)

        anim.bind(on_complete=lambda *args: self.in_transition())

    def clear_screen(self):
        HangManFig4.lose_screen_reference.ids.animation_area.clear_widgets([
                                                                          self])

    def in_transition(self):
        self.clear_screen()
        HangManFig4.lose_screen_reference.ids.animation_area.add_widget(
            HangManFig4Part2())


class HangManFig4Part2(Widget):
    w = NumericProperty(950)
    h = NumericProperty(750)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda *args: self.show_popup(), 3)
    
    def clear_screen(self):
        HangManFig4.lose_screen_reference.ids.animation_area.clear_widgets()

    def show_popup(self):
        self.clear_screen()
        HangManFig4.lose_screen_reference.lose_popup(self)


class HangManFig4(Widget):
    lose_screen_reference = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        screens.losescreen.LoseScreen.widget_reference = self

    def start_animation(self):
        HangManFig4.lose_screen_reference.ids.animation_area.add_widget(
            HangManFig4Part1())
        HangManFig4.lose_screen_reference.ids.animation_area.add_widget(
            figures.framebase.FrameBase()
        )
   