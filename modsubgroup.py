import sys

#a = int(sys.argv[1])
a = 43
for b in range (1,a):
    r = b
    count = 1
    elems = []
    while (r % a) != 1:
        r *= b
        r = r % a
        elems.append(r)
        count += 1
    elems.append(b)
    #elems.sort()
    #modelems = []
    #for e in elems:
    #    modelems.append(e % a)
    #print 'generator: %d' % b,elems
    #print 'generator: %d' %b,modelems
    if count == 6 or count == 21:
        print "generator:%d (count: %d)" % (b, count)
    
