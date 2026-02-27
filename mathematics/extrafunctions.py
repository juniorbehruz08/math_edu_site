import random
import json


def generate_math_problems():
    """
    Generates a list of 20 math problems and their solutions,
    combining four different types of quadratic function problems.
    The problems are formatted as a JSON string.
    """
    problems = []

    def generate_quadratic(x):
        a = random.randint(-5, 5)
        while a == 0:
            a = random.randint(-5, 5)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)

        func_str = f'{a}x²'
        if b != 0:
            func_str += f' + {b}x' if b > 0 else f' - {abs(b)}x'
        if c != 0:
            func_str += f' + {c}' if c > 0 else f' - {abs(c)}'

        # Clean up the string to make it look nicer
        func_str = func_str.replace('1x²', 'x²').replace('-1x²', '-x²').replace('+ 1x', ' + x').replace('- 1x', ' - x')

        # Correctly handle initial positive/negative signs
        if func_str.startswith('+ '):
            func_str = func_str[2:]

        question = f'What is the value of the function f(x) = {func_str}, when x = {x}?'
        answer = a * x ** 2 + b * x + c
        fake_answers4 = []
        while True:
            x = random.randint(answer - 10, answer + 10)
            if x not in fake_answers4 and x != answer:
                fake_answers4.append(x)
            if len(fake_answers4) == 3:
                break
        return question, answer, fake_answers4

    def x_intersection_of_quadratic_function():
        r1 = random.randint(-10, 10)
        r2 = random.randint(-10, 10)

        b = -1 * (r1 + r2)
        c = r1 * r2

        func_str = 'x²'
        if b != 0:
            func_str += f' + {b}x' if b > 0 else f' - {abs(b)}x'
        if c != 0:
            func_str += f' + {c}' if c > 0 else f' - {abs(c)}'

        question = f'Find the x-intercepts of the function f(x) = {func_str}.'
        # Sort for consistent output
        answer = f'({min(r1, r2)}, 0) and ({max(r1, r2)}, 0)'
        fake_answers = []
        while True:
            fake_answer = f'({random.randint(min(r1, r2) - 10, max(r1, r2) + 10)}, 0) and ({random.randint(min(r1, r2), max(r1, r2))}, 0)'
            if fake_answer != answer and fake_answer not in fake_answers:
                fake_answers.append(fake_answer)
            if len(fake_answers) == 3:
                break

        return question, answer, fake_answers

    def generate_integer_vertex_quadratic():
        a = random.randint(-5, 5)
        while a == 0:
            a = random.randint(-5, 5)
        h = random.randint(-10, 10)
        k = random.randint(-15, 15)

        b = -2 * a * h
        c = a * (h ** 2) + k

        func_str = f'{a}x²'
        if b != 0:
            func_str += f' + {b}x' if b > 0 else f' - {abs(b)}x'
        if c != 0:
            func_str += f' + {c}' if c > 0 else f' - {abs(c)}'

        func_str = func_str.replace('1x²', 'x²').replace('-1x²', '-x²').replace('+ 1x', ' + x').replace('- 1x', ' - x')
        if func_str.startswith('+ '):
            func_str = func_str[2:]

        question = f'Find the vertex of the function f(x) = {func_str}.'
        answer = f'({h}, {k})'
        fake_answers1 = []
        while True:
            fake_answer1 = f'({random.randint(h - 10, h + 10)}, {random.randint(k - 10, k + 10)})'
            if fake_answers1 != answer and fake_answer1 not in fake_answers1:
                fake_answers1.append(fake_answer1)
            if len(fake_answers1) == 3:
                break
        return question, answer, fake_answers1

    def generate_find_a_problem_single_answer():
        a = random.randint(-4, 4)
        while a == 0:
            a = random.randint(-4, 4)
        root = random.randint(-8, 8)
        y_value = random.randint(-20, 20)

        b = -2 * a * root
        c = a * root ** 2 + y_value

        func_str = f'{a}x²'
        if b != 0:
            func_str += f' + {b}x' if b > 0 else f' - {abs(b)}x'
        if c != 0:
            func_str += f' + {c}' if c > 0 else f' - {abs(c)}'

        func_str = func_str.replace('1x²', 'x²').replace('-1x²', '-x²').replace('+ 1x', ' + x').replace('- 1x', ' - x')
        if func_str.startswith('+ '):
            func_str = func_str[2:]

        question = f'The function is given as f(x) = {func_str}. If f(a)={y_value}, find the value of a.'
        answer = str(root)
        fake_answers3 = []
        while True:
            fake_answer2 = random.randint(root - 10, root + 10)
            if fake_answer2 not in fake_answers3 and fake_answer2 != root:
                fake_answers3.append(fake_answer2)
            if len(fake_answers3) == 3:
                break
        return question, answer, fake_answers3

    # Generate 5 problems of each type
    for i in range(5):
        q1, a1, fake_4 = generate_quadratic(random.randint(-10, 10))
        problems.append({'question': q1, 'answer': str(a1), 'wrong_answers': list(map(str, fake_4))})

    for i in range(5):
        q2, a2, fake_answers = x_intersection_of_quadratic_function()
        problems.append({'question': q2, 'answer': str(a2), 'wrong_answers': list(map(str, fake_answers))})

    for _ in range(5):
        q, a, fake_answers2 = generate_integer_vertex_quadratic()
        problems.append({'question': q, 'answer': str(a), 'wrong_answers': list(map(str, fake_answers2))})

    for _ in range(5):
        q, a, fake_answers3 = generate_find_a_problem_single_answer()
        problems.append({'question': q, 'answer': str(a), 'wrong_answers': list(map(str, fake_answers3))})

    return json.dumps(problems, indent=4, ensure_ascii=False)


import random
import json


