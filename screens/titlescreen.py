from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.animation import Animation
from kivy.clock import Clock

from kivymd.app import MDApp

Builder.load_file('screens/titlescreen.kv')

class TitleScreen(Screen):
    sz_offset = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        anim = Animation(sz_offset=.7, duration=3)
        anim.start(self)

        Clock.schedule_once(lambda *args: self.change_screen(), 5)

    def change_screen(self):
        app_root = MDApp.get_running_app().root

        setattr(app_root, 'current', '_main_screen_')

    
