with open('day11.txt') as f:
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
                    if inpt != None:
                        code[args[0][0]+self.rb] = inpt

                    self.ip += 2
                elif opcode == DUMP:
                    self.out = self.p(args[0])
                    self.ip += 2
                    return
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

painted_points = {}
intc = IntCode()
# TURTLE GRAPHICSSSSS
loc = [0,0]
painted_points[tuple(loc)] = 1
headings = [(0,1), (1,0), (0,-1), (-1,0)]
heading = 0
while not intc.halt:
    if tuple(loc) not in painted_points.keys():
        painted_points[tuple(loc)] = 0
    
    intc.run(painted_points[tuple(loc)])
    color = intc.out
    
    painted_points[tuple(loc)] = color
    
    intc.run()
    rot = intc.out

    # Rotate bot
    if rot == 1:
        heading = (heading + 1) % len(headings)
    elif rot == 0:
        heading = (heading - 1) % len(headings)
    
    loc[0] += headings[heading][0]
    loc[1] += headings[heading][1]

# Ironically displaying the answer might end up being the hardest part...
min_x = min([s[0] for s in painted_points.keys()])
min_y = min([s[1] for s in painted_points.keys()])
max_x = max([s[0] for s in painted_points.keys()])
max_y = max([s[1] for s in painted_points.keys()])

hull = []
for _ in range(max_y - min_y +1):
    hull.append([0] * (max_x - min_x+1))

for pt, v in painted_points.items():
    try:
        # offset cords by minimum
        y = pt[1] + abs(min_y)
        x = pt[0] + abs(min_x)
        hull[y][x] = v
    except IndexError as e:
        print(pt)
        print("Shit's fucked - ({},{})".format(pt[1],pt[0]))

for h in hull[::-1]:
    for c in range(len(h)):
        if h[c] == 0:
            h[c] = ' '
        else:
            h[c] = 'X'
    print(''.join(map(str,h)))

# Just gonna ignore the fact that this seems to print an extra point.