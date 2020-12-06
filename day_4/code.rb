require "awesome_print"

pwHash = {}
index = 0
File.open("input.txt", "r") do |f|
    f.each_line do |line|
        if(line.strip.length == 0)
            index += 1
            next
        end
        pwHash[index] ||= {}
        line.split("\n").each do |v|
            v.split(" ").each do |v1|
                next if v1.strip.length == 0
                keyVal = v1.split(":")
                pwHash[index][keyVal[0]] = keyVal[1]
            end
        end
    end
end

=begin
valid = 0
#Part1
pwHash.each do |key_,val|
    if(val.length == 8 || (val.length == 7 && val["cid"].nil?))
        valid += 1
    end
end

ap valid
=end

valid = 0
#Part 2
pwHash.each do |key_,val|
    if(val.length == 8 || (val.length == 7 && val["cid"].nil?))
        next unless(val["byr"].length == 4 && val["byr"].to_i >= 1920 && val["byr"].to_i <= 2002)

        next unless(val["iyr"].length == 4 && val["iyr"].to_i >= 2010 && val["iyr"].to_i <= 2020)

        next unless(val["eyr"].length == 4 && val["eyr"].to_i >= 2020 && val["eyr"].to_i <= 2030)

        if(val["hgt"][0..-3].match(/\A[-+]?[0-9]*\.?[0-9]+\Z/))
            if(val["hgt"][-2..-1] == "cm")
                unless(val["hgt"][0..-3].to_i >= 150 && val["hgt"][0..-3].to_i <= 193)
                    next
                end
            elsif(val["hgt"][-2..-1] == "in")
                unless(val["hgt"][0..-3].to_i >= 59 && val["hgt"][0..-3].to_i <= 76)
                    next
                end
            else
                next
            end
        end

        next unless(val["hcl"].length == 7 && val["hcl"][0] == "#" && val["hcl"][1..-1].length == 6 && val["hcl"][1..-1].match(/[0-9a-f]{6}/))

        eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        next unless(eyeColors.include?(val["ecl"]))


        next unless(val["pid"].length == 9 && val["pid"].match(/\A[-+]?[0-9]*\.?[0-9]+\Z/))
        valid += 1
    end
end

ap valid