# from secondcase import add,mul
from tkinter import *
# window = Tk()
# photo = PhotoImage(file='/Users/littleprince/Desktop/截屏2022-10-01 19.22.12.png')
# label = Label(window,
#             text="hello world",
#             font=('Arial',40,'bold'),
#             fg='green',
#             bg='black',
#             # relief=RAISED,
#             padx=20,pady=20,
#             image=photo,
#             compound='top'
#             )
# label.pack()
# # label.place(x=0,y=0)
# window.mainloop()

#widgets = GUI elements: buttons, testboxes, labels, images
#windows = serves as a container to hold or contain these widgets
# window = Tk()#instantiate an instance of a window
# window.geometry("420x420")
# window.title("Bro Code first")
# icon = PhotoImage(file='/Users/littleprince/Desktop/截屏2022-09-26 23.48.03.png')
# window.iconphoto(True,icon)
# window.config(background='#5cfcff')
# window.mainloop()#place window on computer screen, listen for events

#Python multiprocessing
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                  multiprocessing = better for cpu bound tasks (heavy cpu usage) I
#                   multithreading = better for io bound tasks (waiting around)
# from multiprocessing import Process,cpu_count
# import time
# def counter(num):
#     count = 0
#     while count<num:
#         count += 1
# def main():
#     start = time.perf_counter()
#     a = Process(target=counter,args=(250000000,))
#     b = Process(target=counter,args=(250000000,))
#     c = Process(target=counter,args=(250000000,))
#     d = Process(target=counter,args=(250000000,))
#     a.start()
#     b.start()
#     c.start()
#     d.start()
#     a.join()
#     b.join()
#     c.join()
#     d.join()
#     end = time.perf_counter()
#     print("finished in:",end-start,"s")
#     print(cpu_count)
# if __name__ == '__main__':
#     main()

#daenon thread = a thread that runs in the background, not important for program to run
#              your program will not wait for daemon thread to complete before exiting
#              non-daemon threads cannot normally be killed, stay alive until task is complete
#              ex.background tasks, garbage collection, waiting for input,long running process
# import threading
# import time
# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count+=1
#         print("logged in for ",count,"seconds")
# x = threading.Thread(target = timer,daemon=True)
# x.start()
# # x.setDaemon(True)
# # print(x.isDaemon())
# answer = input("Do you wish to exit?\n")
#thread = a flow of execution. Like a seoarate order of instructons.
#         However each thread takes a  turn running to achieve concurrency
#         GIL = (golbal interpreter lock),
#         allows only one thread to hold the control of the Python interpreter at any one time
#cup bound = program/task spends most of it's time waiting for internal events(CPU interpreter)
#            use multiprocessing
#io bound = program/task spends most of it's time waiting for ecternal events(user interpreter)
#           use multithreading
# import threading
# import time
# def eat_breakfast():
#     time.sleep(3)
#     print("You eat breakfast")
# def drink_coffee():
#     time.sleep(4)
#     print("You drink coffee")
# def study():
#     time.sleep(5)
#     print("You finish studying")
# start = time.perf_counter()
# x = threading.Thread(target=eat_breakfast,args=())
# x.start()
# y = threading.Thread(target=drink_coffee,args=())
# y.start()
# z = threading.Thread(target=study,args=())
# z.start()
# x.join()
# y.join()
# z.join()
# end = time.perf_counter()
# # eat_breakfast()
# # drink_coffee()
# # study()
# print(threading.active_count())
# print(threading.enumerate())
# print(end-start)

#yield用法
# def Fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a+b
#         n += 1
# for n in Fab(5):
#     print(n)

#-----------------------------Object Oriented Programming-------------------------------------
#iter
# class A:
#     def __init__(self):
#         self.a = [1,2,3,4,5]
#     def __iter__(self):
#         for i in range(len(self.a)):
#             yield self.a[i]
# a = A()
# a = iter(a)
# for i in range(5):
#     print(next(a))
#duck typing = concept where the class of an object is less important than methods attributes
#              class type is not checked if minimum methods/attribute are present
#              "if it makes like a duck, and it quacks like a duck, then it must a duck"
# class Duck:
#     def walk(self):
#         print("The duck is walking")
#     def talk(self):
#         print("The duck is qwuacking")
# class Chicken:
#     def walk(self):
#         print("The chilken is walking")
#     def talk(self):
#         print("The chilken is clucking")
#     def fly(self):
#         print("The chilken is flying")
# class Person():
#     def catch(self,duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter!")
# duck = Duck()
# chilken = Chicken()
# person = Person()
# person.catch(chilken)

