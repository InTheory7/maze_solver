from cell import Cell
from time import sleep
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x,cell_size_y,win=None,seed=None):
        if (num_rows < 1) or (num_cols < 1):
            raise ValueError("Invalid number of rows or columns")
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        # Break the entrance and exit walls:
        self._break_entrance_and_exit()
        # Break internal walls to create the maze structure:
        self._break_walls_r(0,0)
        # Reset the visited property of all cells:
        self._reset_cells_visited()

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

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # Determine which cells to visit next
            # Left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i-1, j))
            # Right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i+1, j))
            # Up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j-1))
            # Down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j+1))

            # If there is nowhere to go from here:
            if len(next_index_list) == 0:
                self._draw_cell(i,j)
                return
            
            # Randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # Knock out walls between this cell and the next cell(s):
            # Right
            if next_index[0] == i + 1:
                self._cells[i][j].right_wall = False
                self._cells[i + 1][j].left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].left_wall = False
                self._cells[i - 1][j].right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].bottom_wall = False
                self._cells[i][j + 1].top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].top_wall = False
                self._cells[i][j - 1].bottom_wall = False

            # Recursively visit the next cell:
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
        