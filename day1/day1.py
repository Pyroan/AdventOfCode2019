with open('day1.txt') as f:
    print(sum([int(x) // 3 - 2 for x in f.readlines()]))