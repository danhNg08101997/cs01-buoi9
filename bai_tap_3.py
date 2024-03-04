# lst_number = [1,1,1,2,2,3,4,4,5]
# Remove duplicate from sorted array(easy)
# Ví dụ:
# input: nums = [1,1,1,2,2,3,4,4,5]
# output: 5 (mảng mói là [1,2,3,4,5])

# Input:
# lst_number = [1,1,1,2,2,3,4,4,5]
# Process
def remove_duplicate_lst(nums):
    # Cách 1:
    # output = []
    # for num in nums:
    #     if num not in output:
    #         output.append(num)
    # return len(output)
    # Cách 2:
    output = []
    for value in nums:
        flag = False
        for num in output:
            if value == num:
                flag = True
                break
        if not flag:
            output.append(value)
    return output
# Output:
# print('Output: ', remove_duplicate_lst(lst_number))