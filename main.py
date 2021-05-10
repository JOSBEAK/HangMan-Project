from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, NoTransition

from screens.mainscreen import MainScreen
from screens.gamescreen import GameScreen
from screens.sharescreen import ShareScreen
from screens.topicscreen import TopicScreen
from screens.creditsscreen import CreditsScreen

class RootScreenManager(ScreenManager):
    transition = NoTransition()


class HangManApp(MDApp):
    def build(self):
        return RootScreenManager()


if __name__ == '__main__':
    HangManApp().run()
