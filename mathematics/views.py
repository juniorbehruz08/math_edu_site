from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate
import random


def main_view(request):
    try:
        data = Profile.objects.get(user=request.user)
    except:
        try:
            data1 = Profile.objects.create(user=request.user)
            data1.save()
        except:
            pass
    if request.user.is_authenticated:
        context = {
            'title': 'Home Page'
        }

        return render(request, 'home.html', context=context)
    else:
        return redirect('login')


def login_view(request):
    if request.method == 'POST':
        if request.POST['type'] == 'login':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user and user.is_active:
                    login(request, user)
                    return redirect('main_view')
                else:
                    return redirect('login')
            return redirect('login')
        else:
            form = RegistrationForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                return redirect('login')
    else:

        context = {
            'title': 'Login'
        }

        return render(request, "login_and_register.html", context)


def log_out(request):
    logout(request)
    return redirect('login')


def fundamental_knowledge(request):
    return render(request, 'fundamental_knowledge.html')


def profile(request):
    user = User.objects.get_by_natural_key(request.user.username)
    profile = Profile.objects.get(user=user)

    context = {
        'profile': profile,
        'user': user
    }

    return render(request, 'profile.html', context)


def equalities_inequalities(request):
    return render(request, 'equations_and_inequalities.html')


def practice_linear(request, back_url):
    print(back_url)
    return render(request, 'practice_linear.html', {'back_url': back_url})


def linear_equalities(request):
    return render(request, 'linear_equalities.html')


def types_of_numbers(request):
    return render(request, 'types_of_numbers.html')


def types_of_numbers_quiz(request):
    return render(request, 'number_types_quiz.html')


def working_with_signs(request):
    return render(request, 'signs.html')


def working_with_signs_practice(request):
    return render(request, 'working_with_signs_practice.html')


def fractions(request):
    return render(request, 'fractions.html')


def fractions_practice(request):
    return render(request, 'fractions_practice.html')


def quadratic_equations(request):
    return render(request, 'quadratic_equations.html')


def quadratic_practice(request, back_url):
    return render(request, 'quadratic_practice.html', {'back_url': back_url})


def inequalities(request):
    return render(request, 'inequalities.html')


def inequalities_practice(request, back_url):
    return render(request, 'inequalities_practice.html', {'back_url': back_url})


def linear_functions(request):
    from fractions import Fraction
    number = Fraction(5, 6)
    return render(request, 'linear_functions.html', {'number': number})


def practice_linear_functions(request):
    import json
    from random import randint, sample
    from fractions import Fraction
    questions = []

    for i in range(20):
        # 1–5: linear, 6–10: slope, 11–20: system
        if i < 5:
            # ---------- LINEAR FUNCTION ----------
            while True:
                a = randint(-10, 10)
                b = randint(-20, 20)
                x = randint(-20, 20)
                if a != 0 and b != 0:
                    break

            answer = a * x + b
            b_str = str(b).replace("-", "- ")

            if a == 1:
                q = f"Find the value of f(x) = x {('+ ' + str(b)) if b >= 0 else b_str} when x = {x}"
            elif a == -1:
                q = f"Find the value of f(x) = -x {('+ ' + str(b)) if b >= 0 else b_str} when x = {x}"
            else:
                q = f"Find the value of f(x) = {a}x {('+ ' + str(b)) if b >= 0 else b_str} when x = {x}"

            wrongs = set()
            while len(wrongs) < 3:
                w = answer + randint(-5, 5)
                if w != answer:
                    wrongs.add(w)

            options = list(wrongs) + [answer]
            questions.append({
                "type": "linear",
                "question": q,
                "answer": str(answer),
                "options": [str(o) for o in sample(options, len(options))]
            })

        elif i < 10:
            # ---------- SLOPE ----------
            while True:
                x1, y1 = randint(-10, 10), randint(-10, 10)
                x2, y2 = randint(-10, 10), randint(-10, 10)
                if x1 != x2:
                    break

            slope = Fraction(y2 - y1, x2 - x1)
            q = f"Find the slope of the line passing through points ({x1}, {y1}) and ({x2}, {y2})"

            wrongs = set()
            while len(wrongs) < 3:
                num = slope.numerator + randint(-3, 3)
                den = slope.denominator + randint(-3, 3)
                if den != 0 and Fraction(num, den) != slope:
                    wrongs.add(Fraction(num, den))

            options = list(wrongs) + [slope]
            questions.append({
                "type": "slope",
                "question": q,
                "answer": str(slope),
                "options": [str(o) for o in sample(options, len(options))]
            })

        else:
            # ---------- SYSTEM ----------
            while True:
                a1 = randint(-5, 5)
                b1 = randint(-10, 10)
                a2 = randint(-5, 5)
                b2 = randint(-10, 10)
                if a1 != a2 and a1 != 0 and a2 != 0:
                    break

            x_val = Fraction(b2 - b1, a1 - a2)
            y_val = Fraction(a1 * x_val + b1)

            def fmt(a, b):
                b_str = str(b).replace("-", "- ")
                if a == 1:
                    return f"y = x {('+ ' + str(b)) if b >= 0 else b_str}"
                elif a == -1:
                    return f"y = -x {('+ ' + str(b)) if b >= 0 else b_str}"
                else:
                    return f"y = {a}x {('+ ' + str(b)) if b >= 0 else b_str}"

            expr1, expr2 = fmt(a1, b1), fmt(a2, b2)
            q = f"Find the intersection point of {expr1} and {expr2}"
            answer = f"({x_val}, {y_val})"

            wrongs = set()
            while len(wrongs) < 3:
                wx = Fraction(randint(-5, 5), randint(1, 5))
                wy = Fraction(randint(-5, 5), randint(1, 5))
                w = f"({wx}, {wy})"
                if w != answer:
                    wrongs.add(w)

            options = list(wrongs) + [answer]
            questions.append({
                "question": q,
                "answer": answer,
                "options": sample(options, len(options))
            })

    data = json.dumps(questions, indent=1)
    return render(request, 'practice_linear_functions.html', {'data': data})


