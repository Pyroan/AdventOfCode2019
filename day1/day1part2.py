total_fuel = 0
with open('day1.txt') as f:
    for line in f.readlines():
        module = int(line)
        fuel = max(module // 3 - 2, 0)
        last_fuel = fuel
        while last_fuel > 0:
            last_fuel = max(last_fuel // 3 - 2, 0)
            fuel += last_fuel
        total_fuel += fuel
print(total_fuel)