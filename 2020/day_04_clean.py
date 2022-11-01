# Read puzzle.
with open("day_04_input.txt", "r") as puzzle:
    content = list(map(lambda x: x.rstrip(), puzzle.readlines()))

# Create a dictionary with every single passport.
passport, passports = {}, []
for line in content:
    if len(line) != 0:
        fields = line.split(" ")
        for field in fields:
            k, v = field.split(":")
            passport[k] = v
    else:
        passports.append(passport)
        passport = {}

# Part 1.
valid = 0
for passport in passports:
    if len(passport) == 8 or len(passport) == 7 and "cid" not in passport:
        valid += 1
print(f"Solution to part 1 is: {valid}")

# Part 2.
valid_counter = 0
for passport in passports:
    is_valid = [0, 0, 0, 0, 0, 0, 0]
    if len(passport) == 8 or len(passport) == 7 and "cid" not in passport:
        is_valid[0] = 1920 <= int(passport["byr"]) <= 2002
        is_valid[1] = 2010 <= int(passport["iyr"]) <= 2020
        is_valid[2] = 2020 <= int(passport["eyr"]) <= 2030
        if passport["hgt"][-2:] == "cm":
            is_valid[3] = 150 <= int(passport["hgt"][:-2]) <= 193
        if passport["hgt"][-2:] == "in":
            is_valid[3] = 50 <= int(passport["hgt"][:-2]) <= 76
        is_valid[4] = all(c.isdigit() or c in "#abcdef" for c in passport["hcl"]) and len(passport["hcl"]) == 7
        is_valid[5] = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        is_valid[6] = all(c.isdigit() for c in passport["pid"]) and len(passport["pid"]) == 9
        if sum(is_valid) == 7:
            valid_counter += 1
print(f"Solution to part 2 is: {valid_counter}")
    