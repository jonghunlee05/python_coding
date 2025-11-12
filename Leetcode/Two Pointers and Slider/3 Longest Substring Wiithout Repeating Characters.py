s = "pwwkew"

longest = ""

l = 0


for r in range(len(s)):
    if s[r] not in longest:
        longest += s[r]
    else:
        l += 1

print(longest)


