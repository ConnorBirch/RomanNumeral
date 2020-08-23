import re
rNumb = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
rNume = {1000 : "M",100 : "C",500 : "D",10 : "X",50 : "L", 1 : "I",5 : "V"}
def getValue(numeral):
    value = rNumb.get(numeral)
    return value

def valueString(numerals):
    result = []
    for i in numerals:
        result.append(getValue(i))
    return result

def convertFromRoman(numerals):
    if ' ' in numerals:
        return "Error"
    elif re.match("(.)\1{4,}", numerals) is not None :
        return "Error"
    numbers = valueString(numerals)
    result = 0
    count = 0
    for i in numbers:
        if count == 0:
            result += i
        elif i > numbers[count-1]: 
            result += (i - 2* numbers[count-1])
        else:
            result += i
        count += 1
    return result
    
def convertToRoman(number):
    if number > 3999:
        return "Error - Too Large"
    result = ""
    count = 0
    values = list(rNume.values())
    for i in rNume.keys():
        p = number // i
        
        number = number % i
        
        if p == 9:
            if count > 1:
                result += values[count] + values[count-2]
            else:
                result += values[count] + values[count-1]
        elif p > 4:
            result += values[count+1] + values[count]*(p-5)
        elif p == 4:
            result += values[count] + values[count+1] 
        else:
            result += rNume[i]*p
        count += 1
    return result

print("812 = " + convertToRoman(812))
print("49 = " + convertToRoman(49))
print("5000 = " + convertToRoman(5000))
print("IV = " + str(convertFromRoman("IV"))) # 4
print("CCCXIV = " + str(convertFromRoman("CCCXIV"))) # 314
print("MCMXCIX = " + str(convertFromRoman("MCMXCIX"))) # 1999
print("MMMM = " + str(convertFromRoman("MMMM"))) # 4000