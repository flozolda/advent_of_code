
#part 1

part_1_counter = 0


red_cap = 12
green_cap = 13
blue_cap = 14

with open("input.txt") as f:
    contents = f.readlines()
    for c in contents:
        game_valid = True
        row = c.strip().split(":")
        #print(row)
        game_id = int(row[0].split()[1])
        sub_games = row[1].split(";")
        #print(sub_games)
        cube_sets = sub_games[1].split(",")
        #print(cube_sets)
        #print(cube_sets[0].strip().split())
        #print(cube_sets)
        for sg in sub_games:
            cube_sets = sg.split(",")
            for s in cube_sets:
                #print(s)
                r = s.strip().split()
                num = int(r[0])
                match r[1]:
                    case "blue":
                        game_valid = False if num > blue_cap else True
                    case "red":
                        #print(num)
                        game_valid = False if num > red_cap else True
                    case "green":
                        game_valid = False if num > green_cap else True
                if game_valid == False:
                    break
            if game_valid == False:
                    break
        if game_valid == True:
            #print(f"{game_id} is valid")
            part_1_counter += game_id

#print(part_1_counter)

#part 2

part_2_counter = 0
with open("input.txt") as f:
    contents = f.readlines()
    for c in contents:
        red_cap = 0
        green_cap = 0
        blue_cap = 0
        row = c.strip().split(":")
        #print(row)
        game_id = int(row[0].split()[1])
        sub_games = row[1].split(";")
        #print(sub_games)
        cube_sets = sub_games[1].split(",")
        #print(cube_sets)
        #print(cube_sets[0].strip().split())
        #print(cube_sets)
        for sg in sub_games:
            cube_sets = sg.split(",")
            for s in cube_sets:
                #print(s)
                r = s.strip().split()
                num = int(r[0])
                match r[1]:
                    case "blue":
                        blue_cap = num if num > blue_cap else blue_cap
                    case "red":
                        red_cap = num if num > red_cap else red_cap
                    case "green":
                        green_cap = num if num > green_cap else green_cap
        #print(blue_cap)
        #print(red_cap)
        #print(green_cap)
        part_2_counter += (red_cap * green_cap * blue_cap)
        

print(part_2_counter)