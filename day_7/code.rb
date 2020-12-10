require "awesome_print"


bag_hash = {}

File.open("input.txt", "r") do |f|
  f.each_line do |line|
    two_split = line.strip.delete(".").split(" contain ")
    right_half = two_split[1].split(", ")

    bag_hash[two_split[0]] ||= []

    right_half.each_with_index do |item, index|
      if index.zero?
        bag_hash[two_split[0]].push(item[2..-1])
      else
        bag_hash[right_half[index - 1][2..-1]] ||= []
        bag_hash[right_half[index - 1][2..-1]].push(item[2..-1])
      end
    end
  end
end

#ap bag_hash
#ap bag_arr.uniq.length
bag_finder("shiny golden bags")

def bag_finder(bag_hash, bag_name)
  bag_hash.each do |key, val|
    if bag.include?(bag_name)
      
    end
  end
end
