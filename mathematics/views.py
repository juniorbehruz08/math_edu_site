from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page


def feedback(request):
    success = False

    if request.method == 'POST':
        message = request.POST.get('message', '').strip()
        sender_name = request.POST.get('sender_name', '').strip() or 'Anonymous'
        message_type = request.POST.get('message_type', 'recommendation')

        if message_type not in ('recommendation', 'problem'):
            message_type = 'recommendation'

        if message:
            Feedback.objects.create(
                sender_name=sender_name[:100],
                message_type=message_type,
                message=message,
            )
            success = True

    return render(request, 'feedback.html', {'success': success})


def return_lesson_name(url):
    topics = {
        "fundamental": "Fundamental Concepts of Mathematics",
        "equalities_inequalities": "Equalities and Inequalities",
        "linear_equalities": "Linear Equations",
        "types_of_numbers": "Types of Numbers",
        "working_with_signs": "Operations with Positive and Negative Numbers",
        "fractions": "Fractions and Rational Numbers",
        "quadratic_equations": "Quadratic Equations",
        "inequalities": "Inequalities",
        "linear_functions": "Linear Functions",
        "other_kind_of_functions": "Other Types of Functions",
        "logarithm": "Introduction to Logarithms",
        "operation_on_logarithm": "Operations on Logarithms",
        "logarithmic_functions": "Logarithmic Functions",
        "trigonometry": "Introduction to Trigonometry",
        "operations_in_trigonometry": "Trigonometric Identities and Operations",
        "inverse_trigonometric_functions": "Inverse Trigonometric Functions",
        "introduction_to_geometry": "Introduction to Geometry",
        "measurement_and_distance": "Measurement and Distance",
        "angles": "Angles and Their Properties",
        "triangle_types": "Types of Triangles",
        "properties_of_triangles": "Properties of Triangles",
        "quadrilaterals_and_squares": "Quadrilaterals",
        "types_of_quadrilateral": "Types of Quadrilaterals",
        "circle_basic": "Basic Concepts of Circles",
        "other_properties_of_circle": "Properties of Circles",
        "equation_of_circle": "Equation of a Circle",
        "plane": "Coordinate Plane",
        "distance_midpoint_slope": "Distance, Midpoint, and Slope Formulas",
        "the_laws_of_sines": "The Law of Sines",
        "the_laws_of_cosines": "The Law of Cosines",
        "similar_triangles": 'Similar Triangles'
    }
    return topics[url]


def save_taken_lessons(url, request):
    from .models import TakenLessons
    TakenLessons.objects.create(lesson=return_lesson_name(url), user=request.user)


@login_required
@cache_page(60 * 10)
def main_view(request):
    if request.user.is_authenticated:
        context = {
            'title': 'Home Page'
        }

        return render(request, 'home.html', context=context)
    else:
        return redirect('login')


def login_view(request):
    if request.method == 'POST':

        if request.POST.get('type') == 'login':
            form = LoginForm(data=request.POST)

            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user and user.is_active:
                    login(request, user)
                    return redirect('main_view')

            return redirect('login')

        else:
            form = RegistrationForm(data=request.POST)

            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('main_view')

            return redirect('login')

    return render(request, "login_and_register.html", {'title': 'Login'})


def log_out(request):
    logout(request)
    return redirect('login')


@login_required
def fundamental_knowledge(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'fundamental_knowledge.html')


