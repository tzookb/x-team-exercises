def alternatingCharacters(s):
    s_chars = list(s)
    amount_chars = len(s_chars)
    if amount_chars <= 1:
        return 0
    
    changes = 0
    i = 1
    while i < amount_chars:
        prev = s_chars[i-1]
        current = s_chars[i]
        if prev == current:
            s_chars[i] = prev
            changes += 1

        i += 1
    return changes
    

res = alternatingCharacters('aaaa')

print(res)