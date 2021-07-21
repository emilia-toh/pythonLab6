#Q3 Example 1
a = True
if a == True:
    print('a result is true')

#Q3 Example 2
b = 5
if b <= 5:
    print('b is less or equal to 5')

#Q4
a,b = 5,6
if a is not b:
    print('a is not b is true')

#Q5
a,b = 5,10
if a > 5 and b > 5 :
    print('a and b is greater than 5')
elif a > 5 or b > 5 :
    print('a or b is greater that 5')
else:
    print('a and b is lesser or equal to 5) # try to change b to value less or equal to 5')

#Q6
n = 6
current_sum = 0
i = 0
while i <= n:
    current_sum += i
    i += 1
    print(current_sum)

#Q7
myFriends = ['Joe', 'Zoe', 'Alvin', 'Paris']
for friend in myFriends:
    invite = 'Hi ' + friend + '. Please come to my party!'
    print(invite)

#Q8
dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'
tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

dictionary_tk = {"name": "Leandro", "nickname": "Tk", "nationality" : "Brazilian", "age": 24}
for attribute, value in dictionary_tk.items():
    print("My %s is %s" %(attribute, value))

#Q9
numbers = [10,5,24,8,6]
for number in numbers:
    if number % 2 == 1:
        print(True)
        break
    else:
        print(False)

#Q10
n = 6
current_sum = 0
i = 0
while i <= n:
    current_sum += i
    i += 1
print('The sum is %s' %(current_sum))

#Q1 Challenge
num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))
Sum = num1 + num2
print('The sum of the 2 numbers, %s and %s is %s' %(num1, num2, Sum))

#Q2 Challenge
a = int(1)
while a<=10:
    print( "%s. Hello World" %(a))
    a=a+1

#Q3 Challenge
numList = [10, 20, 30, 40, 50]
totalsum = 0
for num in numList:
    totalsum += num
print('The total of the 5 numbers is %a' %(totalsum))

#Q4 Challenge
Number = int(input("Enter a number "))
if Number >= 1 and Number <= 100:
    if (Number % 2) == 0:
        print('Number entered, %s is even' %(Number))

#Q5 Challenge
mark =int(input("Enter your mark "))
if(mark >=50):
    print("You have passed M2 PA1")
else:
    print("You have failed M2 PA1")

#Q6 Challenge
Mark = int(input("Enter your mark "))
if(Mark==30):
    print("Your grade is F")
elif(Mark==80):
    print("Your grade is A")
elif(Mark==60):
    print("Your grade is C")
else:
    print("End Program")

#Q7 Challenge
Num = 0
for i in range(5, 101, 5):
    print(i)
    Num += i
print('The sum of multiples of 5 is %s' %(Num))

#Q8 Challenge
mark1 = float(input("Please enter mark "))
mark2 = float(input("Please enter mark "))
mark3 = float(input("Please enter mark "))
mark4 = float(input("Please enter mark "))
mark5 = float(input("Please enter mark "))
markList = [float(mark1), float(mark2), float(mark3), float(mark4), float(mark5)]
print('The mark list is %s' %(markList))
totalmark = sum(markList)
print('Total mark is %s' %(totalmark))
itemsInTheList = len(markList)
averagemark = round(totalmark / itemsInTheList,2)
print('The average mark is %s' %(averagemark))

#Q9 Challenge
numbers = ["1 is 55", "2 is 155", "3 is 255", "4 is 355", "5 is 455", "6 is 555", "7 is 655", "8 is 755", "9 is 855", "10 is 955"]
set = ['Sum for set']
for a in set:
    for x in numbers:
        print(a, x)

#Q10 Challenge
n=10
while n > 1:
    print(int(n))
    if (n % 2) == 0:
        n=n/2
    else:
        n=3*n+1
