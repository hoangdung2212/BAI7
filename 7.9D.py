print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
def copy_file(source_file, destination_file):
    with open(source_file, 'r', encoding='utf-8') as src, open(destination_file, 'w', encoding='utf-8') as dst:
        content = src.read()
        dst.write(content)
source_file = input("Nhập tên tệp nguồn: ")
destination_file = input("Nhập tên tệp đích: ")
copy_file(source_file, destination_file)
print(f"Nội dung từ tệp '{source_file}' đã được sao chép sang tệp '{destination_file}'.")

