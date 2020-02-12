"""Newton's Method                                                                                                                
A NumPy implementation of newton's method optimization algorithm                                                                          
                                                                                                                  
Author: Trevor Martin                                                                                                              
Date: 15 January 2020                                                                                                              
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


def newton(w_0, func, d1, d2):
    """performs newton's method on a given function"""
    w_k = w_0
    for step in range(0, 15): # number of descents
        plt.plot(w_k, func(w_k), marker='o',color='red')
        w_k_minus_1 = w_k
        w_k = w_k - (d1(w_k_minus_1) / d2(w_k_minus_1))
        w_K_minus_1 = abs(w_k - w_k_minus_1)
    plt.show()

        
def main():
    w_0 = 1 # the initial point
    alpha = 0.1 # the "learning rate or "step length" of each descent
    
    # one possible function, where w is scalar input
    func1 =  lambda w: np.log(1 + np.exp(1)**(w**2)) 
    # first order derivative of func1
    d1 = lambda w: (2*(np.exp(1)**(w**2))*w)/(1+np.exp(1)**(w**2)) 
    # second order derivative of func1
    d2 = lambda w: (2*(np.exp(1)**(w**2))) * (2*(w**2) + (np.exp(1)**(w**2)) + 1) / (1 + (np.exp(1)**(w**2)))**2
    
    # for plotting purposes
    w = np.linspace(start=-1, stop=1, num=50)
    plt.xlabel("w")
    plt.ylabel("x")
    plt.plot(w, func1(w))
    
    newton(w_0, func1, d1, d2)
    
if __name__ == '__main__':
    main()
