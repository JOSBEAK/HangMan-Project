from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from random import choice

import widgets.keyboard as keyboard

Builder.load_file('screens/gamescreen.kv')

class GameScreen(Screen):
    word = str()

    def find_word(self, afile='Dict.txt'):
        return choice(list(open(afile))).rstrip()

    def on_enter(self):
        GameScreen.word = self.find_word()
        keyboard.KeyBoard.correct_guess = 0
        keyboard.KeyBoard.wrong_guess = 0
