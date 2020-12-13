require "awesome_print"

instr_hash = {} 
current_index = 0

File.open("input.txt", "r") do |f|
  f.each_line do |line|
    instr_hash[current_index] = {}
    instructions = line.split(" ")
    instr_hash[current_index]["instr"] = instructions[0]
    instr_hash[current_index]["jumps"] = instructions[1].to_i
    instr_hash[current_index]["visited"] = false
    current_index += 1
  end
end

# ap instr_hash

# Part1
def find_loop(instr_hash)
    current_index = 0
    accumulator = 0

    until instr_hash[current_index]["visited"] == true
        instr_hash[current_index]["visited"] = true
        case instr_hash[current_index]["instr"]
        when "acc"
            accumulator += instr_hash[current_index]["jumps"]
            current_index += 1
        when "jmp"
          current_index += instr_hash[current_index]["jumps"]
        when "nop"
            current_index += 1
        else
          "Error: Invalid Instruction (#{instr_hash[current_index]["instr"]})"
        end
    end
    accumulator
end

# ap "Part 1"
# ap find_loop(instr_hash)

def find_error(instr_hash, changed_indexes)
    ap "New Run"
    current_index = 0
    changed_index = nil
    accumulator = 0
    res_hash= {}
    instr_hash_copy = Marshal.load(Marshal.dump(instr_hash))

    until current_index > instr_hash_copy.length - 1 || instr_hash_copy[current_index]["visited"] == true
        instr_hash_copy[current_index]["visited"] = true

        if changed_index.nil? && !changed_indexes.include?(current_index) && (instr_hash_copy[current_index]["instr"] == "jmp" || instr_hash_copy[current_index]["instr"]=="nop")
            ap "changing #{instr_hash_copy[current_index]["instr"]}"
            case instr_hash_copy[current_index]["instr"]
            when "jmp"
                instr_hash_copy[current_index]["instr"] = "nop"
                changed_index = current_index
                changed_indexes.push(current_index)
            when "nop"
                instr_hash_copy[current_index]["instr"] = "jmp"
                changed_index = current_index
                changed_indexes.push(current_index)
            end
        end

        case instr_hash_copy[current_index]["instr"]
        when "acc"
            accumulator += instr_hash_copy[current_index]["jumps"]
            current_index += 1
        when "jmp"
          current_index += instr_hash_copy[current_index]["jumps"]
        when "nop"
            current_index += 1
        else
          "Error: Invalid Instruction (#{instr_hash_copy[current_index]["instr"]})"
        end
    end

    res_hash["changed_indexes"] = changed_indexes
    res_hash["accumulator"] = accumulator
    res_hash["last_index"] = current_index

    res_hash
end

changed_indexes = []

last_index = 0

until last_index == instr_hash.length
    initial = find_error(instr_hash,changed_indexes)
    last_index = initial["last_index"]
    changed_indexes = initial["changed_indexes"]
end

ap initial["accumulator"]