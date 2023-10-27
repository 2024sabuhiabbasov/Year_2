class Pixel:
    def __init__(self, row: int, col: int, active: bool):
        self.row = row
        self.col = col
        self.active = active

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def __repr__(self):
        return f"Pixel ({self.row}, {self.col}, {self.active})"


class Screen:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = []
        for i in range(width):
            list_temp = []
            for j in range(height):
                pixel = Pixel(i, j, False)
                list_temp.append(pixel)
            self.grid.append(list_temp)

    def getGrid(self):
        return self.grid


screen = Screen(3, 3)
grid = screen.getGrid()
for i in range(3):
    print(grid[i])