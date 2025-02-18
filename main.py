from window_class import Window
from point_and_line import Point, Line

def main():
    # Create window
    win = Window(800, 600)

    # Draw some lines:
    pt1 = Point(100,150)
    pt2 = Point(150,30)
    pt3 = Point(50,200)

    line1 = Line(pt1,pt2)
    line2 = Line(pt2,pt3)
    line3 = Line(pt3,pt1)

    win.draw_line(line1,"black")
    win.draw_line(line2,"red")
    win.draw_line(line3,"green")

    # Wait for window to close
    win.wait_for_close()

main()