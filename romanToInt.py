def from_roman(roman_num):
    dict = {
        "M" : 1000, "CM" : 900, "D" : 500, "CD" : 400, "C" : 100, "XC" : 90, "L" : 50, "XL" : 40, "X" : 10, "IX" : 9, "V" : 5, "IV" : 4, "I" : 1
    }
    number = 0
    while len(roman_num) > 0:
        for key in sorted(dict.keys(), reverse = True):
            if len(roman_num) < 1: break
            if key == roman_num[0] or key == roman_num or key == roman_num[0:2]:
                number += dict.get(key)
                if key == roman_num[0:2]: # to optimize the program when "key" is a composite. ex "IX"
                    roman_num = roman_num.removeprefix(roman_num[0:2])
                    break
                roman_num = roman_num.removeprefix(roman_num[0])
            
    return number


print(from_roman("MXIX"))



