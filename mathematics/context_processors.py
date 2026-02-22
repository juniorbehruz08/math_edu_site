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


def return_total_views(request):
    from .models import TakenLessons
    types = ['Fundamental Concepts of Mathematics', 'Equalities and Inequalities', 'Linear Equations',
             'Types of Numbers', 'Operations with Positive and Negative Numbers', 'Fractions and Rational Numbers',
             'Quadratic Equations', 'Inequalities', 'Linear Functions', 'Other Types of Functions',
             'Introduction to Logarithms', 'Operations on Logarithms', 'Logarithmic Functions',
             'Introduction to Trigonometry', 'Trigonometric Identities and Operations',
             'Inverse Trigonometric Functions', 'Introduction to Geometry', 'Measurement and Distance',
             'Angles and Their Properties', 'Types of Triangles', 'Properties of Triangles', 'Quadrilaterals',
             'Types of Quadrilaterals', 'Basic Concepts of Circles', 'Properties of Circles', 'Equation of a Circle',
             'Coordinate Plane', 'Distance, Midpoint, and Slope Formulas', 'The Law of Sines', 'The Law of Cosines',
             'Similar Triangles']
    all_data = {}
    for i in types:
        data = TakenLessons.objects.filter(lesson=i)
        new_data = len(data)
        x = return_lesson_name(i)
        all_data[x] = new_data
    return {'all_data': all_data}