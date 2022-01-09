# print keypad combination
codes = [".;","abc","def","ghi","jkl","mno","pqrs","tu","vwx","yz"]
def gkpc(keypad):
    if len(keypad) ==0:
        return [""]
    key = keypad[0]  
    rok = keypad[1:]
    rres = gkpc(rok)
    mres =[]
    for word in rres:
        for char in codes[int(key)]:
            mres.append(char+word)
    print(len(mres))
    return mres
    
keypad = input()
print(gkpc(keypad))
