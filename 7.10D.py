print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
def find_longest_words(text):
    words = text.split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words
text = input("Nhập văn bản: ")
longest_words = find_longest_words(text)
print("Những từ dài nhất trong văn bản là:")
for word in longest_words:
    print(word)
