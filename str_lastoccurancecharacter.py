s= "banana"
ch= "a"
for i in range (len(s)-1,-1,-1):
    if s[i]==ch:
        print("last position:",i)
        break