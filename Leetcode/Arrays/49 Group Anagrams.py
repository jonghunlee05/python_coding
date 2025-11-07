from collections import defaultdict


anagrams = defaultdict(list)
strs = ["eat","tea","tan","ate","nat","bat"]



for s in strs:
    key = ''.join(sorted(s))
    anagrams[key].append(s)

sorted_anagrams = sorted(anagrams.values())


print(sorted_anagrams)
