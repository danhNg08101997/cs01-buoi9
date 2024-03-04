# Input
lst_number = [2,7,11,15]
# process
def two_sum (lst, target):
    output = []
    for index, value in enumerate(lst):
        result = target - value
        for i in range(index + 1, len(lst)):
            if lst[i] == result:
                output = [index, i]
    if output == []:
        output = f'không có giá trị phù hợp'
    return output
# Output: [0,1] vì num[0] + num[1] = 2+7 = 9 ngược lại nếu không có
print(two_sum(lst_number, 14))
