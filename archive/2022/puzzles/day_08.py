# Read puzzle.
with open("../data/day_08.txt", "r") as file:
    content = list(map(lambda x: list(x.rstrip()), file.readlines()))
    content = list(map(lambda x: [eval(i) for i in x], content))

# Part 1.
def is_edge(i, j, grid):
    if i == 0 or j == 0:
        return True
    if i == len(grid)-1 or j == len(grid[0])-1:
        return True
    return False

def get_sight_lines(i, j, grid):

    l = grid[i][:j]
    r = grid[i][j+1:]
    u = [grid[k][j] for k in range(0, i)]
    d = [grid[k][j] for k in range(i+1, len(grid))]
    return l, r, u, d

def is_visible(i, j, grid):
    if is_edge(i, j, grid):
        return True
    else:
        l, r, u, d = get_sight_lines(i, j, grid)
        if (sum([x < grid[i][j] for x in l]) == len(l)):
            return True
        if (sum([x < grid[i][j] for x in r]) == len(r)):
            return True
        if (sum([x < grid[i][j] for x in u]) == len(u)):
            return True
        if (sum([x < grid[i][j] for x in d]) == len(d)):
            return True
    return False

cnt = 0
for i, row in enumerate(content):
    for j, col in enumerate(row):
        if is_visible(i, j, content):
            cnt += 1
print(cnt)

# Part 2.
def compute_view_distances(i, j, grid):
    if is_edge(i, j, grid):
        return 0
    else:
        l, r, u, d = get_sight_lines(i, j, grid)
        l.reverse()
        u.reverse()

        partial_cnt = []
        for n in [l, r, u, d]:
            p_cnt = 0
            for el in n:
                if el < grid[i][j]:
                    p_cnt += 1
                else:
                    p_cnt += 1
                    break
            partial_cnt.append(p_cnt)
        
        x = 1
        for el in partial_cnt:
            x *= el
    return x
        
view_distances = []
for i, row in enumerate(content):
    for j, col in enumerate(row):
        if is_visible(i, j, content):
            view_distances.append(compute_view_distances(i, j, content))
print(max(view_distances))