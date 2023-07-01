require "awesome_print"

preamble = 25
num_arr = []

File.open("input.txt", "r") do |f|
  f.each_line do |line|
    num_arr << line.to_i
  end
end

def find_num(num_array, value)
  num_array.each do |val|
    num_array.each do |val1|
        return true if val + val1 == value
    end
  end

  false
end

def sum_num(num_array,start_index,goal_value)
  goal_arr = []
  sum = 0
  (start_index..num_array.length()).each do |i|
    sum += num_array[i]
    goal_arr << num_array[i]
    if sum == goal_value
      return goal_arr
    end

    return nil if sum > goal_value
  end
end

false_val = 0
# Part 1
num_arr.each_with_index do |value, index|
  next if index < preamble

  start_index = index - preamble

  temp_arr = []

  (start_index..index-1).each do |i|
    temp_arr << num_arr[i]
  end
  if find_num(temp_arr,value) == false
    false_val = value
    break
  end
end

# Part 2
num_arr.each_with_index do |value, index|
  res = sum_num(num_arr,index,false_val)
  unless res.nil?
    ap res.min + res.max
    break
  end
end