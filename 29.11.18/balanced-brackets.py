def is_bracket_opener(c):
    return c in ["{", "[", "("]

def is_bracket_closer(c):
    return c in ["}", "]", ")"]

def are_brothers(a, b):
    if a=="{" and b=="}":
        return True
    if a=="[" and b=="]":
        return True
    if a=="(" and b==")":
        return True
    return False

def isBalanced(s):
    brackets_stack = []
    chars = list(s)
    for char in chars:
        if is_bracket_opener(char):
            brackets_stack.append(char)
        else:
            last_inserted_bracket = brackets_stack.pop()
            if not are_brothers(last_inserted_bracket, char):
                return "NO"
    
    if len(brackets_stack) > 0:
        return "NO"
    
    return "YES"