# class Tweet:
#     def __init__(self, message):
#         self.x = message
#
# a = Tweet('Sample')
# print(a.x)

# class Tweet:
#     def __init__(self, message, message1):
#         self.x = message
#         self.y = message1
#     def print_tweet(self):
#         print(self.x)
#         print(self.y)
# t = Tweet('Tweet it', 'Twitter')
# t.print_tweet()

# class ClassLearning:
#
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#         # result1 = num1 + num2
#         # print(result1)
#
#     def add_to_another_number(self, n1):
#         res = self.num1 + self.num2 + n1
#         # res = result1 + n1 -> wrong code because result1 is not defined, only the instances with the keyword 'self'
#         # will be accessed from the ClassLearning()
#         print(res)
# total = ClassLearning(9,5)
# total.add_to_another_number(1)

# Sample of sorting with a function passed in the key

# list_of_nums = [8, 15, 42, 23, 4, 16]
# sorted_list = sorted(list_of_nums)
# print(sorted_list)
# print(list_of_nums)
#
# list_of_orders = ['#53', '#7', '#3356', '#19', '#17185']
# print(list_of_orders)
# print(sorted(list_of_orders))
#
# sorted_by_length = sorted(list_of_orders, key=len)
# print(sorted_by_length)
#
# def orders_sorting(string):
#     return  int(string[1:])
#
# sorted_by_size = sorted(list_of_orders, key=orders_sorting)
# print(sorted_by_size)

# Another sample of sorting with passed in functions in the key, with a list and a dictionary

# list_of_guitars =[
#     {
#         'guitar': 'Cort',
#         'rating': 2,
#         'type': 'telecaster'
#     },
#     {
#         'guitar': 'Jay Turser',
#         'rating': 1,
#         'type': 'stratocaster',
#     },
#     {
#         'guitar': 'Aria',
#         'rating': 3,
#         'type': 'thin series'
#     },
# ]
# # print(list_of_guitars)
# # sorted(list_of_guitars) -> this will produce an error because python will have no parameters to compare
# # print(list_of_guitars[2]['rating'])
# def sorted_by_rating(guit):
#     return guit['rating']
# result1 = sorted(list_of_guitars, key=sorted_by_rating)
# print(result1)
# print('==========')
# print(result1[0])
# print('==========')
# # Order in reverse
# result2 = sorted(list_of_guitars, key=sorted_by_rating,  reverse=True)
# print(result2)
# print('==========')
# print(result2[0])

# Two ways of creating a list using list comprehension
# nums = [0,1,2,3,4,5,6,7,8,9]
# numlist1 = []
# for i in nums:
#     numlist1.append(i)
# print(numlist1)
# print('==========')
# # Easier way of creating a list
# numlist2 = [j for j in nums]
# print(numlist2)
# # Creating a list comprehension with if statements
# numlist3 = [j for j in nums if j%2 == 0]
# print(numlist3)
# # Creating a list comprehension squaring each element
# numlist4 = [j*j for j in nums]
# print(numlist4)

# Another example of list comprehension
# list1 = []
# for i in 'abcd':
#     for j in range(0,4):
#         list1.append((i,j))
# print(list1)
# # The code above will have the same output as this code below:
# list2 = [(i,j) for i in 'abcd' for j in range(4)]
# print(list2)

# # Example of zip
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(list(zip(names, heroes)))
#
# # Using a for loop. Creating a dictionary{'name': 'hero'} for each name, hero in zip(names, heroes)
# dict1 = {}
# for name, hero in zip(names, heroes):
#     dict1[name] = hero
# print(dict1)
#
# # Using dictionary comprehension
# # dict2 = {name1: hero1 for name1, hero1 in zip(names, heroes)}
# # print(dict2)
# dict2 = {name: hero for name, hero in zip(names, heroes)}
# print(dict2)
#
# # To have an exception
# dict3 = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
# print(dict3)

# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# zipped = zip(numbers, letters)
# print(list(zipped))

# Examples of set comprehension
# Using for loop, a set in Python is to output only a list with only unique values
# nums  = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9,9,9,9,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)
#
# # Using set comprehension
# my_set1 = {n for n  in nums}
# print(my_set1)

# Generator Expressions
# Outputting the square of each element
# nums1 = [1,2,3,4,5,6,7,8,9,10]
# def gen_func(nums1):
#     for n in nums1:
#         yield  n*n
#
# my_gen = gen_func(nums1)
# for i in my_gen:
#     print(i)
#
# # Using  generator expression
# my_gen1 = (n*n for n in nums1)
#
# for j in my_gen1:
#     print(j)

# arr = ['-', '+', '', '--', '++']
# arr_sorted = sorted(arr, reverse=True)
# print(arr_sorted)
#
# x = lambda a, b: (a * b)/2
# print(x(5, 6))
#
# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# Input: ['B++', 'C-', 'C+', 'A31-', 'B', 'B22-', 'B70', 'C', 'A82+']
# Output: ['C-', 'C', 'C+', 'B', 'B++', 'B22-', 'B70', 'A31-', 'A82+']

