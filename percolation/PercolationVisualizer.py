import graphics as gr
import percolation
from sys import argv

class PercolationVisualizer(object):
    """Visualizes a N-by-N percolation grid"""

    # Window size variables
    _size = 512
    _edge = .05
    _scale = 1 - 2 * _edge

    _win = gr.GraphWin("Percolation", _size, _size * 1.2, autoflush=False)
    _win.setBackground("black")

    @staticmethod
    def draw(perc, N):
        """Draw N-by-N percolation system"""
        box_size = PercolationVisualizer._size / float(N)
        opened = 0

        for row in range(1,N+1):
            for col in range(1,N+1):
                box = gr.Rectangle(gr.Point((col-1)*box_size, (row-1)*box_size),
                    gr.Point(box_size*(col-1 + PercolationVisualizer._scale),
                        box_size*(row-1 + PercolationVisualizer._scale)))
                if perc.isFull(row, col):
                    box.setFill('blue2')
                    box.setOutline('blue2')
                    opened += 1
                elif (perc.isOpen(row, col)):
                    box.setFill('white')
                    box.setOutline('white')
                    opened += 1
                else:
                    box.setFill('black')
                box.draw(PercolationVisualizer._win)

        # Set text for open sites and if percolating
        openmsg = gr.Text(gr.Point(.25 * PercolationVisualizer._size,
            1.1 * PercolationVisualizer._size),
            str(opened) + " open sites")

        p = gr.Text(gr.Point(.75 * PercolationVisualizer._size,
                1.1 * PercolationVisualizer._size), "does not percolate")

        if perc.percolates():
            p.setText("percolates")

        # Draw text background box
        textbox = gr.Rectangle(gr.Point(0,PercolationVisualizer._size),
            gr.Point(PercolationVisualizer._size, PercolationVisualizer._size*1.2))
        textbox.setFill('white')
        textbox.setOutline('white')

        # Text font formatting
        openmsg.setSize(16)
        p.setSize(16)
        openmsg.setTextColor('red')
        p.setTextColor('red')

        # Draws items
        textbox.draw(PercolationVisualizer._win)
        openmsg.draw(PercolationVisualizer._win)
        p.draw(PercolationVisualizer._win)



def main():
    """Opens command line argument as file

    Then opens each coordinate, while assigning a color: black if closed
    site, white if open site and blue if filled site. System percolates
    when the top edge is connected to the bottom edge.
    """

    with open(argv[1], 'r') as my_file:
        N = my_file.readline()
        print N
        N = int(N)
        perc = percolation.Percolation(N)
        PercolationVisualizer.draw(perc, N)
        for line in my_file.readlines():
            i, j = line.split()
            i = int(i)
            j = int(j)
            perc.open(i, j)
            PercolationVisualizer.draw(perc, N)

            # Forces update to redraw grid
            PercolationVisualizer._win.update()
    raw_input()


if __name__ == '__main__':
    main()
