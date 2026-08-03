#1int  convert to float boolan and string
# a=10
# b=float(a)
# print(b)
# c=bool(a)
# print(c)
# d=str(a)
# print(d)

#2float convert to int boolan AND string
# a=10.5
# b=int(a)
# print(b)
# c=bool(a)
# print(c)
# d=str(a)
# print(d)

#3boolan to convert to float int AND string
# a=True
# b=float(a)
# print(b)
# c=int(a)
# print(c)
# d=str(a)
# print(d)

#4string to convert to float int AND boolan
# a="90"
# b=float(a)
# print(b)
# c=int(a)
# print(c)
# d=bool(a)
# print(d)


#5int,string,float values convert in boolan and zero ans 
# a=0
# b=bool(a)
# print(b)
# c=0.0
# d=bool(c)
# print(d)
# str=""
# bool=bool(str)
# print(bool)

#6Arithmatics operation
# val1=int(input("enter the value in 1:-"))
# val2=int(input("enter the value in 2:-"))
# sum=val1+val2
# print(sum)
# sub=val1-val2
# print(sub)
# mul=val1*val2
# print(mul)
# div=val1/val2
# print(div)

#7Bit-wise operation
# val1=int(input("enter the value in 1:-"))
# val2=int(input("enter the value in 2:-"))
# bit_and=val1&val2
# print(bit_and)
# bit_OR=val1^val2
# print(bit_OR)
# bit_not=(~val1)
# print(bit_not)
# bit_left=(val1 << 2)
# print(bit_left)
# bit_right=(val1 >> 2)
# print(bit_right)


#8Relation operation
# val1=int(input("enter the value in 1:-"))
# val2=int(input("enter the value in 2:-"))

# print("equal to the value:-",val1==val2)
# print("less than equal to the value:-",val1<=val2)
# print("less than the value:-",val1<val2)
# print("grater to the value:-",val1>val2)
# print("grater than to the value:-",val1>=val2)
# print("notequal to the value:-",val1!=val2)

#9logical operation
# val1=int(input("enter the value in 1:-"))
# val2=int(input("enter the value in 2:-"))

# print("logical and to the value:-",(val1<val2)and(val1>val2))
# print("logical or to the value:-",(val1<val2)or(val1>val2))
# print("logical not to the value:-",not(val1>val2))


#10 input 3 number is biggest number
# num1=int(input("enter the number:-"))
# num2=int(input("enter the number:-"))
# num3=int(input("enter the number:-"))

# if num1>num2 and num1>num3:
#     print("num1 is biggest value")

# elif num2>num1 and num2>num3:
#     print("num2 is biggest value")

# else:
#     print("num3 is biggest value")

# if num1<num2 and num1<num3:
#     print("num1 is smaller value")

# elif num2<num1 and num2<num3:
#     print("num2 is smaller value")

# else:
#     print("num3 is smaller value")
# 11. Create another script/program using 'input' and pass all the three parameters as a
# single input and execute the same program as mentioned above.

# num1, num2, num3= input("enter 3 parameters sparated by spaces:").split()

# print(f"value1:{num1}")
# print(f"value2:{num2}")
# print(f"value3:{num3}")

# if num1>num2 and num1>num3:
#     print("num1 is biggest value")

# elif num2>num1 and num2>num3:
#     print("num2 is biggest value")

# else:
#     print("num3 is biggest value")

# if num1<num2 and num1<num3:
#     print("num1 is smaller value")

# elif num2<num1 and num2<num3:
#     print("num2 is smaller value")

# else:
#     print("num3 is smaller value")



# import sys
# num1, num2, num3= input("enter 3 parameters sparated by spaces:").split()

# print(f"value1:{num1}")
# print(f"value2:{num2}")
# print(f"value3:{num3}")




#12odd number to 1 to 10 number while loop in revesed
# i=10
# while(i>=1):
#     if(i%2!=0):
#         print((i))
#     i-=1

#13 odd number to 1 to 10 number while loop in revesed
# for i in range(10,-1,-1):
#     if(i%2!=0):
#         print(i)
# 14odd number to 1 to 10 number while loop in reversed to continue
# i=10
# while(i>=1):
#     if(i%2!=0):
#         i-=1
#         continue
#     print((i))
#     i-=1

