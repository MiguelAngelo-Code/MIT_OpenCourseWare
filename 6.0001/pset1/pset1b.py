
# User Inputs
annual_salary = float(input("Annual Salary: "))
portion_saved = float(input("Portion of Salary to be Saved: "))
total_cost = float(input("Home Cost: "))
semie_annual_raise = float(input("Enter your semi annual raise, as a decimal: "))


# Consts: Down payment & annual return
PDP = 0.25
ARR = 0.04

current_savings = 0.0
NumMonths = 0
time_to_raise = 0

while (current_savings < (total_cost * PDP)):

    current_savings += (current_savings * (ARR / 12))
    current_savings += ((annual_salary / 12) * portion_saved)
    
    NumMonths += 1

    if (time_to_raise < 5):
        time_to_raise += 1
    else:
        annual_salary += (annual_salary * semie_annual_raise)
        time_to_raise = 0

print(NumMonths)

