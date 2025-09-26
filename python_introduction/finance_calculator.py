monthly_income =int(input("enter your monthly income:"))
monthly_expenses =int(input("enter your monthly expenses:"))
monthly_savings =monthly_income-monthly_expenses
projected_savings =monthly_savings * 12 *0.05
print(f"your monthly_income is: {monthly_income}")
print(f"your monthly_expense is:{monthly_expenses}")
print(f"your monthly_savings is: {monthly_savings}")
print("projected savings after year with interest is: ", projected_savings)