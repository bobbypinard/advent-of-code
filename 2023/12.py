def count(springs, nums):
    if springs == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in springs else 1

    result = 0
    
    if springs[0] in ".?":
        result += count(springs[1:], nums)
        
    if springs[0] in "#?":
        if nums[0] <= len(springs) and "." not in springs[:nums[0]] and (nums[0] == len(springs) or springs[nums[0]] != "#"):
            result += count(springs[nums[0] + 1:], nums[1:])

    return result

total = 0

for line in open('12_input.txt'):
    springs, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    total += count(springs, nums)
    print(nums)

print(total)
