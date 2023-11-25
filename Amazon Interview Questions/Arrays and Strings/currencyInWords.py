'''
Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Constraints:
0 <= num <= 231 - 1
'''

def number_to_words(num):
    if num == 0:
        return "Zero"

    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def helper(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + helper(n % 10)
        else:
            return ones[n // 100] + " Hundred " + helper(n % 100)

    def to_words(num):
        if num == 0:
            return "Zero"
        result = ""
        billion = num // 1000000000
        million = (num % 1000000000) // 1000000
        thousand = (num % 1000000) // 1000
        remainder = num % 1000

        if billion != 0:
            result += helper(billion) + " Billion "
        if million != 0:
            result += helper(million) + " Million "
        if thousand != 0:
            result += helper(thousand) + " Thousand "
        if remainder != 0:
            if remainder >= 10 and remainder <= 19:
                result += teens[remainder-10]
            else:
                result += helper(remainder)

        print("The number is {}\n"
              "Billions: {}\n"
              "Millions: {}\n"
              "Thousands: {}\n"
              "Reminders: {}\n"
              "-----------------\n"
              "Final Result: {}\n"
              "".format(num,billion,million,thousand,remainder,result))

        return result.strip()

    return to_words(num)

# Example usage:
number = 23
result = number_to_words(number)
print(result)
