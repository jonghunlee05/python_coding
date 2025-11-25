s = "pwwkew"

seen = set()
l = 0
max_len = 0

for r in range(len(s)):
    
    # if it is repeated, start moving the left window and drop that letter on the set. 
    while s[r] in seen:
        seen.removes(s[l])
        l += 1
    
    seen.add(s[r])
    max_len = max(max_len, r - l + 1)


print(max_len)