from PIL import Image
import numpy as np

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
    
    z = c
    for n in range(max_iter):
        if abs(z) > 2.0:
            return n
        z = z*z + c # the complex function :)
    return max_iter

def _mandelbrot_set(xmin : float, xmax : float, ymin : float, ymax : float, width : int, height : int, max_iter : int) -> np.ndarray:  
     
    x_space = np.linspace(xmin, xmax, width)
    y_space = np.linspace(ymin, ymax, height)
    return (np.array([[mandelbrot(complex(x, y),max_iter) for x in x_space] for y in y_space]))

def plot_mandelbrot(xmin : float, xmax : float, ymin : float, ymax : float, width : int, height : int, max_iter : int):
    """
    Plots a mandelbrot set corresponding to the given parameters.
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
        max_inter : int
            The maximum amount of recursive iterations to be done before deciding whether a point is in the set

        Raises
        ------
        TypeError
            If ranges are not floats or integers, or if sizes are not integers or if max_iter is not int
    """
    if not isinstance(xmin, (float, int)):
        raise TypeError("All ranges must be of type float or int.")
    if not isinstance(xmax, (float, int)):
        raise TypeError("All ranges must be of type float or int.")
    if not isinstance(ymin, (float, int)):
        raise TypeError("All ranges must be of type float or int.")
    if not isinstance(ymax, (float, int)):
        raise TypeError("All ranges must be of type float or int.")
    if not isinstance(width,  int):
        raise TypeError("Sizes of image must be of type int.")
    if not isinstance(height, int):
        raise TypeError("Sizes of image must be of type int.")
    if not isinstance(max_iter, int):
        raise TypeError("Max iterations must be of size int.")

    set = _mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter)
    image = Image.new("RGB", (width, height))
    normalized_iterations = set / max_iter

    # Here I iterate over each pixel to change the color scheme to look a bit cooler :0
    for y in range(height):
        for x in range(width):
            iter_count = normalized_iterations[y, x]
            if iter_count == 1:
                r, g, b = (0, 0, 0)
            else: r, g, b = (iter_count, 0.2 * iter_count, 0.3)
            
            image.putpixel((x, y), (int(r * 255), int(g * 255), int(b * 255)))

    image.show()
    
if __name__ == "__main__":
    
    # Set the range and resolution for the plot  
    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
    width, height = 1000, 1000
    max_iter = 80
    plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)