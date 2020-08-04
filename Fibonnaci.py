
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
