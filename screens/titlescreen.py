from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.animation import Animation

from kivymd.app import MDApp

Builder.load_file('screens/titlescreen.kv')

class TitleScreen(Screen):
    col_offset = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        anim = Animation(col_offset=1)
        anim += Animation(col_offset=0)

        anim.repeat = True
        anim.start(self)
            
    def on_touch_down(self,touch):
        if touch.is_double_tap:
            self.change_screen()

    def change_screen(self):
        app_root = MDApp.get_running_app().root
        setattr(app_root, 'current', '_main_screen_')

    
