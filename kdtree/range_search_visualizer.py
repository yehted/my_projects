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
        print "Loading ", args.file_name
        for line in f:
            i, j = line.split()
            i = float(i)
            j = float(j)
            p = point.Point2D(i,j)
            brute.add(p)
            kdtree.add(p)

    print "Finished Loading Points"

def get_rect():
    p = win.getMouse()
    x0 = p.getX()
    y0 = p.getY()
    q = win.getMouse()
    x1 = q.getX()
    y1 = q.getY()

    a0 = min(x0,x1)
    b0 = min(y0,y1)
    a1 = max(x0,x1)
    b1 = max(y0,y1)

    return point.RectHV(a0,b0,a1,b1)

def draw_rect(query_rect):
    query_draw_rect = gr.Rectangle(
        gr.Point(query_rect.xmin, query_rect.ymin),
        gr.Point(query_rect.xmax, query_rect.ymax))
    query_draw_rect.setOutline('green')
    query_draw_rect.draw(win)
    win.update()
    return query_draw_rect

def undraw_rect(rect):
    rect.undraw()
    win.update()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    args = parser.parse_args()

    # Load points from file
    load_data(args)

    # Draw points
    brute.draw(win)
    win.update()

    # Get rectangle from user input
    query_rect = get_rect()
    qrd = draw_rect(query_rect)

    while True:
        # Get and draw points for brute force
        b = brute_range(query_rect)
        bp = draw_points(b, 'red', .008)

        # Get and draw points for kdtree
        k = kdtree_range(query_rect)
        kp = draw_points(k, 'blue', .006)

        # Clear screen on mouse click
        win.getMouse()
        undraw_points(bp)
        undraw_points(kp)
        undraw_rect(qrd)

        # Get next rectangle
        query_rect = get_rect()
        qrd = draw_rect(query_rect)

    # win.getMouse()

def brute_range(query_rect):
    return brute.range(query_rect)

def kdtree_range(query_rect):
    return kdtree.range(query_rect)

def draw_points(pointset, color, size):
    p_set = []
    for p in pointset:
        point = gr.Circle(gr.Point(p.x(), p.y()), size)
        point.setFill(color)
        point.setOutline(color)
        point.draw(win)
        p_set.append(point)

    win.update()
    return p_set

def undraw_points(pointset):
    for p in pointset:
        p.undraw()
    win.update()

if __name__ == '__main__':
    main()