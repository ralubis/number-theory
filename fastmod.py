import sys

base = int(sys.argv[1])
exp = int(sys.argv[2])
mod = int(sys.argv[3])

explist = [1,2,4]
modlist = []

for i in explist:
    ans = (base**i) % mod
    print '%d^%d mod %d = %d' % (base, i, mod, ans)
    modlist.append(ans)


print '%d^7 = %d (mod %d)' % ( base ,(modlist[0] * modlist[1] * modlist[2]) % mod, mod)