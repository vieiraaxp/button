from kivy.app import App
from kivy.uix.button import Button 

def botao_pressionado(instance):
    print("Botão pressionado")

class MyApp(App):
    def build(self):
        btn = Button(text='no coco e no relógio!!!')
        btn.bind(on_press=botao_pressionado)

        return btn
    
if __name__ == '__main__':
    MyApp().run()