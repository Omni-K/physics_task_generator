"""
Генератор заданий по физике за 8-ой класс
"""
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField


class MainApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical')
        text = 'Показание вольтметра, присоединенного к горящей электрической лампе накаливания, равно 10 В, а амперметра, измеряющего силу тока в лампе, 56 А. Чему равно сопротивление лампы?'
        layout.add_widget(MDLabel(text=text))
        layout.add_widget(MDTextField())
        layout.add_widget(MDRectangleFlatButton(text='Check answer'))
        layout.add_widget(MDLabel(text=''))

        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()