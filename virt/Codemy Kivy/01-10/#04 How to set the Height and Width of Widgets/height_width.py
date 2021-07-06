import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayot(GridLayout):
    #Initialize infinite keywords
    def __init__(self, **kwargs):
        #Call grid layout constructor
        super(MyGridLayot, self).__init__(**kwargs)

        #set columns
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 100

        #Create a secondary grid layout
        self.top_grid = GridLayout(row_force_default = True,
                                   row_default_height = 40,
                                   col_force_default = True,
                                   col_default_width = 100)
        self.top_grid.cols = 2

        #Add new top_grid to the App
        self.add_widget(self.top_grid)

        #Adding widgets:

        #Add Name Label
        self.top_grid.add_widget(Label(text="Name: "))

        #Add Name Input Box
        self.name = TextInput(multiline = False)
        self.top_grid.add_widget(self.name)

        #Add Pizza Label
        self.top_grid.add_widget(Label(text = "Favorite Pizza: "))

        #Add Pizza Input Box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        #Add Color Label
        self.top_grid.add_widget(Label(text = "Favorite Color: "))

        #Add Color Input Box
        self.color = TextInput(multiline = False)
        self.top_grid.add_widget(self.color)

        #Create a Submit Button
        self.submit = Button(text="Submit",
                             font_size=32,
                             size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=200)
        #Bind the button
        self.submit.bind(on_press=self.press) #the press function will be defined
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        #print(f"hello {name}, you like {pizza} pizza, and your favorite color is {color}!")
        self.add_widget(Label(text = f"hello {name}, you like {pizza} pizza, and your favorite color is {color}!"))

        #clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayot()

if __name__ == "__main__":
    MyApp().run()