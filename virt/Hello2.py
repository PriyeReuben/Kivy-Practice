# File name: hello2.py
import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.filechooser import FileChooser

class Hello2App(App):
    def build(self):
        return Label()

if __name__=="__main__":
    Hello2App().run()
