import re
part_1 = 0

#part1

# with open("input.txt") as f:
#    contents = f.readlines()
#    for c in contents:
#        #print(c)
#        nums = re.sub('\D', '', c)
#        line_res = str(nums[0]) + str(nums[-1])
#        part_1 += int(line_res)

# print(part_1)

#part2

part_2 = 0

num_dict = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

with open("input.txt") as f:
    contents = f.readlines()
    for c in contents:
        #temp = c[:4]
        #for x in range(4,len(c)):
            #temp = temp + c[x:x+1]
            #for n,k in num_dict.items():
                #temp = temp.replace(str(n),str(k))
            #print(temp)
        temp = c
        print(temp.find("one"))
        for n,k in num_dict.items():
            while temp.find(n) != -1:
                print(temp.find(n))
                index = temp.find(n)+1
                temp = temp[:index] + str(k) + temp[index + 1:]

        nums = re.sub('\D', '', temp)
        print(nums)
        line_res = str(nums[0]) + str(nums[-1])
        #print(line_res)
        part_2 += int(line_res)

print(part_2)