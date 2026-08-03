# 1. Generate Atleassalaryt 5 different Errors.
# #syntax error
# age=20
# if(age>19)
# print("age is above the 19")

#zero divisible error

# a=int(input("enter the value of :-"))
# ans=a/0
# print(ans)

#index error
# l=[0,1,2]

# print(l[4])

#type error
# result = "age" + 25
# print(result)

#indentation error

# def hii():
# print("hello world")
# hii()

# 2. Handle all the 5 different Erros using Exception Handling.

# #syntax error
# try:
#     age=20
#     if(age>19)
#     print("age is above the 19")
# except:
#     print("syntax error")

#zero divisible error
# try:
#     a=int(input("enter the value of :-"))
#     ans=a/0
#     print(ans)
# except:
#     print("zero divsible error")

#index error
# try:
#     l=[0,1,2]
#     print(l[4])
# except:
#     print("index error")


# #type error
# try:
#     result = "age" + 25
#     print(result)
# except:
#     print("type error")

#indentation error
# try:
#     def hii():
#     print("hello world")
#     hii()
# except:
#     print("indendation error")


# 3. Handle an error with try-except-else.

#def divisble(numerator,denomation):
#     try:
#         num=numerator/denomation
#     except:
#         print("zero divisble error")
#     else:
#         print("not divid the number in zero")

# divisble(20,0)
# divisble(10,2)

#4. Handle an error with try-except-else-finally

# def divisble(numerator,denomation):
#     try:
#         num=numerator/denomation
#     except:
#         print("zero divisble error")
#     else:
#         print("not divid the number in zero")
#     finally:
#         print("file is closed and error is not solved")

# divisble(10,2)
# divisble(10,0)

# 5. Use raise for generating User Defined Exception for minimum length of a list should be 5

# class listsort(Exception):
#     pass

# def list(input):
#     if len(input)<5:
#         raise listsort(f"list is minimum 5 length.{len(input)}")
#     return"list processing"
        
# mylist=[1,2,3,4,5,6]
# print(list(mylist))

# mylist=[1,2,3]
# print(list(mylist))


# 6. Create a file 'mod.py' with a class with multiple methods and few member 
# variables. Also create an individual methods outside the class as well. Create 
# another file 'test.py' and without executing the 'mod.py' get it executed using the 
# 'test.py' file
# import mod
#6
#file name is mod
# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
    
#     def display(self):
#         print("Name",self.name)
#         print("age",self.rollno)
#     def display_name(self):
#         print("Name:",self.name)

# def add(a,b):
#     return a+b
# def message():
#     print("this is a function from of mod.py")  

#file name is test.py
#import mod
# s1 = mod.student("het",10)

# s1.display()
# s1.display_name()

# print("sum=",mod.add(10,20))
# mod.message()

#7
#mod.pu file
# class calcuator:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b

#test.py file

# from mod import calcuator

# obj=calcuator()

# print("addition:-",obj.add(10,5))
# print("subtratcion:-",obj.sub(20,10))
# print("multiplication",obj.mul(20,10))
#8
#mod.py file
# def message():
#     print("these is student class :-")
    
# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def display(self):
#         print("Name:-",self.name)
#         print("rollno:-",self.rollno)
  

#test.py file
# from mod import message

# message()

# s1 = mod.student("het",10)
# s1.display()

# #9

# from mypackage.add import add
# from mypackage.sub import sub

# a=10
# b=20
# add(a,b)
# sub(a,b)

##10

# from mypackage.add import add
# a=10
# b=20
# add(a,b)

#11
# from mypackage import modle

# s1=modle.student("het",101)
# s1.display()



##12

# file=open("test_flie.txt","w")

# file.write("Hello!,this is a file created")

# file.close()

# print("string writting is succesfully")


# file=open("test_flie.txt","w")

# file.write("first line of code in the file")
# file.close()

# print("string writting is succesfully")


#13
# file=open("test_flie.txt","r")

# context=file.read()
# print(context)

#14

# file=open("test_flie.txt","r")

# for line in file:
#     print(line,end="")

# file.close()


#15

# file=open("test_flie.txt","a")

# file.write("\nthese string is append in the file")

# file.close()
# print("line append is succesfully")

# #16
# file=open("test_file.data.txt","wb")

# file.write(b"these code is binary form")
# file.close()
# print("data stored in test_file.data.txt")


# file = open("test_file.data.txt", "wb")

# data = b"Hello Python Binary File"

