require "awesome_print"

counter = 0;
numHash = {};

File.open("input.txt", "r") do |f|
    f.each_line do |line|
      #puts line
      #feedHash
      numHash[counter] = line.to_i;
      counter += 1;
    end
  end

#ap(numHash);

numHash.each do |key,value|
    currVal = value;
    numHash.each do |key1,value1|
# Part1
#        if(value + value1 == 2020)
#            ap(value*value1*value2);
#            exit;
#        end
        numHash.each do |key2,value2|
            if(value + value1 + value2 == 2020)
                ap(value*value1*value2);
                exit;
            end
        end
    end
end