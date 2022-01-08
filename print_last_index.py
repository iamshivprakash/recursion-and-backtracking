# Find last index of occurance  from an array using recursion
def lastIndex(arr,index,data):
    if index == len(arr):
        return -1
    
    liisa = lastIndex(arr,index+1,data)
    if liisa == -1:
        if arr[index] == data:
            return index
        else:
            return liisa
    else:
        return liisa
    
arr = list(map(int,input().split()))
x = int(input())
print(lastIndex(arr,0,x))
        
