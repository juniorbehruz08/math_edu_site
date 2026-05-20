# from django.test import TestCase


# Create your tests here.
# import random
# def return_lesson_name(word):
#     data = {'Fundamental Concepts of Mathematics': 'fundamental',
#             'Equalities and Inequalities': 'equalities_inequalities', 'Linear Equations': 'linear_equalities',
#             'Types of Numbers': 'types_of_numbers',
#             'Operations with Positive and Negative Numbers': 'working_with_signs',
#             'Fractions and Rational Numbers': 'fractions', 'Quadratic Equations': 'quadratic_equations',
#             'Inequalities': 'inequalities', 'Linear Functions': 'linear_functions',
#             'Other Types of Functions': 'other_kind_of_functions', 'Introduction to Logarithms': 'logarithm',
#             'Operations on Logarithms': 'operation_on_logarithm', 'Logarithmic Functions': 'logarithmic_functions',
#             'Introduction to Trigonometry': 'trigonometry',
#             'Trigonometric Identities and Operations': 'operations_in_trigonometry',
#             'Inverse Trigonometric Functions': 'inverse_trigonometric_functions',
#             'Introduction to Geometry': 'introduction_to_geometry',
#             'Measurement and Distance': 'measurement_and_distance', 'Angles and Their Properties': 'angles',
#             'Types of Triangles': 'triangle_types', 'Properties of Triangles': 'properties_of_triangles',
#             'Quadrilaterals': 'quadrilaterals_and_squares', 'Types of Quadrilaterals': 'types_of_quadrilateral',
#             'Basic Concepts of Circles': 'circle_basic', 'Properties of Circles': 'other_properties_of_circle',
#             'Equation of a Circle': 'equation_of_circle', 'Coordinate Plane': 'plane',
#             'Distance, Midpoint, and Slope Formulas': 'distance_midpoint_slope',
#             'The Law of Sines': 'the_laws_of_sines', 'The Law of Cosines': 'the_laws_of_cosines',
#             'Similar Triangles': 'similar_triangles'}
#     return data.va


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

