s = input("Enter string: ")
count = 0

for char in s:
    if not char.isalnum() and not char.isspace():
        count += 1

print("Special characters:", count)