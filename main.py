from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager


# KV = '''
# MDScreenManager:
#
#     MDScreen:
#         name: "screen A"
#         md_bg_color: "lightblue"
#
#         MDHeroFrom:
#             id: hero_from
#             tag: "hero"
#             size_hint: None, None
#             size: "120dp", "120dp"
#             pos_hint: {"top": .98}
#             x: 24
#
#             FitImage:
#                 source: "kivymd/images/logo/kivymd-icon-512.png"
#                 size_hint: None, None
#                 size: hero_from.size
#
#         MDRaisedButton:
#             text: "Move Hero To Screen B"
#             pos_hint: {"center_x": .5}
#             y: "36dp"
#             on_release:
#                 root.current_heroes = ["hero"]
#                 root.current = "screen B"
#
#     MDScreen:
#         name: "screen B"
#         hero_to: hero_to
#         md_bg_color: "cadetblue"
#
#         MDHeroTo:
#             id: hero_to
#             tag: "hero"
#             size_hint: None, None
#             size: "220dp", "220dp"
#             pos_hint: {"center_x": .5, "center_y": .5}
#
#         MDRaisedButton:
#             text: "Move Hero To Screen A"
#             pos_hint: {"center_x": .5}
#             y: "36dp"
#             on_release:
#                 root.current_heroes = ["hero"]
#                 root.current = "screen A"
# '''


class SManager(ScreenManager):
    pass


class OpeningScreen(MDScreen):
    pass


class LoadingScreen(MDScreen):
    pass


class UserTypeScreen(MDScreen):
    pass


class Test(MDApp):
    def build(self):
        # Set the window size to match a typical mobile app size
        Config.set('graphics', 'width', '360')
        Config.set('graphics', 'height', '640')
        Window.size = (360, 640)
        kv = Builder.load_file('Interfaces/Main/loadingScreen.kv')
        self.theme_cls.primary_palette = "BlueGray"
        return kv

    # def on_start(self):
    #     self.fps_monitor_start()


Test().run()
