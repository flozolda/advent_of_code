from collections import Counter
from functools import reduce
import re

rx = r"\b(?:\w*[aeiou]){3}\w*"
counter = 0

def double_letters(word):
    for i in range (len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False

def double_letter_w_space(word):
    for i in range (len(word)-2):
      if word[i] == word[i+2]:
          return True
    return False

def double_letters_twice(word):
    for i in range (len(word)-1):
      temp_string = f"{word[i]}{word[i+1]}"
      if word.count(temp_string)>1:
        return True
    return False

with open("input.txt") as f:
    contents = f.readlines()

#part 1
for c in contents:
  # print(c)
  if "ab" in c or "cd" in c or "pq" in c or "xy" in c:
    continue
  if double_letters(c):
    if len(re.findall(rx, c))>0:
      counter +=1

print("Part 1")
print(counter)

counter = 0

#part 2
for c in contents:
  if double_letter_w_space(c) and double_letters_twice(c):
    counter +=1

print("part 2")
print(counter)