# # odd number to 1 to 10 number for loop in revesed
# for i in range(10,-1,-1):
#     if(i%2!=0):
#         continue
#     print(i)

# 15. Take 10 numbers in a list(array) and print only first 3 numbers using loop

# l=[1,2,3,4,5,6,7,8,9,10]
# i=0

# while i<3:
#     print(l[i])
#     i+=1

# for i in range(3):
#     print(l[i])

#16create the funtion and print 10 number
# def sum():
#     i=0
#     while i<=10:
#         print(i)
#         i+=1
# sum()
 

#17 def calcuate(a,b,c=None,d=None):
#     if c is None and d is None:
#         print("mulitiplication",a*b)
#     elif c is not None and d is None:
#         print("additon",a+b+c)
#     elif c is not None and d is not None:
#         print("subtratcion",(a+b)-(c+d))


# calcuate(10,20)

# calcuate(10,20,30)
# calcuate(10,20,30,40)

# 18 unlimited argument  in add in the function
# def add(*args):
#     total=0
#     for i in args:
#         total=total+i
#     print(total)

# add(10,20,30)

# 19. Create a function which will take unlimited arguments both non keyword and
# keyword arguments. Add the values of all non keyword arguments and also the
# value of keyword arguments.

# def add(*args,**args2):#* is used non-key argument and ** is used of unliment keybord of used
#     total=0
#     for i in args:
#         total=total+i
#     print(total)
#     for value in args2:
#         total += value
# add(10,20,30)

# 20.Write a function with recursion to give the power of a number. It will be having
# two parameters no and power. If no power is passed it should take 0.

# def power(no, exp=0):
#     if exp==0:
#         return 1
#     return no * power(no , exp- 1)


# print(power(4,5))

#21factorial number

# def factorial(n):
#     if n ==0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# num=int(input("enter the number"))
# print("factorial = ",factorial(num))

# 22
# def calculator(choice):
#     def addition(a,b,c):
#         print("addition",a+b+c)
#     def subtraction(a,b,c):
#         print("subtraction",a-b-c)
#     def multiplication(a,b,c):
#         print("mulitiplcation",a*b*c)
#     def division(a,b):
#         print("division",a/b)
#     def exponent(a,b):
#         print("exponent",a**b)
#     def floor_divison(a,b):
#         print("floor_division",a//b)
#     if choice==1:
#         a=int(input("enter the number:-"))
#         b=int(input("enter the number:-"))
#         c=int(input("enter the number:-"))
#         addition(a,b,c)
#     elif choice==2:
#         a=int(input("enter the number:-"))
#         b=int(input("enter the number:-"))
#         c=int(input("enter the number:-"))
#         subtraction(a,b,c)
#     elif choice==3:
#         a=int(input("enter the number:-"))
#         b=int(input("enter the number:-"))
#         c=int(input("enter the number:-"))
#         multiplication(a,b,c)
#     elif choice==4:
#         a=int(input("enter the number:-"))
#         b=int(input("enter the number:-"))
#         division(a,b)
#     elif choice==5:
#         a=int(input("enter the number:-"))
#         b=int(input("enter the number:-"))
#         exponent(a,b)
#     elif choice==6:
#         a=int(input("enter the number:-"))
#         b=int(input("enter the number:-"))
#         floor_divison(a,b)
# print('''
#     1.Addition
#     2.subtratction
#     3.mulitiplcation
#     4.division
#     5.exponent
#     6.floor_division
# ''')
# num=int(input("enter the chioce"))
# print("calcuate the number",calculator(num))

#23.one method calling to another method
# def calcuate():
#     x=int(input("enter the number:-"))
#     y=int(input("enter the number:-"))
#     sum(x,y)

# def sum(a,b):
#     print("addition",a+b)

# calcuate()

#24.
# def calculator(a,b,c=None,d=None,e=None):
#     if c is None and d is None and e is None:
#         print("mulitiplcation",a*b)
#     elif c is not None and d is None and e is None:
#         print("first element",a)
#         print("second element",b)
#         print("thrid element",c)
#     elif c is not None and d is not None and e is None:
#         print("addition",a+b+c+d)
#     elif c is not None and d is None and e is not None:
#         print("multiplication",(a*b)+(c*d*e))

