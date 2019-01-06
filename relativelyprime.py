import sys
for i in range(20):
        a = 20
        b = i

        while b != 0:
                coeff = a//b
                r = a%b

                a = b
                b = r
        if a == 1:
                print('(%d,%d) = 1' % (i,20))

