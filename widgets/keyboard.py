from kivy.uix.relativelayout import RelativeLayout
from kivy.lang.builder import Builder
from kivy.graphics import Line, Ellipse

import screens.gamescreen
import widgets.dynamicwidget

Builder.load_file('widgets/keyboard.kv')

class KeyBoard(RelativeLayout):
    correct_guess = 0
    wrong_guess = 0
    game_screen_reference = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        screens.gamescreen.GameScreen.keyboard_reference = self

    def check_in_word(self, btn):
        word = screens.gamescreen.GameScreen.word

        if btn.text.lower() in word:
            KeyBoard.correct_guess += 1
        else:  
            KeyBoard.wrong_guess += 1
            self.draw_next_part()

        if KeyBoard.correct_guess >= len(set(word)):
            print("YOU WIN")
        elif KeyBoard.wrong_guess >= 6:
            print("YOU LOSE")

        btn.disabled = True

    def clear_buttons(self):
        for btn in self.ids.values():
            btn.disabled = False

    def draw_next_part(self):
        with KeyBoard.game_screen_reference.ids.drawing_area.canvas:

            if KeyBoard.wrong_guess == 1:
                widgets.dynamicwidget.DynamicLineWidget(
                        circle=[600, 568, 68], width=10,
                        parent=KeyBoard.game_screen_reference.ids.drawing_area)

            elif KeyBoard.wrong_guess == 2:
                widgets.dynamicwidget.DynamicLineWidget(
                        bezier=[610, 510, 630, 400, 570, 350],
                        width=10, parent=KeyBoard.game_screen_reference.ids.drawing_area)

            elif KeyBoard.wrong_guess == 3:
                widgets.dynamicwidget.DynamicLineWidget(
                        bezier=[570, 350, 510, 370, 450, 270],
                        width=10, parent=KeyBoard.game_screen_reference.ids.drawing_area)

            elif KeyBoard.wrong_guess == 4:
                widgets.dynamicwidget.DynamicLineWidget(
                        bezier=[570, 350, 600, 300, 550, 200],
                        width=10, parent=KeyBoard.game_screen_reference.ids.drawing_area)

            elif KeyBoard.wrong_guess == 5:
                widgets.dynamicwidget.DynamicLineWidget(
                        bezier=[610, 480, 530, 430, 500, 430],
                        width=10, parent=KeyBoard.game_screen_reference.ids.drawing_area)

            else:
                widgets.dynamicwidget.DynamicLineWidget(
                        bezier=[610, 480, 630, 500, 680, 390],
                        width=10, parent=KeyBoard.game_screen_reference.ids.drawing_area)
