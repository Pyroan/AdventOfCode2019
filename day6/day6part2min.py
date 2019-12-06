t,l,y,s={n[4:7]:n[:3]for n in open('day6.txt')},[],'YOU','SAN'
while y!='COM':l,y=l+[y],t[y]
while s!='COM':
 if s in l:l.remove(s)
 else:l+=[s]
 s=t[s]
print(len(l)-2)