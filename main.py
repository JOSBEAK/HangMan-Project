from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App

from screens.mainscreen import MainScreen
from screens.gamescreen import GameScreen
from screens.sharescreen import ShareScreen
from screens.creditsscreen import CreditsScreen

class RootScreenManager(ScreenManager):
    pass


class HangManApp(App):
    def build(self):
        return RootScreenManager()


if __name__ == '__main__':
    HangManApp().run()
