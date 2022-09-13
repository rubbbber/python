from distutils.command.install_egg_info import to_filename
from secondcase import add,mul
from multiprocessing import Process,cpu_count
# print(cpu_count())
#map function countinuing
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

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
# age_check =lambda age : True if  age >=18 else False
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