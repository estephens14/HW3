"""Support functions - Homework 3

"""

#Remember that all libraries needed from your functions should be
#imported at the start:

import numpy as np
import matplotlib.pyplot as plt 

# Problem 2 d) Create a function called square. Its input is x. The goal is 
# to return the square of this input, x.
def square(x):
    ''' 
    Parameters:
    x is the scalar or array. This will be squared.

    Returns: 
    The square of the input, x.

    Example:
    square(3)
    9
    '''
    return x**2
