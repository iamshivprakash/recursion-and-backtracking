# Print array using Recursion
def dar(arr,index):
    if index==len(arr):
        return
    dar(arr,index+1)
    print(arr[index])
    
arr = list(map(int,input().split(' ')))
dar(arr,0)
    
