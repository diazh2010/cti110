user_text = input()
 
non_chars = ' .!,'
count = 0

for char in user_text:
    if char not in non_chars:
        count += 1
print(count)


