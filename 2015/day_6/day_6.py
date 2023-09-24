from collections import Counter

grid = [[False]*4]*4
print(grid)

def turn_on(grid,instr):
    action_list = instr.strip().split()
    action = action_list[0]
    extra = 0
    if action == "turn":
        extra = 1
    startcord =  list(map(int, action_list[1+extra].split(",")))
    endcord = list(map(int, action_list[3+extra].split(",")))

    for i in range(startcord[0],endcord[0]):
        print(i)
        for j in range(startcord[1],endcord[1]):
            print(j)
            grid[i][j]=True


with open("input.txt") as f:
    contents = f.readlines()
    for c in contents:
        turn_on(grid, c)

counter = 0

for i in grid:
    for j in i:
        if j == True:
            counter +=1
print(grid)
print(counter)