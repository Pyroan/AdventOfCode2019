# Would be easier with numpy if i knew how to use that offhand
with open('day8.txt') as f:
    img = f.read()

w,h = 25,6

layers = [img[n:n+w*h] for n in range(0,len(img),w*h) ]
final = [0]*w*h
for l in layers[::-1]:
    for i in range(len(l)):
        if l[i] !='2':
            final[i] = l[i]

for i in range(0,len(final)//w):
    s = ''
    for j in final[w*i:w*i+w]:
        if j == '2':
            s+=' '
        elif j == '1':
            s+='X'
        elif j == '0':
            s+=' '
    print(s)
