def balancedStringSplit(s):
    r = 0
    l = 0
    result = 0
    for element in s:
        if element == "R":
            r += 1
        if element == "L":
            l += 1
        if (r != 0 and l != 0 and r==l):
            result += 1
            r = 0
            l = 0
    return result

print(balancedStringSplit('RLLLLRRRLR'))