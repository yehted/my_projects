from sys import maxint
import point
import graphics as gr

class PointSet(set):
    def draw(self, win):
        for p in self:
            p.draw().draw(win)

    def range(self, rect):
        result = []
        for p in self:
            if rect.contains(p):
                result.append(p)
        return result

    def nearest(self, p):
        if len(self) == 0:
            return None

        min_dist = maxint
        nearest = p
        for s in self:
            distance = p.distance_squared_to(s)
            if distance < min_dist:
                min_dist = distance
                nearest = s

        return nearest


class KdTree(object):
    class Node(object):
        def __init__(self, p, xmin, ymin, xmax, ymax):
            self.p = p
            self.rect = point.RectHV(xmin, ymin, xmax, ymax)
            self.lb = None
            self.rt = None

        def comparebyX(self, p):
            if p.x() < self.p.x():
                return -1
            if p.x() > self.p.x():
                return 1
            return 0

        def comparebyY(self, p):
            if p.y() < self.p.y():
                return -1
            if p.y() > self.p.y():
                return 1
            return 0


    def __init__(self):
        self.root = None
        self.N = 0

    def is_empty(self):
        return self.N == 0

    def __len__(self):
        return self.N

    def add(self, p):
        self.root = self.insert(self.root, p, False, 0, 0, 1, 1)
        self.N += 1

    def insert(self, node, p, h_node, xmin, ymin, xmax, ymax):
        if node is None:
            return KdTree.Node(p, xmin, ymin, xmax, ymax)

        # Determine if vertical or horizontal split
        if not h_node:
            compare = node.comparebyX(p)
            edge = node.p.x()
        else:
            compare = node.comparebyY(p)
            edge = node.p.y()

        # Insert node
        if compare < 0:
            if not h_node:
                node.lb = self.insert(node.lb, p, not h_node, xmin, ymin, edge, ymax)
            else:
                node.lb = self.insert(node.lb, p, not h_node, xmin, ymin, xmax, edge)
        else:
            if p == node.p:
                self.N -= 1
            else:
                if not h_node:
                    node.rt = self.insert(node.rt, p, not h_node, edge, ymin, xmax, ymax)
                else:
                    node.rt = self.insert(node.rt, p, not h_node, xmin, edge, xmax, ymax)

        return node

    def __contains__(self, p):
        return self.get(self.root, p, False) is not None

    def get(self, node, p, h_node):
        if node is None:
            return None

        if not h_node:
            compare = node.comparebyX(p)
        else:
            compare = node.comparebyY(p)

        if compare < 0:
            return self.get(node.lb, p, not h_node)
        elif compare > 0:
            return self.get(node.rt, p, not h_node)
        else:
            if h_node:
                compare = node.comparebyX(p)
            else:
                compare = node.comparebyY(p)

            if compare == 0:
                return node
            else:
                return self.get(node.rt, p, not h_node)

    def range(self, rect):
        lst =[]
        self._range(self.root, lst, rect, False)
        return lst

    def _range(self, node, lst, rect, h_node):
        if node is None:
            return

        if rect.contains(node.p):
            lst.append(node.p)

        if not h_node:
            if rect.xmax >= node.p.x():
                self._range(node.rt, lst, rect, not h_node)
            if rect.xmin <= node.p.x():
                self._range(node.lb, lst, rect, not h_node)

        else:
            if rect.ymax >= node.p.y():
                self._range(node.rt, lst, rect, not h_node)
            if rect.ymin <= node.p.y():
                self._range(node.lb, lst, rect, not h_node)

    def nearest(self, p):
        if self.N == 0:
            return point.Point2D(0,0)

        return self._nearest(self.root, p, self.root.p, self.root.p.distance_squared_to(p), False)

    def _nearest(self, node, p, champ, d, h_node):
        if node is None:
            return champ
        if d < node.rect.distance_squared_to(p):
            return champ

        distance = node.p.distance_squared_to(p)
        if distance < d:
            d = distance
            champ = node.p

        if not h_node:
            compare = node.comparebyX(p)
        else:
            compare = node.comparebyY(p)

        rchamp = champ
        if compare < 0:
            rchamp = self._nearest(node.lb, p, champ, d, not h_node)
            rd = rchamp.distance_squared_to(p)
            if rd < d:
                champ = rchamp
                d = rd
            champ = self._nearest(node.rt, p, champ, d, not h_node)
        else:
            rchamp = self._nearest(node.rt, p, champ, d, not h_node)
            rd = rchamp.distance_squared_to(p)
            if rd < d:
                champ = rchamp
                d = rd
            champ = self._nearest(node.lb, p, champ, d, not h_node)

        return champ

    def draw(self, win):
        if self.root is not None:
            self._draw(self.root, False, win)

    def _draw(self, node, h_node, win):
        if node.lb is not None:
            self._draw(node.lb, not h_node, win)
        if node.rt is not None:
            self._draw(node.rt, not h_node, win)


        if not h_node:
            line = gr.Line(gr.Point(node.p.x(), node.rect.ymin),
                gr.Point(node.p.x(), node.rect.ymax))
            line.setOutline('red')
        else:
            line = gr.Line(gr.Point(node.rect.xmin, node.p.y()),
                gr.Point(node.rect.xmax, node.p.y()))
            line.setOutline('blue')
        line.draw(win)