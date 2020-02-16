from kivy.uix.togglebutton import ToggleButton


class MenuButton(ToggleButton):
    """This is a class for menu button
    """
    def select_workspace(self, app):
        """ This is a method used for callback
        when button change self state.
        If button state is down it means
        what button pressed and we change current
        screen, through workspace manager, on screen
        """
        if not(not(app.root)) & (self.state == 'down'):
            workspace_manager = app.root.ids.workspace_manager
            workspace_manager.current = self.text
