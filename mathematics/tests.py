from django.test import TestCase


# Create your tests here.
# import random
#
#
# def linear_function_practice(request):
#     from random import randint
#     while True:
#         a = randint(-10, 10)
#         b = randint(-20, 20)
#         x = randint(-20, 20)
#         if a != 0 and b != 0:
#             break
#
#     print(a, 'and', b)
#     if a == 1:
#
#         if b >= 0:
#             expression = f'Find the value of x + {b} when x = {x}'
#             answer = a*x + b
#             return expression, answer
#         else:
#             result = ''
#             cycle = 0
#             for i in str(b):
#                 if cycle == 1:
#                     result += ' '
#                 result += str(i)
#                 cycle += 1
#             expression = f'Find the value of -x {result} when x = {x}'
#             answer = a*x + b
#             return expression, answer
#
#     elif a == -1:
#
#         if b >= 0:
#             expression = f'Find the value of -x + {b} when x = {x}'
#             answer = a*x + b
#             return expression, answer
#
#         else:
#             result = ''
#             cycle = 0
#             for i in str(b):
#                 if cycle == 1:
#                     result += ' '
#                 result += str(i)
#                 cycle += 1
#             expression = f'Find the value of -x {result} when x = {x}'
#             answer = a*x + b
#             return expression, answer
#
#     else:
#
#         if b >= 0:
#             expression = f'Find the value of {a}x + {b} when x = {x}'
#             answer = a*x + b
#             return expression, answer
#
#         else:
#             result = ''
#             cycle = 0
#             for i in str(b):
#                 if cycle == 1:
#                     result += ' '
#                 result += str(i)
#                 cycle += 1
#             expression = f'Find the value of {a}x {result} when x = {x}'
#             answer = a*x + b
#             return expression, answer
#
#
# print(linear_function_practice('a'))
#
#
# from random import randint
#
# def linear_function_practice():
#     while True:
#         a = randint(-10, 10)
#         b = randint(-20, 20)
#         x = randint(-20, 20)
#         if a != 0 and b != 0:
#             break
#
#     answer = a * x + b
#     b_str = str(b).replace("-", "- ")
#
#     if a == 1:
#         expression = f"Find the value of x {('+ ' + str(b)) if b >= 0 else b_str} when x = {x}"
#     elif a == -1:
#         expression = f"Find the value of -x {('+ ' + str(b)) if b >= 0 else b_str} when x = {x}"
#     else:
#         expression = f"Find the value of {a}x {('+ ' + str(b)) if b >= 0 else b_str} when x = {x}"
#
#     return expression, answer
#
# print(linear_function_practice())
# from random import randint
# from fractions import Fraction
#
#
# def linear_system_practice():
#     while True:
#         a1 = randint(-5, 5)
#         b1 = randint(-10, 10)
#         a2 = randint(-5, 5)
#         b2 = randint(-10, 10)
#
#         # parallel emas, nollar emas bo‘lsin
#         if a1 != a2 and a1 != 0 and a2 != 0:
#             break
#
#     # Kesishish nuqtasini topamiz
#     # a1*x + b1 = a2*x + b2  =>  x = (b2 - b1)/(a1 - a2)
#     x_val = Fraction(b2 - b1, a1 - a2)
#     y_val = Fraction(a1 * x_val + b1)
#
#     # ifodalarni chiroyli qilish
#     def format_line(a, b):
#         b_str = str(b).replace("-", "- ")
#         if a == 1:
#             return f"y = x {('+ ' + str(b)) if b >= 0 else b_str}"
#         elif a == -1:
#             return f"y = -x {('+ ' + str(b)) if b >= 0 else b_str}"
#         else:
#             return f"y = {a}x {('+ ' + str(b)) if b >= 0 else b_str}"
#
#     expr1 = format_line(a1, b1)
#     expr2 = format_line(a2, b2)
#
#     question = f"Find the intersection point of {expr1} and {expr2}"
#     answer = f"({x_val}, {y_val})"
#
#     return question, answer
#
#
# print(linear_system_practice())
#
# from random import randint
# from fractions import Fraction
#
#
# def slope_from_points():
#     while True:
#         x1, y1 = randint(-10, 10), randint(-10, 10)
#         x2, y2 = randint(-10, 10), randint(-10, 10)
#         if x1 != x2:  # vertical chiziq bo‘lmasin
#             break
#
#     question = f"Find the slope of the line passing through points ({x1}, {y1}) and ({x2}, {y2})"
#     slope = Fraction(y2 - y1, x2 - x1)  # kasr ko‘rinishida chiqadi
#
#     return question, slope
#
#
# print(slope_from_points())


