#! /usr/bin/env python

'''Lista 1 Zadanie 3 '''
from random import randint 
from time import time
from scipy.optimize import curve_fit
from tqdm import tqdm
from zad2 import time_algorithm
import matplotlib.pyplot as plt
import numpy as np

test_cases = [[randint(0, 100) for i in range(i)] for i in tqdm(range(100, 1000, 100))]

def nlogn(x, a, b):
    return a*x*np.log(b*x)

def timeit(sample: list, reps: int):
    start = time()
    for i in range(reps):
        _ = sorted(sample)
    return len(sample), time() - start

results = [time_algorithm(case, 1000) for case in tqdm(test_cases)]

x, y = zip(*results)

popt, _ = curve_fit(nlogn, x, y)


plt.title('Złożoność obliczeniowa dla algorytmu sorted')
plt.xlabel('size')
plt.ylabel('time')
plt.scatter(x, y, label='ro')

plt.show()

plt.title(f'Przewidywana złożoność: n * log(n)')
plt.xlabel('size')
plt.ylabel('time')
plt.scatter(x, y, label='ro')
plt.plot(np.array(x), nlogn(np.array(x), *popt))
plt.show()
print(*popt)