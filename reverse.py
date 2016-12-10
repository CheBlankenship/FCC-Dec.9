# Reverse a String

def reverseStr(string):
    result = "";
    spt = list(string)
    # print spt
    length = len(spt)
    # print length
    re = spt.reverse()
    # print re
    for i in range(length):
        print spt[i]
        result += spt[i]
        print result



reverseStr("hello")
