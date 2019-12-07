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

class Accelerator:
    
    def __init__(self, phase):
        self.code = c[:]
        self.phase = phase
        self.out = 0
        self.ip = 0
        self.phase_used = False

    def run(self, sig):
        code=self.code
        while self.ip < len(code):
            # Process instruction
            i = str(code[self.ip])
            opcode = int(''.join(i[-2:]))
            pmods = list(map(int, i[-3::-1]))        # get parameter modes
            pmods.extend([0] * (3-len(pmods)))       # pad w/ 0s
            args = list(zip(code[self.ip+1:self.ip+4], pmods)) # bind parameter modes to params

            # Run the op
            if opcode == ADD:
                code[code[self.ip+3]] = p(code,args[0]) + p(code,args[1])
                self.ip += 4
            elif opcode == MULTIPLY:
                code[code[self.ip+3]] = p(code,args[0]) * p(code,args[1])
                self.ip += 4
            elif opcode == STORE:
                if not self.phase_used:
                    code[code[self.ip+1]] = self.phase
                    self.phase_used = True
                else:
                    code[code[self.ip+1]] = sig
                self.ip += 2
            elif opcode == DUMP:
                self.out = p(code, args[0])
                self.ip += 2
                return self.out
            elif opcode == JT:
                if p(code,args[0]):
                    self.ip = p(code,args[1])
                else:
                    self.ip += 3
            elif opcode == JF:
                if not p(code,args[0]):
                    self.ip = p(code,args[1])
                else:
                    self.ip += 3
            elif opcode == LT:
                if p(code,args[0]) < p(code,args[1]):
                    code[code[self.ip+3]] = 1
                else:
                    code[code[self.ip+3]] = 0
                self.ip += 4
            elif opcode == EQ:
                if p(code,args[0]) == p(code,args[1]):
                    code[code[self.ip+3]] = 1
                else:
                    code[code[self.ip+3]] = 0
                self.ip += 4
            elif opcode == HALT:
                return -1


perms = itertools.permutations(range(5,10))
biggest = -1
for i in perms:
    accels = [Accelerator(p) for p in i]
    s =accels[0].run(0)
    j = 1
    while s != -1:
        s = accels[j].run(s)
        j = (j+1)%5
    if accels[4].out > biggest:
        biggest = accels[4].out
print(biggest)