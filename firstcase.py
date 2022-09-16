from distutils.command.install_egg_info import to_filename
from math import factorial
from sqlite3 import ProgrammingError
from turtle import st
from secondcase import add,mul
from multiprocessing import Process,cpu_count
# import functools
import time
# print(cpu_count())

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
# 1
# letters = ["H","E","L","L","O"]
# word = functools.reduce(lambda x,y:x+y,letters)
# print(word)
#2
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
# foods = list()
# while food := input("what's your food? ")!="quit":
#     foods.append(food)

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