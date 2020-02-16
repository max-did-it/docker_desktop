from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout


class DynamicColsGridLayout(GridLayout):
    min_columns = NumericProperty(2)
    max_columns = NumericProperty(1)

    def child_width(self, child):
        return child.width
    def children_width(self, children):
        return sum(list(map(self.child_width, children)))

    def calc_row_width(self, children):
        spacing = sum(self.spacing) + self.spacing[0]
        width = self.children_width(children)
        return width + spacing

    def do_layout(self, *args):
        # ch_size = self.child_width(children[0])
        self.cols = self.recalculate_columns()
        super(DynamicColsGridLayout, self).do_layout(*args)

    def recalculate_columns(self):
        if len(self.children) == 0:
            return 1

        columns = self.cols
        children_row = self.children[0:columns]
        cell_width = self.children[0].width
        width = self.width
        row_width = self.children_width(children_row)
        if (width < row_width) & (columns > self.min_columns):
            while width < row_width:
                if (columns-1) < self.min_columns:
                    break
                else:
                    columns -= 1
                    children_row = self.children[0:columns]
                    row_width = self.calc_row_width(children_row)
        elif (width > (row_width + cell_width)) & (columns < self.max_columns):
            while width > row_width:
                if (columns + 1) > self.max_columns:
                    break
                else:
                    columns += 1
                    children_row = self.children[0:columns]
                    row_width = self.calc_row_width(children_row)

        return columns
