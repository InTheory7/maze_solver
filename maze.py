from cell import Cell
from time import sleep

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x,cell_size_y,win=None):
        if (num_rows < 1) or (num_cols < 1):
            raise ValueError("Invalid number of rows or columns")
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        # Initialize the maze of cells:
        self._cells = []
        if (self._num_rows == 0) or (self._num_cols == 0):
            return
        # Populate the maze with default cells:
        for col in range(0,self._num_cols):
            row_of_cells = []
            for row in range(0,self._num_rows):
                row_of_cells.append(Cell(self._win))
            self._cells.append(row_of_cells)
        # Draw each cell:
        for col in range(0,self._num_cols):
            for row in range(0,self._num_rows):
                self._draw_cell(col, row)
        
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        # Cell class draw() method requires x-y
            # co-ords of tl and br corners:
        tl_x = self._x1 + (i * self._cell_size_x)
        tl_y = self._y1 + (j * self._cell_size_y)
        br_x = self._x1 + ((i+1) * self._cell_size_x)
        br_y = self._y1 + ((j+1) * self._cell_size_y)
        # Draw the cell:
        self._cells[i][j].draw(tl_x,tl_y,br_x,br_y)
        # Call the animate cell:
        self._animate()

    def _animate(self):
        # Redraw the window and wait a fraction of a second before moving on:
        self._win.redraw()
        sleep(0.05)

