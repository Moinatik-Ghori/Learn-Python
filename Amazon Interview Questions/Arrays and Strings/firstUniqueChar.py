'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
'''
def firstUniqueChar(s):
    l = len(s)
    ind = 0
    exist = ""
    while ind < l:
        for i in range(ind+1,l+1):
            print(f"Index={ind}, i={i}, Char={s[ind]} ")
            if s[ind] in s[i:l]:
                exist = exist + s[ind]
                print("Index {} and Length {} and existing characters {}".format(ind,l,exist))
                break
            else:
                if s[ind] not in exist:
                    return ind
                else:
                    print(f" Char {s[ind]} is already existing in {exist}")
                    break
        ind += 1
    return -1


def solution2(s):
    occurance ={}
    for char in s:
        if char in occurance:
            occurance[char] += 1
        else:
            occurance[char] = 1

    for ind, char in enumerate(s):
        if occurance[char] == 1:
            return ind
    return -1


s="aabb"
print(firstUniqueChar(s))

print(solution2(s))
