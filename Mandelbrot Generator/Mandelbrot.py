import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter):
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

# Set the range and resolution for the plot
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
max_iter = 256

if __name__ == "__main__":
    plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
