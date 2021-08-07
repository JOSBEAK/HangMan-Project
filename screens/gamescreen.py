from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from random import choice

import widgets.keyboard
import widgets.dynamicwidget

Builder.load_file('screens/gamescreen.kv')


class GameScreen(Screen):
    word = str()
    guess = str()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.choose_word()
        widgets.keyboard.KeyBoard.game_screen_reference = self

    def choose_word(self, afile='Dict.txt'):
        GameScreen.word = choice(list(open(afile))).rstrip()
        GameScreen.guess = "_" * len(GameScreen.word)

    def update_guess(self, btn_text):
        guess_list = list(GameScreen.guess)
        for pos, letter in enumerate(GameScreen.word):
            if(letter == btn_text.lower()):
                guess_list[pos] = btn_text
        GameScreen.guess = self.ids.guess_label.text = "".join(guess_list)
