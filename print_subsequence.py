# print subsequence of the string 
# ros-->rest of string
# bres-->base case result
# rres--> recursion result
# mres--> my result
# rch--> character in recursion result list
def get_ssq(string):
    if len(string) ==0:
        bres =[]
        # substring of blank string is blank itself.
        # so we have to add blank string in base result and then return
        bres.append("")
        return bres
    # faith bc-->[--,-c,b-,bc]
    # expectation abc-->[---,--c,-b-,-bc,a--,a-c,ab-,abc]
    ch = string[0]
    ros = string[1:]
    rres = get_ssq(ros)
    mres = []
    for rch in rres:
        mres.append(rch)
        mres.append(ch+rch)
    return mres
    
string = input()
print(get_ssq(string))
