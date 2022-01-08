# Find first index of occurance  from an array using recursion
def firstIndex(arr,index,data):
    if index == len(arr):
        return -1
    fiisa = firstIndex(arr,index+1,data)
    if data == arr[index]:
        return index
    return fiisa
    
# Better Solution__________________
def Fi(arr,index,data):
    if index == len(arr):
        return -1
    if data == arr[index]:
        return index
    fiisa = Fi(arr,index+1,data)
    return fiisa
    
arr = list(map(int,input().split()))
x = int(input())
print(firstIndex(arr,0,x))
print(Fi(arr,0,x))
        
