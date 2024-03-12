from PIL import Image
import numpy as np

def mandelbrot(c : complex, max_iter : int) -> int:      
    
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

    set = _mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter)
    image = Image.new("RGB", (width, height))
    normalized_iterations = set / max_iter

    # Here I iterate over each pixel to a cooler color scheme than without it.
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