
## what is python ?

- Python is a popular programming language.
- Python can be used on a server to create web applications.
- Python can be used for a wide range of applications, including web development, scientific computing, data analysis, artificial intelligence, and machine learning.

# Variables:

```python
Name = "JAY PATEL "
```
Here,
Name is Variable 
"JAY PATEL" id data

Name Variable store tha data in memory location
- Variable e Data ne Meromri ma store kare so apde ene game tyae use kari sakiye jyare jarur Hoy Tyare 

varibale ne Game e name api saky  Jemk ke 
- NAME = "JAY"
- name = "JAY"
- _name = "JAY"
- name1 = "jay"
pan  AA Use na kari sakiye 
- 1name = "JAY" NOT VALID 
- @name = "jay" NOT VALID 
- -name = "JAy" NOT VALID 
- etc 
Use only readable varibales 
 Alwasy try simple name for storing datas like
```python
Name_1 = "JAY PATEL "
roll_n_1 = 20
Mobile_num_1 = 123456

Name_2 = "SALMAN KHAN "
roll_n_1 = 21
Mobile_num_1 = 654321

```

# Data Type :

1. List:
- A list is a collection of items in a specific order, and it can contain duplicate items. Lists are mutable, which means their elements can be modified after they are created.

```python
fruits = ["apple", "banana", "cherry"]
```
2. Set:
- A set is a collection of unique items, and it doesn't have a specific order. Sets are useful for removing duplicates from a collection, and for performing mathematical operations like union, intersection, and difference.

- intersection " banne ma je same hase te leva mate 
- difference " banne ma je alag hase te "
- union "banne ne sathe kari dey and dublicate ni thay koy values "

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 
z = x.difference(y) 
z = x.union(y) 

print(z)

```
3. Tuple:
- A tuple is similar to a list, but it's immutable, which means its elements cannot be modified once it's created. Tuples are useful for situations where you want to store a collection of values that should not be changed.

```python
coordinates = (10, 20)
```
4. Dictionary:
- A dictionary is a collection of key-value pairs, where each key is associated with a value. Dictionaries are useful for storing data in a way that allows you to quickly look up values based on their keys.

```python
person = {"name": "John", "age": 30, "city": "New York"}
```
Here,
person is variable 
{"name": "Jay", "age": 30, "city": "Valsad "} is Data
"name" is Key
"jay" is value



## IF AND ELSE:

- if and else conditions are used in programming to make decisions based on certain conditions. 
- The if statement allows the program to test a condition and perform an action if the condition is true. If the condition is false, the program can either move on to the next statement or execute an alternative action using the else statement.

```python

x = 10
if x > 0:
    print("x is positive")
else:
    print("x is zero or negative")

# ----------------------------------------

x = "My name is jay patel
if "jay" in x:
    print("yes ")
else:
    print("no ")
# ----------------------------------------
x = ["jay","ajay","salman"]
if "jay" in x:
    print(" jay yes ")

elif "ajay" in x:
    print("ajay yes ")

elif "salman" in x:
    print("ajay yes ")
else:
    print("list ma nathi")
```
- here, only first condition check and stop 
- khali paheli j condition chek kari ne exit they geyu kem ke e khotu pade to j next stage ma jase 

- darek vastu check karvi Hoy to ena mate  loop use karva padse next video 


# for Loop and While Loop
- In Python, for and while loops are used for iterating over a sequence of elements or repeating a block of code until a certain condition is met.

1. For loop
- Khabar Hase ke ketli var loop farse 

``` python

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

```

 - In this example, the for loop iterates over each element in the list numbers. The loop variable num takes on each value in the list, and the code inside the loop body is executed for each value.

2. For loop
- Khabar Na  Hoy ke  loop farse 
- Jya sudhi sachu nay pade tya sudhi farse 

``` python

while True:
    num = input("Enter a number: ")
    if num ==  5 ():
        print(" numer 5 malse tya sudhi faryu ")
        break
    else:
        print(" sacho number nathi try again ")

