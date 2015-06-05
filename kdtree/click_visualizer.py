import point_set
import point
import argparse
import graphics as gr

size = 1024
win = gr.GraphWin("Points", size, size)
win.setCoords(-0.1,-0.1,1.1,1.1)

kdtree = point_set.KdTree()

def main():

    while True:
        p = win.getMouse()
        point_p = point.Point2D(p.getX(), p.getY())
        draw_point = gr.Circle(p, 0.004)
        draw_point.setFill('black')
        draw_point.draw(win)
        kdtree.add(point_p)
        kdtree.draw(win)

if __name__ == '__main__':
    main()