from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('whatever.kv') #designates the .kv file to be used.
#Builder.load_string(""" kivy design file goes here""") #this is not reccommended.  Yes, 3 quotation marks.

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)


    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f"hello {name}, you like {pizza} pizza, and your favorite color is {color}!")
        #self.add_widget(Label(text = f"hello {name}, you like {pizza} pizza, and your favorite color is {color}!"))

        #clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class AwesomeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    AwesomeApp().run()