# file.write(data)
# file.close()

# print("Binary data written successfully.")

# file = open("test_file.data", "rb")

# content = file.read()

# print("Binary data read from file:")
# print(content)

# file.close()
#17
import pickle

# num=12
# pi=3.14
# name="het"
# bol=True
# fruits=["apple","banana","orange"]
# person={'name':'het','age':20}

# with open('my_vaiables.data.text','wb') as file:
#     pickle.dump(num,file)
#     pickle.dump(pi,file)
#     pickle.dump(name,file)
#     pickle.dump(fruits,file)
#     pickle.dump(person,file)
# print("all datatypes is dump in my_vaiables.data.text")


# with open('my_vaiables.data.text',"rb") as file:
#     num=pickle.load(file)
#     pi=pickle.load(file)
#     name=pickle.load(file)
#     bol=pickle.load(file)
#     fruits=pickle.load(file)
#     person=pickle.load(file)
# print(num,pi,name,bol.fruits,person)

# #18
# import pickle
# name="het"
# age=20
# gender="male"
# with open("my_vaiables.data.txt","wb") as file:
#     pickle.dump(name,file)
#     pickle.dump(age,file)
#     pickle.dump(gender,file)
# file.close()

# with open("my_vaiables.data.txt","rb") as file:
#     name = pickle.load(file)
#     age= pickle.load(file)
#     gender =pickle.load(file)
#     print(name,age,gender)
# file.close()

#19
# from datetime import datetime,date

# current_date=date.today()
# print(current_date)
# current_datetime=datetime.now().date()
# print(current_datetime)

# # 20
# from datetime import datetime,date

# current_date=datetime.now()
# st=str(current_date)
# print(st)

# #21
# from datetime import date
# date1=date(2024,5,1)
# date2=date(2024,4,1)

# difference=date1-date2
# print(difference)

#22
# from datetime import date
# from dateutil.relativedelta import relativedelta
# birth_date=date(2006,6,2)

# today=date.today()
# age=relativedelta(today,birth_date)
# print(age)


# #23
# from datetime import  date,timedelta
# current_day=date.today()
# first_weekday=current_day+timedelta(weeks=1)

# print(current_day)
# print(first_weekday)

# #24
# from datetime import date,timedelta
# current_day=date.today()
# next_year=current_day+timedelta(days=365)

# print(current_day)
# print(next_year)


#25
# from datetime import date,timedelta
# current_day=date.today()
# next_month=current_day+timedelta(days=30)
# print(current_day)
# print(next_month)

# #26
# from datetime import date
# today=date.today()
# td=today.replace(day=1)
# print(td)

#27
# from datetime import date
# today=date.today()
# ty=today.replace(month=1,day=1)
# print(ty)

# #28
# import calendar
# from datetime import date

# today=date.today()
# year=today.year
# month=today.month

# calendar.setfirstweekday(calendar.MONDAY)

# weeks=calendar.monthcalendar(year,month)

# print(weeks)

# #29
# import calendar
# from datetime import date

# today=date.today()
# first_day=today.replace(day=1)
# last_day=today.replace(day=30)
# print(today)
# print(first_day)
# print(last_day)

# #30
# from datetime import datetime
# import calendar

# today=datetime.now()

# first_day=today.replace(day=1)

# last_day=calendar.monthrange(today.year,today.month)[1]
# last_day=today.replace(day=last_day)

# def suffix(day):
#     if 11 <= day <=13:
#         return "th"
#     elif day %10==1:
#         return "st"
#     elif day % 10 ==2:
#         return "nd"
#     elif day %10 ==3:
#         return "rd"
#     else:
#         return "th"

# def formate(dt):
#     return dt.strftime(f"%d{suffix(dt.day)}%B %Y %A %I %M %S %p")

# print("first date of current month")
# print(format(first_day))

# print("last day of current month")
# print(format(last_day))

#31
# import random
# random=random.randint(1,100)
# print(random)

# #32
# import random
# random=random.sample(range(1,100),4)
# print(random)

# #33
# import random
# l=[1,2,3,4,5,6,7,8,9,10]
# random.shuffle(l)
# print(l)

#34
# import os
# os.system("echo the shell script")


#35
# import re
# url=input("enter a URL")
# pattern=r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/[^\s]*)?$"
# if re.match(pattern,url):
#     print("valid url")
# else:
#     print("not valid url")
#36
# import re #re means is regualr experision libiaries

