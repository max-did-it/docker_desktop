from kivy.uix.togglebutton import ToggleButton


class MenuButton(ToggleButton):
    def select_workspace(self, app):
        if not(not(app.root)) & (self.state == 'down'):
            workspace_manager = app.root.ids.workspace_manager
            workspace_manager.current = self.text
