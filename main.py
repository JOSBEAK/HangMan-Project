from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp

from screens.mainscreen import MainScreen
from screens.gamescreen import GameScreen
from screens.sharescreen import ShareScreen
from screens.topicscreen import TopicScreen
from screens.creditsscreen import CreditsScreen


class RootScreenManager(ScreenManager):
    pass


class HangManApp(MDApp):
    def build(self):
        return RootScreenManager()


if __name__ == '__main__':
    HangManApp().run()
