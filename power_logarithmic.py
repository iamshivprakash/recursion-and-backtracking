# write power function recursively
def power(x,n): 
    if n==0:
        return 1
    xpnb2 = power(x,n//2)
    xpn = xpnb2 * xpnb2
    if n%2 == 1:
        xpn = xpn * x
    return xpn  
    """This return is very important else you will get an type error"""
    # print(fn)
x = int(input())
n = int(input())
print(power(x,n))
