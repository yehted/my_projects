from math import sqrt
import graphics as gr

class Point2D(object):
    """ Implementation of a 2D point object which compares points by y-
    coordinate and breaks ties by x-coordinate
    """

    def __init__(self, x, y):
        self.p = (x, y)

    def __repr__(self):
        return self.p.__repr__()

    def __hash__(self):
        return self.p.__hash__()

    def x(self):
        return self.p[0]

    def y(self):
        return self.p[1]

    def distance_squared_to(self, other):
        dx = self.x() - other.x()
        dy = self.y() - other.y()
        return (dx*dx + dy*dy)

    def distance_to(self, other):
        return sqrt(self.distance_squared_to(other))

    def __cmp__(self, other):
        if self.y() < other.y():
            return -1
        if self.y() > other.y():
            return 1
        if self.x() < other.x():
            return -1
        if self.x() > other.x():
            return 1
        return 0

    def draw(self):
        p = gr.Circle(gr.Point(self.x(), self.y()), 0.004)
        p.setFill('black')
        return p


class RectHV(object):
    """Implementation of a 2D axis-aligned rectangles"""

    def __init__(self, xmin, ymin, xmax, ymax):
        if (xmin > xmax or ymin > ymax):
            raise ValueError("Invalid Rectangle")

        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def width(self):
        return self.xmax - self.xmin

    def height(self):
        return self.ymax - self.ymin

    def intersects(self, other):
        return self.xmax >= other.xmin and self.ymax >= other.ymin and \
            other.xmax >= self.xmin and other.ymax >= self.ymin

    def distance_squared_to(self, p):
        """Distance squared from p to the closest point on the rectangle"""
        dx = 0.0
        dy = 0.0
        if   p.x() < self.xmin:
            dx = p.x() - self.xmin
        elif p.x() > self.xmax:
            dx = p.x() - self.xmax

        if   p.y() < self.ymin:
            dy = p.y() - self.ymin
        elif p.y() > self.ymax:
            dy = p.y() - self.ymax

        return dx*dx + dy*dy

    def distance_to(self, p):
        """Distance from p to the closest point on the rectangle"""
        return sqrt(self.distance_squared_to(p))

    def contains(self, p):
        """Does the rectangle contain the point p"""
        return p.x() >= self.xmin and p.x() <= self.xmax and \
            p.y() >= self.ymin and p.y() <= self.ymax

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __repr__(self):
        return ("[{x1},{y1}] x [{x2},{y2}]".format(x1=self.xmin,
            y1=self.ymin, x2=self.xmax, y2=self.ymax))

    def draw(self):
        return gr.Rectangle(gr.Point(xmin,ymin), gr.Point(xmax,ymax))