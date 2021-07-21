#Q2
class SquareInfo:
    def calAvgArea(totalArea,totalCount):
        averageArea = totalArea / totalCount
        print("Square average area is", round(averageArea, 2), "square meters for", totalCount, "squares.")
#Q3
f = open("listOfSquareArea.txt", "r")
#Q4
names = []
areas = []

#Q6
for line in f:
    name, area = line.split()
    names.append(name)
    areas.append(float(area))
f.close()
print(names, areas)
#Q7
totalArea = 0
totalCount = 0

for i in areas:
    totalArea += i
    totalCount += 1

#Q8
SquareInfo.calAvgArea(totalArea,totalCount)
#Q9 & 10
newSquareName = input("Enter new square name: ")
names.append(newSquareName)
print(names)
while True:
    try:
        newArea = float(input("Enter square area: "))
        break
    except ValueError:
        print("You have entered the area wrongly! Please enter the area in number!")
        continue

areas.append(newArea)
print(areas)
#Q11
newTotalArea = 0
newTotalCount = 0
for i in areas:
    newTotalArea += i
    newTotalCount += 1
#Q12
SquareInfo.calAvgArea(newTotalArea,newTotalCount)