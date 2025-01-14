str1="ABC"
str2="ABCABC"

# if set(str1) == set(str2):
#     print("equal")

def isDivisor(l, str1, str2):
    len1, len2 = len(str1), len(str2)
    if (len1%l == 0 and len2%l == 0):
        f1 = len1//l
        f2 = len2//l
        small = min(str1, str2, key=len)
        small[:l]*f1 == str1 and small[:l]*f2 == str2
        return True
    else:
        return False

def gcdOfStrings(str1, str2):
    len1, len2 = len(str1), len(str2)
        
    for i in range(min(len1, len2)+1):
        if isDivisor(i):
            print(str1[:i])
