from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        main_layout = StackLayout()
        checkbox1 = CheckBox(size_hint = (0.1, 0.1), group = 'group1', active = True)
        label1 = Label(text = checkbox1.state, size_hint = (0.1, 0.1))

        def checkbox1_solution(instance, value):
            if value:
                label1.text = 'down'
            else:
                label1.text = 'normal'

        checkbox1.bind(active = checkbox1_solution)
        main_layout.add_widget(checkbox1)
        main_layout.add_widget(label1)

        return main_layout

if __name__ == '__main__':
    MyApp().run()