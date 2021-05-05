from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.


# Declare both screens
class MenuScreen(Screen):
    pass

class Level1Screen(Screen):
    pass

class Level2Screen(Screen):
    pass
class Level3Screen(Screen):
    pass
class Level4Screen(Screen):
    pass
class TopicsScreen(Screen):
    pass


class HangManApp(App):
    def animate_the_button(self,widget,*args):
        anim=Animation(background_color=(0.3,0.6,0.7,1))
        anim.start(widget)
    def popup(self,widget,*args):
        anim=Animation(top_h=0.3)
        anim.start(widget)
        pass

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(Level1Screen(name='Level1'))
        sm.add_widget(Level2Screen(name='Level2'))
        sm.add_widget(Level3Screen(name='Level3'))
        sm.add_widget(Level4Screen(name='Level4'))
        sm.add_widget(TopicsScreen(name='Topics'))
        return sm

if __name__ == '__main__':
    HangManApp().run()
