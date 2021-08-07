from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from random import choice

import widgets.keyboard
import widgets.dynamicwidget

Builder.load_file('screens/gamescreen.kv')


class GameScreen(Screen):
    word = str()
    drawing_area = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        choose_word()
        widgets.keyboard.KeyBoard.game_screen_reference = self


def choose_word(afile='Dict.txt'):
    GameScreen.word = choice(list(open(afile))).rstrip()
