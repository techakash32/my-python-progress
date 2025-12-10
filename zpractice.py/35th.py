text='a b c d e'
new_text=""
for i in text:
    if i==" ":
        new_text += "-"
    else:
        new_text+=i
print(new_text)