# # # # # class Car():
# # # # #     def __init__(self,model,tires,colour):
# # # # #         self.model = model
# # # # #         self.tires=  tires
# # # # #         self.colour = colour

# # # # #     def  aboutModel():
# # # # #             print(self.model+self.tires+self.colour)

# # # # #     def lexus(self):
# # # # #             if self.model=="Lexus":
# # # # #                 print('I need this car') 
# # # # #             elif self.colour=="Black":
# # # # #                 print('This is my car')
# # # # #             else:
# # # # #                 print('i NO NEED THIS CAR')   



# # # # # obj =  Car("Lexus",4,"Black")  



# # # # # obj.lexus()        


        

# # # # # class Book():
# # # # #     def __init__(self,name,author,zhanr,date):
# # # # #         self.name = name
# # # # #         self.author = author
# # # # #         self.zhanr= zhanr
# # # # #         self.date = date
      
# # # # #     def  ageBook(self):
# # # # #         print(2024-self.date)

# # # # #                                             def allInfo(self):.zhanr+self.date)    
    

# # # # # book1 = Book('jsd','ksdkj',1971)
# # # # # book1.allInfo()

# # # # import math as m

# # # # class Point:
# # # #     def __init__(self, x, y):
# # # #         self.x = x
# # # #         self.y = y

# # # #     def get_distance_origin(self):
# # # #         return m.sqrt(self.x ** 2 + self.y ** 2)

# # # #     def move(self, dx, dy):
# # # #         self.x += dx
# # # #         self.y += dy

# # # # # Создание нескольких объектов класса Point
# # # # point1 = Point(3, 4)
# # # # point2 = Point(-1, 2)
# # # # point3 = Point(5, -2)

# # # # # Вычисление расстояния до начала координат для каждой точки
# # # # distance1 = point1.get_distance_origin()
# # # # distance2 = point2.get_distance_origin()
# # # # distance3 = point3.get_distance_origin()

# # # # print("Расстояние от точки 1 до начала координат:", distance1)
# # # # print("Расстояние от точки 2 до начала координат:", distance2)
# # # # print("Расстояние от точки 3 до начала координат:", distance3)

# # # # # Перемещение точек на разные расстояния
# # # # point1.move(2, 3)
# # # # point2.move(-1, 1)
# # # # point3.move(3, -5)

# # # # # Проверка новых координат точек
# # # # print("Новые координаты точки 1:", point1.x, point1.y)
# # # # print("Новые координаты точки 2:", point2.x, point2.y)
# # # # print("Новые координаты точки 3:", point3.x, point3.y)





# # # # class Student():
# # # #     def __init__(self,name,surname,age,gpa):
# # # #         self.name =  name
# # # #         self.surname = surname
# # # #         self.age = age
# # # #         self.gpa = gpa

# # # #     def get_fullname(self):
# # # #                 return f"{self.name} {self.surname} {self.age} {self.gpa}"
# # # # student1=  Student('jkfdf','jdkfj',45,'kejre')
# # # # print(student1.get_fullname())     
# # # # class Car():
# # # #     def __init__(self,brand,model,year,colour):
# # # #         self.brand = brand
# # # #         self.model = model
# # # #         self.year = year
# # # #         self.colour = colour
# # # #     def start_engine(self):
# # # #         print(f'Двигатель запущен {self.model}')    


# # # # car1  = Car('hsgh','shjsh',2013,'red')
# # # # car1.start_engine()        

# # # # class Bank():
# # # #     def __init__(self,account_number,balance,owner,interest_rate,is_active):
# # # #         self.account_number = account_number
# # # #         self.__balance = balance
# # # #         self.owner = owner
# # # #         self.rate = interest_rate
# # # #         self.active = is_active
# # # #     def set_deposit (self,amount):
# # # #         self.amount = amount
# # # #         print(self.__balance+amount)

# # # #     def withdraw(self,amount):
# # # #         self.amount= amount
# # # #         print(self.__balance-amount
# # # #               )
# # # #     def add_interest(self):
        
