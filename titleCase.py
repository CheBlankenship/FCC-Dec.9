def titleCase(string):
    result = ""
    lower = string.lower()
    print lower
    spt = lower.split(" ")
    print spt
    length = len(spt)
    for i in range(length):
        print spt[i]
        firstUpper = spt[i][0].upper()
        print firstUpper
        if spt[i][0] != firstUpper:
            spt[i][0] == firstUpper
            result += spt[i]

    print result



titleCase("I'm a little tea pot")
