import os 



from pathlib import Path

path_to_2023 = str(Path.cwd()) + "\\2023"

print(path_to_2023)
#print(f"{Path.cwd()}\\2023")

for x in range(1,25):
  #print(x)
  day_path = path_to_2023 + f"\\day_{x}"
  #print(day_path)
  os.mkdir(day_path)
  md = day_path + f"\\day_{x}.md"
  py = day_path + f"\\day_{x}.py"
  txt = day_path + "\\input.txt"
  f = open(md,"x")
  f = open(txt,"x")
  f = open(py,"x")