# import random
#
#
# def generate_quadratic(x):
#     a = random.randint(-5, 5)
#     while a == 0:
#         a = random.randint(-5, 5)
#     b = random.randint(-10, 10)
#     c = random.randint(-10, 10)
#     b_str = str(b)
#     c_str = str(c)
#     if b < 0:
#         b_str = b_str.replace('-', '- ')
#     if c < 0:
#         c_str = c_str.replace('-', '- ')
#     result = f'{a}x² + {b_str}x + {c_str}'
#     edited1 = result.replace('+ -', '-')
#     edited2 = edited1.replace('-1x²', '-x²')
#     edited3 = edited2.replace('1x²', 'x²')
#     edited4 = edited3.replace('1x', 'x')
#     edited5 = edited4.replace(' + 0x', '')
#     function = edited5.replace(' + 0', '')
#     question = f'What is the value of the function of f(x) = {function}, when the value of x = {x}'
#     return question, a * x ** 2 + b * x + c
#
#
# def x_intersection_of_quadratic_function():
#     a = random.randint(-10, 10)
#     b = random.randint(-10, 10)
#     print(a, b)
#     equation = f'x² + {(a + b) * (-1)}x + {a * b}'
#     function = equation.replace(' + -', ' - ')
#     question = f'Find the x-intercepts of the function 𝑓(𝑥) = {function}'
#     return question, f'{a} and {b}'
#
#
# import random
#
#
# def generate_integer_vertex_quadratic():
#     a = random.randint(-5, 5)
#     while a == 0:
#         a = random.randint(-5, 5)
#
#     h = random.randint(-10, 10)
#     k = random.randint(-15, 15)
#
#     b = -2 * a * h
#     c = a * (h ** 2) + k
#
#     if a == 1:
#         result = 'x²'
#     elif a == -1:
#         result = '-x²'
#     else:
#         result = f'{a}x²'
#
#     if b != 0:
#         if b == 1:
#             result += ' + x'
#         elif b == -1:
#             result += ' - x'
#         elif b > 0:
#             result += f' + {b}x'
#         else:  # b < 0
#             result += f' - {abs(b)}x'
#
#     if c != 0:
#         if c > 0:
#             result += f' + {c}'
#         else:  # c < 0
#             result += f' - {abs(c)}'
#
#     if result.startswith('-x²') or result.startswith('- '):
#         pass  # To'g'ri format
#     elif result.startswith('+ '):
#         result = result[2:]
#
#     return result, f'({h}, {k})'
#
#
#
#
# def generate_find_a_problem_single_answer():
#     a = random.randint(-4, 4)
#     while a == 0:
#         a = random.randint(-4, 4)
#
#     root = random.randint(-8, 8)
#
#     y_value = random.randint(-20, 20)
#
#     b = -a * (root + root)  # Ya'ni -2 * a * root
#     c = a * root * root + y_value  # Ya'ni a * root² + y_value
#
#     if a == 1:
#         func_str = 'x²'
#     elif a == -1:
#         func_str = '-x²'
#     else:
#         func_str = f'{a}x²'
#
#     if b != 0:
#         if b == 1:
#             func_str += ' + x'
#         elif b == -1:
#             func_str += ' - x'
#         elif b > 0:
#             func_str += f' + {b}x'
#         else:
#             func_str += f' - {abs(b)}x'
#
#     if c != 0:
#         if c > 0:
#             func_str += f' + {c}'
#         else:
#             func_str += f' - {abs(c)}'
#
#     if func_str.startswith(' + '):
#         func_str = func_str[3:]
#
#     question = f'The function is given as 𝑓(𝑥) = {func_str}. If 𝑓(𝑎)={y_value}, find the value of 𝑎'
#
#     return question, root


def return_lesson_name(word):
    data = {'Fundamental Concepts of Mathematics': 'fundamental',
            'Equalities and Inequalities': 'equalities_inequalities', 'Linear Equations': 'linear_equalities',
            'Types of Numbers': 'types_of_numbers',
            'Operations with Positive and Negative Numbers': 'working_with_signs',
            'Fractions and Rational Numbers': 'fractions', 'Quadratic Equations': 'quadratic_equations',
            'Inequalities': 'inequalities', 'Linear Functions': 'linear_functions',
            'Other Types of Functions': 'other_kind_of_functions', 'Introduction to Logarithms': 'logarithm',
            'Operations on Logarithms': 'operation_on_logarithm', 'Logarithmic Functions': 'logarithmic_functions',
            'Introduction to Trigonometry': 'trigonometry',
            'Trigonometric Identities and Operations': 'operations_in_trigonometry',
            'Inverse Trigonometric Functions': 'inverse_trigonometric_functions',
            'Introduction to Geometry': 'introduction_to_geometry',
            'Measurement and Distance': 'measurement_and_distance', 'Angles and Their Properties': 'angles',
            'Types of Triangles': 'triangle_types', 'Properties of Triangles': 'properties_of_triangles',
            'Quadrilaterals': 'quadrilaterals_and_squares', 'Types of Quadrilaterals': 'types_of_quadrilateral',
            'Basic Concepts of Circles': 'circle_basic', 'Properties of Circles': 'other_properties_of_circle',
            'Equation of a Circle': 'equation_of_circle', 'Coordinate Plane': 'plane',
            'Distance, Midpoint, and Slope Formulas': 'distance_midpoint_slope',
            'The Law of Sines': 'the_laws_of_sines', 'The Law of Cosines': 'the_laws_of_cosines',
            'Similar Triangles': 'similar_triangles'}
    return data.va


#
#
# def return_total_views(request):
#     from .models import TakenLessons
#     types = ['Fundamental Concepts of Mathematics', 'Equalities and Inequalities', 'Linear Equations',
#              'Types of Numbers', 'Operations with Positive and Negative Numbers', 'Fractions and Rational Numbers',
#              'Quadratic Equations', 'Inequalities', 'Linear Functions', 'Other Types of Functions',
#              'Introduction to Logarithms', 'Operations on Logarithms', 'Logarithmic Functions',
#              'Introduction to Trigonometry', 'Trigonometric Identities and Operations',
#              'Inverse Trigonometric Functions', 'Introduction to Geometry', 'Measurement and Distance',
#              'Angles and Their Properties', 'Types of Triangles', 'Properties of Triangles', 'Quadrilaterals',
#              'Types of Quadrilaterals', 'Basic Concepts of Circles', 'Properties of Circles', 'Equation of a Circle',
#              'Coordinate Plane', 'Distance, Midpoint, and Slope Formulas', 'The Law of Sines', 'The Law of Cosines',
#              'Similar Triangles']
#     all_data = {}
#     for i in types:
#         data = TakenLessons.objects.filter(lesson=i)
#         new_data = len(data)
#         x = return_lesson_name(i)
#         all_data[x] = new_data
#     return all_data


