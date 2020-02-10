from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition


class WorkspaceManager(ScreenManager):
    def __init__(self, **kwargs):
        self.transition = SwapTransition()
        super(WorkspaceManager, self).__init__(**kwargs)


class ImageScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'IMAGES'
        super(ImageScreen, self).__init__(**kwargs)


class ContainerScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'CONTAINERS'
        super(ContainerScreen, self).__init__(**kwargs)


class SettingScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'SETTINGS'
        super(SettingScreen, self).__init__(**kwargs)


class ComposeScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'DOCKER-COMPOSES'
        super(ComposeScreen, self).__init__(**kwargs)