s = "aabbcde"

# Step 1: count frequency
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Step 2: find first non-repeating
for ch in s:
    if freq[ch] == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character")