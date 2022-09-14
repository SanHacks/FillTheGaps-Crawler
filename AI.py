import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class ChatInterface(Widget):
    def __init__(self, **kwargs):
        super(ChatInterface, self).__init__(**kwargs)

        self.background_color = (0, 1, 0, 1) # green

        self. bubble = Bubble(size = (300, 200),
                              pos = (self.x, self.y),
                              text = "Hello, I'm an AI created by OpenAI. How can I help you today?",
                             )

        self.button = Button(text = "Run Script",
                              font_size = 40,
                              size_hint = (.5, .5),
                              pos = (self.x+self.width/2-self.button.width/2, self.y-50),
                              on_press = self.run_script,
                             )

        self.add_widget(self.bubble)
        self.add_widget(self.button)

    def run_script(self, instance):
        print("Running script...")

class Bubble(Widget):
    def __init__(self, **kwargs):
        super(Bubble, self).__init__(**kwargs)

        self.size = (300, 200)
        self.pos = (self.x, self.y)
        self.text = "Hello, I'm an AI created by OpenAI. How can I help you today?"

class Button(Widget):
    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)

        self.text = "Run Script"
        self.font_size = 40
        self.size_hint = (.5, .5)
        self.pos = (self.x+self.width/2-self.button.width/2, self.y-50)
        self.on_press = self.run_script

class MainApp(App):
    def build(self):
        return ChatInterface()

if __name__ == "__main__":
    MainApp().run()