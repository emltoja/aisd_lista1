#! /usr/bin/env python

from random import randint
from time import time
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit 
from typing import Callable
import numpy as np

'''Lista 1. Zadanie 2'''

# Przeprowadzić analizę eksperymentalną poniższych algorytmów: 
def example1(S): 
    """Return the sum of the elements in sequence S.""" 
    n = len(S) 
    total = 0 
    for j in range(n): 
        total += S[j] 
    return total

def example2(S): 
    """Return the sum of the elements with even index in sequence S. """ 
    n = len(S) 
    total = 0 
    for j in range(0, n, 2):
        total += S[j]
    return total

def example3(S): 
    """Return the sum of the prex sums of sequence S.""" 
    n = len(S) 
    total = 0 
    for j in range(n): 
        for k in range(1+j): 
            total += S[k]
    return total 

def example4(A, B): # assume that A and B have equal length 
    """Return the number of elements in B equal to the sum of prex sums in A."""
    n = len(A)
    count = 0 
    for i in range(n): 
        total = 0 
        for j in range(n): 
            for k in range(1+j): 
                total += A[k] 
        if B[i] == total: 
            count += 1 
    return count

# Funkcja zwracająca czas wykonania określonej liczby powtórzeń algorytmu na określonej próbce
def time_algorithm(algo: Callable, sample: list, reps: int, x:list = None):
    start = time()
    for _ in range(reps):
        _ = algo(sample) if not x else algo(sample, x)
    return len(sample), time() - start

# Analiza eksperymentalna algorytmu example1
linear_samples = [[randint(0, 100) for _ in range(10**i)] for i in range(1, 7)]
quadratic_samples = [[randint(0, 100) for _ in range(10*i)] for i in range(10, 100, 10)]
cubic_samples = [[randint(0, 100) for _ in range(10*i)] for i in range(10, 20, 1)]
def linear(x, a, b):
    return a*x + b

def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

def cubic(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

def analyze_algo(algo: Callable, samples: list[list], prediction: Callable):
    
    if algo == example4:
        results = [time_algorithm(algo, x, 10, x) for x in samples]
    else:
        results = [time_algorithm(algo, sample, 100) for sample in samples]
    x, y = zip(*results)

    popt, _ = curve_fit(prediction, x, y)
    
    
    plt.title(f'Złożoność obliczeniowa dla algorytmu {algo.__name__}')
    plt.xlabel('log(size)')
    plt.ylabel('log(time)')
    plt.scatter(x, y, label='ro')
    plt.loglog()
    plt.show()

    plt.title(f'Przewidywana złożoność: {prediction.__name__}')
    plt.xlabel('size')
    plt.ylabel('time')
    plt.scatter(x, y, label='ro')
    plt.plot(np.array(x), prediction(np.array(x), *popt))
    plt.show()
    print(*popt)

if __name__ == '__main__':
    analyze_algo(example1, linear_samples, linear)
    analyze_algo(example2, linear_samples, linear)
    analyze_algo(example3, quadratic_samples, quadratic)
    analyze_algo(example4, cubic_samples, cubic)
