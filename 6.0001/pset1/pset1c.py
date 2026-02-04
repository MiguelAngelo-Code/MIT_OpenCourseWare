# User Inputs
annual_salary = float(input("Annual Salary: "))


# Consts: Down payment & annual return
total_cost = 1000000
semie_annual_raise = 0.07
PDP = 0.25
ARR = 0.04
months_to_save = 36


# Down payment and epsilon
down_payment = total_cost * PDP
epsilon = 100

# set guess range
low = 0 
high = 1000

steps = 0
    
while True:
    current_savings = 0
    time_to_raise = 0   

    guess = (high + low)/2
    portion_saved = guess/1000

    steps += 1

    annual_salary_temp = annual_salary

    for months in range(36):
        current_savings += (current_savings * (ARR / 12))
        current_savings += ((annual_salary_temp / 12) * portion_saved)
            
        if (time_to_raise < 5):
            time_to_raise += 1
        else:
            annual_salary_temp += (annual_salary_temp * semie_annual_raise)
            time_to_raise = 0
    
    if (down_payment - current_savings) > 100: 
        low = guess
    elif (down_payment - current_savings) < -100:
        high = guess
    else:
        break

    if steps > 100:
        print("Not possible on this salary")
        break

print(portion_saved)
print(steps)


