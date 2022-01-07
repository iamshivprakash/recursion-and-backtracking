# Print max of array using Recursion
def moa(arr,index):
    if index==len(arr)-1:
        return arr[index]
    until_max = moa(arr,index+1)
    if arr[index] > until_max:
        return arr[index]
    else:
        return until_max
    
arr = list(map(int,input().split(' ')))
print(moa(arr,0))
    
