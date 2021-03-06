from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
class BaseBlock(BoxLayout):
    """This is a class for base ui Blocks
    Base settings do this class like rectangle block
    Kv contains image block and label for more information
    about object.
    """
    max_x = NumericProperty(200)
    max_y = NumericProperty(100)
    min_x = NumericProperty(int(200*0.7))
    min_y = NumericProperty(int(100*0.7))
    s_hint_max = ReferenceListProperty(max_x, max_y)
    s_hint_min = ReferenceListProperty(min_x, min_y)
    image_path = 'images/base_block.png'

    def __init__(self, label_name='', **kwargs):
        if not hasattr(self, 'label_name'):
            self.label_name = label_name
        self.label_name_full = self.label_name
        if len(self.label_name) >= 10:
            self.label_name = self.label_name[0:10] + '...'
        self.bg_color = (0.27, 0.27, 0.27, 1)
        super(BaseBlock, self).__init__(**kwargs)

    def image_click_event(self, *args, **kwargs):
        pass

            
class BaseBlockImage(ButtonBehavior, Image):
    def on_press(self):
        if hasattr(self.parent.parent, 'on_image_click'):
            self.parent.parent.on_image_click()
