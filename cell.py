
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value += 1

    def set_sketched_value(self, value):
        if self.value == 1:
            pass  # graphic for 1
        # ...
        else:
            pass # no graphic

        def draw(self):
            pass
            # if mouse coordinate is from (self.col * cellsize, self.row * cellsize) to ((self.col + 1) * cellsize, (self.row + 1) * cellsize)
                # color: red
            # else
                # color: black

            # starting point (horrizontal lines)
                # (self.row + i) * cellsize, self.col * cellsize
                # i = 0,1
                # color
            # ending point
                # (self.row + i) * cellsize, (self.col + 1) * cellsize
                # i = 0,1
                # color

            # starting point (vertical lines)
                # self.row * cellsize, (self.col + i) * cellsize
                # i = 0,1
                # color
            # ending point
                # (self.row + 1) * cellsize, (self.col + i) * cellsize
                # i = 0,1
                # color

            # Graphic (if self.value != 0)
                # x coordinate
                    # self.col * cellsize + cellsize // 2
                # y coordinate
                    # self.row * cellsize + cellsize // 2
