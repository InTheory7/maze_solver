from window_class import Window
from point_and_line import Point, Line
from cell import Cell
from maze import Maze

def main():
    # Create window
    win = Window(1024,720)

    # Draw some lines:
    # pt1 = Point(100,150)
    # pt2 = Point(150,30)
    # pt3 = Point(50,200)
    # 
    # line1 = Line(pt1,pt2)
    # line2 = Line(pt2,pt3)
    # line3 = Line(pt3,pt1)
    # 
    # win.draw_line(line1,"black")
    # win.draw_line(line2,"red")
    # win.draw_line(line3,"green")

    # Draw some cells:
    # x1, y1 = (10, 10)
    # x2, y2 = (110,110)
    # x3, y3 = (210,210)
    # 
    # cell1 = Cell(win)
    # cell1.bottom_wall = False
    # cell2 = Cell(win)
    # cell2.top_wall = False
    # cell2.left_wall = False
    # cell1.draw(x1, y1, x2, y2)
    # cell2.draw(x2, y2, x3, y3)
    # 
    # # Draw a line between the two cells:
    # # cell1.draw_move(cell2)        # Red
    # cell1.draw_move(cell2, True)    # Grey
     
    # Create a maze:
    x1, y1 = (10,10)
    num_rows = 15
    num_cols = 15
    cell_size_x = 40
    cell_size_y = 40
    maze = Maze(x1, y1, num_rows, num_cols, cell_size_x,cell_size_y,win,10)
    maze.solve()

    # Wait for window to close
    win.wait_for_close()

main()