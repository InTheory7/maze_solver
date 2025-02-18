from point_and_line import Point, Line

class Cell:
    def __init__(self, win):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        # Create lines associated with each wall and draw them:
        tl = Point(self._x1,self._y1)
        tr = Point(self._x2,self._y1)
        br = Point(self._x2,self._y2)
        bl = Point(self._x1,self._y2)
        if self.left_wall:
            left_line = Line(bl,tl)
            self._win.draw_line(left_line,"black")
        if self.top_wall:
            top_line = Line(tl,tr)
            self._win.draw_line(top_line,"black")
        if self.right_wall:
            right_line = Line(tr,br)
            self._win.draw_line(right_line,"black")
        if self.bottom_wall:
            bottom_line = Line(br,bl)
            self._win.draw_line(bottom_line,"black")
        