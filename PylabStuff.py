from datetime import datetime
 
age = int(input("How old are you in years? "))
year_birth = datetime.now().year - age
print("We think you were born in the year " + str(year_birth))
