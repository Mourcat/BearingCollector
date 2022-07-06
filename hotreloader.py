"""
HotReloader
-----------
Uses kaki module for Hot Reload (limited to some uses cases).
Before using, install kaki by `pip install kaki`

"""


import os
import platform
import sys

root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "libs", "applibs"))

from kaki.app import App as HotReloaderApp  # NOQA: E402
from kivy.logger import LOG_LEVELS, Logger  # NOQA: E402

Logger.setLevel(LOG_LEVELS["debug"])

from kivy.core.window import Window  # NOQA: E402
from kivymd.app import MDApp  # NOQA: E402

from libs.uix.baseclass.root import Root  # NOQA: E402

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

KV_FOLDER = os.path.join(os.getcwd(), "libs", "uix", "kv")


class BearingCollector(MDApp, HotReloaderApp): 
    DEBUG = 1  # To enable Hot Reload

    # *.kv files to watch
    KV_FILES = [os.path.join(KV_FOLDER, i) for i in os.listdir(KV_FOLDER)]

    # Class to watch from *.py files
    # You need to register the *.py files in libs/uix/baseclass/*.py
    CLASSES = {'Root': 'libs.uix.baseclass.root', 'HomeScreen': 'libs.uix.baseclass.home_screen', 'ContentNavigationDrawer': 'libs.uix.baseclass.content_nav_drawer'} 

    # Auto Reloader Path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def __init__(self, **kwargs):
        super(BearingCollectorUi, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "BearingCollector"

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "300"

        self.theme_cls.accent_palette = "Red"
        self.theme_cls.accent_hue = "300"

        self.theme_cls.theme_style = "Dark"

    def build_app(self):  # build_app works like build method
        return Root()


if __name__ == "__main__":
    BearingCollector().run()
