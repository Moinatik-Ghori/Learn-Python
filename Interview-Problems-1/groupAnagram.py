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
