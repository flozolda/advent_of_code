with open("input.txt") as f:
    contents = f.readlines()[0]
    start = 0
    for floor in range(0, len(contents)):
      if contents[floor] == "(":
        start += 1
      elif contents[floor] == ")":
        start -= 1
      if start == -1:
        print(floor)
        print(start+1)
        break
print(start)