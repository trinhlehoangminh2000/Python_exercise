#line = input("input words: ")

inLine = "hello"

def mirrorIt(line):
    list = list(line)
    enil = ""
    for i in range (len(list)-1,-1,-1):
        enil += list[i]
    return enil

def mirrorRe(line):
    if line == "" :
        return ""
    l = list(line)
    letter = l[len(l)-1]
    line = combineList(l)
    return letter + mirrorRe(line)

def combineList(l):
    line = ""
    for i in range(0, len(l)-1):
        line += l[i]
    return line

print(mirrorRe(inLine))
