s1 = "nana"
s2 = "nanana"

if (len(s1) > len(s2)) :
    sto = len(s2)
else :
    sto = len(s1)

mergeString = ""
for i in range (0, sto, 1) :
    mergeString += s1[i: i+1: 1] + s2[i: i+1: 1]
print(mergeString)
