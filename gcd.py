import sys

a = max(int(sys.argv[1]), int(sys.argv[2]))
b = min(int(sys.argv[1]), int(sys.argv[2]))

while b != 0:
    coeff = a//b
    r = a%b

    print("%d = %d - %d(%d)" % (r,a,coeff,b))

    a = b
    b = r
print('GCD is %d' % a)
