def intTOroman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        i =0
        romanNum = ""
        while num > 0:
            div, num  = divmod(num, val[i])
            romanNum += symbols[i] * div
            i += 1
        return romanNum

num = 1994
print(intTOroman(num))
