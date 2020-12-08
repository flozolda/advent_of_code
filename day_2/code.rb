require "awesome_print"
require "csv"

pw_table = CSV.parse(File.read("input.csv"), headers: true)

counter = 0

# Part1
# pw_table.each do |item|
#    #ap(item)
#    rule = item["rule"].split("-")
#    min = rule[0].to_i
#    max = rule[1].to_i
#
#    letter = item["letter"][0..-2]
#    #ap(letter)
#
#    pw = item["password"]
#
#    countOccurence = pw.count(letter)
#
#    if(countOccurence >= min && countOccurence <= max)
#            counter += 1
#    end
# end

# ap counter

# Part 2

pw_table.each do |item|
  # ap(item)
  rule = item["rule"].split("-")
  pos1 = rule[0].to_i - 1
  pos2 = rule[1].to_i - 1

  letter = item["letter"][0..-2]
  # ap(letter)

  pw = item["password"]

  # countOccurence = pw.count(letter)

  if pw[pos1] == letter || pw[pos2] == letter
    counter += 1 unless pw[pos1] == letter && pw[pos2] == letter
  end
end

ap counter
