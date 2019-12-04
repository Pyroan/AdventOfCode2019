# one liner because i enjoy pain.
# input is hardcoded because holy hecc what do you want from me
print(len(list(filter(lambda x:len(list(filter(lambda y:y[0]==y[1],x)))>len(list(filter(lambda y:y[0]>y[1],x)))<1,map(lambda b:list(zip(b,b[1:])),map(str,range(134792,675810)))))))