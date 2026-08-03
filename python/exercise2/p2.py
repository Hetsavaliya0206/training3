#list number of used and odd number list given
# l=[]

# for i in range(1,20,2):
#         l.append(i)
    
# print(l)

# l=[]

# for i in range(1,20,1):
#     if i%2==0:
#         l.append(i)
        
# print(l)

#Get a list of 1 to 8 and then 4 to 10. Get the common elements from both the list in a new list.
# item1=[1,2,3,4,5,6,7,8]
# item2=[4,5,6,7,8,9,10,]
# item3=[]

# for i in item1:
#     if i in item2:
#         item3.append(i)
# print(item3)


# Sort a shuffled list of 10 random numbers in descending order

# import random
# l=[20,55,33,66,99,55,88,30,9,2]
# random.shuffle(l)
# l.sort(reverse=True)
# print(l)

# x=(1,2,3,4,5), y=(4,5,6,7). Combine these two tuples in a single tuple ignoring the common elements

# x=(1,2,3,4,5)
# y=(4,5,6,7)

# z=tuple(set(x)^set(y))
# print(z)

#Define two sets and perform all the set operations and validation operations

# x={1,2,3,4,5}
# y={4,5,6,7,8,9,10}


# Union=x | y
# print("Union operation used:-",Union)

# intersection = x.intersection(y)
# print("intersection operation used:-",intersection)

# difference=x.difference(y)
# print("difference operation",difference)

# symmetricdifference=x.symmetric_difference(y)
# print("symmetric difference:-",symmetricdifference)

#  Generate a dictionary {1:1,2:1,3:1,4:1,...,10:1} in one line using dictionary's method.

# d={i:1 for i in range(1,11,1)}

# print(d)

#Print all the keys and values of a dictionary

# d={
#     'name':"het",
#     'age':20,
#     'education':'B.E Enginnering'
# }

# print(d)
# for a,b in d.items():
#     print(a,":",b)
# Two dictionaries {'a':1,'b':2,'c':3}, {'a':4,'d':5,'e':6}. Merge these two dictionaries.
# d1={
#     'a':1,
#     'b':2,
#     'c':'3'
# }

# d2={
#     'a':4,
#     'd':5,
#     'e':6
# }

# d1.update(d2)
# print(d1)

# How to check whether a key is existing in a dictionary or not

# user_input=input("enter the key in dictonrary:-")
# d1={
#     'a':1,
#     'b':2,
#     'c':'3'
# }

# if user_input in d1:
#     print("key is exisiting")
# else:
#     print("key is not exisiting")


# How can we have two variables refering to a single list, set and dictionary.
# l=[10,20,30]
# list=l
# list.append(40)

# print(list)

# s={1,2,3}
# set=s
# set.add(4)
# print(set)
# d={
#     'name':'het',
#     'age':20
# }
# dict=d
# dict["city"]="Rajkot"
# print(dict)



#case method of string
# s1="het"
# print(s1.upper())
# s2="HET"
# print(s2.lower())
# print(s1.replace("het","hetsavaliya"))
# print(s1.count("e"))
# print(s1.capitalize())
# print(s1.title())


#validation method
# s1=input("enter the number:-")

# if s1.isalpha():
#     print("string is only for the letters ")
# elif s1.isdigit():
#     print("string is only for digit")
# elif s1.isalnum():
#     print("string contain both is letter and number")
# else:
#     print("special character is not used in the string")

#14Create a text document using the justification methods.

#15 How to split a string with a substring?

# st="python is open source language and asily to used"
# print(st.split())

#16 . Take a multiline string and split each line of this string as an element of the list.
# str='''
# hello world
# python programing language
# welcome to coding
# '''

# print(str.splitlines())


# 17How to replace a string with a substring?
# s1="python is open source language"
# s=s1.replace("python","Java")
# print(s)

# 18How to join multiple strings with a substring?
# s1='''
# hello world 
# python programing language
# welcome to coding
# '''
# s2="-"

# result=s2.join(s1)
# print(result)

# 19 How to make partition of a string?

# s1="welcome to coding"

# x=s1.partition("el")
# print(x)

#20 How to find the no of occurences of a substring?
# str="hello world"
# str1="hello"
# s=str[0:3]
# print(s)

#21  How to find the no of occurences of a substring?

# str="hellohellohell0"
# sub="hell"
# c=str.count(sub)
# print(c)

#21Create a transaction no of 5 digits. Even though the given number is 15.
# num="123456789012345"
# tr=num[:5]
# print(tr)

