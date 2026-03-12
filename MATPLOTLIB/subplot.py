import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,30,40,50]
students = ["Arun","Priya","Rahul","Sneha"]
marks = [85,90,78,88]
data = [50,55,60,65,70,75,80,85,90,95]
subjects = ["Math","Science","English","Computer"]
scores = [30,25,20,25]
plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
plt.scatter(x,y,color="blue")
plt.title("Scatter Plot")
plt.subplot(2,2,2)
plt.bar(students,marks,color="green")
plt.title("Bar Chart")
plt.subplot(2,2,3)
plt.hist(data,bins=5,color="orange",edgecolor="black")
plt.title("Histogram")
plt.subplot(2,2,4)
plt.pie(scores,labels=subjects,autopct="%1.1f%%")
plt.title("Pie Chart")
plt.tight_layout()
plt.show()