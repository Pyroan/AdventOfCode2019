t,l={n[4:7]:n[:3]for n in open('day6.txt').readlines()},0
for n in t:
 while n!='COM':l,n=l+1,t[n]
print(l)