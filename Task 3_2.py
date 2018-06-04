two_digit_number = input('Enter two-digit number: ')
entered_number = input('Enter the number checker: ')
first_number = two_digit_number[0]
second_number = two_digit_number[1]
if first_number == entered_number or second_number == entered_number:
    print('Your number have ' + entered_number + ' in it')
else:
    print('Your number does not have ' + entered_number + ' in it')
