from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('box.kv') #designates the .kv file to be used.
#Builder.load_string(""" kivy design file goes here""") #this is not reccommended.  Yes, 3 quotation marks.

class MyLayout(Widget):
    pass



class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()

