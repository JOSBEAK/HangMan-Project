from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.lang.builder import Builder

Builder.load_file('widgets/custombutton.kv')

class CustomButton(MDFillRoundFlatIconButton):
    pass
