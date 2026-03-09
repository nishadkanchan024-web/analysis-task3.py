import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ultimate_student_productivity_dataset_5000.csv")

print(data.head())
print(data.info())
print(data.describe())
print(data.isnull().sum())
print(data.corr(numeric_only=True))
print(data.columns)
data['Study_Category'] = pd.cut(
    data['study_hours'],
    bins=[0,2,4,6,8,10,12],
    labels=['0-2','2-4','4-6','6-8','8-10','10-12']
)

#sactterchart

plt.scatter(data['study_hours'], data['productivity_score'])
plt.xlabel("Study Hours")
plt.ylabel("Productivity Score")
plt.title("Study Hours vs Productivity")
plt.show()

#bar chart

data["gender"].value_counts().plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()


#pie chart

study_count = data['Study_Category'].value_counts()

plt.figure()
study_count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Distribution of Students by Study Hours")
plt.ylabel("")
plt.show()

#line graph

avg_productivity = data.groupby('Study_Category')['productivity_score'].mean()

avg_productivity.plot(kind='bar')
plt.title("Average Productivity by Study Hours")
plt.xlabel("Study Hours Category")
plt.ylabel("Average Productivity Score")
plt.show()