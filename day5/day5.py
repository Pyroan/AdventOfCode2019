with open('day5.txt') as f:
    code = list(map(int, f.readline().split(',')))

# Opcodes
ADD = 1
MULTIPLY = 2
STORE = 3
DUMP = 4
HALT = 99

def p(arg):
    if arg[1] == 0:
        return code[arg[0]]
    elif arg[1] == 1:
        return arg[0]

ip = 0 # instruction pointer    

while ip < len(code):
    # Process instruction
    i = str(code[ip])
    opcode = int(''.join(i[-2:]))
    pmods = list(map(int, i[-3::-1]))        # get parameter modes
    pmods.extend([0]*(3-len(pmods)))         # pad w/ 0s
    args = list(zip(code[ip+1:ip+4], pmods)) # bind parameter modes to params

    # Run the op
    if opcode == ADD:
        code[code[ip+3]] = p(args[0]) + p(args[1])
        ip += 4
    elif opcode == MULTIPLY:
        code[code[ip+3]] = p(args[0]) * p(args[1])
        ip += 4
    elif opcode == STORE:
        code[code[ip+1]] = int(input("Enter an int pls: "))
        ip += 2
    elif opcode == DUMP:
        print(p(args[0]))
        ip += 2
    elif opcode == HALT:
        exit()
