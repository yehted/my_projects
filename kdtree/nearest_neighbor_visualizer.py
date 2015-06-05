import point_set
import point
import argparse
import graphics as gr
import timeit

size = 1024
win = gr.GraphWin("Points", size, size, autoflush=False)
win.setCoords(-0.1,-0.1,1.1,1.1)

brute = point_set.PointSet()
kdtree = point_set.KdTree()

def load_data(args):
    with open(args.file_name, 'r') as f:
        for line in f:
            i, j = line.split()
            i = float(i)
            j = float(j)
            p = point.Point2D(i,j)
            brute.add(p)
            kdtree.add(p)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    args = parser.parse_args()

    # Load data points from file
    print "Loading", args.file_name
    load_data(args)
    print "Finished Loading Points"

    # Draw points
    brute.draw(win)
    win.update()

    # Visualize nearest neighbor calculation
    visualize()

def visualize():
    p = win.getMouse()
    brute_dot = gr.Circle(gr.Point(0,0),0)
    kdtree_dot = gr.Circle(gr.Point(0,0),0)
    query_dot = gr.Circle(gr.Point(0,0),0)

    while True:
        query_dot.undraw()
        brute_dot.undraw()
        kdtree_dot.undraw()

        query_point = point.Point2D(p.getX(), p.getY())
        query_dot = gr.Circle(gr.Point(query_point.x(), query_point.y()), 0.003)
        query_dot.setFill('green')
        query_dot.setOutline('green')
        query_dot.draw(win)

        brute_point = brute.nearest(query_point)
        brute_dot = gr.Circle(gr.Point(brute_point.x(), brute_point.y()), 0.008)
        brute_dot.setFill('red')
        brute_dot.setOutline('red')
        brute_dot.draw(win)

        kdtree_point = kdtree.nearest(query_point)
        kdtree_dot = gr.Circle(gr.Point(kdtree_point.x(), kdtree_point.y()), 0.006)
        kdtree_dot.setFill('blue')
        kdtree_dot.setOutline('blue')
        kdtree_dot.draw(win)

        win.update()

        p = win.getMouse()

if __name__ == '__main__':
    main()