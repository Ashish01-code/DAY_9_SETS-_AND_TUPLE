#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Create a set and add n elements from user input.
s=set()
num=int(input("ENTER THE LIMIT OF NUMBER"))
for i in range(num):
        value=int(input())
        s.add(value)
print("SET",s)


# In[15]:


#Remove an element given by the user (handle if not present).
s=set()
num=int(input("ENTER THE LIMIT OF NUMBER"))
for i in range(num):
        value=int(input())
        s.add(value)
print(" ORIGINAL SET:",s)
find=int(input("ENTER THE VALUE OR NUMBER" ))
if find in s:
    s.discard(find)
    print("NEW SET:",s)
else:
    print("NO SUCH VALUE EXIST")


# In[14]:


#find length,max,min,sum of sets
s=set()
num=int(input("ENTER THE LIMIT OF NUMBER"))
for i in range(num):
        value=int(input())
        s.add(value)
print("LENGTH: ",len(s))
print("MAX: ",max(s))
print("MIN: ",min(s))
print("SUM: ",sum(s))


# In[28]:


#menu program explaining all operation
s = set()
ns = set()

while True:
    print("\n------ SET OPERATIONS MENU ------")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference (s - ns)")
    print("4. Symmetric Difference")
    print("5. Exit")
    print("6. Add elements to Set s")
    print("7. Add elements to Set ns")

    choice = int(input("ENTER YOUR CHOICE (1-7): "))

    if choice == 1:
        print("UNION:", s | ns)

    elif choice == 2:
        print("INTERSECTION:", s & ns)

    elif choice == 3:
        print("DIFFERENCE (s - ns):", s - ns)

    elif choice == 4:
        print("SYMMETRIC DIFFERENCE:", s ^ ns)

    elif choice == 5:
        print("Exiting program...")
        break

    elif choice == 6:
        num = int(input("ENTER NUMBER OF ELEMENTS FOR SET s: "))
        for i in range(num):
            value = int(input("Enter value: "))
            s.add(value)
        print("Set s:", s)

    elif choice == 7:
        num = int(input("ENTER NUMBER OF ELEMENTS FOR SET ns: "))
        for i in range(num):
            value = int(input("Enter value: "))
            ns.add(value)
        print("Set ns:", ns)

    else:
        print("PLEASE ENTER A VALID CHOICE BETWEEN 1 TO 7")


# In[34]:


#Remove duplicate elements from a list using a set.
list=[]
num = int(input("ENTER NUMBER OF ELEMENTS FOR LIST : "))
print("ENTER THE ELEMENTS")
for i in range(num):
    list.append(int(input()))
print("LIST IS:",list) 
y=set(list)
print("SET IS :",y)


# In[45]:


# menu program explaining all operation
tup=[]
while True:
    print("\n......TUPLE MENU...,.")
    print("1.  ADD ELEMENTS")
    print("2.  LENGTH")
    print("3.  MAXIMUM")
    print("4.  MINIMUM")
    print("5.  SUM")
    print("6.  COUNT THE ENTERED NUMBER")
    print("7.  SEARCH AN ELEMENT")
    print("8.  CONVERSION AND PRINT LIST AND TUPLE")
    print("9.  EXIT THE LOOP")
    choice=int(input("\nCHOOSE AN OPERATION 1-8: "))
    if choice==1:
        num=int(input("ENTER THE LIMIT OF TUPLE: "))
        print("ENTER THE ELEMENTS")
        for i in range(num):
             tup.append(int(input()))
        y=tuple(tup)
        print("TUPLE:",y)
    elif choice==2:
        print("LENGTH :",len(tup))
    elif choice==3:
        if len(tup)>0:
            print("MAXIMUM: ",max(tup))
        else:
            print("PLEASE ADD ELEMENTS FIRST")
    elif choice==4:
        if len(tup)>0:
            print("MINIMUM: ",min(tup))
        else:
            print("PLEASE ADD ELEMENTS FIRST")
    elif choice==5:
        print("SUM OF ELEMENTS: ",sum(tup))
    elif choice==6:
        value=int(input("ENTER THE NUMBER"))
        if value in tup:
            print("THE COUNT IS: ",tup.count(value))
        else:
            print("NUMBER NOT IN THE TUPLE")
    elif choice==7:
        if len(tup)>0:
            value=int(input("ENTER AN ELEMENTS"))
            if value in tup:
                print("THE INDEX OF",value, "IS",tup.index(value))
            else:
                print("NUMBER NOT PRESENT")
    elif choice==8:
        print("THE LIST: ",tup)
        print("THE TUPLE: ",tuple(tup))
    elif choice==9:
        print("Exiting.....")
        break
    else:
        print("PLEASE ENTER BETWEEN 1 TO 9")








# In[ ]:






