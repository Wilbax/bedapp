from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager


class MainScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("bedx.kv")


class bedApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    bedApp().run()
