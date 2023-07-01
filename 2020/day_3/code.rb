require "awesome_print"

map = []

File.open("input.txt", "r") do |f|
  f.each_line do |line|
    map.push(line.strip.split(""))
  end
end

# ap map

# horz = 0
# counter = 0
# index = vertical val
# Part 1
=begin
map.each_with_index do |val,i|
    break if (i+1 > map.length-1)
    row_size = val.length()
    horz = (horz+3) % row_size
    counter +=1 if(map[i+1][horz] == "#")
end

ap counter
=end

def tree_checker(map,right,down)
  horz = 0
  counter = 0
  vert = down
  map.each_with_index do |val, _i|
    break if vert > map.length - 1

    row_size = val.length
    horz = (horz + right) % row_size
    counter += 1 if map[vert][horz] == "#"
    vert += down
  end
  counter
end

ap(
  tree_checker(map, 1, 1) *
  tree_checker(map, 3, 1) *
  tree_checker(map, 5, 1) *
  tree_checker(map, 7, 1) *
  tree_checker(map, 1, 2)
)
