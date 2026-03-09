import pandas as pd
import numpy as np
#ds=pd.read_csv(r"C:\Users\Vishal KS\OneDrive\Desktop\New folder\pandas\data.csv")
#print(ds.isnull())
#print(ds.isnull().sum())



data = {
    "Name": ["Arun", "Priya", "Rahul", "Sneha", "Kiran", None],
    "Math": [85, 90, None, 70, 88, 95],
    "Science": [78, None, 85, 80, 90, 87],
    "English": [92, 88, 76, None, 85, 91],
    "Attendance": [90, 85, None, 88, 92, 95]
}

ds = pd.DataFrame(data)
#print(ds)




data = {
    "Name": ["Arun", "Priya", "Rahul", "Sneha", "Kiran", None],
    "Math": [85, 90, None, 70, 88, 95],
    "Science": [78, None, 85, 80, 90, 87],
    "English": [92, 88, 76, None, 85, 91],
    "Attendance": [90, 85, None, 88, 92, 95]
}

ds = pd.DataFrame(data)


#ds["Math"] = ds["Math"].fillna(ds["Math"].mean())
#print("Fill Math NaN with mean:\n", ds)


#ds = ds.fillna(0)
#print("\nFill remaining NaN with 0:\n", ds)


#ds = ds.rename(columns={"Math": "Math_Marks"})
#print("\nAfter renaming column:\n", ds)


ds = ds.drop_duplicates()
print("\nAfter removing duplicates:\n", ds)


#ds["Math_Marks"] = ds["Math_Marks"].astype(int)
#print("\nAfter converting to int:\n", ds)


#filtered = ds[ds["Math_Marks"] > 80]
#print("\nStudents with Math_Marks > 80:\n", filtered)