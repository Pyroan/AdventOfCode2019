from collections import Counter
with open('day8.txt') as f:
    img = f.read()

w,h = 25,6

counters = [dict(Counter(img[n:n+w*h])) for n in range(0,len(img),w*h) ]
leastest = counters[0]
for c in counters:
    if c['0'] < leastest['0']:
        leastest = c
print(leastest['1']*leastest['2'])
