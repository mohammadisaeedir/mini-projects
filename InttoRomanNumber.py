import Separator
sym = ["I", "IV", "V", "IX", "X", "XL",
       "L", "XC", "C", "CD", "D", "CM",
       "M", "iv", "v", "vi", "ix", "x", "xl",
       "l", "xc", "c", "cd", "d", "cm",
       "m"]
numbers = [1, 4, 5, 9, 10, 40,
           50, 90, 100, 400, 500, 900,
           1000, 4000, 5000, 6000, 9000, 10000, 40000,
           50000, 90000, 100000, 500000, 900000,
           100000]
symr = ['cm', 'cd', 'xc', 'xl', 'ix', 'vi',
        'iv', 'CM', 'CD', 'XC', 'XL', 'IX',
        'IV', 'm', 'd', 'c', 'l', 'x', 'v',
        'M', 'D', 'C', 'L', 'X', 'V', 'I']

myDigitR = [900000, 400000, 90000, 40000, 9000, 6000,
            4000, 900, 400, 90, 40, 9,
            4, 1000000, 500000, 100000, 50000, 10000,
            5000, 1000, 500, 100, 50, 10, 5, 1]


def roman_to_int(num):
    print(num)
    result = ''
    if num > 999999 or num < 0:
        raise ValueError('this in not a roman number')
    while num:
        for i in range(len(numbers)):  # (0,12)
            if numbers[i] <= num < numbers[i + 1]:
                for j in range(num // numbers[i]):
                    result += sym[i]
                num %= numbers[i]
    return result


def int_to_roman(roman):
    print(roman)
    result = 0
    while roman:
        for i in range(len(symr)):
            if symr[i] in roman:
                result += myDigitR[i]
                roman = roman.replace(symr[i], '', 1)

    return Separator.separator(result)


print(int_to_roman('MMMCC'))  # 248 -> 2 CC, 4 XL, 8 VII

print(roman_to_int(600))
