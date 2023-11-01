import time
def stringtoint(s):
    s = s.lstrip()
    result = ""
    maxInt = 2**31 - 1
    minINt = -2**31
    print(s)
    for c in s:
        if c == "-" or c == "+" or c.isdigit():
            if c == "+":
                continue
            else:
                result = result + c
        else:
            break
    if result == "" or result == "-":
        return 0
    if int(result) < minINt:
        return minINt
    elif int(result) > maxInt:
        return maxInt
    else:
        return int(result)

start = time.time()
str = "    -42"
str = "4193 with words"
str = "words and 987"
str= "-91283472332"
str = "     -42"
str = "+1"
print(stringtoint(str))
end = time.time()
print(f"Total Execution time: {(end-start) * 1000:.2f} miliseconds")


