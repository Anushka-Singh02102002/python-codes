s=input("enter string:")
ch=input("enter chararcter to count:")
count=0
for char in s:
    if char==ch:
        count=count+1
print("occurance:",count)