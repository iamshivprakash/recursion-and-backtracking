# Print array using Recursion
def pa(arr,index):
    if index==len(arr):
        return
    print(arr[index])
    pa(arr,index+1)
    
arr = list(map(int,input().split(' '))
pa(arr,0)
    
