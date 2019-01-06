from math import gcd as py_gcd

ans = []
for i in range (2,35):
    g = py_gcd(i,35)
    if g != 1:
        print ('(i={0},35) = g={1}'.format(i,g)) 
        ans.append(i)
print (ans)
