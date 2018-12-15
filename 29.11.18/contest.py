def makingAnagrams(s1, s2):
    total_diff = 0
    letters_counts = {}
    for char in s1:
        if char not in letters_counts:
            letters_counts[char] = 0
        letters_counts[char] += 1
    
    for char in s2:
        if char not in letters_counts:
            letters_counts[char] = 0
        letters_counts[char] -= 1
    
    for char_key in letters_counts:
        count = letters_counts[char_key]
        total_diff += abs(count)
    return total_diff

res = makingAnagrams('cde', 'abc')
print(res)