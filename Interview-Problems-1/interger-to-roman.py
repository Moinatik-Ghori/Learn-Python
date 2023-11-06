def intTOroman(romanNum):
    val = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I' : 1
    }

    l = len(romanNum)
    i = 0
    num = 0
    char = ''
    while i < l:

        char = romanNum[i]
        if romanNum[i] == 'C':
            if (i+1) < l and romanNum[i+1] in ('M','D'):
                char = char + romanNum[i+1]
                print("Double Char",char)
                i+=1
        if romanNum[i] == 'X':
            if (i+1) < l and romanNum[i+1] in ('C','L'):
                char = char + romanNum[i+1]
                print("Double Char",char)
                i+=1
        if romanNum[i] == 'I':
            if (i+1) < l and romanNum[i+1] in ('X','V'):
                char = char + romanNum[i+1]
                print("Double Char",char)
                i+=1
        num = num + val[char]
        i+=1
        print("{} Char {} , Number {}".format(i,char,num))

    return num

romanNum = "MCMLXXXVII"
print(intTOroman(romanNum))
