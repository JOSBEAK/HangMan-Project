from kivymd.uix.button import MDRoundFlatIconButton
from kivy.lang.builder import Builder

Builder.load_file('widgets/custombutton.kv')

class CustomButton(MDRoundFlatIconButton):
    pass
