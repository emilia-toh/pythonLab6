#Q3
a = 10
print(a)
print(type(a))

#Q4
b = 5 + 6j
print(b)
print(type(b))

#Q5
c = True
print(c)
print(type(c))

#Q6
d = 10.5
print(d)
print(type(d))

#Q7
e = 'Testing String'
print(e)
print(type(e))

#Q9
f = [1,2,3]
print(f)
print(type(f))

#Q10
g = (4,5,6)
print(g)
print(type(g))

#Q11
h = {'Student' : 'Aaron'}
print(h)
print(type(h))

#Q12
i = {7,8,9}
print(i)
print(type(i))

#Q13
j = [1,2,3]
k = f+j
print(k)
print(type(k))
print(1 in k)

#Q14
l = (10,11,12)
m = l + g
print(m)
print(type(m))

#Q15
k[0] = 11
print(k)

# m[0] = 11
# print(m)

#Q16
n = {'Lectuer' : 'Judy'}
h.update(n)
print(h)
print(type(h))

#Q17
o = {9, 10 ,11}
# Union
print(o.union(i))
print(type(o))
# Intersect
print(o.intersection(i))
print(type(o))

#Q19
country = {'Australia': 'AU', 'Belgium': 'BE', 'China': 'CN', 'Denmark': 'DK'}
for k, v in country.items():
    print(k + 'country code is ' + str(v))

#Q20
names = ['Thomas', 'Linda', 'Cath', 'Benny']
names.sort()
print(names)
print(names.pop(0))
print(names.pop(0))
print(names.pop(0))
print(names.pop(0))
print(names)
print(names.pop(0))