
# User Inputs
total_cost = float(input("Home Cost: "))
annual_salary = float(input("Annual Salary: "))
portion_saved = float(input("Portion of Salary to be Saved: "))

# Consts: Down payment & annual return
PDP = 0.25
ARR = 0.04

current_savings = 0.0
NumMonths = 0

while (current_savings < (total_cost * PDP)):

    current_savings += (current_savings * (ARR / 12))
    current_savings += ((annual_salary / 12) * portion_saved)
    
    NumMonths += 1

print(NumMonths)


