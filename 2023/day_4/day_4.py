res = 0

with open("input.txt") as f:
    contents = f.readlines()
    for c in contents:
        winners = 0
        add_res = 1
        numbers = c.strip().split(":")[1].split("|")
        winning = numbers[0].split(" ")
        your = numbers[1].split(" ")
        winning = list(filter(None, winning))
        your = list(filter(None, your))
        for y in your:
            if y in winning:
                winners += 1
        if winners > 0:
            for i in range(1,winners):
                add_res *= 2
            res += add_res
print("Part #1")
print(res)
print("Part #2")
scratch_dict = {}
copies = []

with open("input.txt") as f:
    contents = f.readlines()
    for i,c in enumerate(contents):
        #print("Current Card")
        winners = 0
        temp = c.strip().split(":")[0].split(" ")
        temp = list(filter(None, temp))
        card_num = int(temp[1])
        #print(card_num)
        scratch_dict[card_num] = 1
        numbers = c.strip().split(":")[1].split("|")
        winning = numbers[0].split(" ")
        your = numbers[1].split(" ")
        winning = list(filter(None, winning))
        your = list(filter(None, your))
        
        for y in your:
            if y in winning:
                winners += 1
        if winners > 0:
            io = 0
            while io < winners:
                copies.append(contents[card_num+io])
                io +=1
index = 0

while index < len(copies):
    #print("Current Card")
    c = copies[index]
    winners = 0
    temp = c.strip().split(":")[0].split(" ")
    temp = list(filter(None, temp))
    card_num = int(temp[1])
    scratch_dict[card_num] += 1
    #print(card_num)
    numbers = c.strip().split(":")[1].split("|")
    winning = numbers[0].split(" ")
    your = numbers[1].split(" ")
    winning = list(filter(None, winning))
    your = list(filter(None, your))
    
    for y in your:
        if y in winning:
            winners += 1
    if winners > 0:
        io = 0
        while io < winners:
            copies.append(contents[card_num+io])
            io +=1
    index += 1

print(scratch_dict)
res_part2 = 0
for j in scratch_dict:
    res_part2 += scratch_dict[j]
print(res_part2)