from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (NumericProperty, ReferenceListProperty,
                             StringProperty)
from .dynamic_cols_grid_layout import DynamicColsGridLayout
from .docker_client import DockerClient

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

                    name, _ = image_name.split(':')
                    text = name
            else:
                text = "Nobody"
            container = StoppedContainer(container_tag=text)
            self.add_widget(container)


class Container(BoxLayout):
    row = NumericProperty(0)
    column = NumericProperty(0)

    def __init__(self, container_tag='', **kwargs):
        self.image_path = 'images/stop_container.png'
        self.container_tag = container_tag
        self.bg_color = (0.27, 0.27, 0.27, 1)
        super(Container, self).__init__(**kwargs)

    def something(self):
        print('something')

    max_x = NumericProperty(200)
    max_y = NumericProperty(100)
    min_x = NumericProperty(int(200*0.7))
    min_y = NumericProperty(int(100*0.7))
    s_hint_max = ReferenceListProperty(max_x, max_y)
    s_hint_min = ReferenceListProperty(min_x, min_y)


class StoppedContainer(Container):
    image_path = StringProperty('')


class ActiveContainer(Container):
    image_path = StringProperty('images/play_container.png')
