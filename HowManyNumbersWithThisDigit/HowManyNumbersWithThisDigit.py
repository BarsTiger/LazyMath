print("©KOTIKOT, script by BarsTiger")
print()

typeFrom = int(input("All numbers from: "))
typeTo = int(input("All numbers to: "))
whichDigit = int(input("What should I find: "))

allNumbers = []
digitCount = 0

for i in range(typeTo - typeFrom + 1):
    allNumbers.append(typeFrom + i)

for n in allNumbers:
    if str(whichDigit) in str(n):
        digitCount += 1

print()
print("I found " + str(digitCount) + " " + str(whichDigit) + "'s")
input()
