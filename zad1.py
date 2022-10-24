#! /usr/bin/env python

''' Lista 1 Zadanie 1 '''

from random import randint
from typing import Callable
from time import time

# 1. Algorytm klasy O(n^2)
def suboptimal(coeffs: list, value: float) -> float:
    result = 0
    for (i, c) in enumerate(coeffs):                # Pętla przebiegająca po każdym jednomianie
        power = 1
        for _ in range(i):                          # Pętla do obliczenia i-tej potęgi argumentu
            power *= value
        result += c*power

    return result 

# 2. Algorytm klasy O(n*log(n))
def midoptimal(coeffs: list, value: float) -> float:

    def calc_power(base, exp):                       # Funkcja do obliczenia potęgi o złożoności O(log(n))
        
        if exp == 0:                                 # Przypadki trywialne
            return 1
        if exp == 1:
            return base
         

        root = calc_power(base, exp//2)              # Korzystamy z:
        if exp % 2 == 0:                             # x^n = (x^(n/2))^2 dla parzystego n 
            return root*root                         #
        return root*root*base                        # x^n = (x^(n//2))^2 * x dla nieparzystego n 

    result = 0
    for (i, c) in enumerate(coeffs):                 # Pętla przebiegająca po kązdym jednomianie
        result += c*calc_power(value, i)
    return result


# 3. Schemat hornera. Złożoność liczbowa O(n) 
def horner(coeffs : list, value : float) -> float:
    result = 0
    for c in coeffs[1:][::-1]:                      # Ustawiamy współczynniki bez a0 w odwrotnej kolejności
        result += c                                 
        result *= value                             
    result += coeffs[0]                             # Dodanie wyrazu wolnego do wyniku 
    return result

def time_algorithm(algo: Callable, sample: list, val: float, reps: int) -> float:
    start = time()
    for _ in range(reps):
        _ = algo(sample, val)
    return time() - start

if __name__ == '__main__':
    print('Testowany wielomian: 3x^2 + 2x + 1')
    print('Wartości podawane dla x = 2')
    print(f'Algorytm O(n^2):      {suboptimal([1, 2, 3], 2)}')
    print(f'Algorytm O(n*log(n)): {midoptimal([1, 2, 3], 2)}')
    print(f'Algorytm O(n):        {horner([1, 2, 3], 2)}')

    reps = 100000
    sample = [randint(1, 10) for _ in range(11)]
    print('------------------------------------------------')
    print(f'Czasy wykonania algorytmów dla {reps} powtórzeń')
    print('Stopień testowanego wielomianu: 10')
    print(f'Czas wykonania dla O(n^2):      {time_algorithm(suboptimal, sample, 2, reps)}')
    print(f'Czas wykonania dla O(n*log(n)): {time_algorithm(midoptimal, sample, 2, reps)}')
    print(f'Czas wykonania dla O(n):        {time_algorithm(horner, sample, 2, reps)}')