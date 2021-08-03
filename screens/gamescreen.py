from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.graphics import Line, Color

from random import choice

import widgets.keyboard
import widgets.dynamicwidget

Builder.load_file('screens/gamescreen.kv')

class GameScreen(Screen):
    word = str()
    drawing_area = ObjectProperty(None)
    keyboard_reference = None

    def find_word(self, afile='Dict.txt'):
        return choice(list(open(afile))).rstrip()

    def on_enter(self):
        GameScreen.word = self.find_word()
        widgets.keyboard.KeyBoard.correct_guess = 0
        widgets.keyboard.KeyBoard.wrong_guess = 0
        widgets.keyboard.KeyBoard.game_screen_reference = self

        for instr in widgets.dynamicwidget.DynamicLineWidget.on_canvas:
            self.ids.drawing_area.canvas.remove(instr)

        widgets.dynamicwidget.DynamicLineWidget.on_canvas.clear()
        widgets.dynamicwidget.DynamicLineWidget.instructions.clear()

        GameScreen.keyboard_reference.clear_buttons()






