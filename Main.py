#introduction to python

First_Name = "Asis"
Last_Name = "Kaur"
Full_Name = First_Name + " " + Last_Name
print("hello " + Full_Name)

first_name = "asis"
last_name = "kaur"
full_name = first_name + " " + last_name
print("Hello " + full_name)

age = 17
age +=1
print("your age is : " +str(age))

height = 20.5
print("your height is : " + str(height) + "cm")
print(type(height))

human = True
print("are you a human? " +str(human))
print(type(human))

name = ("asis")
age = 17
hot = True

print(name)
print(age)
print(hot)

name, age, hot = "asis", 17, True
print(name, age, hot)

asis = gunnu = gaggu = dhillon = 17
print(asis, gunnu, gaggu, dhillon)

name= "asis kaur"
print(len(name))
print(name.find("k"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("s"))
print(name.replace("s", "z"))
print(name*100)

#Convert the data type of one value to another data type

x = 1     #int
y = 2.0   #float
z = "3"   #string

x = float(x)
y = int(y)
z = float(z)

print("X is " + str(x))
print("Y is " + str(y))
print("Z is " + str(z*4))

#how to accept input

name = input("what is your name?: ")
age = int(input("what is your age?: "))
height = float(input("what is your height?: "))

age = age + 1
print("hello " +name)
print("you are " +str(age)+ " years old")
print("your height is " +str(height)+ "fts")

import math

pi = 3.14
x = 1
y = 2
z = 3
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(420))
print(max(x,y,z))
print(min(x,y,z))

#Slicing is equal to create a substring by extracting elements from another string

name = "asis kaur"
first_name = name[0:4]
last_name = name[5:9]
funky_name = name[0:9:2]
print(first_name)
print(last_name)
print(funky_name)


# List

vegetables = ['onion','tomato','capsicum','cucumber']
print(vegetables)

# Indexing of the list

print(vegetables[2])

print()

for i in vegetables:
    print(i)

print(vegetables[::2])               # Slicing in Lists

vegetables.append('carrot')         # Adding new element
print(vegetables)
print()

vegetables.insert(5,'raddish')        # Using insert element
print(vegetables)
print()

stationary = ['Pencil','eraser','scissors','tape']

Grocery = vegetables + stationary
print(Grocery)
print()

# Tuples

t1 = ('almirah','cupboard','curtains','bed')
print(type(t1))
print()

# Sets

A = {'chaap','momos','noodles','burger','pasta'}

print(A)
print(type(A))

# If statements

Age = eval(input('Enter the Age: '))
if Age>18 :
    print("You are eligible  to vote")

else :
    print("You are not eligible to vote")
print()

 # Use of if elif and else conditions and logical operators

Age = eval(input("Enter your age: "))
if Age<=13:
    print("You are a child")

elif (Age>13 and Age<18):
    print("You are a teenager")

elif (Age>=18 and Age<60):
    print("You are an adult")

else :
    print("You are a senior citizen")

# Loops

x = 1
while x < 11:                            # It displays numbers from 1 to 10
    print(x)
    x+=1
print()

list = ['Apple','Banana','Mango','Cherry']
for x in list:
    print(x)
print()

# Conditional statements

x = 0
while x < 10:
    print(x)                               # break is used to terminate the execution
    x+=1
    if x == 5:
        break
print()

i = 0
while i < 10:
    print(i)                               #it continues the execution
    i+=1
    if i == 5:
        continue
print()

# Dictionary

dict = {'soap':'toothpaste','cleanser':'shampoo','conditioner':'shaving cream'}
print(dict)
print()
print(type(dict))
print()

print(dict.keys())
print(dict.items())

print(dict['soap'])


# functions

def multiply(num1,num2):
    result = num1*num2
    return result

print(multiply(2,3))

def simple_interest(P,R,T):
    result = (P*R*T)/100
    return result

P = eval(input("Enter the Principal: "))
R = eval(input("Enter the Rate: "))
T = eval(input("Enter the Time:  "))

SI = simple_interest(P,R,T)
print('Simple Interest is ',SI)

# random module

import random
a = random.randint(1,11)
print(a)
print()

Choice = ['Head','Tail']
Toss = random.choice(Choice)
print(Toss)

#module

import random

colors = ["red","blue","white","Black","Pink"]
print("the list of colors is:",colors)

color = random.choice(colors)
print("The randomly selecteed value from the list is:",color)