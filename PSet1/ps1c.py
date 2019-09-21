annual_salary = float(input('Enter the starting salary: '))

semi_annual_raise = 0.07
annual_investment_rate = 0.04
total_cost = 1000000
portion_down_payment = 0.25 * total_cost
current_saving = 0
month_to_save_goal = 36
month_saving = 0
r = 0.04
bisection_steps = 0
space_max = 10000
space_min = 0
portion_saved = int(space_max / 2)

def check_rate(annual_salary_int, portion_saved_test):
    current_saving_int = 0
    month_to_save = 0
    portion_saved_test_int = portion_saved_test / 10000.0
    for month in range(month_to_save_goal):
        if month_to_save > 0 and month_to_save % 6 == 0:
            annual_salary_int += annual_salary_int * semi_annual_raise
        current_saving_int += current_saving_int * r / 12
        current_saving_int += annual_salary_int * portion_saved_test_int / 12
        month_to_save += 1
    return current_saving_int


if check_rate(annual_salary, space_max) < portion_down_payment:
    print('It is not possible to pay the down payment in three years.')
else:
    while True:
        bisection_steps += 1
        current_saving = int(check_rate(annual_salary, portion_saved))
        if current_saving > int(portion_down_payment + 100):
            space_max = portion_saved
        elif current_saving < int(portion_down_payment - 100):
            space_min = portion_saved
        else:
            break
        portion_saved = int(space_min + (space_max - space_min) / 2)
    print('Best saving rate:', portion_saved/10000)
    print('Steps in bisection search:', bisection_steps)
