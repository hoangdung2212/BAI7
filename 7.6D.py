print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
def read_last_n_lines(filename, n):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        last_n_lines = lines[-n:]
    return last_n_lines
filename = input("Nhập tên tệp: ")
n = int(input("Nhập số dòng cuối cần đọc: "))
last_n_lines = read_last_n_lines(filename, n)
print(f"{n} dòng cuối cùng của tệp {filename}:")
for line in last_n_lines:
    print(line, end='')
