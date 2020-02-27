def house_hunting():
    annual_salary = float(input('Please enter your salary: '))
    portion_saved_salary = float(input('How much can you saving every month :'))
    total_cost_house = float(input("What is the cost of your house: "))
    r = 0.04
    count_months = 0
    current_savings = 0
    portion_down_payment = total_cost_house * 0.25
    monthly_salary = annual_salary / 12
    while current_savings <= portion_down_payment:
        current_savings += monthly_salary * portion_saved_salary
        current_savings += current_savings * r / 12
        count_months += 1
    return count_months
print(house_hunting())
