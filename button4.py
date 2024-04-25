from kivy.app import App
from kivy.uix.button import Button 

class MyApp(App):
    def build(self):
        return Button(text='cuida pai', size_hint=(0.5, 0.2))
    #size_hint == mudança da altura/largura do obj

if __name__ == '__main__':
    MyApp().run()  