from kivy.uix.togglebutton import ToggleButton


class MenuButton(ToggleButton):
    def select_workspace(self, root):
        if self.state == 'down':
            workspace_manager = root.ids.workspace_manager
            workspace_manager.current = self.text
