
monthly_income = input("Enter your monthly income:") 
monthly_expenses =input("Enter your monthly expenses:")
monthly_savings = monthly_income - monthly_expenses

print("Your monthly savings are $"+str(monthly_savings))

savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Projected savings after one year, with interest, is:" + str(savings) )
