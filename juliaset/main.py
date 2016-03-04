import numpy as np

import pyximport; pyximport.install()
from _julia_figure import julia_cython

def save_png(T, filename):
    from PIL import Image
    # Normalize arbitrary range to [0,1] -> color tuples -> color tuples as uint8
    # This can be saved as an image.
    normalizer = plt.Normalize(vmin=0, vmax=70)
    mapper = plt.cm.ScalarMappable(norm=normalizer, cmap=plt.cm.viridis)
    im = Image.fromarray(np.uint8(mapper.to_rgba(T)*255))
    im.save(filename)

if __name__ == "__main__":
    import time
    t0 = time.time()
    N = 16000
    T = julia_cython(N)
    t1 = time.time()
    print t1 - t0

    import sys
    if len(sys.argv) > 1:
        print "Importing matplotlib...",
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from scipy.ndimage.interpolation import zoom
        print "Done"
        print "Zooming matrix...",
        T = zoom(T, 0.20)
        print "Done"
        print "image has size", T.shape
        save_png(T, "julia2.png")
