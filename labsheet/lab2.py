#Q3 i & ii #
print ('Single Quotes')
print ("Double Quotes")

#Q4 i , ii & iii #
print ('Single' +' Quote')
print ("Single" + " Quote")
print ("Single" + ' Quote')

#Q5 i , ii , iii & iv #
b = 'Quote'
print ('Single %s' %b)
a = "Single"
print ('%a %a' %(a, b))

#Q6 i , ii , iii & iv #
c = 5
print(c)
print ('There are', c, 'apple in the fridge')
print ('There are %d' %c, 'apple in the fridge')

#Q7 i & ii #
name = input ("Please enter your name")
print(name) # you will see the name you type in the console

#Q8 i , ii , iii & iv #
a = 10
b=20
x = a + b
print (a+b) or print (x)

#Q9 i , ii & iii
a = [1,2,3]
b = [1,2,3]
print ('a is equal to b:', a == b)

#Q10 i & ii #
print(2 ** 4)
x = pow(4, 2)
print(x)

#Q11 i
print(19%5)

#Q12 i & ii
a = 10
b = 12
print(a>b)
print('a > b is' , a > b)

#Q13 i & ii
a = True
b = False
print(a and b)
print("Combine result of x and y is", a and b)

#Q14 i , ii & iii
a = [1,2,3]
b = [1,2,3]
c = b
print(a is b)
print(c is b)

print(id(a))
print(id(b))
print(id(c))