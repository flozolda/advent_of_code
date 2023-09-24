
import re

total_code = 0
total_memory = 0

with open("input.txt") as f:
    contents = f.readlines()
    for c in contents:
        if len(c.strip()) == 2:
            total_code += len(c.strip())
        else:
            total_code += len(c.strip())
            temp = c[1:-2].strip()
            print("asd")
            print(b'{}'.format(temp).decode("ascii"))
            temp = temp.replace(r"\"",r'"')
            print(temp)
            while temp.find(r"\x"):
                print("found")
                s = temp.find(r"\x")
                print("aaaaaa")
                print(temp)
                print(temp[:s])
                print(temp[s+1:])
                temp = temp[:s] + temp[s+1:]
                #print(temp)
                exit()
            asd = temp.replace(r"\x",r"\"")
            temp = temp.replace(r"\\",'\\')
            total_memory += len(c[1:-2].strip())
        print(total_code)