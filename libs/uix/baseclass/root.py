import json
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
import utils


utils.load_kv("root.kv")


class Root(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.add_screens)

    def add_screens(self, interval):
        with open("screens.json") as f:
            screens = json.load(f)
        for screen_name in screens.keys():
            screen_details = screens[screen_name]
            Builder.load_file(screen_details["kv"])
            exec(screen_details["import"])
            screen_object = eval(screen_details["object"]) 
            screen_object.name = screen_name
            self.add_widget(
                screen_object
            )