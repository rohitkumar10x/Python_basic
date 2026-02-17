print("Hello World")

===========================
name = input('Enter the your Name :')
print(name)

==========================
num_1  = int(input("Enter the First Number :"))
num_2  = int(input('Enter the Seconf Num :'))
print(num_1+num_2)

=========================
num  = int(input("Enter the num :"))
num1  = num**2
print(num1)

=============================
celcius = int(input('Enter the celcius :'))
fahrenheit = (celcius * 1.8) + 32
print(fahrenheit)

================================
num = int(input('Enter the a number'))
if num%2==0:
    print(f'{num} is a Even Number')
else:
    print(f'{num} is the Odd Number')

==================================
age = int(input('Enter the Your age :'))
if age>=18:
    print('You are Eligible to vote')
else:
    print('You are not Eligible to vote')

===================================
a =  int(input('Enter the first number :'))
b =  int(input('Enter the Secound Number :'))
c =  int(input('Enter the third Number :'))
if a>b and a>c:
    print(f'{a} is greater then {b} and {c}')
elif b>a and b>c:
    print(f'{b} is greater then {a} and {c}')
else:
    print(f'{c} is greater then {a} and {b}')

====================================
year  = int(input('Enetr the year :'))
if year%4 ==0:
    print(f'{year} is the leap year')
else:
    print(f'{year} not leap yaer')

====================================
marks  = int(input('Enter the marks :'))
if marks>=90:
    print('Grade A')
elif marks>=75:
    print('Grade B')
elif marks>=50:
    print('Grade C')
else:
    print('fail')

for i in range(1,51):
    print(i)

=====================================
num = 7
rg =1
while rg<=10:
    print(f'{num} X {rg}= {num*rg}')
    rg = rg+1

====================================
n = 9
total = 0
i = 1
while i <= n:
    total += i  # total = total + i
    i += 1      # i = i + 1
print(total)

=======================================
fac = 1
num = 5
rg  = 1
while rg<=num:
    fac = fac*rg
    rg =rg + 1
print(fac)

====================================
num  = 123
print(int(str(num)[::-1]))

=======================================
name   = 'Rohit Singh'
reverse  = name[::-1]
print(reverse)

==================================
vowel  = 'aeiouAEIOU'
name =  'Rohit Singh'
count = 0
for char in name:
    if char in vowel:
        count +=1
print(count)

==============================
num = 'radar'
if num == num[::-1]:
    print('Yes')
else:
    print('No')

==============================
name  = 'ROHTI SIGNH'
print(name.lower())

=================================
course = 'Python'
count=0
for chr in course:
    count+=1
print(count)

================================
name  = 'Rohit Singh'
print(name.replace(' ',''))

==============================
list = [54,9,8,4,55,4,5]
print(max(list))
print(min(list))
list.remove(54)
print(list)
list.pop(1)
print(list)
reverse =  list[::-1]
print(reverse)

=============================
count = 0
while count<=len(list):
    if list[0] in list:
        count += 1
        list[0] += 1
    print(count)

===============================
num = int(input("Number daalo: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime Number")
else:
    print("Not Prime")

=========================== 
# Scound highest no.
a = 188
b = 2
c = 3
list  = [a,b,c]
list.sort()
print(list[-2])

==============================
list = [5,45,46,45,44,5,4,5454,45,44]
count = 0
for i in list:
    count += 1
print(count)

==================================
def word_co(data):
    count = 0
    for i in data:
        count += 1
    print(count)
list = [5,45,46,45,44,5,4,5454,45,44]
word_co(list)



