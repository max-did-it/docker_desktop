from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


class WorkspaceManager(ScreenManager):
    """ Contains all application screens
    located in the work area.
    """
    def __init__(self, **kwargs):
        kwargs['transition'] = NoTransition()
        super(WorkspaceManager, self).__init__(**kwargs)


class ImageScreen(Screen):
    """ contain image layout """
    def __init__(self, **kwargs):
        self.name = 'IMAGES'
        super(ImageScreen, self).__init__(**kwargs)


class ContainerScreen(Screen):
    """ contain container layout"""
    def __init__(self, **kwargs):
        self.name = 'CONTAINERS'
        super(ContainerScreen, self).__init__(**kwargs)

    def pause_events(self):
        """ proxy method pause events
        on container layout
        """
        self.children[0].children[0].pause_events()

    def start_events(self):
        """ proxy method start events
        on container layout
        """
        self.children[0].children[0].start_events()

class SettingScreen(Screen):
    """ screen contains settings layout """
    def __init__(self, **kwargs):
        self.name = 'SETTINGS'
        super(SettingScreen, self).__init__(**kwargs)


class ComposeScreen(Screen):
    """ screen contains compose layout (Docker-Compose)"""
    def __init__(self, **kwargs):
        self.name = 'DOCKER-COMPOSES'
        super(ComposeScreen, self).__init__(**kwargs)
