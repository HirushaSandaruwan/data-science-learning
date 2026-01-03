import pandas as pd

#Exercise 1
#Creating a dataFrame
data = {
    "Name" : ["John", "Will", "Ron", "Joey"],
    "Age" : [23,25,28,23],
    "Salary" : [40000,58000,60000,55000]
}

df1 = pd.DataFrame(data)
print(df1)

print(df1.head(3)) #print first 3 rows
print(df1.info()) #get data types
print(df1.describe()) #get summary statistics
print(df1.columns) #get columns
print(df1.index) #get index

#Exercise 2
data = pd.read_csv("employee.csv")
print(data) #print csv data

print(data.loc[0:5,['Name', 'Salary']]) #select rows using loc
print(data.iloc[:, [1,4]]) #use iloc to select data
print(data[data["Salary"] > 50000]) #boolean filtering

#Exercise 3
product = pd.read_csv("product.csv")
print(product)

#filling missing values
print( product["Price"].fillna(product["Price"].mean()))
print( product["Stock"].fillna(0))
print( product["Color"].fillna("Unknown"))

#drop null values
print(product.dropna(axis=1)) #drop columns
print( product.dropna(axis=0)) #drop rows

#replace values
print(product.replace("Blue", "White"))

#Exercise 4
sales = pd.read_csv("sales.csv")
print(sales)

#Group by Department
print(sales.groupby(["Department"]).agg({'Sales': ['sum', 'mean', 'count']}))
#Sort values
print(sales.sort_values("Sales", ascending=False))

#Exercise 5
employees = pd.read_csv("employees.csv")
salaries = pd.read_csv("salaries.csv")
print(salaries)
print(employees)

print(pd.merge(employees, salaries, on="EmployeeID", how= 'left')) #left join
print(pd.merge(employees, salaries, on="EmployeeID", how= 'inner')) #inner join
print(pd.merge(employees, salaries, on="EmployeeID", how= 'right')) #right join
print(pd.merge(employees, salaries, on="EmployeeID", how= 'outer')) #outer join






