import hashlib

from collections import Counter
with open("input.txt") as f:
    contents = f.readlines()[0]

num = 1
while True:
  temp = contents+str(num)
  result = hashlib.md5(temp.encode('utf-8')).hexdigest()
  if result[0] == "0" and result[1] == "0" and result[2] == "0" and result[3] == "0" and result[4] == "0" and result[5] == "0":
    break
  
  num += 1



# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(num)
print(result)