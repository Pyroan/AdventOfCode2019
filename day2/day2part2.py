with open('day2.txt') as f:
    start_code = list(map(int, f.readline().split(',')))

for i in range(100):
    for j in range(100):
        code = start_code[:]
        code[1] = i
        code[2] = j
        fp = 0
        while code[fp] != 99:
            if code[fp] == 1:
                code[code[fp+3]] = code[code[fp+1]] + code[code[fp+2]]
            elif code[fp] == 2:
                code[code[fp+3]] = code[code[fp+1]] * code[code[fp+2]]
            fp += 4
        if code[0] == 19690720:
            print(i,j)
            exit(0)
