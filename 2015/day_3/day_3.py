from collections import Counter
with open("input.txt") as f:
    contents = f.readlines()

x=0
y=0
x1=0
y1=0
list_houses = []
list_houses.append(f"{x},{y}")
list_houses1 = []
list_houses1.append(f"{x1},{y1}")

robo = False

for c in contents:
  stripped = c.strip()
  #print(stripped)
  for dirs in stripped:
    #print(dirs)
    if robo:
      match dirs:
        case "<":
          x1 -= 1
        case ">":
          x1 += 1
        case "^":
          y1 += 1
        case "v":
          y1 -= 1
      list_houses1.append(f"{x1},{y1}")
    if not robo:
      match dirs:
        case "<":
          x -= 1
        case ">":
          x += 1
        case "^":
          y += 1
        case "v":
          y -= 1
      list_houses.append(f"{x},{y}")
    robo = not robo

#print(list_houses)
counter = 0

list_houses.extend(list_houses1)

a = dict(Counter(list_houses))
for k,v in a.items():
  if v > 0:
    counter +=1
print(counter)