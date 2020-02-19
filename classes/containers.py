from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty

from .base_blocks import BaseBlock
from .docker_client import DockerClient
from .dynamic_cols_grid_layout import DynamicColsGridLayout


class ContainersLayout(DynamicColsGridLayout):
    """ This is a base layout for ContainerBlock.
    Controls play/pause dispath docker client
    on each ContainerBlock.
    """
    cols = 7
    min_columns = NumericProperty(1)
    max_columns = NumericProperty(7)
    def pause_events(self):
        """This is a method for pause
        events on each container
        """
        for i in self.children:
            if hasattr(i, 'update_event'):
                i.update_event.cancel()

    def start_events(self):
        """This is a method for start
        events on each container
        """
        for i in self.children:
            if hasattr(i, 'update_event'):
                i.update_event()

    def __init__(self, **kwargs):
        super(ContainersLayout, self).__init__(**kwargs)
        docker = DockerClient.conn
        containers = docker.containers.list('all')
        for c in containers:
            cont = ContainerBlock(c, docker)
            self.add_widget(cont)

class ContainerBlock(BaseBlock):
    """This is a class for ui docker container.
    Contains base information about container like
    name, status, and others

    Arguments:
        container (Container): Docker-container
        docker_conn (DockerClient): Docker client.
    """
    image_path = ''
    exited_icon = StringProperty('images/stop.png')
    active_icon = StringProperty('images/play.png')

    def __init__(self, container, docker_conn, **kwargs):
        self.docker_conn = docker_conn
        self.container = container
        self.label_name = self.container.name
        self.set_image_path()
        self.update_event = Clock.schedule_interval(self._update_container, 1/30)
        self.update_event.cancel()
        super(ContainerBlock, self).__init__(**kwargs)


    def _update_container(self):
        """ This is a method for update
        container state. Dispatch docker client and
        get current state. If state not eql with saved
        then updates saved container, and reload image.
        """
        curr_cont = self.docker_conn.containers.get(self.container.name)
        if self.container.status != curr_cont.status:
            self.container = curr_cont
            self.__set_image_path()
            image = self.ids.block_image
            image.source = self.image_path
            image.reload()

    def __set_image_path(self):
        """This is a method for select image by
        container status.
        """
        if self.container.status != 'running':
            self.image_path = self.exited_icon
        else:
            self.image_path = self.active_icon
