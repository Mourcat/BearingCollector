import os
import platform
from kivy.core.window import Window
from kivymd.app import MDApp
from libs.uix.baseclass.root import Root

if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


class BearingCollector(MDApp): 

    def __init__(self, **kwargs):
        super(BearingCollector, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "Bearing Collector"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "300"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.accent_hue = "300"
        self.theme_cls.theme_style = "Dark"

    def build(self):
        return Root()
        
    def on_start(self):
        print('Started..')