#22. Convert all the data structures to other data structures
# l=[1,2,3,4,5]
# s=set(l)
# print("convert to the list following the set:-",s)

# t=tuple(l)
# print("convert to the list following the tuple:-",t)
# d=dict(enumerate(l))win
# print("convert to the list following the dictornary:-",d)

# st=str(l)
# print("convert to the list following the string:-",st)

# s={1,2,3,4,5}
# l=list(s)
# print("convert to the set following the list ",s)

# t=tuple(s)
# print("convert to the set following the tuple ",t)

# d=dict(enumerate(s))
# print("convert to the set following the dictornary ",d)

# st=str(s)
# print("converting the set following the string :-",st)
# t=(1,2,3,4,5)
# l=list(t)
# print("convert to the tuple following the list ",l)

# s=set(t)
# print("convert to the tuple following the set ",s)

# d=dict(enumerate(t))
# print("converting to tuple following the dict:- ",d)

# st=str(s)
# print("convert to the tuple following the string ",s)

# dict={
#     0:1,
#     1:2,
#     2:3,
#     3:4
# }
# l=list(dict)
# print("convert to the dict following the list ",l)

# s=set(dict)
# print("convert to the dict following the set ",s)

# t=tuple(dict)
# print("convert to the dict following the tuple ",t)

# st=str(dict)
# print("convert to the dict following the string",st)





# 23 Get the last element of the list, tuple and string.
# l=[1,2,3,4,5,6]
# print(l[5:])
# t=(2,3,4,5,6,7,8)
# print(t[5:])

# st="savaliyahet"
# print(st[10:])

#24 Get last 3 elements of the list, tuple and string.

# l=[1,2,3,4,5,6]
# print(l[3:])
# t=(2,3,4,5,6,7,8)
# print(t[3:])

# st="savaliyahet"
# print(st[7:])

#25  Get first 5 elements of list, tuple and string.


# l=[1,2,3,4,5,6]
# print(l[1:])
# t=(2,3,4,5,6,7,8)
# print(t[1:])

# st="savaliyahet"
# print(st[5:])

# 26. Get all the elements excluding first and last elements from list, tuple and string.

# l=[1,2,3,4,5,6]
# print(l[1:5])

# t=(2,3,4,5,6,7,8)
# print(t[1:7])

# st="savaliyahet"
# print(st[1:11])

#27. Get all the elements in a list using : operator.

# my_list=[1,2,3,4,5,6]
# list=my_list[:]
# print("original list",my_list)
# print("All element[:]:",list)

# # 28. Get last 5 elements from a list of 1 to 10 using negative indexing.
# l=[1,2,3,4,5,6,7,8,9,10]
# print(l[-5:])

# 29. Get 4 elements of the list excluding last 2 elements using negative indexing
# l=[1,2,3,4,5,6,7,8,9,10]
# print(l[-10:-5])


# 30. Convert a list of tuple to dictionary
# l=[1,2,3,4,5]
# t=tuple(l)
# print("converting the tuple",t)
# d=dict(enumerate(l))
# print("converting the dict",d)

# 31. Iterate through all the data structures.
# l=['apple','mango','grapes','orange']
# print("iterte")
# for item in l:
#     print(item)

# 32. Use the overloaded operators ‘+’ and ‘*’ with list, tuple and string.

# list1=[1,2,3,4,5]
# list2=[2,3,4,5]
# print(list1+list2)

# print(list2*2)


# tuple1=(1,2,3,4,5)
# tuple2=(2,3,4,5)
# print(tuple1+tuple2)

# print(tuple2*2)

# str="welcome to you"
# str2="Het"
# print(str+str2)

# print(str*2)

# 33. Use the in, not in, is and is not operators with data structures.
# list=["mango","orange","pinaple"]

# print("mango" in list)
# print("apple" not in list)
# print("apple" in list)

# list = [1,2,3,4,5]
# list1=[1,2,3,4,5]

# print(list is list1)
# print(list is not list1)

# 34. Create a dictionary as following. {'a':1, 'b':2, 'c':3, 'd':4, 'e':5....'y':25, 'z':26}

# dict={
#     'a':1,
#     'b':2,
#     'c':3,
#     'd':4,
#     'e':5,
#     'f':6,
#     'g':7,
#     'h':8,
#     'i':9,
#     'j':10,
#     'k':11,
#     'l':12,
#     'm':13,
#     'n':14,
#     'o':15,
#     'p':16,
#     'q':17,
#     'r':18,
#     's':19,
#     't':20,
#     'u':21,
#     'v':22,
#     'w':23,
#     'x':24,
#     'y':25,
#     'z':26

