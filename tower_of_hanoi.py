# Tower of Hanoi
def toh(n,A,B,C):
    if n==0:
        return
    toh(n-1,A,C,B)
    print("Moved Disk",n,"From Tower",A,"To Tower ",B)
    toh(n-1,C,B,A)
    
no_of_disk = int(input())
not1 = input()
not2 = input()
not3 = input()
toh(no_of_disk,not1,not2,not3)
