text=input("enter a string")
reverse=""
for char in text:
    reverse=char+reverse
if text==reverse:
    print("palindrome")
else:
    print("not a palindrome")