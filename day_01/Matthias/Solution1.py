total_fuel = 0

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = int(line)
        fuel_per_module = round((line/3)-0.5)-2
        total_fuel += fuel_per_module
        while fuel_per_module > 0:
            fuel_per_module = round((fuel_per_module/3)-0.5)-2
            if fuel_per_module >= 0:
                total_fuel += fuel_per_module
            print fuel_per_module
print total_fuel
