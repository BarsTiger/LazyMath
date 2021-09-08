print("©KOTIKOT, script by BarsTiger")
print()
print("Please, type only int numbers, str is allowed only in hex")

hextonum = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}



systypefrom = int(input("Type base number of system convert FROM: "))
systypeto = int(input("Type base number of system convert TO: "))
convertfrom = input("Type number, that you want to convert: ")
if systypefrom > 16 or systypeto > 16:
    print("Sorry, more than hexal systems aren't supported RIGHT NOW. Come back in several centuries")
    input()
    exit()

convertfrom = convertfrom.upper()

def todecimal(number, base):
    n = len(str(number))
    i = 0
    res = 0
    while n - i != 0:
        i += 1
        res += int(int(hextonum[str(number)[i - 1]]) * (base ** (n - i)))

    return res

print(todecimal(convertfrom, systypefrom))

input()
