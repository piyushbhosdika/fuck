import math
import numpy as np
import matplotlib.pyplot as plt
def sine(list):
    plt.plot(list, [math.sin(x) for x in list])
    plt.xlabel('Degrees')
    plt.ylabel('Values')
    plt.title('sin(x)')
    plt.grid()
    plt.show()
def cosine(list):
    plt.plot(list, [math.cos(x) for x in list])
    plt.xlabel('Degrees')
    plt.ylabel('Values')
    plt.title('cos(x)')
    plt.grid()
    plt.show()
def poly(list):
    plt.plot(list, [(x ** 2 - 4 * x + 10) for x in list]) 
    plt.xlabel('Degrees')
    plt.ylabel('Values')
    plt.title('x^2 - 4*x + 10')
    plt.grid()
    plt.show()
def exp(list):
    plt.plot(list, [math.exp(x) for x in list]) 
    plt.xlabel('Degrees')
    plt.ylabel('Values')
    plt.title('exp(x)')
    plt.grid()
    plt.show()
def plot():
    sine(np.linspace(0, 10, 100)) 
    cosine(np.linspace(0, 10, 100)) 
    poly(np.linspace(-10, 10, 100)) 
    exp(np.linspace(0, 10, 100))
plot()