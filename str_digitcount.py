s=input("enter string:")
count=0
for char in s:
    if char.isdigit():
        count=count+1
print("digit:",count)
    