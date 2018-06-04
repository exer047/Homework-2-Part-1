first_triangle_side = int(input('Enter first triangle side: '))
second_triangle_side = int(input('Enter second triangle side: '))
third_triangle_side = int(input('Enter third triangle side: '))
if first_triangle_side == second_triangle_side or first_triangle_side == third_triangle_side or \
        second_triangle_side == third_triangle_side:
    print('Your triangle is equilateral!')
else:
    print('Your  triangle is not equilateral!')
