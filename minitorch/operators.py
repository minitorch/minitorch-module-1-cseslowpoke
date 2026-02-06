"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(x:float, y:float) -> float:
    return x * y

def id(x:float) -> float:
    return x

def add(x:float, y:float) -> float:
    return x + y

def neg(x:float) -> float:
    return -x

def lt(x:float, y:float) -> bool:
    return x < y

def eq(x:float, y:float) -> bool:
    return x == y

def max(x:float, y:float) -> float:
    return x if x > y else y

def is_close(x:float, y:float) -> bool:
    return abs(x - y) < 1e-2

def sigmoid(x:float) -> float:
    return 1.0 / (1.0 + math.exp(-x)) if x >= 0 else math.exp(x) / (1.0 + math.exp(x))

def relu(x:float) -> float:
    return max(0, x)

def log(x:float) -> float:
    return math.log(x)

def exp(x:float) -> float:
    return math.exp(x)

def inv(x:float) -> float:
    return 1.0 / x

def inv_back(x:float, y:float) -> float:
    return -1.0 / (x * x)

def log_back(x:float, y:float) -> float:
    return 1.0 / x

def relu_back(x:float, y:float) -> float:
    return y if x > 0 else 0
# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(fn):
    """Higher-order map. Returns a function that applies `fn` to each element of a list."""
    return lambda ls: [fn(x) for x in ls]


def zipWith(fn):
    """Higher-order zipWith. Returns a function that applies `fn` to pairs from two lists."""
    return lambda ls1, ls2: [fn(x, y) for x, y in zip(ls1, ls2)]
    

def reduce(fn, start):
    """Higher-order reduce. Returns a function that reduces a list using `fn` starting from `start`."""
    def reduce_fn(ls):
        if len(ls) == 0:
            return start
        return fn(reduce_fn(ls[1:]), ls[0])
    return reduce_fn


def negList(ls):
    """Negate each element in `ls`."""
    return map(neg)(ls)


def addLists(ls1, ls2):
    """Add corresponding elements from `ls1` and `ls2`."""
    return zipWith(add)(ls1, ls2)


def sum(ls):
    """Sum up all elements in `ls`."""
    return reduce(add, 0)(ls)


def prod(ls):
    """Take the product of all elements in `ls`."""
    return reduce(mul, 1)(ls)
