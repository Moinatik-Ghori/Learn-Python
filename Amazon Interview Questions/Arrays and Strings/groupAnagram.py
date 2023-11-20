'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
def groupAnagrams(strs):
    resultDict = {}
    for word in strs:
        sortedWord = "".join(sorted(word))
        if sortedWord not in resultDict:
            resultDict[sortedWord] = [word]
        else:
            resultDict[sortedWord].append(word)
    result = list(resultDict.values())
    return result

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = groupAnagrams(strs)
print(output)
