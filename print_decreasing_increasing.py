# write a recursive function that will print n integers
# in first decreasing and then in increasing order
def print_decreasing_increasing(n): 
    if n==0:
        return
    else:
        print(n)
        print_decreasing_increasing(n-1)
        print(n)
    
a= int(input())
print_decreasing_increasing(a)
