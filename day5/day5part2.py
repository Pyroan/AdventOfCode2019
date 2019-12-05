with open('day5.txt') as f:
    code = list(map(int, f.readline().split(',')))

# Opcodes
ADD = 1
MULTIPLY = 2
STORE = 3
DUMP = 4
JT = 5
JF = 6
LT = 7
EQ = 8
HALT = 99

def p(arg: int, pm: int = 0):
    if pm == 0:
        return int(code[int(code[arg])])
    elif pm == 1:
        return int(code[arg])

ip = 0 # instruction pointer    

while ip < len(code):
    # Process instruction
    i = str(code[ip])
    opcode = int(''.join(i[-2:]))
    argpms = list(map(int, i[-3::-1])) # i <3 slices
    argpms.extend([0] * (3-len(argpms)))  # pad with zeroes bc i'm too lazy to think of better solution
    #print("IP:", ip, "Instruction:", opcode, argpms)

    # Run the op
    if opcode == ADD:
        code[code[ip+3]] = p(ip+1, argpms[0]) + p(ip+2, argpms[1])
        ip += 4
    elif opcode == MULTIPLY:
        code[code[ip+3]] = p(ip+1, argpms[0]) * p(ip+2, argpms[1])
        ip += 4
    elif opcode == STORE:
        code[code[ip+1]] = int(input("Enter an int pls: "))
        ip += 2
    elif opcode == DUMP:
        print(p(ip+1, argpms[0]))
        ip += 2
    elif opcode == JT:
        if p(ip+1, argpms[0]):
            ip = p(ip+2, argpms[1])
        else:
            ip += 3
    elif opcode == JF:
        if not p(ip+1, argpms[0]):
            ip = p(ip+2, argpms[1])
        else:
            ip += 3
    elif opcode == LT:
        if p(ip+1, argpms[0]) < p(ip+2, argpms[1]):
            code[code[ip+3]] = 1
        else:
            code[code[ip+3]] = 0
        ip += 4
    elif opcode == EQ:
        if p(ip+1, argpms[0]) == p(ip+2, argpms[1]):
            code[code[ip+3]] = 1
        else:
            code[code[ip+3]] = 0
        ip += 4
    elif opcode == HALT:
        exit()

    # CORE DUMPPPP
    #print(code)