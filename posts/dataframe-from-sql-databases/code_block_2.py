sales_employees = df[df["department"] == "Sales"]
print("\nSales Employees:\n", sales_employees)

average_salary = df["salary"].mean()
print("\nAverage Salary:", average_salary)

average_salary_by_department = df.groupby("department")["salary"].mean()
print("\nAverage Salary by Department:\n", average_salary_by_department)
