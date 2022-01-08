# Find first index of occurance  from an array using recursion
def firstIndex(arr,index,data):
    if index == len(arr):
        return -1
    fiisa = firstIndex(arr,index+1,data)
    if data == arr[index]:
        return index
    return fiisa
    
arr = list(map(int,input().split()))
x = int(input())
print(firstIndex(arr,0,x))
        