# calculator(5,6)
# calculator(5,6,7)
# calculator(5,6,7,8)
# calculator(5,6,7,8,9)
#25.
# class calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         self.result=0

#     def calculate(self,n):
#         self.result= (self.a + self.b) * n

#     def display(self):
#         print("first number",self.a)
#         print("second number",self.b)
#         print("result",self.result)

# cal=calculator(10,20)
# cal.calculate(2)
# cal.display()
#26.
# class a:
#     def A(self):
#         print("these is a")
#     def B(self):
#         print("these of b")
# class b(a):
#     def c(self):
#         print("these of c")

# p=a()
# p.A()
# p.B()

# c=b()
# c.c()
# c.A()
# c.B()

#27.
# class calcuator:
#     def __init__(self):
#         print("the parent construction")
#     def method1(self):
#         print("method1")
#     def method2(self):
#         print("method2")
#     def __del__(self):
#         print("destroction")
    
# class b(calcuator):
#     def __init__(self):
#         super().__init__()
#         print("child construction")
#     def method3(self):
#         print("method1")
#     def method4(self):
#         print("method2")
#     def __del__(self):
#         print("destroction")
# cal=calcuator()
# cal.method1()

# B=b()
# B.method4()

#28.
# class partent:
#     def show(self):

#         print("partent class method")
# class child :
#     def show(self):
#         print("child class")

# c=child()
# c.show()
#29.

# class Parent:
#     def display(self):
#         print("This is Parent Display Method")

# class Child(Parent):
#     def display(self):
#         super().display()     # Calls Parent method
#         print("This is Child Display Method")

# c = Child()
# c.display()

#
#3
# class A:
#     def a(self):
#         print("a class method")
# class B(A):
#     def b(self):
#         print("b is class")
# class C(B):
#     def c(self):
#         print("c is class")

# d=C()
# d.c()
# d.b()
# d.a()


# class A:
#     def a(self):
#         print("a class method")
# class B:
#     def b(self):
#         print("b is class")
# class C(A,B):
#     def c(self):
#         print("c is class")

# d=C()
# d.c()
# d.b()
# d.a()
#30
# class calcuate:
#     def __init__(self,name=None,age=None):
#         if name is None and age is None:
#             print("Default Construction")
#         elif age is None:
#             print("Name",name)
#         else:
#             print("Name",name)
#             print("age",age)

# cal=calcuate()
# cal=calcuate("het")
# cal=calcuate("het",20)

#31.
# class my_parent_class:
#     x = 10
#     y = 5

    
#     def __init__(self, a=None, b=None):
#         if a is None:
#             self.a = self.x
#         else:
#             self.a = a

#         if b is None:
#             self.b = self.y
#         else:
#             self.b = b


#     def add(self, p=0, q=0):
#         self.res1 = self.a + self.b
#         self.print_result()

    
#     def sub(self, p=0, q=0):
#         self.res2 = self.a - self.b
#         self.print_result()


#     def print_result(self):
#         if hasattr(self, "res1"):
#             print("Addition =", self.res1)
#         if hasattr(self, "res2"):
#             print("Subtraction =", self.res2)



# class my_child_class(my_parent_class):

    
#     def __init__(self, a=None, b=None, z=2):
#         super().__init__(a, b)
#         self.z = z

    
#     def add(self, p=0, q=0):
#         super().add()      # Calls parent add()
#         print("Addition of x, y and z =", self.a + self.b + self.z)

    
#     def print_result(self):
#         print("Addition of x, y and z =", self.a + self.b + self.z)

#     def sub(self, p=0, q=0):
#         print("Multiplication =", self.a * self.b * self.z)

    
#     def __del__(self):
#         print("Destructor called for Child Object")



# print(" Parent Class Objects ")

# obj1 = my_parent_class()
# print("Object 1:")
# obj1.add()
# obj1.sub()

# print()

# obj2 = my_parent_class(20)
# print("Object 2:")
# obj2.add()
# obj2.sub()

# print()

# obj3 = my_parent_class(30, 15)
# print("Object 3:")
# obj3.add()
# obj3.sub()
# print("\n Child Class Object ")

# c1 = my_child_class(10, 5, 3)
# c1.add()
# c1.sub()


# print("\nManual Destructor Call")
# del c1

# print("Program End")
