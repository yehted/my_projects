from PIL import Image, ImageColor
import numpy as np
from sys import maxint
import argparse

MAX_ENERGY = 195075

class SeamCarver(object):

    def __init__(self, image):
        """Create a seam carver object based on the given picture"""
        self.image = image.convert('RGB')
        self.width = image.size[0]
        self.height = image.size[1]
        self.transposed = False
        self.color = np.asarray(image, dtype=int)
        # self.color = self.color.transpose(1,0,2)
        self.energy_matrix = np.zeros(image.size)
        self.energy_matrix = self.energy_matrix.transpose()
        for x in xrange(self.height):
            for y in xrange(self.width):
                self.energy_matrix[x][y] = self.energy(x,y)

    def picture(self):
        """Return the current picture"""
        temp = self.color.astype('uint8')
        return Image.fromarray(temp[:self.height, :self.width], mode='RGB')

    def energy(self, x, y):
        """Energy of pixel at column x and row y"""

        # Check if pixel is in bounds
        if (x < 0 or x > self.height - 1):
            raise IndexError("Invalid x pixel")
        if (y < 0 or y > self.width - 1):
            raise IndexError("Invalid y pixel")

        # Edge pixels
        if (x == 0 or x == self.height - 1):
            return MAX_ENERGY
        if (y == 0 or y == self.width - 1):
            return MAX_ENERGY

        delta_x =  self.color[x+1][y] - self.color[x-1][y]
        x_squared = delta_x.dot(delta_x)
        delta_y =  self.color[x][y+1] - self.color[x][y-1]
        y_squared = delta_y.dot(delta_y)

        return x_squared + y_squared

    def find_vertical_seam(self):
        """Sequence of indices for vertical seam"""

        energy_to = np.full(self.image.size, maxint)
        energy_to = energy_to.transpose()
        pixel_to = np.zeros(self.image.size)
        pixel_to = pixel_to.transpose()

        for y in xrange(self.width):
            energy_to[0][y] = self.energy_matrix[0][y]

        # Relaxes all energies
        # for i in xrange(1, self.height):
        #     for j in xrange(self.width):
        #         for k in [-1, 0, 1]:
        #             if (j + k < 0 or j + k >= self.width):
        #                 continue
        #             if (energy_to[i, j] > energy_to[i - 1, j + k] + self.energy_matrix[i, j]):
        #                 energy_to[i, j] = energy_to[i - 1, j + k] + self.energy_matrix[i, j]
        #                 pixel_to[i, j] = k

        for (i, j) in np.ndenumerate(energy_to):
            for k in [-1, 0, 1]:
                if (j + k < 0 or j + k >= self.width):
                    continue
                if (energy_to[i, j] > energy_to[i - 1, j + k] + self.energy_matrix[i, j]):
                    energy_to[i, j] = energy_to[i - 1, j + k] + self.energy_matrix[i, j]
                    pixel_to[i, j] = k

        # Finds the minimum pixel in the last row
        min_energy = maxint
        v = 0
        for j in xrange(self.width):
            if energy_to[self.height - 1][j] < min_energy:
                min_energy = energy_to[self.height - 1][j]
                v = j

        seam = np.zeros(self.height)
        seam[self.height-1] = v

        # Generates the seam path to the top row
        for i in xrange(self.height-2, -1, -1):
            seam[i] = v + pixel_to[i + 1][v]
            v = v + pixel_to[i + 1][v]

        return seam

    def find_horizontal_seam(self):
        """Sequence of indices for horizontal seam"""
        if not self.transposed:
            self._transpose()
        seam = self.find_vertical_seam()
        self._tranpose()
        return seam

    def remove_horizontal_seam(self, seam):
        """Remove horizontal seam from current picture"""
        pass

    def remove_vertical_seam(self, seam):
        """Remove vertical seam from current picture"""
        # Check validity of seam
        if len(seam) != self.height:
            raise RuntimeError("Seam is wrong length")

        for i in xrange(len(seam) - 1):
            if seam[i+1] - seam[i] > 1 or seam[i+1] - seam[i] < -1:
                raise RuntimeError("Invalid seam")

        if self.height <= 1:
            raise RuntimeError("Picture is too small")

        # Shift the image over according to the seam
        for i in xrange(self.height):
            for j in xrange(int(seam[i]), self.width - 1):

                self.color[i][j] = self.color[i][j+1]
                self.energy_matrix[i][j] = self.energy_matrix[i][j+1]

        self.width -= 1

        # Recalculate energy and color matrices
        for i in xrange(self.height):
            if seam[i] > 0:
                self.energy_matrix[i][seam[i] - 1] = self.energy(i, seam[i]-1)
            if seam[i] < self.width:
                self.energy_matrix[i][seam[i]] = self.energy(i, seam[i])


    def _transpose(self):
        """Transpose the color and energy matrix"""
        self.color = np.transpose(self.color, (1,0,2))
        self.energy_matrix = np.transpose(self.energy_matrix)
        self.transposed = not self.transposed
        temp = self.width
        self.width = self.height
        self.height = temp

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="Image to load")
    parser.add_argument("length", help="Number of columns to remove")
    args = parser.parse_args()

    image = Image.open(args.file_name)
    image.show()
    carver = SeamCarver(image)

    for x in xrange(int(args.length)):
        seam = carver.find_vertical_seam()
        carver.remove_vertical_seam(seam)

    carved = carver.picture()
    carved.show()

if __name__ == '__main__':
    main()