# }
# print(dict)


# 35. There are two lists [1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]. Get a third list from these two lists as [12,14,16,18,20,22,24,26,28,30]

# list1=[1,2,3,4,5,6,7,8,9,10]
# list2=[11,12,13,14,15,16,17,18,19,20]
# list=[]
# l=len(list1)
# for i in range(l):
#     list.append(list1[i]+list2[i])

# print(list)

# 36. Get Square of all the elments in a list from 1 to 10 numbers

# list1=[1,2,3,4,5,6,7,8,9,10,11]
# list2=[]
# l=len(list1)
# for i in range(l):
#     list2.append(i**2)

# print(list2)

# 37. There are two lists [1,2,3,4,5], [4,5,6,7] get a list from these two lists [1,2,3,6,7].

# list1=[1,2,3,4,5]
# list2=[4,5,6,7]
# list3=[x for x in list1  if x  not in list2] + [x for x in list2 if x  not in list1]


# print(list3)

# 38. Fetch the data from the following.
# 1. Fetch 5 which is the value of ‘e’ from below which is marked in red.
# x = {
#     'a':1,
#     'b':2,
#     'c':3,
#     'd':[1,2,3,4,(5,6,7,{'e':5},10,15)],
#     'f':45
# }
# print(x['d'][4][3])
# x = {
#     'a': {
#         'b': [1, 2, (3, 4, {'c': 3, 'd': 4, 'e': [1, 2, 3]})],
#     },
#     'x': [1, 2, 3, 4]
# }

# print(x['a']['b'][2][2]['e'][1])

# x=[1 ,2 ,(3, 4, 5, {'a':1, 'b':[2,3,4,(5,6)]})]

# print(x[2][3]['b'][3][1])

# x={
#     True:[1, 2, 3, {'a':1, 'b':2}],
#     False:[(2 ,3 ,4 ,5 ,{1:2})]
# }
# print(x[False][0][4][1])

# x={
#     1:2,
#     2:3,
#     3:4,
#     4:{'a':'b',
#        'c':'d',
#        'e':'f',
#        'f':[1,2,3,{1:9,3:8}]
#        }

# }

# print(x[4]['f'][3][1])

# 39. Create a function for string that will check whether a string is having the first letter as Capital and not anyother letter is capital.


# def check(s):
#     if s[0].isupper() and s[1:].islower():
#         print("Valid String")
#     else:
#         print("Invalid String")

# name = input("Enter a string: ")
# check(name)


# checkstring("HET")
# checkstring("het")

# 40. Format a string with inputs passed using the index and keyword techniques.

# first="Hello {1}, you have any message passed {0}".format("alice",5)

# information="hii my name is {0},my age is {1}".format("het",20)
# print(first)
# print(information)

class Student:

    def __init__(self,name,regno,rollno,std,year):

        self.marks=[]
        self.result=False

        if name.isalpha():
            self.name=name

        if regno.isalnum():
            self.regno=regno

        if rollno.isdigit():
            self.rollno=rollno

        if std.isdigit():
            self.standard=std

        if year.isdigit():
            self.admission_year=year

    def add_marks(self,d):

        result="PASS"

        for sub,mark in d.items():

            if mark>100:
                print("Invalid Marks")
                return

            if mark<40:
                result="FAIL"

        d["Result"]=result

        self.marks.append(d)

    def generate_result(self):

        total=0
        passing=0
        obtained=0
        final="PASS"

        print("*"*60)
        print("Name :",self.name)
        print("Roll No :",self.rollno)
        print("Standard :",self.standard)
        print("*"*60)

        print("{:<15}{:<15}{:<15}{:<15}".format(
        "Subject","Total","Passing","Obtained"))

        for d in self.marks:

            for k,v in d.items():

                if k!="Result":

                    print("{:<15}{:<15}{:<15}{:<15}".format(
                    k,100,40,v))

                    total+=100
                    passing+=40
                    obtained+=v

            if d["Result"]=="FAIL":
                final="FAIL"

        print("*"*60)
        print("Total :",total)
        print("Passing :",passing)
        print("Obtained :",obtained)
        print("Percentage :",obtained/total*100)
        print("Result :",final)


s=Student("Het","GTU123","101","4","2026")

s.add_marks({
"Python":80,
"Java":70,
"C":35
})

s.generate_result()