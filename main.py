import kivymd
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.image import Image
from screens.mainscreen import MainScreen
from screens.gamescreen import GameScreen
from screens.sharescreen import ShareScreen
from screens.creditsscreen import CreditsScreen

class RootScreenManager(ScreenManager):
    pass


class HangManApp(MDApp):
    def __init__(self, **kwargs):
        self.theme_cls.theme_style='Dark'
        super().__init__(**kwargs)

    
    def build(self):
        return RootScreenManager()


if __name__ == '__main__':
    HangManApp().run()
