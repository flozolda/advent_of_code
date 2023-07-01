require "awesome_print"

counter = 0
num_hash = {}

File.open("input.txt", "r") do |f|
  f.each_line do |line|
    # puts line
    # feedHash
    num_hash[counter] = line.to_i
    counter += 1
  end
end

# ap(num_hash)

num_hash.each do |_key, value|
  num_hash.each do |_key1, value1|
  # Part1
  # if(value + value1 == 2020)
  #     ap(value*value1*value2);
  #     exit;
  # end
    num_hash.each do |_key2, value2|
      if value + value1 + value2 == 2020
        ap(value * value1 * value2)
        exit
      end
    end
  end
end
