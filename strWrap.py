def wrap(string, max_width):
    splitString = []
    widthString = ''
    Splitstring = string.split()
    for x in range(0, max_width):
        x = 0
        widthString = ''
        if x % max_width == 0:
            print(widthString)
        else:
            widthString = widthString + ' ' +  string[x % max_width]
    return widthString
print(wrap('abcdefghijklmnopqrstuvwxyz', 4))
