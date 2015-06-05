import point_set
import point
import argparse
import random
import numpy as np
from scipy.spatial import cKDTree
import timeit

brute = point_set.PointSet()
kdtree = point_set.KdTree()

def load_kdtree_data(args):
    with open(args.file_name, 'r') as f:
        for line in f:
            i, j = line.split()
            i = float(i)
            j = float(j)
            p = point.Point2D(i,j)
            kdtree.add(p)

def load_brute_data(args):
    with open(args.file_name, 'r') as f:
        for line in f:
            i, j = line.split()
            i = float(i)
            j = float(j)
            p = point.Point2D(i,j)
            brute.add(p)

def load_data_using_numpy(args):
    arr = np.loadtxt(args.file_name)
    return arr

def load_data_using_scipy(args):
    arr = np.loadtxt(args.file_name)
    tree = cKDTree(arr)
    return tree

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help='File to load')
    parser.add_argument("repeat", help='number of repeats')
    parser.add_argument("trials", help='number of trials per repeat')
    args = parser.parse_args()

    repeat = int(args.repeat)
    number = int(args.trials)

    # Time numpy
    # print "Loading into numpy", args.file_name
    # arr = load_data_using_numpy(args)
    # print "Finished Loading Points"
    # print "-------------------------------------------------"
    # print "Testing numpy with {} repeats of {} trials".format(repeat, number)
    # timer = timeit.Timer(lambda: find_numpy(arr))
    # result = timer.repeat(repeat=repeat, number=number)
    # print result

    # Time brute force
    # print "Loading into point_set PointSet", args.file_name
    # load_brute_data(args)
    # print "Finished Loading Points"
    # print "Testing set with {} repeats of {} trials".format(repeat, number)
    # timer = timeit.Timer(lambda: find_brute())
    # result = timer.repeat(repeat=repeat, number=number)
    # print result

    # Time kdtree
    # print "Loading into point_set KdTree", args.file_name
    # load_kdtree_data(args)
    # print "Finished Loading Points"
    # print "-------------------------------------------------"
    # print "Testing kdtree with {} repeats of {} trials".format(repeat, number)
    # timer = timeit.Timer(lambda: find_kdtree())
    # result = timer.repeat(repeat=repeat, number=number)
    # print result

    # Time SciPy KDTree
    print "Loading into scipy tree", args.file_name
    tree = load_data_using_scipy(args)
    print "Finished Loading Points"
    print "-------------------------------------------------"
    print "Testing cKDTree with {} repeats of {} trials".format(repeat, number)
    timer = timeit.Timer(lambda: find_scipy(tree))
    result = timer.repeat(repeat=repeat, number=number)
    print result


def find_brute():
    query_point = get_random_point()
    return brute.nearest(query_point)

def find_kdtree():
    query_point = get_random_point()
    return kdtree.nearest(query_point)

def find_numpy(arr):
    x = random.random()
    y = random.random()
    d = (arr[:,0]-x)**2 + (arr[:,1]-y)**2
    return arr[d.argmin()]

def find_scipy(tree):
    x = random.random()
    y = random.random()
    return tree.query([x, y], p=2)

def get_random_point():
    x = random.random()
    y = random.random()
    return point.Point2D(x, y)

if __name__ == '__main__':
    main()