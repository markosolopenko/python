def house_hunting():
    """
    TODO: FINISH THIS TASK!!!
    :return:
    """

    annual_salary = float(input('Please enter your salary: '))
    portion_saved_salary = float(input('How much can you saving every month :'))
    total_cost_house = float(input("What is the cost of your house: "))

    r = 0.04
    count_month = 0
    current_savings = 0
    portion_down_payment = total_cost_house * 25 / 100
    total_cost_house -= portion_down_payment
    monthly_salary = annual_salary / 12
    current_saving = monthly_salary * portion_saved_salary / 100
    saving_of_year = current_saving * 12

    while current_savings <= total_cost_house:
        current_savings += current_saving
        current_savings = saving_of_year * r / 12
        count_month += 1
    return count_month


if __name__ == "__main__":
    print(house_hunting())
