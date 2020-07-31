def caesarShift(shiftThis, shiftChars):
  allChars = "abcdefghijklmonpqrstuvwxyz"
  shiftedString = ''
  shiftChars = int(shiftChars)
  for x in shiftThis:
      xIndex = allChars.index(x)
      if x in allChars:
        if xIndex >= 25:
            xIndex -= 26
        x = allChars[xIndex + shiftChars]
        shiftedString += x
  return shiftedString



print(caesarShift('xyz', 1))
