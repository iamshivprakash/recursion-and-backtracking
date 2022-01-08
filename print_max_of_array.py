# Find max from an array using recursion
def moa(arr,index):
    if index==len(arr)-1:
        return arr[index]
    misa = moa(arr,index+1)
    if misa> arr[index]:
        return misa
    return arr[index]
    
arr = list(map(int,input().split()))
print(moa(arr,0))
        
