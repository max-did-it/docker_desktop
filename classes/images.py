from kivy.properties import NumericProperty, StringProperty

from .base_blocks import BaseBlock
from .docker_client import DockerClient
from .dynamic_cols_grid_layout import DynamicColsGridLayout


class ImagesLayout(DynamicColsGridLayout):
    cols = 7
    min_columns = NumericProperty(1)
    max_columns = NumericProperty(7)

    def __init__(self, **kwargs):
        super(ImagesLayout, self).__init__(**kwargs)
        images = DockerClient.conn.images.list()
        for image in images:
            if len(image.tags) > 0:
                text = image.tags[0]
                if not text.find('/') == -1:
                    names_list = text.split('/')
                    if len(names_list) > 2:
                        image_name = names_list[-1]
                    else:
                        image_name = names_list[1]

                    name, _ = image_name.split(':')
                    text = name
            else:
                text = "Nobody"
            container = ImageBlock(label_name=text)
            self.add_widget(container)


class ImageBlock(BaseBlock):
    image_path = StringProperty('images/image.png')
