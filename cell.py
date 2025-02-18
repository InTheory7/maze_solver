from point_and_line import Point, Line

class Cell:
    def __init__(self, tl, br, win):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._x1 = tl.x
        self._y1 = tl.y
        self._x2 = br.x
        self._y2 = br.y
        self._win = win

    def draw(self):
        # Create lines associated with each wall and draw them:
        tl = Point(self._x1,self._y1)
        tr = Point(self._x2,self._y1)
        br = Point(self._x2,self._y2)
        bl = Point(self._x1,self._y2)
        if self.left_wall:
            left_line = Line(bl,tl)
            left_line.draw(self._win._canvas, "black")
        if self.top_wall:
            top_line = Line(tl,tr)
            top_line.draw(self._win._canvas, "black")
        if self.right_wall:
            right_line = Line(tr,br)
            right_line.draw(self._win._canvas, "black")
        if self.bottom_wall:
            bottom_line = Line(br,bl)
            bottom_line.draw(self._win._canvas, "black")
        