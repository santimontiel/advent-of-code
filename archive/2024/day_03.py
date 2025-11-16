with open("day_03_input.txt") as f:
    data = f.read().splitlines()

# Part 1.
count = 0
for line in data:
    for i in range(len(line) - 3):
        substr = line[i:i+3]
        postfix = ""
        if substr == "mul":
            op, j = True, 1
            while op:
                if i+3+j > len(line):
                    op = False
                elif line[i+3+j] in ["(", ")", ","] or line[i+3+j].isdigit():
                    postfix += line[i+3+j]
                    j += 1
                else:
                    op = False
                    
                if line[i+3+j] == ")":
                    op = False
                    try:
                        t = eval(postfix)
                    except:
                        continue
                    if isinstance(t, tuple):
                        count += t[0] * t[1]
print(count)
            
# Part 2.
count = 0
condition = True

for line in data:
    for i in range(len(line) - 3):

        if i < len(line) - 4:
            substr_do = line[i:i+4]
            if substr_do == "do()":
                condition = True

        if i < len(line) - 7:
            substr_do = line[i:i+7]
            if substr_do == "don't()":
                condition = False   

        substr_mul = line[i:i+3]
        postfix = ""
        if substr_mul == "mul" and condition:
            op, j = True, 1
            while op:
                if i+3+j > len(line):
                    op = False
                elif line[i+3+j] in ["(", ")", ","] or line[i+3+j].isdigit():
                    postfix += line[i+3+j]
                    j += 1
                else:
                    op = False
                    
                if line[i+3+j] == ")":
                    op = False
                    try:
                        t = eval(postfix)
                    except:
                        continue
                    if isinstance(t, tuple):
                        count += t[0] * t[1]
print(count)