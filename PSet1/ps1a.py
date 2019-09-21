annual_salary = float(input('Your salary: '))
portion_saved = float(input('How many % you want to save: '))/100
total_cost = float(input('How much!: '))
portion_down_payment = 0.25 * total_cost
current_saving = 0
month_to_save = 0
r = 0.04
while int(portion_down_payment) >= int(current_saving):
    current_saving += current_saving*r/12
    current_saving += annual_salary*portion_saved/12
    month_to_save += 1
print('You need', month_to_save, 'month to pay your down')