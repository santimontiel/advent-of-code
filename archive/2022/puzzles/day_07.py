from typing import List

# Read puzzle.
with open("../data/day_07.txt", "r") as file:
    content = list(map(lambda x: x.rstrip(), file.readlines()))

def absolute_dir_path(chunks: List) -> str:
    return ''.join([chunk + "/" if i!=0 else chunk for i, chunk in enumerate(chunks)])

curr_dir = []
dir_size = {"/": 0}
for line in content:

    splitted = line.split(" ")
    # If it is a command.
    if line.startswith("$"):
        if splitted[1] == "cd":
            if splitted[2] != "..":
                curr_dir.append(splitted[2])
            else:
                curr_dir.pop()
        elif splitted[1] == "ls":
            pass
    
    # If it is a lecture of ls
    elif line.startswith("dir"):
        dir_size[absolute_dir_path(curr_dir + [splitted[1]])] = 0
    else:
        aux_dir = curr_dir.copy()
        dir_size[absolute_dir_path(curr_dir)] += int(splitted[0])
        while(len(aux_dir) != 1):
            aux_dir.pop()
            dir_size[absolute_dir_path(aux_dir)] += int(splitted[0])

sof = 0
for k, v in dir_size.items():
    if v <= 100000:
        sof += v
print(sof)

# Part 2.
dir_sizes = sorted([v for k, v in dir_size.items()])
for el in dir_sizes:
    if dir_size["/"] - el < 70000000 - 30000000:
        print(el)
        break