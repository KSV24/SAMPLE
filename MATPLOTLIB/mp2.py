#import matplotlib.pyplot as plt
#x = [1,2,3,4,5]
#y = [10,20,25,30,40]
#plt.scatter(x, y, color="blue")
#plt.title("Scatter Plot Example")
#plt.xlabel("X Values")
#plt.ylabel("Y Values")
#plt.savefig("scatter.png")
#plt.show()

#import matplotlib.pyplot as plt
#students = ["Arun","Priya","Rahul","Sneha"]
#marks = [85,90,78,88]
#plt.bar(students, marks, color="green")
#plt.title("Student Marks")
#plt.xlabel("Students")
#plt.ylabel("Marks")
#plt.savefig("bar.png")
#plt.show()

#import matplotlib.pyplot as plt
#marks = [50,35,60,25,70,15,80,41,90,88]
#plt.hist(marks, bins=5, color="orange", edgecolor="black")
#plt.title("Marks Distribution")
#plt.xlabel("Marks")
#plt.ylabel("Frequency")
#plt.savefig("histogram.png")
#plt.show()

import matplotlib.pyplot as plt
subjects = ["Math","Science","English","Computer"]
marks = [30,25,20,25]
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Subject Marks Percentage")
plt.savefig("piechart.png")
plt.show()

