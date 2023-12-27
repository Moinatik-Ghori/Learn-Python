'''
def letter_combinations_Method_1(digits):
    if not digits:
        return []
    mapping = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }
    print(f"Digits:{digits} Mapping:{mapping}")

    def recursion1(index, path):
        print(f"Index:{index} Path:{path}")
        if index == len(digits):
            result.append(''.join(path))
            return

        currnt_digit = digits[index]
        print(f"Current Digit : {currnt_digit}")
        for digit in mapping[currnt_digit]:
            path.append(digit)
            print(f"Digit in Mapping :{digit}, Path:{path}")
            recursion1(index + 1 , path)
            path.pop()


    result = []
    recursion1(0,[])
    return  result

# Example usage:
digits = "234"
result = letter_combinations_Method_1(digits)
print(result)
'''


class Solution(object):
    def letterCombinations(self, digits):
        if digits == "": return []
        res = []

        map = {'2': "abc",
               '3': "def",
               '4': "ghi",
               '5': "jkl",
               '6': "mno",
               '7': "pqrs",
               '8': "tuv",
               '9': "wxyz"}

        def backTracking(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                print(f"Res:{res}")
                return

            for char in map[digits[i]]:
                print(f"Char:{char} , CurrStr:{curStr}")
                backTracking(i + 1, curStr + char)

        backTracking(0, "")
        return res

b1 = Solution()
print(b1.letterCombinations("23"))