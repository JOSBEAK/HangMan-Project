from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.core.window import Window
from kivy.uix.widget import Widget
from screens.mainscreen import MainScreen
from screens.gamescreen import GameScreen
from screens.sharescreen import ShareScreen
from screens.topicscreen import TopicScreen
from screens.creditsscreen import CreditsScreen
from kivy.properties import StringProperty, ListProperty, NumericProperty
import random

#Window.maximize()

class RootScreenManager(ScreenManager):
    pass

class HangManApp(MDApp):
    def build(self):
        return RootScreenManager()


if __name__ == '__main__':
    HangManApp().run()
