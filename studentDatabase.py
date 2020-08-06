
with open("studentScores.txt", "r") as f:
    content = f.readlines()
    gradesDict = {}
    gradeList = []
    for line in content:
        name, score = line.split(' ')
        score = int(score)
        gradeList.append(score)
        if name not in gradesDict:
            gradesDict[name] = [score]
            
        else:
            gradesDict[name].append(score)


while True:
    studentQuery = input("Which student would you like to check? ")
    if studentQuery in gradesDict:
        print(sum(list(gradesDict[studentQuery]))/len(gradesDict[studentQuery]))
    else:
        print("You did not enter a existing student's name, or you may have spelled it wrong. Goodbye!")
    



