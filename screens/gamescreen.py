from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from random import choice

from kivymd.app import MDApp

import widgets.keyboard
import widgets.dynamicwidget

Builder.load_file('screens/gamescreen.kv')


class GameScreen(Screen):
    score = 0
    level = 1
    lives = 3

    word = str()
    guess = str()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.choose_word()
        widgets.keyboard.KeyBoard.game_screen_reference = self

    def choose_word(self, afile='Dict.txt'):
        GameScreen.word = choice(list(open(afile))).rstrip()
        GameScreen.guess = "_" * len(GameScreen.word)

    def next_game(self):
        self.clear_hangman()
        self.choose_word()
        self.ids.guess_label.text = GameScreen.guess

    def clear_hangman(self):
        for instr in widgets.dynamicwidget.DynamicLineWidget.on_canvas:
            self.ids.drawing_area.canvas.remove(instr)

        widgets.dynamicwidget.DynamicLineWidget.on_canvas.clear()
        widgets.dynamicwidget.DynamicLineWidget.instructions.clear()

    def reset_game(self):
        self.clear_hangman()
        self.choose_word()

        GameScreen.lives = 3
        GameScreen.level = 1
        GameScreen.score = 0

        self.ids.lives_label.text = "💜" * GameScreen.lives
        self.ids.score_label.text = str(GameScreen.score)
        self.ids.level_label.text = "Level: " + str(GameScreen.level)

    def update_guess(self, btn_text):
        guess_list = list(GameScreen.guess)
        for pos, letter in enumerate(GameScreen.word):
            if(letter == btn_text.lower()):
                guess_list[pos] = btn_text
        GameScreen.guess = self.ids.guess_label.text = "".join(guess_list)

    def update_win(self):
        GameScreen.score += 100 * GameScreen.level
        GameScreen.level += 1

        if GameScreen.level == 6:
            app_root = MDApp.get_running_app().root
            setattr(app_root, 'current', '_win_screen_')
            self.reset_game()
        else:
            self.ids.score_label.text = str(GameScreen.score)
            self.ids.level_label.text = "Level: " + str(GameScreen.level)

    def update_lose(self):
        if GameScreen.score >= 10 * GameScreen.level:
            GameScreen.score -= 10 * GameScreen.level
        else:
            GameScreen.score = 0

        GameScreen.lives -= 1
        self.ids.score_label.text = str(GameScreen.score)
        self.ids.lives_label.text = "💜" * GameScreen.lives
