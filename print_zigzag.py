# Writing a function with 2 recerdive calls to understand the flow of recursion.
def pzz(n):
    if n==0:
        return
    print("Pre",n)
    pzz(n-1)
    print("In",n)
    pzz(n-1)
    print("Post",n)
    
x = int(input())
pzz(x)
