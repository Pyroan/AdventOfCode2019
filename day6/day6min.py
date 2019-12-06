
t,l={n[1]:n[0]for n in[s.strip().split(')')for s in open('day6.txt').readlines()]},0
for n in t:
 while n!='COM':l,n=l+1,t[n]
print(l)