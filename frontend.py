from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

# потыкалась с кнопками и цветом, пока не ясно, как с этим всем работать

Window.size = (700, 600)
Window.clearcolor = (.96, 1, .88, 1)

Config.set('graphics', 'resizable', '0')


class BookListApp(App):
    def build(self):
        gl = GridLayout(rows=1, cols=5, row_force_default=True, row_default_height=60, spacing=[10], padding=[20])
        gl.add_widget(Button(text='Добавить запись',
                      font_size=10, background_color=[.56, .55, .81, 1], background_normal=''))
        gl.add_widget(Button(text='Удалить запись',
                      font_size=10, background_color=[.56, .55, .81, 1], background_normal=''))
        gl.add_widget(Button(text='Поиск по записям',
                      font_size=10, background_color=[.56, .55, .81, 1], background_normal=''))
        gl.add_widget(Button(text='Сохранить файл',
                      font_size=10, background_color=[.56, .55, .81, 1], background_normal=''))
        gl.add_widget(Button(text='Загрузить файл',
                      font_size=10, background_color=[.56, .55, .81, 1], background_normal=''))
        return gl


if __name__ == '__main__':
    BookListApp().run()
