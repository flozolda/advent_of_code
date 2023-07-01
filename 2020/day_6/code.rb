require "awesome_print"

group_num = 0
group_arr = []

File.open("input.txt", "r") do |f|
  f.each_line do |line|
    if line == "\n"
      group_num += 1
      next
    end
    group_arr[group_num] ||= []
    # Part 1 solution
    # group_arr[group_num] = (group_arr[group_num] + line.strip.split(""))
    group_arr[group_num].push(line.strip)
  end
end

counter = 0

# part 1
# group_arr.each do |arr|
# counter += arr.uniq.length
# end

# part 2
# ap group_arr

group_arr.each do |arr|
  temp_arr = []
  arr.each_with_index do |value, index|
    split_val = value.split("")
    if index.zero?
      temp_arr = split_val
    else
      temp_arr.clone.each do |letr|
        temp_arr.delete(letr) unless value.include?(letr)
      end
    end
  end
  counter += temp_arr.length
end
ap counter
