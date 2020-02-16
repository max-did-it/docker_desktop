from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty

from .base_blocks import BaseBlock
from .docker_client import DockerClient
from .dynamic_cols_grid_layout import DynamicColsGridLayout


class ContainersLayout(DynamicColsGridLayout):
    cols = 7
    min_columns = NumericProperty(1)
    max_columns = NumericProperty(7)
    def pause_events(self):
        for i in self.children:
            if hasattr(i, 'update_event'):
                i.update_event()

    def start_events(self):
        for i in self.children:
            if hasattr(i, 'update_event'):
                i.update_event.cancel()

    def __init__(self, **kwargs):
        super(ContainersLayout, self).__init__(**kwargs)
        docker = DockerClient.conn
        containers = docker.containers.list('all')
        for c in containers:
            cont = ContainerBlock(c, docker)
            self.add_widget(cont)

class ContainerBlock(BaseBlock):
    image_path = ''
    exited_icon = StringProperty('images/stop_container.png')
    active_icon = StringProperty('images/play_container.png')

    def __init__(self, container, docker_conn, **kwargs):
        self.docker_conn = docker_conn
        self.container = container
        self.label_name = self.container.name
        self.set_image_path()
        self.update_event = Clock.schedule_interval(self.update_container, 1/30)
        self.update_event.cancel()
        super(ContainerBlock, self).__init__(**kwargs)

    def update_container(self):
        curr_cont = self.docker_conn.containers.get(self.container.name)
        if self.container.status != curr_cont.status:
            self.container = curr_cont
            self.set_image_path()
            image = self.ids.block_image
            image.source = self.image_path
            image.reload()

    def set_image_path(self):
        if self.container.status != 'running':
            self.image_path = self.exited_icon
        else:
            self.image_path = self.active_icon
