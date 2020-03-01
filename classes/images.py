from kivy.properties import NumericProperty, StringProperty

from .base_blocks import BaseBlock
from .docker_client import DockerClient
from .dynamic_cols_grid_layout import DynamicColsGridLayout


class ImagesLayout(DynamicColsGridLayout):
    """Layout for group and rule ImageBlock"""
    cols = 7
    min_columns = NumericProperty(1)
    max_columns = NumericProperty(7)

    def __init__(self, **kwargs):
        super(ImagesLayout, self).__init__(**kwargs)
        docker = DockerClient.conn
        images = docker.images.list()
        for i in images:
            img_wgt = ImageBlock(i, docker)
            self.add_widget(img_wgt)

class ImageBlock(BaseBlock):
    """This is a class for ui Docker Image enitity.
     Contains base information about image like:
     name, tag, owner and others
    """
    image_path = StringProperty('images/image.png')
    def __init__(self, image, docker_conn, **kwargs):
        self.docker_conn = docker_conn
        self.image = image
        self.label_name = self.__prepare_name(image)
        super(ImageBlock, self).__init__(**kwargs)

    def __prepare_name(self, image):
        """ This is a function for generate
        block label, from tag or short_id

        Arguments:
            image (Image): image first tag

        Returns:
            name (string): image name
        """
        if len(image.tags) > 0:
            return image.tags[0].split('/')[-1].split(':')[0]
        else:
            return image.short_id
