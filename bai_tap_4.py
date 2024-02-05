# Mô tả: cho một mảng số nguyên, tìm k phần tử xuất hiện nhiều lần nhất trong mảng và trả về chúng dưới dạng danh sách. Nếu có
# Ví dụ:
# Input: lst_number = [1,1,1,2,2,3,4,4,4,7,7,7,7,7], k=2
# Output: [7,1]
import bai_tap_3
def print_frequency_occurrence(lst, k):
    output = []
    lst_remove_dup = bai_tap_3.remove_duplicate_lst(lst)
    arr_temp = []
    for num in lst_remove_dup:
        frequency = 0
        for item in lst:
            if num == item:
                frequency += 1
        arr_num_frequency = [num, frequency]
        arr_temp.append(arr_num_frequency)
    # Tìm phần tử có số lần xuất hiện theo k
    for k_0 in  range(0, k):
        max_frequency_res = max_frequency(arr_temp)
        # remove ra khỏi list
        for item_list in arr_temp:
            if max_frequency_res == item_list[0]:
                arr_temp.remove(item_list)
        # Thêm vào output
        output.append(max_frequency_res)
    return output

def max_frequency(lst_num):
    output = lst_num[0][0]
    max_frequency = lst_num[0][1]
    for item_list in lst_num:
        if item_list[1] > max_frequency:
            max_frequency = item_list[1]
            output = item_list[0]
    return output

lst_number = [1,1,1,2,2,3,4,4,4,7,7,7,7,7]
print(print_frequency_occurrence(lst_number, 3))