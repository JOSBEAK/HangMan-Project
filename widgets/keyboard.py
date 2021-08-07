from kivy.uix.relativelayout import RelativeLayout
from kivy.lang.builder import Builder

from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp

import screens.mainscreen
import screens.gamescreen
import widgets.dynamicwidget

Builder.load_file('widgets/keyboard.kv')


class KeyBoard(RelativeLayout):
    correct_guess = 0
    wrong_guess = 0
    game_screen_reference = None

    def check_in_word(self, btn):
        word = screens.gamescreen.GameScreen.word
        print(word)
        btn.disabled = True

        if btn.text.lower() in word:
            KeyBoard.correct_guess += 1
        else:
            KeyBoard.wrong_guess += 1
            self.draw_next_part()

        if KeyBoard.correct_guess >= len(set(word)):
            print("YOU WIN")
            self.win_popup(word)
        elif KeyBoard.wrong_guess >= 6:
            print("YOU LOSE")
            self.lose_popup(word)

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

    def lose_popup(self, hidden_word):
        self.reset()

        retry_button = MDFillRoundFlatIconButton(
            text="Retry", icon="rotate-right")

        return_main = MDFillRoundFlatIconButton(
            text="Home Screen", icon="arrow-left")

        dialog = MDDialog(text=f"You Lose, The hidden word was {hidden_word}!",
                          buttons=[retry_button, return_main],
                          auto_dismiss=False)

        dialog.open()
        retry_button.bind(on_press=dialog.dismiss)

        app_root = MDApp.get_running_app().root
        return_main.bind(
            on_release=lambda *args: setattr(app_root, 'current', "_main_screen_"))
        return_main.bind(on_release=dialog.dismiss)

    def win_popup(self, hidden_word):
        self.reset()
        play_again = MDFillRoundFlatIconButton(
            text="Play Again", icon="rotate-right")

        return_main = MDFillRoundFlatIconButton(
            text="Home Screen", icon="arrow-left")

        dialog = MDDialog(text=f"You Win, The hidden word was {hidden_word}!",
                          buttons=[play_again, return_main],
                          auto_dismiss=False)

        dialog.open()
        play_again.bind(on_press=dialog.dismiss)

        app_root = MDApp.get_running_app().root
        return_main.bind(
            on_release=lambda *args: setattr(app_root, 'current', "_main_screen_"))
        return_main.bind(on_release=dialog.dismiss)

    def reset(self):
        for instr in widgets.dynamicwidget.DynamicLineWidget.on_canvas:
            KeyBoard.game_screen_reference.ids.drawing_area.canvas.remove(
                instr)

        widgets.dynamicwidget.DynamicLineWidget.on_canvas.clear()
        widgets.dynamicwidget.DynamicLineWidget.instructions.clear()

        KeyBoard.wrong_guess = 0
        KeyBoard.correct_guess = 0

        self.clear_buttons()
        screens.gamescreen.choose_word()
