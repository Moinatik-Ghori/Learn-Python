import time
def longestSubstring(str):
    result = ""
    for char in str:
        if char not in result:
            result = result + char
    return len(result)


str = "pwwkew"
start = time.time()
print(longestSubstring(str))
end = time.time()
print(f"Total Execution time: {(end-start) * 1000:.2f} miliseconds")
