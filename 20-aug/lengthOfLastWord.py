# s = 'Hello  World'
# print(s.split(' '))

#counting the vowels in a string
v='aeiou'
s='leetcode'
c={}.fromkeys(v,0)
count=0
for i in s:
    if i in v:
        c[i]+=1

print(c)