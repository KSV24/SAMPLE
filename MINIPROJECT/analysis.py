import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv(r"C:\Users\Vishal KS\OneDrive\Desktop\New folder\MINI PROJECT\hospital_readmission_dataset.csv")
numeric_data = dataset.select_dtypes(include=[np.number])
mean_values = numeric_data.mean()
print("Mean values:")
print(mean_values)
cols = numeric_data.columns

plt.figure(figsize=(10,6))
plt.subplot(1,3,1)
plt.scatter(dataset[cols[0]], dataset[cols[1]])
plt.title("Scatter Plot")
plt.xlabel(cols[0])
plt.ylabel(cols[1])
plt.grid(True)

plt.subplot(1,3,2)
plt.hist(dataset[cols[0]], bins=10)
plt.title("Histogram")
plt.xlabel(cols[0])
plt.ylabel("Frequency")
plt.grid(True)

plt.subplot(1,3,3)
plt.bar(mean_values.index, mean_values.values)
plt.title("Mean Values")
plt.xlabel("Columns")
plt.ylabel("Mean")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("hospital_analysis_graph.png")
plt.show()