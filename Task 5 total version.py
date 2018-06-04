first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
number_list = [first_number, second_number, third_number]
max = number_list[1]
for i in range(3):
    if number_list[i] > max:
        max = number_list[i]
print("Maximum number is: ", max)

min = max

for i in range(3):
    if number_list[i] < min:
        min = number_list[i]
print("Minimal number is: ", min)

for i in range(3):
    if number_list[i] != min and number_list[i] != max:
        avr = number_list[i]
print("Average number is: ", avr)
