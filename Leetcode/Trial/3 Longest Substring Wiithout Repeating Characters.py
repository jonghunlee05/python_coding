s = "pwwkew"

longest = ""
current = ""




for i in range(len(s)):
    current += s[i]
    if current in longest: 
        print("duplicate " + "longest: " + longest + " current: " + current) 
        current = ""
        
    if current not in longest:
        if len(current) > len(longest):
            print("longest: " + longest + " current: " + current)
            longest = current
            current = ""
        else:
            longest += current
            current = ""

    
        

print(longest)
