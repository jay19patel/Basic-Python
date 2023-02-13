
# variables

# a= 50 # variables
# print(type(a)) # data type
# print(id(a))# id  (every time id change) memory location

# do not use  keyword name as a Variable

# Data Types:
    # numeric : int,float,complex(8+8j)
    # sequence type : list,tuple ,range
    # text : str
    # mapping type  : dict
    # set type : set
    # boolean type : bool
    # binary type : byte,bytearray ,memoryview

# complex data type:
# num=5+9j #only J is use
# print(type(num))
# print(num.real) #first number
# print(num.imag)#last num who is join with J

# float to int
# num = 7.1
# n = int(num) #convert float into int 
# print(n)
# print(type(n))

# list  data type
# methods: 
# append
# insert
# extend
# index
# remove
# sort
# reverse
# del 
# pop
# clear
# count
    
# list contain multiple type values
# l1=["jay",1,"nj","nj"]
# l2=[77,"nj"]
# print(l1+l2)

# set data type
# set1 ={'a','b',1,2,3}
# set2 ={'x','y','x','y'}
# print(set2) #only print x and y cause set are not print duplicates values for multiple times
# print(set1) # set first print numbers and then alphabets
 
# a ="jay_patel"
# print(list(a))#convert string to list []
# print(set(a))#convert string to set so delete duplication {}


# slice
# a =" hi jay how are you "
# print(a[0:5]) #slice the string ,0,1,2,3,4 = 5 
# print(a[3:]) #print values where key is graterthan 3
# print(a[:5]) #print values where key is lessthan 5
# print(a[::-1]) # reverse string
# print(a.replace("jay","lalit")) #replace the obj.

# dictionary
# dic= {'name':"jay",'age':22,'mo':123456}
# print(dic.keys())# print all keys 
# print(dic.values())# print all values 
# print(dic["age"]) #access values using key


# strings
# a ="jay patel"
# r=a.capitalize()#first letter convert to a capital
# r=a.casefold()#to a small letter
# r=a.upper()#to all capital letter
# r=a.title() # first letter of word are capitalize
# r=a.count('a') #count the letter how time they rept
# r=a.replace("jay","lalit")
# r=a.split()# split each word  
# print(r)

# operator:

# x=5
# y=8
# if x==y:
# if x!=y:
# if x==5 and y ==8: #x and y both are true 
# if x==9 or y ==8: #x and y both one are true
# if x is not y:
#     print("yes")
# else:
#     print("no")

# x=["a","b","c"]
# if "a" in x:
#     print("yes")
# else:
#     print("no")



# looping technic

# a = [5,2,10,12,18,1]
# for i in sorted(a):#Print for loop as a sorted : incresed
# for i in sorted(a,reverse=True):#Print for loop as a sorted : dicrese
    # print(i)

# list1= {1:"jay",2:"ajay"}
# for i in sorted(list1.items()):
#     print(i)

# std = [{"name":"jay","age":22,"std":12},{"name":"lalit","age":33,"std":10}]
    
# for i in std:
#     print(i["age"] ,"and",i["name"] )#only print age and name
    
# for i in filter(lambda i : i["age"]%2==0,std ):
#     print(i["age"] ,"and",i["name"] )#only print age is divide by 2 using lambda function

# enumerate : (use for giving key automated)
# for i , values in enumerate(["jay","ajay","lalit"]):
#     print(i,values)
# only i is represent  data as a tuple 
# where i and values both are given data as a objcte
# lambda function 
# add = lambda a,b:a+b
# add(5,5)

# --------------------------imp------------------------------

# functions : 
    # builtin functions
    # user dEfined function

# def functionname(paramiters):
#     print("jay")
#     return data

#  class  

# class student:
#     def jay():
#         print("hiii")

# std= student # create object as instense 
# std.jay() # call function 


# init function 
# autometicly call when  call are activate

# class student:
#     # auto run\ call when  object are created
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# s1=student("jay",22) #creaet Objcet
# print(s1.age)#call and print using object


# ----------------oops-------------------

# class
# objcet (class in andar variables rey te)
# method (class ni andar function rey te)
# inheritance 
# polymorphism
# encapsulation
# abstraction

# Inharitance :
# class Std:
#     def students(name):
#         print(f"im name is {name} a student of xyz school")
#     def hostel(no):
#         print(f"im in hostel no : {no}")

#single level
# class clg(Std): #clg inherit all data of std 
#     def clg(clg):
#         print(f"im in clg {clg}")

# # multi level
# class job(clg): #job accesing all method and object  of clg and std.
#     def myjob(job):
#         print(f"i work as a role of {job} office") 

# mutliple
# a and b claass are inheritne in c 
# a and b not a multilevel 
        

# s = job
# s.hostel(50) #call function of student using clg objcet
# s.clg("gecr") #call function of clg using clg objcet
# s.myjob("it") 


# map
# map  the data with functuon and return
# # map the function and list object
# def sum(a):#function
#     print(a+a)

# data=(1,2,3,4,5) # input data set 
# obj = map(sum,data) #maping the function and data set
# print(list(obj)) # print and call function 



# # filter
# filtter data using condition
# def sum(a): #conditional function
#     if a==5:
#         print("done ")
#     else:
#         print(a)

# out = filter(sum,(1,2,3,4,5)) # take conditiond and filtter
# print(list(out)) #print and call
    


# ----------------exception handling-------------------

# run time error 
# genrate a message withoyt giveing error message

# compile time erre --      Logical error  ---runtime errors

# synetx :

# try: code
# except: message
# else: no exception when run
# finally: allways code run 

# exmle

# a=10
# b="jya"
# try:
#     #add functions here 
#     # call  here
#     # if have some error -> except()
#     print(a+b)
# except:
#     # Exception
#     #nameError

#     print("this was error")
# else:
#     print("i try other way")
# finally:
#     print("soryy not working")
