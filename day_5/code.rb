require "awesome_print"

rows = 128



highestSeatId = 0

File.open("input.txt", "r") do |f|
    min = 0
    max = rows
    f.each_line do |line|
        line[0..-4].split("").each do |fb|
            if(fb == "F")
                min = 
                max = max / 2
            elsif(fb == "B")
                min = max / 2
                max = 
            end
            ap "Min"
            ap min
            ap "Max"
            ap max
        end
        exit
        line[-3..-1].each do |lr|
            if(fb == "L")

            elsif(fb == "R")

            end
        end
    end
end