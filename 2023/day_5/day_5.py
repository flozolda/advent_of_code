with open("input.txt") as f:
    contents = f.readlines()
    mode = ""
    master_dict = {}
    for c in contents:
        #print(c)
        if c == "\n":
            mode = ""
            continue
        if mode and ":" not in c:
            if mode not in master_dict:
                master_dict[mode] = []
            nums = c.strip().split()
            #print(mode)
            #print(nums)
            a = {}
            a["dest"] = int(nums[0])
            a["source"] = int(nums[1])
            a["steps"] = int(nums[2])
            master_dict[mode].append(a)
        else:
            if ":" in c: # means textline
                if "seeds:" in c:
                    seeds = c.strip().split(":")[1].split(" ")
                    seeds = list(filter(None, seeds))
                    master_dict["seeds"] = seeds
                else:
                    match c.strip():
                        case "seed-to-soil map:":
                            mode = "seed-to-soil map"
                            #print("stsm")
                        case "soil-to-fertilizer map:":
                            mode = "soil-to-fertilizer map"
                            #print("stfm")
                        case "fertilizer-to-water map:":
                            mode = "fertilizer-to-water map"
                            #print("ftsw")
                        case "water-to-light map:":
                            mode = "water-to-light map"
                            #print("wtlm")
                        case "light-to-temperature map:":
                            mode = "light-to-temperature map"
                            #print("wtl")
                        case "temperature-to-humidity map:":
                            mode = "temperature-to-humidity map"
                            #print("tth")
                        case "humidity-to-location map:":
                            mode = "humidity-to-location map"
                            #print("htlm")
            else: #means not defined line since all \n skipped and nums are caught with mode
                print("Else path")

#print(master_dict["humidity-to-location map"])
#print(master_dict)
location = 999999999999999999999
for s in master_dict["seeds"]:
    temp = int(s)
    #print(temp)
    #print(f"{temp} seed")
    for o in master_dict["seed-to-soil map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    for o in master_dict["soil-to-fertilizer map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    for o in master_dict["fertilizer-to-water map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    for o in master_dict["water-to-light map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    for o in master_dict["light-to-temperature map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    for o in master_dict["temperature-to-humidity map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    for o in master_dict["humidity-to-location map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    #print(temp)
    if temp < location:
        location = temp

print(f"Part 1: {location}")

master_seeds = []

with open("input.txt") as f:
    contents = f.readlines()
    mode = ""
    master_dict = {}
    for c in contents:
        #print(c)
        if c == "\n":
            mode = ""
            continue
        if mode and ":" not in c:
            if mode not in master_dict:
                master_dict[mode] = []
            nums = c.strip().split()
            #print(mode)
            #print(nums)
            a = {}
            a["dest"] = int(nums[0])
            a["source"] = int(nums[1])
            a["steps"] = int(nums[2])
            master_dict[mode].append(a)
        else:
            if ":" in c: # means textline
                if "seeds:" in c:
                    c = c.strip()
                    seeds = c.split(":")[1].strip().split(" ")

                    for i in range(0,len(seeds),2):
                        tempo = {}
                        tempo["start"]=int(seeds[i])
                        tempo["steps"]=int(seeds[i+1])
                        master_seeds.append(tempo)
                else:
                    match c.strip():
                        case "seed-to-soil map:":
                            mode = "seed-to-soil map"
                            #print("stsm")
                        case "soil-to-fertilizer map:":
                            mode = "soil-to-fertilizer map"
                            #print("stfm")
                        case "fertilizer-to-water map:":
                            mode = "fertilizer-to-water map"
                            #print("ftsw")
                        case "water-to-light map:":
                            mode = "water-to-light map"
                            #print("wtlm")
                        case "light-to-temperature map:":
                            mode = "light-to-temperature map"
                            #print("wtl")
                        case "temperature-to-humidity map:":
                            mode = "temperature-to-humidity map"
                            #print("tth")
                        case "humidity-to-location map:":
                            mode = "humidity-to-location map"
                            #print("htlm")
            else: #means not defined line since all \n skipped and nums are caught with mode
                print("Else path")

#print(master_dict["humidity-to-location map"])
#print(master_dict)

#create a reverse lookup, go from locations to seeds

filtered_seeds = []
location = 99999999999999999999999
def seed_checker(master_seeds,seed):#
    temp = False
    for s in master_seeds:
        s_start = s["start"]
        s_steps = s["steps"]
        if seed > s_start and seed < s["start"]+s["steps"]:
            temp = True
    return temp

i = 0
while True:
    temp = int(i)
    #print(temp)
    #print(f"{temp} seed")
    for o in master_dict["seed-to-soil map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    for o in master_dict["soil-to-fertilizer map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    for o in master_dict["fertilizer-to-water map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    for o in master_dict["water-to-light map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    for o in master_dict["light-to-temperature map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    for o in master_dict["temperature-to-humidity map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    for o in master_dict["humidity-to-location map"]:
        #print(o)
        #print(temp)
        if o["source"]+o["steps"] >= temp and temp >= o["source"]:
            temp = temp + (o["dest"]-o["source"])
            break
    i += 1
    if temp < location and seed_checker(master_seeds,i):
        print(i)
        location = temp
        print("New Location")
        print(location)

print(f"Part 2: {location}")