def other_kind_of_functions(request):
    return render(request, 'other_kind_of_functions.html')


# views.py

from .extrafunctions import generate_math_problems, generate_cubic_math_problems_en, \
    generate_rational_math_problems_fixed  # import faylning boshida


def practice_with_quadratic(request):
    data = generate_math_problems()
    return render(request, 'practice_functions.html', {'data': data})


def practice_with_cubic(request):
    data = generate_cubic_math_problems_en()
    return render(request, 'practice_functions.html', {'data': data})


def practice_with_rational(request):
    data = generate_rational_math_problems_fixed()
    return render(request, 'practice_rational_functions.html', {'data': data})


def practice_with_exponential(request):
    from .extrafunctions import generate_exponential_problems
    data = generate_exponential_problems()
    return render(request, 'practice_functions.html', {'data': data})


def logarithm(request):
    return render(request, 'logarithm.html')


def logarithm_practice(request):
    from .extrafunctions import logarithm_generator
    data = logarithm_generator()
    return render(request, 'logarithm_practice.html', {'data': data})


def operation_on_logarithm(request):
    return render(request, 'operations_on_logarithm.html')


def operations_on_logarithm_practice(request):
    from .extrafunctions import logarithm_generator_ops_v2
    data = logarithm_generator_ops_v2()
    return render(request, 'operations_on_logarithm_practice.html', {'data': data})


def logarithmic_functions(request):
    return render(request, 'logarithmic_functions.html')


def trigonometry(request):
    return render(request, 'trigonometry.html')


def operations_in_trigonometry(request):
    return render(request, 'operations_in_trigonometry.html')


def inverse_trigonometric_functions(request):
    return render(request, 'inverse_trigonometric_functions.html')


def test(request):
    return render(request, 'myfirstfrontend_code.html')


def introduction_to_geometry(request):
    return render(request, 'introduction_to_geometry.html')


def measurement_and_distance(request):
    return render(request, 'measurement_and_distance_in_plane.html')


def angles(request):
    return render(request, 'angles.html')


def triangle_types(request):
    return render(request, 'triangle_types.html')


def properties_of_triangles(request):
    return render(request, 'properties_of_triangles.html')


def quadrilaterals_and_squares(request):
    return render(request, 'quadrilaterals_and_squares.html')


def types_of_quadrilateral(request):
    return render(request, 'types_of_quadrilaterals.html')


def circle_basic(request):
    return render(request, 'circle_basic.html')


def other_properties_of_circle(request):
    return render(request, 'other_properties_of_circle.html')


def equation_of_circle(request):
    return render(request, 'formula_of_circle.html')


def plane(request):
    return render(request, 'plane.html')


def distance_midpoint_slope(request):
    return render(request, 'distance_midpoint_slope.html')


def the_laws_of_sines(request):
    return render(request, 'law_of_sines.html')


def the_laws_of_cosines(request):
    return render(request, 'law_of_cosines.html')


def practice_in_trigonometry(request):
    from .extrafunctions import angle_test_in_trigonometry
    data = angle_test_in_trigonometry()
    return render(request, 'practice_in_trigonometry.html', {'data': data})


def practice_in_inverse_trigonometry(request):
    from .extrafunctions import test_for_inverse_function
    data = test_for_inverse_function()
    return render(request, 'practice_in_inverse_trigonometry.html', {'data': data})


def practice_with_distance_and_midpoint(request):
    from .extrafunctions import midpoint_between_two_points, distance_between_two_points
    data = distance_between_two_points() + midpoint_between_two_points()
    return render(request, 'practice_with_distance_and_midpoint.html', {'data': data})


def practice_right_triangle(request):
    import random
    from .extrafunctions import right_triangle_area_perimeter, right_triangle_angles, pythagoras_find_hypotenuse
    data = right_triangle_angles() + right_triangle_area_perimeter() + pythagoras_find_hypotenuse()
    random.shuffle(data)
    return render(request, 'practice_right_triangle.html', {'data': data})


def practice_equilateral_triangle(request):
    from .extrafunctions import generate_equilateral_triangle_questions
    data = generate_equilateral_triangle_questions()
    random.shuffle(data)
    return render(request, 'practice_right_triangle.html', {'data': data})

