from kivy.uix.relativelayout import RelativeLayout
from kivy.lang.builder import Builder
import random
Builder.load_file('widgets/keyboard.kv')

class KeyBoard(RelativeLayout):
    wrong_guess = 0
    correct_guess = 0


    #to select a random string
    def FindHangmanWord(self):
        afile = 'Dict.txt'

        # find number of lines in file
        with open(afile) as f:
            for i, l in enumerate(f):
                pass

        # grab a random line and return it
        randNum = random.randrange(i+1)
        with open(afile) as f:
            for i, line in enumerate(f):
                if i+1 >= randNum:
                    return line[:len(line)-1]
                    break
        return None

    #to check if word present in string
    def check_in_word(self, btn):
        count = 0;
        for i, letter in enumerate(self.FindHangmanWord()):
            if btn.text == letter.upper():
                self.correct_guess+=1
                count += 1
                
                if self.correct_guess >= len(self.FindHangmanWord()):
                    print('GAME OVER, YOU WIN')
                
        if count == 0:
            # count wrong guess
            self.wrong_guess+=1
            if self.wrong_guess >= 6:
                print('GAME OVER, YOU LOSE!')

        btn.disabled = True # True is synonymous with         
     
   
