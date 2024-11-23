##                                  HOMEWORK 1






import pandas as pd
import matplotlib.pyplot as plt




data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}
df2 = pd.DataFrame(data2)








##1




total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Total sales for each product:")
print(total_sales)






##2





df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
highest_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
print("\nDate with the highest total sales:")
print(highest_sales_date)





##3







percentage_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
print("\nPercentage change in sales for each product:")
print(percentage_change)





##4





plt.figure(figsize=(10, 6))
plt.plot(df2['Date'], df2['Product_A'], label='Product_A')
plt.plot(df2['Date'], df2['Product_B'], label='Product_B')
plt.plot(df2['Date'], df2['Product_C'], label='Product_C')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trends for Each Product')
plt.legend()
plt.grid(True)
plt.show()







##                              HOMEWORK 2






import pandas as pd
import matplotlib.pyplot as plt




data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)







##1


average_salary = df3.groupby('Department')['Salary'].mean()
print("Average salary for each department:")
print(average_salary)







##2


most_experienced_employee = df3.loc[df3['Experience (Years)'].idxmax()]
print("\nEmployee with the most experience:")
print(most_experienced_employee)






##3


min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100
print("\nSalary data with percentage increase:")
print(df3[['Name', 'Salary', 'Salary Increase']])







##4


employee_distribution = df3['Department'].value_counts()
plt.figure(figsize=(8, 6))
employee_distribution.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()











##                                      HOMEWORK 3







import pandas as pd
import matplotlib.pyplot as plt




data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}



df4 = pd.DataFrame(data4)






##1


total_revenue = df4['Total_Price'].sum()
print("Total revenue from all orders:", total_revenue)







##2


most_ordered_product = df4.groupby('Product')['Quantity'].sum().idxmax()
print("Most ordered product:", most_ordered_product)






##3


average_quantity = df4['Quantity'].mean()
print("Average quantity of products ordered:", average_quantity)







##4


sales_distribution = df4.groupby('Product')['Total_Price'].sum()
plt.figure(figsize=(8, 6))
sales_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'salmon'])
plt.title('Sales Distribution Across Products')
plt.ylabel('')  
plt.show()
