def validParentheses(s):
    stack = []
    mapping = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    print(f"Input is {s}")
    for char in s:
        if char in mapping:
            print(f"Char {char} is present in mapping")
            top_Element = stack.pop() if stack else '#'
            if mapping[char] != top_Element:
                return False
        else:
            stack.append(char)
            print(f"Building the stack, the symbol is {char}")
    return not stack






str = "(]"
print(validParentheses(str))

