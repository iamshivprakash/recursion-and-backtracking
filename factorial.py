# write a recursive function that will print factorial of n numbers
def factorial(n): 
    if n==1:
        return 1
    else:
        fnm1 = factorial(n-1)
        fn = n * fnm1
        return fn  """This return is very important else you will get an type error"""
    # print(fn)
a= int(input())
print(factorial(a))
