from kivy.uix.relativelayout import RelativeLayout
from kivy.lang.builder import Builder
from kivy.graphics import Line, Ellipse
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.uix.gridlayout import GridLayout


import screens.gamescreen
from widgets.dynamicwidget import DynamicLineWidget

Builder.load_file('widgets/keyboard.kv')

class KeyBoard(RelativeLayout):
    correct_guess = 0
    wrong_guess = 0
    game_screen_reference = None

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
            self.Win_Popup()


        btn.disabled = True

    def draw_next_part(self):
        with KeyBoard.game_screen_reference.ids.drawing_area.canvas:

            if KeyBoard.wrong_guess == 1:
                DynamicLineWidget(circle=[600, 568, 68], width=10, parent=KeyBoard.game_screen_reference.ids.drawing_area)

            elif KeyBoard.wrong_guess == 2:
                DynamicLineWidget(bezier=[610, 510, 630, 400, 570, 350], width=10, parent=KeyBoard.game_screen_reference.ids.drawing_area)

            elif KeyBoard.wrong_guess == 3:
                DynamicLineWidget(bezier=[570, 350, 510, 370, 450, 270], width=10, parent=KeyBoard.game_screen_reference.ids.drawing_area)

            elif KeyBoard.wrong_guess == 4:
                DynamicLineWidget(bezier=[570, 350, 600, 300, 550, 200], width=10, parent=KeyBoard.game_screen_reference.ids.drawing_area)

            elif KeyBoard.wrong_guess == 5:
                DynamicLineWidget(bezier=[610, 480, 530, 430, 500, 430], width=10, parent=KeyBoard.game_screen_reference.ids.drawing_area)

            else:
                DynamicLineWidget(bezier=[610, 480, 630, 500, 680, 390], width=10, parent=KeyBoard.game_screen_reference.ids.drawing_area)
    def Win_Popup(self):
        layout=GridLayout(cols=1,padding=10)
        label=Label(text="You Lose! Game Over!")
        closebutton=MDFillRoundFlatIconButton(text="Retry",icon="rotate-right",pos_hint ={'center_x':.7, 'center_y':.5})
        
        layout.add_widget(label)
        layout.add_widget(closebutton)

        popup = Popup(
          content= layout,
            size_hint=(None, None), size=(300, 300),auto_dismiss=False)
        popup.open()
        closebutton.bind(on_press=popup.dismiss)