@login_required
def profile(request):
    from .extrafunctions import countries_flags
    scores = MathTestResult.objects.filter(user=request.user).order_by('-created_at')[:20]
    lessons = TakenLessons.objects.filter(user=request.user).order_by('-date_taken')[:20]
    lessons2 = []

    lesson_urls = {'Fundamental Concepts of Mathematics': 'fundamental',
                   'Equalities and Inequalities': 'equalities_inequalities', 'Linear Equations': 'linear_equalities',
                   'Types of Numbers': 'types_of_numbers',
                   'Operations with Positive and Negative Numbers': 'working_with_signs',
                   'Fractions and Rational Numbers': 'fractions', 'Quadratic Equations': 'quadratic_equations',
                   'Inequalities': 'inequalities', 'Linear Functions': 'linear_functions',
                   'Other Types of Functions': 'other_kind_of_functions', 'Introduction to Logarithms': 'logarithm',
                   'Operations on Logarithms': 'operation_on_logarithm',
                   'Logarithmic Functions': 'logarithmic_functions',
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
    for i in lessons:
        lessons2.append(
            {'url': lesson_urls[i.lesson],
             'lesson': i}
        )
    try:
        country = Country.objects.get(user=request.user)
        country_name = country.country
        country_flag_code = countries_flags[country_name]
    except:
        country_name = 'Anonymous'
        country_flag_code = ''
    context = {
        'profile': profile,
        'user': request.user,
        'scores': scores,
        'lessons': lessons2,
        'country': country_name,
        'country_flag_code': country_flag_code,
        'urls': lesson_urls
    }

    return render(request, 'profile.html', context)


@login_required
def equalities_inequalities(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'equations_and_inequalities.html')


@login_required
def linear_equalities(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'linear_equalities.html')


@login_required
def types_of_numbers(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'types_of_numbers.html')


@login_required
def working_with_signs(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'signs.html')


@login_required
def fractions(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'fractions.html')


@login_required
def quadratic_equations(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'quadratic_equations.html')


@login_required
def inequalities(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'inequalities.html')


@login_required
def linear_functions(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    from fractions import Fraction
    number = Fraction(5, 6)
    return render(request, 'linear_functions.html', {'number': number})


@login_required
def other_kind_of_functions(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'other_kind_of_functions.html')


@login_required
def logarithm(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'logarithm.html')


@login_required
def operation_on_logarithm(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'operations_on_logarithm.html')


@login_required
def logarithmic_functions(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'logarithmic_functions.html')


@login_required
def trigonometry(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'trigonometry.html')


@login_required
def operations_in_trigonometry(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'operations_in_trigonometry.html')


@login_required
def inverse_trigonometric_functions(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'inverse_trigonometric_functions.html')


@login_required
def test(request):
    if request.user.is_superuser:
        return render(request, 'myfirstfrontend_code.html')
    else:
        return redirect('/')


@login_required
def introduction_to_geometry(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'introduction_to_geometry.html')


@login_required
def measurement_and_distance(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'measurement_and_distance_in_plane.html')


@login_required
def angles(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'angles.html')


@login_required
def triangle_types(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'triangle_types.html')


@login_required
def properties_of_triangles(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'properties_of_triangles.html')


@login_required
def quadrilaterals_and_squares(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'quadrilaterals_and_squares.html')


@login_required
def types_of_quadrilateral(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'types_of_quadrilaterals.html')


@login_required
def circle_basic(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'circle_basic.html')


@login_required
def other_properties_of_circle(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'other_properties_of_circle.html')


@login_required
def equation_of_circle(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'formula_of_circle.html')


@login_required
def plane(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'plane.html')


@login_required
def distance_midpoint_slope(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'distance_midpoint_slope.html')


@login_required
def the_laws_of_sines(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'law_of_sines.html')


@login_required
def the_laws_of_cosines(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'law_of_cosines.html')


@login_required
def similar_triangles(request):
    save_taken_lessons(request.resolver_match.url_name, request)
    return render(request, 'similar_triangles.html')


import json
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required


def practice(request):
    from .math_problems_json import math_problems_json
    url = request.GET.get('url')

    data = math_problems_json[url]
    print(len(data))

    return render(request, 'practice.html', {'data': data, 'url': url})


@login_required  # agar login kerak bo'lsa
def save_results(request, url):
    if request.method == 'POST':
        print(url)
        data = json.loads(request.body)
        lesson = Lessons.objects.get(url=url)
        data1 = MathTestResult.objects.create(
            lesson=lesson,
            user=request.user,
            correct=data['correct'],
            wrong=data['wrong'],
            correct_percentage=data['correct_percentage'],
            time_spent_seconds=data['time_spent_seconds'],
            time_spent_display=data['time_spent_display'],
            avg_time_per_question_seconds=data['avg_time_per_question_seconds'],
            test_taken_at=data['test_taken_at'],
            total_questions=data['total_questions'],
            questions_json_formatted=data['questions']
        )
        pk = data1.pk
        data1.save()
        return JsonResponse({'status': 'ok', 'pk': pk})
    return JsonResponse({'error': 'Only POST'}, status=405)


def adding_values(request):
    if request.user.is_superuser:

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
        from .models import Lessons
        for i, j in data.items():
            data = Lessons.objects.create(
                lesson_name=i,
                url=j,
            )
            data.save()
        return JsonResponse({'status': 'ok'})
    else:
        return redirect('/')


def review_past_test_results(request, pk):
    data = MathTestResult.objects.get(pk=pk)
    complete_data = {
        'correct': data.correct,
        'wrong': data.wrong,
        'correct_percentage': data.correct_percentage,
        'time_spent_seconds': data.time_spent_seconds,
        'avg_time_per_question_seconds': data.avg_time_per_question_seconds,
        'test_taken_at': data.test_taken_at,
        'questions': data.questions_json_formatted
    }

    return render(request, 'results_description.html', {'data': complete_data})


from django.core.mail import send_mail


def send_code(request):
    from django.contrib.auth.hashers import make_password
    from random import randint
    from .models import PendingUser
    data = json.loads(request.body)
    code = randint(100000, 999999)

    pending_data = PendingUser.objects.create(
        email=data['email'],
        username=data['username'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        password=make_password(data['password']),  # ✅ hash qilib saqlash
        code=code,
        country=data['country']
    )

    pending_data.save()
    send_mail(
        "Math Academy",
        f"Your code: {code}",
        "botbexruz640@gmail.com",
        [data['email']],
        fail_silently=False,
    )
    return JsonResponse({"success": True})


def verify_email(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        data = json.loads(request.body)
        code = data.get('code', '').strip()
        email = data.get('email', '').strip()

        try:
            pending = PendingUser.objects.get(email=email, code=code)
        except PendingUser.DoesNotExist:
            return JsonResponse({'error': 'Invalid or expired code.'}, status=400)

        if pending.is_expired():
            pending.delete()
            return JsonResponse({'error': 'Code expired. Request a new one.'}, status=400)

        if User.objects.filter(username=pending.username).exists():
            return JsonResponse({'error': 'Username already taken.'}, status=400)

        user = User.objects.create_user(
            username=pending.username,
            email=pending.email,
            first_name=pending.first_name,
            last_name=pending.last_name,
            password=None,  # ← None beryapsan
        )

        user.password = pending.password  # ← keyin qo'lyapsan
        user.save()
        country = Country.objects.create(country=pending.country, user=user)
        country.save()

        pending.delete()

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return JsonResponse({'success': True, 'redirect': '/'})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