# email_regx=r"^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# is_vaild=bool(re.match(email_regx,"'ser@example.com"))
# print(is_vaild)

# #37
# import re
# pincode=input("enter the 6 digit:-")

# pattern=r"^[1-9][0-9]{5}$"

# if re.fullmatch(pattern,pincode):
#     print("vaild pin code ")
# else:
#     print("invaid pincode")

# #38
# class student:
#     def __init__(self,name,reg_no,roll_no,standard,admission_year):
#         self.name=False
#         self.reg_no=False
#         self.roll_no=False
#         self.standard=False
#         self.admission_year=False
#         self.marks=[]
#         self.result=False

#         if not (isinstance(name,str)and
#                 isinstance(reg_no,str)and
#                 isinstance(roll_no,str)and
#                 isinstance(standard,str)and
#                 isinstance(admission_year,str)):
#             raise TypeError("All values must be string")

#         if not name.isalpha():
#             raise ValueError("Name must contain only alphabets.")
#         if not reg_no.isalnum():
#             raise ValueError("Registration number must be alphanumeric")
#         if not roll_no.isdigit():
#             raise ValueError("Roll no is numberic.")
#         if not standard.isdigit():
#             raise ValueError("standard is numberic")
#         if not admission_year.isdigit():
#             raise ValueError("admmission year is must be numberic ")

#         self.name=name
#         self.reg_no=reg_no
#         self.roll_no=roll_no
#         self.standard=standard
#         self.admission_year=admission_year

#         def add_marks(self,subject_marks):

#             for subject, mark in subject_marks.items():

#                 if mark > 100:
#                     raise ValueError("Marks can be grater than Zero")

#                 if mark>=40:
#                     result="pass"
#                 else:
#                     result="fail"

#                 data={
#                     "Subject":subject,
#                     "Marks":mark,
#                     "Result":result
#                 }

#                 self.mark.append(data)
#         def calcuate_grade(self,percentage,final_result):


        
        
# class Student:

#     # Constructor
#     def __init__(self, name, reg_no, roll_no, standard, admission_year):

#         # Default values
#         self.name = False
#         self.reg_no = False
#         self.roll_no = False
#         self.standard = False
#         self.admission_year = False
#         self.marks = []      # Blank list
#         self.result = False

#         # Check all values are strings
#         if not (isinstance(name, str) and
#                 isinstance(reg_no, str) and
#                 isinstance(roll_no, str) and
#                 isinstance(standard, str) and
#                 isinstance(admission_year, str)):
#             raise TypeError("All values must be string.")

#         # Validation
#         if not name.isalpha():
#             raise ValueError("Name must contain only alphabets.")

#         if not reg_no.isalnum():
#             raise ValueError("Registration Number must be alphanumeric.")

#         if not roll_no.isdigit():
#             raise ValueError("Roll Number must be numeric.")

#         if not standard.isdigit():
#             raise ValueError("Standard must be numeric.")

#         if not admission_year.isdigit():
#             raise ValueError("Admission Year must be numeric.")

#         # Assign values
#         self.name = name
#         self.reg_no = reg_no
#         self.roll_no = roll_no
#         self.standard = standard
#         self.admission_year = admission_year

#     # Method to add marks
#     def add_marks(self, subject_marks):

#         for subject, mark in subject_marks.items():

#             if mark > 100:
#                 raise ValueError("Marks cannot be greater than 100.")

#             if mark >= 40:
#                 result = "PASS"
#             else:
#                 result = "FAIL"

#             data = {
#                 "Subject": subject,
#                 "Marks": mark,
#                 "Result": result
#             }

#             self.marks.append(data)

#     # Function to calculate grade
#     def calculate_grade(self, percentage, final_result):

#         if final_result == "FAIL":
#             return "F"

#         elif percentage >= 95:
#             return "O+"

#         elif percentage >= 90:
#             return "O"

#         elif percentage >= 85:
#             return "A+"

#         elif percentage >= 80:
#             return "A"

#         elif percentage >= 75:
#             return "B+"

#         elif percentage >= 70:
#             return "B"

#         elif percentage >= 60:
#             return "C"

#         elif percentage >= 50:
#             return "D"

#         elif percentage >= 40:
#             return "E"

#     # Method to generate result
#     def generate_result(self):

#         total_marks = 0
#         max_marks = len(self.marks) * 100
#         final_result = "PASS"

