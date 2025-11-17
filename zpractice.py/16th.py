my_list = ["apple", "Banana", "orange", "GrApE"]
new_list = []

for item in my_list:
    word = ""
    for char in item:
        if 'a' <= char <= 'z':
            word += chr(ord(char) - 32)
        else:
            word += char
    new_list.append(word)

print(new_list)
