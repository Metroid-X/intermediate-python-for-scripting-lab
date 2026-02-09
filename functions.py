import math

def validate_age(age):
    result = None
    if age <= 0:
        result = ValueError
        # If 'age' is not a positive integer, this will throw a ValueError.
    else:
        result = f"Age: {age}"
    return result


print(validate_age(11))

PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

def calculate_rectangle_area(len, wid):
    return f"Area is {len*wid} square units."

def calculate_circle_area(rad):
    return f"Area is ≈{PI*(rad^2)} square units."

def get_area(shape, *args):
    if shape.lower() == "rectangle":
        return calculate_rectangle_area(args[0], args[1])
    elif shape.lower() == "circle":
        return calculate_circle_area(args[0])
    else:
        return ValueError


print(get_area("circle",6))