#objects as arguments
# class Car:
#     color = None
# def change_color(vehicle,color):
#     vehicle.color = color
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
# change_color(car_1,"blue")
# change_color(car_2,"yellow")
# change_color(car_3,"red")
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)

#abstract class = a class which contains one or more abstract methods
#abstract method = a method that has a declaration but does not have an implementation
#Prevents a user from creating an object of class
#+compels a user to override abstract methods in a child class
# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
# class Car(Vehicle):#correct
#     def go(self):
#         print("The car is going")
#     def stop(self):
#         print("The car is stopped")
# class Motocycle(Vehicle):#false because of the lack of definition
#     def go(self):
#         print("The motocycle is going")
# vehicle = Vehicle()#correct
# vehicle.go()#false because you cannot use the inner funct in abstract

#super() = function used to give access to the methods of a parent class
#          returns a temporary object of a parent class when used
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def fun(self,*stuff):
#         sum = 1
#         for i in stuff:
#             sum *= i
#         return sum
# class Square(Rectangle):
#     def __init__(self,length,width):
#         super().__init__(length,width)
#         self.area = super().fun(self.length,self.width)
# class Cube(Rectangle):
#     def __init__(self,length,width,height):
#         super().__init__(length,width)
#         self.height = height
#         self.volume =  super().fun(self.length,self.width,self.height)
# area = Square(3,3)
# cube = Cube(3,3,3)
# print(area.area)
# print(cube.volume)

#method chainning = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self
# class Car:
#     def drive(self):
#         print("U drive the car")
#         return self
#     def turn_on(self):
#         print("U start the engine")
#         return self
#     def brake(self):
#         print("U step on the brakes")
#         return self
# car = Car()
# car.turn_on()\
#     .drive()\
#      .brake()

#method overriding
# class Animal:
#     def eat(self):
#         print("This animal is eating")
# class Rabbit:
#     def eat(self):
#         print("This rabbit is eating")
# rabbit = Rabbit()
# rabbit.eat()
# # stdout:This rabbit is eating

#multiple inheritance = whea child class is derived from
#                       more than one parent class
# class Prey:
#     def flee(self):
#         print("This animal flees")
# class Predator:
#     def hunt(self):
#         print("This animal hunts")
# class Fish(Prey,Predator):
#     pass

#multi-level inheritance
# class Orgnism:
#     alive = True
# class Animal(Orgnism):
#     def eat(self):
#         print("This animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("This dog is barking")

#inheritance
# class Animal:#parent
#     alive = True
#     def eat(self):
#         print("This animal is eating")
#     def sleep(self):
#         print("This animal is sleeping")
# class Rabbit(Animal):#child
#     def run(self):
#         print("This rabbit is running")
# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming")
# class Hawk(Animal):
#     def fly(self):
#         print("This hawk is flying")
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
# print(rabbit.alive)
# fish.eat()

# class Car:
#     wheels = 4#all have
#     def __init__(self,make,model,year,color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#     def drive(self):
#         print("This "+self.model+" is driving!")
#     def stop(self):
#         print("The car is stopping!")
# car_1 = Car("Chevy","Corovette",2021,"blue")
# print(car_1.color)
# print(car_1.model)
# print(car_1.year)
# print(car_1.make)
# car_1.drive()
# car_1.stop()
# Car.wheels = 2#change all
# car_1.wheels = 2#only change car_1
# print(Car.wheels)
# --------------------------------------------------------------------------------------------

# from messages import hello,bye# from messages import *
# hello()
# bye()
# import messages as msg
# msg.hello()
# msg.bye()

#if __name__ == '__main__'
# 1.Module can be run as a standalone Program
#   or
# 2.Module can be imported and used by other Modules
# python interpreter sets "special variables",one of which is __name__
# python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

