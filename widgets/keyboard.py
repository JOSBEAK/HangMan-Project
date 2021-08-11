from kivy.uix.relativelayout import RelativeLayout
from kivy.lang.builder import Builder

from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
import screens.mainscreen
import screens.gamescreen
import widgets.dynamicwidget

Builder.load_file('widgets/keyboard.kv')


class KeyBoard(RelativeLayout):
    correct_guess = 0
    wrong_guess = 0
    game_screen_reference = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        screens.gamescreen.GameScreen.keyboard_reference=self

    def check_in_word(self, btn):
        word = screens.gamescreen.GameScreen.word
        btn.disabled = True

        if btn.text.lower() in word:
            KeyBoard.correct_guess += 1
            KeyBoard.game_screen_reference.update_guess(btn.text)
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
        self.next_game()

        retry_button = MDFillRoundFlatIconButton(
            text="Retry", icon="rotate-right")

        return_main = MDFillRoundFlatIconButton(
            text="Quit", icon="arrow-left")

        dialog = MDDialog(title="WRONG ANSWER!",
                          text=f"The hidden word was {hidden_word}!",
                          buttons=[return_main,retry_button],
                          auto_dismiss=False)

        dialog.open()
        retry_button.bind(on_press=lambda *args: self.update_lose())
        retry_button.bind(on_press=lambda *args: self.next_game())
        retry_button.bind(on_press=dialog.dismiss)

        app_root = MDApp.get_running_app().root
        tr = app_root.transition
        return_main.bind(
            on_press=lambda *args: setattr(tr,'direction',"right"),
            on_release=lambda *args: setattr(app_root,'current',"_main_screen_"))
        return_main.bind(
            on_press=lambda *args: self.reset())
        return_main.bind(on_press=dialog.dismiss)


    def win_popup(self, hidden_word):
        self.next_game()
        next_level = MDFillRoundFlatIconButton(
            text="Next Level", icon="rotate-right")

        return_main = MDFillRoundFlatIconButton(
            text="Quit", icon="arrow-left")

        dialog = MDDialog(title="CORRECT ANSWER!",
                          text=f"The hidden word was {hidden_word}!",
                          buttons=[return_main,next_level],
                          auto_dismiss=False)

        dialog.open()
        next_level.bind(on_press=lambda *args: self.update_win())
        next_level.bind(on_press=lambda *args: self.next_game())
        next_level.bind(on_press=dialog.dismiss)

        app_root = MDApp.get_running_app().root
        transition = app_root.transition
        return_main.bind(
            on_press=lambda *args: setattr(tr,'direction',"right"),
            on_release=lambda *args: setattr(app_root, 'current', "_main_screen_"))
        return_main.bind(on_press=lambda *args: self.reset())
        return_main.bind(on_press=dialog.dismiss)

    def next_game(self):
        KeyBoard.wrong_guess = 0
        KeyBoard.correct_guess = 0

        self.clear_buttons()
        KeyBoard.game_screen_reference.next_game()

    def reset(self):
        KeyBoard.wrong_guess = 0
        KeyBoard.correct_guess = 0

        self.clear_buttons()
        KeyBoard.game_screen_reference.reset_game()

    def update_win(self):
        KeyBoard.game_screen_reference.update_win()

    def update_lose(self):
        KeyBoard.game_screen_reference.update_lose()
