from window_class import Window
from point_and_line import Point, Line
from cell import Cell

def main():
    # Create window
    win = Window(800, 600)

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
    pt1 = Point(10,10)
    pt2 = Point(110,10)
    pt3 = Point(210,10)
    pt4 = Point(10,110)
    pt5 = Point(110,110)
    pt6 = Point(210,110)
    pt7 = Point(10,210)
    pt8 = Point(110,210)
    pt9 = Point(210,210)

    cell1 = Cell(pt1,pt5,win)
    cell1.bottom_wall = False
    cell2 = Cell(pt5,pt9,win)
    cell2.top_wall = False
    cell2.left_wall = False
    cell1.draw()
    cell2.draw()

    # Wait for window to close
    win.wait_for_close()

main()