#time function
# time_object = time. localtime() # local time
# time_object = time. gmtime()# UTC time
# local_time = time. strftime ("9B 9d %Y %H:9M:9S"', time_object)
# print (local_time)
# time_string = "20 April, 2020"
# time_object = time. strptime (time_ string, "%d %B, %Y")
# print (time_ object)
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime (time_tuple)
# time string = time.mktime (time_tuple)
# print (time_string)
# print(time_string)

#zip(*iterables) = aggregate elsments from two or more iterables(list,tuples,sets,etc.)
#                  creates a zip object with paired elements stored in tuples for each elements
#1
# usernames = ["Dude","Bro","Mister"]
# passwords =("password","abc123","guest")
# users = dict(zip(usernames,passwords))
# print(type(users))
# for key,value in users.items():
#     print(key +":"+ value)
#2
# usernames = ["Dude","Bro","Mister"]
# passwords = ("password","abc123","guest")
# login_date = ["1/1/2021","1/2/2021","1/3/2021"]
# users = zip(usernames,passwords,login_date)
# print(type(users))
# for i in users:
#     print(i)

#reduce function
# import functools
# 1
# letters = ["H","E","L","L","O"]
# word = functools.reduce(lambda x,y:x+y,letters)
# print(word)
# 2
# factorial = [1,2,3,4,5]
# result = functools.reduce(lambda x,y:x*y,factorial)
# print(result)

#filter function
# friends = [("Rachel",19),
#            ("Monica",18),
#            ("Phoebe",17),
#            ("Joey",16),
#            ("Chandler",21),
#            ("Ross",20)]
# age = lambda date:date[1]>=18
# drinking_buddies = list(filter(age,friends))
# for i in drinking_buddies:
#     print(i)

#map function
# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]
# to_euro = lambda date:date[1]*0.82
# to_dollar = lambda date:format(date[1]/0.82,".2f")
# store_dollar = list(map(to_dollar,store))
# for i in store_dollar:
#     print(i)

#sort() method = used with lists
#sort() function = used with iterables
#1
# students = ["Squidward","Sandy","Pateick","Songebob","Mr.Krabs"]
# students.sort(reverse = True)
# for i in students:
#     print(i)
#2
# students = ("Squidward","Sandy","Pateick","Songebob","Mr.Krabs")
# sorted_student = sorted(students,reverse=False)
# for i in sorted_student:
#     print(i)
#3
# students = [("Squidward","F",60),
#             ("Sandy","A",33),
#             ("Patrick","D",36),
#             ("Spongebob","B",20),
#             ("Mr.Krabs","C",78)]
# age = lambda date:date[2]
# sorted_student = sorted(students,key=age)
# for i in sorted_student:
#     print(i)

#lambda functionfunction written in 1 line using
# lambda keyword
# accepts any number of arguments, but only has one expression.
# (think of it as a shortcut)
# (useful if needed for a short period of time,
# throw-away)
# double = lambda x : x*x
# multiply = lambda x,y,:x*y
# add = lambda x,y,z:x+y+z
# full_name = lambda first_name,last_name:first_name+""+last_name
# age_check = lambda age : True if  age >=18 else False
# print(age_check(18))
# print(double(5))

#function address
#1
# def hello():
#     print("hello world")
# print(hello)
# say = print
# say(hello)
# stdio:<function hello at 0x10452beb0>
#2
# def loud(text):
#     return text.upper()
# def hello(func):
#     print(func("hello"))
# hello(loud)
#3inhance
# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend
# num = divisor(2)
# print(num(10))

#sim stdin and stdout
# info = list(input("please enter your name and age:"))
# print( "name is : ",end = "")
# for i in info:
#     if i == " ":
#         print()
#         print(" age is : ",end = "")
#         continue
#     print(i,end = "")
# print()

