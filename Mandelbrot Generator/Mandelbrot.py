from PIL import Image
import colorsys
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
    
    z = c
    for n in range(max_iter):
        if abs(z) > 2.0:
            return n
        z = z*z + c
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
            If number is not complex type or if max iter is not integer.
    """
    set = _mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter)
    image = Image.new("RGB", (width, height))
    normalized_iterations = set / max_iter * 255

# Iterate over each pixel and set its color based on the iteration count
    for y in range(height):
        for x in range(width):
        # Get the iteration count at this pixel
            iter_count = normalized_iterations[y, x]
        # Convert the iteration count to a color
            r, g, b = colorsys.hsv_to_rgb(0.7 + 10 * iter_count, 0.6, 0.8)
        # Convert RGB values to the range [0, 255] and set the pixel color
            image.putpixel((x, y), (int(r * 255), int(g * 255), int(b * 255)))

# Display the image
    image.show()
    #plt.imshow(set, extent=(xmin, xmax, ymin, ymax))
    #plt.colorbar()
    #plt.title("Mandelbrot Set")
    #plt.xlabel("Real")
    #plt.ylabel("Imaginary")
    #plt.show()

#def _typecheck():
    
# Set the range and resolution for the plot
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
#xmin, xmax, ymin, ymax = 0.6, 0.8, 0.05, 0.25
width, height = 1000, 1000
max_iter = 1000

if __name__ == "__main__":
    plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
