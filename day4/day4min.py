# one liner because i enjoy pain.
# input is hardcoded because holy hecc what do you want from me
print(len(list(filter(lambda x:len(list(filter(lambda y:y[0]==y[1],x)))and len(list(filter(lambda y:y[0]>y[1],x)))<1,list(map(lambda b:list(zip(b,b[1:])),map(lambda a:list(map(int,list(str(a)))),range(134792,675810))))))))