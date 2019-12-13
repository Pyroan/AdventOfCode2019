# Includes a bunch of extra crap bc like an idiot i didn't immediately think to make a bot
with open('day13.txt') as f:
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

class IntCode:
    
    def __init__(self):
        self.code = c[:]
        self.ip = 0
        self.rb = 0
        self.out = 0
        self.halt = False

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

    def run(self, inpt=None):
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
                    #drawfield()
                    #inpt = int(input("Next move... "))# uncomment to play manually
                    b = get_ball_x()
                    pad = get_paddle_x()
                    if b > pad:
                        inpt = 1
                    elif b < pad:
                        inpt = -1
                    else:
                        inpt = 0
                    if args[1][1]== 2:
                        code[args[0][0]+self.rb] = inpt
                    else:
                        code[args[0][0]] = inpt

                    self.ip += 2
                elif opcode == DUMP:
                    self.out = self.p(args[0])
                    self.ip += 2
                    return self.out
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
                    self.halt=True
                    return
                else:
                    #print(code)
                    print("Something's royally hecked up. (Opcode {})".format(opcode))
                    return
            except IndexError:
                code.append(0)

EMPTY = 0
WALL = 1
BLOCK = 2
HPAD = 3
BALL = 4
intc = IntCode()
intc.code[0] = 2
tiles = {}
scores = set()

def get_ball_x():
    for k,v in tiles.items():
        if v == BALL:
            return int(k.split(',')[0])
    return -1

def get_paddle_x():
    for k, v in tiles.items():
        if v == HPAD:
            return int(k.split(',')[0])
    return -1

def drawfield():
    max_y = max([int(k.split(',')[1]) for k in tiles])+1
    max_x = max([int(k.split(',')[0]) for k in tiles])+1
    field = []
    for _ in range(max_y):
        field.append([0] * max_x)
    field.append(0)

    for k in tiles:
        x,y = map(int, k.split(','))
        try:
            if x == -1 and y == 0:
                field[max_y] = tiles['-1,0']
            else:
                    field[y][x] = tiles[k]
        except IndexError as e:
            print (e, max_y)

    for i in field[:-1]:
        s = ''
        for j in i:
            if j == EMPTY:
                s += ' '
            elif j == WALL:
                s += '#'
            elif j == BLOCK:
                s += 'X'
            elif j == HPAD:
                s += '='
            elif j == BALL:
                s += 'O'
            else:
                print('something is hecked up')
                exit(0)
        s += '\n'
    print(s)
    print("Score:",field[-1])
    scores.add(field[-1])

while intc.halt == False:
    x = intc.run()
    y = intc.run()
    tile = intc.run()
    if x != None:
        tiles[str(x)+','+str(y)] = tile
print("Score:", tiles["-1,0"])
print("Remaining Blocks: " + str(sum(1 if v == BLOCK else 0 for k,v in tiles.items())))