# from .math_problems_json import math_problems_json
# data = math_problems_json
# total = sum(len(v) for v in data.values())
# print(total)
data = [
  {
    "question": "Use the Pythagorean identity to simplify $\\sin^2x+\\cos^2x$.",
    "answer": "$1$",
    "wrong": [
      "$0$",
      "$\\tan x$",
      "$\\sin x\\cos x$"
    ],
    "explanation": "The fundamental identity is $\\sin^2x+\\cos^2x=1$. Since the expression matches this identity exactly, it simplifies to $1$."
  },
  {
    "question": "Use $\\sin^2x+\\cos^2x=1$ to rewrite $\\sin^2x$.",
    "answer": "$1-\\cos^2x$",
    "wrong": [
      "$1+\\cos^2x$",
      "$\\cos^2x-1$",
      "$\\frac{1}{\\cos^2x}$"
    ],
    "explanation": "Subtract $\\cos^2x$ from both sides of $\\sin^2x+\\cos^2x=1$. This gives $\\sin^2x=1-\\cos^2x$."
  },
  {
    "question": "Use $\\sin^2x+\\cos^2x=1$ to rewrite $\\cos^2x$.",
    "answer": "$1-\\sin^2x$",
    "wrong": [
      "$1+\\sin^2x$",
      "$\\sin^2x-1$",
      "$\\frac{1}{\\sin^2x}$"
    ],
    "explanation": "Subtract $\\sin^2x$ from both sides of $\\sin^2x+\\cos^2x=1$. This gives $\\cos^2x=1-\\sin^2x$."
  },
  {
    "question": "Simplify $1-\\sin^2x$.",
    "answer": "$\\cos^2x$",
    "wrong": [
      "$\\sin^2x$",
      "$1+\\cos^2x$",
      "$\\tan^2x$"
    ],
    "explanation": "From $\\sin^2x+\\cos^2x=1$, we get $\\cos^2x=1-\\sin^2x$. Therefore, $1-\\sin^2x=\\cos^2x$."
  },
  {
    "question": "Simplify $1-\\cos^2x$.",
    "answer": "$\\sin^2x$",
    "wrong": [
      "$\\cos^2x$",
      "$1+\\sin^2x$",
      "$\\cot^2x$"
    ],
    "explanation": "From $\\sin^2x+\\cos^2x=1$, we get $\\sin^2x=1-\\cos^2x$. Therefore, $1-\\cos^2x=\\sin^2x$."
  },
  {
    "question": "Rewrite $\\tan x$ using sine and cosine.",
    "answer": "$\\frac{\\sin x}{\\cos x}$",
    "wrong": [
      "$\\frac{\\cos x}{\\sin x}$",
      "$\\sin x\\cos x$",
      "$\\sin^2x+\\cos^2x$"
    ],
    "explanation": "The tangent identity is $\\tan x=\\frac{\\sin x}{\\cos x}$. Sine is in the numerator and cosine is in the denominator."
  },
  {
    "question": "Rewrite $\\cot x$ using sine and cosine.",
    "answer": "$\\frac{\\cos x}{\\sin x}$",
    "wrong": [
      "$\\frac{\\sin x}{\\cos x}$",
      "$\\sin x\\cos x$",
      "$1-\\cos^2x$"
    ],
    "explanation": "The cotangent identity is $\\cot x=\\frac{\\cos x}{\\sin x}$. It is the reverse comparison of tangent."
  },
  {
    "question": "Simplify $\\tan x\\cdot\\cot x$.",
    "answer": "$1$",
    "wrong": [
      "$0$",
      "$\\tan^2x$",
      "$\\cot^2x$"
    ],
    "explanation": "The lesson gives $\\tan x\\cdot\\cot x=1$. Using sine and cosine forms, the factors cancel to $1$."
  },
  {
    "question": "Simplify $1+\\tan^2x$.",
    "answer": "$\\frac{1}{\\cos^2x}$",
    "wrong": [
      "$\\frac{1}{\\sin^2x}$",
      "$1-\\tan^2x$",
      "$\\cos^2x$"
    ],
    "explanation": "The related identity is $1+\\tan^2x=\\frac{1}{\\cos^2x}$. So the expression becomes the reciprocal of $\\cos^2x$."
  },
  {
    "question": "Simplify $1+\\cot^2x$.",
    "answer": "$\\frac{1}{\\sin^2x}$",
    "wrong": [
      "$\\frac{1}{\\cos^2x}$",
      "$1-\\cot^2x$",
      "$\\sin^2x$"
    ],
    "explanation": "The related identity is $1+\\cot^2x=\\frac{1}{\\sin^2x}$. So the expression becomes the reciprocal of $\\sin^2x$."
  },
  {
    "question": "Rewrite $\\frac{1}{\\cos^2x}-1$.",
    "answer": "$\\tan^2x$",
    "wrong": [
      "$\\cot^2x$",
      "$\\sin^2x$",
      "$\\cos^2x$"
    ],
    "explanation": "From $1+\\tan^2x=\\frac{1}{\\cos^2x}$, subtract $1$ from both sides. This gives $\\tan^2x=\\frac{1}{\\cos^2x}-1$."
  },
  {
    "question": "Rewrite $\\frac{1}{\\sin^2x}-1$.",
    "answer": "$\\cot^2x$",
    "wrong": [
      "$\\tan^2x$",
      "$\\sin^2x$",
      "$\\cos^2x$"
    ],
    "explanation": "From $1+\\cot^2x=\\frac{1}{\\sin^2x}$, subtract $1$ from both sides. This gives $\\cot^2x=\\frac{1}{\\sin^2x}-1$."
  },
  {
    "question": "If $\\cos^2x=\\frac14$, find $\\sin^2x$.",
    "answer": "$\\frac34$",
    "wrong": [
      "$\\frac14$",
      "$\\frac12$",
      "$1$"
    ],
    "explanation": "Use $\\sin^2x=1-\\cos^2x$. Then $\\sin^2x=1-\\frac14=\\frac34$."
  },
  {
    "question": "If $\\sin^2x=\\frac34$, find $\\cos^2x$.",
    "answer": "$\\frac14$",
    "wrong": [
      "$\\frac34$",
      "$\\frac12$",
      "$1$"
    ],
    "explanation": "Use $\\cos^2x=1-\\sin^2x$. Then $\\cos^2x=1-\\frac34=\\frac14$."
  },
  {
    "question": "If $\\sin^2x=\\frac{9}{25}$, find $\\cos^2x$.",
    "answer": "$\\frac{16}{25}$",
    "wrong": [
      "$\\frac{9}{25}$",
      "$\\frac{25}{16}$",
      "$\\frac45$"
    ],
    "explanation": "Use $\\cos^2x=1-\\sin^2x$. Then $\\cos^2x=1-\\frac{9}{25}=\\frac{16}{25}$."
  },
  {
    "question": "If $\\cos^2x=\\frac{16}{25}$, find $\\sin^2x$.",
    "answer": "$\\frac{9}{25}$",
    "wrong": [
      "$\\frac{16}{25}$",
      "$\\frac{25}{9}$",
      "$\\frac35$"
    ],
    "explanation": "Use $\\sin^2x=1-\\cos^2x$. Then $\\sin^2x=1-\\frac{16}{25}=\\frac{9}{25}$."
  },
  {
    "question": "If $\\sin x=\\frac35$ and $\\cos x=\\frac45$, find $\\tan x$.",
    "answer": "$\\frac34$",
    "wrong": [
      "$\\frac43$",
      "$\\frac35$",
      "$\\frac45$"
    ],
    "explanation": "Use $\\tan x=\\frac{\\sin x}{\\cos x}$. So $\\tan x=\\frac{\\frac35}{\\frac45}=\\frac34$."
  },
  {
    "question": "If $\\sin x=\\frac35$ and $\\cos x=\\frac45$, find $\\cot x$.",
    "answer": "$\\frac43$",
    "wrong": [
      "$\\frac34$",
      "$\\frac35$",
      "$\\frac45$"
    ],
    "explanation": "Use $\\cot x=\\frac{\\cos x}{\\sin x}$. So $\\cot x=\\frac{\\frac45}{\\frac35}=\\frac43$."
  },
  {
    "question": "If $\\tan x=\\frac34$, find $\\cot x$.",
    "answer": "$\\frac43$",
    "wrong": [
      "$\\frac34$",
      "$1$",
      "$\\frac74$"
    ],
    "explanation": "Since $\\tan x\\cdot\\cot x=1$, cotangent is the reciprocal-style value of tangent. Thus $\\cot x=\\frac43$."
  },
  {
    "question": "If $\\cot x=\\frac52$, find $\\tan x$.",
    "answer": "$\\frac25$",
    "wrong": [
      "$\\frac52$",
      "$1$",
      "$\\frac72$"
    ],
    "explanation": "Since $\\tan x\\cdot\\cot x=1$, tangent is the reciprocal-style value of cotangent. Thus $\\tan x=\\frac25$."
  },
  {
    "question": "Expand $\\sin(x+y)$ using the angle formula.",
    "answer": "$\\sin x\\cos y+\\cos x\\sin y$",
    "wrong": [
      "$\\sin x\\cos y-\\cos x\\sin y$",
      "$\\cos x\\cos y-\\sin x\\sin y$",
      "$\\frac{\\tan x+\\tan y}{1-\\tan x\\tan y}$"
    ],
    "explanation": "Use the sine addition formula. Sine keeps the plus sign, so $\\sin(x+y)=\\sin x\\cos y+\\cos x\\sin y$."
  },
  {
    "question": "Expand $\\sin(x-y)$ using the angle formula.",
    "answer": "$\\sin x\\cos y-\\cos x\\sin y$",
    "wrong": [
      "$\\sin x\\cos y+\\cos x\\sin y$",
      "$\\cos x\\cos y+\\sin x\\sin y$",
      "$\\frac{\\tan x-\\tan y}{1+\\tan x\\tan y}$"
    ],
    "explanation": "Use the sine subtraction formula. Sine keeps the minus sign, so $\\sin(x-y)=\\sin x\\cos y-\\cos x\\sin y$."
  },
  {
    "question": "Expand $\\cos(x+y)$ using the angle formula.",
    "answer": "$\\cos x\\cos y-\\sin x\\sin y$",
    "wrong": [
      "$\\cos x\\cos y+\\sin x\\sin y$",
      "$\\sin x\\cos y+\\cos x\\sin y$",
      "$\\frac{\\tan x+\\tan y}{1-\\tan x\\tan y}$"
    ],
    "explanation": "Use the cosine addition formula. Cosine changes the sign, so $\\cos(x+y)=\\cos x\\cos y-\\sin x\\sin y$."
  },
  {
    "question": "Expand $\\cos(x-y)$ using the angle formula.",
    "answer": "$\\cos x\\cos y+\\sin x\\sin y$",
    "wrong": [
      "$\\cos x\\cos y-\\sin x\\sin y$",
      "$\\sin x\\cos y-\\cos x\\sin y$",
      "$\\frac{\\tan x-\\tan y}{1+\\tan x\\tan y}$"
    ],
    "explanation": "Use the cosine subtraction formula. Cosine changes the sign, so $\\cos(x-y)=\\cos x\\cos y+\\sin x\\sin y$."
  },
  {
    "question": "Expand $\\tan(x+y)$ using the angle formula.",
    "answer": "$\\frac{\\tan x+\\tan y}{1-\\tan x\\tan y}$",
    "wrong": [
      "$\\frac{\\tan x-\\tan y}{1+\\tan x\\tan y}$",
      "$\\tan x+\\tan y$",
      "$\\frac{\\tan x+\\tan y}{1+\\tan x\\tan y}$"
    ],
    "explanation": "Use the tangent addition formula. The numerator has plus, and the denominator is $1-\\tan x\\tan y$."
  },
  {
    "question": "Expand $\\tan(x-y)$ using the angle formula.",
    "answer": "$\\frac{\\tan x-\\tan y}{1+\\tan x\\tan y}$",
    "wrong": [
      "$\\frac{\\tan x+\\tan y}{1-\\tan x\\tan y}$",
      "$\\tan x-\\tan y$",
      "$\\frac{\\tan x-\\tan y}{1-\\tan x\\tan y}$"
    ],
    "explanation": "Use the tangent subtraction formula. The numerator has minus, and the denominator is $1+\\tan x\\tan y$."
  },
  {
    "question": "Expand $\\sin(a+b)$ using the angle formula.",
    "answer": "$\\sin a\\cos b+\\cos a\\sin b$",
    "wrong": [
      "$\\sin a\\cos b-\\cos a\\sin b$",
      "$\\cos a\\cos b-\\sin a\\sin b$",
      "$\\cos a\\cos b+\\sin a\\sin b$"
    ],
    "explanation": "Replace $x,y$ with $a,b$ in the sine addition formula. The correct expansion is $\\sin a\\cos b+\\cos a\\sin b$."
  },
  {
    "question": "Expand $\\sin(a-b)$ using the angle formula.",
    "answer": "$\\sin a\\cos b-\\cos a\\sin b$",
    "wrong": [
      "$\\sin a\\cos b+\\cos a\\sin b$",
      "$\\cos a\\cos b+\\sin a\\sin b$",
      "$\\cos a\\cos b-\\sin a\\sin b$"
    ],
    "explanation": "Replace $x,y$ with $a,b$ in the sine subtraction formula. The correct expansion is $\\sin a\\cos b-\\cos a\\sin b$."
  },
  {
    "question": "Expand $\\cos(a+b)$ using the angle formula.",
    "answer": "$\\cos a\\cos b-\\sin a\\sin b$",
    "wrong": [
      "$\\cos a\\cos b+\\sin a\\sin b$",
      "$\\sin a\\cos b+\\cos a\\sin b$",
      "$\\sin a\\cos b-\\cos a\\sin b$"
    ],
    "explanation": "Replace $x,y$ with $a,b$ in the cosine addition formula. The sign changes to minus."
  },
  {
    "question": "Expand $\\cos(a-b)$ using the angle formula.",
    "answer": "$\\cos a\\cos b+\\sin a\\sin b$",
    "wrong": [
      "$\\cos a\\cos b-\\sin a\\sin b$",
      "$\\sin a\\cos b-\\cos a\\sin b$",
      "$\\sin a\\cos b+\\cos a\\sin b$"
    ],
    "explanation": "Replace $x,y$ with $a,b$ in the cosine subtraction formula. The sign changes to plus."
  },
  {
    "question": "Set up $\\sin75^\\circ$ using $45^\\circ+30^\\circ$.",
    "answer": "$\\sin45^\\circ\\cos30^\\circ+\\cos45^\\circ\\sin30^\\circ$",
    "wrong": [
      "$\\sin45^\\circ\\cos30^\\circ-\\cos45^\\circ\\sin30^\\circ$",
      "$\\cos45^\\circ\\cos30^\\circ-\\sin45^\\circ\\sin30^\\circ$",
      "$\\frac{\\tan45^\\circ+\\tan30^\\circ}{1-\\tan45^\\circ\\tan30^\\circ}$"
    ],
    "explanation": "$75^\\circ=45^\\circ+30^\\circ$. Apply $\\sin(x+y)=\\sin x\\cos y+\\cos x\\sin y$."
  },
  {
    "question": "Set up $\\sin15^\\circ$ using $45^\\circ-30^\\circ$.",
    "answer": "$\\sin45^\\circ\\cos30^\\circ-\\cos45^\\circ\\sin30^\\circ$",
    "wrong": [
      "$\\sin45^\\circ\\cos30^\\circ+\\cos45^\\circ\\sin30^\\circ$",
      "$\\cos45^\\circ\\cos30^\\circ+\\sin45^\\circ\\sin30^\\circ$",
      "$\\frac{\\tan45^\\circ-\\tan30^\\circ}{1+\\tan45^\\circ\\tan30^\\circ}$"
    ],
    "explanation": "$15^\\circ=45^\\circ-30^\\circ$. Apply $\\sin(x-y)=\\sin x\\cos y-\\cos x\\sin y$."
  },
  {
    "question": "Set up $\\cos75^\\circ$ using $45^\\circ+30^\\circ$.",
    "answer": "$\\cos45^\\circ\\cos30^\\circ-\\sin45^\\circ\\sin30^\\circ$",
    "wrong": [
      "$\\cos45^\\circ\\cos30^\\circ+\\sin45^\\circ\\sin30^\\circ$",
      "$\\sin45^\\circ\\cos30^\\circ+\\cos45^\\circ\\sin30^\\circ$",
      "$\\frac{\\tan45^\\circ+\\tan30^\\circ}{1-\\tan45^\\circ\\tan30^\\circ}$"
    ],
    "explanation": "$75^\\circ=45^\\circ+30^\\circ$. Apply $\\cos(x+y)=\\cos x\\cos y-\\sin x\\sin y$."
  },
  {
    "question": "Set up $\\cos15^\\circ$ using $45^\\circ-30^\\circ$.",
    "answer": "$\\cos45^\\circ\\cos30^\\circ+\\sin45^\\circ\\sin30^\\circ$",
    "wrong": [
      "$\\cos45^\\circ\\cos30^\\circ-\\sin45^\\circ\\sin30^\\circ$",
      "$\\sin45^\\circ\\cos30^\\circ-\\cos45^\\circ\\sin30^\\circ$",
      "$\\frac{\\tan45^\\circ-\\tan30^\\circ}{1+\\tan45^\\circ\\tan30^\\circ}$"
    ],
    "explanation": "$15^\\circ=45^\\circ-30^\\circ$. Apply $\\cos(x-y)=\\cos x\\cos y+\\sin x\\sin y$."
  },
  {
    "question": "According to the lesson example, what is $\\sin75^\\circ$?",
    "answer": "$\\frac{\\sqrt6+\\sqrt2}{4}$",
    "wrong": [
      "$\\frac{\\sqrt6-\\sqrt2}{4}$",
      "$2+\\sqrt3$",
      "$2-\\sqrt3$"
    ],
    "explanation": "The lesson uses $75^\\circ=45^\\circ+30^\\circ$ and the sine addition formula. Substitution gives $\\frac{\\sqrt6+\\sqrt2}{4}$."
  },
  {
    "question": "According to the lesson example, what is $\\sin15^\\circ$?",
    "answer": "$\\frac{\\sqrt6-\\sqrt2}{4}$",
    "wrong": [
      "$\\frac{\\sqrt6+\\sqrt2}{4}$",
      "$2+\\sqrt3$",
      "$2-\\sqrt3$"
    ],
    "explanation": "The lesson uses $15^\\circ=45^\\circ-30^\\circ$ and the sine subtraction formula. The result is $\\frac{\\sqrt6-\\sqrt2}{4}$."
  },
  {
    "question": "According to the lesson example, what is $\\cos75^\\circ$?",
    "answer": "$\\frac{\\sqrt6-\\sqrt2}{4}$",
    "wrong": [
      "$\\frac{\\sqrt6+\\sqrt2}{4}$",
      "$2+\\sqrt3$",
      "$2-\\sqrt3$"
    ],
    "explanation": "The lesson uses the cosine addition formula for $45^\\circ+30^\\circ$. The simplified value is $\\frac{\\sqrt6-\\sqrt2}{4}$."
  },
  {
    "question": "According to the lesson example, what is $\\cos15^\\circ$?",
    "answer": "$\\frac{\\sqrt6+\\sqrt2}{4}$",
    "wrong": [
      "$\\frac{\\sqrt6-\\sqrt2}{4}$",
      "$2+\\sqrt3$",
      "$2-\\sqrt3$"
    ],
    "explanation": "The lesson uses the cosine subtraction formula for $45^\\circ-30^\\circ$. The simplified value is $\\frac{\\sqrt6+\\sqrt2}{4}$."
  },
  {
    "question": "According to the lesson example, what is $\\tan75^\\circ$?",
    "answer": "$2+\\sqrt3$",
    "wrong": [
      "$2-\\sqrt3$",
      "$\\frac{\\sqrt6+\\sqrt2}{4}$",
      "$\\frac{\\sqrt6-\\sqrt2}{4}$"
    ],
    "explanation": "The lesson applies the tangent addition formula to $45^\\circ+30^\\circ$. After simplification, the result is $2+\\sqrt3$."
  },
  {
    "question": "According to the lesson example, what is $\\tan15^\\circ$?",
    "answer": "$2-\\sqrt3$",
    "wrong": [
      "$2+\\sqrt3$",
      "$\\frac{\\sqrt6+\\sqrt2}{4}$",
      "$\\frac{\\sqrt6-\\sqrt2}{4}$"
    ],
    "explanation": "The lesson applies the tangent subtraction formula to $45^\\circ-30^\\circ$. After simplification, the result is $2-\\sqrt3$."
  },
  {
    "question": "Which function keeps the same sign in the addition/subtraction formulas?",
    "answer": "Sine",
    "wrong": [
      "Cosine",
      "Tangent",
      "Cotangent"
    ],
    "explanation": "The lesson's memory note says sine keeps the same sign as the angle operation. So plus stays plus and minus stays minus."
  },
  {
    "question": "Which function changes the sign in the addition/subtraction formulas?",
    "answer": "Cosine",
    "wrong": [
      "Sine",
      "Tangent",
      "Cotangent"
    ],
    "explanation": "The lesson's memory note says cosine changes the sign. So cosine of a sum uses minus, while cosine of a difference uses plus."
  },
  {
    "question": "Set up $\\tan(60^\\circ-30^\\circ)$ using the tangent subtraction formula.",
    "answer": "$\\frac{\\tan60^\\circ-\\tan30^\\circ}{1+\\tan60^\\circ\\tan30^\\circ}$",
    "wrong": [
      "$\\frac{\\tan60^\\circ+\\tan30^\\circ}{1-\\tan60^\\circ\\tan30^\\circ}$",
      "$\\tan60^\\circ-\\tan30^\\circ$",
      "$\\frac{\\tan60^\\circ-\\tan30^\\circ}{1-\\tan60^\\circ\\tan30^\\circ}$"
    ],
    "explanation": "The tangent difference formula is $\\frac{\\tan x-\\tan y}{1+\\tan x\\tan y}$. Substitute $60^\\circ$ and $30^\\circ$."
  },
  {
    "question": "Set up $\\tan(45^\\circ+45^\\circ)$ using the tangent addition formula.",
    "answer": "$\\frac{\\tan45^\\circ+\\tan45^\\circ}{1-\\tan45^\\circ\\tan45^\\circ}$",
    "wrong": [
      "$\\frac{\\tan45^\\circ-\\tan45^\\circ}{1+\\tan45^\\circ\\tan45^\\circ}$",
      "$\\tan45^\\circ+\\tan45^\\circ$",
      "$\\frac{\\tan45^\\circ+\\tan45^\\circ}{1+\\tan45^\\circ\\tan45^\\circ}$"
    ],
    "explanation": "The tangent sum formula is $\\frac{\\tan x+\\tan y}{1-\\tan x\\tan y}$. Here both angles are $45^\\circ$."
  },
  {
    "question": "Rewrite $\\sin(2x)$ using a double-angle formula.",
    "answer": "$2\\sin x\\cos x$",
    "wrong": [
      "$\\cos^2x-\\sin^2x$",
      "$2\\cos^2x-1$",
      "$\\frac{2\\tan x}{1-\\tan^2x}$"
    ],
    "explanation": "$\\sin(2x)=2\\sin x\\cos x$ is the sine double-angle formula."
  },
  {
    "question": "Rewrite $\\cos(2x)$ as cosine squared minus sine squared.",
    "answer": "$\\cos^2x-\\sin^2x$",
    "wrong": [
      "$2\\sin x\\cos x$",
      "$2\\cos^2x+1$",
      "$1+2\\sin^2x$"
    ],
    "explanation": "One cosine double-angle formula is $\\cos(2x)=\\cos^2x-\\sin^2x$."
  },
  {
    "question": "Rewrite $\\cos(2x)$ using only $\\cos^2x$.",
    "answer": "$2\\cos^2x-1$",
    "wrong": [
      "$1-2\\cos^2x$",
      "$2\\sin^2x-1$",
      "$2\\sin x\\cos x$"
    ],
    "explanation": "The cosine double-angle form using only cosine is $\\cos(2x)=2\\cos^2x-1$."
  },
  {
    "question": "Rewrite $\\cos(2x)$ using only $\\sin^2x$.",
    "answer": "$1-2\\sin^2x$",
    "wrong": [
      "$2\\sin^2x-1$",
      "$2\\cos^2x-1$",
      "$2\\sin x\\cos x$"
    ],
    "explanation": "The cosine double-angle form using only sine is $\\cos(2x)=1-2\\sin^2x$."
  },
  {
    "question": "Rewrite $\\tan(2x)$ using a double-angle formula.",
    "answer": "$\\frac{2\\tan x}{1-\\tan^2x}$",
    "wrong": [
      "$\\frac{\\tan x+\\tan y}{1-\\tan x\\tan y}$",
      "$\\frac{\\cot^2x-1}{2\\cot x}$",
      "$2\\sin x\\cos x$"
    ],
    "explanation": "$\\tan(2x)=\\frac{2\\tan x}{1-\\tan^2x}$ is the tangent double-angle formula."
  },
  {
    "question": "Rewrite $\\cot(2x)$ using a double-angle formula.",
    "answer": "$\\frac{\\cot^2x-1}{2\\cot x}$",
    "wrong": [
      "$\\frac{2\\tan x}{1-\\tan^2x}$",
      "$2\\sin x\\cos x$",
      "$\\cos^2x-\\sin^2x$"
    ],
    "explanation": "$\\cot(2x)=\\frac{\\cot^2x-1}{2\\cot x}$ is the cotangent double-angle formula."
  },
  {
    "question": "Rewrite $\\sin(2a)$ using a double-angle formula.",
    "answer": "$2\\sin a\\cos a$",
    "wrong": [
      "$\\sin^2a+\\cos^2a$",
      "$\\cos^2a-\\sin^2a$",
      "$2\\cos^2a-1$"
    ],
    "explanation": "Replace $x$ with $a$ in $\\sin(2x)=2\\sin x\\cos x$."
  },
  {
    "question": "Rewrite $\\cos(2a)$ as cosine squared minus sine squared.",
    "answer": "$\\cos^2a-\\sin^2a$",
    "wrong": [
      "$2\\sin a\\cos a$",
      "$2\\cos^2a+1$",
      "$1+2\\sin^2a$"
    ],
    "explanation": "Replace $x$ with $a$ in $\\cos(2x)=\\cos^2x-\\sin^2x$."
  },
  {
    "question": "Rewrite $\\tan(2a)$ using a double-angle formula.",
    "answer": "$\\frac{2\\tan a}{1-\\tan^2a}$",
    "wrong": [
      "$\\frac{2\\tan a}{1+\\tan^2a}$",
      "$\\tan^2a-1$",
      "$\\frac{\\cot^2a-1}{2\\cot a}$"
    ],
    "explanation": "Replace $x$ with $a$ in $\\tan(2x)=\\frac{2\\tan x}{1-\\tan^2x}$."
  },
  {
    "question": "Rewrite $\\cot(2a)$ using a double-angle formula.",
    "answer": "$\\frac{\\cot^2a-1}{2\\cot a}$",
    "wrong": [
      "$\\frac{2\\tan a}{1-\\tan^2a}$",
      "$2\\sin a\\cos a$",
      "$\\frac{\\cot a+1}{2\\cot a}$"
    ],
    "explanation": "Replace $x$ with $a$ in $\\cot(2x)=\\frac{\\cot^2x-1}{2\\cot x}$."
  },
  {
    "question": "Write $\\sin60^\\circ$ using $30^\\circ$ and the sine double-angle formula.",
    "answer": "$2\\sin30^\\circ\\cos30^\\circ$",
    "wrong": [
      "$\\cos^230^\\circ-\\sin^230^\\circ$",
      "$2\\cos^230^\\circ-1$",
      "$\\frac{2\\tan30^\\circ}{1-\\tan^230^\\circ}$"
    ],
    "explanation": "Since $60^\\circ=2\\cdot30^\\circ$, substitute $x=30^\\circ$ into $\\sin(2x)=2\\sin x\\cos x$."
  },
  {
    "question": "Write $\\cos60^\\circ$ using $\\cos^2 30^\\circ-\\sin^2 30^\\circ$.",
    "answer": "$\\cos^230^\\circ-\\sin^230^\\circ$",
    "wrong": [
      "$2\\sin30^\\circ\\cos30^\\circ$",
      "$1-2\\cos^230^\\circ$",
      "$\\frac{2\\tan30^\\circ}{1-\\tan^230^\\circ}$"
    ],
    "explanation": "Use $\\cos(2x)=\\cos^2x-\\sin^2x$ with $x=30^\\circ$."
  },
  {
    "question": "Write $\\cos60^\\circ$ using $2\\cos^230^\\circ-1$.",
    "answer": "$2\\cos^230^\\circ-1$",
    "wrong": [
      "$1-2\\cos^230^\\circ$",
      "$2\\sin^230^\\circ-1$",
      "$2\\sin30^\\circ\\cos30^\\circ$"
    ],
    "explanation": "Use $\\cos(2x)=2\\cos^2x-1$ with $x=30^\\circ$."
  },
  {
    "question": "Write $\\cos60^\\circ$ using $1-2\\sin^230^\\circ$.",
    "answer": "$1-2\\sin^230^\\circ$",
    "wrong": [
      "$2\\sin^230^\\circ-1$",
      "$2\\cos^230^\\circ-1$",
      "$2\\sin30^\\circ\\cos30^\\circ$"
    ],
    "explanation": "Use $\\cos(2x)=1-2\\sin^2x$ with $x=30^\\circ$."
  },
  {
    "question": "According to the lesson, what is $\\sin60^\\circ$ from the double-angle example?",
    "answer": "$\\frac{\\sqrt3}{2}$",
    "wrong": [
      "$\\frac12$",
      "$\\frac{\\sqrt3}{3}$",
      "$1$"
    ],
    "explanation": "The lesson evaluates $2\\sin30^\\circ\\cos30^\\circ=2\\cdot\\frac12\\cdot\\frac{\\sqrt3}{2}=\\frac{\\sqrt3}{2}$."
  },
  {
    "question": "According to the lesson, what is $\\cos60^\\circ$ from the double-angle examples?",
    "answer": "$\\frac12$",
    "wrong": [
      "$\\frac{\\sqrt3}{2}$",
      "$\\frac14$",
      "$1$"
    ],
    "explanation": "The lesson shows that each cosine double-angle form for $60^\\circ$ simplifies to $\\frac12$."
  },
  {
    "question": "According to the lesson, what is $\\tan60^\\circ$ from the double-angle example?",
    "answer": "$\\sqrt3$",
    "wrong": [
      "$\\frac{\\sqrt3}{3}$",
      "$1$",
      "$\\frac12$"
    ],
    "explanation": "The lesson applies $\\tan(2x)=\\frac{2\\tan x}{1-\\tan^2x}$ with $x=30^\\circ$ and simplifies to $\\sqrt3$."
  },
  {
    "question": "According to the lesson, what is $\\cot60^\\circ$ from the double-angle example?",
    "answer": "$\\frac{\\sqrt3}{3}$",
    "wrong": [
      "$\\sqrt3$",
      "$1$",
      "$\\frac12$"
    ],
    "explanation": "The lesson applies $\\cot(2x)=\\frac{\\cot^2x-1}{2\\cot x}$ with $x=30^\\circ$ and simplifies to $\\frac{\\sqrt3}{3}$."
  },
  {
    "question": "Which identity helps derive $\\cos(2x)=2\\cos^2x-1$?",
    "answer": "$\\sin^2x+\\cos^2x=1$",
    "wrong": [
      "$\\tan x=\\frac{\\sin x}{\\cos x}$",
      "$\\cot x=\\frac{\\cos x}{\\sin x}$",
      "$\\tan x\\cdot\\cot x=1$"
    ],
    "explanation": "The derivation replaces $\\sin^2x$ with $1-\\cos^2x$, which comes from the Pythagorean identity."
  },
  {
    "question": "In the derivation of $\\cos(2x)=2\\cos^2x-1$, what replaces $\\sin^2x$?",
    "answer": "$1-\\cos^2x$",
    "wrong": [
      "$1+\\cos^2x$",
      "$\\cos^2x-1$",
      "$\\frac{1}{\\cos^2x}$"
    ],
    "explanation": "From $\\sin^2x+\\cos^2x=1$, isolating $\\sin^2x$ gives $\\sin^2x=1-\\cos^2x$."
  },
  {
    "question": "Simplify $\\cos^2x-(1-\\cos^2x)$.",
    "answer": "$2\\cos^2x-1$",
    "wrong": [
      "$1$",
      "$1-2\\cos^2x$",
      "$2\\sin^2x-1$"
    ],
    "explanation": "Distribute the negative: $\\cos^2x-1+\\cos^2x=2\\cos^2x-1$."
  },
  {
    "question": "Which expression is NOT one of the cosine double-angle formulas in the lesson?",
    "answer": "$\\cos(2x)=2\\sin^2x-1$",
    "wrong": [
      "$\\cos(2x)=\\cos^2x-\\sin^2x$",
      "$\\cos(2x)=2\\cos^2x-1$",
      "$\\cos(2x)=1-2\\sin^2x$"
    ],
    "explanation": "The lesson lists $\\cos^2x-\\sin^2x$, $2\\cos^2x-1$, and $1-2\\sin^2x$. The expression $2\\sin^2x-1$ reverses the sign order."
  },
  {
    "question": "Rewrite $\\sin\\frac{x}{2}$ using a half-angle formula.",
    "answer": "$\\pm\\sqrt{\\frac{1-\\cos x}{2}}$",
    "wrong": [
      "$\\pm\\sqrt{\\frac{1+\\cos x}{2}}$",
      "$\\frac{\\sin x}{1+\\cos x}$",
      "$\\frac{1-\\cos x}{\\sin x}$"
    ],
    "explanation": "The sine half-angle formula is $\\sin\\frac{x}{2}=\\pm\\sqrt{\\frac{1-\\cos x}{2}}$. The sign depends on the quadrant of the half-angle."
  },
  {
    "question": "Rewrite $\\cos\\frac{x}{2}$ using a half-angle formula.",
    "answer": "$\\pm\\sqrt{\\frac{1+\\cos x}{2}}$",
    "wrong": [
      "$\\pm\\sqrt{\\frac{1-\\cos x}{2}}$",
      "$\\frac{\\sin x}{1+\\cos x}$",
      "$\\frac{1-\\cos x}{\\sin x}$"
    ],
    "explanation": "The cosine half-angle formula is $\\cos\\frac{x}{2}=\\pm\\sqrt{\\frac{1+\\cos x}{2}}$. The sign depends on the quadrant of the half-angle."
  },
  {
    "question": "Rewrite $\\tan\\frac{x}{2}$ using $\\sin x$ and $1+\\cos x$.",
    "answer": "$\\frac{\\sin x}{1+\\cos x}$",
    "wrong": [
      "$\\frac{1-\\cos x}{\\sin x}$",
      "$\\pm\\sqrt{\\frac{1-\\cos x}{2}}$",
      "$\\pm\\sqrt{\\frac{1+\\cos x}{2}}$"
    ],
    "explanation": "One tangent half-angle formula is $\\tan\\frac{x}{2}=\\frac{\\sin x}{1+\\cos x}$. This form is useful when $1+\\cos x\\ne0$."
  },
  {
    "question": "Rewrite $\\tan\\frac{x}{2}$ using $1-\\cos x$ and $\\sin x$.",
    "answer": "$\\frac{1-\\cos x}{\\sin x}$",
    "wrong": [
      "$\\frac{\\sin x}{1+\\cos x}$",
      "$\\pm\\sqrt{\\frac{1-\\cos x}{2}}$",
      "$\\pm\\sqrt{\\frac{1+\\cos x}{2}}$"
    ],
    "explanation": "Another tangent half-angle formula is $\\tan\\frac{x}{2}=\\frac{1-\\cos x}{\\sin x}$. This form is useful when $\\sin x\\ne0$."
  },
  {
    "question": "What determines the sign in $\\sin\\frac{x}{2}=\\pm\\sqrt{\\frac{1-\\cos x}{2}}$?",
    "answer": "The quadrant of $\\frac{x}{2}$",
    "wrong": [
      "The quadrant of $x$ only",
      "The value of $\\tan x$ only",
      "The denominator only"
    ],
    "explanation": "The lesson warns that the $\\pm$ sign must be chosen based on where the half-angle $\\frac{x}{2}$ lies."
  },
  {
    "question": "What determines the sign in $\\cos\\frac{x}{2}=\\pm\\sqrt{\\frac{1+\\cos x}{2}}$?",
    "answer": "The quadrant of $\\frac{x}{2}$",
    "wrong": [
      "The quadrant of $x$ only",
      "The value of $\\tan x$ only",
      "The numerator only"
    ],
    "explanation": "The correct sign in the cosine half-angle formula depends on the quadrant of the half-angle $\\frac{x}{2}$."
  },
  {
    "question": "Set up $\\sin15^\\circ$ using the half-angle formula with $30^\\circ$.",
    "answer": "$\\sqrt{\\frac{1-\\cos30^\\circ}{2}}$",
    "wrong": [
      "$\\sqrt{\\frac{1+\\cos30^\\circ}{2}}$",
      "$\\frac{\\sin30^\\circ}{1-\\cos30^\\circ}$",
      "$\\frac{1+\\cos30^\\circ}{\\sin30^\\circ}$"
    ],
    "explanation": "Since $15^\\circ$ is half of $30^\\circ$, use $\\sin\\frac{x}{2}=\\pm\\sqrt{\\frac{1-\\cos x}{2}}$ with $x=30^\\circ$."
  },
  {
    "question": "Set up $\\cos15^\\circ$ using the half-angle formula with $30^\\circ$.",
    "answer": "$\\sqrt{\\frac{1+\\cos30^\\circ}{2}}$",
    "wrong": [
      "$\\sqrt{\\frac{1-\\cos30^\\circ}{2}}$",
      "$\\frac{\\sin30^\\circ}{1+\\cos30^\\circ}$",
      "$\\frac{1-\\cos30^\\circ}{\\sin30^\\circ}$"
    ],
    "explanation": "Since $15^\\circ$ is half of $30^\\circ$, use $\\cos\\frac{x}{2}=\\pm\\sqrt{\\frac{1+\\cos x}{2}}$ with $x=30^\\circ$."
  },
  {
    "question": "Set up $\\tan15^\\circ$ using $\\tan\\frac{x}{2}=\\frac{\\sin x}{1+\\cos x}$.",
    "answer": "$\\frac{\\sin30^\\circ}{1+\\cos30^\\circ}$",
    "wrong": [
      "$\\frac{1-\\cos30^\\circ}{1+\\sin30^\\circ}$",
      "$\\sqrt{\\frac{1-\\cos30^\\circ}{2}}$",
      "$\\frac{\\sin30^\\circ}{1-\\cos30^\\circ}$"
    ],
    "explanation": "Because $15^\\circ=\\frac{30^\\circ}{2}$, substitute $x=30^\\circ$ into the formula."
  },
  {
    "question": "Set up $\\tan15^\\circ$ using $\\tan\\frac{x}{2}=\\frac{1-\\cos x}{\\sin x}$.",
    "answer": "$\\frac{1-\\cos30^\\circ}{\\sin30^\\circ}$",
    "wrong": [
      "$\\frac{\\sin30^\\circ}{1-\\cos30^\\circ}$",
      "$\\sqrt{\\frac{1+\\cos30^\\circ}{2}}$",
      "$\\frac{1+\\cos30^\\circ}{\\sin30^\\circ}$"
    ],
    "explanation": "Because $15^\\circ=\\frac{30^\\circ}{2}$, substitute $x=30^\\circ$ into the second tangent half-angle formula."
  },
  {
    "question": "According to the lesson example, what does $\\tan15^\\circ$ simplify to using half-angle formulas?",
    "answer": "$2-\\sqrt3$",
    "wrong": [
      "$2+\\sqrt3$",
      "$\\frac{\\sqrt6+\\sqrt2}{4}$",
      "$\\frac{\\sqrt6-\\sqrt2}{4}$"
    ],
    "explanation": "Both tangent half-angle forms shown in the lesson simplify to $2-\\sqrt3$ for $15^\\circ$."
  },
  {
    "question": "Which double-angle identity is used to derive the sine half-angle formula?",
    "answer": "$\\cos(2u)=1-2\\sin^2u$",
    "wrong": [
      "$\\sin(2u)=2\\sin u\\cos u$",
      "$\\cos(2u)=2\\cos^2u-1$",
      "$\\tan(2u)=\\frac{2\\tan u}{1-\\tan^2u}$"
    ],
    "explanation": "The lesson derives the sine half-angle formula from $\\cos(2u)=1-2\\sin^2u$."
  },
  {
    "question": "From $\\cos(2u)=1-2\\sin^2u$, what is $\\sin^2\\frac{x}{2}$?",
    "answer": "$\\frac{1-\\cos x}{2}$",
    "wrong": [
      "$\\frac{1+\\cos x}{2}$",
      "$1-\\cos^2x$",
      "$\\frac{\\sin x}{1+\\cos x}$"
    ],
    "explanation": "Let $u=\\frac{x}{2}$, so $2u=x$. Solving gives $\\sin^2\\frac{x}{2}=\\frac{1-\\cos x}{2}$."
  },
  {
    "question": "If $u=\\frac{x}{2}$, then $2u$ equals what?",
    "answer": "$x$",
    "wrong": [
      "$\\frac{x}{4}$",
      "$2x$",
      "$x^2$"
    ],
    "explanation": "Multiplying $u=\\frac{x}{2}$ by $2$ gives $2u=x$. This is why $\\cos(2u)$ becomes $\\cos x$ in the derivation."
  },
  {
    "question": "From $\\sin^2\\frac{x}{2}=\\frac{1-\\cos x}{2}$, what operation gives $\\sin\\frac{x}{2}$?",
    "answer": "Taking the square root",
    "wrong": [
      "Adding $1$",
      "Multiplying by $2$",
      "Changing sine to cosine"
    ],
    "explanation": "To move from $\\sin^2\\frac{x}{2}$ to $\\sin\\frac{x}{2}$, take the square root. This also creates the $\\pm$ sign."
  },
  {
    "question": "Rewrite $\\sin\\frac{a}{2}$ using a half-angle formula.",
    "answer": "$\\pm\\sqrt{\\frac{1-\\cos a}{2}}$",
    "wrong": [
      "$\\pm\\sqrt{\\frac{1+\\cos a}{2}}$",
      "$\\frac{\\sin a}{1+\\cos a}$",
      "$\\frac{1-\\cos a}{\\sin a}$"
    ],
    "explanation": "Replace $x$ with $a$ in the sine half-angle formula."
  },
  {
    "question": "Rewrite $\\cos\\frac{a}{2}$ using a half-angle formula.",
    "answer": "$\\pm\\sqrt{\\frac{1+\\cos a}{2}}$",
    "wrong": [
      "$\\pm\\sqrt{\\frac{1-\\cos a}{2}}$",
      "$\\frac{\\sin a}{1+\\cos a}$",
      "$\\frac{1-\\cos a}{\\sin a}$"
    ],
    "explanation": "Replace $x$ with $a$ in the cosine half-angle formula."
  },
  {
    "question": "Rewrite $\\tan\\frac{a}{2}$ using $1+\\cos a$.",
    "answer": "$\\frac{\\sin a}{1+\\cos a}$",
    "wrong": [
      "$\\frac{1-\\cos a}{\\sin a}$",
      "$\\pm\\sqrt{\\frac{1-\\cos a}{2}}$",
      "$\\pm\\sqrt{\\frac{1+\\cos a}{2}}$"
    ],
    "explanation": "Replace $x$ with $a$ in $\\tan\\frac{x}{2}=\\frac{\\sin x}{1+\\cos x}$."
  },
  {
    "question": "Rewrite $\\tan\\frac{a}{2}$ using $1-\\cos a$.",
    "answer": "$\\frac{1-\\cos a}{\\sin a}$",
    "wrong": [
      "$\\frac{\\sin a}{1+\\cos a}$",
      "$\\pm\\sqrt{\\frac{1-\\cos a}{2}}$",
      "$\\pm\\sqrt{\\frac{1+\\cos a}{2}}$"
    ],
    "explanation": "Replace $x$ with $a$ in $\\tan\\frac{x}{2}=\\frac{1-\\cos x}{\\sin x}$."
  },
  {
    "question": "Which condition belongs to $\\tan\\frac{x}{2}=\\frac{\\sin x}{1+\\cos x}$?",
    "answer": "$1+\\cos x\\ne0$",
    "wrong": [
      "$\\sin x\\ne0$",
      "$\\cos x=0$",
      "$\\tan x=0$"
    ],
    "explanation": "The denominator is $1+\\cos x$, so the lesson notes that this form is useful when $1+\\cos x\\ne0$."
  },
  {
    "question": "Which condition belongs to $\\tan\\frac{x}{2}=\\frac{1-\\cos x}{\\sin x}$?",
    "answer": "$\\sin x\\ne0$",
    "wrong": [
      "$1+\\cos x\\ne0$",
      "$\\cos x=0$",
      "$\\tan x=0$"
    ],
    "explanation": "The denominator is $\\sin x$, so the lesson notes that this form is useful when $\\sin x\\ne0$."
  },
  {
    "question": "Use product-to-sum to rewrite $\\sin x\\sin y$.",
    "answer": "$\\frac12[\\cos(x-y)-\\cos(x+y)]$",
    "wrong": [
      "$\\frac12[\\cos(x-y)+\\cos(x+y)]$",
      "$\\frac12[\\sin(x+y)+\\sin(x-y)]$",
      "$2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$"
    ],
    "explanation": "The product-to-sum formula for two sines is $\\sin x\\sin y=\\frac12[\\cos(x-y)-\\cos(x+y)]$."
  },
  {
    "question": "Use product-to-sum to rewrite $\\cos x\\cos y$.",
    "answer": "$\\frac12[\\cos(x-y)+\\cos(x+y)]$",
    "wrong": [
      "$\\frac12[\\cos(x-y)-\\cos(x+y)]$",
      "$\\frac12[\\sin(x+y)-\\sin(x-y)]$",
      "$2\\cos\\frac{x+y}{2}\\cos\\frac{x-y}{2}$"
    ],
    "explanation": "The product-to-sum formula for two cosines is $\\cos x\\cos y=\\frac12[\\cos(x-y)+\\cos(x+y)]$."
  },
  {
    "question": "Use product-to-sum to rewrite $\\sin x\\cos y$.",
    "answer": "$\\frac12[\\sin(x+y)+\\sin(x-y)]$",
    "wrong": [
      "$\\frac12[\\sin(x+y)-\\sin(x-y)]$",
      "$\\frac12[\\cos(x-y)-\\cos(x+y)]$",
      "$2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$"
    ],
    "explanation": "The product-to-sum formula is $\\sin x\\cos y=\\frac12[\\sin(x+y)+\\sin(x-y)]$."
  },
  {
    "question": "Use product-to-sum to rewrite $\\cos x\\sin y$.",
    "answer": "$\\frac12[\\sin(x+y)-\\sin(x-y)]$",
    "wrong": [
      "$\\frac12[\\sin(x+y)+\\sin(x-y)]$",
      "$\\frac12[\\cos(x-y)+\\cos(x+y)]$",
      "$2\\cos\\frac{x+y}{2}\\sin\\frac{x-y}{2}$"
    ],
    "explanation": "The product-to-sum formula is $\\cos x\\sin y=\\frac12[\\sin(x+y)-\\sin(x-y)]$."
  },
  {
    "question": "Use sum-to-product to rewrite $\\sin x+\\sin y$.",
    "answer": "$2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
    "wrong": [
      "$2\\cos\\frac{x+y}{2}\\sin\\frac{x-y}{2}$",
      "$2\\cos\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
      "$-2\\sin\\frac{x+y}{2}\\sin\\frac{x-y}{2}$"
    ],
    "explanation": "The formula is $\\sin x+\\sin y=2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$."
  },
  {
    "question": "Use sum-to-product to rewrite $\\sin x-\\sin y$.",
    "answer": "$2\\cos\\frac{x+y}{2}\\sin\\frac{x-y}{2}$",
    "wrong": [
      "$2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
      "$2\\cos\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
      "$-2\\sin\\frac{x+y}{2}\\sin\\frac{x-y}{2}$"
    ],
    "explanation": "The formula is $\\sin x-\\sin y=2\\cos\\frac{x+y}{2}\\sin\\frac{x-y}{2}$."
  },
  {
    "question": "Use sum-to-product to rewrite $\\cos x+\\cos y$.",
    "answer": "$2\\cos\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
    "wrong": [
      "$2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
      "$2\\cos\\frac{x+y}{2}\\sin\\frac{x-y}{2}$",
      "$-2\\sin\\frac{x+y}{2}\\sin\\frac{x-y}{2}$"
    ],
    "explanation": "The formula is $\\cos x+\\cos y=2\\cos\\frac{x+y}{2}\\cos\\frac{x-y}{2}$."
  },
  {
    "question": "Use sum-to-product to rewrite $\\cos x-\\cos y$.",
    "answer": "$-2\\sin\\frac{x+y}{2}\\sin\\frac{x-y}{2}$",
    "wrong": [
      "$2\\cos\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
      "$2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
      "$2\\cos\\frac{x+y}{2}\\sin\\frac{x-y}{2}$"
    ],
    "explanation": "The formula is $\\cos x-\\cos y=-2\\sin\\frac{x+y}{2}\\sin\\frac{x-y}{2}$."
  },
  {
    "question": "Use product-to-sum to rewrite $\\sin40^\\circ\\sin20^\\circ$.",
    "answer": "$\\frac12[\\cos20^\\circ-\\cos60^\\circ]$",
    "wrong": [
      "$\\frac12[\\cos20^\\circ+\\cos60^\\circ]$",
      "$\\frac12[\\sin60^\\circ+\\sin20^\\circ]$",
      "$2\\sin30^\\circ\\cos10^\\circ$"
    ],
    "explanation": "Use $\\sin x\\sin y=\\frac12[\\cos(x-y)-\\cos(x+y)]$. Here $x-y=20^\\circ$ and $x+y=60^\\circ$."
  },
  {
    "question": "Use product-to-sum to rewrite $\\cos40^\\circ\\cos20^\\circ$.",
    "answer": "$\\frac12[\\cos20^\\circ+\\cos60^\\circ]$",
    "wrong": [
      "$\\frac12[\\cos20^\\circ-\\cos60^\\circ]$",
      "$\\frac12[\\sin60^\\circ-\\sin20^\\circ]$",
      "$2\\cos30^\\circ\\cos10^\\circ$"
    ],
    "explanation": "Use $\\cos x\\cos y=\\frac12[\\cos(x-y)+\\cos(x+y)]$. Here $x-y=20^\\circ$ and $x+y=60^\\circ$."
  },
  {
    "question": "Use product-to-sum to rewrite $\\sin40^\\circ\\cos20^\\circ$.",
    "answer": "$\\frac12[\\sin60^\\circ+\\sin20^\\circ]$",
    "wrong": [
      "$\\frac12[\\sin60^\\circ-\\sin20^\\circ]",
      "$\\frac12[\\cos20^\\circ-\\cos60^\\circ]",
      "$2\\sin30^\\circ\\cos10^\\circ"
    ],
    "explanation": "Use $\\sin x\\cos y=\\frac12[\\sin(x+y)+\\sin(x-y)]$. Here $x+y=60^\\circ$ and $x-y=20^\\circ$."
  },
  {
    "question": "Use product-to-sum to rewrite $\\cos40^\\circ\\sin20^\\circ$.",
    "answer": "$\\frac12[\\sin60^\\circ-\\sin20^\\circ]$",
    "wrong": [
      "$\\frac12[\\sin60^\\circ+\\sin20^\\circ]",
      "$\\frac12[\\cos20^\\circ+\\cos60^\\circ]",
      "$2\\cos30^\\circ\\sin10^\\circ"
    ],
    "explanation": "Use $\\cos x\\sin y=\\frac12[\\sin(x+y)-\\sin(x-y)]$. Here $x+y=60^\\circ$ and $x-y=20^\\circ$."
  },
  {
    "question": "According to the product-to-sum example, what is $\\sin60^\\circ\\sin30^\\circ$?",
    "answer": "$\\frac{\\sqrt3}{4}$",
    "wrong": [
      "$\\frac34$",
      "$\\frac14$",
      "$\\frac{\\sqrt6}{2}$"
    ],
    "explanation": "The example gives $\\frac12[\\cos30^\\circ-\\cos90^\\circ]$. Since $\\cos90^\\circ=0$, the result is $\\frac{\\sqrt3}{4}$."
  },
  {
    "question": "According to the product-to-sum example, what is $\\cos60^\\circ\\cos30^\\circ$?",
    "answer": "$\\frac{\\sqrt3}{4}$",
    "wrong": [
      "$\\frac34$",
      "$\\frac14$",
      "$\\frac{\\sqrt6}{2}$"
    ],
    "explanation": "The example gives $\\frac12[\\cos30^\\circ+\\cos90^\\circ]$. Since $\\cos90^\\circ=0$, the result is $\\frac{\\sqrt3}{4}$."
  },
  {
    "question": "According to the product-to-sum example, what is $\\sin60^\\circ\\cos30^\\circ$?",
    "answer": "$\\frac34$",
    "wrong": [
      "$\\frac14$",
      "$\\frac{\\sqrt3}{4}$",
      "$\\frac{\\sqrt2}{2}$"
    ],
    "explanation": "The example gives $\\frac12[\\sin90^\\circ+\\sin30^\\circ]=\\frac12[1+\\frac12]=\\frac34$."
  },
  {
    "question": "According to the product-to-sum example, what is $\\cos60^\\circ\\sin30^\\circ$?",
    "answer": "$\\frac14$",
    "wrong": [
      "$\\frac34$",
      "$\\frac{\\sqrt3}{4}$",
      "$\\frac{\\sqrt2}{2}$"
    ],
    "explanation": "The example gives $\\frac12[\\sin90^\\circ-\\sin30^\\circ]=\\frac12[1-\\frac12]=\\frac14$."
  },
  {
    "question": "Use sum-to-product to rewrite $\\sin80^\\circ+\\sin20^\\circ$.",
    "answer": "$2\\sin50^\\circ\\cos30^\\circ$",
    "wrong": [
      "$2\\cos50^\\circ\\sin30^\\circ$",
      "$2\\cos50^\\circ\\cos30^\\circ$",
      "$-2\\sin50^\\circ\\sin30^\\circ$"
    ],
    "explanation": "Use the sine-sum formula. The half-sum is $50^\\circ$ and the half-difference is $30^\\circ$."
  },
  {
    "question": "Use sum-to-product to rewrite $\\sin80^\\circ-\\sin20^\\circ$.",
    "answer": "$2\\cos50^\\circ\\sin30^\\circ$",
    "wrong": [
      "$2\\sin50^\\circ\\cos30^\\circ$",
      "$2\\cos50^\\circ\\cos30^\\circ$",
      "$-2\\sin50^\\circ\\sin30^\\circ$"
    ],
    "explanation": "Use the sine-difference formula. The half-sum is $50^\\circ$ and the half-difference is $30^\\circ$."
  },
  {
    "question": "Use sum-to-product to rewrite $\\cos80^\\circ+\\cos20^\\circ$.",
    "answer": "$2\\cos50^\\circ\\cos30^\\circ$",
    "wrong": [
      "$2\\sin50^\\circ\\cos30^\\circ$",
      "$2\\cos50^\\circ\\sin30^\\circ$",
      "$-2\\sin50^\\circ\\sin30^\\circ$"
    ],
    "explanation": "Use the cosine-sum formula. The half-sum is $50^\\circ$ and the half-difference is $30^\\circ$."
  },
  {
    "question": "Use sum-to-product to rewrite $\\cos80^\\circ-\\cos20^\\circ$.",
    "answer": "$-2\\sin50^\\circ\\sin30^\\circ$",
    "wrong": [
      "$2\\cos50^\\circ\\cos30^\\circ$",
      "$2\\sin50^\\circ\\cos30^\\circ$",
      "$2\\cos50^\\circ\\sin30^\\circ$"
    ],
    "explanation": "Use the cosine-difference formula. The formula includes a negative coefficient, so the answer begins with $-2$."
  },
  {
    "question": "According to the sum-to-product example, what is $\\sin75^\\circ+\\sin15^\\circ$?",
    "answer": "$\\frac{\\sqrt6}{2}$",
    "wrong": [
      "$\\frac{\\sqrt2}{2}$",
      "$-\\frac{\\sqrt2}{2}$",
      "$\\frac{\\sqrt3}{4}$"
    ],
    "explanation": "The example uses $2\\sin45^\\circ\\cos30^\\circ$, which simplifies to $\\frac{\\sqrt6}{2}$."
  },
  {
    "question": "According to the sum-to-product example, what is $\\sin75^\\circ-\\sin15^\\circ$?",
    "answer": "$\\frac{\\sqrt2}{2}$",
    "wrong": [
      "$\\frac{\\sqrt6}{2}$",
      "$-\\frac{\\sqrt2}{2}$",
      "$\\frac14$"
    ],
    "explanation": "The example uses $2\\cos45^\\circ\\sin30^\\circ$, which simplifies to $\\frac{\\sqrt2}{2}$."
  },
  {
    "question": "According to the sum-to-product example, what is $\\cos75^\\circ+\\cos15^\\circ$?",
    "answer": "$\\frac{\\sqrt6}{2}$",
    "wrong": [
      "$\\frac{\\sqrt2}{2}$",
      "$-\\frac{\\sqrt2}{2}$",
      "$\\frac34$"
    ],
    "explanation": "The example uses $2\\cos45^\\circ\\cos30^\\circ$, which simplifies to $\\frac{\\sqrt6}{2}$."
  },
  {
    "question": "According to the sum-to-product example, what is $\\cos75^\\circ-\\cos15^\\circ$?",
    "answer": "$-\\frac{\\sqrt2}{2}$",
    "wrong": [
      "$\\frac{\\sqrt2}{2}$",
      "$\\frac{\\sqrt6}{2}$",
      "$\\frac14$"
    ],
    "explanation": "The example uses $-2\\sin45^\\circ\\sin30^\\circ$, which simplifies to $-\\frac{\\sqrt2}{2}$."
  },
  {
    "question": "Which product-to-sum formula gives a difference of cosines?",
    "answer": "$\\sin x\\sin y=\\frac12[\\cos(x-y)-\\cos(x+y)]$",
    "wrong": [
      "$\\cos x\\cos y=\\frac12[\\cos(x-y)+\\cos(x+y)]$",
      "$\\sin x\\cos y=\\frac12[\\sin(x+y)+\\sin(x-y)]$",
      "$\\cos x\\sin y=\\frac12[\\sin(x+y)-\\sin(x-y)]$"
    ],
    "explanation": "The product of two sine functions becomes a difference of cosine expressions."
  },
  {
    "question": "Which product-to-sum formula gives a sum of cosines?",
    "answer": "$\\cos x\\cos y=\\frac12[\\cos(x-y)+\\cos(x+y)]$",
    "wrong": [
      "$\\sin x\\sin y=\\frac12[\\cos(x-y)-\\cos(x+y)]$",
      "$\\sin x\\cos y=\\frac12[\\sin(x+y)+\\sin(x-y)]$",
      "$\\cos x\\sin y=\\frac12[\\sin(x+y)-\\sin(x-y)]$"
    ],
    "explanation": "The product of two cosine functions becomes a sum of cosine expressions."
  },
  {
    "question": "Which sum-to-product formula has the negative coefficient $-2$?",
    "answer": "$\\cos x-\\cos y=-2\\sin\\frac{x+y}{2}\\sin\\frac{x-y}{2}$",
    "wrong": [
      "$\\sin x+\\sin y=2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
      "$\\sin x-\\sin y=2\\cos\\frac{x+y}{2}\\sin\\frac{x-y}{2}$",
      "$\\cos x+\\cos y=2\\cos\\frac{x+y}{2}\\cos\\frac{x-y}{2}$"
    ],
    "explanation": "The cosine-difference sum-to-product formula is the one with the negative coefficient $-2$."
  },
  {
    "question": "Rewrite $\\sin^2x$ using power reduction.",
    "answer": "$\\frac{1-\\cos(2x)}{2}$",
    "wrong": [
      "$\\frac{1+\\cos(2x)}{2}$",
      "$\\frac{1}{\\cos^2x}-1$",
      "$\\frac{1}{\\sin^2x}-1$"
    ],
    "explanation": "The power-reduction formula is $\\sin^2x=\\frac{1-\\cos(2x)}{2}$. It rewrites sine squared using a double angle."
  },
  {
    "question": "Rewrite $\\cos^2x$ using power reduction.",
    "answer": "$\\frac{1+\\cos(2x)}{2}$",
    "wrong": [
      "$\\frac{1-\\cos(2x)}{2}$",
      "$\\frac{1}{\\cos^2x}-1$",
      "$\\frac{1}{\\sin^2x}-1$"
    ],
    "explanation": "The power-reduction formula is $\\cos^2x=\\frac{1+\\cos(2x)}{2}$. It rewrites cosine squared using a double angle."
  },
  {
    "question": "Rewrite $\\tan^2x$ using the related formula.",
    "answer": "$\\frac{1}{\\cos^2x}-1$",
    "wrong": [
      "$\\frac{1}{\\sin^2x}-1$",
      "$\\frac{1-\\cos(2x)}{2}$",
      "$\\frac{1+\\cos(2x)}{2}$"
    ],
    "explanation": "The lesson gives $\\tan^2x=\\frac{1}{\\cos^2x}-1$. This comes from $1+\\tan^2x=\\frac{1}{\\cos^2x}$."
  },
  {
    "question": "Rewrite $\\cot^2x$ using the related formula.",
    "answer": "$\\frac{1}{\\sin^2x}-1$",
    "wrong": [
      "$\\frac{1}{\\cos^2x}-1$",
      "$\\frac{1-\\cos(2x)}{2}$",
      "$\\frac{1+\\cos(2x)}{2}$"
    ],
    "explanation": "The lesson gives $\\cot^2x=\\frac{1}{\\sin^2x}-1$. This comes from $1+\\cot^2x=\\frac{1}{\\sin^2x}$."
  },
  {
    "question": "From $\\cos(2x)=1-2\\sin^2x$, what is the next step toward solving for $\\sin^2x$?",
    "answer": "$2\\sin^2x=1-\\cos(2x)$",
    "wrong": [
      "$2\\sin^2x=1+\\cos(2x)$",
      "$\\sin^2x=1-\\cos(2x)$",
      "$\\sin^2x=\\frac{1+\\cos(2x)}{2}$"
    ],
    "explanation": "Move terms so that the squared sine term is positive. This gives $2\\sin^2x=1-\\cos(2x)$."
  },
  {
    "question": "Solve $2\\sin^2x=1-\\cos(2x)$ for $\\sin^2x$.",
    "answer": "$\\frac{1-\\cos(2x)}{2}$",
    "wrong": [
      "$1-\\cos(2x)$",
      "$\\frac{1+\\cos(2x)}{2}$",
      "$2[1-\\cos(2x)]$"
    ],
    "explanation": "Divide both sides by $2$. This gives $\\sin^2x=\\frac{1-\\cos(2x)}{2}$."
  },
  {
    "question": "Solve $\\cos(2x)=2\\cos^2x-1$ for $\\cos^2x$.",
    "answer": "$\\frac{1+\\cos(2x)}{2}$",
    "wrong": [
      "$\\frac{1-\\cos(2x)}{2}$",
      "$1+\\cos(2x)$",
      "$2\\cos(2x)+1$"
    ],
    "explanation": "Add $1$ to both sides to get $1+\\cos(2x)=2\\cos^2x$. Then divide by $2$."
  },
  {
    "question": "Use power reduction to write $\\sin^230^\\circ$.",
    "answer": "$\\frac{1-\\cos60^\\circ}{2}$",
    "wrong": [
      "$\\frac{1+\\cos60^\\circ}{2}$",
      "$\\frac{1}{\\cos^230^\\circ}-1$",
      "$\\frac{1}{\\sin^230^\\circ}-1$"
    ],
    "explanation": "Use $\\sin^2x=\\frac{1-\\cos(2x)}{2}$. With $x=30^\\circ$, the double angle is $60^\\circ$."
  },
  {
    "question": "Use power reduction to write $\\cos^230^\\circ$.",
    "answer": "$\\frac{1+\\cos60^\\circ}{2}$",
    "wrong": [
      "$\\frac{1-\\cos60^\\circ}{2}$",
      "$\\frac{1}{\\cos^230^\\circ}-1$",
      "$\\frac{1}{\\sin^230^\\circ}-1$"
    ],
    "explanation": "Use $\\cos^2x=\\frac{1+\\cos(2x)}{2}$. With $x=30^\\circ$, the double angle is $60^\\circ$."
  },
  {
    "question": "According to the lesson example, what is $\\sin^230^\\circ$?",
    "answer": "$\\frac14$",
    "wrong": [
      "$\\frac34$",
      "$\\frac12$",
      "$1$"
    ],
    "explanation": "The lesson uses $\\sin^230^\\circ=\\frac{1-\\cos60^\\circ}{2}$. Since $\\cos60^\\circ=\\frac12$, the result is $\\frac14$."
  },
  {
    "question": "According to the lesson example, what is $\\cos^230^\\circ$?",
    "answer": "$\\frac34$",
    "wrong": [
      "$\\frac14$",
      "$\\frac12$",
      "$1$"
    ],
    "explanation": "The lesson uses $\\cos^230^\\circ=\\frac{1+\\cos60^\\circ}{2}$. Since $\\cos60^\\circ=\\frac12$, the result is $\\frac34$."
  },
  {
    "question": "According to the lesson example, what is $\\tan^245^\\circ$?",
    "answer": "$1$",
    "wrong": [
      "$2$",
      "$0$",
      "$\\frac12$"
    ],
    "explanation": "The lesson uses $\\tan^2x=\\frac{1}{\\cos^2x}-1$. For $45^\\circ$, it gives $2-1=1$."
  },
  {
    "question": "According to the lesson example, what is $\\cot^245^\\circ$?",
    "answer": "$1$",
    "wrong": [
      "$2$",
      "$0$",
      "$\\frac12$"
    ],
    "explanation": "The lesson uses $\\cot^2x=\\frac{1}{\\sin^2x}-1$. For $45^\\circ$, it gives $2-1=1$."
  },
  {
    "question": "Rewrite $\\sin^2a$ using power reduction.",
    "answer": "$\\frac{1-\\cos(2a)}{2}$",
    "wrong": [
      "$\\frac{1+\\cos(2a)}{2}$",
      "$\\frac{1}{\\cos^2a}-1$",
      "$\\frac{1}{\\sin^2a}-1$"
    ],
    "explanation": "Replace $x$ with $a$ in $\\sin^2x=\\frac{1-\\cos(2x)}{2}$."
  },
  {
    "question": "Rewrite $\\cos^2a$ using power reduction.",
    "answer": "$\\frac{1+\\cos(2a)}{2}$",
    "wrong": [
      "$\\frac{1-\\cos(2a)}{2}$",
      "$\\frac{1}{\\cos^2a}-1$",
      "$\\frac{1}{\\sin^2a}-1$"
    ],
    "explanation": "Replace $x$ with $a$ in $\\cos^2x=\\frac{1+\\cos(2x)}{2}$."
  },
  {
    "question": "Rewrite $\\tan^2a$ using the related formula.",
    "answer": "$\\frac{1}{\\cos^2a}-1$",
    "wrong": [
      "$\\frac{1}{\\sin^2a}-1$",
      "$\\frac{1-\\cos(2a)}{2}$",
      "$\\frac{1+\\cos(2a)}{2}$"
    ],
    "explanation": "Replace $x$ with $a$ in $\\tan^2x=\\frac{1}{\\cos^2x}-1$."
  },
  {
    "question": "Rewrite $\\cot^2a$ using the related formula.",
    "answer": "$\\frac{1}{\\sin^2a}-1$",
    "wrong": [
      "$\\frac{1}{\\cos^2a}-1$",
      "$\\frac{1-\\cos(2a)}{2}$",
      "$\\frac{1+\\cos(2a)}{2}$"
    ],
    "explanation": "Replace $x$ with $a$ in $\\cot^2x=\\frac{1}{\\sin^2x}-1$."
  },
  {
    "question": "Use power reduction to write $\\sin^245^\\circ$.",
    "answer": "$\\frac{1-\\cos90^\\circ}{2}$",
    "wrong": [
      "$\\frac{1+\\cos90^\\circ}{2}$",
      "$\\frac{1}{\\cos^245^\\circ}-1$",
      "$\\frac{1}{\\sin^245^\\circ}-1$"
    ],
    "explanation": "Use $\\sin^2x=\\frac{1-\\cos(2x)}{2}$. With $x=45^\\circ$, the double angle is $90^\\circ$."
  },
  {
    "question": "Use power reduction to write $\\cos^245^\\circ$.",
    "answer": "$\\frac{1+\\cos90^\\circ}{2}$",
    "wrong": [
      "$\\frac{1-\\cos90^\\circ}{2}$",
      "$\\frac{1}{\\cos^245^\\circ}-1$",
      "$\\frac{1}{\\sin^245^\\circ}-1$"
    ],
    "explanation": "Use $\\cos^2x=\\frac{1+\\cos(2x)}{2}$. With $x=45^\\circ$, the double angle is $90^\\circ$."
  },
  {
    "question": "If $\\cos90^\\circ=0$, evaluate $\\sin^245^\\circ$ from $\\frac{1-\\cos90^\\circ}{2}$.",
    "answer": "$\\frac12$",
    "wrong": [
      "$1$",
      "$0$",
      "$\\frac14$"
    ],
    "explanation": "Substitute $\\cos90^\\circ=0$: $\\sin^245^\\circ=\\frac{1-0}{2}=\\frac12$."
  },
  {
    "question": "If $\\cos90^\\circ=0$, evaluate $\\cos^245^\\circ$ from $\\frac{1+\\cos90^\\circ}{2}$.",
    "answer": "$\\frac12$",
    "wrong": [
      "$1$",
      "$0$",
      "$\\frac14$"
    ],
    "explanation": "Substitute $\\cos90^\\circ=0$: $\\cos^245^\\circ=\\frac{1+0}{2}=\\frac12$."
  },
  {
    "question": "If $\\cos^245^\\circ=\\frac12$, evaluate $\\tan^245^\\circ=\\frac{1}{\\cos^245^\\circ}-1$.",
    "answer": "$1$",
    "wrong": [
      "$2$",
      "$\\frac12$",
      "$0$"
    ],
    "explanation": "Substitute $\\cos^245^\\circ=\\frac12$: $\\tan^245^\\circ=\\frac{1}{\\frac12}-1=2-1=1$."
  },
  {
    "question": "If $\\sin^245^\\circ=\\frac12$, evaluate $\\cot^245^\\circ=\\frac{1}{\\sin^245^\\circ}-1$.",
    "answer": "$1$",
    "wrong": [
      "$2$",
      "$\\frac12$",
      "$0$"
    ],
    "explanation": "Substitute $\\sin^245^\\circ=\\frac12$: $\\cot^245^\\circ=\\frac{1}{\\frac12}-1=2-1=1$."
  },
  {
    "question": "Which formula group mainly connects sine, cosine, tangent, and cotangent?",
    "answer": "Fundamental identities",
    "wrong": [
      "Half-angle formulas",
      "Product-to-sum formulas",
      "Power-reduction formulas"
    ],
    "explanation": "The overview table says fundamental identities connect sine, cosine, tangent, and cotangent. These are the base identities for simplification."
  },
  {
    "question": "Which formula group is used for values of combined angles like $x+y$ or $x-y$?",
    "answer": "Angle addition and subtraction",
    "wrong": [
      "Power reduction",
      "Product-to-sum",
      "Fundamental identities"
    ],
    "explanation": "Angle addition and subtraction formulas are used when the angle is a sum or difference, such as $x+y$ or $x-y$."
  },
  {
    "question": "Which formula group rewrites functions of $2x$?",
    "answer": "Double-angle formulas",
    "wrong": [
      "Half-angle formulas",
      "Fundamental identities",
      "Sum-to-product formulas"
    ],
    "explanation": "Double-angle formulas are used for expressions like $\\sin(2x)$, $\\cos(2x)$, $\\tan(2x)$, and $\\cot(2x)$."
  },
  {
    "question": "Which formula group finds functions of $\\frac{x}{2}$?",
    "answer": "Half-angle formulas",
    "wrong": [
      "Double-angle formulas",
      "Power-reduction formulas",
      "Fundamental identities"
    ],
    "explanation": "Half-angle formulas are used to find or rewrite expressions such as $\\sin\\frac{x}{2}$ and $\\cos\\frac{x}{2}$."
  },
  {
    "question": "Which formula group is helpful for squared expressions like $\\sin^2x$ and $\\cos^2x$?",
    "answer": "Power-reduction formulas",
    "wrong": [
      "Angle addition formulas",
      "Product-to-sum formulas",
      "Tangent addition formulas"
    ],
    "explanation": "Power-reduction formulas rewrite squared trig functions using double angles, such as $\\sin^2x=\\frac{1-\\cos(2x)}{2}$."
  },
  {
    "question": "Which formula group should you use to change $\\sin x\\sin y$ into an expression involving cosine?",
    "answer": "Product-to-sum",
    "wrong": [
      "Half-angle",
      "Power reduction",
      "Fundamental identities"
    ],
    "explanation": "Product-to-sum formulas convert products of trig functions into sums or differences. The product $\\sin x\\sin y$ becomes a difference of cosines."
  },
  {
    "question": "Which formula group should you use to change $\\sin x+\\sin y$ into a product?",
    "answer": "Sum-to-product",
    "wrong": [
      "Double-angle",
      "Fundamental identities",
      "Power reduction"
    ],
    "explanation": "Sum-to-product formulas convert sums or differences into products. The expression $\\sin x+\\sin y$ becomes $2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$."
  },
  {
    "question": "Which formula group should you use to find $\\sin15^\\circ$ from $\\cos30^\\circ$?",
    "answer": "Half-angle formulas",
    "wrong": [
      "Product-to-sum formulas",
      "Power-reduction formulas",
      "Fundamental identities"
    ],
    "explanation": "Since $15^\\circ$ is half of $30^\\circ$, the half-angle formula is the appropriate tool."
  },
  {
    "question": "Which formula group should you use to find $\\sin75^\\circ$ from $45^\\circ+30^\\circ$?",
    "answer": "Angle addition",
    "wrong": [
      "Power reduction",
      "Half-angle",
      "Product-to-sum"
    ],
    "explanation": "$75^\\circ$ is written as $45^\\circ+30^\\circ$, so the angle addition formula is the correct group."
  },
  {
    "question": "Which formula group should you use to rewrite $\\cos(2x)$ as $2\\cos^2x-1$?",
    "answer": "Double-angle formulas",
    "wrong": [
      "Half-angle formulas",
      "Product-to-sum formulas",
      "Sum-to-product formulas"
    ],
    "explanation": "$\\cos(2x)=2\\cos^2x-1$ is one of the double-angle formulas for cosine."
  },
  {
    "question": "According to the lesson's best study order, which group should be learned first?",
    "answer": "Fundamental identities",
    "wrong": [
      "Half-angle formulas",
      "Product-to-sum formulas",
      "Power-reduction formulas"
    ],
    "explanation": "The lesson recommends learning fundamental identities first because many later formulas come from them."
  },
  {
    "question": "According to the lesson's best study order, what comes after fundamental identities?",
    "answer": "Angle addition",
    "wrong": [
      "Half-angle",
      "Product-to-sum",
      "Power reduction"
    ],
    "explanation": "The lesson's study order puts angle addition after fundamental identities."
  },
  {
    "question": "According to the lesson's best study order, what comes after angle addition?",
    "answer": "Double-angle",
    "wrong": [
      "Fundamental identities",
      "Product-to-sum",
      "Power reduction"
    ],
    "explanation": "The lesson recommends studying double-angle formulas after angle addition formulas."
  },
  {
    "question": "Which statement best matches the lesson's main idea about trigonometric formulas?",
    "answer": "Most formulas come from a small number of core identities.",
    "wrong": [
      "All formulas are unrelated facts.",
      "Only tangent formulas are important.",
      "Formulas should not be connected to identities."
    ],
    "explanation": "The lesson emphasizes that trigonometric formulas are not random. Many of them come from a small group of core identities."
  },
  {
    "question": "Which identity avoids extra names like secant by writing the reciprocal directly?",
    "answer": "$1+\\tan^2x=\\frac{1}{\\cos^2x}$",
    "wrong": [
      "$\\tan x=\\frac{\\sin x}{\\cos x}$",
      "$\\sin(x+y)=\\sin x\\cos y+\\cos x\\sin y$",
      "$\\cos(2x)=\\cos^2x-\\sin^2x$"
    ],
    "explanation": "The lesson avoids extra names and writes reciprocal forms directly. This identity uses the reciprocal of $\\cos^2x$."
  },
  {
    "question": "Which identity writes the reciprocal of $\\sin^2x$ directly?",
    "answer": "$1+\\cot^2x=\\frac{1}{\\sin^2x}$",
    "wrong": [
      "$\\tan x=\\frac{\\sin x}{\\cos x}$",
      "$\\cot x=\\frac{\\cos x}{\\sin x}$",
      "$\\sin(2x)=2\\sin x\\cos x$"
    ],
    "explanation": "The lesson writes the reciprocal directly instead of using extra function names. Here the reciprocal of $\\sin^2x$ appears as $\\frac{1}{\\sin^2x}$."
  },
  {
    "question": "Simplify $\\frac{\\sin x}{\\cos x}\\cdot\\frac{\\cos x}{\\sin x}$.",
    "answer": "$1$",
    "wrong": [
      "$\\tan^2x$",
      "$\\cot^2x$",
      "$\\sin^2x+\\cos^2x$"
    ],
    "explanation": "The factors cancel: $\\sin x$ cancels with $\\sin x$, and $\\cos x$ cancels with $\\cos x$. This is the same idea as $\\tan x\\cdot\\cot x=1$."
  },
  {
    "question": "Which expression is equivalent to $\\tan x$?",
    "answer": "$\\frac{\\sin x}{\\cos x}$",
    "wrong": [
      "$\\frac{\\cos x}{\\sin x}$",
      "$\\frac{1}{\\sin^2x}$",
      "$\\cos^2x-\\sin^2x$"
    ],
    "explanation": "The tangent identity in the lesson is $\\tan x=\\frac{\\sin x}{\\cos x}$."
  },
  {
    "question": "Which expression is equivalent to $\\cot x$?",
    "answer": "$\\frac{\\cos x}{\\sin x}$",
    "wrong": [
      "$\\frac{\\sin x}{\\cos x}$",
      "$\\frac{1}{\\cos^2x}$",
      "$2\\sin x\\cos x$"
    ],
    "explanation": "The cotangent identity in the lesson is $\\cot x=\\frac{\\cos x}{\\sin x}$."
  },
  {
    "question": "Which formula is best for rewriting $\\cos x-\\cos y$ as a product?",
    "answer": "$-2\\sin\\frac{x+y}{2}\\sin\\frac{x-y}{2}$",
    "wrong": [
      "$2\\cos\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
      "$2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
      "$\\frac12[\\cos(x-y)-\\cos(x+y)]$"
    ],
    "explanation": "This is the sum-to-product formula for a cosine difference. The negative sign is essential."
  },
  {
    "question": "Which formula should you use to expand $\\sin(p+q)$?",
    "answer": "$\\sin p\\cos q+\\cos p\\sin q$",
    "wrong": [
      "$\\sin p\\cos q-\\cos p\\sin q$",
      "$\\cos p\\cos q-\\sin p\\sin q$",
      "$\\frac{\\tan p+\\tan q}{1-\\tan p\\tan q}$"
    ],
    "explanation": "Use the sine addition formula. Replace $x$ with $p$ and $y$ with $q$, keeping the plus sign."
  },
  {
    "question": "Which formula should you use to expand $\\sin(p-q)$?",
    "answer": "$\\sin p\\cos q-\\cos p\\sin q$",
    "wrong": [
      "$\\sin p\\cos q+\\cos p\\sin q$",
      "$\\cos p\\cos q+\\sin p\\sin q$",
      "$\\frac{\\tan p-\\tan q}{1+\\tan p\\tan q}$"
    ],
    "explanation": "Use the sine subtraction formula. Sine keeps the same sign as the operation inside the angle."
  },
  {
    "question": "Which formula should you use to expand $\\cos(p+q)$?",
    "answer": "$\\cos p\\cos q-\\sin p\\sin q$",
    "wrong": [
      "$\\cos p\\cos q+\\sin p\\sin q$",
      "$\\sin p\\cos q+\\cos p\\sin q$",
      "$\\frac{\\tan p+\\tan q}{1-\\tan p\\tan q}$"
    ],
    "explanation": "Use the cosine addition formula. Cosine changes the sign, so the sum formula has a minus sign."
  },
  {
    "question": "Which formula should you use to expand $\\cos(p-q)$?",
    "answer": "$\\cos p\\cos q+\\sin p\\sin q$",
    "wrong": [
      "$\\cos p\\cos q-\\sin p\\sin q$",
      "$\\sin p\\cos q-\\cos p\\sin q$",
      "$\\frac{\\tan p-\\tan q}{1+\\tan p\\tan q}$"
    ],
    "explanation": "Use the cosine subtraction formula. Cosine changes the sign, so the difference formula has a plus sign."
  },
  {
    "question": "Which formula should you use to expand $\\tan(p+q)$?",
    "answer": "$\\frac{\\tan p+\\tan q}{1-\\tan p\\tan q}$",
    "wrong": [
      "$\\frac{\\tan p-\\tan q}{1+\\tan p\\tan q}$",
      "$\\tan p+\\tan q$",
      "$\\frac{\\tan p+\\tan q}{1+\\tan p\\tan q}$"
    ],
    "explanation": "Use the tangent addition formula. The numerator keeps plus, while the denominator contains $1-\\tan p\\tan q$."
  },
  {
    "question": "Which formula should you use to expand $\\tan(p-q)$?",
    "answer": "$\\frac{\\tan p-\\tan q}{1+\\tan p\\tan q}$",
    "wrong": [
      "$\\frac{\\tan p+\\tan q}{1-\\tan p\\tan q}$",
      "$\\tan p-\\tan q$",
      "$\\frac{\\tan p-\\tan q}{1-\\tan p\\tan q}$"
    ],
    "explanation": "Use the tangent subtraction formula. The denominator changes to plus when the angle operation is subtraction."
  },
  {
    "question": "Use $\\sin(2x)=2\\sin x\\cos x$ to rewrite $2\\sin x\\cos x$ as one function.",
    "answer": "$\\sin(2x)$",
    "wrong": [
      "$\\cos(2x)$",
      "$\\tan(2x)$",
      "$\\sin^2x$"
    ],
    "explanation": "The sine double-angle formula works both directions. Since $\\sin(2x)=2\\sin x\\cos x$, the product rewrites as $\\sin(2x)$."
  },
  {
    "question": "Use $\\cos(2x)=\\cos^2x-\\sin^2x$ to rewrite $\\cos^2x-\\sin^2x$ as one function.",
    "answer": "$\\cos(2x)$",
    "wrong": [
      "$\\sin(2x)$",
      "$\\tan(2x)$",
      "$1$"
    ],
    "explanation": "The cosine double-angle identity states that $\\cos(2x)=\\cos^2x-\\sin^2x$. Therefore, the expression is $\\cos(2x)$."
  },
  {
    "question": "Use $\\cos(2x)=2\\cos^2x-1$ to rewrite $2\\cos^2x-1$ as one function.",
    "answer": "$\\cos(2x)$",
    "wrong": [
      "$\\sin(2x)$",
      "$\\tan(2x)$",
      "$\\cos^2x$"
    ],
    "explanation": "The expression $2\\cos^2x-1$ is exactly one of the cosine double-angle forms. It equals $\\cos(2x)$."
  },
  {
    "question": "Use $\\cos(2x)=1-2\\sin^2x$ to rewrite $1-2\\sin^2x$ as one function.",
    "answer": "$\\cos(2x)$",
    "wrong": [
      "$\\sin(2x)$",
      "$\\tan(2x)$",
      "$\\sin^2x$"
    ],
    "explanation": "The expression $1-2\\sin^2x$ is another form of the cosine double-angle identity. It equals $\\cos(2x)$."
  },
  {
    "question": "Which formula changes $\\sin^2x$ into an expression without a square on sine?",
    "answer": "$\\sin^2x=\\frac{1-\\cos(2x)}{2}$",
    "wrong": [
      "$\\cos^2x=\\frac{1+\\cos(2x)}{2}$",
      "$\\tan^2x=\\frac{1}{\\cos^2x}-1$",
      "$\\sin(2x)=2\\sin x\\cos x$"
    ],
    "explanation": "Power reduction is used to reduce powers. The sine-squared formula is $\\sin^2x=\\frac{1-\\cos(2x)}{2}$."
  },
  {
    "question": "Which formula changes $\\cos^2x$ into an expression without a square on cosine?",
    "answer": "$\\cos^2x=\\frac{1+\\cos(2x)}{2}$",
    "wrong": [
      "$\\sin^2x=\\frac{1-\\cos(2x)}{2}$",
      "$\\cot^2x=\\frac{1}{\\sin^2x}-1$",
      "$\\cos(2x)=1-2\\sin^2x$"
    ],
    "explanation": "Power reduction reduces squared trig expressions. The cosine-squared formula is $\\cos^2x=\\frac{1+\\cos(2x)}{2}$."
  },
  {
    "question": "Use product-to-sum to rewrite $\\sin70^\\circ\\sin10^\\circ$.",
    "answer": "$\\frac12[\\cos60^\\circ-\\cos80^\\circ]$",
    "wrong": [
      "$\\frac12[\\cos60^\\circ+\\cos80^\\circ]",
      "$\\frac12[\\sin80^\\circ+\\sin60^\\circ]",
      "$2\\sin40^\\circ\\cos30^\\circ"
    ],
    "explanation": "Use $\\sin x\\sin y=\\frac12[\\cos(x-y)-\\cos(x+y)]$. Here $70^\\circ-10^\\circ=60^\\circ$ and $70^\\circ+10^\\circ=80^\\circ$."
  },
  {
    "question": "Use product-to-sum to rewrite $\\cos70^\\circ\\cos10^\\circ$.",
    "answer": "$\\frac12[\\cos60^\\circ+\\cos80^\\circ]$",
    "wrong": [
      "$\\frac12[\\cos60^\\circ-\\cos80^\\circ]",
      "$\\frac12[\\sin80^\\circ-\\sin60^\\circ]",
      "$2\\cos40^\\circ\\cos30^\\circ"
    ],
    "explanation": "Use $\\cos x\\cos y=\\frac12[\\cos(x-y)+\\cos(x+y)]$. Here the difference is $60^\\circ$ and the sum is $80^\\circ$."
  },
  {
    "question": "Use product-to-sum to rewrite $\\sin70^\\circ\\cos10^\\circ$.",
    "answer": "$\\frac12[\\sin80^\\circ+\\sin60^\\circ]$",
    "wrong": [
      "$\\frac12[\\sin80^\\circ-\\sin60^\\circ]",
      "$\\frac12[\\cos60^\\circ-\\cos80^\\circ]",
      "$2\\sin40^\\circ\\cos30^\\circ"
    ],
    "explanation": "Use $\\sin x\\cos y=\\frac12[\\sin(x+y)+\\sin(x-y)]$. Here the sum is $80^\\circ$ and the difference is $60^\\circ$."
  },
  {
    "question": "Use product-to-sum to rewrite $\\cos70^\\circ\\sin10^\\circ$.",
    "answer": "$\\frac12[\\sin80^\\circ-\\sin60^\\circ]$",
    "wrong": [
      "$\\frac12[\\sin80^\\circ+\\sin60^\\circ]",
      "$\\frac12[\\cos60^\\circ+\\cos80^\\circ]",
      "$2\\cos40^\\circ\\sin30^\\circ"
    ],
    "explanation": "Use $\\cos x\\sin y=\\frac12[\\sin(x+y)-\\sin(x-y)]$. Here the sum is $80^\\circ$ and the difference is $60^\\circ$."
  },
  {
    "question": "Use sum-to-product to rewrite $\\sin70^\\circ+\\sin10^\\circ$.",
    "answer": "$2\\sin40^\\circ\\cos30^\\circ$",
    "wrong": [
      "$2\\cos40^\\circ\\sin30^\\circ$",
      "$2\\cos40^\\circ\\cos30^\\circ$",
      "$-2\\sin40^\\circ\\sin30^\\circ$"
    ],
    "explanation": "For $\\sin x+\\sin y$, use $2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$. The half-sum is $40^\\circ$ and the half-difference is $30^\\circ$."
  },
  {
    "question": "Use sum-to-product to rewrite $\\sin70^\\circ-\\sin10^\\circ$.",
    "answer": "$2\\cos40^\\circ\\sin30^\\circ$",
    "wrong": [
      "$2\\sin40^\\circ\\cos30^\\circ$",
      "$2\\cos40^\\circ\\cos30^\\circ$",
      "$-2\\sin40^\\circ\\sin30^\\circ$"
    ],
    "explanation": "For $\\sin x-\\sin y$, use $2\\cos\\frac{x+y}{2}\\sin\\frac{x-y}{2}$. The half-sum is $40^\\circ$ and the half-difference is $30^\\circ$."
  },
  {
    "question": "Use sum-to-product to rewrite $\\cos70^\\circ+\\cos10^\\circ$.",
    "answer": "$2\\cos40^\\circ\\cos30^\\circ$",
    "wrong": [
      "$2\\sin40^\\circ\\cos30^\\circ$",
      "$2\\cos40^\\circ\\sin30^\\circ$",
      "$-2\\sin40^\\circ\\sin30^\\circ$"
    ],
    "explanation": "For $\\cos x+\\cos y$, use $2\\cos\\frac{x+y}{2}\\cos\\frac{x-y}{2}$. The half-sum is $40^\\circ$ and the half-difference is $30^\\circ$."
  },
  {
    "question": "Use sum-to-product to rewrite $\\cos70^\\circ-\\cos10^\\circ$.",
    "answer": "$-2\\sin40^\\circ\\sin30^\\circ$",
    "wrong": [
      "$2\\cos40^\\circ\\cos30^\\circ$",
      "$2\\sin40^\\circ\\cos30^\\circ$",
      "$2\\cos40^\\circ\\sin30^\\circ$"
    ],
    "explanation": "For $\\cos x-\\cos y$, use $-2\\sin\\frac{x+y}{2}\\sin\\frac{x-y}{2}$. The negative sign is required."
  },
  {
    "question": "Which formula should be used for a product like $\\cos x\\cos y$?",
    "answer": "Product-to-sum",
    "wrong": [
      "Sum-to-product",
      "Half-angle",
      "Power reduction"
    ],
    "explanation": "A product such as $\\cos x\\cos y$ is handled by product-to-sum formulas, which convert products into sums or differences."
  },
  {
    "question": "Which formula should be used for a sum like $\\cos x+\\cos y$?",
    "answer": "Sum-to-product",
    "wrong": [
      "Product-to-sum",
      "Double-angle",
      "Fundamental identity"
    ],
    "explanation": "A sum such as $\\cos x+\\cos y$ is handled by sum-to-product formulas, which convert sums into products."
  },
  {
    "question": "Which formula should be used for $\\sin^2x$ when the goal is to reduce the power?",
    "answer": "Power-reduction formula",
    "wrong": [
      "Angle addition formula",
      "Product-to-sum formula",
      "Tangent subtraction formula"
    ],
    "explanation": "The power-reduction formula rewrites $\\sin^2x$ using a double-angle cosine expression."
  },
  {
    "question": "Which formula should be used for $\\tan\\frac{x}{2}$ when $1+\\cos x\\ne0$?",
    "answer": "$\\frac{\\sin x}{1+\\cos x}$",
    "wrong": [
      "$\\frac{1-\\cos x}{\\sin x}$",
      "$\\pm\\sqrt{\\frac{1-\\cos x}{2}}$",
      "$2\\sin x\\cos x$"
    ],
    "explanation": "The lesson states that $\\tan\\frac{x}{2}=\\frac{\\sin x}{1+\\cos x}$ is useful when $1+\\cos x\\ne0$."
  },
  {
    "question": "Which formula should be used for $\\tan\\frac{x}{2}$ when $\\sin x\\ne0$?",
    "answer": "$\\frac{1-\\cos x}{\\sin x}$",
    "wrong": [
      "$\\frac{\\sin x}{1+\\cos x}$",
      "$\\pm\\sqrt{\\frac{1+\\cos x}{2}}$",
      "$\\frac{2\\tan x}{1-\\tan^2x}$"
    ],
    "explanation": "The lesson states that $\\tan\\frac{x}{2}=\\frac{1-\\cos x}{\\sin x}$ is useful when $\\sin x\\ne0$."
  },
  {
    "question": "If $1+\\tan^2x=\\frac{1}{\\cos^2x}$, what is $\\tan^2x$?",
    "answer": "$\\frac{1}{\\cos^2x}-1$",
    "wrong": [
      "$\\frac{1}{\\sin^2x}-1$",
      "$1-\\cos^2x$",
      "$\\frac{1+\\cos(2x)}{2}$"
    ],
    "explanation": "Subtract $1$ from both sides of $1+\\tan^2x=\\frac{1}{\\cos^2x}$. This gives $\\tan^2x=\\frac{1}{\\cos^2x}-1$."
  },
  {
    "question": "If $1+\\cot^2x=\\frac{1}{\\sin^2x}$, what is $\\cot^2x$?",
    "answer": "$\\frac{1}{\\sin^2x}-1$",
    "wrong": [
      "$\\frac{1}{\\cos^2x}-1$",
      "$1-\\sin^2x$",
      "$\\frac{1-\\cos(2x)}{2}$"
    ],
    "explanation": "Subtract $1$ from both sides of $1+\\cot^2x=\\frac{1}{\\sin^2x}$. This gives $\\cot^2x=\\frac{1}{\\sin^2x}-1$."
  },
  {
    "question": "Which formula directly connects $\\sin^2x$ and $\\cos^2x$?",
    "answer": "$\\sin^2x+\\cos^2x=1$",
    "wrong": [
      "$\\tan x=\\frac{\\sin x}{\\cos x}$",
      "$\\sin(2x)=2\\sin x\\cos x$",
      "$\\cos x-\\cos y=-2\\sin\\frac{x+y}{2}\\sin\\frac{x-y}{2}$"
    ],
    "explanation": "The Pythagorean identity directly connects sine squared and cosine squared. It is one of the fundamental identities."
  },
  {
    "question": "Which formula directly connects $\\tan x$ and $\\cot x$?",
    "answer": "$\\tan x\\cdot\\cot x=1$",
    "wrong": [
      "$\\sin^2x+\\cos^2x=1$",
      "$1+\\tan^2x=\\frac{1}{\\cos^2x}$",
      "$\\sin(x+y)=\\sin x\\cos y+\\cos x\\sin y$"
    ],
    "explanation": "The identity $\\tan x\\cdot\\cot x=1$ directly connects tangent and cotangent as reciprocal-style functions."
  },
  {
    "question": "Which formula is a sine double-angle formula?",
    "answer": "$\\sin(2x)=2\\sin x\\cos x$",
    "wrong": [
      "$\\sin^2x=\\frac{1-\\cos(2x)}{2}$",
      "$\\sin x+\\sin y=2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
      "$\\sin(x-y)=\\sin x\\cos y-\\cos x\\sin y$"
    ],
    "explanation": "The formula with $\\sin(2x)$ is the sine double-angle formula."
  },
  {
    "question": "Which formula is a cosine power-reduction formula?",
    "answer": "$\\cos^2x=\\frac{1+\\cos(2x)}{2}$",
    "wrong": [
      "$\\cos(2x)=2\\cos^2x-1$",
      "$\\cos(x+y)=\\cos x\\cos y-\\sin x\\sin y$",
      "$\\cos x+\\cos y=2\\cos\\frac{x+y}{2}\\cos\\frac{x-y}{2}$"
    ],
    "explanation": "The formula that rewrites $\\cos^2x$ using $\\cos(2x)$ is the cosine power-reduction formula."
  },
  {
    "question": "Which formula is a product-to-sum formula?",
    "answer": "$\\sin x\\cos y=\\frac12[\\sin(x+y)+\\sin(x-y)]$",
    "wrong": [
      "$\\sin x+\\sin y=2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
      "$\\sin(2x)=2\\sin x\\cos x$",
      "$\\sin^2x=\\frac{1-\\cos(2x)}{2}$"
    ],
    "explanation": "Product-to-sum formulas start with a product of trig functions and rewrite it as a sum or difference."
  },
  {
    "question": "Which formula is a sum-to-product formula?",
    "answer": "$\\cos x+\\cos y=2\\cos\\frac{x+y}{2}\\cos\\frac{x-y}{2}$",
    "wrong": [
      "$\\cos x\\cos y=\\frac12[\\cos(x-y)+\\cos(x+y)]$",
      "$\\cos(2x)=2\\cos^2x-1$",
      "$\\cos\\frac{x}{2}=\\pm\\sqrt{\\frac{1+\\cos x}{2}}$"
    ],
    "explanation": "Sum-to-product formulas start with a sum or difference of trig functions and rewrite it as a product."
  },
  {
    "question": "Which formula is a half-angle formula?",
    "answer": "$\\sin\\frac{x}{2}=\\pm\\sqrt{\\frac{1-\\cos x}{2}}$",
    "wrong": [
      "$\\sin(2x)=2\\sin x\\cos x$",
      "$\\sin^2x=\\frac{1-\\cos(2x)}{2}$",
      "$\\sin x+\\sin y=2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$"
    ],
    "explanation": "Half-angle formulas contain $\\frac{x}{2}$ and express a half-angle using values involving $x$."
  },
  {
    "question": "Which formula is an angle addition formula?",
    "answer": "$\\cos(x+y)=\\cos x\\cos y-\\sin x\\sin y$",
    "wrong": [
      "$\\cos(2x)=2\\cos^2x-1$",
      "$\\cos^2x=\\frac{1+\\cos(2x)}{2}$",
      "$\\cos x-\\cos y=-2\\sin\\frac{x+y}{2}\\sin\\frac{x-y}{2}$"
    ],
    "explanation": "Angle addition formulas expand trigonometric functions of sums such as $x+y$."
  },
  {
    "question": "Which formula is an angle subtraction formula?",
    "answer": "$\\sin(x-y)=\\sin x\\cos y-\\cos x\\sin y$",
    "wrong": [
      "$\\sin(2x)=2\\sin x\\cos x$",
      "$\\sin^2x=\\frac{1-\\cos(2x)}{2}$",
      "$\\sin x-\\sin y=2\\cos\\frac{x+y}{2}\\sin\\frac{x-y}{2}$"
    ],
    "explanation": "Angle subtraction formulas expand trigonometric functions of differences such as $x-y$."
  },
  {
    "question": "Which formula would simplify $\\frac{\\sin x}{\\cos x}$ to a single trig function?",
    "answer": "$\\tan x=\\frac{\\sin x}{\\cos x}$",
    "wrong": [
      "$\\cot x=\\frac{\\cos x}{\\sin x}$",
      "$\\sin^2x+\\cos^2x=1$",
      "$\\sin(2x)=2\\sin x\\cos x$"
    ],
    "explanation": "The expression $\\frac{\\sin x}{\\cos x}$ is the definition of tangent in the lesson."
  },
  {
    "question": "Which formula would simplify $\\frac{\\cos x}{\\sin x}$ to a single trig function?",
    "answer": "$\\cot x=\\frac{\\cos x}{\\sin x}$",
    "wrong": [
      "$\\tan x=\\frac{\\sin x}{\\cos x}$",
      "$\\cos(2x)=1-2\\sin^2x$",
      "$\\sin x+\\sin y=2\\sin\\frac{x+y}{2}\\cos\\frac{x-y}{2}$"
    ],
    "explanation": "The expression $\\frac{\\cos x}{\\sin x}$ is the definition of cotangent in the lesson."
  },
  {
    "question": "Use the formula $\\sin^2x+\\cos^2x=1$: if $\\sin^2x=0$, what is $\\cos^2x$?",
    "answer": "$1$",
    "wrong": [
      "$0$",
      "$-1$",
      "$\\frac12$"
    ],
    "explanation": "Substitute $\\sin^2x=0$ into $\\sin^2x+\\cos^2x=1$. Then $0+\\cos^2x=1$, so $\\cos^2x=1$."
  },
  {
    "question": "Use the formula $\\sin^2x+\\cos^2x=1$: if $\\cos^2x=0$, what is $\\sin^2x$?",
    "answer": "$1$",
    "wrong": [
      "$0$",
      "$-1$",
      "$\\frac12$"
    ],
    "explanation": "Substitute $\\cos^2x=0$ into $\\sin^2x+\\cos^2x=1$. Then $\\sin^2x+0=1$, so $\\sin^2x=1$."
  },
  {
    "question": "If $1+\\tan^2x=4$, find $\\tan^2x$.",
    "answer": "$3$",
    "wrong": [
      "$4$",
      "$2$",
      "$\\frac14$"
    ],
    "explanation": "Subtract $1$ from both sides: $\\tan^2x=4-1=3$."
  },
  {
    "question": "If $1+\\cot^2x=9$, find $\\cot^2x$.",
    "answer": "$8$",
    "wrong": [
      "$9$",
      "$10$",
      "$3$"
    ],
    "explanation": "Subtract $1$ from both sides: $\\cot^2x=9-1=8$."
  },
  {
    "question": "If $\\cos^2x=\\frac14$, find $1+\\tan^2x$.",
    "answer": "$4$",
    "wrong": [
      "$\\frac14$",
      "$2$",
      "$3$"
    ],
    "explanation": "Use $1+\\tan^2x=\\frac{1}{\\cos^2x}$. If $\\cos^2x=\\frac14$, then $1+\\tan^2x=4$."
  }
]
print(len(data))
