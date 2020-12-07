require "awesome_print"

def seatFinder(min_num,max_num,input,min_id,max_id)

    min = min_num
    max = max_num
    res = 0

    #ap input

    input.split("").each do |l|
        if(l == min_id)
            max = ((max + min ).to_f/2.0).floor
        elsif(l == max_id)
            min = ((max + min).to_f/ 2.0).ceil
        end


        #ap "Min"
        #ap min
        #ap "Max"
        #ap max
        #ap l


        if(max-min <= 1)
            if(l == min_id)
                #ap "The row is " + min.to_s
                res = min
            else
                #ap "The row is " + max.to_s
                res = max
            end
        end
        #ap "Res"
        #ap res
    end
    return res
end

rows = 127
highestSeatId = 0

seatArr = []

File.open("input.txt", "r") do |f|
    f.each_line do |line|
        min = 0
        max = rows
        leftMost = 0
        rightMost= 7

        line = line.strip
        row = seatFinder(min,max,line[0..-4],"F","B")
        col = seatFinder(leftMost,rightMost,line[-3..-1],"L","R")
        seatArr[row] ||= []
        seatArr[row][col] = true
        #ap row
        #ap col

        #ap line
        # This is for part 1
        #highestSeatId = row * 8 + col if(row * 8 + col > highestSeatId)
    end
end

#ap highestSeatId

seatArr.each_with_index do |val,i|
    next if val.nil?
    val.each_with_index do |seats,j|
        if(seats.nil?)
            ap "Row"
            ap i
            ap "Column"
            ap j 
            ap "id"
            ap i*8+j
        end
    end
end