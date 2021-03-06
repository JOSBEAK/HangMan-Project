from re import M
from kivy.uix.behaviors import button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from random import choice
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.app import MDApp
import widgets.keyboard
import widgets.dynamicwidget

Builder.load_file('screens/gamescreen.kv')


class GameScreen(Screen):
    score = 0
    level = 1
    lives = 3

    word = str()
    word_list = list(word)

    guess = str()
    keyboard_reference = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.choose_word()
        widgets.keyboard.KeyBoard.game_screen_reference = self

    def choose_word(self, afile='Dict.txt'):
        GameScreen.word = choice(list(open(afile))).rstrip()
        GameScreen.word_list = list(GameScreen.word)

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

    def quit_gamescreen(self):
        cancel_button = MDFillRoundFlatIconButton(
            text="NO", icon="close")

        return_main = MDFillRoundFlatIconButton(
            text="Quit", icon="arrow-left")

        dialog = MDDialog(title="Return To Main Screen?",
                          text="Sure Want to Quit the Game?",
                          buttons=[return_main, cancel_button],
                          auto_dismiss=False)

        dialog.open()
        cancel_button.bind(on_press=dialog.dismiss)

        app_root = MDApp.get_running_app().root
        tr = app_root.transition
        return_main.bind(
            on_press=lambda *args: setattr(tr, 'direction', "right"))
        return_main.bind(
            on_press=lambda *args: setattr(app_root, 'current', "_main_screen_"))
        return_main.bind(
            on_press=lambda *args: GameScreen.keyboard_reference.reset())
        return_main.bind(on_press=dialog.dismiss)

    def reset_game(self):
        self.next_game()

        GameScreen.lives = 3
        GameScreen.level = 1
        GameScreen.score = 0

        self.ids.lives_label.text = "????" * GameScreen.lives
        self.ids.score_label.text = str(GameScreen.score)
        self.ids.level_label.text = "Level: " + str(GameScreen.level)

    def update_guess(self, btn_text):
        guess_list = list(GameScreen.guess)
        for pos, letter in enumerate(GameScreen.word):
            if(letter == btn_text.lower()):
                guess_list[pos] = btn_text
                GameScreen.word_list.remove(letter) 
        GameScreen.guess = self.ids.guess_label.text = "".join(guess_list)

    def update_win(self):
        GameScreen.score += 100 * GameScreen.level
        GameScreen.level += 1

        if GameScreen.level == 6:
            app_root = MDApp.get_running_app().root
            self.reset_game()
            setattr(app_root, 'current', '_win_screen_')
        else:
            self.ids.score_label.text = str(GameScreen.score)
            self.ids.level_label.text = "Level: " + str(GameScreen.level)

    def update_lose(self):
        if GameScreen.score >= 10 * GameScreen.level:
            GameScreen.score -= 10 * GameScreen.level
        else:
            GameScreen.score = 0

        GameScreen.lives -= 1

        if GameScreen.lives == 0:
            app_root = MDApp.get_running_app().root
            self.reset_game()
            setattr(app_root, 'current', '_lose_screen_')
        else:
            self.ids.score_label.text = str(GameScreen.score)
            self.ids.lives_label.text = "????" * GameScreen.lives

    def hint_popup(self):
        hint_button = MDFillRoundFlatIconButton(
            text="Take Hint", icon="key")

        cancel_button = MDFillRoundFlatIconButton(
            text="Cancel", icon="arrow-left")

        dialog = MDDialog(
            title="Buy a Hint?", text="50 points will be deducted from the score",
            buttons=[cancel_button, hint_button], auto_dismiss=False)

        dialog.open()
        cancel_button.bind(on_press=dialog.dismiss)

        hint_button.bind(on_press=lambda *args: self.credit_check())
        hint_button.bind(on_press=dialog.dismiss)

    def credit_check(self):
        if GameScreen.score < 50:
            self.insuff_credit()
        else:
            self.take_hint()
    
    def insuff_credit(self):
        ok_button = MDFillRoundFlatIconButton(text="OK", icon="")

        dialog = MDDialog(title="Insufficient Credit", 
        text="Score must be atleast 50 to buy a hint", buttons=[ok_button], 
        auto_dismiss=False)

        dialog.open()
        ok_button.bind(on_press=dialog.dismiss)

    def take_hint(self):
        letter = GameScreen.word_list[0]
        GameScreen.keyboard_reference.ids[letter.upper()].background_color = [1, 1, 1, 1]
        GameScreen.keyboard_reference.ids[letter.upper()].color = [0, 0, 0, 1]

        GameScreen.score -= 50
        self.ids.score_label.text = str(GameScreen.score)





