first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
divider_check = first_number % second_number
if divider_check == 0:
    print(int(first_number / second_number), 'Остача отсутсвует')
else:
    print('Второе число не является делителем первого!')
