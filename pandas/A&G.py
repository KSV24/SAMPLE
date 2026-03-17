import pandas as pd

dataset = pd.read_csv(r"C:\Users\Vishal KS\OneDrive\Desktop\New folder\pandas\data.csv")
#print(dataset)
#print(dataset.columns)

#avgscore = dataset.groupby("gender")[["math score","reading score","writing score"]].mean()
#print(avgscore)


#group_data = dataset.groupby("lunch")[["math score","reading score","writing score"]].mean()
#print(group_data)

#s_count = dataset.groupby("gender").size()
#print(s_count)

#max_score = dataset.groupby("gender")[["math score","writing score"]].max()
#print(max_score)

#min_score = dataset.groupby("gender")[["math score","writing score"]].min()
#print(min_score)

#mul_grpby = dataset.groupby(["gender","lunch"])[["math score","reading score","writing score"]].mean()
#print(mul_grpby)

#agg = dataset.groupby("gender").agg({
#    "math score":"mean",
#    "reading score":"max",
#    "writing score":"min"
#})
#print(agg)

scholarship = {
    "gender": ["female","male"],
    "scholarship": [5000,4000] }
#scholarship_dataframe = pd.DataFrame(scholarship)
#print(scholarship_dataframe)

#merged_dataframe = pd.merge(dataset, scholarship_dataframe, on="gender")
#print(merged_dataframe)

#concatenation_dataframe = pd.concat([dataset,scholarship_dataframe])
#print(concatenation_dataframe)

print(dataset[["math score","reading score","writing score"]].corr())