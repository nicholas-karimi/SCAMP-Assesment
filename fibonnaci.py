#!/usr/bin/env python
## -*- coding: utf-8 -*-

"""A python program that prints the Fibonnaci series,
    using recursion and dynamic programming
    """

# set the first Fibonnaci terms (1, 2)
initial_cache = {0:0, 1:1}

def fibonacci(term):
    # base case
    if term in initial_cache: #check if term already computed and return it
        return initial_cache[term]
    else:
        # recursive logic to compute the terms
        initial_cache[term] = fibonacci(term-2) + fibonacci(term-1)
        return initial_cache[term]

def main():
    print(fibonacci(10))

if __name__ == '__main__':
    main()
