with open("input.txt") as f:
    contents = f.readlines()

contents_nws = []
total_sqf = 0
total_ribbon = 0
for c in contents:
  stripped = c.strip()
  print(stripped)
  nums = stripped.split('x')
  l = int(nums[0])
  w = int(nums[1])
  h = int(nums[2])
  total_sqf += 2*(l*w)+2*(w*h)+2*(h*l)+min(l*w,w*h,h*l)
  s = tuple([l,w,h])
  s = sorted(s)
  print(s)
  total_ribbon += (s[0]+s[0]+s[1]+s[1])+(l*w*h)
print(total_sqf)
print(total_ribbon)