#dictionary comprehension
#dictionary = {key:expression for (key:value) in iterable}
#dictionary = {key: expression for (key:value) in iterable if conditional}
#dictionary = {key: (if/else) for (key:value) in iterable}
#dictionary = {key: function(value) for (key,value) in iterable}
#1
# cities_in_F = {"New York":32,"Boston":75,"Los Angeles":100,"Chiago":50}
# cities_in_C = {key:format((value-32)*(5/9),'.2f') for (key,value) in cities_in_F.items()}
# print(cities_in_C)
#2
# weather = {'New York':'snowing','Boston':'sunning','Los Angeles':'sunning','Chiago':'cloudy'}
# sunny_weather = {key:("warm" if value == "sunning" else "cold") for (key,value) in weather.items()}
# print(sunny_weather)
#3
# def check_temp(value):
#     if value >= 70:
#         return "HOT"
#     elif 69 >= value >=40:
#         return "WARM"
#     else:
#         return "COLD"
# desc_cities = {key:check_temp(value) for (key,value) in cities.items()}
# print(desc_cities)

#list comprehension
#1 
# squares =  []
# for i in range(1,11):
#     squares.append(i*i)
# print(squares)
# equal to
# squares = [i*i for i in range(1,11)]
# print(squares)
#2
# students = [100,90,80,70,60,50,40,30,20,0]
# pass_student = str(filter(lambda x:x>=60,students))
# or
# pass_student = [i for i in students if i >= 60]
# pass_student = [i if i >= 60 else print("failed")for i in students]
# print(pass_student)

#海象符
# print(happy := True)
# foods = list()
# while food := input("what's your food? ")!="quit":
#     foods.append(food)

#deletefile&dictionary&tree
# import os
# import shutil
# path = '/Users/littleprince/Desktop/test'
# try:
#     os.remove(path)#remove a file
#     os.rmkir(path)#remove an empty dictionary
#     shutil.rmtree(path)#monstrous delete a dictionary cantaining files
# except FileNotFoundError:
#     print("That file was not found!")
# except PermissionError:
#     print("You do not have permission!")
# except OSError:
#     print("You can't delete an empty dictionary")
# else:
#     print(path + "is deleted")

#movefile&dictionary
# import os
# source = 'test.txt'
# destination = '/Users/littleprince/Desktop/move.txt'
# try:
#     if os.path.exists(destination):
#         print("This file is already there")
#     else:
#         os.replace(source,destination)
#         print("move success!")
# except FileNotFoundError as e:
#     print(e)
#     print("The file does not exist")
#replace source to 'test'-a dictionary can also succeed

#copyfile() = copies contents of a file
#copy() = copyfile() + permission mode + destination can be a dirtionary
#copy2()= copy + copies metadata(file's creation and modification times)
# import shutil
# shutil.copy2("test.txt",'/Users/littleprince/Desktop')
#src,dst default mode is in the same console

#open function
#"r" - Read mode (which is a default mode) - it opens a file
#      for reading the data and if the file does not exist,
#      it return an error
#"a" - Append mode - it opens a file for appending the data,
#      it creates a new file if the file does not exist
#"w" - Write mode - it opens a file in write mode to write data
#      in it,if the file is opened in write mode then existing 
#      data will be removed,it also created a file,if the file
#      does not exist
#"x" - Creates a file - if the file already exists,it returns an error
# import os
#1
# test = "Uh oh This text has been overwritten"
# with open("/Users/littleprince/begin to believe/test.txt",'a') as file:
# with open("test.txt",'a') as file:
#     file.write(test)
# with open("test.txt") as file:
#     print(file.read())###not use except handling
#2
# with open("test.tx",'a') as file:
#     file.write(test) 

#file detection
# path = "/Users/littleprince/begin to believe/test.txt"
# if os.path.exists(path):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("That is a file")
# else:
#     print("That location doesn't exists!")

#try&exception statement
# try:
#     numerator = int(input("Enter a number to be divided: "))
#     denominator = int(input("Enter a number divide by: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero! idiot!")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers plz")
# except Exception as e:
#     print(e)
#     print("something went wrong :(")
# else:
#     print(result)

# import random
# x = random.randint(1,6)
# y = random.random()
# mylist = ['rock','paper','scissors']
# z = random.choice(mylist)
# cards = [2,3,4,5,6,7,8,9,'J','Q','K','A']
# random.shuffle(cards)
# print(cards)

