#Learn Python - Full Course for Beginners [Tutorial] - freecodecamp.org

# stuff = ["Hello, World!", "Hi there, Everyone!", 6]
# for i in stuff:
#     print(i + " Foobar!")

#STRINGS
print("Giraffe\nAcademy")
print("Giraffe\"Academy")

phrase = "Giraffe Academy"
phrase.lower()
phrase.upper()

phrase.issupper()
phrase.islower()

len(phrase)

phrase[0]
phrase.index("G")
phrase.replace("Giraffe", "Sloth")

#NUMBERS
print(-2.0897)
print(3+4)
print(3 * 4 + 5)
print(3 * (4 + 5))
print(10 % 3) ##mod
my_number = 3
print(str(my_number)) ##converting to string
print(abs(-5)) ##absolute value. In this case, 5
print(pow(3, 2)) ##3 to the power of 2
print(pow(2**3)) ##2 to the power of 3
print(max(4, 6))
print(min(4, 6))
print(round(3.7))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))##raiz quadrada

from math import * ##import math class


#GETTING INPUT FROM USERS
name = input("Enter your name:")
age = input("Enter your age:")
print("Hello " + name + "!You are " + age)

result = int("3") + int("5")
result = float("3.3") + float("5.8")


#LISTS
friends = ["Noor", "Kelly", "Yvet"]
friends[3] = "Gui"
print(friends[-1])##print the last index of the array
print(friends[1:])##print everything after index 1
print(friends[1:3])##print everything between index 1 and 3


#LIST FUNCTIONS
friends = ["Noor", "Kelly", "Yvet"]
number = [4,5,6,7]

friends.extend(numbers)##join arrays
friends.append("Yaell")
friends.insert(1, "Lonneke")##add element to position and push off to the right all the others
friends.remove("Gui")
friends.clear()
friends.pop()##pops last element
friends.index("Gui")
friends.sort()
friends.reverse()
friends2 = friends.copy()##copy one array to another


#TUPLES
##tuples are like lists, but with a few differences
##they are immutable
##people use tuples for data that is never gonna change
coordinates = (4, 5)
coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates[0])


#FUNCTIONS
##function is a collection of code which performs a specific task
##instructions inside the function need to be indented
##use _ for functions with compound names
def say_hi():
    print("Hi")

say_hi()##calling the function

def cube(num):
    return num*num*num
print(cube(3))


#IF STATEMENTS
is_male = True
is_tall= True

if is_male:
    print("You are a male")
else:
    print("You are not a male")


if is_male or is_tall:
    print("You are a male")
else:
    print("You are not a male")

if is_male and is_tall:
    print("blabla")
else:
    print("blablabla")

if is_male and is_tall:
    print("blabla")
elif is_male and not(is_tall):
    print("blabla")
else:
    print("blablabla")


#DICTIONARIES
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
}

print(monthConversions["Jan"])
print(monthConversions.get("Jan"))
print(monthConversions.get("Test", "Not a valid key"))


#LOOPS
i = 1
while i <= 10:
    print(i)
    i += s1
    
secret_word = "giraffe"
gress = ""
while guess != secret_word:
    guess = input("Enter guess: ")

##for each
for letter in "Giraffe Academy":
    print(letter)

friends = ["Noor", "Kelly", "Yvet"]
for friend in friends:
    print(letter)


## RANGE from 0 to 10, not including 10
for index in range(10):
    print(letter)

## RANGE from 3 to 10, not including 10
for index in range(3, 10):
    print(letter)

## LOOP SIZE ARRAY
for index in range(len(friends)):
    print(friends[index])

##FOR LOOP 0 TO 10
for i in range(11):
    print(i)


#MATRIX
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for row in number_grid:
    for col in row:
        print(col)


#COMMENTS
#THIS IS A COMMENT
'''
THIS
IS
A
COMMENT
'''

#TRY CATCH
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")

##catch specific errors
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError as err:
    print(err)

#READING FILES
open("employees.txt", "r")##read
open("employees.txt", "w")##write
open("employees.txt", "a")##append
open("employees.txt", "r+")##read and write
employee_file = open("employees.txt", "r")
print(employee_file.readable())##check if it's readable
print(employee_file.read())
print(employee_file.readline())
print(employee_file.readlines()[1])
employee_file.close()##always close files that you open

for employee in employee_file.readlines():
    print(employee)


#WRITING FILES
employee_file = open("employees.txt", "a")
employee_file.write("Toby is a good boy")
employee_file.close()


#MODULES & PIP
#modules in python are the same as libraries in java
https://docs.python.org/3/py-modindex.html
#put the libraries in the 'lib' folder

#pip - dependency manager
pip install python-docx
pip uninstall python-docx


#CLASSES AND OBJECTS
class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
    if self.gpa >= 3.5:
        return True
    else
        return False

from Student import Student

student1 = Student("Gon", "Business", 3.1, False)

print(student1)
print(student1.name)


#INHERITANCE
from Chef import Chef

class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The chef makes fried rice")
    
    def make_special_dish(self):
        print("The chef makes noodles")


#INTERPRETER
#type 'python3' on the terminal
#to exit, type 'exit()'