a0 = .55
b0 = .45

ai = a0 * .4 + b0 * .5
bi = a0 * .6 + b0 * .5

while (ai is None or ai != a0) and (bi is None or bi != b0):
     a0 = ai
     b0 = bi
     ai = a0 * .4 + b0 * .5
     bi = a0 * .6 + b0 * .5

print ai
print bi

ab = 1/bi
print ab