# # # #         print(self.__balance*(self.rate/100))      
# # # #     def close_account(self):
# # # #         self.active = False
# # # #     def get_display(self):
# # # #         print(f"{self.account_number,self.__balance,self.owner,self.rate,self.active}")   


# # # # acc1 = Bank(625635263,93939393,'Murtazo',10,True)       
# # # # acc1.set_deposit(898090909090909) 
# # # # class Product():
# # # #     def __init__(self,name,price,quantity,discount) :
# # # #         self.name = name
# # # #         self.price= price
# # # #         self.quantity = quantity
# # # #         self.__discount = discount

# # # #     def get_total_price(self) :
# # # #         print(f"{self.price}-{self.__discount}")  
# # # #     def set_apply_discount(self,__discount)  :
# # # #         print(f'Your discount is {self.__discount}') 
# # # #     def set_price(self,new_price) :
# # # #         self.price = new_price


# # # # pro1=  Product('Murtazo',90384)
# # # # pro1.get_total_price(823)           
# # # # class Shopp():
# # # #     def __init__(self,items,total_price):
# # # #         self.items = items
# # # #         self.total_price = total_price
# # # #     def add_item(self,product):
# # # #         self.items.append(product)
        
# # # #         # self.items.add(product)

# # # #     def remove_item(self,product)  :  
# # # #         self.items.remove(product)
# # # #     def empty_cart(self):
# # # #         self.items.clear() 
# # # #     # def calculate_total_price(self):
# # # #     #     self
# # # #     def checkout(self):
        
        
# # # #         pass
    

# # # # sho1= Shopp('Iphone',84483)
# # # # print(sho1.empty_cart())
        
# # # class Book:
# # #     def __init__(self, title, author, genre, is_available):
# # #         self.title = title
# # #         self.author = author
# # #         self.genre = genre
# # #         self.is_available = is_available

# # #     def mark_as_borrowed(self):
# # #         self.is_available = False

# # #     def mark_as_returned(self):
# # #         self.is_available = True

# # #     def display_info(self):
# # #         print(f"Title: {self.title}")
# # #         print(f"Author: {self.author}")
# # #         print(f"Genre: {self.genre}")
# # #         print(f"Availability: {'Available' if self.is_available else 'Not Available'}")


# # # class Action(Book):
# # #     def __init__(self, title, author, genre, is_available):
# # #         super().__init__(title, author, genre, is_available)

# # #     def display(self):
# # #         self.display_info()


# # # b1 = Action('woej', 'uweieu', 'whejhwej', True)
# # # b1.mark_as_borrowed()
# # import random as r


# # # class Animal:
# # #     def __init__(self, name, sound):
# # #         self.__name = name
# # #         self.__sound = sound

# # #     def make_sound(self):
# # #         return self.__sound

# # # def play_game():
# # #     animals = [
# # #         Animal("Собака", "Гав-гав"),
# # #         Animal("Кошка", "Мяу"),
# # #         Animal("Птица", "Чирик")
# # #     ]
# # #     random_animal = r.choice(animals)
# # #     guess = input(f"Угадайте звук {random_animal._Animal__name}: ")
# # #     if guess == random_animal.make_sound():
# # #         print("Правильно!")
# # #     else:
# # #         print(f"Неправильно. Звук {random_animal._Animal__name} - {random_animal.make_sound()}")

# # # play_game()

# class Animal():
#     def __init__(self,name,price,species) :
#         self.name= name
#         self.price= price
#         self.species =  species


#     def make_sound(self):
#         pass
#     def get_info(self):
#         return f"{self.name} {self.price} {self.species}"
# class Dog(Animal):
      

#     def make_sound(self):
#         return 'Гав гав'
            
# class Cat(Animal):
    
#     def make_sound(self):
#         return 'Мяу' 

# class Bird(Animal)  :
  
        

#     def make_sound(self):
#         return 'Чирик'

# # def play_game():
# #  lst = [Dog('СОБАКА',8943,'hjhjh'),Cat('КОШКА',834989,'jdfkjfd'),Bird('Птица',495849,'hjdh')]
# #  rand = r.choice(lst)
  


