from kivy.uix.relativelayout import RelativeLayout
from kivy.lang.builder import Builder

import screens.gamescreen as gamescreen

Builder.load_file('widgets/keyboard.kv')

class KeyBoard(RelativeLayout):
    correct_guess = 0
    wrong_guess = 0

    def check_in_word(self, btn):
        word = gamescreen.GameScreen.word

        if btn.text.lower() in word:
            KeyBoard.correct_guess += 1
        else:  
            KeyBoard.wrong_guess += 1;

        if KeyBoard.correct_guess >= len(set(word)):
            print("YOU WIN")
        elif KeyBoard.wrong_guess >= 6:
            print("YOU LOSE")

        btn.disabled = True
