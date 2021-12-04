import sys

def most_common_digit(nums, position):
    count0 = 0
    for num in nums:
        count0 += 1 if num[position] == '0' else 0
    if count0 > (len(nums) - count0):
        result = '0'
    elif count0 < (len(nums) - count0):
        result = '1'
    else:
        result = 'x'
    return result

def find_digits(nums):
    num_digits = len(nums[0])
    digits = ''
    for d in range(num_digits):
        digit = most_common_digit(nums, d)
        digits += digit
    gamma = int(digits, 2)
    reverse = ''.join('1' if x == '0' else '0' for x in digits)
    epsilon = int(reverse, 2)
    return gamma * epsilon

def findnums2(nums):
    num_digits = len(nums[0])
    digits = ''
    oxygen = nums
    co2 = nums
    for d in range(num_digits):
        digit = most_common_digit(oxygen, d)
        if digit == 'x':
            digit = '1'
        oxygen = [num for num in oxygen if num[d] == digit]
        if len(oxygen) == 1:
            break
    for d in range(num_digits):
        digit = most_common_digit(co2, d)
        if digit == 'x':
            digit = '0'
        else:
            digit = '1' if digit == '0' else '0'
        co2 = [num for num in co2 if num[d] == digit]
        if len(co2) == 1:
            break

    onum = int(oxygen[0], 2)
    cnum = int(co2[0], 2)
    return onum * cnum

if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        values = [row.strip() for row in f.readlines()]

    result1 = find_digits(values)
    print(result1)

    result1 = findnums2(values)
    print(result1)