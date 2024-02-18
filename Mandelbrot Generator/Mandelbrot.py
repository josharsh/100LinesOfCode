import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c : complex, max_iter : int) -> int:      
    """
    Returns the amount of recursive iterations used to guess whether the point is in the set.
        Parameters
        ----------
        c : complex
            The number to be calculated
        max_iter : int
            The number of iterations of recursion
            
        Raises
        ------
        TypeError
            If number is not complex type or if max_iter is not integer.
    """
    if not isinstance(c, complex):
        raise TypeError("Number must be complex type.")
    if not isinstance(max_iter, int):
        raise TypeError("Max iterations must be of type int.")
    
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin : float, xmax : float, ymin : float, ymax : float, width : int, height : int, max_iter : int) -> np.ndarray:
    """
    Returns a 2D np.array of size width * height with each element the point's corresponding amount of iterations of recursive calculations.
        Parameters
        ----------
        xmin : float
            The leftmost x-point on the image
        xmax : float
            The rightmost x-point on the image
        ymin : float
            The bottom y-point on the image
        ymax : float
            The top y-point on the image
        width : int
            The width of the image in pixels
        height : int
            The height of the image in pixels
        max_inter : iter
            The maximum amount of recursive iterations to be done before deciding whether a point is in the set

        Raises
        ------
        TypeError
            If number is not complex type or if max iter is not integer.
    """
    x_space = np.linspace(xmin, xmax, width)
    y_space = np.linspace(ymin, ymax, height)
    return np.array([[mandelbrot(complex(x, y),max_iter) for x in x_space] for y in y_space])

def plot_mandelbrot(xmin,xmax,ymin,ymax,width,height,max_iter):
    set = mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter)
    plt.imshow(set, extent=(xmin, xmax, ymin, ymax))
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.show()

def _typecheck():
    
# Set the range and resolution for the plot
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
max_iter = 256

if __name__ == "__main__":
    plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