#         print("*" * 70)
#         print("Name :", self.name)
#         print("Roll No :", self.roll_no)
#         print("Standard :", self.standard)
#         print("*" * 70)

#         print("{:<15}{:<15}{:<15}{:<15}{:<10}".format(
#             "Subject", "Total", "Passing", "Obtained", "Result"))

#         for item in self.marks:

#             total_marks += item["Marks"]

#             if item["Result"] == "FAIL":
#                 final_result = "FAIL"

#             print("{:<15}{:<15}{:<15}{:<15}{:<10}".format(
#                 item["Subject"],
#                 100,
#                 40,
#                 item["Marks"],
#                 item["Result"]
#             ))

#         print("*" * 70)

#         print("Total Marks Obtained :", total_marks)

#         if final_result == "PASS":
#             percentage = (total_marks / max_marks) * 100
#             print("Percentage : {:.2f}%".format(percentage))
#         else:
#             percentage = 0
#             print("Percentage : --")

#         grade = self.calculate_grade(percentage, final_result)

#         print("Final Result :", final_result)
#         print("Grade :", grade)


# s1 = Student("Rahul", "REG101", "1", "10", "2024")

# marks = {
#     "Math": 90,
#     "Science": 80,
#     "English": 35
# }

# s1.add_marks(marks)

# s1.generate_result()

        

# #39
# x={'a':1,'b':2}
# print(x)

# # 40
# text = "Skyscend Business Solutions Pvt. Ltd."

# print(text[:3].upper(), text.split()[0].upper(), text.split()[1][:3], text.split()[2].lower())
#41

# power = lambda base,expoenent:base**expoenent
# result=power(2,3)
# print(result)

#42

# text="python programming"

# assert len(str)>=10,f"error:string length is {len(text)},must be at least 10"
# print("assertion passed")

#43

# file= open("python.txt","r")

# content=file.read()
# exec(content) #exec is means execut the text file in python file
# file.close()


# #44
# result=[2*x +11 for x in range(1,11)]
# print(result)

# #45
# even_number=list(range(2,100,2))
# print(even_number)

# #46
# result=[i**2 for i in range(1,26)]
# print(result)

#47

# def prime_number():
#     for num in range(2, 101):
#         is_prime=True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime =False
#                 break
#         if is_prime:
#             yield num

# print("prime number between 1 and 100:")
# for prime in prime_number():
#     print(prime,end=" ")

#48
# import random

# def random_genter():
#     numbers=list(range(1,101))
#     random.shuffle(numbers)

#     for num in numbers[:10]:
#         print(num)

# random_genter()


#49

# dec=15

# binary=bin(dec)
# print("binary Number:",binary)
# octal=oct(dec)
# print("octal Number:-",octal)
# hexadecmial=hex(dec)
# print("hexadecimal Number:-",hexadecmial)

#50

# def hex_convert(hex_str):

#     decimal_value=int(hex_str,16)
#     binary_value=bin(decimal_value)
#     octal_number=oct(decimal_value)

#     print("hexadecimal number:-",hex_str)
#     print("decimal number:-",decimal_value)
#     print("binary Number:-",binary_value)
#     print("octal Number:-",octal_number)

# hex_convert('10')

#51

# def oct_convet(oct_str):

#     decimal_value=int(oct_str,8)
#     binary_value=bin(decimal_value)
#     hexa_value=hex(decimal_value)

#     print("octal Number:-",oct_str)
#     print("binary Number:-",binary_value)
#     print("decimal Number:-",decimal_value)
#     print("hexadecimal Number:-",hexa_value)

# oct_convet('13')


#52

# def bin_convert(bin_str):

#     decimal_value=int(bin_str,2)
#     octal_value=oct(decimal_value)
#     hexa_value=hex(decimal_value)

#     print("binary Number:-",bin_str)
#     print("decimal Number:-",decimal_value)
#     print("octal Number:-",octal_value)
#     print("Hexadecimal Number:-",hexa_value)

# bin_convert('11010001111100111')


#53

# ascii_gen1=(
#     (chr(i),ord(chr(i)))
#     for i in range(65,91)
# )

# ascii_gen2=(
#     (chr(i),ord(chr(i)))
#     for i in range(97,123)
# )

# ascii_gen3=(
#     (chr(i),ord(chr(i)))
#     for i in range(48,58)
# )

# ascii_dict=dict(list(ascii_gen1) + list(ascii_gen2) + list(ascii_gen3))

# print(ascii_dict)

