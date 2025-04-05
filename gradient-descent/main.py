### Made By Elston
### https://github.com/Elstuhn
### Gradient descent using approximation

from functools import cache 
import sympy

@cache
def findgrad(x : float, f, step : float):
    return (f(x+step)-f(x))/step

def cleanfunc(func : str):
    x = sympy.Symbol("x")
    try:
        f = sympy.sympify(func)
        return sympy.lambdify(x, f)
    except:
        try:
            func = func.replace("^", "**")
            f = sympy.sympify(func)
            return sympy.lambdify(x, f)
        except:
            pass
    inds = []
    func = list(func)
    for i, j in enumerate(func):
        if all([
            j == "x",
            func[i-1] != "(",
            func[i-1].isdigit(),
            i != 0,
        ]):
            inds.append(i)
    
    prev = 0
    result = ""
    for index in inds:
        result += "".join(func[prev:index])+"*"
        prev = index
    result += "".join(func[prev:])
    f = sympy.sympify(result)
    return sympy.lambdify(x, f)        


def grad_desc(x : float, func : str, step : int = 0.05, lr : float = 3e-4, threshold : float = 0.001):
    """
    Trains x by approximating the gradient and checks it against the threshold
    """
    f = cleanfunc(func)
    while findgrad(x, f, step) > threshold:
        x -= findgrad(x, f, step)*lr
        
    return x