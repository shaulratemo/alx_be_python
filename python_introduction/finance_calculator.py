monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses

print("Your monthly savings are $", monthly_savings)
annual_interest = 0.05
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * annual_interest)

print("Projected savings after one year, with interest, is: $", projected_annual_savings)