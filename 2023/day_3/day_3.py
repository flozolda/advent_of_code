map = []
res = 0
sum_where = {}

with open("input.txt") as f:
    contents = f.readlines()
    for c in contents:
        map.append(list(c.strip()))

for i in range(0,len(map)):
    found_num = ""
    sum_up = False
    last = ""
    for j in range(0,len(map[i])):
        if map[i][j] == "." or not map[i][j].isnumeric():
            if sum_up == True:
                #print(found_num)
                res += int(found_num)
                sum_up = False
                #print(found_num)
                l = last.split(",")
                if l[0] not in sum_where:
                    sum_where[l[0]] = {}
                if l[1] not in sum_where[l[0]]:
                    sum_where[l[0]][l[1]] = []
                sum_where[l[0]][l[1]].append(found_num)
                found_num = ""
            if not map[i][j] == "." and not map[i][j].isnumeric() and found_num:
                res += int(found_num)
                found_num = ""
                sum_up = False
            if found_num:
                found_num = ""
            continue
        if map[i][j].isnumeric():
            found_num += str(map[i][j])
        if j == len(map[i])-1 and sum_up == True:
            res += int(found_num)
            l = last.split(",")
            if l[0] not in sum_where:
                sum_where[l[0]] = {}
            if l[1] not in sum_where[l[0]]:
                sum_where[l[0]][l[1]] = []
            sum_where[l[0]][l[1]].append(found_num)
        if sum_up == True:
            continue
        #check left
        if j-1 >= 0:
            if map[i][j-1] != "." and not map[i][j-1].isnumeric():
                sum_up = True
                last = f"{i},{j-1}"
        #check right
        if j+1 < len(map[i]):
            if map[i][j+1] != "." and not map[i][j+1].isnumeric():
                sum_up = True
                last = f"{i},{j+1}"
        #check up
        if i-1 >= 0:
            if map[i-1][j] != "." and not map[i-1][j].isnumeric():
                sum_up = True
                last = f"{i-1},{j}"
        #check down
        if i+1 < len(map):
            if map[i+1][j] != "." and not map[i+1][j].isnumeric():
                sum_up = True
                last = f"{i+1},{j}"
        #check top left
        if i-1 >= 0 and j-1 >= 0:
            if map[i-1][j-1] != "." and not map[i-1][j-1].isnumeric():
                sum_up = True
                last = f"{i-1},{j-1}"
        #check top right
        if i-1 >= 0 and j+1 < len(map[i]):
            if map[i-1][j+1] != "." and not map[i-1][j+1].isnumeric():
                sum_up = True
                last = f"{i-1},{j+1}"
        #check bottom left
        if i+1 < len(map) and j-1 >= 0:
            if map[i+1][j-1] != "." and not map[i+1][j-1].isnumeric():
                sum_up = True
                last = f"{i+1},{j-1}"
        #check bottom right
        if i+1 < len(map) and j+1 < len(map[i]):
            if map[i+1][j+1] != "." and not map[i+1][j+1].isnumeric():
                sum_up = True
                last = f"{i+1},{j+1}"
print("Part 1")
print(res)
res = 0

for i in range(0,len(map)):
    for j in range(0,len(map[i])):
            if map[i][j] == "*":
                bool_list = []
                bool_list.append(False) #0left
                bool_list.append(False) #1right
                bool_list.append(False) #2up
                bool_list.append(False) #3down
                bool_list.append(False) #4topleft
                bool_list.append(False) #5topright
                bool_list.append(False) #6bottomleft
                bool_list.append(False) #7bottomright
                #check left
                if j-1 >= 0:
                    if map[i][j-1].isnumeric():
                        bool_list[0] = True
                #check right
                if j+1 < len(map[i]):
                    if map[i][j+1].isnumeric():
                        bool_list[1] = True
                #check up
                if i-1 >= 0:
                    if map[i-1][j].isnumeric():
                        bool_list[2] = True
                #check down
                if i+1 < len(map):
                    if map[i+1][j].isnumeric():
                         bool_list[3] = True
                if bool_list.count(True) > 2:
                    continue

                #check top left
                if i-1 >= 0 and j-1 >= 0:
                    if map[i-1][j-1].isnumeric() and map[i-1][j]==".":
                        bool_list[4] = True
                #check top right
                if i-1 >= 0 and j+1 < len(map[i]):
                    if map[i-1][j+1].isnumeric() and map[i-1][j]==".":
                        bool_list[5] = True
                #check bottom left
                if i+1 < len(map) and j-1 >= 0:
                    if map[i+1][j-1].isnumeric() and map[i+1][j]==".":
                        bool_list[6] = True
                #check bottom right
                if i+1 < len(map) and j+1 < len(map[i]):
                    if map[i+1][j+1].isnumeric() and map[i+1][j]==".":
                        bool_list[7] = True
                if bool_list.count(True) == 2:
                    #print(sum_where)
                    temp_dict = {}
                    print(sum_where)
                    for x,y in sum_where.items():
                        for j,k in y.items():
                            if len(k) == 2:
                                res += int(k[0]) * int(k[1])
                                sum_where[x][j] = []
                else:
                    continue
print("Part 2")
print(res)