# #  nam = input(f'Угадай звук: {rand.name}' )
# #  if nam ==rand.make_sound():
# #     print('вы угадали')
# #  else:
# #     print(f'Вы не угадали этот звук:{rand.make_sound()} ')

# # print(play_game())

# class Pet():
#     def __init__(self):
         
        
#         self.animals = []
#     def add(self,animal):
#         self.animals.append(animal)
#     def rem(self,animal):
#         self.animals.remove (animal)
#     def all(self):
#         return self.animals
#     def get_sell(self,name):
#         for animal in self.animals:
#             if animal.get_info().startswith(str(name)):
#                 self.rem(animal)
#                 return f"{name} продан"
#         print(f"{name} не найден")
       
# a1 = Pet()
# (a1.add(Dog('SHARIK',8999,'Dog')) )
# (a1.add(Cat('TUZIK',779,'CAT')) )
# (a1.add(Bird('BRIN',99,'BIRD')) )
# for animal in a1.all():
#     (animal.get_info())


# print(a1.rem('SHARIK'))
# nim =  open('/')


# linza1= open('d:/WinUsers/Asus/Desktop/car.txt','r')
# info =(linza1.readlines())

# linza = open('d:/WinUsers/Asus/Desktop/car1.txt','w')



# def names():
#     result = []

#     sur = ['rx-350','cruiser','eshka','x5']
#     for name in info:

#         if name.strip()=='lexus':
#              result.append(name.strip()+'' + sur[0]+'\n')
#         elif name.strip()=='toyota':
#              result.append(name.strip()+ '' + sur[1]+'\n')
#         elif name.strip() =='merc':
#              result.append(name.strip() +'' + sur[2]+'\n')
#         elif name.strip()=='bmw':
#              result.append(name.strip()+'' + sur[3]+'\n')
#     return result         


# new_name=names()
# with open('d:/WinUsers/Asus/Desktop/car1.txt','a') as linza:
#    for name in new_name:
#       linza.write(name+'\t')
    
# linza1.close()
# linza.close()

from tkinter import *
import tkinter as t
root  = t.Tk()

   
       

def yakk(e):
    button = t.Label(root,text='1')
    button.place(x=300,y=64)
    return button







       
 
label = t.Button(root,text="1",command=yakk
    width=5,
    height=5,
    bg="blue",
    fg="yellow")
label.place(x=50,y=34)
labe = t.Button(root,text="2",command=yakk(),
    width=5,
    height=5,
    bg="blue",
    fg="yellow")
labe.place(x=175,y=34)
lab = t.Button(root,text="3",command=yakk(),
    width=5,
    height=5,
    bg="blue",
    fg="yellow")
lab.place(x=300,y=34)
lab = t.Button(root,text="4",command=yakk(),
    width=5,
    height=5,
    bg="blue",
    fg="yellow")
lab.place(x=50,y=140)
la = t.Button(root,text="5",command=yakk(),
    width=5,
    height=5,
    bg="grey",
    fg="yellow")
la.place(x=175,y=140)
l = t.Button(root,text="6",command=yakk(),
    width=5,
    height=5,
    bg="black",
    fg="yellow")
l.place(x=300,y=140)
lu = t.Button(root,text="7",command=yakk(),
    width=5,
    height=5,
    bg="yellow",
    fg="blue")
lu.place(x=50,y=256)
li = t.Button(root,text="8",command=yakk(),
    width=5,
    height=5,
    bg="green",
    fg="yellow")
li.place(x=175,y=256)
lb = t.Button(root,text="9",command=yakk(),
    width=5,
    height=5,
    bg="orange",
    fg="yellow")
lb.place(x=300,y=256)
lk = t.Button(root,text="0",command=yakk(),
    width=5,
    height=5,
    bg="red",
    fg="yellow")
lk.place(x=175,y=370)



root.title('akakak')
root.geometry('500x500')
root
root.mainloop()