#54

# negative_interge=-3
# result=abs(negative_interge)
# print("negative value covnvert to positive value",result)

#55

# def calcuate(a,b):
#     maximum=max(a,b)
#     print(maximum)

# calcuate(10,30)

# #56
# class info():
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id

#     def display(self):
#         print("name of person",self.name)
#         print("id of person",self.id)
        
# in1=info('abc','101010')
#
# if hasattr(in1,"name"):
#     print("attribute is exisited")
# else:
#     print("attrbuite is not exisited")

#2
# if hasattr(in1,'id'):
#     current_value=getattr(in1,'id')
#     print("attribute value:- ",current_value)
# else:
#     print("attribute is not exisited")

# #3
# if hasattr(in1,'id'):
#     setattr(in1,'id''rollno')
#     print(f"update is successfully{in1.id}")
# else:
#     print("attrbuited is not exisited")

#4
# if hasattr(in1,'id'):
#     delattr(in1,'id')
#     print(f'delete the element in class')
    
# else:
#     print("attributed is not deleted is not exisited the class")

#57
# import random

# numbers=[random.randint(0,1) for _ in range(10)]

# print(numbers)

# if all(numbers):
#     print("ALL")
# elif any(numbers):
#     print("any")
# else:
#     print("None")

#58
# import random

# numbers=[random.randint(0,10) for i in range(10)]

# maximum=max(numbers)
# print(numbers)
# print(maximum)

# #59
# import random

# numbers=[random.randint(0,10) for i in range(10)]

# minmum=min(numbers)
# print(numbers)
# print(minmum)

# #60
# import random

# numbers=[random.randint(0,10) for i in range(10)]

# def even(n):
#     return n%2==0
# def odd(n):
#     return n%2!=0

# even_number=list(filter(even,numbers))
# odd_number=list(filter(odd,numbers))

# print("even number",even_number)
# print("odd nummber",odd_number)

# # # #61
# def cube(n):
#     return n**3
    

# numbers=[1,2,3,4,5,6,7,8,9,10]

# result=map(cube,numbers)
# print(list(result))

#62
# l1=[1,2,3,4,5]
# l2=[2,3,4,6,7]

# result=list(map(lambda x,y:x*y,l1,l2))
# print(l1)
# print(l2)
# print(result)

#63
# import random
# numbers=[random.randint(0,100) for i in range(15)]

# total=sum(numbers)
# print(total)


# #64
# import random
# import string

# char=[random.choice(string.ascii_letters) for i in range(10)]

# print("characters list",char)

# result="".join(char)
# print(result)

#65
#global variable
# name="shakshi"
# age='20'
# class student:
#     def show(self):
#         name="het"
#         age=20
#         print("\nglobal varablible")
#         print(globals())

#         print("\n local varalible")
#         print(locals())

# s1=student()
# s1.show()


# #66
# class A:
#     def show(self):
#         print("these is first class")
# class B(A):
#     def display(self):
#         print("these is base class")

# b1=B()

# if issubclass(B,A):
#     print("B is subclass A is parent class")
# else:
#     print("b is not a subclass of a")


# #67
# l1=['a','b','c','d','e']
# l2=[1,2,3,4,5]

# result=dict(zip(l1,l2))
# print(result)

#68
# import random

# number=[random.randint(1,100) for i in range(25)]

# print(number)

# n=len(number)

# for i in range(n):
#     for j in range(0,n-i-1):
#         if number[j]>number[j+1]:
#             number[j],number[j+1]=number[j+1],number[j]

# print("sorted list")
# print(number)

# #69
# list=[[4,'a'],[9,'x'],[10,'c'],[25,'z'],[32,'b']]

# result=sorted(list,key=lambda x:x[1])
# print(result)

# #70
#  def calcuate(a,b):
#     if isinstance(a,(int,float)) and isinstance(a,(int,float)):
#         print("addition",a+b)
#     else:
#         print("not data found")

# calcuate(10,20.5)


#71

# x=20
# y=30
# def outer():
#     a=100
#     global b
#     b=200
#     print("\ninside outer function")
#     print("local variable",locals())
#     print("global variable",globals())
#     def inner():
#         p=300
#         global y
#         q=500
#         print("\ninside inner function")
#         print("local variable",locals())
#         print("global variable",globals())
#     inner()
# outer()

# print("\nouterside the function")
# print("local variable",locals())
# print("global variable",globals())
#print("hello world")