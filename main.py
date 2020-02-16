import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


kivy_dir = 'kivy_files/'
kvs = list(map(lambda el: kivy_dir + el, os.listdir(kivy_dir)))
for kv in kvs:
    Builder.load_file(kv)

class DockerWorkspace(BoxLayout):
    pass

class DockerDesktopApp(App):
    def build(self):
        return DockerWorkspace()


if __name__ == "__main__":
    DockerDesktopApp().run()
