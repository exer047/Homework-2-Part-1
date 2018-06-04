first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
number_list = [first_number, second_number, third_number]
min_number = number_list[0]
for i in range(3):
    if number_list[i] < min_number:
        mmin_number = number_list[i]
print("max: ", min_number)
