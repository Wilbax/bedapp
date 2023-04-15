from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen


class LoadingScreen(MDScreen):
    pass


class UserTypeScreen(MDScreen):
    pass


class WindowManager(MDScreenManager):
    pass


class mainApp(MDApp):

    def build(self):
        kv = Builder.load_file("Interfaces/Main/loadingScreen.kv")
        return kv


if __name__ == "__main__":
    mainApp().run()
