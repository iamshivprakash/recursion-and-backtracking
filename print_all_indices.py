# Find last index of occurance  from an array using recursion
# fsf---->found so far
def allIndices(arr,index,data,fsf):
    if index == len(arr):
        # in base case we will create an array of size fsf and will return
        return [0]*fsf
    
    if arr[index] == data:
        iarr = allIndices(arr,index+1,data,fsf+1)
        # here we have received iarr returend from recursion
        iarr[fsf]=index
        return iarr
    else:
        iarr = allIndices(arr,index+1,data,fsf)
        return iarr
    
arr = list(map(int,input().split()))
x = int(input())
print(allIndices(arr,0,x,0))
        
