"""Rudimentary Classification Metrics                                                                    

Author: Trevor Martin                                                                                                              
Date: 15 January 2020                                                                                                              
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


def main():

    # low[, high, size, dtype]
    rand_size = lambda: np.random.randint(low=25, high=100)
    rand_dist_x = lambda: np.random.randint(low=1, high=100, size=rand_size())
    rand_dist_y = lambda length: np.random.randint(low=1, high=100, size=length)
    
    tp, tn, fp, fn = rand_dist_x(), rand_dist_x(), rand_dist_x(), rand_dist_x()

    plt.scatter(tp, rand_dist_y(tp.size), color='red', label=f'TruePositive = {tp.size}')
    plt.scatter(tn, rand_dist_y(tn.size), color='blue', label=f'TrueNegative = {tn.size}')
    plt.scatter(fp, rand_dist_y(fp.size), color='green', label=f'FalsePositive = {fp.size}')
    plt.scatter(fn, rand_dist_y(fn.size), color='orange', label=f'FalseNegative = {fn.size}')

    plt.xlabel("x")
    plt.ylabel("y")

    plt.legend()
    plt.show()
    
    accuracy = (tp.size+tn.size) / (tp.size+fn.size+fp.size+tn.size) 
    balanced_acc = ((tp.size/(tp.size+fn.size)) + (tn.size/(fp.size+tn.size))) / 2
    specificity = tn.size / (tn.size+fp.size)
    precision = tp.size / (tp.size+fp.size)
    recall = tp.size / (tp.size+fn.size)
    f1_score = 2 * ((recall*precision)/(recall+precision))
    mcc = ((tp.size*tn.size) - (fp.size*fn.size)) / np.sqrt((tp.size+fp.size)*(tp.size+fn.size)*(tn.size+fp.size)*(tn.size+fn.size))
    
    print(f"ACC: {accuracy}\nBAL: {balanced_acc}\nSPEC: {specificity}\nPREC: {precision}\nREC: {recall}\nF1: {f1_score}\nMCC: {mcc}")

    

if __name__ == '__main__':
    main()
