math_problems_json = {
    'working_with_signs': [
        {
            'question': "Evaluate: $-4^2$",
            'answer': "$-16$",
            'wrong': ["$16$", "$8$", "$-8$"],
            'explanation': "According to the order of operations (PEMDAS/BODMAS), exponentiation is performed before multiplication. The expression $-4^2$ is interpreted as the negative of $4^2$. So, we first calculate $4^2 = 16$, and then apply the negative sign, resulting in $-16$."
        },
        {
            'question': "Evaluate: $(-4)^2$",
            'answer': "$16$",
            'wrong': ["$-16$", "$8$", "$-8$"],
            'explanation': "The parentheses here indicate that the base of the exponent is $-4$. So, $(-4)^2$ means $-4 \\times -4$. Multiplying two negative numbers results in a positive number, so the answer is $16$."
        },
        {
            'question': "Evaluate: $-6^2$",
            'answer': "$-36$",
            'wrong': ["$36$", "$12$", "$-12$"],
            'explanation': "Following the order of operations, we handle the exponent first: $6^2 = 36$. Then we apply the negative sign, so $-6^2 = -36$."
        },
        {
            'question': "Evaluate: $(-6)^2$",
            'answer': "$36$",
            'wrong': ["$-36$", "$12$", "$-12$"],
            'explanation': "The exponent applies to the entire number inside the parentheses. $(-6)^2 = (-6) \\times (-6) = 36$, because a negative times a negative yields a positive."
        },
        {
            'question': "Evaluate: $-1^2$",
            'answer': "$-1$",
            'wrong': ["$1$", "$0$", "$-2$"],
            'explanation': "Without parentheses, the exponent applies only to the 1. So, $1^2 = 1$, and then the negative sign is applied, giving $-1$."
        },
        {
            'question': "Evaluate: $(-1)^2$",
            'answer': "$1$",
            'wrong': ["$-1$", "$0$", "$-2$"],
            'explanation': "The exponent applies to $-1$. So, $(-1)^2 = (-1) \\times (-1) = 1$."
        },
        {
            'question': "Evaluate: $-10^2$",
            'answer': "$-100$",
            'wrong': ["$100$", "$20$", "$-20$"],
            'explanation': "Exponentiation first: $10^2 = 100$. Then apply the negative sign: $-100$."
        },
        {
            'question': "Evaluate: $(-10)^2$",
            'answer': "$100$",
            'wrong': ["$-100$", "$20$", "$-20$"],
            'explanation': "The parentheses tell us to square $-10$. $(-10) \\times (-10) = 100$."
        },
        {
            'question': "Evaluate: $-2^4$",
            'answer': "$-16$",
            'wrong': ["$16$", "$8$", "$-8$"],
            'explanation': "Order of operations: compute the exponent first. $2^4 = 16$. Then apply the negative sign, resulting in $-16$."
        },
        {
            'question': "Evaluate: $(-2)^4$",
            'answer': "$16$",
            'wrong': ["$-16$", "$8$", "$-8$"],
            'explanation': "The exponent applies to $-2$. Multiplying $-2$ by itself four times: $(-2) \\times (-2) \\times (-2) \\times (-2)$. Grouping them as pairs: $[(-2)\\times(-2)] \\times [(-2)\\times(-2)] = (4) \\times (4) = 16$."
        },
        {
            'question': "Evaluate: $-3^2$",
            'answer': "$-9$",
            'wrong': ["$9$", "$6$", "$-6$"],
            'explanation': "First, square the 3: $3^2 = 9$. Then, apply the negative sign outside: $-9$."
        },
        {
            'question': "Evaluate: $(-3)^2$",
            'answer': "$9$",
            'wrong': ["$-9$", "$6$", "$-6$"],
            'explanation': "The exponent applies to $-3$. So, $(-3) \\times (-3) = 9$."
        },
        {
            'question': "Evaluate: $-5^2$",
            'answer': "$-25$",
            'wrong': ["$25$", "$10$", "$-10$"],
            'explanation': "Calculate the power first: $5^2 = 25$. Then include the negative sign: $-25$."
        },
        {
            'question': "Evaluate: $(-5)^2$",
            'answer': "$25$",
            'wrong': ["$-25$", "$10$", "$-10$"],
            'explanation': "The parentheses indicate that the base is $-5$. So, $(-5) \\times (-5) = 25$."
        },
        {
            'question': "Evaluate: $-7^2$",
            'answer': "$-49$",
            'wrong': ["$49$", "$14$", "$-14$"],
            'explanation': "Exponentiation before negation: $7^2 = 49$, so the answer is $-49$."
        },
        {
            'question': "Evaluate: $(-7)^2$",
            'answer': "$49$",
            'wrong': ["$-49$", "$14$", "$-14$"],
            'explanation': "Squaring a negative number yields a positive: $(-7) \\times (-7) = 49$."
        },
        {
            'question': "Evaluate: $-8^2$",
            'answer': "$-64$",
            'wrong': ["$64$", "$16$", "$-16$"],
            'explanation': "First, compute $8^2 = 64$. Then, apply the negative sign to get $-64$."
        },
        {
            'question': "Evaluate: $(-8)^2$",
            'answer': "$64$",
            'wrong': ["$-64$", "$16$", "$-16$"],
            'explanation': "The exponent applies to $-8$: $(-8) \\times (-8) = 64$."
        },
        {
            'question': "Evaluate: $-9^2$",
            'answer': "$-81$",
            'wrong': ["$81$", "$18$", "$-18$"],
            'explanation': "Order of operations: $9^2 = 81$, then the negative sign makes it $-81$."
        },
        {
            'question': "Evaluate: $(-9)^2$",
            'answer': "$81$",
            'wrong': ["$-81$", "$18$", "$-18$"],
            'explanation': "The negative sign is inside the parentheses, so it is part of the base. $(-9)^2 = (-9) \\times (-9) = 81$."
        },
        {
            'question': "Evaluate: $-12^2$",
            'answer': "$-144$",
            'wrong': ["$144$", "$24$", "$-24$"],
            'explanation': "Calculate the exponent: $12^2 = 144$. Then apply the negative sign: $-144$."
        },
        {
            'question': "Evaluate: $(-12)^2$",
            'answer': "$144$",
            'wrong': ["$-144$", "$24$", "$-24$"],
            'explanation': "Squaring $-12$ gives a positive result because the exponent is even: $(-12) \\times (-12) = 144$."
        },
        {
            'question': "Evaluate: $-15^2$",
            'answer': "$-225$",
            'wrong': ["$225$", "$30$", "$-30$"],
            'explanation': "The exponent is applied to 15 only: $15^2 = 225$, so the expression is $-225$."
        },
        {
            'question': "Evaluate: $(-15)^2$",
            'answer': "$225$",
            'wrong': ["$-225$", "$30$", "$-30$"],
            'explanation': "The exponent applies to the entire number $-15$, so $(-15) \\times (-15) = 225$."
        },
        {
            'question': "Evaluate: $-20^2$",
            'answer': "$-400$",
            'wrong': ["$400$", "$40$", "$-40$"],
            'explanation': "Exponentiation first: $20^2 = 400$. Then apply the negative sign, giving $-400$."
        },
        {
            'question': "Evaluate: $(-20)^2$",
            'answer': "$400$",
            'wrong': ["$-400$", "$40$", "$-40$"],
            'explanation': "With parentheses, the base is $-20$. Squaring it yields a positive: $400$."
        },
        {
            'question': "Evaluate: $-1^3$",
            'answer': "$-1$",
            'wrong': ["$1$", "$0$", "$-3$"],
            'explanation': "First, compute $1^3 = 1$. The negative sign is applied after, resulting in $-1$."
        },
        {
            'question': "Evaluate: $(-1)^3$",
            'answer': "$-1$",
            'wrong': ["$1$", "$0$", "$-3$"],
            'explanation': "Here, the exponent applies to $-1$. Multiplying $-1$ by itself three times: $-1 \\times -1 \\times -1 = (1) \\times -1 = -1$."
        },
        {
            'question': "Evaluate: $-2^3$",
            'answer': "$-8$",
            'wrong': ["$8$", "$6$", "$-6$"],
            'explanation': "Exponent first: $2^3 = 8$. Then apply the negative sign to get $-8$."
        },
        {
            'question': "Evaluate: $(-2)^3$",
            'answer': "$-8$",
            'wrong': ["$8$", "$6$", "$-6$"],
            'explanation': "The exponent applies to $-2$. So, $(-2) \\times (-2) \\times (-2)$. First, $-2 \\times -2 = 4$, then $4 \\times -2 = -8$."
        },
        {
            'question': "Evaluate: $-3^3$",
            'answer': "$-27$",
            'wrong': ["$27$", "$9$", "$-9$"],
            'explanation': "Compute the power: $3^3 = 27$. Then apply the negative sign: $-27$."
        },
        {
            'question': "Evaluate: $(-3)^3$",
            'answer': "$-27$",
            'wrong': ["$27$", "$9$", "$-9$"],
            'explanation': "The base is $-3$, raised to the third power. Since the exponent is odd, the result is negative: $(-3) \\times (-3) \\times (-3) = 9 \\times -3 = -27$."
        },
        {
            'question': "Evaluate: $-4^3$",
            'answer': "$-64$",
            'wrong': ["$64$", "$16$", "$-16$"],
            'explanation': "Order of operations: $4^3 = 64$, so the expression is $-64$."
        },
        {
            'question': "Evaluate: $(-4)^3$",
            'answer': "$-64$",
            'wrong': ["$64$", "$16$", "$-16$"],
            'explanation': "Cubing $-4$: $(-4) \\times (-4) \\times (-4) = 16 \\times -4 = -64$."
        },
        {
            'question': "Evaluate: $-5^3$",
            'answer': "$-125$",
            'wrong': ["$125$", "$25$", "$-25$"],
            'explanation': "First, $5^3 = 125$. Then apply the negative sign: $-125$."
        },
        {
            'question': "Evaluate: $(-5)^3$",
            'answer': "$-125$",
            'wrong': ["$125$", "$25$", "$-25$"],
            'explanation': "The base is $-5$. An odd exponent keeps the sign negative: $(-5) \\times (-5) \\times (-5) = 25 \\times -5 = -125$."
        },
        {
            'question': "Evaluate: $-1^4$",
            'answer': "$-1$",
            'wrong': ["$1$", "$4$", "$-4$"],
            'explanation': "Exponent first: $1^4 = 1$. Then apply the negative: $-1$."
        },
        {
            'question': "Evaluate: $(-1)^4$",
            'answer': "$1$",
            'wrong': ["$-1$", "$4$", "$-4$"],
            'explanation': "The exponent is even, so raising $-1$ to the fourth power makes it positive: $(-1) \\times (-1) \\times (-1) \\times (-1) = 1 \\times 1 = 1$."
        },
        {
            'question': "Evaluate: $-2^5$",
            'answer': "$-32$",
            'wrong': ["$32$", "$10$", "$-10$"],
            'explanation': "Calculate the exponent first: $2^5 = 32$. Then the negative sign gives $-32$."
        },
        {
            'question': "Evaluate: $(-2)^5$",
            'answer': "$-32$",
            'wrong': ["$32$", "$10$", "$-10$"],
            'explanation': "The base is $-2$ and the exponent is odd, so the result is negative: $(-2)^5 = -32$."
        },
        {
            'question': "Evaluate: $-10^3$",
            'answer': "$-1000$",
            'wrong': ["$1000$", "$30$", "$-30$"],
            'explanation': "First, $10^3 = 1000$. Then apply the negative: $-1000$."
        },
        {
            'question': "Evaluate: $(-10)^3$",
            'answer': "$-1000$",
            'wrong': ["$1000$", "$30$", "$-30$"],
            'explanation': "Cubing a negative number yields a negative: $(-10) \\times (-10) \\times (-10) = 100 \\times -10 = -1000$."
        },
        {
            'question': "Evaluate: $-(4^2)$",
            'answer': "$-16$",
            'wrong': ["$16$", "$8$", "$-8$"],
            'explanation': "The parentheses emphasize that we compute $4^2 = 16$ first, and then apply the negative sign, giving $-16$."
        },
        {
            'question': "Evaluate: $(-4)^2$",
            'answer': "$16$",
            'wrong': ["$-16$", "$8$", "$-8$"],
            'explanation': "The parentheses are around the $-4$, making it the base. So, $(-4)^2 = 16$."
        },
        {
            'question': "Evaluate: $-(-2)^2$",
            'answer': "$-4$",
            'wrong': ["$4$", "$-2$", "$2$"],
            'explanation': "First, resolve the exponent inside the parentheses: $(-2)^2 = 4$. Then, apply the outer negative sign: $-4$."
        },
        {
            'question': "Evaluate: $(-2^2)$",
            'answer': "$-4$",
            'wrong': ["$4$", "$2$", "$-2$"],
            'explanation': "Inside the parentheses, the exponent applies only to the 2 before the negative sign, so $2^2 = 4$, making the inside $-4$. The parentheses don't change that, so the answer is $-4$."
        },
        {
            'question': "Evaluate: $-(-3)^2$",
            'answer': "$-9$",
            'wrong': ["$9$", "$-6$", "$6$"],
            'explanation': "First, compute $(-3)^2 = 9$. Then, the outer negative gives $-9$."
        },
        {
            'question': "Evaluate: $(-3^2)$",
            'answer': "$-9$",
            'wrong': ["$9$", "$6$", "$-6$"],
            'explanation': "Inside, $3^2 = 9$, and the negative sign is applied to that result, giving $-9$. The outer parentheses are just for grouping."
        },
        {
            'question': "Evaluate: $-2^2 + 3^2$",
            'answer': "$5$",
            'wrong': ["$13$", "$-5$", "$1$"],
            'explanation': "Apply exponents first: $-2^2 = -4$ and $3^2 = 9$. Then add: $-4 + 9 = 5$."
        },
        {
            'question': "Evaluate: $(-2)^2 + 3^2$",
            'answer': "$13$",
            'wrong': ["$5$", "$-5$", "$1$"],
            'explanation': "First, $(-2)^2 = 4$ and $3^2 = 9$. Then, $4 + 9 = 13$."
        },
        {
            'question': "Evaluate: $-4^2 - 1^2$",
            'answer': "$-17$",
            'wrong': ["$15$", "$17$", "$-15$"],
            'explanation': "Compute exponents: $4^2 = 16$ so $-4^2 = -16$, and $1^2 = 1$. So $-16 - 1 = -17$."
        },
        {
            'question': "Evaluate: $(-4)^2 - 1^2$",
            'answer': "$15$",
            'wrong': ["$-17$", "$17$", "$-15$"],
            'explanation': "First, $(-4)^2 = 16$ and $1^2 = 1$. Then, $16 - 1 = 15$."
        },
        {
            'question': "Evaluate: $-5^2 + (-2)^2$",
            'answer': "$-21$",
            'wrong': ["$29$", "$21$", "$-29$"],
            'explanation': "Calculate each term: $-5^2 = -25$, and $(-2)^2 = 4$. Then, $-25 + 4 = -21$."
        },
        {
            'question': "Evaluate: $(-5)^2 + (-2)^2$",
            'answer': "$29$",
            'wrong': ["$-21$", "$21$", "$-29$"],
            'explanation': "Both terms are squares of negatives, so they are positive: $25 + 4 = 29$."
        },
        {
            'question': "Evaluate: $-6^2 + (-3)^2$",
            'answer': "$-27$",
            'wrong': ["$45$", "$27$", "$-45$"],
            'explanation': "First, $-6^2 = -36$, and $(-3)^2 = 9$. Adding them: $-36 + 9 = -27$."
        },
        {
            'question': "Evaluate: $(-6)^2 + (-3)^2$",
            'answer': "$45$",
            'wrong': ["$-27$", "$27$", "$-45$"],
            'explanation': "Both are positive: $36 + 9 = 45$."
        },
        {
            'question': "Evaluate: $-7^2 + 4^2$",
            'answer': "$-33$",
            'wrong': ["$65$", "$33$", "$-65$"],
            'explanation': "$-7^2 = -49$ and $4^2 = 16$. So, $-49 + 16 = -33$."
        },
        {
            'question': "Evaluate: $(-7)^2 + 4^2$",
            'answer': "$65$",
            'wrong': ["$-33$", "$33$", "$-65$"],
            'explanation': "$49 + 16 = 65$."
        },
        {
            'question': "Evaluate: $-8^2 - (-2)^2$",
            'answer': "$-68$",
            'wrong': ["$68$", "$60$", "$-60$"],
            'explanation': "First, $-8^2 = -64$. Next, $(-2)^2 = 4$, but we are subtracting that, so it's $-64 - 4 = -68$."
        },
        {
            'question': "Evaluate: $(-8)^2 - (-2)^2$",
            'answer': "$60$",
            'wrong': ["$-68$", "$68$", "$-60$"],
            'explanation': "$64 - 4 = 60$."
        },
        {
            'question': "Evaluate: $-9^2 \\times (-1)^2$",
            'answer': "$-81$",
            'wrong': ["$81$", "$0$", "$1$"],
            'explanation': "First, $-9^2 = -81$. Next, $(-1)^2 = 1$. Multiplying: $-81 \\times 1 = -81$."
        },
        {
            'question': "Evaluate: $(-9)^2 \\times (-1)^2$",
            'answer': "$81$",
            'wrong': ["$-81$", "$0$", "$1$"],
            'explanation': "$81 \\times 1 = 81$."
        },
        {
            'question': "Evaluate: $-2^2 \\times 3^2$",
            'answer': "$-36$",
            'wrong': ["$36$", "$12$", "$-12$"],
            'explanation': "$-2^2 = -4$ and $3^2 = 9$. So, $-4 \\times 9 = -36$."
        },
        {
            'question': "Evaluate: $(-2)^2 \\times 3^2$",
            'answer': "$36$",
            'wrong': ["$-36$", "$12$", "$-12$"],
            'explanation': "$4 \\times 9 = 36$."
        },
        {
            'question': "Evaluate: $-1^2 + (-1)^3$",
            'answer': "$-2$",
            'wrong': ["$0$", "$2$", "$-1$"],
            'explanation': "$-1^2 = -1$ and $(-1)^3 = -1$. Adding: $-1 + (-1) = -2$."
        },
        {
            'question': "Evaluate: $(-1)^2 + (-1)^3$",
            'answer': "$0$",
            'wrong': ["$-2$", "$2$", "$-1$"],
            'explanation': "$1 + (-1) = 0$."
        },
        {
            'question': "Evaluate: $-3^2 / 3$",
            'answer': "$-3$",
            'wrong': ["$3$", "$-9$", "$9$"],
            'explanation': "First, $-3^2 = -9$. Then, $-9 \\div 3 = -3$."
        },
        {
            'question': "Evaluate: $(-3)^2 / 3$",
            'answer': "$3$",
            'wrong': ["$-3$", "$-9$", "$9$"],
            'explanation': "$9 \\div 3 = 3$."
        },
        {
            'question': "Evaluate: $-4^2 / (-2)^2$",
            'answer': "$-4$",
            'wrong': ["$4$", "$16$", "$-16$"],
            'explanation': "Numerator: $-4^2 = -16$. Denominator: $(-2)^2 = 4$. So, $-16 \\div 4 = -4$."
        },
        {
            'question': "Evaluate: $(-4)^2 / (-2)^2$",
            'answer': "$4$",
            'wrong': ["$-4$", "$16$", "$-16$"],
            'explanation': "$16 \\div 4 = 4$."
        },
        {
            'question': "Evaluate: $-2^2 \\cdot (-3)^2$",
            'answer': "$-36$",
            'wrong': ["$36$", "$-12$", "$12$"],
            'explanation': "$-4 \\times 9 = -36$."
        },
        {
            'question': "Evaluate: $(-2)^2 \\cdot (-3)^2$",
            'answer': "$36$",
            'wrong': ["$-36$", "$-12$", "$12$"],
            'explanation': "$4 \\times 9 = 36$."
        },
        {
            'question': "Evaluate: $-(-4)^3$",
            'answer': "$64$",
            'wrong': ["$-64$", "$12$", "$-12$"],
            'explanation': "First, $(-4)^3 = -64$. Then, the outer negative makes it $-(-64) = 64$."
        },
        {
            'question': "Evaluate: $-(-4^3)$",
            'answer': "$64$",
            'wrong': ["$-64$", "$12$", "$-12$"],
            'explanation': "Inside, $4^3 = 64$, so $-4^3 = -64$. Then, $-(-64) = 64$."
        },
        {
            'question': "Evaluate: $-(-2)^4$",
            'answer': "$-16$",
            'wrong': ["$16$", "$8$", "$-8$"],
            'explanation': "First, $(-2)^4 = 16$. Then, $-16$."
        },
        {
            'question': "Evaluate: $-(-2^4)$",
            'answer': "$16$",
            'wrong': ["$-16$", "$8$", "$-8$"],
            'explanation': "Inside the parentheses, we have $-2^4$. According to order of operations, this is $-(2^4) = -16$. Then, we have the outer negative: $-(-16) = 16$."
        },
        {
            'question': "Evaluate: $-((-2)^4)$",
            'answer': "$-16$",
            'wrong': ["$16$", "$8$", "$-8$"],
            'explanation': "First, inside the parentheses, $(-2)^4 = 16$. Then apply the outer negative: $-16$."
        },
        {
            'question': "Evaluate: $-5^0$",
            'answer': "$-1$",
            'wrong': ["$1$", "$0$", "$-5$"],
            'explanation': "Any non-zero number to the power of 0 is 1. So, $5^0 = 1$. Then apply the negative: $-1$."
        },
        {
            'question': "Evaluate: $(-5)^0$",
            'answer': "$1$",
            'wrong': ["$-1$", "$0$", "$-5$"],
            'explanation': "Any non-zero base raised to the 0 power is 1. So, $(-5)^0 = 1$."
        },
        {
            'question': "Evaluate: $-(3^2) + (-2)^3$",
            'answer': "$-17$",
            'wrong': ["$1$", "$17$", "$-1$"],
            'explanation': "First, $3^2 = 9$, so $-(9) = -9$. Next, $(-2)^3 = -8$. Then, $-9 + (-8) = -17$."
        },
        {
            'question': "Evaluate: $(-3)^2 + (-2)^3$",
            'answer': "$1$",
            'wrong': ["$-17$", "$17$", "$-1$"],
            'explanation': "$9 + (-8) = 1$."
        },
        {
            'question': "Evaluate: $-2^2 \\times (-1)^3$",
            'answer': "$4$",
            'wrong': ["$-4$", "$2$", "$-2$"],
            'explanation': "First, $-2^2 = -4$. Next, $(-1)^3 = -1$. Then, $-4 \\times -1 = 4$."
        },
        {
            'question': "Evaluate: $(-2)^2 \\times (-1)^3$",
            'answer': "$-4$",
            'wrong': ["$4$", "$2$", "$-2$"],
            'explanation': "$4 \\times -1 = -4$."
        },
        {
            'question': "Evaluate: $-3^2 \\div (-1)^2$",
            'answer': "$-9$",
            'wrong': ["$9$", "$3$", "$-3$"],
            'explanation': "$-9 \\div 1 = -9$."
        },
        {
            'question': "Evaluate: $(-3)^2 \\div (-1)^2$",
            'answer': "$9$",
            'wrong': ["$-9$", "$3$", "$-3$"],
            'explanation': "$9 \\div 1 = 9$."
        },
        {
            'question': "Evaluate: $-(-1)^3 \\times 2^2$",
            'answer': "$4$",
            'wrong': ["$-4$", "$2$", "$-2$"],
            'explanation': "First, $(-1)^3 = -1$, so $-(-1) = 1$. Then, $1 \\times 4 = 4$."
        },
        {
            'question': "Evaluate: $(-1)^3 \\times 2^2$",
            'answer': "$-4$",
            'wrong': ["$4$", "$2$", "$-2$"],
            'explanation': "$-1 \\times 4 = -4$."
        },
        {
            'question': "Evaluate: $-4^2 + (-5)^2$",
            'answer': "$9$",
            'wrong': ["$-9$", "$41$", "$-41$"],
            'explanation': "$-16 + 25 = 9$."
        },
        {
            'question': "Evaluate: $(-4)^2 + (-5)^2$",
            'answer': "$41$",
            'wrong': ["$9$", "$-9$", "$-41$"],
            'explanation': "$16 + 25 = 41$."
        },
        {
            'question': "Evaluate: $-1^2 - (-1)^2$",
            'answer': "$-2$",
            'wrong': ["$0$", "$2$", "$-1$"],
            'explanation': "$-1 - 1 = -2$."
        },
        {
            'question': "Evaluate: $(-1)^2 - 1^2$",
            'answer': "$0$",
            'wrong': ["$-2$", "$2$", "$-1$"],
            'explanation': "$1 - 1 = 0$."
        },
        {
            'question': "Evaluate: $-(-2^3)$",
            'answer': "$8$",
            'wrong': ["$-8$", "$6$", "$-6$"],
            'explanation': "Inside, $2^3 = 8$, so $-2^3 = -8$. Then, $-(-8) = 8$."
        },
        {
            'question': "Evaluate: $-((-2)^3)$",
            'answer': "$8$",
            'wrong': ["$-8$", "$6$", "$-6$"],
            'explanation': "Inside, $(-2)^3 = -8$. Then, $-(-8) = 8$."
        },
        {
            'question': "Evaluate: $-(-4^2)$",
            'answer': "$16$",
            'wrong': ["$-16$", "$8$", "$-8$"],
            'explanation': "Inside, $4^2 = 16$, so $-4^2 = -16$. Then, $-(-16) = 16$."
        },
        {
            'question': "Evaluate: $-((-4)^2)$",
            'answer': "$-16$",
            'wrong': ["$16$", "$8$", "$-8$"],
            'explanation': "Inside, $(-4)^2 = 16$. Then, $-16$."
        },
        {
            'question': "Evaluate: $-3^2 \\cdot 2^2$",
            'answer': "$-36$",
            'wrong': ["$36$", "$12$", "$-12$"],
            'explanation': "$-9 \\times 4 = -36$."
        },
        {
            'question': "Evaluate: $(-3)^2 \\cdot 2^2$",
            'answer': "$36$",
            'wrong': ["$-36$", "$12$", "$-12$"],
            'explanation': "$9 \\times 4 = 36$."
        },
        {
            'question': "Evaluate: $-(-2)^4 \\div (-1)^3$",
            'answer': "$16$",
            'wrong': ["$-16$", "$8$", "$-8$"],
            'explanation': "Step 1: Inside parentheses: $(-2)^4 = 16$ (even exponent). So we have $-16$. Step 2: Denominator: $(-1)^3 = -1$ (odd exponent). Step 3: Division: $-16 \\div (-1) = 16$."
        },
        {
            'question': "Evaluate: $(-1)^{101} \\times -2^2$",
            'answer': "$4$",
            'wrong': ["$-4$", "$2$", "$-2$"],
            'explanation': "Step 1: $(-1)^{101}$: 101 is odd, so result is $-1$. Step 2: $-2^2 = -(2^2) = -4$. Step 3: Multiply: $-1 \\times -4 = 4$."
        },
        {
            'question': "Evaluate: $-(-3)^2 + (-2)^4$",
            'answer': "$7$",
            'wrong': ["$-7$", "$25$", "$-25$"],
            'explanation': "Step 1: First term: $(-3)^2 = 9$, so $-9$. Step 2: Second term: $(-2)^4 = 16$ (even exponent). Step 3: Add: $-9 + 16 = 7$."
        }
    ],
    'fraction_practice':

    # ═══════════════════════════════════════════════════════════════════════════
    # SECTION 1 — ADDITION WITH FRACTIONS (25 problems)
    # ═══════════════════════════════════════════════════════════════════════════

        [{
            'question': r"Evaluate: $-\dfrac{1}{2} + \left(-\dfrac{1}{3}\right)$",
            'answer': r"$-\dfrac{5}{6}$",
            'wrong': [r"$\dfrac{5}{6}$", r"$-\dfrac{1}{6}$", r"$\dfrac{1}{5}$"],
            'explanation': r"Both terms are negative, so add their absolute values: $\frac{1}{2} + \frac{1}{3} = \frac{3}{6} + \frac{2}{6} = \frac{5}{6}$. Since both are negative, the result is $-\frac{5}{6}$."
        },
            {
                'question': r"Evaluate: $\dfrac{3}{4} + \left(-\dfrac{1}{2}\right)$",
                'answer': r"$\dfrac{1}{4}$",
                'wrong': [r"$-\dfrac{1}{4}$", r"$\dfrac{5}{4}$", r"$-\dfrac{5}{4}$"],
                'explanation': r"Different signs: $\frac{3}{4} - \frac{1}{2} = \frac{3}{4} - \frac{2}{4} = \frac{1}{4}$. Since $\frac{3}{4} > \frac{1}{2}$, the result is positive: $\frac{1}{4}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{5}{6} + \dfrac{1}{3}$",
                'answer': r"$-\dfrac{1}{2}$",
                'wrong': [r"$\dfrac{1}{2}$", r"$-\dfrac{7}{6}$", r"$\dfrac{7}{6}$"],
                'explanation': r"$-\frac{5}{6} + \frac{1}{3} = -\frac{5}{6} + \frac{2}{6} = -\frac{3}{6} = -\frac{1}{2}$. The negative term has the larger absolute value, so the result is negative."
            },
            {
                'question': r"Evaluate: $-\dfrac{2}{3} + \left(-\dfrac{3}{4}\right)$",
                'answer': r"$-\dfrac{17}{12}$",
                'wrong': [r"$\dfrac{17}{12}$", r"$-\dfrac{5}{12}$", r"$\dfrac{5}{12}$"],
                'explanation': r"Both negative: $\frac{2}{3} + \frac{3}{4} = \frac{8}{12} + \frac{9}{12} = \frac{17}{12}$, so the answer is $-\frac{17}{12}$."
            },
            {
                'question': r"Evaluate: $\dfrac{1}{5} + \left(-\dfrac{3}{10}\right)$",
                'answer': r"$-\dfrac{1}{10}$",
                'wrong': [r"$\dfrac{1}{10}$", r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$"],
                'explanation': r"$\frac{1}{5} = \frac{2}{10}$, so $\frac{2}{10} + \left(-\frac{3}{10}\right) = -\frac{1}{10}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{7}{8} + \dfrac{3}{4}$",
                'answer': r"$-\dfrac{1}{8}$",
                'wrong': [r"$\dfrac{1}{8}$", r"$-\dfrac{13}{8}$", r"$\dfrac{13}{8}$"],
                'explanation': r"$\frac{3}{4} = \frac{6}{8}$, so $-\frac{7}{8} + \frac{6}{8} = -\frac{1}{8}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{1}{4} + \left(-\dfrac{5}{8}\right)$",
                'answer': r"$-\dfrac{7}{8}$",
                'wrong': [r"$\dfrac{7}{8}$", r"$-\dfrac{3}{8}$", r"$\dfrac{3}{8}$"],
                'explanation': r"$-\frac{1}{4} = -\frac{2}{8}$, so $-\frac{2}{8} + \left(-\frac{5}{8}\right) = -\frac{7}{8}$."
            },
            {
                'question': r"Evaluate: $\dfrac{5}{6} + \left(-\dfrac{7}{9}\right)$",
                'answer': r"$\dfrac{1}{18}$",
                'wrong': [r"$-\dfrac{1}{18}$", r"$\dfrac{2}{3}$", r"$-\dfrac{2}{3}$"],
                'explanation': r"Common denominator 18: $\frac{5}{6} = \frac{15}{18}$, $\frac{7}{9} = \frac{14}{18}$. So $\frac{15}{18} - \frac{14}{18} = \frac{1}{18}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{3}{5} + \dfrac{7}{10}$",
                'answer': r"$\dfrac{1}{10}$",
                'wrong': [r"$-\dfrac{1}{10}$", r"$-\dfrac{13}{10}$", r"$\dfrac{13}{10}$"],
                'explanation': r"$-\frac{3}{5} = -\frac{6}{10}$, so $-\frac{6}{10} + \frac{7}{10} = \frac{1}{10}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{4}{9} + \left(-\dfrac{2}{3}\right)$",
                'answer': r"$-\dfrac{10}{9}$",
                'wrong': [r"$\dfrac{10}{9}$", r"$-\dfrac{2}{9}$", r"$\dfrac{2}{9}$"],
                'explanation': r"$-\frac{2}{3} = -\frac{6}{9}$, so $-\frac{4}{9} - \frac{6}{9} = -\frac{10}{9}$."
            },
            {
                'question': r"Evaluate: $\dfrac{2}{7} + \left(-\dfrac{5}{14}\right)$",
                'answer': r"$-\dfrac{1}{14}$",
                'wrong': [r"$\dfrac{1}{14}$", r"$\dfrac{9}{14}$", r"$-\dfrac{9}{14}$"],
                'explanation': r"$\frac{2}{7} = \frac{4}{14}$, so $\frac{4}{14} - \frac{5}{14} = -\frac{1}{14}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{5}{12} + \dfrac{1}{4}$",
                'answer': r"$-\dfrac{1}{6}$",
                'wrong': [r"$\dfrac{1}{6}$", r"$-\dfrac{1}{3}$", r"$\dfrac{1}{3}$"],
                'explanation': r"$\frac{1}{4} = \frac{3}{12}$, so $-\frac{5}{12} + \frac{3}{12} = -\frac{2}{12} = -\frac{1}{6}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{3}{8} + \left(-\dfrac{1}{4}\right) + \dfrac{3}{4}$",
                'answer': r"$\dfrac{1}{8}$",
                'wrong': [r"$-\dfrac{1}{8}$", r"$\dfrac{7}{8}$", r"$-\dfrac{7}{8}$"],
                'explanation': r"$-\frac{1}{4} = -\frac{2}{8}$ and $\frac{3}{4} = \frac{6}{8}$. So $-\frac{3}{8} - \frac{2}{8} + \frac{6}{8} = \frac{1}{8}$."
            },
            {
                'question': r"Evaluate: $\dfrac{1}{6} + \left(-\dfrac{1}{2}\right) + \dfrac{2}{3}$",
                'answer': r"$\dfrac{1}{3}$",
                'wrong': [r"$-\dfrac{1}{3}$", r"$\dfrac{1}{6}$", r"$-\dfrac{1}{6}$"],
                'explanation': r"Common denominator 6: $\frac{1}{6} - \frac{3}{6} + \frac{4}{6} = \frac{2}{6} = \frac{1}{3}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{7}{10} + \dfrac{2}{5} + \left(-\dfrac{1}{10}\right)$",
                'answer': r"$-\dfrac{2}{5}$",
                'wrong': [r"$\dfrac{2}{5}$", r"$-\dfrac{4}{5}$", r"$\dfrac{4}{5}$"],
                'explanation': r"$\frac{2}{5} = \frac{4}{10}$. So $-\frac{7}{10} + \frac{4}{10} - \frac{1}{10} = -\frac{4}{10} = -\frac{2}{5}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{1}{3} + \dfrac{5}{6} + \left(-\dfrac{1}{2}\right)$",
                'answer': r"$0$",
                'wrong': [r"$\dfrac{1}{6}$", r"$-\dfrac{1}{6}$", r"$1$"],
                'explanation': r"Common denominator 6: $-\frac{2}{6} + \frac{5}{6} - \frac{3}{6} = \frac{0}{6} = 0$."
            },
            {
                'question': r"Evaluate: $-\dfrac{9}{10} + \dfrac{3}{5}$",
                'answer': r"$-\dfrac{3}{10}$",
                'wrong': [r"$\dfrac{3}{10}$", r"$-\dfrac{3}{2}$", r"$\dfrac{3}{2}$"],
                'explanation': r"$\frac{3}{5} = \frac{6}{10}$, so $-\frac{9}{10} + \frac{6}{10} = -\frac{3}{10}$."
            },
            {
                'question': r"Evaluate: $\dfrac{5}{8} + \left(-\dfrac{7}{8}\right)$",
                'answer': r"$-\dfrac{1}{4}$",
                'wrong': [r"$\dfrac{1}{4}$", r"$-\dfrac{3}{4}$", r"$\dfrac{3}{2}$"],
                'explanation': r"Same denominator: $\frac{5}{8} - \frac{7}{8} = -\frac{2}{8} = -\frac{1}{4}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{11}{12} + \dfrac{5}{6}$",
                'answer': r"$-\dfrac{1}{12}$",
                'wrong': [r"$\dfrac{1}{12}$", r"$-\dfrac{1}{4}$", r"$\dfrac{1}{4}$"],
                'explanation': r"$\frac{5}{6} = \frac{10}{12}$, so $-\frac{11}{12} + \frac{10}{12} = -\frac{1}{12}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{1}{2}\right) + \left(-\dfrac{1}{3}\right) + \left(-\dfrac{1}{6}\right)$",
                'answer': r"$-1$",
                'wrong': [r"$1$", r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$"],
                'explanation': r"Common denominator 6: $-\frac{3}{6} - \frac{2}{6} - \frac{1}{6} = -\frac{6}{6} = -1$."
            },
            {
                'question': r"Evaluate: $-\dfrac{2}{5} + \dfrac{3}{10} + \left(-\dfrac{1}{2}\right)$",
                'answer': r"$-\dfrac{3}{5}$",
                'wrong': [r"$\dfrac{3}{5}$", r"$-\dfrac{1}{5}$", r"$\dfrac{1}{5}$"],
                'explanation': r"Common denominator 10: $-\frac{4}{10} + \frac{3}{10} - \frac{5}{10} = -\frac{6}{10} = -\frac{3}{5}$."
            },
            {
                'question': r"Evaluate: $\dfrac{7}{12} + \left(-\dfrac{3}{4}\right)$",
                'answer': r"$-\dfrac{1}{6}$",
                'wrong': [r"$\dfrac{1}{6}$", r"$-\dfrac{1}{3}$", r"$\dfrac{4}{3}$"],
                'explanation': r"$\frac{3}{4} = \frac{9}{12}$, so $\frac{7}{12} - \frac{9}{12} = -\frac{2}{12} = -\frac{1}{6}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{5}{9} + \dfrac{1}{3} + \left(-\dfrac{1}{9}\right)$",
                'answer': r"$-\dfrac{1}{3}$",
                'wrong': [r"$\dfrac{1}{3}$", r"$-\dfrac{5}{9}$", r"$\dfrac{5}{9}$"],
                'explanation': r"$\frac{1}{3} = \frac{3}{9}$. So $-\frac{5}{9} + \frac{3}{9} - \frac{1}{9} = -\frac{3}{9} = -\frac{1}{3}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{3}{7} + \dfrac{5}{14}$",
                'answer': r"$-\dfrac{1}{14}$",
                'wrong': [r"$\dfrac{1}{14}$", r"$-\dfrac{11}{14}$", r"$\dfrac{11}{14}$"],
                'explanation': r"$-\frac{3}{7} = -\frac{6}{14}$, so $-\frac{6}{14} + \frac{5}{14} = -\frac{1}{14}$."
            },
            {
                'question': r"Evaluate: $\dfrac{4}{15} + \left(-\dfrac{2}{5}\right) + \dfrac{1}{3}$",
                'answer': r"$\dfrac{1}{15}$",
                'wrong': [r"$-\dfrac{1}{15}$", r"$\dfrac{1}{5}$", r"$-\dfrac{1}{5}$"],
                'explanation': r"Common denominator 15: $\frac{4}{15} - \frac{6}{15} + \frac{5}{15} = \frac{3}{15} = \frac{1}{5}$. Wait, let me recheck: $4 - 6 + 5 = 3$, $\frac{3}{15} = \frac{1}{5}$."
            },

            # ═══════════════════════════════════════════════════════════════════════════
            # SECTION 2 — SUBTRACTION WITH FRACTIONS (25 problems)
            # ═══════════════════════════════════════════════════════════════════════════

            {
                'question': r"Evaluate: $-\dfrac{3}{4} - \dfrac{1}{4}$",
                'answer': r"$-1$",
                'wrong': [r"$1$", r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$"],
                'explanation': r"$-\frac{3}{4} - \frac{1}{4} = -\frac{4}{4} = -1$. Subtracting a positive from a negative makes it more negative."
            },
            {
                'question': r"Evaluate: $\dfrac{1}{2} - \dfrac{3}{4}$",
                'answer': r"$-\dfrac{1}{4}$",
                'wrong': [r"$\dfrac{1}{4}$", r"$\dfrac{5}{4}$", r"$-\dfrac{5}{4}$"],
                'explanation': r"$\frac{1}{2} = \frac{2}{4}$, so $\frac{2}{4} - \frac{3}{4} = -\frac{1}{4}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{2}{3} - \left(-\dfrac{1}{3}\right)$",
                'answer': r"$-\dfrac{1}{3}$",
                'wrong': [r"$\dfrac{1}{3}$", r"$-1$", r"$1$"],
                'explanation': r"Subtracting a negative is the same as adding a positive: $-\frac{2}{3} + \frac{1}{3} = -\frac{1}{3}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{5}{6} - \dfrac{1}{3}$",
                'answer': r"$-\dfrac{7}{6}$",
                'wrong': [r"$\dfrac{7}{6}$", r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$"],
                'explanation': r"$\frac{1}{3} = \frac{2}{6}$, so $-\frac{5}{6} - \frac{2}{6} = -\frac{7}{6}$."
            },
            {
                'question': r"Evaluate: $\dfrac{3}{8} - \dfrac{5}{8}$",
                'answer': r"$-\dfrac{1}{4}$",
                'wrong': [r"$\dfrac{1}{4}$", r"$-1$", r"$\dfrac{1}{8}$"],
                'explanation': r"$\frac{3}{8} - \frac{5}{8} = -\frac{2}{8} = -\frac{1}{4}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{1}{4} - \left(-\dfrac{3}{4}\right)$",
                'answer': r"$\dfrac{1}{2}$",
                'wrong': [r"$-\dfrac{1}{2}$", r"$-1$", r"$1$"],
                'explanation': r"$-\frac{1}{4} - (-\frac{3}{4}) = -\frac{1}{4} + \frac{3}{4} = \frac{2}{4} = \frac{1}{2}$."
            },
            {
                'question': r"Evaluate: $\dfrac{2}{5} - \dfrac{4}{5}$",
                'answer': r"$-\dfrac{2}{5}$",
                'wrong': [r"$\dfrac{2}{5}$", r"$-\dfrac{6}{5}$", r"$\dfrac{6}{5}$"],
                'explanation': r"Same denominator: $\frac{2}{5} - \frac{4}{5} = -\frac{2}{5}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{7}{9} - \left(-\dfrac{4}{9}\right)$",
                'answer': r"$-\dfrac{1}{3}$",
                'wrong': [r"$\dfrac{1}{3}$", r"$-\dfrac{11}{9}$", r"$\dfrac{11}{9}$"],
                'explanation': r"$-\frac{7}{9} + \frac{4}{9} = -\frac{3}{9} = -\frac{1}{3}$."
            },
            {
                'question': r"Evaluate: $\dfrac{1}{3} - \dfrac{5}{6}$",
                'answer': r"$-\dfrac{1}{2}$",
                'wrong': [r"$\dfrac{1}{2}$", r"$-\dfrac{1}{6}$", r"$\dfrac{1}{6}$"],
                'explanation': r"$\frac{1}{3} = \frac{2}{6}$, so $\frac{2}{6} - \frac{5}{6} = -\frac{3}{6} = -\frac{1}{2}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{3}{10} - \dfrac{2}{5}$",
                'answer': r"$-\dfrac{7}{10}$",
                'wrong': [r"$\dfrac{7}{10}$", r"$-\dfrac{1}{10}$", r"$\dfrac{1}{10}$"],
                'explanation': r"$\frac{2}{5} = \frac{4}{10}$, so $-\frac{3}{10} - \frac{4}{10} = -\frac{7}{10}$."
            },
            {
                'question': r"Evaluate: $\dfrac{5}{12} - \dfrac{3}{4}$",
                'answer': r"$-\dfrac{1}{3}$",
                'wrong': [r"$\dfrac{1}{3}$", r"$\dfrac{1}{6}$", r"$-\dfrac{1}{6}$"],
                'explanation': r"$\frac{3}{4} = \frac{9}{12}$, so $\frac{5}{12} - \frac{9}{12} = -\frac{4}{12} = -\frac{1}{3}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{1}{6} - \left(-\dfrac{1}{2}\right)$",
                'answer': r"$\dfrac{1}{3}$",
                'wrong': [r"$-\dfrac{1}{3}$", r"$\dfrac{2}{3}$", r"$-\dfrac{2}{3}$"],
                'explanation': r"$-\frac{1}{6} + \frac{1}{2} = -\frac{1}{6} + \frac{3}{6} = \frac{2}{6} = \frac{1}{3}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{5}{8} - \dfrac{3}{8}$",
                'answer': r"$-1$",
                'wrong': [r"$1$", r"$-\dfrac{1}{4}$", r"$\dfrac{1}{4}$"],
                'explanation': r"$-\frac{5}{8} - \frac{3}{8} = -\frac{8}{8} = -1$."
            },
            {
                'question': r"Evaluate: $\dfrac{7}{10} - \dfrac{9}{10}$",
                'answer': r"$-\dfrac{1}{5}$",
                'wrong': [r"$\dfrac{1}{5}$", r"$-\dfrac{1}{10}$", r"$\dfrac{1}{10}$"],
                'explanation': r"$\frac{7}{10} - \frac{9}{10} = -\frac{2}{10} = -\frac{1}{5}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{4}{7} - \left(-\dfrac{2}{7}\right)$",
                'answer': r"$-\dfrac{2}{7}$",
                'wrong': [r"$\dfrac{2}{7}$", r"$-\dfrac{6}{7}$", r"$\dfrac{6}{7}$"],
                'explanation': r"$-\frac{4}{7} + \frac{2}{7} = -\frac{2}{7}$."
            },
            {
                'question': r"Evaluate: $\dfrac{1}{4} - \dfrac{7}{12}$",
                'answer': r"$-\dfrac{1}{3}$",
                'wrong': [r"$\dfrac{1}{3}$", r"$-\dfrac{1}{6}$", r"$\dfrac{1}{6}$"],
                'explanation': r"$\frac{1}{4} = \frac{3}{12}$, so $\frac{3}{12} - \frac{7}{12} = -\frac{4}{12} = -\frac{1}{3}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{2}{9} - \dfrac{5}{9}$",
                'answer': r"$-\dfrac{7}{9}$",
                'wrong': [r"$\dfrac{7}{9}$", r"$-\dfrac{1}{3}$", r"$\dfrac{1}{3}$"],
                'explanation': r"$-\frac{2}{9} - \frac{5}{9} = -\frac{7}{9}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{3}{5} - \left(-\dfrac{4}{10}\right)$",
                'answer': r"$-\dfrac{1}{5}$",
                'wrong': [r"$\dfrac{1}{5}$", r"$-1$", r"$1$"],
                'explanation': r"$-\frac{4}{10} = -\frac{2}{5}$. So $-\frac{3}{5} - (-\frac{2}{5}) = -\frac{3}{5} + \frac{2}{5} = -\frac{1}{5}$."
            },
            {
                'question': r"Evaluate: $\dfrac{3}{4} - \dfrac{5}{6}$",
                'answer': r"$-\dfrac{1}{12}$",
                'wrong': [r"$\dfrac{1}{12}$", r"$\dfrac{1}{6}$", r"$-\dfrac{1}{6}$"],
                'explanation': r"Common denominator 12: $\frac{9}{12} - \frac{10}{12} = -\frac{1}{12}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{1}{2} - \dfrac{1}{3} - \dfrac{1}{6}$",
                'answer': r"$-1$",
                'wrong': [r"$1$", r"$-\dfrac{1}{6}$", r"$\dfrac{1}{6}$"],
                'explanation': r"Common denominator 6: $-\frac{3}{6} - \frac{2}{6} - \frac{1}{6} = -\frac{6}{6} = -1$."
            },
            {
                'question': r"Evaluate: $\dfrac{5}{6} - \left(-\dfrac{1}{6}\right) - \dfrac{3}{2}$",
                'answer': r"$-\dfrac{2}{3}$",
                'wrong': [r"$\dfrac{2}{3}$", r"$-\dfrac{4}{3}$", r"$\dfrac{4}{3}$"],
                'explanation': r"$\frac{5}{6} + \frac{1}{6} - \frac{9}{6} = \frac{6}{6} - \frac{9}{6} = -\frac{3}{6} = -\frac{1}{2}$. Wait — $\frac{3}{2} = \frac{9}{6}$; $\frac{5+1-9}{6} = -\frac{3}{6} = -\frac{1}{2}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{11}{15} - \dfrac{1}{5}$",
                'answer': r"$-\dfrac{14}{15}$",
                'wrong': [r"$\dfrac{14}{15}$", r"$-\dfrac{2}{3}$", r"$\dfrac{2}{3}$"],
                'explanation': r"$\frac{1}{5} = \frac{3}{15}$, so $-\frac{11}{15} - \frac{3}{15} = -\frac{14}{15}$."
            },
            {
                'question': r"Evaluate: $\dfrac{1}{8} - \left(-\dfrac{3}{8}\right)$",
                'answer': r"$\dfrac{1}{2}$",
                'wrong': [r"$-\dfrac{1}{2}$", r"$\dfrac{1}{4}$", r"$-\dfrac{1}{4}$"],
                'explanation': r"$\frac{1}{8} + \frac{3}{8} = \frac{4}{8} = \frac{1}{2}$."
            },
            {
                'question': r"Evaluate: $-\dfrac{7}{8} - \left(-\dfrac{5}{8}\right)$",
                'answer': r"$-\dfrac{1}{4}$",
                'wrong': [r"$\dfrac{1}{4}$", r"$-\dfrac{3}{2}$", r"$\dfrac{3}{2}$"],
                'explanation': r"$-\frac{7}{8} + \frac{5}{8} = -\frac{2}{8} = -\frac{1}{4}$."
            },
            {
                'question': r"Evaluate: $\dfrac{2}{3} - \dfrac{5}{3}$",
                'answer': r"$-1$",
                'wrong': [r"$1$", r"$-\dfrac{1}{3}$", r"$\dfrac{7}{3}$"],
                'explanation': r"$\frac{2}{3} - \frac{5}{3} = -\frac{3}{3} = -1$."
            },

            # ═══════════════════════════════════════════════════════════════════════════
            # SECTION 3 — MULTIPLICATION WITH FRACTIONS (25 problems)
            # ═══════════════════════════════════════════════════════════════════════════

            {
                'question': r"Evaluate: $\left(-\dfrac{2}{3}\right) \times \dfrac{3}{4}$",
                'answer': r"$-\dfrac{1}{2}$",
                'wrong': [r"$\dfrac{1}{2}$", r"$-\dfrac{6}{7}$", r"$\dfrac{6}{7}$"],
                'explanation': r"Multiply numerators and denominators: $\frac{2 \times 3}{3 \times 4} = \frac{6}{12} = \frac{1}{2}$. One negative factor $\Rightarrow$ result is $-\frac{1}{2}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{3}{5}\right) \times \left(-\dfrac{5}{6}\right)$",
                'answer': r"$\dfrac{1}{2}$",
                'wrong': [r"$-\dfrac{1}{2}$", r"$\dfrac{1}{3}$", r"$-\dfrac{1}{3}$"],
                'explanation': r"Two negatives multiply to a positive. $\frac{3 \times 5}{5 \times 6} = \frac{15}{30} = \frac{1}{2}$."
            },
            {
                'question': r"Evaluate: $\dfrac{4}{7} \times \left(-\dfrac{7}{8}\right)$",
                'answer': r"$-\dfrac{1}{2}$",
                'wrong': [r"$\dfrac{1}{2}$", r"$-\dfrac{4}{8}$", r"$\dfrac{11}{15}$"],
                'explanation': r"$\frac{4 \times 7}{7 \times 8} = \frac{28}{56} = \frac{1}{2}$. One negative $\Rightarrow -\frac{1}{2}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{1}{4}\right) \times \left(-\dfrac{8}{3}\right)$",
                'answer': r"$\dfrac{2}{3}$",
                'wrong': [r"$-\dfrac{2}{3}$", r"$\dfrac{1}{3}$", r"$-\dfrac{1}{3}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{1 \times 8}{4 \times 3} = \frac{8}{12} = \frac{2}{3}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{5}{6}\right) \times \dfrac{3}{10}$",
                'answer': r"$-\dfrac{1}{4}$",
                'wrong': [r"$\dfrac{1}{4}$", r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$"],
                'explanation': r"$\frac{5 \times 3}{6 \times 10} = \frac{15}{60} = \frac{1}{4}$. One negative $\Rightarrow -\frac{1}{4}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{2}{9}\right) \times \left(-\dfrac{3}{4}\right)$",
                'answer': r"$\dfrac{1}{6}$",
                'wrong': [r"$-\dfrac{1}{6}$", r"$\dfrac{1}{3}$", r"$-\dfrac{1}{3}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{2 \times 3}{9 \times 4} = \frac{6}{36} = \frac{1}{6}$."
            },
            {
                'question': r"Evaluate: $\dfrac{7}{8} \times \left(-\dfrac{4}{21}\right)$",
                'answer': r"$-\dfrac{1}{6}$",
                'wrong': [r"$\dfrac{1}{6}$", r"$-\dfrac{7}{42}$", r"$\dfrac{7}{42}$"],
                'explanation': r"$\frac{7 \times 4}{8 \times 21} = \frac{28}{168} = \frac{1}{6}$. One negative $\Rightarrow -\frac{1}{6}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{3}{4}\right)^2$",
                'answer': r"$\dfrac{9}{16}$",
                'wrong': [r"$-\dfrac{9}{16}$", r"$\dfrac{3}{8}$", r"$-\dfrac{3}{8}$"],
                'explanation': r"$\left(-\frac{3}{4}\right)^2 = \left(-\frac{3}{4}\right)\times\left(-\frac{3}{4}\right) = \frac{9}{16}$. Two negatives $\Rightarrow$ positive."
            },
            {
                'question': r"Evaluate: $-\left(\dfrac{2}{5}\right)^2$",
                'answer': r"$-\dfrac{4}{25}$",
                'wrong': [r"$\dfrac{4}{25}$", r"$-\dfrac{2}{10}$", r"$\dfrac{2}{10}$"],
                'explanation': r"First square: $\left(\frac{2}{5}\right)^2 = \frac{4}{25}$. Then apply the negative sign: $-\frac{4}{25}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{1}{2}\right)^3$",
                'answer': r"$-\dfrac{1}{8}$",
                'wrong': [r"$\dfrac{1}{8}$", r"$-\dfrac{3}{8}$", r"$\dfrac{3}{2}$"],
                'explanation': r"$\left(-\frac{1}{2}\right)^3 = \left(-\frac{1}{2}\right)\left(-\frac{1}{2}\right)\left(-\frac{1}{2}\right) = \frac{1}{4}\cdot\left(-\frac{1}{2}\right) = -\frac{1}{8}$. Odd power keeps the negative."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{2}{3}\right)^3$",
                'answer': r"$-\dfrac{8}{27}$",
                'wrong': [r"$\dfrac{8}{27}$", r"$-\dfrac{6}{27}$", r"$\dfrac{6}{9}$"],
                'explanation': r"$\left(-\frac{2}{3}\right)^3 = -\frac{2^3}{3^3} = -\frac{8}{27}$. Odd exponent, negative base $\Rightarrow$ negative result."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{3}{5}\right) \times \left(-\dfrac{5}{3}\right)$",
                'answer': r"$1$",
                'wrong': [r"$-1$", r"$\dfrac{9}{25}$", r"$-\dfrac{9}{25}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{3}{5} \times \frac{5}{3} = \frac{15}{15} = 1$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{4}{5}\right) \times \dfrac{15}{8}$",
                'answer': r"$-\dfrac{3}{2}$",
                'wrong': [r"$\dfrac{3}{2}$", r"$-\dfrac{60}{40}$", r"$\dfrac{1}{2}$"],
                'explanation': r"$\frac{4 \times 15}{5 \times 8} = \frac{60}{40} = \frac{3}{2}$. One negative $\Rightarrow -\frac{3}{2}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{1}{3}\right) \times \left(-\dfrac{1}{3}\right) \times \left(-\dfrac{1}{3}\right)$",
                'answer': r"$-\dfrac{1}{27}$",
                'wrong': [r"$\dfrac{1}{27}$", r"$-\dfrac{1}{9}$", r"$\dfrac{1}{9}$"],
                'explanation': r"Three negative factors $\Rightarrow$ negative result. $\frac{1}{3} \times \frac{1}{3} \times \frac{1}{3} = \frac{1}{27}$, so the answer is $-\frac{1}{27}$."
            },
            {
                'question': r"Evaluate: $\dfrac{9}{16} \times \left(-\dfrac{8}{3}\right)$",
                'answer': r"$-\dfrac{3}{2}$",
                'wrong': [r"$\dfrac{3}{2}$", r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$"],
                'explanation': r"$\frac{9 \times 8}{16 \times 3} = \frac{72}{48} = \frac{3}{2}$. One negative $\Rightarrow -\frac{3}{2}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{5}{4}\right) \times \left(-\dfrac{4}{5}\right)$",
                'answer': r"$1$",
                'wrong': [r"$-1$", r"$\dfrac{25}{16}$", r"$-\dfrac{25}{16}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{5}{4} \times \frac{4}{5} = 1$, so the answer is $1$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{7}{12}\right) \times \dfrac{4}{7}$",
                'answer': r"$-\dfrac{1}{3}$",
                'wrong': [r"$\dfrac{1}{3}$", r"$-\dfrac{4}{12}$", r"$\dfrac{28}{84}$"],
                'explanation': r"$\frac{7 \times 4}{12 \times 7} = \frac{28}{84} = \frac{1}{3}$. One negative $\Rightarrow -\frac{1}{3}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{2}{5}\right)^2 \times \left(-5\right)$",
                'answer': r"$-\dfrac{4}{5}$",
                'wrong': [r"$\dfrac{4}{5}$", r"$-4$", r"$4$"],
                'explanation': r"$\left(-\frac{2}{5}\right)^2 = \frac{4}{25}$. Then $\frac{4}{25} \times (-5) = -\frac{20}{25} = -\frac{4}{5}$."
            },
            {
                'question': r"Evaluate: $6 \times \left(-\dfrac{5}{12}\right)$",
                'answer': r"$-\dfrac{5}{2}$",
                'wrong': [r"$\dfrac{5}{2}$", r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$"],
                'explanation': r"$\frac{6 \times 5}{12} = \frac{30}{12} = \frac{5}{2}$. One negative $\Rightarrow -\frac{5}{2}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{3}{8}\right) \times \left(-\dfrac{8}{9}\right)$",
                'answer': r"$\dfrac{1}{3}$",
                'wrong': [r"$-\dfrac{1}{3}$", r"$\dfrac{3}{9}$", r"$-\dfrac{3}{9}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{3 \times 8}{8 \times 9} = \frac{24}{72} = \frac{1}{3}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{1}{2}\right)^4$",
                'answer': r"$\dfrac{1}{16}$",
                'wrong': [r"$-\dfrac{1}{16}$", r"$\dfrac{1}{8}$", r"$-\dfrac{1}{8}$"],
                'explanation': r"Even exponent $\Rightarrow$ positive. $\left(\frac{1}{2}\right)^4 = \frac{1}{16}$, so $\left(-\frac{1}{2}\right)^4 = \frac{1}{16}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{2}{7}\right) \times \dfrac{7}{4} \times \left(-2\right)$",
                'answer': r"$1$",
                'wrong': [r"$-1$", r"$\dfrac{1}{2}$", r"$-\dfrac{1}{2}$"],
                'explanation': r"Two negative factors $\Rightarrow$ positive overall. $\frac{2}{7} \times \frac{7}{4} \times 2 = \frac{2 \times 7 \times 2}{7 \times 4} = \frac{28}{28} = 1$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{5}{3}\right) \times \dfrac{9}{25}$",
                'answer': r"$-\dfrac{3}{5}$",
                'wrong': [r"$\dfrac{3}{5}$", r"$-\dfrac{45}{75}$", r"$\dfrac{1}{5}$"],
                'explanation': r"$\frac{5 \times 9}{3 \times 25} = \frac{45}{75} = \frac{3}{5}$. One negative $\Rightarrow -\frac{3}{5}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{3}{4}\right) \times \left(-\dfrac{4}{3}\right) \times \left(-1\right)$",
                'answer': r"$-1$",
                'wrong': [r"$1$", r"$-\dfrac{9}{16}$", r"$\dfrac{9}{16}$"],
                'explanation': r"Three negative factors $\Rightarrow$ negative. $\frac{3}{4} \times \frac{4}{3} \times 1 = 1$, so with three negatives: $-1$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{11}{6}\right) \times \dfrac{12}{11}$",
                'answer': r"$-2$",
                'wrong': [r"$2$", r"$-\dfrac{1}{2}$", r"$\dfrac{132}{66}$"],
                'explanation': r"$\frac{11 \times 12}{6 \times 11} = \frac{132}{66} = 2$. One negative $\Rightarrow -2$."
            },

            # ═══════════════════════════════════════════════════════════════════════════
            # SECTION 4 — DIVISION WITH FRACTIONS (25 problems)
            # ═══════════════════════════════════════════════════════════════════════════

            {
                'question': r"Evaluate: $\left(-\dfrac{3}{4}\right) \div \dfrac{3}{8}$",
                'answer': r"$-2$",
                'wrong': [r"$2$", r"$-\dfrac{9}{32}$", r"$\dfrac{9}{32}$"],
                'explanation': r"Dividing by a fraction $=$ multiplying by its reciprocal. $-\frac{3}{4} \times \frac{8}{3} = -\frac{24}{12} = -2$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{2}{5}\right) \div \left(-\dfrac{4}{5}\right)$",
                'answer': r"$\dfrac{1}{2}$",
                'wrong': [r"$-\dfrac{1}{2}$", r"$2$", r"$-2$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{2}{5} \times \frac{5}{4} = \frac{10}{20} = \frac{1}{2}$."
            },
            {
                'question': r"Evaluate: $\dfrac{5}{6} \div \left(-\dfrac{5}{3}\right)$",
                'answer': r"$-\dfrac{1}{2}$",
                'wrong': [r"$\dfrac{1}{2}$", r"$-\dfrac{25}{18}$", r"$\dfrac{25}{18}$"],
                'explanation': r"$\frac{5}{6} \times \left(-\frac{3}{5}\right) = -\frac{15}{30} = -\frac{1}{2}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{7}{8}\right) \div \dfrac{7}{4}$",
                'answer': r"$-\dfrac{1}{2}$",
                'wrong': [r"$\dfrac{1}{2}$", r"$-\dfrac{49}{32}$", r"$\dfrac{49}{32}$"],
                'explanation': r"$-\frac{7}{8} \times \frac{4}{7} = -\frac{28}{56} = -\frac{1}{2}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{1}{3}\right) \div \left(-\dfrac{1}{6}\right)$",
                'answer': r"$2$",
                'wrong': [r"$-2$", r"$\dfrac{1}{18}$", r"$-\dfrac{1}{18}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{1}{3} \times \frac{6}{1} = \frac{6}{3} = 2$."
            },
            {
                'question': r"Evaluate: $\left(-6\right) \div \left(-\dfrac{3}{4}\right)$",
                'answer': r"$8$",
                'wrong': [r"$-8$", r"$\dfrac{9}{2}$", r"$-\dfrac{9}{2}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $6 \times \frac{4}{3} = \frac{24}{3} = 8$."
            },
            {
                'question': r"Evaluate: $\dfrac{4}{9} \div \left(-\dfrac{8}{3}\right)$",
                'answer': r"$-\dfrac{1}{6}$",
                'wrong': [r"$\dfrac{1}{6}$", r"$-\dfrac{32}{27}$", r"$\dfrac{32}{27}$"],
                'explanation': r"$\frac{4}{9} \times \left(-\frac{3}{8}\right) = -\frac{12}{72} = -\frac{1}{6}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{5}{12}\right) \div \dfrac{5}{6}$",
                'answer': r"$-\dfrac{1}{2}$",
                'wrong': [r"$\dfrac{1}{2}$", r"$-\dfrac{25}{72}$", r"$\dfrac{25}{72}$"],
                'explanation': r"$-\frac{5}{12} \times \frac{6}{5} = -\frac{30}{60} = -\frac{1}{2}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{9}{10}\right) \div \left(-\dfrac{3}{5}\right)$",
                'answer': r"$\dfrac{3}{2}$",
                'wrong': [r"$-\dfrac{3}{2}$", r"$\dfrac{27}{50}$", r"$-\dfrac{27}{50}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{9}{10} \times \frac{5}{3} = \frac{45}{30} = \frac{3}{2}$."
            },
            {
                'question': r"Evaluate: $\dfrac{3}{7} \div \left(-\dfrac{9}{14}\right)$",
                'answer': r"$-\dfrac{2}{3}$",
                'wrong': [r"$\dfrac{2}{3}$", r"$-\dfrac{27}{98}$", r"$\dfrac{27}{98}$"],
                'explanation': r"$\frac{3}{7} \times \left(-\frac{14}{9}\right) = -\frac{42}{63} = -\frac{2}{3}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{1}{2}\right) \div \dfrac{3}{4}$",
                'answer': r"$-\dfrac{2}{3}$",
                'wrong': [r"$\dfrac{2}{3}$", r"$-\dfrac{3}{8}$", r"$\dfrac{3}{8}$"],
                'explanation': r"$-\frac{1}{2} \times \frac{4}{3} = -\frac{4}{6} = -\frac{2}{3}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{4}{3}\right) \div \left(-\dfrac{2}{9}\right)$",
                'answer': r"$6$",
                'wrong': [r"$-6$", r"$\dfrac{8}{27}$", r"$-\dfrac{8}{27}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{4}{3} \times \frac{9}{2} = \frac{36}{6} = 6$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{5}{8}\right) \div \left(-\dfrac{15}{4}\right)$",
                'answer': r"$\dfrac{1}{6}$",
                'wrong': [r"$-\dfrac{1}{6}$", r"$\dfrac{75}{32}$", r"$-\dfrac{75}{32}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{5}{8} \times \frac{4}{15} = \frac{20}{120} = \frac{1}{6}$."
            },
            {
                'question': r"Evaluate: $\dfrac{2}{3} \div \left(-4\right)$",
                'answer': r"$-\dfrac{1}{6}$",
                'wrong': [r"$\dfrac{1}{6}$", r"$-\dfrac{8}{3}$", r"$\dfrac{8}{3}$"],
                'explanation': r"$\frac{2}{3} \div (-4) = \frac{2}{3} \times \left(-\frac{1}{4}\right) = -\frac{2}{12} = -\frac{1}{6}$."
            },
            {
                'question': r"Evaluate: $\left(-8\right) \div \dfrac{4}{3}$",
                'answer': r"$-6$",
                'wrong': [r"$6$", r"$-\dfrac{32}{3}$", r"$\dfrac{32}{3}$"],
                'explanation': r"$-8 \times \frac{3}{4} = -\frac{24}{4} = -6$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{11}{4}\right) \div \left(-\dfrac{11}{8}\right)$",
                'answer': r"$2$",
                'wrong': [r"$-2$", r"$\dfrac{1}{2}$", r"$-\dfrac{1}{2}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{11}{4} \times \frac{8}{11} = \frac{88}{44} = 2$."
            },
            {
                'question': r"Evaluate: $\dfrac{7}{10} \div \left(-\dfrac{7}{5}\right)$",
                'answer': r"$-\dfrac{1}{2}$",
                'wrong': [r"$\dfrac{1}{2}$", r"$-\dfrac{49}{50}$", r"$\dfrac{49}{50}$"],
                'explanation': r"$\frac{7}{10} \times \left(-\frac{5}{7}\right) = -\frac{35}{70} = -\frac{1}{2}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{3}{5}\right) \div \left(-\dfrac{9}{10}\right)$",
                'answer': r"$\dfrac{2}{3}$",
                'wrong': [r"$-\dfrac{2}{3}$", r"$\dfrac{27}{50}$", r"$-\dfrac{27}{50}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{3}{5} \times \frac{10}{9} = \frac{30}{45} = \frac{2}{3}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{1}{6}\right) \div \dfrac{5}{12}$",
                'answer': r"$-\dfrac{2}{5}$",
                'wrong': [r"$\dfrac{2}{5}$", r"$-\dfrac{5}{72}$", r"$\dfrac{5}{72}$"],
                'explanation': r"$-\frac{1}{6} \times \frac{12}{5} = -\frac{12}{30} = -\frac{2}{5}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{8}{15}\right) \div \left(-\dfrac{4}{5}\right)$",
                'answer': r"$\dfrac{2}{3}$",
                'wrong': [r"$-\dfrac{2}{3}$", r"$\dfrac{32}{75}$", r"$-\dfrac{32}{75}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{8}{15} \times \frac{5}{4} = \frac{40}{60} = \frac{2}{3}$."
            },
            {
                'question': r"Evaluate: $\dfrac{5}{6} \div \left(-\dfrac{10}{9}\right)$",
                'answer': r"$-\dfrac{3}{4}$",
                'wrong': [r"$\dfrac{3}{4}$", r"$-\dfrac{50}{54}$", r"$\dfrac{50}{54}$"],
                'explanation': r"$\frac{5}{6} \times \left(-\frac{9}{10}\right) = -\frac{45}{60} = -\frac{3}{4}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{7}{3}\right) \div 14$",
                'answer': r"$-\dfrac{1}{6}$",
                'wrong': [r"$\dfrac{1}{6}$", r"$-\dfrac{98}{3}$", r"$\dfrac{98}{3}$"],
                'explanation': r"$-\frac{7}{3} \times \frac{1}{14} = -\frac{7}{42} = -\frac{1}{6}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{2}{3}\right) \div \left(-\dfrac{8}{3}\right)$",
                'answer': r"$\dfrac{1}{4}$",
                'wrong': [r"$-\dfrac{1}{4}$", r"$\dfrac{16}{9}$", r"$-\dfrac{16}{9}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{2}{3} \times \frac{3}{8} = \frac{6}{24} = \frac{1}{4}$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{9}{4}\right) \div \left(-\dfrac{3}{8}\right)$",
                'answer': r"$6$",
                'wrong': [r"$-6$", r"$\dfrac{27}{32}$", r"$-\dfrac{27}{32}$"],
                'explanation': r"Two negatives $\Rightarrow$ positive. $\frac{9}{4} \times \frac{8}{3} = \frac{72}{12} = 6$."
            },
            {
                'question': r"Evaluate: $\left(-\dfrac{5}{14}\right) \div \dfrac{15}{7}$",
                'answer': r"$-\dfrac{1}{6}$",
                'wrong': [r"$\dfrac{1}{6}$", r"$-\dfrac{75}{98}$", r"$\dfrac{75}{98}$"],
                'explanation': r"$-\frac{5}{14} \times \frac{7}{15} = -\frac{35}{210} = -\frac{1}{6}$."
            }

        ]

}
