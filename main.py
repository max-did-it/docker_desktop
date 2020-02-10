from kivy.app import App
from kivy.properties import (NumericProperty, StringProperty)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
import classes.buttons
import classes.containers
from classes.screens import (WorkspaceManager, SettingScreen, ImageScreen,
                             ComposeScreen, ContainerScreen)


class DockerWorkspace(BoxLayout):
    pass


class DockerDesktopApp(App):
    def build(self):
        return DockerWorkspace()


if __name__ == "__main__":
    DockerDesktopApp().run()