def generate_cubic_math_problems_en():
    """
    Generates three types of cubic function problems
    (total of 21 problems) similar to quadratic function tasks.
    Returns the result as a JSON formatted string.
    """
    problems = []

    def format_polynomial(a, b, c, d):
        """Format cubic polynomial in the form a*x³ + b*x² + c*x + d."""
        func_str = f'{a}x³'
        if b != 0:
            func_str += f' + {b}x²' if b > 0 else f' - {abs(b)}x²'
        if c != 0:
            func_str += f' + {c}x' if c > 0 else f' - {abs(c)}x'
        if d != 0:
            func_str += f' + {d}' if d > 0 else f' - {abs(d)}'

        # Clean up forms like 1x, -1x
        func_str = func_str.replace('1x³', 'x³').replace('-1x³', '-x³')
        func_str = func_str.replace('1x²', 'x²').replace('-1x²', '-x²')
        func_str = func_str.replace('+ 1x', ' + x').replace('- 1x', ' - x')

        if func_str.startswith('+ '):
            func_str = func_str[2:]
        if func_str.startswith(' '):
            func_str = func_str[1:]

        return func_str

    # --- Problem Type 1: Function Evaluation (f(x) = ?) ---
    def generate_cubic_evaluation(x_val):
        """Find the value of a cubic function at a given x."""
        a = random.randint(-3, 3)
        while a == 0:
            a = random.randint(-3, 3)
        b = random.randint(-5, 5)
        c = random.randint(-7, 7)
        d = random.randint(-10, 10)

        func_str = format_polynomial(a, b, c, d)

        # Question
        question = f'If f(x) = {func_str}, find the value of f({x_val}).'

        # Answer
        answer = a * x_val ** 3 + b * x_val ** 2 + c * x_val + d

        # Wrong answers
        fake_answers = []
        while len(fake_answers) < 3:
            x = random.randint(answer - 20, answer + 20)
            if x not in fake_answers and x != answer:
                fake_answers.append(x)
        return question, answer, fake_answers

    # --- Problem Type 2: X-Intercepts (Roots) ---
    def x_intercepts_of_cubic_function():
        """Find the x-intercepts (roots) of a factored cubic function."""
        r1 = random.randint(-5, 5)
        r2 = random.randint(-5, 5)
        r3 = random.randint(-5, 5)

        a = 1
        b = -1 * (r1 + r2 + r3)
        c = (r1 * r2 + r1 * r3 + r2 * r3)
        d = -1 * r1 * r2 * r3

        func_str = format_polynomial(a, b, c, d)

        # Question
        question = f'For f(x) = {func_str}, find the x-intercepts (roots).'

        # Answer
        roots = sorted([r1, r2, r3])
        answer = f'({roots[0]}, 0), ({roots[1]}, 0), ({roots[2]}, 0)'

        # Wrong answers
        fake_answers = []
        while len(fake_answers) < 3:
            fake_roots = list(roots)
            indices_to_change = random.sample(range(3), random.randint(1, 3))

            for idx in indices_to_change:
                change = random.choice([-2, -1, 1, 2])
                fake_roots[idx] += change

            fake_roots.sort()
            fake_answer_str = f'({fake_roots[0]}, 0), ({fake_roots[1]}, 0), ({fake_roots[2]}, 0)'

            if fake_answer_str != answer and fake_answer_str not in fake_answers:
                fake_answers.append(fake_answer_str)

        return question, answer, fake_answers

    # --- Problem Type 3: Find X when f(x) = Y ---
    def generate_find_x_for_y_problem():
        """Solve for x when f(x) = y given a cubic function in vertex form-like structure."""
        a = random.randint(-2, 2)
        while a == 0:
            a = random.randint(-2, 2)
        root = random.randint(-5, 5)
        y_val = random.randint(-15, 15)

        b = -3 * a * root
        c = 3 * a * (root ** 2)
        d = -a * (root ** 3) + y_val

        func_str = format_polynomial(a, b, c, d)

        # Question
        question = f'The function f(x) = {func_str} is given. If f(x) = {y_val}, find the value of x.'

        # Answer
        answer = str(root)

        # Wrong answers
        fake_answers = []
        while len(fake_answers) < 3:
            fake_answer = random.randint(root - 5, root + 5)
            if fake_answer not in fake_answers and str(fake_answer) != answer:
                fake_answers.append(fake_answer)
        return question, answer, fake_answers

    # Generate 7 problems of each type
    for _ in range(5):
        x_to_evaluate = random.randint(-5, 5)
        q, a, fake_answers = generate_cubic_evaluation(x_to_evaluate)
        problems.append({'question': q, 'answer': str(a), 'wrong_answers': list(map(str, fake_answers))})

    for _ in range(5):
        q, a, fake_answers = x_intercepts_of_cubic_function()
        problems.append({'question': q, 'answer': str(a), 'wrong_answers': list(map(str, fake_answers))})

    for _ in range(10):
        q, a, fake_answers = generate_find_x_for_y_problem()
        problems.append({'question': q, 'answer': str(a), 'wrong_answers': list(map(str, fake_answers))})

    random.shuffle(problems)

    return json.dumps(problems, indent=4, ensure_ascii=False)


# Example:
# print(generate_cubic_math_problems_en())
import random
import json
from math import gcd


