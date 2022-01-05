# write power function recursively
def power(x,n): 
    if n==1:
        return x
    else:
        pnm1 = power(x,n-1)
        pn = x * pnm1
        return pn  """This return is very important else you will get an type error"""
    # print(fn)
x = int(input())
n = int(input())
print(power(x,n))
