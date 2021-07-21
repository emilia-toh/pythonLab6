#Q2
# f = open("demofile.txt", "r")
# print(f.read())
# f.close()

#Q3
# print(f.read(5))
# f.close()

#Q4
# print(f.readline())

#Q5
# print(f.readline())
# print(f.readline())

#Q6
# for x in f:
#     print(x)

#Q7
# f = open("demofile.txt", "a")
# f.write("Now the file has more content!")
# f.close()
#
# f = open("demofile.txt", "r")
# print(f.read())
# f.close()

#Q8
# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
# f = open("demofile3.txt", "r")
# print(f.read())

#Q9
# f = open("myfile.txt", "x")
# f = open("myfile1.txt", "w")

#Q10
# import os
# os.remove("demofile.txt")
#
# import os
# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
# else:
#     print("The file does not exist")

#Q11
# f = open("test.txt", "r")
# print(f.read())

#Q12
# readFile = open("test.txt", "r")

#Q13
names = []
marks = []
readFile = open("test.txt", "r")
for line in readFile:
    name,mark = line.split()
    names.append(name)
    marks.append(float(mark))
readFile.close()
print(names, marks)

#Q14
totalMark = 0
studentCount = 0
for i in marks:
    totalMark += i
    studentCount += 1
print(totalMark)

#Q15
# newName = input("Please enter new student name: ")
# while True:
#     try:
#         newMark = float(input("Please enter his mark in number: "))
#         break
#     except ValueError:
#         print("Oh, you have entered the mark wrongly! Please enter the mark in number!")
#         continue

#Q16
class MarkStudent:
    def calAverage(totalMark, count):
        average = totalMark / count
        print(average)
MarkStudent.calAverage(totalMark,studentCount)
