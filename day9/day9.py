with open('day9.txt') as f:
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
RB = 9
HALT = 99

class Booster:
    
    def __init__(self):
        self.code = c[:]
        self.ip = 0
        self.rb = 0

    def p(self, arg):
        while True:
            try:
                if arg[1] == 0:
                    return self.code[arg[0]]
                elif arg[1] == 1:
                    return arg[0]
                elif arg[1] == 2:
                    return self.code[arg[0]+self.rb]
            except IndexError:
                self.code.append(0)

    def run(self):
        code=self.code
        while self.ip < len(code):
            try:
                # Process instruction
                i = str(code[self.ip])
                opcode = int(''.join(i[-2:]))
                pmods = list(map(int, i[-3::-1]))        # get parameter modes
                pmods.extend([0] * (3-len(pmods)))       # pad w/ 0s
                args = list(zip(code[self.ip+1:self.ip+4], pmods)) # bind parameter modes to params
                #print(self.ip, ':', opcode, args, ',', self.rb)
                # Run the op
                if opcode == ADD:
                    if args[2][1] == 2:
                        code[args[2][0]+self.rb] = self.p(args[0]) + self.p(args[1])
                    else:
                        code[args[2][0]] = self.p(args[0]) + self.p(args[1])
                    self.ip += 4
                elif opcode == MULTIPLY:
                    if args[2][1] == 2:
                        code[args[2][0]+self.rb] = self.p(args[0]) * self.p(args[1])
                    else:
                        code[args[2][0]] = self.p(args[0]) * self.p(args[1])
                    self.ip += 4
                elif opcode == STORE:
                    code[args[0][0]+self.rb] = int(input("Enter an int pls: "))
                    #print('code[1000]:',code[1000])
                    self.ip += 2
                elif opcode == DUMP:
                    print(self.p(args[0]))
                    self.ip += 2
                elif opcode == JT:
                    if self.p(args[0]):
                        self.ip = self.p(args[1])
                    else:
                        self.ip += 3
                elif opcode == JF:
                    if not self.p(args[0]):
                        self.ip = self.p(args[1])
                    else:
                        self.ip += 3
                elif opcode == LT:
                    if self.p(args[0]) < self.p(args[1]):
                        if args[2][1] == 2:
                            code[args[2][0]+self.rb] = 1
                        else:
                            code[args[2][0]] = 1
                    else:
                        if args[2][1] == 2:
                            code[args[2][0]+self.rb] = 0
                        else:
                            code[args[2][0]] = 0
                    self.ip += 4
                elif opcode == EQ:
                    if self.p(args[0]) == self.p(args[1]):
                        if args[2][1] == 2:
                            code[args[2][0]+self.rb] = 1
                        else:
                            code[args[2][0]] = 1
                    else:
                        if args[2][1] == 2:
                            code[args[2][0]+self.rb] = 0
                        else:
                            code[args[2][0]] = 0
                    self.ip += 4
                elif opcode == RB:
                    #print(self.ip, ':', opcode, args, ',', self.rb)
                    self.rb += self.p(args[0])
                    #print('rb:',self.rb)
                    self.ip += 2 
                elif opcode == HALT:
                    return
                elif opcode == 0:
                    #print(code)
                    print("Something's royally hecked up.")
                    return
            except IndexError:
                code.append(0)

b = Booster()
b.run()