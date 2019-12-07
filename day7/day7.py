import itertools
with open('day7.txt') as f:
    c = list(map(int, f.readline().split(',')))

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

def p(code,arg):
    if arg[1] == 0:
        return code[arg[0]]
    elif arg[1] == 1:
        return arg[0]

def run(phase, sig):
    ip = 0 # instruction pointer
    phase_used = False    
    code = c[:]
    while ip < len(code):
        # Process instruction
        i = str(code[ip])
        opcode = int(''.join(i[-2:]))
        pmods = list(map(int, i[-3::-1]))        # get parameter modes
        pmods.extend([0] * (3-len(pmods)))       # pad w/ 0s
        args = list(zip(code[ip+1:ip+4], pmods)) # bind parameter modes to params

        # Run the op
        if opcode == ADD:
            code[code[ip+3]] = p(code,args[0]) + p(code,args[1])
            ip += 4
        elif opcode == MULTIPLY:
            code[code[ip+3]] = p(code,args[0]) * p(code,args[1])
            ip += 4
        elif opcode == STORE:
            if not phase_used:
                code[code[ip+1]] = phase
                phase_used = True
            else:
                code[code[ip+1]] = sig
            ip += 2
        elif opcode == DUMP:
            return p(code,args[0])
        elif opcode == JT:
            if p(code,args[0]):
                ip = p(code,args[1])
            else:
                ip += 3
        elif opcode == JF:
            if not p(code,args[0]):
                ip = p(code,args[1])
            else:
                ip += 3
        elif opcode == LT:
            if p(code,args[0]) < p(code,args[1]):
                code[code[ip+3]] = 1
            else:
                code[code[ip+3]] = 0
            ip += 4
        elif opcode == EQ:
            if p(code,args[0]) == p(code,args[1]):
                code[code[ip+3]] = 1
            else:
                code[code[ip+3]] = 0
            ip += 4
        elif opcode == HALT:
            return -1
    return -1


perms = itertools.permutations(range(5))
biggest = -1
for i in perms:
    s = 0
    for j in i:
        s = run(j, s)
    if s > biggest:
        biggest = s
print(biggest)