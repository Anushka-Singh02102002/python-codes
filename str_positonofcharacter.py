s = input("enter string: ")
ch = input("enter character to find position: ")

for i in range(len(s)):
    if s[i] == ch:
        print("character found at:", i)