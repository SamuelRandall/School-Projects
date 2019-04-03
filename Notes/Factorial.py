import sys

def factorial(n):
    if n == 0:
        return(1)
    else:
        return(n*factorial(n-1))

# def factorial_tail_recursion(n):
#     assert n >= 0
#     def f(n,v):
#         if

def factorial_range_reduce(n):
    assert n>= 0
    # take binary operator,
    return reduce(mul, range(1, n+1), 1)

def main():
    while(True):
        try:
            x = input("Input number: ")
            print(factorial(int(x)))
        except ValueError:
            break
main()
