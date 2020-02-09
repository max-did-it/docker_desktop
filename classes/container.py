from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty


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
