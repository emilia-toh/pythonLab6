"""
a=10
b=12

print('a > b is', a>b)

a = True
b = False
print('Combine result of a and b is', a and b)

a = [1,2,3]
b = [1,2,3]
c = b
print(a is b)
print(c is b)

import math
print(math.pi)

x = "python" + " exercise"
str.title(x)
print(x)

mark1 = float(input("Please enter mark "))
mark2 = float(input("Please enter mark "))
mark3 = float(input("Please enter mark "))
mark4 = float(input("Please enter mark "))
mark5 = float(input("Please enter mark "))
markList = [mark1, mark2, mark3, mark4, mark5]
print('The mark list is %s' %(markList))
totalmark = sum(markList)
print('Total mark is %s' %(totalmark))
itemsInTheList = len(markList)
averagemark = round(totalmark / itemsInTheList,2)
print('The average mark is %s' %(averagemark))

n = int(input('enter n '))
counter=1
base=2
value=1
while counter <= n:
    value = base * value
    counter += 1
    print(value)


counter=1
n=10
n1=0
n2=1
while counter <= n:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    counter += 1

n = int(input('enter n '))
counter = 1
while counter <= n:
    print(counter)
    counter += 1
"""
failedStudents = []
passedStudents = []

readFile = open ("ExamResult.txt","r")

scoresCount = 0
names = []
scores = []

for split in readFile:
    name, score = split.split()
    names.append(name)
    scores.append(int(score))

    while scoresCount < len(scores):
        if scores[scoresCount] < 50:
            failedStudents.append(name)
            failedStudents.append(score)
        elif scores[scoresCount] > 51:
            passedStudents.append(name)
            passedStudents.append(score)
        scoresCount += 1
print(failedStudents, passedStudents)
