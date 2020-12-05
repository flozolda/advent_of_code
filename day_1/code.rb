require "awesome_print"

counter = 0;
numHash = {};

File.open("input.txt", "r") do |f|
    f.each_line do |line|
      #puts line
      numHash[counter] = line.to_i;
      counter += 1;
      #feedHash
    end
  end

#ap(numHash);

#Added the found to stop after the first match
#TODO: Use recursion to solve this
numHash.each do |key,value|
    currVal = value;
    numHash.each do |key1,value1|
        numHash.each do |key2,value2|
            if(value + value1 + value2== 2020)
                ap(value*value1*value2);
                exit;
            end
        end
    end
end