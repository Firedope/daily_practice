def checkPalindrome(s):
    s = str(s)
    if s==s[::-1]:
        out= True
    else:
        out = False
    return out

def usingRev(s):
    inp = list(str(s))
    rev = list(reversed(inp))
    if inp==rev:
        return True
    else:
        return False

def logic(s):
    string = str(s)
    o = ''
    for i in range(len(string)):
        o.add(s%10)
        s = s//10
    print(string,o)

print(checkPalindrome(1001))
print(checkPalindrome(2003))
print(usingRev(1001), usingRev(2003))
print(logic(1001), logic(2004))