import point_set
import point
import argparse
import graphics as gr

size = 1024
win = gr.GraphWin("Points", size, size)
win.setCoords(-0.1,-0.1,1.1,1.1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    args = parser.parse_args()

    with open(args.file_name, 'r') as f:
        print args.file_name
        brute = point_set.PointSet()
        kdtree = point_set.KdTree()
        for line in f.readlines():
            i, j = line.split()
            i = float(i)
            j = float(j)
            p = point.Point2D(i,j)
            brute.add(p)
            kdtree.add(p)
            p.draw().draw(win)
        kdtree.draw(win)
    raw_input()
    win.close()

if __name__ == '__main__':
    main()