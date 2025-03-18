# import math
# def quadratic():
#     a = int(input("a="))
#     b = int(input("b="))
#     c = int(input("c="))
#     d = (b*b)-(4*a*c)
#     if(d<0):
#         print("roots are imaginary")
#     else:
#         x1 = (-b+math.sqrt(d))/(2*a)
#         x2 = (-b-math.sqrt(d))/(2*a)
#         print(x1,x2)
#     print("roots are real")
#     quadratic    


import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c  # D = b² - 4ac

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Real and Distinct Roots: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"Real and Equal Roots: {root}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        return f"Complex Roots: {real_part} ± {imaginary_part}i"

# উদাহরণ হিসেবে a = 1, b = -3, c = 2 দিলে:
print(solve_quadratic(1, -3, 2))  # আউটপুট হবে: Real and Distinct Roots: 2.0, 1.0
