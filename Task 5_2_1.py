first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
if first_number < second_number and first_number < third_number:
    print("First number is the smallest!")
elif second_number < first_number and second_number < third_number:
    print("Second number is the smallest")
elif third_number < second_number and third_number < first_number:
    print("Third number is the smallest!")
