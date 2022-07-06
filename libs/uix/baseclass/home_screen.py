from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivymd.uix.screen import MDScreen
from PyPDF2 import PdfReader
import os
from libs.uix.baseclass.text_page import TextPage


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
    
    
class HomeScreen(MDScreen):
    text_input = ObjectProperty(None)
    file_opened = StringProperty()
    pages = []

    def dismiss_popup(self):
        self._popup.dismiss()
        
    def load(self, path, filename):
        if filename[0].endswith('.txt'):
            with open(os.path.join(path, filename[0])) as stream:
                self.text_input.text = stream.read()
        elif filename[0].endswith('.pdf'):
            reader = PdfReader(filename[0])
            self.pages = reader.pages
            text = self.pages[self.text_input.page_number].extract_text().strip()
            self.text_input.text = text.replace('\n', ' ')
        self.dismiss_popup()
        self.file_opened = filename[0].split("/")[-1]
        self.ids.info_lbl.text = f'{self.file_opened} {self.text_input.page_number+1}/{len(self.pages)}'
        self.text_input.ids.grid.opacity = .7

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(.9, .9))
        self._popup.open()
    
    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)
            self.dismiss_popup()
            
    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content, size_hint=(.9, .9))
        self._popup.open()