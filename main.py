# primitive type (Kiểu dữ liệu cơ sở): int, string, float, boolean, None giá trí máy tính có thể phân biệt và xử lý được
# collection type (Kiểu dữ liệu tập hợp): dữ liệu tập hợp quản lý nhiều giá trị thường để xây dựng lưu trữ liệu theo cấu trúc ta quy định
# List: khởi tạo, quản lý(CRUD)

lst_name: list[str] = ["Nam", "Minh", "Hằng"]

# Create: thêm dữ liệu lst.append(gia_tri)
lst_name.append("Danh")
print(lst_name)

# Read: đọc dữ liệu hoặc tìm kiếm dữ liệu...
print(lst_name[2])
    # Lấy phần tử cuối cùng
length = len(lst_name)
print(lst_name[length - 1])
print(lst_name[-1])
    # Lấy phần tử từ vị trí start đến vị trí end -1
print(lst_name[1:3])
    # Lấy từ phần tử đầu đến vị trí cuối -1 thì không cần ghi 0
print(lst_name[:3])
    # Lấy từ phần tử bắt đầu đến hết list
print(lst_name[1:])
    # Duyệt list
        # for index
for index in range (0, length):
    print (lst_name[index])
        # for value
for name in lst_name:
    print(name)
        # for index, value
for index,value in enumerate(lst_name):
    print(index, value)

if 'Danh' in lst_name:
    print("Yes")
else:
    print("No")

    # Thuật toán search trên list
index = -1
for i, value in enumerate(lst_name):
    if value == 'Hằng':
        index = i
        break
if index != -1:
    print(lst_name[index])

# Update: cập nhật giá trị trên list
lst_phone = ['0123', '0222', '0333', '0444']
for index, value in enumerate(lst_phone):
    if value == '0444':
        lst_phone[index] = '0555'
print(lst_phone)

# Delete: xóa 1 phần tử khỏi list
lst_phone.remove('0123')
print(lst_phone)
del lst_phone[1]
print(lst_phone)
    # xóa toàn bộ giá trị
lst_phone.clear()
print(lst_phone)
    # xóa list khỏi bộ nhớ
del lst_phone
print(lst_phone)