from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout


class DynamicColsGridLayout(GridLayout):
    """This is a class based on GridLayout.
    Has dynamic width. Children must has the same
    width.
    On each redraw this layout calculate how much
    elements can contains in row
    and reassign self.cols (property from
    parent GridLayout class)
    """
    min_columns = NumericProperty(2)
    max_columns = NumericProperty(1)

    def __child_width(self, child):
        """This is a function for get
        child width

        Parameters:
            child (Widget): Child must has width property

        Returns:
            Int: Width of children
        """
        if hasattr(child, 'width'):
            return child.width
        else:
            return 0

    def __children_width(self, children):
        """This is a function for return sum of
        widths all children
        Call for each children __child_width function

        Parameters:
            children (list): List contains obj

        Returns:
            Int: Sum of result __child_width methods
        """
        return sum(list(map(self.__child_width, children)))

    def __calc_row_width(self, children):
        """This is a function for calculate
        row width given the width of children and
        elements spacing.

        Parameters:
            children (list): children

        Returns:
            Int: Sum width children and spacings
        """
        spacing = sum(self.spacing) + self.spacing[0]
        width = self.__children_width(children)
        return width + spacing

    def do_layout(self, *args):
        self.cols = self.__recalculate_columns()
        super(DynamicColsGridLayout, self).do_layout(*args)

    def __recalculate_columns(self):
        """This is function for calculate
        how much elements can contains in one row

        Returns:
            Int: columns
        """
        if len(self.children) == 0:
            return 1

        columns = self.cols
        children_row = self.children[0:columns]
        cell_width = self.children[0].width
        width = self.width
        row_width = self.__children_width(children_row)
        if (width < row_width) & (columns > self.min_columns):
            while width < row_width:
                if (columns-1) < self.min_columns:
                    break
                else:
                    columns -= 1
                    children_row = self.children[0:columns]
                    row_width = self.__calc_row_width(children_row)
        elif (width > (row_width + cell_width)) & (columns < self.max_columns):
            while width > row_width:
                if (columns + 1) > self.max_columns:
                    break
                else:
                    columns += 1
                    children_row = self.children[0:columns]
                    row_width = self.__calc_row_width(children_row)

        return columns