#str.format() = optional method that gives users
#               more control when displaying output
#1
# animal = "cow"
# item = "moon"
# print("The "+animal+"jumped over the "+item)
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {1}".format(animal,item))#positional argument
# print("The {animal} jumped over the {animal}".format(animal = "cow",item = "moon"))
# #keyword argument
#2
# name = "Bro"
# pi = 3.1415926
# number = 100000
# print("Hello,my name is {}".format(name))
# print("Hello,my name is {:10}".format(name))
# print("Hello,my name is {:<10}".format(name))
# print("Hello,my name is {:>10}".format(name))
# print("Hello,my name is {:^10}".format(name))
# print("The number pi is {:.3f}".format(pi))
# print("The number is {:,}".format(number))
# print("The number is {:b}".format(number))
# print("The number is {:o}".format(number))
# print("The number is {:X}".format(number))
# print("The number is {:E}".format(number))

#**kwargs = parameter that will pack all argument into a dictionary
#           useful so that a function can accept a varying amount of keyward
# def hello(**kwargs):
#     # print("Hello "+kwargs['first']+" "+kwargs['last'])
#     print("Hello",end=" ")
#     for key,value in kwargs.items():
#         print(value,end=" ")
# hello(first="Bro",middle="Dude",last="Code")

#args = parameter that will pack all argument into a tuple
#       useful so that a function can accept a varying amount of argument
#1
# def add(*stuff):
#     sum = 0
#     for i in stuff:
#         sum+=i
#     return sum
# print(add(1,2,3,4,5,6))
#2
# def link(*stuff):
#     sum = []
#     for i in stuff:
#         sum.append(i)
#     return sum
# print(link(["Bro"],"Code"))

#scope
# LEGB:L=local,E=enclosing,G=global,B=built-in
# name = "Bro"
# def display_name():
#     name = "Code"
#     print(name)
# display_name()
# print(name)

#keyboard argument
# def hello(first,middle,last):
#     print("Hello "+first+" "+middle+" "+last)
# hello(last="Code",middle="Dude",last="Bro")

#dictionary
# capitals = {'USA':'Washington DC',
#             'India':'New Dehli',
#             'China':'Beijing',
#             'Russia':'Moscow',}
# capitals.update({'Germany':'Prais'})
# print(capitals['Germany'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# for key,value in capitals.items():
#     print(key,value)

#set
# utensils = {"fork","spoon","knife"}
# dishes = {"bowl","plate","cup","knife"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# dinner_table = utensils.union(dishes)
# print(utensils.intersection(dishes))
# print(utensils)
# for x in dinner_table:
#     print(x)

#tuple = collection which is ordered and unchangeable
#        used to group together related data
# student = ("Bro",21,"male")
# print(student.count("Bro"))
# print(student.index(21))

#2D lists = a list of lists
# drinks = ["coffee","soda","tea"]
# dinner = ["pizza","hamburger","hotdog"]
# dessert = ["cake","ice cream"]
# food = [drinks,dinner,dessert]
# lens = lambda date:len(date[i])
# for i in range(0,len(food)):
#     for j in range(0,lens(food)):
#         print(food[i][j],end = "\t")
#         if j == lens(food)-1:
#             print("")

#list = used to store multiple items in a single variable
# food = ["pizza","hamburger","hotdog","spaghetti","pudding"]
# food[0] = "sushi"
# food.append("ice cream")
# food.remove("hotdog")
# food.insert(0,"cake")
# food.sort(reverse = True)
# for i in food:
#     print(i)

#range
# for i in range(10):
#     print(i+1)
# for i in range(50,100+1,2):
#     print(i)
# for i in "Bro Code":
#     print(i)
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!!")

#string
#slicing = create a substring by elements from another string
#          indexing[] or slice()
#          [start:stop:step]
#1
# name = "Bro Code"
# first_name = name[:3]
# last_name = name[4:]
# reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(reversed_name)
#2
# website1 = "http://google.com"
# website2 = "http://wikpedie.com"
# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])

#print
# name = "Bro"
# print(len(name))
# print(name.find("o"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.count("o"))
# print(name.replace("o","e"))
# print(name*3)