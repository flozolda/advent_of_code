require "awesome_print"

def seat_finder(min_num, max_num, input, min_id, max_id)
  min = min_num
  max = max_num
  res = 0

  # ap input

  input.split("").each do |l|
    if l == min_id
      max = ((max + min).to_f / 2.0).floor
    elsif l == max_id
      min = ((max + min).to_f / 2.0).ceil
    end

    # ap "Min"
    # ap min
    # ap "Max"
    # ap max
    # ap l

    if max - min <= 1
      if l == min_id
        # ap "The row is " + min.to_s
        res = min
      else
        # ap "The row is " + max.to_s
        res = max
      end
    end
    # ap "Res"
    # ap res
  end
  res
end

rows = 127
highest_seat_id = 0

seat_arr = []

File.open("input.txt", "r") do |f|
  f.each_line do |line|
    min = 0
    max = rows
    left_most = 0
    right_most = 7

    line = line.strip
    row = seat_finder(min, max, line[0..-4], "F", "B")
    col = seat_finder(left_most, right_most, line[-3..-1],"L", "R")
    seat_arr[row] ||= []
    seat_arr[row][col] = true
    # ap row
    # ap col

    # ap line
    # This is for part 1
    # highest_seat_id = row * 8 + col if(row * 8 + col > highest_seat_id)
  end
end

ap highest_seat_id

seat_arr.each_with_index do |val, i|
  next if val.nil?

  val.each_with_index do |seats, j|
    if seats.nil?
      ap "Row"
      ap i
      ap "Column"
      ap j
      ap "id"
      ap i * 8 + j
    end
  end
end
