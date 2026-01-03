import pandas as pd

students = pd.read_csv("students.csv")
print(students)

#inspect
print(students.info())

#remove duplicate value
students = students.drop_duplicates()

#Handle missing values
students = students.dropna() #drop rows include Nan

#Add new columns
students['Total_score'] = students['Math'] + students['Science'] + students['English']

# Create a new column "Grade" by categorizing "Total_score" values into ranges:
# 0–150 -> Low, 150–225 -> Medium, 225–300 -> High
students['Grade'] = pd.cut(students['Total_score'],bins=[0,150,225,300],labels=['Low','Medium','High'])

#analysis
#find mean score of three subject
print(students[['Math','Science','English']].mean())

#groupby analysis
print(students.groupby(['Gender'])['Total_score'].mean())
print(students.groupby(['Gender'])['Total_score'].sum())
print(students.groupby(['Gender'])['Total_score'].max())

#Top 5 students
print(students.sort_values('Total_score', ascending=False).head())

#save cleaned version
students.to_csv("cleaned_student.csv", index=False)






