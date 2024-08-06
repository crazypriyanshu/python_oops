import numpy as np
class Point:
    '''
    A point located at (x, y) in a 2D-space
    '''
    def __init__(self, x, y, payload):
        self.x = x
        self.y = y
        self.payload = payload
    def __repr__(self):
        return '{}: {}'.format(str((self.x, self.y)), repr(self.payload))
    def __str__(self):
        return 'P({:.2f}, {:.2f})'.format(self.x, self.y)
    def distance_to(self, other):
        try:
            other_x, other_y = other.x, other.y
        except AttributeError:
            other_x, other_y = other
        return np.hypot(self.x - other_x, self.y - other_y)

class Rectangle:
    '''
    A rectangle is centered at (cx, cy) in a 2D-space with width w and height h
    '''
    def __init__(self, cx, cy, w, h):
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h
        self.westEdge = cx - w / 2
        self.eastEdge = cx + w / 2
        self.northEdge = cy + h / 2
        self.southEdge = cy - h / 2

    def __repr__(self):
        return str((self.westEdge, self.eastEdge, self.northEdge,
                    self.southEdge))

    def __str__(self):
        return 'P({:.2f}, {:.2f}, {:.2f}, {:.2f})'.format(self.westEdge, self.northEdge, self.eastEdge, self.southEdge)

    def contains(self, point):
        '''
        is this point (x, y) inside the rectangle?
        :param point:
        :return:
        '''
        try:
            point_x, point_y = point.x, point.y
        except AttributeError:
            point_x, point_y = point
        return (self.westEdge <= point_x < self.eastEdge and
                self.northEdge <= point_y < self.southEdge)

    def intersects(self, other):
        '''
        Does Rect object other interesect this Rect?
        :param other:
        :return:
        '''
        return not (other.westEdge > self.eastEdge)