```
- break use to stop when condition are satisfy
- In this example, the for loop iterates over each element in the list numbers. The loop variable num takes on each value in the list, and the code inside the loop body is executed for each value.




# Function

- je rite varible ma data save kari ne jya jarur hoy tya use kari sakiye te rite  koy block of program ne vara farti ghani var use karvu hoy to funtion no upyo thay 

- A function in Python is a reusable block of code that performs a specific task. It can take inputs, perform operations on them, and return outputs. Functions help to organize code, make it more modular and easier to read, and avoid code repetition.

- In Python, functions are defined using the def keyword, 

- function  ne run karva mate ene call karva pade je rite variable ne call karva mate variable use kariye  te rite function ne call karava funcion karva pade

```python
name = "jay"

print(name)


def my_function():
    print("jay patel is my name ")

my_function()
```

- function ni andar peramiter pan pass kari sakay (varables pass kari sakaya)

```python



def my_function(name):
    print(f"{name} patel is my name ")
my_function("jay")
```
- jo tamare kayk print na karvu hoy and simple kay answr joyto hoy to tame return function no use kari sako

- Jo kayk return kareli vastu ne print karvu hoy to te ne koy varable ma store kari sakay ane pasi print kari sakay

```python

def my_function():
    return "my name is jay"

my_data = my_function()
print = my_data
```

- simple ke function a ek variable na jem kam karse jyare te return value karavse 
- function pote return karel value bani jase and apde teno use kari sakiye
- ena vadhare example project ma joysu 



# Class
- class is group of method or Functions 

- dhoran 10 no ek class chhe (class)
- class ni andar students chhe (functions)
- name ,rollnumber (attributes)

```python

class STD:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def Students_boy(self):
        n = f"student name {self.name} and  Roll no is {self.roll}"
        return n


# obj = STD("jay patel",25)
obj = STD("salman khan",25)
print(obj.Students_boy())

```

- __init__ is by defaultb run when object arw Created ,It is also known as the constructor method
- self is a self refers to the current instance of a class, which allows you to access the attributes and methods of that instance. self is a convention in Python and is not a keyword.

# MODULS 

- In Python, a module is a file containing Python definitions and statements. A module can define functions, classes, and variables, and can also include runnable code. Modules are used to organize Python code into reusable and maintainable units, and can be imported into other Python scripts or modules.

- jyare code bo ghnao they jay to tyare tene alag alag file ma bhag padi devana and jayre je nu ka  hoy tyare tene class na use kari ne call kari ne upyog kari levano 

- In Python, there are two types of modules: built-in modules and third-party modules.
- Build in modul atle ke tene import karva ni jarur nay hoy
-  Third Party Moduls ne create ke install kari ne import kari ne Use kari sakay 

- buidl exmple 


# TRY and EXCEPT

- In Python, try and except are used for exception handling, which allows you to handle errors or exceptions that may occur during program execution.
- Koy prakar ni error ave to te ne run karvanu ban kari ne Exept manu print ke run karavi dese 

- The try block contains the code that you want to execute, and the except block contains the code that is executed if an error occurs. Here's an example:

```python

try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result:", y)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")

else :
    print("else Part ")
# ------------------------------------------

try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result:", y)
except:
    print(" Some error Found")
```


- main upyog to e ke error ave te chata apde error ni jovi hoy to apde  eno upyog kari sakiye 




# Python with MONGODB


 storing data :

 {  "name":"jay",
    "roll No : 20,
    "city ": "valdas"
    }
1. What is MONGODB ?
=> MongoDB is a popular open-source, document-oriented NoSQL database that uses a JSON-like format for storing and retrieving data. It was developed by MongoDB Inc. and is designed to be scalable, flexible, and efficient in managing large volumes of data.
=>  It is widely used in web applications, big data processing, and other data-intensive applications.

- We Need Some type of data base then we take a MONGODB as well as MYSQL whatever 
- but we chose MONGODB 


2. HOW to Conect with Python ?

install MONGODB using pip 
pip in a installer to install any libraries in pythons(pakege manager)

```python


import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
foldername = client["mydatabase"]
filename = foldername["mycollection"]

```

- only few line of code to connect with data base 
- Here, 
we First Connect oure File with Mongodb using MongoClient 
create a FOlder where our all file are store 
create oure file where our data are stores 

3. How to CRUD in MONGODB ?
- insert: insert new data in data
    filename.insert(query, values)

- find : for find data in data base 
    filename.find(query, values)

- update : Update data
    filename.update(query, values)
    
- delete : delete item(document)
    filename.delete(query, values)