def generate_rational_math_problems_fixed():
    """
    Generates 4 types of rational function problems
    (total of 20 problems). Ensures wrong answers are unique.
    Returns the result as a JSON string.
    """
    import random
    from math import gcd
    import json

    problems = []

    def format_polynomial(a, b=0, c=0):
        """Formats a polynomial up to quadratic (a*x² + b*x + c)."""
        parts = []
        if a != 0:
            if abs(a) == 1 and a < 0:
                parts.append('-x²')
            elif abs(a) == 1 and a > 0:
                parts.append('x²')
            else:
                parts.append(f'{a}x²')

        if b != 0:
            term = 'x' if abs(b) == 1 else f'{abs(b)}x'
            if b > 0 and parts:
                parts.append(f'+ {term}')
            elif b > 0 and not parts:
                parts.append(term)
            else:
                parts.append(f'- {term}')

        if c != 0:
            sign = '+' if c > 0 and parts else ''
            sign = '' if c > 0 and not parts else sign
            parts.append(f'{sign} {abs(c)}' if sign else str(c))

        return ''.join(parts).strip().replace('+ -', '- ')

    def format_rational_function(px_params, qx_params):
        """Formats a rational function nicely."""
        P_x = format_polynomial(*px_params)
        Q_x = format_polynomial(*qx_params)
        return f'\\frac{{{P_x}}}{{{Q_x}}}'

    # --- Problem Type 1: Function Evaluation ---
    def generate_rational_evaluation():
        p_b = random.randint(-10, 10)
        p_c = random.randint(-10, 10)
        q_b = random.randint(-5, 5)
        q_c = random.randint(-5, 5)
        x_val = random.randint(-5, 5)
        while q_b * x_val + q_c == 0:
            x_val = random.randint(-5, 5)

        px_params = (0, p_b, p_c)
        qx_params = (0, q_b, q_c)
        func_str = format_rational_function(px_params, qx_params)

        numerator = p_b * x_val + p_c
        denominator = q_b * x_val + q_c

        if numerator % denominator == 0:
            answer = str(numerator // denominator)
        else:
            common_divisor = gcd(numerator, denominator)
            num = numerator // common_divisor
            den = denominator // common_divisor
            answer = f'{num}/{den}'
            if den < 0:
                answer = f'{-num}/{-den}'

        question = f'If f(x) = {func_str}, find the value of the function at x = {x_val}.'

        fake_answers_set = set()
        while len(fake_answers_set) < 3:
            if answer.isdigit() or (answer.startswith('-') and answer[1:].isdigit()):
                ans_int = int(answer)
                fake = str(random.randint(ans_int - 5, ans_int + 5))
            else:
                fake_num = random.randint(numerator - 5, numerator + 5)
                if fake_num % denominator == 0:
                    fake = str(fake_num // denominator)
                else:
                    g = gcd(fake_num, denominator)
                    fake = f'{fake_num // g}/{denominator // g}'

            if fake != answer:
                fake_answers_set.add(fake)

        return question, answer, list(fake_answers_set)

    # --- Problem Type 2: Vertical Asymptotes ---
    def generate_vertical_asymptote():
        choice = random.choice(['linear', 'quadratic'])

        if choice == 'linear':
            root = random.randint(-5, 5)
            q_b, q_c = 1, -root

            px_params = (0, random.randint(1, 5), random.randint(-5, 5))
            qx_params = (0, q_b, q_c)
            func_str = format_rational_function(px_params, qx_params)

            question = f'Find the vertical asymptotes of f(x) = {func_str}.'
            answer = f'x = {root}'

            fake_answers_set = set()
            while len(fake_answers_set) < 3:
                fake = f'x = {root + random.choice([-3, -2, -1, 1, 2, 3])}'
                if fake != answer:
                    fake_answers_set.add(fake)
            fake_answers = list(fake_answers_set)
        else:
            r1 = random.randint(1, 5)
            r2 = -r1
            roots = sorted([r1, r2])

            px_params = (0, random.randint(1, 5), random.randint(-5, 5))
            qx_params = (1, 0, -r1 ** 2)
            func_str = format_rational_function(px_params, qx_params)

            question = f'Find the vertical asymptotes of f(x) = {func_str}.'
            answer = f'x = {roots[0]} and x = {roots[1]}'

            fake_answers_set = set()
            while len(fake_answers_set) < 3:
                r_fake = random.randint(-6, 6)
                if r_fake != r1 and r_fake != r2:
                    fake = f'x = {roots[0]} and x = {r_fake}'
                    if sorted([roots[0], r_fake]) != roots:
                        fake_answers_set.add(fake)
            fake_answers = list(fake_answers_set)

        return question, answer, fake_answers

    # --- Problem Type 3: Horizontal/Slant Asymptotes ---
    def generate_horizontal_or_slant_asymptote():
        choice = random.choice(['HA_eq', 'HA_low', 'SA'])

        if choice == 'HA_eq':
            a_p = random.randint(1, 5)
            a_q = random.randint(1, 5)

            px_params = (a_p, random.randint(-5, 5), random.randint(-10, 10))
            qx_params = (a_q, random.randint(-5, 5), random.randint(-10, 10))
            func_str = format_rational_function(px_params, qx_params)

            question = f'Find the horizontal asymptote of f(x) = {func_str}.'

            common_divisor = gcd(a_p, a_q)
            num = a_p // common_divisor
            den = a_q // common_divisor
            answer = f'y = {num}/{den}' if den != 1 else f'y = {num}'

            fake_answers_set = set()
            fake_answers_set.add(f'y = {a_q}/{a_p}' if a_q != a_p else f'y = {a_p + 1}/{a_q}')
            fake_answers_set.add('y = 0')
            fake_answers_set.add(f'y = {num + 1}/{den}')

            if answer in fake_answers_set: fake_answers_set.remove(answer)

            fake_answers = list(fake_answers_set)[:3]

        elif choice == 'HA_low':
            px_params = (0, random.randint(1, 5), random.randint(-5, 5))
            qx_params = (random.randint(1, 5), random.randint(-5, 5), random.randint(-10, 10))
            func_str = format_rational_function(px_params, qx_params)

            question = f'Find the horizontal asymptote of f(x) = {func_str}.'
            answer = 'y = 0'
            fake_answers = ['y = 1', 'y = x', 'No asymptote']

        else:  # Slant
            q_b = random.choice([-2, -1, 1, 2])
            q_c = random.randint(-3, 3)
            a = random.choice([-1, 1])
            b = random.randint(-2, 2)

            p_a = a * q_b
            p_b = a * q_c + b * q_b
            p_c = b * q_c + random.randint(1, 5)

            px_params = (p_a, p_b, p_c)
            qx_params = (0, q_b, q_c)
            func_str = format_rational_function(px_params, qx_params)

            question = f'Find the slant asymptote of f(x) = {func_str}.'

            answer = f'y = {a}x + {b}' if b != 0 else f'y = {a}x'
            answer = answer.replace('1x', 'x').replace('-1x', '-x').replace('+ -', '- ').replace(' + -', ' - ')

            fake_answers_set = set()
            fake_b = b + random.choice([-2, 2])
            fake_answers_set.add(f'y = {a}x + {fake_b}' if fake_b != 0 else f'y = {a}x')
            fake_answers_set.add(f'y = {a}x')
            fake_answers_set.add('Horizontal asymptote exists')

            fake_answers = [f.replace('1x', 'x').replace('-1x', '-x').replace('+ -', '- ') for f in fake_answers_set]
            if answer in fake_answers: fake_answers.remove(answer)

        return question, answer, fake_answers[:3]

    # --- Problem Type 4: X-Intercepts ---
    def generate_x_intercepts():
        choice = random.choice(['linear', 'quadratic'])

        if choice == 'linear':
            root = random.randint(-5, 5)
            p_b, p_c = 1, -root

            qx_params = (0, random.randint(1, 5), random.randint(-5, 5))
            while qx_params[1] * root + qx_params[2] == 0:
                root = random.randint(-5, 5)
                p_c = -root

            px_params = (0, p_b, p_c)
            func_str = format_rational_function(px_params, qx_params)

            question = f'Find the x-intercept of f(x) = {func_str}.'
            answer = f'x = {root}'

            fake_answers_set = set()
            while len(fake_answers_set) < 3:
                fake = f'x = {root + random.choice([-3, -2, -1, 1, 2, 3])}'
                if fake != answer:
                    fake_answers_set.add(fake)
            fake_answers = list(fake_answers_set)

        else:
            r1, r2 = random.randint(-4, 4), random.randint(-4, 4)
            while r1 == r2: r2 = random.randint(-4, 4)

            p_a, p_b, p_c = 1, -1 * (r1 + r2), r1 * r2
            qx_params = (0, random.randint(1, 5), random.randint(-5, 5))

            q_b, q_c = qx_params[1], qx_params[2]
            while q_b * r1 + q_c == 0 or q_b * r2 + q_c == 0:
                r1, r2 = random.randint(-4, 4), random.randint(-4, 4)
                while r1 == r2: r2 = random.randint(-4, 4)
                p_b, p_c = -1 * (r1 + r2), r1 * r2

            px_params = (p_a, p_b, p_c)
            func_str = format_rational_function(px_params, qx_params)

            question = f'Find the x-intercepts of f(x) = {func_str}.'
            roots = sorted([r1, r2])
            answer = f'x = {roots[0]} and x = {roots[1]}'

            fake_answers_set = set()
            while len(fake_answers_set) < 3:
                r_fake = random.randint(min(roots) - 3, max(roots) + 3)
                fake_roots = sorted([roots[0], r_fake])
                fake = f'x = {fake_roots[0]} and x = {fake_roots[1]}'
                if fake != answer:
                    fake_answers_set.add(fake)
            fake_answers = list(fake_answers_set)

        return question, answer, fake_answers

    # Generate 20 problems (5 each type)
    for _ in range(5):
        q, a, fake_answers = generate_rational_evaluation()
        problems.append({'question': q, 'answer': a, 'wrong_answers': fake_answers})

    for _ in range(5):
        q, a, fake_answers = generate_vertical_asymptote()
        problems.append({'question': q, 'answer': a, 'wrong_answers': fake_answers})

    for _ in range(5):
        q, a, fake_answers = generate_horizontal_or_slant_asymptote()
        problems.append({'question': q, 'answer': a, 'wrong_answers': fake_answers})

    for _ in range(5):
        q, a, fake_answers = generate_x_intercepts()
        problems.append({'question': q, 'answer': a, 'wrong_answers': fake_answers})

    random.shuffle(problems)

    return json.dumps(problems, indent=4, ensure_ascii=False)


def generate_exponential_problems():
    """
    Generates 4 types of exponential function problems (total 20 problems),
    using HTML <sup> for exponents for frontend display.
    Returns the result as a JSON string.
    """
    import random
    import json

    problems = []

    # --- Problem Type 1: Function Evaluation ---
    def generate_exponential_evaluation():
        a = random.randint(1, 5)
        b = random.randint(2, 5)
        x_val = random.randint(0, 5)

        question = f'If f(x) = {a}·{b}<sup>x</sup>, find the value of f({x_val}).'
        answer = a * (b ** x_val)

        fake_answers_set = set()
        while len(fake_answers_set) < 3:
            delta = random.choice([-3, -2, -1, 1, 2, 3])
            fake = answer + delta
            if fake != answer:
                fake_answers_set.add(fake)

        return question, str(answer), list(fake_answers_set)

    # --- Problem Type 2: Solve for x given f(x) = y ---
    def generate_solve_for_x():
        a = random.randint(1, 5)
        b = random.randint(2, 5)
        x_val = random.randint(0, 5)
        y_val = a * (b ** x_val)

        question = f'The function f(x) = {a}·{b}<sup>x</sup> is given. If f(x) = {y_val}, find the value of x.'
        answer = str(x_val)

        fake_answers_set = set()
        while len(fake_answers_set) < 3:
            fake = random.randint(max(0, x_val - 3), x_val + 3)
            if str(fake) != answer:
                fake_answers_set.add(str(fake))

        return question, answer, list(fake_answers_set)

    # --- Problem Type 3: Identify base or growth factor ---
    def generate_find_base():
        a = random.randint(1, 5)
        b = random.randint(2, 5)
        x_val = random.randint(1, 4)
        y_val = a * (b ** x_val)

        question = f'If f(x) = {a}·b<sup>x</sup> and f({x_val}) = {y_val}, find the value of b.'
        answer = str(b)

        fake_answers_set = set()
        while len(fake_answers_set) < 3:
            fake = random.randint(2, 6)
            if str(fake) != answer:
                fake_answers_set.add(str(fake))

        return question, answer, list(fake_answers_set)

    # --- Problem Type 4: Find coefficient a ---
    def generate_find_coefficient():
        a = random.randint(1, 5)
        b = random.randint(2, 5)
        x_val = random.randint(0, 5)
        y_val = a * (b ** x_val)

        question = f'If f(x) = a·{b}<sup>x</sup> and f({x_val}) = {y_val}, find the value of a.'
        answer = str(a)

        fake_answers_set = set()
        while len(fake_answers_set) < 3:
            fake = random.randint(1, 6)
            if str(fake) != answer:
                fake_answers_set.add(str(fake))

        return question, answer, list(fake_answers_set)

    # Generate 5 problems of each type (total 20)
    for _ in range(5):
        q, a, fakes = generate_exponential_evaluation()
        problems.append({'question': q, 'answer': a, 'wrong_answers': fakes})

    for _ in range(5):
        q, a, fakes = generate_solve_for_x()
        problems.append({'question': q, 'answer': a, 'wrong_answers': fakes})

    for _ in range(5):
        q, a, fakes = generate_find_base()
        problems.append({'question': q, 'answer': a, 'wrong_answers': fakes})

    for _ in range(5):
        q, a, fakes = generate_find_coefficient()
        problems.append({'question': q, 'answer': a, 'wrong_answers': fakes})

    import random
    random.shuffle(problems)
    return json.dumps(problems, indent=4, ensure_ascii=False)


def logarithm_generator():
    subscript_digits = {
        0: "₀",
        1: "₁",
        2: "₂",
        3: "₃",
        4: "₄",
        5: "₅",
        6: "₆",
        7: "₇",
        8: "₈",
        9: "₉"
    }
    superscript_digits = {
        0: "⁰",
        1: "¹",
        2: "²",
        3: "³",
        4: "⁴",
        5: "⁵",
        6: "⁶",
        7: "⁷",
        8: "⁸",
        9: "⁹"
    }
    questions = []
    from random import randint, shuffle
    for i in range(5):
        fakes1 = []

        x = randint(0, 5)
        a = randint(2, 4)
        b = a ** x
        question = f'log{subscript_digits[a]}({b})'
        answer = x
        while True:
            if len(fakes1) == 3:
                break
            fake_answer = randint(answer - 3, answer + 3)
            if fake_answer != x and fake_answer not in fakes1:
                fakes1.append(fake_answer)
        questions.append({'question': question, 'answer': answer, 'wrong_answers': fakes1})
    for i in range(5):
        fakes2 = []

        x = randint(0, 5)
        a = randint(2, 4)
        c = randint(2, 5)
        b = a ** x
        question = f'log{subscript_digits[a]}({b}{superscript_digits[c]})'
        answer = c * x
        while True:
            if len(fakes2) == 3:
                break
            fake_answer = randint(answer - 3, answer + 3)
            if fake_answer != x and fake_answer not in fakes2:
                fakes2.append(fake_answer)
        questions.append({'question': question, 'answer': answer, 'wrong_answers': fakes2})
    for i in range(5):
        fakes3 = []

        x = randint(0, 5)
        a = randint(2, 4)
        b = a ** x
        question = f'log<sub>1/{a}</sub>({b})'
        answer = -x
        print(question, answer)
        while True:
            if len(fakes3) == 3:
                break
            fake_answer = randint(answer - 3, answer + 3)
            if fake_answer != x and fake_answer not in fakes3:
                fakes3.append(fake_answer)
        questions.append({'question': question, 'answer': answer, 'wrong_answers': fakes3})
    for i in range(5):
        fakes5 = []

        b = randint(2, 4)  # asos
        d = randint(2, 3)  # asos darajasi
        k = randint(1, 3)  # x = b^k
        x = b ** k
        y = d * randint(1, 3)  # y d ga bo‘linadigan qilib tanlanadi

        question = f'log<sub>{b}{superscript_digits[d]}</sub>({x}{superscript_digits[y]})'
        answer = (y // d) * k  # butun son chiqadi

        while len(fakes5) < 3:
            fake_answer = answer + randint(-3, 3)
            if fake_answer != answer and fake_answer not in fakes5:
                fakes5.append(fake_answer)

        questions.append({'question': question, 'answer': answer, 'wrong_answers': fakes5})

    shuffle(questions)
    return questions


import random


def logarithm_generator_ops_v2():
    # sub/sup yozuvlar
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")

    def to_sub(n):
        return str(n).translate(SUB)

    def to_sup(n):
        return str(n).translate(SUP)

    def log_fmt(base_num, val_str):
        return f"log{to_sub(base_num)}({val_str})"

    def power_fmt(num, exp):
        return f"{num}{to_sup(exp)}"

    PRIMES = [2, 3, 5, 7]

    def build_term_value(p=None, r=None, u=None, t=None, target=None):
        """
        log_{p^r}((p^u)^{t*r})  ->  qiymat = u*t
        Agar target berilsa, u*t = target qilib quramiz (u ∈ {1,2,3}\{r}).
        """
        if p is None: p = random.choice(PRIMES)
        if r is None: r = random.randint(1, 3)

        if target is None:
            # erkin (butun) qiymatli term
            u_choices = [x for x in (1, 2, 3) if x != r]
            u = random.choice(u_choices) if u is None else u
            t = random.randint(1, 6) if t is None else t
        else:
            # maqsad qiymatni aniq qurish: u*t = target
            # u ni {1,2,3}\{r} dan va target ga bo'linadigan qilib tanlaymiz
            u_choices = [x for x in (1, 2, 3) if x != r and target % x == 0]
            # agar hech biri bo'lmasa, r ni o'zgartiramiz
            tries = 0
            while not u_choices:
                r = random.randint(1, 3)
                u_choices = [x for x in (1, 2, 3) if x != r and target % x == 0]
                tries += 1
                if tries > 20:  # zaruratda fallback: target=1 qiling
                    u_choices = [x for x in (1, 2, 3) if x != r]
                    target = max(1, abs(target))
                    if target % u_choices[0] != 0:
                        target = u_choices[0]
                    break
            u = random.choice(u_choices)
            t = target // u

        base_num = p ** r  # asos: p^r  (son ko'rinishida)
        arg_base_num = p ** u  # argumentdagi pastki son: p^u
        s = t * r  # ko'tarilayotgan daraja: t*r
        expr = log_fmt(base_num, power_fmt(arg_base_num, s))
        value = u * t
        return expr, value

    def term_int():
        return build_term_value()

    def term_with_value(target):
        return build_term_value(target=target)

    def wrongs_around(ans, k=3):
        pool = [ans + d for d in range(-3, 4) if d != 0]
        random.shuffle(pool)
        out = []
        for v in pool:
            if len(out) == k: break
            if v not in out:
                out.append(v)
        return out

    questions = []

    # 1) Qo‘shish
    for _ in range(5):
        e1, v1 = term_int()
        e2, v2 = term_int()
        q = f"{e1} + {e2}"
        a = v1 + v2
        questions.append({"question": q, "answer": a, "wrong_answers": wrongs_around(a)})

    # 2) Ayirish
    for _ in range(5):
        e1, v1 = term_int()
        e2, v2 = term_int()
        q = f"{e1} − {e2}"
        a = v1 - v2
        questions.append({"question": q, "answer": a, "wrong_answers": wrongs_around(a)})

    # 3) Ko‘paytirish
    for _ in range(5):
        e1, v1 = term_int()
        e2, v2 = term_int()
        q = f"{e1} × {e2}"
        a = v1 * v2
        questions.append({"question": q, "answer": a, "wrong_answers": wrongs_around(a)})

    # 4) Bo‘lish — ANIQ butun: v1 = k * v2 qilib quramiz
    for _ in range(5):
        e2, v2 = term_int()
        k = random.randint(1, 5)
        target = k * v2
        e1, v1 = term_with_value(target)  # v1 = k*v2 kafolat
        q = f"{e1} ÷ {e2}"
        a = k
        questions.append({"question": q, "answer": a, "wrong_answers": wrongs_around(a)})

    random.shuffle(questions)
    return questions


countries_flags = {
    "Afghanistan": "fi fi-af",
    "Albania": "fi fi-al",
    "Algeria": "fi fi-dz",
    "Andorra": "fi fi-ad",
    "Angola": "fi fi-ao",
    "Antigua and Barbuda": "fi fi-ag",
    "Argentina": "fi fi-ar",
    "Armenia": "fi fi-am",
    "Australia": "fi fi-au",
    "Austria": "fi fi-at",
    "Azerbaijan": "fi fi-az",
    "Bahamas": "fi fi-bs",
    "Bahrain": "fi fi-bh",
    "Bangladesh": "fi fi-bd",
    "Barbados": "fi fi-bb",
    "Belarus": "fi fi-by",
    "Belgium": "fi fi-be",
    "Belize": "fi fi-bz",
    "Benin": "fi fi-bj",
    "Bhutan": "fi fi-bt",
    "Bolivia": "fi fi-bo",
    "Bosnia and Herzegovina": "fi fi-ba",
    "Botswana": "fi fi-bw",
    "Brazil": "fi fi-br",
    "Brunei": "fi fi-bn",
    "Bulgaria": "fi fi-bg",
    "Burkina Faso": "fi fi-bf",
    "Burundi": "fi fi-bi",
    "Cabo Verde": "fi fi-cv",
    "Cambodia": "fi fi-kh",
    "Cameroon": "fi fi-cm",
    "Canada": "fi fi-ca",
    "Central African Republic": "fi fi-cf",
    "Chad": "fi fi-td",
    "Chile": "fi fi-cl",
    "China": "fi fi-cn",
    "Colombia": "fi fi-co",
    "Comoros": "fi fi-km",
    "Congo": "fi fi-cg",
    "Costa Rica": "fi fi-cr",
    "Croatia": "fi fi-hr",
    "Cuba": "fi fi-cu",
    "Cyprus": "fi fi-cy",
    "Czech Republic": "fi fi-cz",
    "Denmark": "fi fi-dk",
    "Djibouti": "fi fi-dj",
    "Dominica": "fi fi-dm",
    "Dominican Republic": "fi fi-do",
    "Ecuador": "fi fi-ec",
    "Egypt": "fi fi-eg",
    "El Salvador": "fi fi-sv",
    "Equatorial Guinea": "fi fi-gq",
    "Eritrea": "fi fi-er",
    "Estonia": "fi fi-ee",
    "Eswatini": "fi fi-sz",
    "Ethiopia": "fi fi-et",
    "Fiji": "fi fi-fj",
    "Finland": "fi fi-fi",
    "France": "fi fi-fr",
    "Gabon": "fi fi-ga",
    "Gambia": "fi fi-gm",
    "Georgia": "fi fi-ge",
    "Germany": "fi fi-de",
    "Ghana": "fi fi-gh",
    "Greece": "fi fi-gr",
    "Grenada": "fi fi-gd",
    "Guatemala": "fi fi-gt",
    "Guinea": "fi fi-gn",
    "Guinea-Bissau": "fi fi-gw",
    "Guyana": "fi fi-gy",
    "Haiti": "fi fi-ht",
    "Honduras": "fi fi-hn",
    "Hungary": "fi fi-hu",
    "Iceland": "fi fi-is",
    "India": "fi fi-in",
    "Indonesia": "fi fi-id",
    "Iran": "fi fi-ir",
    "Iraq": "fi fi-iq",
    "Ireland": "fi fi-ie",
    "Israel": "fi fi-il",
    "Italy": "fi fi-it",
    "Jamaica": "fi fi-jm",
    "Japan": "fi fi-jp",
    "Jordan": "fi fi-jo",
    "Kazakhstan": "fi fi-kz",
    "Kenya": "fi fi-ke",
    "Kiribati": "fi fi-ki",
    "Kuwait": "fi fi-kw",
    "Kyrgyzstan": "fi fi-kg",
    "Laos": "fi fi-la",
    "Latvia": "fi fi-lv",
    "Lebanon": "fi fi-lb",
    "Lesotho": "fi fi-ls",
    "Liberia": "fi fi-lr",
    "Libya": "fi fi-ly",
    "Liechtenstein": "fi fi-li",
    "Lithuania": "fi fi-lt",
    "Luxembourg": "fi fi-lu",
    "Madagascar": "fi fi-mg",
    "Malawi": "fi fi-mw",
    "Malaysia": "fi fi-my",
    "Maldives": "fi fi-mv",
    "Mali": "fi fi-ml",
    "Malta": "fi fi-mt",
    "Marshall Islands": "fi fi-mh",
    "Mauritania": "fi fi-mr",
    "Mauritius": "fi fi-mu",
    "Mexico": "fi fi-mx",
    "Micronesia": "fi fi-fm",
    "Moldova": "fi fi-md",
    "Monaco": "fi fi-mc",
    "Mongolia": "fi fi-mn",
    "Montenegro": "fi fi-me",
    "Morocco": "fi fi-ma",
    "Mozambique": "fi fi-mz",
    "Myanmar": "fi fi-mm",
    "Namibia": "fi fi-na",
    "Nauru": "fi fi-nr",
    "Nepal": "fi fi-np",
    "Netherlands": "fi fi-nl",
    "New Zealand": "fi fi-nz",
    "Nicaragua": "fi fi-ni",
    "Niger": "fi fi-ne",
    "Nigeria": "fi fi-ng",
    "North Korea": "fi fi-kp",
    "North Macedonia": "fi fi-mk",
    "Norway": "fi fi-no",
    "Oman": "fi fi-om",
    "Pakistan": "fi fi-pk",
    "Palau": "fi fi-pw",
    "Palestine": "fi fi-ps",
    "Panama": "fi fi-pa",
    "Papua New Guinea": "fi fi-pg",
    "Paraguay": "fi fi-py",
    "Peru": "fi fi-pe",
    "Philippines": "fi fi-ph",
    "Poland": "fi fi-pl",
    "Portugal": "fi fi-pt",
    "Qatar": "fi fi-qa",
    "Romania": "fi fi-ro",
    "Russia": "fi fi-ru",
    "Rwanda": "fi fi-rw",
    "Saint Kitts and Nevis": "fi fi-kn",
    "Saint Lucia": "fi fi-lc",
    "Saint Vincent and the Grenadines": "fi fi-vc",
    "Samoa": "fi fi-ws",
    "San Marino": "fi fi-sm",
    "Sao Tome and Principe": "fi fi-st",
    "Saudi Arabia": "fi fi-sa",
    "Senegal": "fi fi-sn",
    "Serbia": "fi fi-rs",
    "Seychelles": "fi fi-sc",
    "Sierra Leone": "fi fi-sl",
    "Singapore": "fi fi-sg",
    "Slovakia": "fi fi-sk",
    "Slovenia": "fi fi-si",
    "Solomon Islands": "fi fi-sb",
    "Somalia": "fi fi-so",
    "South Africa": "fi fi-za",
    "South Korea": "fi fi-kr",
    "South Sudan": "fi fi-ss",
    "Spain": "fi fi-es",
    "Sri Lanka": "fi fi-lk",
    "Sudan": "fi fi-sd",
    "Suriname": "fi fi-sr",
    "Sweden": "fi fi-se",
    "Switzerland": "fi fi-ch",
    "Syria": "fi fi-sy",
    "Tajikistan": "fi fi-tj",
    "Tanzania": "fi fi-tz",
    "Thailand": "fi fi-th",
    "Timor-Leste": "fi fi-tl",
    "Togo": "fi fi-tg",
    "Tonga": "fi fi-to",
    "Trinidad and Tobago": "fi fi-tt",
    "Tunisia": "fi fi-tn",
    "Turkey": "fi fi-tr",
    "Turkmenistan": "fi fi-tm",
    "Tuvalu": "fi fi-tv",
    "Uganda": "fi fi-ug",
    "Ukraine": "fi fi-ua",
    "United Arab Emirates": "fi fi-ae",
    "United Kingdom": "fi fi-gb",
    "United States": "fi fi-us",
    "Uruguay": "fi fi-uy",
    "Uzbekistan": "fi fi-uz",
    "Vanuatu": "fi fi-vu",
    "Vatican City": "fi fi-va",
    "Venezuela": "fi fi-ve",
    "Vietnam": "fi fi-vn",
    "Yemen": "fi fi-ye",
    "Zambia": "fi fi-zm",
    "Zimbabwe": "fi fi-zw",
}


def angle_test_in_trigonometry():
    import random

    def test_type1():
        values = {
            "sin": {
                "0": "0", "30": "1/2", "45": "√2/2", "60": "√3/2", "90": "1",
                "120": "√3/2", "135": "√2/2", "150": "1/2", "180": "0",
                "210": "-1/2", "225": "-√2/2", "240": "-√3/2", "270": "-1",
                "300": "-√3/2", "315": "-√2/2", "330": "-1/2", "360": "0"
            },
            "cos": {
                "0": "1", "30": "√3/2", "45": "√2/2", "60": "1/2", "90": "0",
                "120": "-1/2", "135": "-√2/2", "150": "-√3/2", "180": "-1",
                "210": "-√3/2", "225": "-√2/2", "240": "-1/2", "270": "0",
                "300": "1/2", "315": "√2/2", "330": "√3/2", "360": "1"
            },
            "tan": {
                "0": "0", "30": "1/√3", "45": "1", "60": "√3", "90": "undefined",
                "120": "-√3", "135": "-1", "150": "-1/√3", "180": "0",
                "210": "1/√3", "225": "1", "240": "√3", "270": "undefined",
                "300": "-√3", "315": "-1", "330": "-1/√3", "360": "0"
            },
            "cot": {
                "0": "undefined", "30": "√3", "45": "1", "60": "1/√3", "90": "0",
                "120": "-1/√3", "135": "-1", "150": "-√3", "180": "undefined",
                "210": "√3", "225": "1", "240": "1/√3", "270": "0",
                "300": "-1/√3", "315": "-1", "330": "-√3", "360": "undefined"
            }
        }

        random_answers = [
            "0", "1/2", "√2/2", "√3/2", "1",
            "-1/2", "-√2/2", "-√3/2", "-1",
            "√3/3", "-√3/3", "√3", "-√3", "undefined"
        ]

        function_options = ["sin", "cos", "tan", "cot"]
        angles = ["0", "30", "45", "60", "90", "120", "135", "150",
                  "180", "210", "225", "240", "270", "300", "315", "330", "360"]

        # 🔥 BARCHA MUMKIN BO‘LGAN SAVOLLAR
        all_pairs = [(f, a) for f in function_options for a in angles]
        selected_pairs = random.sample(all_pairs, 16)

        questions = []

        for func, angle in selected_pairs:
            question = f"What is the value of {func}{angle}°"
            answer = values[func][angle]

            wrong_answers = random.sample(
                [x for x in random_answers if x != answer], 3
            )

            questions.append({
                "question": question,
                "answer": answer,
                "wrong_answers": wrong_answers
            })

        return questions

    def trig_definition_test():
        import random

        definitions = {
            "sin": "opposite divided by hypotenuse",
            "cos": "adjacent divided by hypotenuse",
            "tan": "opposite divided by adjacent",
            "cot": "adjacent divided by opposite"
        }

        wrong_definitions = [
            "adjacent divided by hypotenuse",
            "hypotenuse divided by opposite",
            "hypotenuse divided by adjacent",
            "opposite divided by adjacent",
            "adjacent divided by opposite"
        ]

        questions = []

        for func, correct in definitions.items():
            wrong_answers = random.sample(
                [x for x in wrong_definitions if x != correct], 3
            )

            questions.append({
                "question": f"What is the definition of {func}?",
                "answer": correct,
                "wrong_answers": wrong_answers
            })

        return questions

    a = test_type1() + trig_definition_test()
    random.shuffle(a)
    return a


def test_for_inverse_function():
    def inverse_trigonometry_test():
        import random

        # 🔹 Inverse trig principal values (degrees)
        inverse_values = {
            "arcsin": {
                "0": "0°",
                "1/2": "30°",
                "√2/2": "45°",
                "√3/2": "60°",
                "-1/2": "-30°",
                "-√2/2": "-45°",
                "-√3/2": "-60°",
                "1": "90°",
                "-1": "-90°"
            },

            "arccos": {
                "1": "0°",
                "√3/2": "30°",
                "√2/2": "45°",
                "1/2": "60°",
                "0": "90°",
                "-1/2": "120°",
                "-√2/2": "135°",
                "-√3/2": "150°",
                "-1": "180°"
            },

            "arctan": {
                "0": "0°",
                "1/√3": "30°",
                "1": "45°",
                "√3": "60°",
                "-1/√3": "-30°",
                "-1": "-45°",
                "-√3": "-60°"
            },

            "arccot": {
                "√3": "30°",
                "1": "45°",
                "1/√3": "60°",
                "0": "90°",
                "-1/√3": "120°",
                "-1": "135°",
                "-√3": "150°"
            }
        }

        # 🔹 ALL possible correct angles (used for wrong_answers pool)
        wrong_angles = sorted(
            {angle for func in inverse_values.values() for angle in func.values()}
        )

        # 🔹 all possible (function, value, answer)
        all_pairs = [
            (func, value, angle)
            for func, vals in inverse_values.items()
            for value, angle in vals.items()
        ]

        selected = random.sample(all_pairs, 5)

        questions = []

        for func, value, correct_angle in selected:
            question = f"What is the value of {func}({value})?"

            wrong_answers = random.sample(
                [a for a in wrong_angles if a != correct_angle], 3
            )

            questions.append({
                "question": question,
                "answer": correct_angle,
                "wrong_answers": wrong_answers
            })

        return questions

    def arcsin_composition_test():
        import random

        # sin values
        sin_values = {
            "270°": "-1",
            "150°": "1/2",
            "210°": "-1/2",
            "330°": "-1/2",
            "390°": "1/2"
        }

        # arcsin principal values
        arcsin_values = {
            "1/2": "30°",
            "-1/2": "-30°",
            "√2/2": "45°",
            "-√2/2": "-45°",
            "√3/2": "60°",
            "-√3/2": "-60°",
            "1": "90°",
            "-1": "-90°"
        }

        wrong_angles = ["-90°", "-60°", "-45°", "-30°", "0°", "30°", "45°", "60°", "90°"]

        # 🔹 TYPE 1: outside range → mapped to principal value
        type1 = [
            ("270°", "-90°"),
            ("390°", "30°"),
            ("330°", "-30°")
        ]

        # 🔹 TYPE 2: inside range → unchanged
        type2 = [
            ("-30°", "-30°"),
            ("45°", "45°"),
            ("60°", "60°")
        ]

        questions = []

        selected_type1 = random.sample(type1, 3)
        selected_type2 = random.sample(type2, 2)

        # TYPE 1 questions
        for angle, correct in selected_type1:
            question = f"What is the value of arcsin(sin({angle}))?"

            wrong_answers = random.sample(
                [a for a in wrong_angles if a != correct], 3
            )

            questions.append({
                "question": question,
                "answer": correct,
                "wrong_answers": wrong_answers
            })

        # TYPE 2 questions
        for angle, correct in selected_type2:
            question = f"What is the value of arcsin(sin({angle}))?"

            wrong_answers = random.sample(
                [a for a in wrong_angles if a != correct], 3
            )

            questions.append({
                "question": question,
                "answer": correct,
                "wrong_answers": wrong_answers
            })

        return questions

    def inverse_trig_composition_test():
        import random

        # --- Base trig values (degree → exact value) ---
        trig_values = {
            "sin": {
                "0°": "0", "30°": "1/2", "45°": "√2/2", "60°": "√3/2",
                "90°": "1", "150°": "1/2", "210°": "-1/2",
                "270°": "-1", "330°": "-1/2"
            },
            "cos": {
                "0°": "1", "60°": "1/2", "90°": "0", "120°": "-1/2",
                "180°": "-1", "240°": "-1/2", "300°": "1/2"
            },
            "tan": {
                "0°": "0", "30°": "1/√3", "45°": "1", "60°": "√3",
                "210°": "1/√3", "225°": "1", "315°": "-1"
            },
            "cot": {
                "30°": "√3", "45°": "1", "60°": "1/√3",
                "210°": "√3", "225°": "1", "330°": "-√3"
            }
        }

        # --- Inverse principal values ---
        inverse_values = {
            "arcsin": {
                "0": "0°", "1/2": "30°", "√2/2": "45°",
                "√3/2": "60°", "1": "90°", "-1/2": "-30°", "-1": "-90°"
            },
            "arccos": {
                "1": "0°", "1/2": "60°", "0": "90°",
                "-1/2": "120°", "-1": "180°"
            },
            "arctan": {
                "0": "0°", "1/√3": "30°", "1": "45°",
                "√3": "60°", "-1": "-45°"
            },
            "arccot": {
                "√3": "30°", "1": "45°", "1/√3": "60°",
                "-1": "135°"
            }
        }

        composition_map = {
            "sin": "arcsin",
            "cos": "arccos",
            "tan": "arctan",
            "cot": "arccot"
        }

        # All possible principal angles (for wrong answers)
        wrong_angles = sorted({
            angle for inv in inverse_values.values() for angle in inv.values()
        })

        # --- Generate ALL possible compositions ---
        all_cases = []

        for trig_func, angle_map in trig_values.items():
            inv_func = composition_map[trig_func]
            for angle, value in angle_map.items():
                if value in inverse_values[inv_func]:
                    principal = inverse_values[inv_func][value]
                    all_cases.append((inv_func, trig_func, angle, principal))

        # --- Split by TYPE ---
        type_inside = [
            case for case in all_cases
            if case[2] == case[3]  # θ inside principal range
        ]

        type_outside = [
            case for case in all_cases
            if case[2] != case[3]  # θ outside → mapped
        ]

        selected = (
                random.sample(type_outside, 5) +
                random.sample(type_inside, 5)
        )

        questions = []

        for inv, trig, angle, answer in selected:
            question = f"What is the value of {inv}({trig}({angle}))?"

            wrong_answers = random.sample(
                [a for a in wrong_angles if a != answer], 3
            )

            questions.append({
                "question": question,
                "answer": answer,
                "wrong_answers": wrong_answers
            })

        return questions

    def inverse_find_x_all_angles_test():
        import random

        inverse_map = {
            # arcsin x = θ  →  x = sin θ
            "arcsin": {
                "-90°": "-1",
                "-60°": "-√3/2",
                "-45°": "-√2/2",
                "-30°": "-1/2",
                "0°": "0",
                "30°": "1/2",
                "45°": "√2/2",
                "60°": "√3/2",
                "90°": "1"
            },

            # arccos x = θ  →  x = cos θ
            "arccos": {
                "0°": "1",
                "30°": "√3/2",
                "45°": "√2/2",
                "60°": "1/2",
                "90°": "0",
                "120°": "-1/2",
                "135°": "-√2/2",
                "150°": "-√3/2",
                "180°": "-1"
            },

            # arctan x = θ  →  x = tan θ   (θ ≠ ±90°)
            "arctan": {
                "-60°": "-√3",
                "-45°": "-1",
                "-30°": "-1/√3",
                "0°": "0",
                "30°": "1/√3",
                "45°": "1",
                "60°": "√3"
            },

            # arccot x = θ  →  x = cot θ   (0° < θ < 180°)
            "arccot": {
                "30°": "√3",
                "45°": "1",
                "60°": "1/√3",
                "90°": "0",
                "120°": "-1/√3",
                "135°": "-1",
                "150°": "-√3"
            }
        }

        # 🔹 ALL possible x-values (used for wrong answers)
        wrong_x_pool = sorted({
            x for func in inverse_map.values() for x in func.values()
        })

        # 🔹 Build all valid questions
        all_cases = [
            (func, angle, x)
            for func, angles in inverse_map.items()
            for angle, x in angles.items()
        ]

        # exactly 5 questions
        selected = random.sample(all_cases, 5)

        questions = []

        for func, angle, correct_x in selected:
            question = f"If {func} x = {angle}, what is the value of x?"

            wrong_answers = random.sample(
                [v for v in wrong_x_pool if v != correct_x], 3
            )

            questions.append({
                "question": question,
                "answer": correct_x,
                "wrong_answers": wrong_answers
            })

        return questions

    a = inverse_trigonometry_test() + inverse_trig_composition_test() + inverse_find_x_all_angles_test()

    random.shuffle(a)
    return a


import random


def distance_between_two_points():
    labels = list("ABCDEFGHIJKLM")
    questions = []

    while len(questions) < 10:
        point_a, point_b = random.sample(labels, 2)

        for _ in range(1000):
            ax, ay = random.randint(-15, 15), random.randint(-15, 15)
            bx, by = random.randint(-15, 15), random.randint(-15, 15)

            dx, dy = bx - ax, by - ay
            answer = (dx * dx + dy * dy) ** 0.5

            if answer.is_integer():
                answer = int(answer)
                break
        else:
            continue

        wrong_answers = set()
        while len(wrong_answers) < 3:
            r = random.randint(answer - 5, answer + 5)
            if r != answer and r > 0:
                wrong_answers.add(r)

        questions.append({
            "question": f"What is the distance between point {point_a} and {point_b} "
                        f"when {point_a}=({ax},{ay}) and {point_b}=({bx},{by})?",
            "answer": answer,
            "wrong_answers": list(wrong_answers)
        })

    return questions


import random


def midpoint_between_two_points():
    labels = list("ABCDEFGHIJKLM")
    questions = []

    while len(questions) < 10:
        point_a, point_b = random.sample(labels, 2)

        ax, ay = random.randint(-20, 20), random.randint(-20, 20)
        bx, by = random.randint(-20, 20), random.randint(-20, 20)

        mx = (ax + bx) / 2
        my = (ay + by) / 2

        if int(mx) == mx:
            mx = int(mx)

        if int(my) == my:
            my = int(my)

        answer = (mx, my)

        wrong_answers = set()
        while len(wrong_answers) < 3:
            dx = random.choice([-2, -1, 1, 2])
            dy = random.choice([-2, -1, 1, 2])
            wrong = (mx + dx, my + dy)
            if wrong != answer:
                wrong_answers.add(wrong)

        questions.append({
            "question": f"What is the midpoint of points {point_a} and {point_b} "
                        f"if {point_a}=({ax},{ay}) and {point_b}=({bx},{by})?",
            "answer": answer,
            "wrong_answers": list(wrong_answers)
        })

    return questions


import random


def right_triangle_angles():
    questions = []

    while len(questions) < 5:
        given_angle = random.randint(10, 80)
        answer = 90 - given_angle

        question = (
            "In a right triangle, one acute angle is "
            f"{given_angle}°. What is the measure of the other acute angle?"
        )

        wrong_answers = set()
        while len(wrong_answers) < 3:
            w = random.randint(10, 80)
            if w != answer:
                wrong_answers.add(w)

        questions.append({
            "question": question,
            "answer": answer,
            "wrong_answers": list(wrong_answers)
        })

    return questions


import random


def right_triangle_area_perimeter():
    pythagorean_triples = [
        (3, 4, 5),
        (5, 12, 13),
        (6, 8, 10),
        (8, 15, 17),
        (9, 12, 15),
        (12, 16, 20)
    ]

    questions = []

    # ---------- AREA QUESTIONS (2) ----------
    for _ in range(5):
        a, b, c = random.choice(pythagorean_triples)

        question = (
            "Find the area of a right-angled triangle "
            f"with legs of length {a} and {b}."
        )

        answer = (a * b) // 2

        wrong_answers = set()
        while len(wrong_answers) < 3:
            w = random.randint(answer - 5, answer + 5)
            if w > 0 and w != answer:
                wrong_answers.add(w)

        questions.append({
            "question": question,
            "answer": answer,
            "wrong_answers": list(wrong_answers)
        })

    # ---------- PERIMETER QUESTIONS (2) ----------
    for _ in range(5):
        a, b, c = random.choice(pythagorean_triples)

        question = (
            "Find the perimeter of a right-angled triangle "
            f"with legs of length {a} and {b}."
        )

        # hypotenuse must be found by Pythagoras
        answer = a + b + c

        wrong_answers = set()
        while len(wrong_answers) < 3:
            w = random.randint(answer - 7, answer + 7)
            if w > 0 and w != answer:
                wrong_answers.add(w)

        questions.append({
            "question": question,
            "answer": answer,
            "wrong_answers": list(wrong_answers)
        })

    return questions


import random


def pythagoras_find_hypotenuse():
    pythagorean_triples = [
        (3, 4, 5),
        (5, 12, 13),
        (6, 8, 10),
        (8, 15, 17),
        (9, 12, 15),
        (12, 16, 20)
    ]

    questions = []

    while len(questions) < 5:
        a, b, c = random.choice(pythagorean_triples)

        question = (
            "In a right-angled triangle, the lengths of the two legs are "
            f"{a} and {b}. Find the length of the hypotenuse."
        )

        answer = c

        wrong_answers = set()
        while len(wrong_answers) < 3:
            w = random.randint(c - 4, c + 4)
            if w > 0 and w != c:
                wrong_answers.add(w)

        questions.append({
            "question": question,
            "answer": answer,
            "wrong_answers": list(wrong_answers)
        })

    return questions


import math
import random

import random


def generate_equilateral_triangle_questions():
    questions = []
    used_height_sides = []
    used_area_sides = []

    # 10 unique height questions
    while len(used_height_sides) < 10:
        side = random.randint(1, 30)
        if side not in used_height_sides:
            wrong_answers = []
            used_height_sides.append(side)
            q = f"Find the height of an equilateral triangle with side {side}."
            if int(side / 2) == side / 2:
                a = f"{int(side / 2)}√3"
            else:
                a = f"{side / 2}√3"
            while True:
                number = random.randint(int(side / 2 - 5), int(side / 2 + 5))
                wrong_answer = f'{number}√3'
                if wrong_answer not in wrong_answers and wrong_answer != a:
                    wrong_answers.append(wrong_answer)
                if len(wrong_answers) == 3:
                    break
            questions.append(
                {"question": q,
                 "answer": a,
                 "wrong_answers": wrong_answers}
            )

    # 10 unique area questions
    while len(used_area_sides) < 10:
        side = random.randint(1, 30)
        if side not in used_area_sides:
            wrong_answers2 = []
            used_area_sides.append(side)
            q = f"Find the area of an equilateral triangle with side {side}."
            if int((side ** 2) / 4) == (side ** 2) / 4:
                a = f"{int((side ** 2) / 4)}√3"
            else:
                a = f"{(side ** 2) / 4}√3"

            while True:
                number = random.randint(int(side ** 2 / 4 - 5), int(side ** 2 / 4 + 5))
                wrong_answer = f'{number}√3'
                if wrong_answer not in wrong_answers2 and wrong_answer != a:
                    wrong_answers2.append(wrong_answer)
                if len(wrong_answers2) == 3:
                    break
            questions.append({"question": q,
                              "answer": a,
                              "wrong_answers": wrong_answers2})

    return questions


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
    return data[word]
