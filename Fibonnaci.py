'''
def fibbonaciSequence(n):
    prevNumber = 1
    currentNumber = 1
    swapper = 0
    for x in range(n - 1):
        swapper = currentNumber + prevNumber
        prevNumber = currentNumber
        if x != n - 2:
            currentNumber = swapper

        
        
    return currentNumber
print(fibbonaciSequence(4))
'''
'''
prevNumber = 1
currentNumber = 1
swapper = 0
def fibbonaciRecursive(n):
    if n <= 1:
        return "1. Why did you need to ask for this one?"
    else:
        return fibbonaciRecursive(n-1) + fibbonaciRecursive(n-2)
    swapper = currentNumber + prevNumber
    prevNumber = currentNumber
    if x != n - 2:
        currentNumber = swapper
    fibbonaciRecursive(n)
    
'''
def fibbonaciRecursive(n):
    if n <= 2:
        return 1
    else:
        return fibbonaciRecursive(n-1) + fibbonaciRecursive(n-2)

termNumber = int(input("Find term number: "))
if termNumber <= 0:
    print("Positive numbers only please... ")

else:
    print(fibbonaciRecursive(termNumber))