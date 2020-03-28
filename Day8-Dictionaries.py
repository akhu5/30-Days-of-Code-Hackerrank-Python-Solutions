# Input the number of entries
T = int(input())
pdict = {}
# Inputting the data
for i in range(0, T):
    s = str(input()).split(" ")
    name = s[0]
    number = int(s[1])
    pdict[name] = number

for j in range(0, T):
    try:
        str1 = str(input()).rstrip()
        if str1 in pdict:
            print(str1 + "=" + str(pdict[str1]))
        else:
            print("Not found")
    except:
        print("EOF Error")
