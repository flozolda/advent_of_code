require "awesome_print"

adapter_arr = []

File.open("input.txt", "r") do |f|
  f.each_line do |line|
    adapter_arr << line.to_i
  end
end

adapter_arr.sort!

ap adapter_arr

last_adapter = 0

one_jolt = 0
three_jolt = 0

temp = 0

adapter_arr.each do |adapter|
  temp = adapter - last_adapter

  case temp
  when 1
    one_jolt += 1
  when 3
    three_jolt += 1
  else
    ap "Other Jolt"
  end

  last_adapter = adapter
end

# For the last jump to the device
three_jolt += 1

ap "One jolt: #{one_jolt}"
ap "Three jolt: #{three_jolt}"

ap one_jolt*three_jolt