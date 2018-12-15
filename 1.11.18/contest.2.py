def twoStrings(s1, s2):
    s1_list = list(set(s1))
    s2_list = list(set(s2))
    intersect = list(set(s1_list) & set(s2_list))
    if len(intersect):
        return True
    return False
    

res = twoStrings('aa', 'llo')

print(res)