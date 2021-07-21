#Q1
class CalUtils:
    def calAvgHeight(totalstudentheight, totalstudentcount):
        average = totalstudentheight / totalstudentcount
        print("Student average height is", str(round(average, 2)), "m for", str(totalstudentcount), "students.")

#Q2i
names = []
heights =[]

#Q2ii
totalStudentHeight = 0
totalStudentCount = 0

#Q3 & 4
file = open("listOfStudentHeight.txt", "r")

#Q5
for line in file:
    name, height = line.split()
    names.append(name)
    heights.append(float(height))
print(names,heights)

#Q6
for i in heights:
    totalStudentHeight += i
    totalStudentCount += 1

CalUtils.calAvgHeight(totalStudentHeight,totalStudentCount)

#Q7
newStudentName = input("Enter new student name: ")
names.append(newStudentName)
print(names)

#Q8
while True:
    try:
        newStudentHeight = float(input("Enter student height (in meters): "))
        break
    except ValueError:
        print("You have entered the height incorrectly! Please enter the height in number!")
        continue

heights.append(newStudentHeight)
print(heights)

#Q9
newTotalStudentHeight = 0
newTotalStudentCount = 0

for i in heights:
    newTotalStudentHeight += i
    newTotalStudentCount += 1

CalUtils.calAvgHeight(newTotalStudentHeight, newTotalStudentCount)