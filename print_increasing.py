# write a recursive function that will print n integers in decreasing order
def print_decreasing(n):
    if n==0:
        return
    else:
        print(n)
        print_decreasing(n-1)
    
a= int(input())
print_decreasing(a)
