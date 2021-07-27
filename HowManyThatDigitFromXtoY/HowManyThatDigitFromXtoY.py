print("©KOTIKOT, script by BarsTiger")
print()

typeFrom = int(input("All numbers from: "))
typeTo = int(input("All numbers to: "))
whichDigit = int(input("What should I find: "))

allNumbers = ""
digitCount = 0

for i in range(typeTo - typeFrom + 1):
    allNumbers = allNumbers + str(typeFrom + i)

allNumbersList = []

for i in range(len(allNumbers)):
    allNumbersList.append(int(allNumbers[i]))

for n in range(len(allNumbersList)):
    if allNumbersList[n] == whichDigit:
        digitCount += 1

print()
print("I found " + str(digitCount) + " " + str(whichDigit) + "'s")
input()
