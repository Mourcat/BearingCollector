from kivy.properties import NumericProperty, StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
import utils


utils.load_kv('text_page.kv')


class TextPage(MDBoxLayout):
    text = StringProperty()
    page_number = NumericProperty(0)
    
    def go_on(self, instance):
        self.page_number = int(instance.text)

    def previous_page(self):
        if self.page_number <= 0:
            self.page_number = 0
        else:
            self.page_number -= 1
        self.text = MDApp.get_running_app().root.screens[0].pages[self.page_number].extract_text()
        MDApp.get_running_app().root.screens[0].ids.info_lbl.text = f'{MDApp.get_running_app().root.screens[0].file_opened} {self.page_number+1}/{len(MDApp.get_running_app().root.screens[0].pages)}'
        self.ids.counter.text = f'{self.page_number+1}'
    
    def next_page(self):
        if self.page_number >= len(MDApp.get_running_app().root.screens[0].pages)-1:
            self.page_number = len(MDApp.get_running_app().root.screens[0].pages)-1
        else:
            self.page_number += 1
        self.text = MDApp.get_running_app().root.screens[0].pages[self.page_number].extract_text()
        MDApp.get_running_app().root.screens[0].ids.info_lbl.text = f'{MDApp.get_running_app().root.screens[0].file_opened} {self.page_number+1}/{len(MDApp.get_running_app().root.screens[0].pages)}'
        self.ids.counter.text = f'{self.page_number+1}'