# arr = ['','-','+']
# arr_sorted = sorted(arr)
# print(arr_sorted)
# for i in arr_sorted:
#     # print(i)
#     if i == '':
#         print(0)
#     elif i == '-':
#         print(1)
#     elif i == '+':
#         print(2)

# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
# user1 = User('001', 'CouponBond')
# print(user1.id)
# print(user1.username)
# print(user1.followers)

# user2 = User('002', 'KokomBond')
# print(user2.id, user2.username, user2.followers)
#
# user1.follow(user2)
# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)

# user1 = User()
# user1.id = '001'
# user1.username = 'PaperBond'
# print(user1.username)
# print(user1.id)
# print(user1.username + user1.id)
# print(f'{user1.username} {user1.id}')

# user2 = User()
# user1.id = '002'
# user1.username = 'CouponBond'
# print(user1.username)
# print(user1.id)
# print(user1.username + user1.id)
# print(f'{user1.username} {user1.id}')

# class Car:
#     def int(self, seats):
#         my_Car = Car(5)
#         self.seats = seats
#         print(my_Car)

# dicts = {}
# keys = range(4)
# values = ["Hi", "I", "am", "John"]
# for i in keys:
#     for x in values:
#         dicts[i] = x
# print(dicts)

# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#
# sort_by_key = dict(sorted(x.items(),key=lambda item:item[0]))
# sort_by_value = dict(sorted(x.items(), key=lambda item: item[1]))
#
# print(sort_by_key)
# print(sort_by_value)
# print(sorted(sort_by_value))

# dictionary = {"A": 9,  "B": 8,  "C": 10}
# print(' '.join(sorted(dictionary.keys(),key=lambda x: -dictionary[x])))

# print(" ")
# print("█")
# print('██████')
# print('██  ██')
# print('██████')
#
# print('  ███')
# print('██  ██')
# print('██████')

# Simple initialization sample
# class Question:
#
#     def __init__(self, qtext, qanswer):
#         self.qtext = qtext
#         self.qanswer = qanswer
#
# result = Question('sampleText', 'sampleAnswer')
# print(result.qtext)
# print(result.qanswer)

# from turtle import Turtle, Screen
#
# tartol_d_turtle = Turtle()
# tartol_d_turtle.setpos(-375,-375)
# tartol_d_turtle.shape('turtle')
# tartol_d_turtle.color('darkcyan')
# tartol_d_turtle.width(10)
# tartol_d_turtle.speed('slowest')
#
# for n in range(4):
#     for _ in range(10):
#         # tartol_d_turtle.left(90)
#         tartol_d_turtle.forward(25)
#         tartol_d_turtle.penup()
#         tartol_d_turtle.forward(25)
#         tartol_d_turtle.pendown()
#         tartol_d_turtle.forward(25)
#     tartol_d_turtle.left(90)
# screen = Screen()
# screen.exitonclick()

# for _ in range(4):
#     tartol_d_turtle.forward(300)
#     tartol_d_turtle.left(90)
#
# # Sample of importing modules
# # When you are going to use it once or a few times, do this approach
# import turtle
# createdTurtle = turtle.Turtle()
#
# # When you are going to use the module many times, use this approach
# from turtle import Turtle
# createdTurtle1 = Turtle()
# createdTurtle2 = Turtle()
# createdTurtle3 = Turtle()
# createdTurtle4 = Turtle()
# createdTurtle5 = Turtle()
# createdTurtle6 = Turtle()
#
# # Renaming or giving a module an alias
# import turtle as t
# createdTurtle7 = t.Turtle()
#
# import heroes
# print(heroes.gen())
#
# import villains
# print(villains.gen())

# Infinite polygon

# import random
# rand_color = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
# print("A Random color is :",rand_color)

# # Infinite polygon
# def polygon(n):
#     from turtle import Turtle, Screen
#     import random
#     poly_turtle = Turtle()
#     poly_turtle.setpos(-45, 400)
#     poly_turtle.shape('turtle')
#     poly_turtle.speed('slow')
#     poly_turtle.width(3)
#     poly_turtle.color('blue')
#     poly_turtle.penup()
#     poly_turtle.forward(100)
#     poly_turtle.pendown()
#
#     s = 3
#     while s<=n:
#         rand_color = ["#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
#         for i in range(n):
#             poly_turtle.color(rand_color)
#             poly_turtle.right(360/n)
#             poly_turtle.forward(100)
#         n +=1
# polygon(3)

# Exercise Output
# 1 / 1
# 2 / 1 / 1,2
# 3 / 1 / 1, 2 / 1,2,3
# n = 10
# j = 1
# while j <= n:
#     arr = []
#     for k in range(j):
#         # print(k+1)
#         arr.append(k+1)
#     j+=1
#     print(arr)