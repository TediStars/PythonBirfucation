#https://stackoverflow.com/questions/14739555/code-for-logistic-equation

import numpy as np
import matplotlib.pyplot as plt
import pylab
import numpy

def f(x, r):
    """Discrete logistic equation with parameter r"""
    return r*x*(1-x)

if __name__ == '__main__':
    # initial condition for x
    ys = []#Κενός πίνακας
    rs = numpy.linspace(0, 4, 400)#Array [0...4] <-400 αριθμοί ίσης απόστασης ο ένας από τον άλλο

    # Loop through `rs`. `r` is assigned the values in `rs` one at a time. 
    for r in rs:
        x = 0.1
        # Repeat this loop 500 times. 
        # i is just a dummy variable since it is not used inside the for-loop.
        for i in range(500):
            # Evaluate f at (x, r). The return value is assigned to x.
            # x is then fed back into f(x, r). 
            # This makes x jump around 500 times according to the logistic equation.
            # r remains fixed.
            x = f(x, r)

        # Do this 50 times
        for i in range(50):
            # Again make the x jump around according to the logistic equation
            x = f(x, r)
            # Save the point (r, x) in the list ys
            ys.append([r, x])

    # ys is a list of lists.
    # You can also think of ys as a list of [r, x] point.
    # This converts the list of lists into a 2D numpy array.
    ys = numpy.array(ys)

    # ys[:,0] is a 1D array of r values
    # ys[:, 1] is a 1D array of x values
    # This draws a scatter plot of (r, x) points.
    pylab.plot(ys[:,0], ys[:,1], '.')
    pylab.show()
