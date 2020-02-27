def house_hunting():
    annual_salary = float(input('Enter your starting annual salary: '))
    portion_saved_salary = float(input('Enter the percent of your salary to save, as a decimal: '))
    total_cost_house = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
    r = 0.04
    semi = 6
    count_months = 0
    current_savings = 0
    portion_down_payment = total_cost_house * 0.25
    monthly_salary = annual_salary / 12
    while current_savings <= portion_down_payment:
        current_savings += monthly_salary * portion_saved_salary
        current_savings += current_savings * r / 12
        if count_months == semi:
            monthly_salary += monthly_salary * semi_annual_raise
            semi += 6
        count_months += 1
    return count_months
print(house_hunting())
