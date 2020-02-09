import docker
from kivy.app import App
from kivy.properties import (NumericProperty, Property, ReferenceListProperty,
                             StringProperty)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from classes.container import Container
from classes.dynamic_cols_grid_layout import DynamicColsGridLayout


class ContainersLayout(DynamicColsGridLayout):
    cols = 7
    min_columns = NumericProperty(1)
    max_columns = NumericProperty(7)

    def __init__(self, **kwargs):
        super(ContainersLayout, self).__init__(**kwargs)
        images = DockerClient.conn.images.list()
        for image in images:
            if (len(image.tags) > 0):
                text = image.tags[0]
                if not (text.find('/') == -1):
                    names_list = text.split('/')
                    if len(names_list) > 2:
                        image_name = names_list[-1]
                    else:
                        image_name = names_list[1]

                    name, tag = image_name.split(':')
                    text = name
            else:
                text = "Nobody"
            container = StoppedContainer(container_tag=text)
            self.add_widget(container)
        


class StoppedContainer(Container):
    image_path = StringProperty('')


class ActiveContainer(Container):
    image_path = StringProperty('images/play_container.png')


class DockerWorkspace(BoxLayout):
    pass


class DockerDesktopApp(App):
    def build(self):
        return DockerWorkspace()

class DockerClient:
    conn = docker.from_env()

if __name__ == "__main__":
    DockerDesktopApp().run()
    # docker_client = docker.from_env()


# btns = []


# grid = GridLayout(cols = 10)
# btns.sort(key=lambda btn: btn.text)
# for b in btns:
#   grid.add_widget(b)

# return grid
