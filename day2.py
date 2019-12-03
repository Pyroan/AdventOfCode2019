with open('day2.txt') as f:
    code = list(map(int, f.readline().split(',')))

code[1] = 12
code[2] = 2
fp = 0
while code[fp] != 99:
    if code[fp] == 1:
        code[code[fp+3]] = code[code[fp+1]] + code[code[fp+2]]
    elif code[fp] == 2:
        code[code[fp+3]] = code[code[fp+1]] * code[code[fp+2]]
    fp += 4
print(code[0])