import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y_orange = [12, 22, 33, 43, 54]
y_violet = [6, 17, 28, 39, 60]
plt.plot(x, y_orange, color='orange', marker='^', linestyle='-.', linewidth=2, label='orange Line')
plt.plot(x, y_violet, color='violet', marker='o', linestyle='--', linewidth=2, label='violet Line')
plt.title("Modified Sample Graph")
plt.xlabel("X Axis Values")
plt.ylabel("Y Axis Values")
plt.legend()
plt.grid(True)
plt.annotate("Peak Value",
             xy=(5,60),
             xytext=(3.5,30),
             arrowprops=dict(facecolor='blue', shrink=0.05))
plt.savefig("graph.png")

plt.show()