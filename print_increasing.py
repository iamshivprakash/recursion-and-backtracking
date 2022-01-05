# write a recursive function that will print n integers in increasing order
def print_increasing(n):
    if n==0:
        return
    else:
        print_increasing(n-1)
        print(n)
    
a= int(input())
print_increasing(a)
