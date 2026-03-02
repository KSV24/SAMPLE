#a=3
#b=2
#print(a,b)
#print(a+b)
#print(a*b)
#y=a**b
#z=a//b
#print(a,b,y,z)

#a=(3*2//3%2)*(5%11*5)
#print(a)

#a=(3*2//3%2)/(5%11*5)
#print(a)

#a=4
#b=5
#x=a&b
#print(x)

#x=a^b
#print(x)

#b=~b
#print(b)

#b=5
#b=b>>2
#print(b)

#for x in range(10):
 #   print(x,end=",") 

#for x in range(10,30,2):
#    print(x,end="|")

#string=" virat kohli "
#print(string.strip())
#for character in string:
    #print(character,end=",")

#for i in range(20):
#    if i==10:
#       continue
#   print(i,end=",")

#sum=0
#for i in range(1,20):
#    sum+=i
#    print("SUM:",sum)   
#else:
#    print("Loop terminated")

#i=0
#while(i<=10):
#    print(i)
#    i=i+1;

name="vishal is a baller"
#print(len(name))
#print(name.upper())
#print(name[2]) 

#print(name.count("a"))    
#print(name.replace("a","A"))
#reverse=name[::-1]
#print(reverse)


#numbers = [10, 20, 30, 40, 50]
#average = sum(numbers) / len(numbers)
#print("Average:", average)

#marks = [85, 90, 78, 92, 88]
#print("Maximum:", max(marks))
#print("Minimum:", min(marks))

#data = [1, 2, 2, 3, 4, 4, 5]
#unique_data = list(set(data))
#print("Without Duplicates:", unique_data)

#student = ("Vishal", 21, "Data Science")
#print("Name:", student[0])
#rint("Age:", student[1])

#numbers = (1, 2, 3, 2, 4, 2, 5)
#print("Count of 2:", numbers.count(2))

#A = {1, 2, 3}
#B = {3, 4, 5}
#print("Union:", A.union(B))

#student_marks = {
#    "Vishal": 85,
#   "Rahul": 90,
#    "Anu": 78
#}
#print("Vishal Marks:", student_marks["Vishal"])

import numpy as np
arr = np.array([10, 20, 30, 40])
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Multiply by 2:", arr * 2)