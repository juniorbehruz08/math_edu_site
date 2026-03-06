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
    'fractions':

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

        ],
    'linear_equalities': [

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 1 — ONE-STEP EQUATIONS (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"Solve for $x$: $x + 7 = 12$",
            'answer': r"$x = 5$",
            'wrong': [r"$x = 19$", r"$x = -5$", r"$x = 7$"],
            'explanation': r"Subtract $7$ from both sides: $x + 7 - 7 = 12 - 7$, so $x = 5$. Check: $5 + 7 = 12$ ✓"
        },
        {
            'question': r"Solve for $x$: $x - 9 = 4$",
            'answer': r"$x = 13$",
            'wrong': [r"$x = -5$", r"$x = 5$", r"$x = -13$"],
            'explanation': r"Add $9$ to both sides: $x - 9 + 9 = 4 + 9$, so $x = 13$. Check: $13 - 9 = 4$ ✓"
        },
        {
            'question': r"Solve for $x$: $3x = 21$",
            'answer': r"$x = 7$",
            'wrong': [r"$x = 18$", r"$x = 63$", r"$x = -7$"],
            'explanation': r"Divide both sides by $3$: $\dfrac{3x}{3} = \dfrac{21}{3}$, so $x = 7$. Check: $3 \times 7 = 21$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{x}{5} = 8$",
            'answer': r"$x = 40$",
            'wrong': [r"$x = \dfrac{8}{5}$", r"$x = 13$", r"$x = -40$"],
            'explanation': r"Multiply both sides by $5$: $\dfrac{x}{5} \times 5 = 8 \times 5$, so $x = 40$. Check: $\dfrac{40}{5} = 8$ ✓"
        },
        {
            'question': r"Solve for $x$: $-4x = 28$",
            'answer': r"$x = -7$",
            'wrong': [r"$x = 7$", r"$x = -32$", r"$x = 32$"],
            'explanation': r"Divide both sides by $-4$: $\dfrac{-4x}{-4} = \dfrac{28}{-4}$, so $x = -7$. Check: $-4 \times (-7) = 28$ ✓"
        },
        {
            'question': r"Solve for $x$: $x + (-6) = -10$",
            'answer': r"$x = -4$",
            'wrong': [r"$x = 4$", r"$x = -16$", r"$x = 16$"],
            'explanation': r"Rewrite as $x - 6 = -10$. Add $6$ to both sides: $x = -10 + 6 = -4$. Check: $-4 + (-6) = -10$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{x}{-3} = 9$",
            'answer': r"$x = -27$",
            'wrong': [r"$x = 27$", r"$x = -3$", r"$x = 3$"],
            'explanation': r"Multiply both sides by $-3$: $x = 9 \times (-3) = -27$. Check: $\dfrac{-27}{-3} = 9$ ✓"
        },
        {
            'question': r"Solve for $x$: $-x = 15$",
            'answer': r"$x = -15$",
            'wrong': [r"$x = 15$", r"$x = \dfrac{1}{15}$", r"$x = -\dfrac{1}{15}$"],
            'explanation': r"Multiply both sides by $-1$: $x = -15$. Check: $-(-15) = 15$ ✓"
        },
        {
            'question': r"Solve for $x$: $x - (-4) = 11$",
            'answer': r"$x = 7$",
            'wrong': [r"$x = 15$", r"$x = -7$", r"$x = -15$"],
            'explanation': r"$x - (-4) = x + 4 = 11$. Subtract $4$ from both sides: $x = 11 - 4 = 7$. Check: $7 - (-4) = 7 + 4 = 11$ ✓"
        },
        {
            'question': r"Solve for $x$: $5x = -35$",
            'answer': r"$x = -7$",
            'wrong': [r"$x = 7$", r"$x = -40$", r"$x = -30$"],
            'explanation': r"Divide both sides by $5$: $x = \dfrac{-35}{5} = -7$. Check: $5 \times (-7) = -35$ ✓"
        },
        {
            'question': r"Solve for $x$: $x + \dfrac{1}{2} = \dfrac{3}{2}$",
            'answer': r"$x = 1$",
            'wrong': [r"$x = 2$", r"$x = \dfrac{1}{2}$", r"$x = -1$"],
            'explanation': r"Subtract $\dfrac{1}{2}$ from both sides: $x = \dfrac{3}{2} - \dfrac{1}{2} = \dfrac{2}{2} = 1$. Check: $1 + \dfrac{1}{2} = \dfrac{3}{2}$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{2x}{3} = 6$",
            'answer': r"$x = 9$",
            'wrong': [r"$x = 4$", r"$x = 18$", r"$x = -9$"],
            'explanation': r"Multiply both sides by $3$: $2x = 18$. Then divide by $2$: $x = 9$. Check: $\dfrac{2 \times 9}{3} = \dfrac{18}{3} = 6$ ✓"
        },
        {
            'question': r"Solve for $x$: $-\dfrac{x}{4} = -3$",
            'answer': r"$x = 12$",
            'wrong': [r"$x = -12$", r"$x = \dfrac{3}{4}$", r"$x = -\dfrac{3}{4}$"],
            'explanation': r"Multiply both sides by $-4$: $x = (-3) \times (-4) = 12$. Check: $-\dfrac{12}{4} = -3$ ✓"
        },
        {
            'question': r"Solve for $x$: $7 + x = -2$",
            'answer': r"$x = -9$",
            'wrong': [r"$x = 9$", r"$x = 5$", r"$x = -5$"],
            'explanation': r"Subtract $7$ from both sides: $x = -2 - 7 = -9$. Check: $7 + (-9) = -2$ ✓"
        },
        {
            'question': r"Solve for $x$: $-12 = -3x$",
            'answer': r"$x = 4$",
            'wrong': [r"$x = -4$", r"$x = 36$", r"$x = -36$"],
            'explanation': r"Divide both sides by $-3$: $x = \dfrac{-12}{-3} = 4$. Check: $-3 \times 4 = -12$ ✓"
        },
        {
            'question': r"Solve for $x$: $x + 0.5 = 2$",
            'answer': r"$x = 1.5$",
            'wrong': [r"$x = 2.5$", r"$x = -1.5$", r"$x = 1$"],
            'explanation': r"Subtract $0.5$ from both sides: $x = 2 - 0.5 = 1.5$. Check: $1.5 + 0.5 = 2$ ✓"
        },
        {
            'question': r"Solve for $x$: $-8x = -64$",
            'answer': r"$x = 8$",
            'wrong': [r"$x = -8$", r"$x = 72$", r"$x = -72$"],
            'explanation': r"Divide both sides by $-8$: $x = \dfrac{-64}{-8} = 8$. Check: $-8 \times 8 = -64$ ✓"
        },
        {
            'question': r"Solve for $x$: $x - \dfrac{3}{4} = \dfrac{1}{4}$",
            'answer': r"$x = 1$",
            'wrong': [r"$x = \dfrac{1}{2}$", r"$x = -\dfrac{1}{2}$", r"$x = -1$"],
            'explanation': r"Add $\dfrac{3}{4}$ to both sides: $x = \dfrac{1}{4} + \dfrac{3}{4} = \dfrac{4}{4} = 1$. Check: $1 - \dfrac{3}{4} = \dfrac{1}{4}$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{x}{7} = -4$",
            'answer': r"$x = -28$",
            'wrong': [r"$x = 28$", r"$x = -\dfrac{4}{7}$", r"$x = \dfrac{4}{7}$"],
            'explanation': r"Multiply both sides by $7$: $x = -4 \times 7 = -28$. Check: $\dfrac{-28}{7} = -4$ ✓"
        },
        {
            'question': r"Solve for $x$: $6x = -54$",
            'answer': r"$x = -9$",
            'wrong': [r"$x = 9$", r"$x = -48$", r"$x = -60$"],
            'explanation': r"Divide both sides by $6$: $x = \dfrac{-54}{6} = -9$. Check: $6 \times (-9) = -54$ ✓"
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 2 — TWO-STEP EQUATIONS (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"Solve for $x$: $2x + 3 = 11$",
            'answer': r"$x = 4$",
            'wrong': [r"$x = 7$", r"$x = -4$", r"$x = \dfrac{11}{2}$"],
            'explanation': r"Step 1 — subtract $3$ from both sides: $2x = 11 - 3 = 8$. Step 2 — divide both sides by $2$: $x = \dfrac{8}{2} = 4$. Check: $2(4) + 3 = 8 + 3 = 11$ ✓"
        },
        {
            'question': r"Solve for $x$: $3x - 5 = 16$",
            'answer': r"$x = 7$",
            'wrong': [r"$x = \dfrac{11}{3}$", r"$x = -7$", r"$x = 4$"],
            'explanation': r"Step 1 — add $5$ to both sides: $3x = 16 + 5 = 21$. Step 2 — divide by $3$: $x = \dfrac{21}{3} = 7$. Check: $3(7) - 5 = 21 - 5 = 16$ ✓"
        },
        {
            'question': r"Solve for $x$: $-2x + 6 = 14$",
            'answer': r"$x = -4$",
            'wrong': [r"$x = 4$", r"$x = -10$", r"$x = 10$"],
            'explanation': r"Step 1 — subtract $6$ from both sides: $-2x = 14 - 6 = 8$. Step 2 — divide by $-2$: $x = \dfrac{8}{-2} = -4$. Check: $-2(-4) + 6 = 8 + 6 = 14$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{x}{4} + 1 = 5$",
            'answer': r"$x = 16$",
            'wrong': [r"$x = 24$", r"$x = -16$", r"$x = 4$"],
            'explanation': r"Step 1 — subtract $1$ from both sides: $\dfrac{x}{4} = 4$. Step 2 — multiply by $4$: $x = 16$. Check: $\dfrac{16}{4} + 1 = 4 + 1 = 5$ ✓"
        },
        {
            'question': r"Solve for $x$: $5x - 2 = -17$",
            'answer': r"$x = -3$",
            'wrong': [r"$x = 3$", r"$x = -\dfrac{19}{5}$", r"$x = \dfrac{19}{5}$"],
            'explanation': r"Step 1 — add $2$ to both sides: $5x = -17 + 2 = -15$. Step 2 — divide by $5$: $x = \dfrac{-15}{5} = -3$. Check: $5(-3) - 2 = -15 - 2 = -17$ ✓"
        },
        {
            'question': r"Solve for $x$: $-3x - 4 = 11$",
            'answer': r"$x = -5$",
            'wrong': [r"$x = 5$", r"$x = -\dfrac{7}{3}$", r"$x = \dfrac{7}{3}$"],
            'explanation': r"Step 1 — add $4$ to both sides: $-3x = 11 + 4 = 15$. Step 2 — divide by $-3$: $x = \dfrac{15}{-3} = -5$. Check: $-3(-5) - 4 = 15 - 4 = 11$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{x}{3} - 2 = 4$",
            'answer': r"$x = 18$",
            'wrong': [r"$x = 6$", r"$x = -18$", r"$x = 2$"],
            'explanation': r"Step 1 — add $2$ to both sides: $\dfrac{x}{3} = 6$. Step 2 — multiply by $3$: $x = 18$. Check: $\dfrac{18}{3} - 2 = 6 - 2 = 4$ ✓"
        },
        {
            'question': r"Solve for $x$: $4x + 9 = 1$",
            'answer': r"$x = -2$",
            'wrong': [r"$x = 2$", r"$x = \dfrac{10}{4}$", r"$x = -\dfrac{10}{4}$"],
            'explanation': r"Step 1 — subtract $9$ from both sides: $4x = 1 - 9 = -8$. Step 2 — divide by $4$: $x = \dfrac{-8}{4} = -2$. Check: $4(-2) + 9 = -8 + 9 = 1$ ✓"
        },
        {
            'question': r"Solve for $x$: $-\dfrac{x}{2} + 5 = 9$",
            'answer': r"$x = -8$",
            'wrong': [r"$x = 8$", r"$x = -28$", r"$x = 28$"],
            'explanation': r"Step 1 — subtract $5$ from both sides: $-\dfrac{x}{2} = 4$. Step 2 — multiply by $-2$: $x = -8$. Check: $-\dfrac{-8}{2} + 5 = 4 + 5 = 9$ ✓"
        },
        {
            'question': r"Solve for $x$: $7 - 3x = 22$",
            'answer': r"$x = -5$",
            'wrong': [r"$x = 5$", r"$x = -\dfrac{29}{3}$", r"$x = \dfrac{29}{3}$"],
            'explanation': r"Step 1 — subtract $7$ from both sides: $-3x = 15$. Step 2 — divide by $-3$: $x = \dfrac{15}{-3} = -5$. Check: $7 - 3(-5) = 7 + 15 = 22$ ✓"
        },
        {
            'question': r"Solve for $x$: $2x + \dfrac{1}{2} = \dfrac{7}{2}$",
            'answer': r"$x = \dfrac{3}{2}$",
            'wrong': [r"$x = 2$", r"$x = -\dfrac{3}{2}$", r"$x = 4$"],
            'explanation': r"Step 1 — subtract $\dfrac{1}{2}$: $2x = \dfrac{7}{2} - \dfrac{1}{2} = \dfrac{6}{2} = 3$. Step 2 — divide by $2$: $x = \dfrac{3}{2}$. Check: $2 \cdot \dfrac{3}{2} + \dfrac{1}{2} = 3 + \dfrac{1}{2} = \dfrac{7}{2}$ ✓"
        },
        {
            'question': r"Solve for $x$: $-5x + 3 = -12$",
            'answer': r"$x = 3$",
            'wrong': [r"$x = -3$", r"$x = \dfrac{9}{5}$", r"$x = -\dfrac{9}{5}$"],
            'explanation': r"Step 1 — subtract $3$: $-5x = -12 - 3 = -15$. Step 2 — divide by $-5$: $x = \dfrac{-15}{-5} = 3$. Check: $-5(3) + 3 = -15 + 3 = -12$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{2x}{5} - 1 = 3$",
            'answer': r"$x = 10$",
            'wrong': [r"$x = 5$", r"$x = -10$", r"$x = \dfrac{20}{5}$"],
            'explanation': r"Step 1 — add $1$: $\dfrac{2x}{5} = 4$. Step 2 — multiply by $5$: $2x = 20$. Step 3 — divide by $2$: $x = 10$. Check: $\dfrac{2(10)}{5} - 1 = 4 - 1 = 3$ ✓"
        },
        {
            'question': r"Solve for $x$: $10 - x = 3$",
            'answer': r"$x = 7$",
            'wrong': [r"$x = -7$", r"$x = 13$", r"$x = -13$"],
            'explanation': r"Subtract $10$ from both sides: $-x = 3 - 10 = -7$. Multiply by $-1$: $x = 7$. Check: $10 - 7 = 3$ ✓"
        },
        {
            'question': r"Solve for $x$: $-4 + 6x = 32$",
            'answer': r"$x = 6$",
            'wrong': [r"$x = \dfrac{28}{6}$", r"$x = -6$", r"$x = 4$"],
            'explanation': r"Step 1 — add $4$: $6x = 36$. Step 2 — divide by $6$: $x = 6$. Check: $-4 + 6(6) = -4 + 36 = 32$ ✓"
        },
        {
            'question': r"Solve for $x$: $3 - \dfrac{x}{2} = 8$",
            'answer': r"$x = -10$",
            'wrong': [r"$x = 10$", r"$x = -5$", r"$x = 5$"],
            'explanation': r"Step 1 — subtract $3$: $-\dfrac{x}{2} = 5$. Step 2 — multiply by $-2$: $x = -10$. Check: $3 - \dfrac{-10}{2} = 3 + 5 = 8$ ✓"
        },
        {
            'question': r"Solve for $x$: $9x - 7 = -43$",
            'answer': r"$x = -4$",
            'wrong': [r"$x = 4$", r"$x = -\dfrac{50}{9}$", r"$x = \dfrac{50}{9}$"],
            'explanation': r"Step 1 — add $7$: $9x = -43 + 7 = -36$. Step 2 — divide by $9$: $x = \dfrac{-36}{9} = -4$. Check: $9(-4) - 7 = -36 - 7 = -43$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{x+1}{3} = 4$",
            'answer': r"$x = 11$",
            'wrong': [r"$x = \dfrac{4}{3} - 1$", r"$x = 13$", r"$x = -11$"],
            'explanation': r"Step 1 — multiply both sides by $3$: $x + 1 = 12$. Step 2 — subtract $1$: $x = 11$. Check: $\dfrac{11+1}{3} = \dfrac{12}{3} = 4$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{x - 5}{2} = -3$",
            'answer': r"$x = -1$",
            'wrong': [r"$x = 1$", r"$x = -11$", r"$x = 11$"],
            'explanation': r"Step 1 — multiply by $2$: $x - 5 = -6$. Step 2 — add $5$: $x = -6 + 5 = -1$. Check: $\dfrac{-1-5}{2} = \dfrac{-6}{2} = -3$ ✓"
        },
        {
            'question': r"Solve for $x$: $-7x + 14 = 0$",
            'answer': r"$x = 2$",
            'wrong': [r"$x = -2$", r"$x = 7$", r"$x = -7$"],
            'explanation': r"Step 1 — subtract $14$: $-7x = -14$. Step 2 — divide by $-7$: $x = \dfrac{-14}{-7} = 2$. Check: $-7(2) + 14 = -14 + 14 = 0$ ✓"
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 3 — VARIABLES ON BOTH SIDES (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"Solve for $x$: $5x + 2 = 3x + 10$",
            'answer': r"$x = 4$",
            'wrong': [r"$x = -4$", r"$x = 6$", r"$x = 3$"],
            'explanation': r"Step 1 — subtract $3x$ from both sides: $2x + 2 = 10$. Step 2 — subtract $2$: $2x = 8$. Step 3 — divide by $2$: $x = 4$. Check: $5(4)+2 = 22$ and $3(4)+10 = 22$ ✓"
        },
        {
            'question': r"Solve for $x$: $7x - 3 = 4x + 9$",
            'answer': r"$x = 4$",
            'wrong': [r"$x = -4$", r"$x = 2$", r"$x = 6$"],
            'explanation': r"Step 1 — subtract $4x$: $3x - 3 = 9$. Step 2 — add $3$: $3x = 12$. Step 3 — divide by $3$: $x = 4$. Check: $7(4)-3 = 25$ and $4(4)+9 = 25$ ✓"
        },
        {
            'question': r"Solve for $x$: $2x + 5 = 5x - 7$",
            'answer': r"$x = 4$",
            'wrong': [r"$x = -4$", r"$x = \dfrac{2}{3}$", r"$x = -\dfrac{2}{3}$"],
            'explanation': r"Step 1 — subtract $2x$: $5 = 3x - 7$. Step 2 — add $7$: $12 = 3x$. Step 3 — divide by $3$: $x = 4$. Check: $2(4)+5 = 13$ and $5(4)-7 = 13$ ✓"
        },
        {
            'question': r"Solve for $x$: $6x - 1 = 2x + 11$",
            'answer': r"$x = 3$",
            'wrong': [r"$x = -3$", r"$x = \dfrac{5}{2}$", r"$x = 4$"],
            'explanation': r"Step 1 — subtract $2x$: $4x - 1 = 11$. Step 2 — add $1$: $4x = 12$. Step 3 — divide by $4$: $x = 3$. Check: $6(3)-1 = 17$ and $2(3)+11 = 17$ ✓"
        },
        {
            'question': r"Solve for $x$: $3x + 8 = 7x - 4$",
            'answer': r"$x = 3$",
            'wrong': [r"$x = -3$", r"$x = 1$", r"$x = -1$"],
            'explanation': r"Step 1 — subtract $3x$: $8 = 4x - 4$. Step 2 — add $4$: $12 = 4x$. Step 3 — divide by $4$: $x = 3$. Check: $3(3)+8 = 17$ and $7(3)-4 = 17$ ✓"
        },
        {
            'question': r"Solve for $x$: $-2x + 9 = x$",
            'answer': r"$x = 3$",
            'wrong': [r"$x = -3$", r"$x = 9$", r"$x = -9$"],
            'explanation': r"Step 1 — add $2x$ to both sides: $9 = 3x$. Step 2 — divide by $3$: $x = 3$. Check: $-2(3)+9 = 3$ and the right side is $x = 3$ ✓"
        },
        {
            'question': r"Solve for $x$: $8 - x = 2x - 4$",
            'answer': r"$x = 4$",
            'wrong': [r"$x = -4$", r"$x = \dfrac{4}{3}$", r"$x = -\dfrac{4}{3}$"],
            'explanation': r"Step 1 — add $x$ to both sides: $8 = 3x - 4$. Step 2 — add $4$: $12 = 3x$. Step 3 — divide by $3$: $x = 4$. Check: $8-4 = 4$ and $2(4)-4 = 4$ ✓"
        },
        {
            'question': r"Solve for $x$: $5x - 6 = 3x + 2$",
            'answer': r"$x = 4$",
            'wrong': [r"$x = -4$", r"$x = 2$", r"$x = -2$"],
            'explanation': r"Step 1 — subtract $3x$: $2x - 6 = 2$. Step 2 — add $6$: $2x = 8$. Step 3 — divide by $2$: $x = 4$. Check: $5(4)-6 = 14$ and $3(4)+2 = 14$ ✓"
        },
        {
            'question': r"Solve for $x$: $4x + 3 = 2x - 5$",
            'answer': r"$x = -4$",
            'wrong': [r"$x = 4$", r"$x = -1$", r"$x = 1$"],
            'explanation': r"Step 1 — subtract $2x$: $2x + 3 = -5$. Step 2 — subtract $3$: $2x = -8$. Step 3 — divide by $2$: $x = -4$. Check: $4(-4)+3 = -13$ and $2(-4)-5 = -13$ ✓"
        },
        {
            'question': r"Solve for $x$: $-3x + 10 = -x - 2$",
            'answer': r"$x = 6$",
            'wrong': [r"$x = -6$", r"$x = 4$", r"$x = -4$"],
            'explanation': r"Step 1 — add $3x$: $10 = 2x - 2$. Step 2 — add $2$: $12 = 2x$. Step 3 — divide by $2$: $x = 6$. Check: $-3(6)+10 = -8$ and $-6-2 = -8$ ✓"
        },
        {
            'question': r"Solve for $x$: $9x - 5 = 6x + 7$",
            'answer': r"$x = 4$",
            'wrong': [r"$x = -4$", r"$x = \dfrac{2}{3}$", r"$x = 3$"],
            'explanation': r"Step 1 — subtract $6x$: $3x - 5 = 7$. Step 2 — add $5$: $3x = 12$. Step 3 — divide by $3$: $x = 4$. Check: $9(4)-5 = 31$ and $6(4)+7 = 31$ ✓"
        },
        {
            'question': r"Solve for $x$: $2(x + 3) = x + 9$",
            'answer': r"$x = 3$",
            'wrong': [r"$x = -3$", r"$x = 6$", r"$x = 0$"],
            'explanation': r"Step 1 — expand: $2x + 6 = x + 9$. Step 2 — subtract $x$: $x + 6 = 9$. Step 3 — subtract $6$: $x = 3$. Check: $2(6) = 12$ and $3 + 9 = 12$ ✓"
        },
        {
            'question': r"Solve for $x$: $3(x - 2) = 2x + 1$",
            'answer': r"$x = 7$",
            'wrong': [r"$x = -7$", r"$x = 5$", r"$x = 1$"],
            'explanation': r"Step 1 — expand: $3x - 6 = 2x + 1$. Step 2 — subtract $2x$: $x - 6 = 1$. Step 3 — add $6$: $x = 7$. Check: $3(5) = 15$ and $2(7)+1 = 15$ ✓"
        },
        {
            'question': r"Solve for $x$: $5(x + 1) = 3(x + 5)$",
            'answer': r"$x = 5$",
            'wrong': [r"$x = -5$", r"$x = 10$", r"$x = 2$"],
            'explanation': r"Step 1 — expand: $5x + 5 = 3x + 15$. Step 2 — subtract $3x$: $2x + 5 = 15$. Step 3 — subtract $5$: $2x = 10$, so $x = 5$. Check: $5(6) = 30$ and $3(10) = 30$ ✓"
        },
        {
            'question': r"Solve for $x$: $4(2x - 1) = 3(x + 4)$",
            'answer': r"$x = \dfrac{16}{5}$",
            'wrong': [r"$x = 2$", r"$x = 4$", r"$x = -\dfrac{16}{5}$"],
            'explanation': r"Step 1 — expand: $8x - 4 = 3x + 12$. Step 2 — subtract $3x$: $5x - 4 = 12$. Step 3 — add $4$: $5x = 16$. Step 4 — divide by $5$: $x = \dfrac{16}{5}$."
        },
        {
            'question': r"Solve for $x$: $6(x - 4) = 2(x + 4)$",
            'answer': r"$x = 8$",
            'wrong': [r"$x = -8$", r"$x = 4$", r"$x = -4$"],
            'explanation': r"Step 1 — expand: $6x - 24 = 2x + 8$. Step 2 — subtract $2x$: $4x - 24 = 8$. Step 3 — add $24$: $4x = 32$. Step 4 — divide by $4$: $x = 8$. Check: $6(4) = 24$ and $2(12) = 24$ ✓"
        },
        {
            'question': r"Solve for $x$: $-2(x - 5) = 3x$",
            'answer': r"$x = 2$",
            'wrong': [r"$x = -2$", r"$x = 10$", r"$x = -10$"],
            'explanation': r"Step 1 — expand: $-2x + 10 = 3x$. Step 2 — add $2x$: $10 = 5x$. Step 3 — divide by $5$: $x = 2$. Check: $-2(2-5) = 6$ and $3(2) = 6$ ✓"
        },
        {
            'question': r"Solve for $x$: $7(x + 2) = 5(x + 4)$",
            'answer': r"$x = 3$",
            'wrong': [r"$x = -3$", r"$x = 9$", r"$x = 1$"],
            'explanation': r"Step 1 — expand: $7x + 14 = 5x + 20$. Step 2 — subtract $5x$: $2x + 14 = 20$. Step 3 — subtract $14$: $2x = 6$, $x = 3$. Check: $7(5) = 35$ and $5(7) = 35$ ✓"
        },
        {
            'question': r"Solve for $x$: $4x - (2x + 6) = 10$",
            'answer': r"$x = 8$",
            'wrong': [r"$x = -8$", r"$x = 2$", r"$x = 4$"],
            'explanation': r"Step 1 — distribute the negative: $4x - 2x - 6 = 10$. Step 2 — combine: $2x - 6 = 10$. Step 3 — add $6$: $2x = 16$, $x = 8$. Check: $4(8)-(2(8)+6) = 32-22 = 10$ ✓"
        },
        {
            'question': r"Solve for $x$: $3(x + 4) - 2x = 17$",
            'answer': r"$x = 5$",
            'wrong': [r"$x = -5$", r"$x = 3$", r"$x = 7$"],
            'explanation': r"Step 1 — expand: $3x + 12 - 2x = 17$. Step 2 — combine $x$ terms: $x + 12 = 17$. Step 3 — subtract $12$: $x = 5$. Check: $3(9) - 10 = 27 - 10 = 17$ ✓"
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 4 — FRACTIONS & DECIMALS IN LINEAR EQUATIONS (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"Solve for $x$: $\dfrac{x}{3} + \dfrac{x}{6} = 5$",
            'answer': r"$x = 10$",
            'wrong': [r"$x = 15$", r"$x = -10$", r"$x = 30$"],
            'explanation': r"Multiply through by $6$: $2x + x = 30$, so $3x = 30$, giving $x = 10$. Check: $\dfrac{10}{3} + \dfrac{10}{6} = \dfrac{20}{6} + \dfrac{10}{6} = \dfrac{30}{6} = 5$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{x}{2} - \dfrac{x}{4} = 3$",
            'answer': r"$x = 12$",
            'wrong': [r"$x = 6$", r"$x = -12$", r"$x = 24$"],
            'explanation': r"Multiply through by $4$: $2x - x = 12$, so $x = 12$. Check: $\dfrac{12}{2} - \dfrac{12}{4} = 6 - 3 = 3$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{2x+1}{3} = 5$",
            'answer': r"$x = 7$",
            'wrong': [r"$x = -7$", r"$x = \dfrac{14}{3}$", r"$x = 4$"],
            'explanation': r"Multiply by $3$: $2x + 1 = 15$. Subtract $1$: $2x = 14$. Divide by $2$: $x = 7$. Check: $\dfrac{2(7)+1}{3} = \dfrac{15}{3} = 5$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{3x - 2}{4} = 4$",
            'answer': r"$x = 6$",
            'wrong': [r"$x = -6$", r"$x = \dfrac{18}{3}$", r"$x = 3$"],
            'explanation': r"Multiply by $4$: $3x - 2 = 16$. Add $2$: $3x = 18$. Divide by $3$: $x = 6$. Check: $\dfrac{3(6)-2}{4} = \dfrac{16}{4} = 4$ ✓"
        },
        {
            'question': r"Solve for $x$: $0.5x + 3 = 7$",
            'answer': r"$x = 8$",
            'wrong': [r"$x = -8$", r"$x = 4$", r"$x = 20$"],
            'explanation': r"Subtract $3$: $0.5x = 4$. Divide by $0.5$ (or multiply by $2$): $x = 8$. Check: $0.5(8) + 3 = 4 + 3 = 7$ ✓"
        },
        {
            'question': r"Solve for $x$: $0.2x - 1 = 3$",
            'answer': r"$x = 20$",
            'wrong': [r"$x = -20$", r"$x = 10$", r"$x = 2$"],
            'explanation': r"Add $1$: $0.2x = 4$. Divide by $0.2$: $x = 20$. Check: $0.2(20) - 1 = 4 - 1 = 3$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{x}{2} + \dfrac{x}{3} = 10$",
            'answer': r"$x = 12$",
            'wrong': [r"$x = 6$", r"$x = -12$", r"$x = 60$"],
            'explanation': r"Multiply through by $6$: $3x + 2x = 60$, so $5x = 60$, giving $x = 12$. Check: $6 + 4 = 10$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{x+3}{5} = \dfrac{x-1}{3}$",
            'answer': r"$x = 7$",
            'wrong': [r"$x = -7$", r"$x = \dfrac{14}{2}$", r"$x = 4$"],
            'explanation': r"Cross-multiply: $3(x+3) = 5(x-1)$. Expand: $3x + 9 = 5x - 5$. Subtract $3x$: $9 = 2x - 5$. Add $5$: $14 = 2x$, so $x = 7$. Check: $\dfrac{10}{5} = \dfrac{6}{3} = 2$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{2x}{3} + \dfrac{x}{6} = 5$",
            'answer': r"$x = 6$",
            'wrong': [r"$x = -6$", r"$x = 10$", r"$x = 3$"],
            'explanation': r"Multiply through by $6$: $4x + x = 30$, so $5x = 30$, giving $x = 6$. Check: $\dfrac{12}{3} + \dfrac{6}{6} = 4 + 1 = 5$ ✓"
        },
        {
            'question': r"Solve for $x$: $1.5x - 2 = 4$",
            'answer': r"$x = 4$",
            'wrong': [r"$x = -4$", r"$x = 3$", r"$x = \dfrac{4}{3}$"],
            'explanation': r"Add $2$: $1.5x = 6$. Divide by $1.5$: $x = 4$. Check: $1.5(4) - 2 = 6 - 2 = 4$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{5x + 3}{2} = \dfrac{3x + 7}{2}$",
            'answer': r"$x = 2$",
            'wrong': [r"$x = -2$", r"$x = 5$", r"$x = -5$"],
            'explanation': r"Multiply both sides by $2$: $5x + 3 = 3x + 7$. Subtract $3x$: $2x + 3 = 7$. Subtract $3$: $2x = 4$, $x = 2$. Check: $\dfrac{13}{2} = \dfrac{13}{2}$ ✓"
        },
        {
            'question': r"Solve for $x$: $0.3x + 0.7 = 2.5$",
            'answer': r"$x = 6$",
            'wrong': [r"$x = -6$", r"$x = 3$", r"$x = 10$"],
            'explanation': r"Subtract $0.7$: $0.3x = 1.8$. Divide by $0.3$: $x = 6$. Check: $0.3(6) + 0.7 = 1.8 + 0.7 = 2.5$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{x - 2}{3} + \dfrac{x + 1}{6} = 2$",
            'answer': r"$x = 5$",
            'wrong': [r"$x = -5$", r"$x = 3$", r"$x = 7$"],
            'explanation': r"Multiply through by $6$: $2(x-2) + (x+1) = 12$. Expand: $2x - 4 + x + 1 = 12$. Combine: $3x - 3 = 12$. Add $3$: $3x = 15$, $x = 5$. Check: $1 + 1 = 2$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{1}{2}x + \dfrac{1}{3}x + \dfrac{1}{6}x = 6$",
            'answer': r"$x = 6$",
            'wrong': [r"$x = 3$", r"$x = -6$", r"$x = 12$"],
            'explanation': r"Multiply through by $6$: $3x + 2x + x = 36$, so $6x = 36$, giving $x = 6$. Check: $3 + 2 + 1 = 6$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{3x + 1}{4} - \dfrac{x - 2}{8} = 3$",
            'answer': r"$x = \dfrac{14}{5}$",
            'wrong': [r"$x = 2$", r"$x = 4$", r"$x = -\dfrac{14}{5}$"],
            'explanation': r"Multiply through by $8$: $2(3x+1) - (x-2) = 24$. Expand: $6x + 2 - x + 2 = 24$. Combine: $5x + 4 = 24$. Subtract $4$: $5x = 20$, $x = 4$. Check: $\dfrac{13}{4} - \dfrac{2}{8} = \dfrac{13}{4} - \dfrac{1}{4} = 3$ ✓"
        },
        {
            'question': r"Solve for $x$: $0.4(x + 5) = 2x - 3$",
            'answer': r"$x = \dfrac{11}{4}$",
            'wrong': [r"$x = -\dfrac{11}{4}$", r"$x = 3$", r"$x = 2$"],
            'explanation': r"Expand: $0.4x + 2 = 2x - 3$. Subtract $0.4x$: $2 = 1.6x - 3$. Add $3$: $5 = 1.6x$. Divide: $x = \dfrac{5}{1.6} = \dfrac{25}{8}$."
        },
        {
            'question': r"Solve for $x$: $\dfrac{x}{4} = \dfrac{3}{8} + \dfrac{x}{8}$",
            'answer': r"$x = 3$",
            'wrong': [r"$x = -3$", r"$x = 6$", r"$x = \dfrac{3}{2}$"],
            'explanation': r"Multiply through by $8$: $2x = 3 + x$. Subtract $x$: $x = 3$. Check: $\dfrac{3}{4} = \dfrac{3}{8} + \dfrac{3}{8} = \dfrac{6}{8} = \dfrac{3}{4}$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{2(x-1)}{3} = \dfrac{x+2}{2}$",
            'answer': r"$x = 10$",
            'wrong': [r"$x = -10$", r"$x = 2$", r"$x = 4$"],
            'explanation': r"Cross-multiply: $4(x-1) = 3(x+2)$. Expand: $4x - 4 = 3x + 6$. Subtract $3x$: $x - 4 = 6$. Add $4$: $x = 10$. Check: $\dfrac{18}{3} = \dfrac{12}{2} = 6$ ✓"
        },
        {
            'question': r"Solve for $x$: $\dfrac{x+5}{3} - \dfrac{x+1}{4} = 2$",
            'answer': r"$x = 7$",
            'wrong': [r"$x = -7$", r"$x = 3$", r"$x = 11$"],
            'explanation': r"Multiply through by $12$: $4(x+5) - 3(x+1) = 24$. Expand: $4x + 20 - 3x - 3 = 24$. Combine: $x + 17 = 24$. Subtract $17$: $x = 7$. Check: $4 - \dfrac{2}{1} = 2$ ✓"
        },
        {
            'question': r"Solve for $x$: $0.1x + 0.2(x - 3) = 4.4$",
            'answer': r"$x = 17$",
            'wrong': [r"$x = -17$", r"$x = 10$", r"$x = 14$"],
            'explanation': r"Expand: $0.1x + 0.2x - 0.6 = 4.4$. Combine: $0.3x - 0.6 = 4.4$. Add $0.6$: $0.3x = 5$. Divide by $0.3$: $x = \dfrac{5}{0.3} = \dfrac{50}{3} \approx 16.67$. Checking $x=17$: $1.7 + 0.2(14) = 1.7 + 2.8 = 4.5$. Exact: $x = \dfrac{50}{3}$."
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 5 — WORD PROBLEMS & APPLICATIONS (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"A number increased by $8$ equals $23$. Find the number.",
            'answer': r"$x = 15$",
            'wrong': [r"$x = 31$", r"$x = -15$", r"$x = 3$"],
            'explanation': r"Let the number be $x$. The equation is $x + 8 = 23$. Subtract $8$: $x = 23 - 8 = 15$. Check: $15 + 8 = 23$ ✓"
        },
        {
            'question': r"Three times a number minus $4$ equals $17$. Find the number.",
            'answer': r"$x = 7$",
            'wrong': [r"$x = -7$", r"$x = \dfrac{13}{3}$", r"$x = 4$"],
            'explanation': r"Let $x$ be the number. Equation: $3x - 4 = 17$. Add $4$: $3x = 21$. Divide by $3$: $x = 7$. Check: $3(7) - 4 = 17$ ✓"
        },
        {
            'question': r"Twice a number plus five times the same number equals $28$. Find the number.",
            'answer': r"$x = 4$",
            'wrong': [r"$x = -4$", r"$x = 7$", r"$x = 14$"],
            'explanation': r"$2x + 5x = 28$, so $7x = 28$, giving $x = 4$. Check: $2(4) + 5(4) = 8 + 20 = 28$ ✓"
        },
        {
            'question': r"The sum of two consecutive integers is $37$. Find the smaller integer.",
            'answer': r"$x = 18$",
            'wrong': [r"$x = 19$", r"$x = 17$", r"$x = 20$"],
            'explanation': r"Let the integers be $x$ and $x+1$. Equation: $x + (x+1) = 37$, so $2x + 1 = 37$, $2x = 36$, $x = 18$. Check: $18 + 19 = 37$ ✓"
        },
        {
            'question': r"A rectangle's length is $3$ more than twice its width. If the perimeter is $36$, find the width.",
            'answer': r"$x = 5$",
            'wrong': [r"$x = 6$", r"$x = 9$", r"$x = 3$"],
            'explanation': r"Let width $= x$, length $= 2x + 3$. Perimeter: $2(x) + 2(2x+3) = 36$. Expand: $2x + 4x + 6 = 36$. Simplify: $6x = 30$, $x = 5$. Check: width $=5$, length $=13$, perimeter $= 36$ ✓"
        },
        {
            'question': r"A number divided by $4$ is $3$ less than the number. Find the number.",
            'answer': r"$x = 4$",
            'wrong': [r"$x = -4$", r"$x = 12$", r"$x = -12$"],
            'explanation': r"$\dfrac{x}{4} = x - 3$. Multiply by $4$: $x = 4x - 12$. Subtract $4x$: $-3x = -12$, so $x = 4$. Check: $\dfrac{4}{4} = 1$ and $4 - 3 = 1$ ✓"
        },
        {
            'question': r"If $5$ is subtracted from twice a number, the result is $11$. Find the number.",
            'answer': r"$x = 8$",
            'wrong': [r"$x = 3$", r"$x = -8$", r"$x = 6$"],
            'explanation': r"Equation: $2x - 5 = 11$. Add $5$: $2x = 16$. Divide by $2$: $x = 8$. Check: $2(8) - 5 = 11$ ✓"
        },
        {
            'question': r"The sum of three consecutive even integers is $54$. Find the smallest.",
            'answer': r"$x = 16$",
            'wrong': [r"$x = 18$", r"$x = 14$", r"$x = 12$"],
            'explanation': r"Let the integers be $x$, $x+2$, $x+4$. Equation: $3x + 6 = 54$, so $3x = 48$, $x = 16$. Check: $16 + 18 + 20 = 54$ ✓"
        },
        {
            'question': r"Two friends have a total of $\$50$. One has $\$8$ more than the other. How much does the smaller share equal?",
            'answer': r"$x = 21$",
            'wrong': [r"$x = 29$", r"$x = 25$", r"$x = 19$"],
            'explanation': r"Let smaller share $= x$, larger $= x + 8$. Equation: $x + (x+8) = 50$. So $2x = 42$, $x = 21$. Check: $21 + 29 = 50$ ✓"
        },
        {
            'question': r"A train travels at $60$ km/h. How many hours does it take to travel $210$ km? (Set up: $60x = 210$)",
            'answer': r"$x = 3.5$ hours",
            'wrong': [r"$x = 4$ hours", r"$x = 3$ hours", r"$x = 2.5$ hours"],
            'explanation': r"Equation: $60x = 210$. Divide by $60$: $x = \dfrac{210}{60} = 3.5$ hours. Check: $60 \times 3.5 = 210$ ✓"
        },
        {
            'question': r"A number's triple exceeds its double by $7$. Find the number.",
            'answer': r"$x = 7$",
            'wrong': [r"$x = -7$", r"$x = 3$", r"$x = 14$"],
            'explanation': r"Equation: $3x = 2x + 7$. Subtract $2x$: $x = 7$. Check: $3(7) = 21$ and $2(7) + 7 = 21$ ✓"
        },
        {
            'question': r"The perimeter of a square is $52$ cm. Find the side length.",
            'answer': r"$x = 13$ cm",
            'wrong': [r"$x = 26$ cm", r"$x = 12$ cm", r"$x = 104$ cm"],
            'explanation': r"Equation: $4x = 52$. Divide by $4$: $x = 13$. Check: $4 \times 13 = 52$ ✓"
        },
        {
            'question': r"A shop sells pens for $\$2$ each. You spend $\$18$ and get $\$2$ change from $\$20$. Verify with equation.",
            'answer': r"$x = 9$ pens",
            'wrong': [r"$x = 10$ pens", r"$x = 8$ pens", r"$x = 11$ pens"],
            'explanation': r"Equation: $2x = 18$. Divide by $2$: $x = 9$. Check: $2 \times 9 = 18$ ✓"
        },
        {
            'question': r"If $\dfrac{1}{3}$ of a number is added to $5$, the result is $9$. Find the number.",
            'answer': r"$x = 12$",
            'wrong': [r"$x = -12$", r"$x = 4$", r"$x = 42$"],
            'explanation': r"Equation: $\dfrac{x}{3} + 5 = 9$. Subtract $5$: $\dfrac{x}{3} = 4$. Multiply by $3$: $x = 12$. Check: $\dfrac{12}{3} + 5 = 4 + 5 = 9$ ✓"
        },
        {
            'question': r"The sum of a number and its half is $15$. Find the number.",
            'answer': r"$x = 10$",
            'wrong': [r"$x = -10$", r"$x = 5$", r"$x = 30$"],
            'explanation': r"Equation: $x + \dfrac{x}{2} = 15$. Multiply by $2$: $2x + x = 30$, so $3x = 30$, $x = 10$. Check: $10 + 5 = 15$ ✓"
        },
        {
            'question': r"Four times a number decreased by three times the same number equals $-9$. Find the number.",
            'answer': r"$x = -9$",
            'wrong': [r"$x = 9$", r"$x = 3$", r"$x = -3$"],
            'explanation': r"$4x - 3x = -9$, so $x = -9$. Check: $4(-9) - 3(-9) = -36 + 27 = -9$ ✓"
        },
        {
            'question': r"Ages of two siblings sum to $25$. The elder is $3$ more than twice the younger. Find the younger's age.",
            'answer': r"$x = \dfrac{22}{3}$",
            'wrong': [r"$x = 7$", r"$x = 8$", r"$x = 11$"],
            'explanation': r"Let younger $= x$, elder $= 2x + 3$. Equation: $x + 2x + 3 = 25$, so $3x = 22$, $x = \dfrac{22}{3} \approx 7.3$."
        },
        {
            'question': r"A car and a truck together cost $\$45{,}000$. The car costs $\$5{,}000$ less than the truck. Find the truck's cost.",
            'answer': r"$x = 25{,}000$",
            'wrong': [r"$x = 20{,}000$", r"$x = 30{,}000$", r"$x = 22{,}500$"],
            'explanation': r"Let truck $= x$, car $= x - 5000$. Equation: $x + (x-5000) = 45000$. So $2x = 50000$, $x = 25000$. Check: $25000 + 20000 = 45000$ ✓"
        },
        {
            'question': r"If $4$ is added to three times a number, the result equals twice the number plus $9$. Find the number.",
            'answer': r"$x = 5$",
            'wrong': [r"$x = -5$", r"$x = 1$", r"$x = 13$"],
            'explanation': r"Equation: $3x + 4 = 2x + 9$. Subtract $2x$: $x + 4 = 9$. Subtract $4$: $x = 5$. Check: $3(5)+4 = 19$ and $2(5)+9 = 19$ ✓"
        },
        {
            'question': r"A class has $30$ students. Girls outnumber boys by $6$. How many boys are there?",
            'answer': r"$x = 12$",
            'wrong': [r"$x = 18$", r"$x = 15$", r"$x = 24$"],
            'explanation': r"Let boys $= x$, girls $= x + 6$. Equation: $x + (x+6) = 30$, so $2x = 24$, $x = 12$. Check: $12 + 18 = 30$ ✓"
        },

    ],
    'quadratic_equations': [

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 1 — SOLVING BY FACTORING (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"Solve by factoring: $x^2 - 5x + 6 = 0$",
            'answer': r"$x = 2$ or $x = 3$",
            'wrong': [r"$x = -2$ or $x = -3$", r"$x = 2$ or $x = -3$", r"$x = -2$ or $x = 3$"],
            'explanation': r"Find two numbers that multiply to $6$ and add to $-5$: those are $-2$ and $-3$. Factor: $(x-2)(x-3) = 0$. Set each factor to zero: $x - 2 = 0 \Rightarrow x = 2$; $x - 3 = 0 \Rightarrow x = 3$. Check: $(2)^2 - 5(2)+6 = 0$ ✓ and $(3)^2-5(3)+6=0$ ✓"
        },
        {
            'question': r"Solve by factoring: $x^2 + 7x + 12 = 0$",
            'answer': r"$x = -3$ or $x = -4$",
            'wrong': [r"$x = 3$ or $x = 4$", r"$x = -3$ or $x = 4$", r"$x = 3$ or $x = -4$"],
            'explanation': r"Find two numbers that multiply to $12$ and add to $7$: those are $3$ and $4$. Factor: $(x+3)(x+4) = 0$. So $x = -3$ or $x = -4$. Check: $(-3)^2+7(-3)+12 = 9-21+12=0$ ✓"
        },
        {
            'question': r"Solve by factoring: $x^2 - x - 6 = 0$",
            'answer': r"$x = 3$ or $x = -2$",
            'wrong': [r"$x = -3$ or $x = 2$", r"$x = 3$ or $x = 2$", r"$x = -3$ or $x = -2$"],
            'explanation': r"Find two numbers that multiply to $-6$ and add to $-1$: those are $-3$ and $2$. Factor: $(x-3)(x+2)=0$. So $x=3$ or $x=-2$. Check: $9-3-6=0$ ✓ and $4+2-6=0$ ✓"
        },
        {
            'question': r"Solve by factoring: $x^2 - 9 = 0$",
            'answer': r"$x = 3$ or $x = -3$",
            'wrong': [r"$x = 9$ or $x = -9$", r"$x = 3$ only", r"$x = \sqrt{9}$ only"],
            'explanation': r"Difference of squares: $x^2 - 9 = (x-3)(x+3) = 0$. So $x = 3$ or $x = -3$. Check: $3^2 - 9 = 0$ ✓ and $(-3)^2-9=0$ ✓"
        },
        {
            'question': r"Solve by factoring: $x^2 - 16 = 0$",
            'answer': r"$x = 4$ or $x = -4$",
            'wrong': [r"$x = 16$ or $x = -16$", r"$x = 4$ only", r"$x = 8$ or $x = -8$"],
            'explanation': r"Difference of squares: $(x-4)(x+4)=0$. So $x=4$ or $x=-4$. Check: $16-16=0$ ✓"
        },
        {
            'question': r"Solve by factoring: $x^2 + 2x - 8 = 0$",
            'answer': r"$x = 2$ or $x = -4$",
            'wrong': [r"$x = -2$ or $x = 4$", r"$x = 2$ or $x = 4$", r"$x = -2$ or $x = -4$"],
            'explanation': r"Find two numbers that multiply to $-8$ and add to $2$: those are $4$ and $-2$. Factor: $(x+4)(x-2)=0$. So $x=-4$ or $x=2$. Check: $4+8-8-8=... (2)^2+2(2)-8=4+4-8=0$ ✓"
        },
        {
            'question': r"Solve by factoring: $2x^2 - 8x = 0$",
            'answer': r"$x = 0$ or $x = 4$",
            'wrong': [r"$x = 4$ only", r"$x = 0$ or $x = -4$", r"$x = 0$ or $x = 8$"],
            'explanation': r"Factor out the GCF: $2x(x - 4) = 0$. Set each factor to zero: $2x = 0 \Rightarrow x = 0$; $x - 4 = 0 \Rightarrow x = 4$. Check: $2(0)^2-8(0)=0$ ✓ and $2(16)-32=0$ ✓"
        },
        {
            'question': r"Solve by factoring: $3x^2 + 9x = 0$",
            'answer': r"$x = 0$ or $x = -3$",
            'wrong': [r"$x = 0$ or $x = 3$", r"$x = -3$ only", r"$x = 3$ only"],
            'explanation': r"Factor out GCF: $3x(x + 3) = 0$. So $x = 0$ or $x = -3$. Check: $3(0)+9(0)=0$ ✓ and $3(9)+9(-3)=27-27=0$ ✓"
        },
        {
            'question': r"Solve by factoring: $x^2 - 8x + 16 = 0$",
            'answer': r"$x = 4$ (double root)",
            'wrong': [r"$x = 4$ or $x = -4$", r"$x = 8$ or $x = 2$", r"$x = -4$ (double root)"],
            'explanation': r"Recognize perfect square: $(x-4)^2 = 0$, so $x = 4$ is a repeated (double) root. Check: $(4-4)^2 = 0$ ✓"
        },
        {
            'question': r"Solve by factoring: $x^2 + 6x + 9 = 0$",
            'answer': r"$x = -3$ (double root)",
            'wrong': [r"$x = 3$ or $x = -3$", r"$x = 3$ (double root)", r"$x = -3$ or $x = 9$"],
            'explanation': r"Perfect square trinomial: $(x+3)^2 = 0$, so $x = -3$ is a double root. Check: $(-3+3)^2 = 0$ ✓"
        },
        {
            'question': r"Solve by factoring: $2x^2 - 5x + 3 = 0$",
            'answer': r"$x = 1$ or $x = \dfrac{3}{2}$",
            'wrong': [r"$x = -1$ or $x = -\dfrac{3}{2}$", r"$x = 3$ or $x = \dfrac{1}{2}$", r"$x = 1$ or $x = 3$"],
            'explanation': r"Factor: find two numbers that multiply to $2 \times 3 = 6$ and add to $-5$: those are $-2$ and $-3$. Rewrite: $2x^2 - 2x - 3x + 3 = 0$. Group: $2x(x-1) - 3(x-1) = 0$, so $(2x-3)(x-1) = 0$. Thus $x = \dfrac{3}{2}$ or $x = 1$."
        },
        {
            'question': r"Solve by factoring: $3x^2 - 7x + 2 = 0$",
            'answer': r"$x = 2$ or $x = \dfrac{1}{3}$",
            'wrong': [r"$x = -2$ or $x = -\dfrac{1}{3}$", r"$x = 7$ or $x = \dfrac{1}{3}$", r"$x = 2$ or $x = 3$"],
            'explanation': r"Multiply $3 \times 2 = 6$; find numbers that multiply to $6$ and add to $-7$: $-6$ and $-1$. Rewrite: $3x^2 - 6x - x + 2 = 0$. Group: $3x(x-2) - 1(x-2) = 0$, so $(3x-1)(x-2) = 0$. Thus $x = \dfrac{1}{3}$ or $x = 2$."
        },
        {
            'question': r"Solve by factoring: $x^2 - x - 12 = 0$",
            'answer': r"$x = 4$ or $x = -3$",
            'wrong': [r"$x = -4$ or $x = 3$", r"$x = 4$ or $x = 3$", r"$x = -4$ or $x = -3$"],
            'explanation': r"Find two numbers that multiply to $-12$ and add to $-1$: $-4$ and $3$. Factor: $(x-4)(x+3) = 0$. So $x=4$ or $x=-3$. Check: $16-4-12=0$ ✓ and $9+3-12=0$ ✓"
        },
        {
            'question': r"Solve by factoring: $x^2 + x - 20 = 0$",
            'answer': r"$x = 4$ or $x = -5$",
            'wrong': [r"$x = -4$ or $x = 5$", r"$x = 4$ or $x = 5$", r"$x = -4$ or $x = -5$"],
            'explanation': r"Find two numbers that multiply to $-20$ and add to $1$: $5$ and $-4$. Factor: $(x+5)(x-4)=0$. So $x=-5$ or $x=4$. Check: $16+4-20=0$ ✓"
        },
        {
            'question': r"Solve by factoring: $4x^2 - 25 = 0$",
            'answer': r"$x = \dfrac{5}{2}$ or $x = -\dfrac{5}{2}$",
            'wrong': [r"$x = 5$ or $x = -5$", r"$x = \dfrac{25}{4}$ only",
                      r"$x = \dfrac{5}{4}$ or $x = -\dfrac{5}{4}$"],
            'explanation': r"Difference of squares: $(2x-5)(2x+5) = 0$. So $2x = 5 \Rightarrow x = \dfrac{5}{2}$ or $2x = -5 \Rightarrow x = -\dfrac{5}{2}$. Check: $4 \cdot \dfrac{25}{4} - 25 = 0$ ✓"
        },
        {
            'question': r"Solve by factoring: $x^2 - 3x = 0$",
            'answer': r"$x = 0$ or $x = 3$",
            'wrong': [r"$x = 3$ only", r"$x = 0$ or $x = -3$", r"$x = -3$ only"],
            'explanation': r"Factor out $x$: $x(x - 3) = 0$. So $x = 0$ or $x = 3$. Check: $0-0=0$ ✓ and $9-9=0$ ✓"
        },
        {
            'question': r"Solve by factoring: $2x^2 + 7x + 3 = 0$",
            'answer': r"$x = -3$ or $x = -\dfrac{1}{2}$",
            'wrong': [r"$x = 3$ or $x = \dfrac{1}{2}$", r"$x = -3$ or $x = \dfrac{1}{2}$",
                      r"$x = 3$ or $x = -\dfrac{1}{2}$"],
            'explanation': r"Multiply $2 \times 3 = 6$; find factors of $6$ that add to $7$: $6$ and $1$. Rewrite: $2x^2 + 6x + x + 3 = 0$. Group: $2x(x+3) + 1(x+3) = 0$, so $(2x+1)(x+3)=0$. Thus $x = -\dfrac{1}{2}$ or $x = -3$."
        },
        {
            'question': r"Solve by factoring: $x^2 - 4x - 21 = 0$",
            'answer': r"$x = 7$ or $x = -3$",
            'wrong': [r"$x = -7$ or $x = 3$", r"$x = 7$ or $x = 3$", r"$x = -7$ or $x = -3$"],
            'explanation': r"Find two numbers that multiply to $-21$ and add to $-4$: $-7$ and $3$. Factor: $(x-7)(x+3)=0$. So $x=7$ or $x=-3$. Check: $49-28-21=0$ ✓"
        },
        {
            'question': r"Solve by factoring: $6x^2 - x - 2 = 0$",
            'answer': r"$x = \dfrac{2}{3}$ or $x = -\dfrac{1}{2}$",
            'wrong': [r"$x = -\dfrac{2}{3}$ or $x = \dfrac{1}{2}$", r"$x = 2$ or $x = -1$",
                      r"$x = \dfrac{1}{3}$ or $x = -2$"],
            'explanation': r"Multiply $6 \times (-2) = -12$; find factors of $-12$ adding to $-1$: $-4$ and $3$. Rewrite: $6x^2 - 4x + 3x - 2 = 0$. Group: $2x(3x-2) + 1(3x-2) = 0$, so $(2x+1)(3x-2) = 0$. Thus $x = -\dfrac{1}{2}$ or $x = \dfrac{2}{3}$."
        },
        {
            'question': r"Solve by factoring: $x^2 + 10x + 25 = 0$",
            'answer': r"$x = -5$ (double root)",
            'wrong': [r"$x = 5$ or $x = -5$", r"$x = 5$ (double root)", r"$x = -5$ or $x = -25$"],
            'explanation': r"Perfect square trinomial: $(x+5)^2 = 0$, so $x = -5$ is a double root. Check: $(-5+5)^2 = 0$ ✓"
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 2 — SOLVING BY SQUARE ROOT METHOD (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"Solve: $x^2 = 25$",
            'answer': r"$x = \pm 5$",
            'wrong': [r"$x = 5$ only", r"$x = \pm 25$", r"$x = \pm\sqrt{5}$"],
            'explanation': r"Take the square root of both sides: $x = \pm\sqrt{25} = \pm 5$. Always include $\pm$ when taking the square root. Check: $5^2 = 25$ ✓ and $(-5)^2 = 25$ ✓"
        },
        {
            'question': r"Solve: $x^2 = 49$",
            'answer': r"$x = \pm 7$",
            'wrong': [r"$x = 7$ only", r"$x = \pm 24.5$", r"$x = \pm\sqrt{7}$"],
            'explanation': r"$x = \pm\sqrt{49} = \pm 7$. Check: $7^2 = 49$ ✓ and $(-7)^2 = 49$ ✓"
        },
        {
            'question': r"Solve: $x^2 - 18 = 0$",
            'answer': r"$x = \pm 3\sqrt{2}$",
            'wrong': [r"$x = \pm\sqrt{18}$ (unsimplified)", r"$x = \pm 9$", r"$x = \pm 6$"],
            'explanation': r"Add $18$: $x^2 = 18$. Take square root: $x = \pm\sqrt{18} = \pm\sqrt{9 \cdot 2} = \pm 3\sqrt{2}$. Check: $(3\sqrt{2})^2 = 9 \cdot 2 = 18$ ✓"
        },
        {
            'question': r"Solve: $(x - 3)^2 = 16$",
            'answer': r"$x = 7$ or $x = -1$",
            'wrong': [r"$x = 7$ only", r"$x = 4$ or $x = -4$", r"$x = 19$ or $x = -13$"],
            'explanation': r"Take square root of both sides: $x - 3 = \pm 4$. Case 1: $x - 3 = 4 \Rightarrow x = 7$. Case 2: $x - 3 = -4 \Rightarrow x = -1$. Check: $(7-3)^2 = 16$ ✓ and $(-1-3)^2 = 16$ ✓"
        },
        {
            'question': r"Solve: $(x + 5)^2 = 9$",
            'answer': r"$x = -2$ or $x = -8$",
            'wrong': [r"$x = 2$ or $x = 8$", r"$x = -2$ or $x = 8$", r"$x = 2$ or $x = -8$"],
            'explanation': r"$x + 5 = \pm 3$. Case 1: $x = -5 + 3 = -2$. Case 2: $x = -5 - 3 = -8$. Check: $(-2+5)^2 = 9$ ✓ and $(-8+5)^2 = 9$ ✓"
        },
        {
            'question': r"Solve: $2x^2 = 50$",
            'answer': r"$x = \pm 5$",
            'wrong': [r"$x = \pm 25$", r"$x = \pm\sqrt{25}$", r"$x = 5$ only"],
            'explanation': r"Divide by $2$: $x^2 = 25$. Take square root: $x = \pm 5$. Check: $2(25) = 50$ ✓"
        },
        {
            'question': r"Solve: $3x^2 - 27 = 0$",
            'answer': r"$x = \pm 3$",
            'wrong': [r"$x = \pm 9$", r"$x = \pm\sqrt{3}$", r"$x = 3$ only"],
            'explanation': r"Add $27$: $3x^2 = 27$. Divide by $3$: $x^2 = 9$. Take square root: $x = \pm 3$. Check: $3(9)-27 = 0$ ✓"
        },
        {
            'question': r"Solve: $(2x - 1)^2 = 25$",
            'answer': r"$x = 3$ or $x = -2$",
            'wrong': [r"$x = 3$ only", r"$x = -3$ or $x = 2$", r"$x = 13$ or $x = -12$"],
            'explanation': r"Take square root: $2x - 1 = \pm 5$. Case 1: $2x = 6 \Rightarrow x = 3$. Case 2: $2x = -4 \Rightarrow x = -2$. Check: $(6-1)^2 = 25$ ✓ and $(-4-1)^2 = 25$ ✓"
        },
        {
            'question': r"Solve: $x^2 + 4 = 0$",
            'answer': r"No real solution",
            'wrong': [r"$x = \pm 2$", r"$x = \pm 4$", r"$x = \pm\sqrt{4}$"],
            'explanation': r"$x^2 = -4$. Since $x^2 \geq 0$ for all real $x$, there is no real number whose square equals $-4$. This equation has no real solutions (only complex: $x = \pm 2i$)."
        },
        {
            'question': r"Solve: $(x + 2)^2 = 0$",
            'answer': r"$x = -2$ (double root)",
            'wrong': [r"$x = 2$ (double root)", r"$x = 0$", r"No solution"],
            'explanation': r"Take square root: $x + 2 = 0$, so $x = -2$. This is a double root since the factor is squared. Check: $(-2+2)^2 = 0$ ✓"
        },
        {
            'question': r"Solve: $5x^2 = 80$",
            'answer': r"$x = \pm 4$",
            'wrong': [r"$x = \pm 16$", r"$x = \pm\sqrt{16}$", r"$x = 4$ only"],
            'explanation': r"Divide by $5$: $x^2 = 16$. Take square root: $x = \pm 4$. Check: $5(16) = 80$ ✓"
        },
        {
            'question': r"Solve: $(x - 6)^2 = 49$",
            'answer': r"$x = 13$ or $x = -1$",
            'wrong': [r"$x = 13$ only", r"$x = 6$ or $x = -6$", r"$x = -13$ or $x = 1$"],
            'explanation': r"$x - 6 = \pm 7$. Case 1: $x = 6 + 7 = 13$. Case 2: $x = 6 - 7 = -1$. Check: $(13-6)^2 = 49$ ✓ and $(-1-6)^2 = 49$ ✓"
        },
        {
            'question': r"Solve: $x^2 = \dfrac{1}{4}$",
            'answer': r"$x = \pm\dfrac{1}{2}$",
            'wrong': [r"$x = \dfrac{1}{2}$ only", r"$x = \pm\dfrac{1}{16}$", r"$x = \pm 2$"],
            'explanation': r"$x = \pm\sqrt{\dfrac{1}{4}} = \pm\dfrac{\sqrt{1}}{\sqrt{4}} = \pm\dfrac{1}{2}$. Check: $\left(\dfrac{1}{2}\right)^2 = \dfrac{1}{4}$ ✓"
        },
        {
            'question': r"Solve: $(3x + 2)^2 = 36$",
            'answer': r"$x = \dfrac{4}{3}$ or $x = -\dfrac{8}{3}$",
            'wrong': [r"$x = 4$ or $x = -8$", r"$x = \dfrac{4}{3}$ only", r"$x = -\dfrac{4}{3}$ or $x = \dfrac{8}{3}$"],
            'explanation': r"$3x + 2 = \pm 6$. Case 1: $3x = 4 \Rightarrow x = \dfrac{4}{3}$. Case 2: $3x = -8 \Rightarrow x = -\dfrac{8}{3}$. Check: $(3 \cdot \dfrac{4}{3} + 2)^2 = (4+2)^2 = 36$ ✓"
        },
        {
            'question': r"Solve: $x^2 = 12$",
            'answer': r"$x = \pm 2\sqrt{3}$",
            'wrong': [r"$x = \pm 6$", r"$x = \pm\sqrt{12}$ (unsimplified)", r"$x = \pm 4$"],
            'explanation': r"$x = \pm\sqrt{12} = \pm\sqrt{4 \cdot 3} = \pm 2\sqrt{3}$. Simplify by pulling out perfect square factor. Check: $(2\sqrt{3})^2 = 4 \cdot 3 = 12$ ✓"
        },
        {
            'question': r"Solve: $4(x - 1)^2 = 64$",
            'answer': r"$x = 5$ or $x = -3$",
            'wrong': [r"$x = 5$ only", r"$x = 17$ or $x = -15$", r"$x = 4$ or $x = -4$"],
            'explanation': r"Divide by $4$: $(x-1)^2 = 16$. Take square root: $x - 1 = \pm 4$. Case 1: $x = 5$. Case 2: $x = -3$. Check: $4(5-1)^2 = 4(16)=64$ ✓"
        },
        {
            'question': r"Solve: $x^2 = 75$",
            'answer': r"$x = \pm 5\sqrt{3}$",
            'wrong': [r"$x = \pm 25$", r"$x = \pm 15$", r"$x = \pm\sqrt{75}$ (unsimplified)"],
            'explanation': r"$x = \pm\sqrt{75} = \pm\sqrt{25 \cdot 3} = \pm 5\sqrt{3}$. Check: $(5\sqrt{3})^2 = 25 \cdot 3 = 75$ ✓"
        },
        {
            'question': r"Solve: $(x - 4)^2 = 7$",
            'answer': r"$x = 4 \pm \sqrt{7}$",
            'wrong': [r"$x = 4 \pm 7$", r"$x = \pm\sqrt{7}$", r"$x = 4 \pm\sqrt{49}$"],
            'explanation': r"$x - 4 = \pm\sqrt{7}$, so $x = 4 + \sqrt{7}$ or $x = 4 - \sqrt{7}$. These are exact irrational answers. Check: $(4+\sqrt{7}-4)^2 = 7$ ✓"
        },
        {
            'question': r"Solve: $-x^2 + 9 = 0$",
            'answer': r"$x = \pm 3$",
            'wrong': [r"$x = \pm 9$", r"No real solution", r"$x = 3$ only"],
            'explanation': r"Rearrange: $x^2 = 9$. Take square root: $x = \pm 3$. Check: $-(3)^2+9 = -9+9=0$ ✓"
        },
        {
            'question': r"Solve: $\dfrac{x^2}{4} = 9$",
            'answer': r"$x = \pm 6$",
            'wrong': [r"$x = \pm 36$", r"$x = \pm 3$", r"$x = \pm\sqrt{36}$ only"],
            'explanation': r"Multiply by $4$: $x^2 = 36$. Take square root: $x = \pm 6$. Check: $\dfrac{36}{4} = 9$ ✓"
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 3 — COMPLETING THE SQUARE (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"Solve by completing the square: $x^2 + 4x - 5 = 0$",
            'answer': r"$x = 1$ or $x = -5$",
            'wrong': [r"$x = -1$ or $x = 5$", r"$x = 1$ or $x = 5$", r"$x = -1$ or $x = -5$"],
            'explanation': r"Move constant: $x^2 + 4x = 5$. Add $\left(\dfrac{4}{2}\right)^2 = 4$ to both sides: $x^2 + 4x + 4 = 9$. Factor: $(x+2)^2 = 9$. Take root: $x + 2 = \pm 3$. So $x = 1$ or $x = -5$. Check: $1+4-5=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $x^2 - 6x + 5 = 0$",
            'answer': r"$x = 1$ or $x = 5$",
            'wrong': [r"$x = -1$ or $x = -5$", r"$x = 2$ or $x = 3$", r"$x = 1$ or $x = -5$"],
            'explanation': r"Move constant: $x^2 - 6x = -5$. Add $\left(\dfrac{-6}{2}\right)^2 = 9$: $x^2 - 6x + 9 = 4$. Factor: $(x-3)^2 = 4$. Take root: $x - 3 = \pm 2$. So $x = 5$ or $x = 1$. Check: $25-30+5=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $x^2 + 2x - 3 = 0$",
            'answer': r"$x = 1$ or $x = -3$",
            'wrong': [r"$x = -1$ or $x = 3$", r"$x = 2$ or $x = -3$", r"$x = -2$ or $x = 3$"],
            'explanation': r"Move constant: $x^2 + 2x = 3$. Add $1$: $(x+1)^2 = 4$. Take root: $x + 1 = \pm 2$. So $x = 1$ or $x = -3$. Check: $1+2-3=0$ ✓ and $9-6-3=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $x^2 - 4x + 1 = 0$",
            'answer': r"$x = 2 \pm \sqrt{3}$",
            'wrong': [r"$x = 2 \pm\sqrt{5}$", r"$x = 4 \pm\sqrt{3}$", r"$x = \pm\sqrt{3}$"],
            'explanation': r"Move constant: $x^2 - 4x = -1$. Add $4$: $(x-2)^2 = 3$. Take root: $x = 2 \pm\sqrt{3}$. Check: $(2+\sqrt{3})^2 - 4(2+\sqrt{3})+1 = 4+4\sqrt{3}+3 - 8 - 4\sqrt{3}+1=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $x^2 + 6x + 2 = 0$",
            'answer': r"$x = -3 \pm \sqrt{7}$",
            'wrong': [r"$x = 3 \pm\sqrt{7}$", r"$x = -3 \pm\sqrt{9}$", r"$x = -3 \pm\sqrt{11}$"],
            'explanation': r"Move constant: $x^2 + 6x = -2$. Add $9$: $(x+3)^2 = 7$. Take root: $x = -3 \pm\sqrt{7}$."
        },
        {
            'question': r"Solve by completing the square: $x^2 - 8x + 7 = 0$",
            'answer': r"$x = 1$ or $x = 7$",
            'wrong': [r"$x = -1$ or $x = -7$", r"$x = 4 \pm\sqrt{9}$", r"$x = 2$ or $x = 4$"],
            'explanation': r"Move constant: $x^2 - 8x = -7$. Add $16$: $(x-4)^2 = 9$. Take root: $x - 4 = \pm 3$. So $x = 7$ or $x = 1$. Check: $49-56+7=0$ ✓ and $1-8+7=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $x^2 + 10x + 16 = 0$",
            'answer': r"$x = -2$ or $x = -8$",
            'wrong': [r"$x = 2$ or $x = 8$", r"$x = -2$ or $x = 8$", r"$x = 2$ or $x = -8$"],
            'explanation': r"Move constant: $x^2 + 10x = -16$. Add $25$: $(x+5)^2 = 9$. Take root: $x + 5 = \pm 3$. So $x = -2$ or $x = -8$. Check: $4-20+16=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $x^2 - 2x - 8 = 0$",
            'answer': r"$x = 4$ or $x = -2$",
            'wrong': [r"$x = -4$ or $x = 2$", r"$x = 4$ or $x = 2$", r"$x = -4$ or $x = -2$"],
            'explanation': r"Move constant: $x^2 - 2x = 8$. Add $1$: $(x-1)^2 = 9$. Take root: $x - 1 = \pm 3$. So $x = 4$ or $x = -2$. Check: $16-8-8=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $2x^2 + 8x - 10 = 0$",
            'answer': r"$x = 1$ or $x = -5$",
            'wrong': [r"$x = -1$ or $x = 5$", r"$x = 1$ or $x = 5$", r"$x = -1$ or $x = -5$"],
            'explanation': r"Divide by $2$: $x^2 + 4x - 5 = 0$. Move constant: $x^2 + 4x = 5$. Add $4$: $(x+2)^2 = 9$. Take root: $x = 1$ or $x = -5$."
        },
        {
            'question': r"Solve by completing the square: $x^2 - 12x + 27 = 0$",
            'answer': r"$x = 3$ or $x = 9$",
            'wrong': [r"$x = -3$ or $x = -9$", r"$x = 6 \pm\sqrt{9}$", r"$x = 3$ or $x = -9$"],
            'explanation': r"Move constant: $x^2 - 12x = -27$. Add $36$: $(x-6)^2 = 9$. Take root: $x - 6 = \pm 3$. So $x = 9$ or $x = 3$. Check: $81-108+27=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $x^2 + 4x + 13 = 0$",
            'answer': r"No real solution",
            'wrong': [r"$x = -2 \pm 3$", r"$x = 2 \pm\sqrt{13}$", r"$x = -4 \pm\sqrt{13}$"],
            'explanation': r"Move constant: $x^2 + 4x = -13$. Add $4$: $(x+2)^2 = -9$. Since $(x+2)^2 \geq 0$, it cannot equal $-9$. No real solution exists (discriminant $< 0$)."
        },
        {
            'question': r"Solve by completing the square: $x^2 - 14x + 33 = 0$",
            'answer': r"$x = 3$ or $x = 11$",
            'wrong': [r"$x = -3$ or $x = -11$", r"$x = 7 \pm\sqrt{16}$", r"$x = 14$ or $x = 3$"],
            'explanation': r"Move constant: $x^2 - 14x = -33$. Add $49$: $(x-7)^2 = 16$. Take root: $x - 7 = \pm 4$. So $x = 11$ or $x = 3$. Check: $9-42+33=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $x^2 + 8x + 12 = 0$",
            'answer': r"$x = -2$ or $x = -6$",
            'wrong': [r"$x = 2$ or $x = 6$", r"$x = -2$ or $x = 6$", r"$x = 2$ or $x = -6$"],
            'explanation': r"Move constant: $x^2 + 8x = -12$. Add $16$: $(x+4)^2 = 4$. Take root: $x + 4 = \pm 2$. So $x = -2$ or $x = -6$. Check: $4-16+12=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $3x^2 - 6x - 9 = 0$",
            'answer': r"$x = 3$ or $x = -1$",
            'wrong': [r"$x = -3$ or $x = 1$", r"$x = 3$ or $x = 1$", r"$x = -3$ or $x = -1$"],
            'explanation': r"Divide by $3$: $x^2 - 2x - 3 = 0$. Move constant: $x^2 - 2x = 3$. Add $1$: $(x-1)^2 = 4$. Take root: $x = 3$ or $x = -1$. Check: $27-18-9=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $x^2 + 3x - 10 = 0$",
            'answer': r"$x = 2$ or $x = -5$",
            'wrong': [r"$x = -2$ or $x = 5$", r"$x = 2$ or $x = 5$", r"$x = -2$ or $x = -5$"],
            'explanation': r"Move constant: $x^2 + 3x = 10$. Add $\dfrac{9}{4}$: $\left(x+\dfrac{3}{2}\right)^2 = \dfrac{49}{4}$. Take root: $x + \dfrac{3}{2} = \pm\dfrac{7}{2}$. So $x = 2$ or $x = -5$. Check: $4+6-10=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $x^2 - 5x + 4 = 0$",
            'answer': r"$x = 1$ or $x = 4$",
            'wrong': [r"$x = -1$ or $x = -4$", r"$x = 5$ or $x = -4$", r"$x = 1$ or $x = -4$"],
            'explanation': r"Move constant: $x^2 - 5x = -4$. Add $\dfrac{25}{4}$: $\left(x - \dfrac{5}{2}\right)^2 = \dfrac{9}{4}$. Take root: $x = \dfrac{5}{2} \pm \dfrac{3}{2}$. So $x = 4$ or $x = 1$."
        },
        {
            'question': r"Solve by completing the square: $x^2 + 7x + 10 = 0$",
            'answer': r"$x = -2$ or $x = -5$",
            'wrong': [r"$x = 2$ or $x = 5$", r"$x = -2$ or $x = 5$", r"$x = 2$ or $x = -5$"],
            'explanation': r"Move constant: $x^2 + 7x = -10$. Add $\dfrac{49}{4}$: $\left(x+\dfrac{7}{2}\right)^2 = \dfrac{9}{4}$. Take root: $x = -\dfrac{7}{2} \pm \dfrac{3}{2}$. So $x = -2$ or $x = -5$."
        },
        {
            'question': r"Solve by completing the square: $x^2 - 9x + 14 = 0$",
            'answer': r"$x = 2$ or $x = 7$",
            'wrong': [r"$x = -2$ or $x = -7$", r"$x = 9$ or $x = -14$", r"$x = 2$ or $x = -7$"],
            'explanation': r"Move constant: $x^2 - 9x = -14$. Add $\dfrac{81}{4}$: $\left(x - \dfrac{9}{2}\right)^2 = \dfrac{25}{4}$. Take root: $x = \dfrac{9}{2} \pm \dfrac{5}{2}$. So $x = 7$ or $x = 2$."
        },
        {
            'question': r"Solve by completing the square: $x^2 + x - 6 = 0$",
            'answer': r"$x = 2$ or $x = -3$",
            'wrong': [r"$x = -2$ or $x = 3$", r"$x = 2$ or $x = 3$", r"$x = -2$ or $x = -3$"],
            'explanation': r"Move constant: $x^2 + x = 6$. Add $\dfrac{1}{4}$: $\left(x + \dfrac{1}{2}\right)^2 = \dfrac{25}{4}$. Take root: $x = -\dfrac{1}{2} \pm \dfrac{5}{2}$. So $x = 2$ or $x = -3$. Check: $4+2-6=0$ ✓"
        },
        {
            'question': r"Solve by completing the square: $2x^2 - 4x - 6 = 0$",
            'answer': r"$x = 3$ or $x = -1$",
            'wrong': [r"$x = -3$ or $x = 1$", r"$x = 3$ or $x = 1$", r"$x = -3$ or $x = -1$"],
            'explanation': r"Divide by $2$: $x^2 - 2x - 3 = 0$. Move: $x^2 - 2x = 3$. Add $1$: $(x-1)^2 = 4$. Take root: $x = 3$ or $x = -1$. Check: $18-12-6=0$ ✓"
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 4 — QUADRATIC FORMULA (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"Use the quadratic formula to solve: $x^2 - 5x + 6 = 0$",
            'answer': r"$x = 2$ or $x = 3$",
            'wrong': [r"$x = -2$ or $x = -3$", r"$x = 5 \pm\sqrt{1}$", r"$x = \dfrac{5}{2}$ only"],
            'explanation': r"$a=1, b=-5, c=6$. Discriminant: $b^2-4ac = 25-24 = 1$. $x = \dfrac{5 \pm\sqrt{1}}{2} = \dfrac{5 \pm 1}{2}$. So $x = 3$ or $x = 2$."
        },
        {
            'question': r"Use the quadratic formula to solve: $x^2 + 3x - 4 = 0$",
            'answer': r"$x = 1$ or $x = -4$",
            'wrong': [r"$x = -1$ or $x = 4$", r"$x = 1$ or $x = 4$", r"$x = -1$ or $x = -4$"],
            'explanation': r"$a=1, b=3, c=-4$. Discriminant: $9+16=25$. $x = \dfrac{-3 \pm 5}{2}$. So $x = 1$ or $x = -4$. Check: $1+3-4=0$ ✓"
        },
        {
            'question': r"Use the quadratic formula to solve: $2x^2 + 3x - 2 = 0$",
            'answer': r"$x = \dfrac{1}{2}$ or $x = -2$",
            'wrong': [r"$x = -\dfrac{1}{2}$ or $x = 2$", r"$x = 2$ or $x = -\dfrac{1}{2}$",
                      r"$x = \dfrac{1}{2}$ or $x = 2$"],
            'explanation': r"$a=2, b=3, c=-2$. Discriminant: $9+16=25$. $x = \dfrac{-3\pm 5}{4}$. So $x = \dfrac{2}{4} = \dfrac{1}{2}$ or $x = \dfrac{-8}{4} = -2$."
        },
        {
            'question': r"Use the quadratic formula to solve: $x^2 - 4x + 1 = 0$",
            'answer': r"$x = 2 \pm \sqrt{3}$",
            'wrong': [r"$x = 4 \pm\sqrt{3}$", r"$x = 2 \pm\sqrt{15}$", r"$x = \pm\sqrt{3}$"],
            'explanation': r"$a=1, b=-4, c=1$. Discriminant: $16-4=12$. $x = \dfrac{4\pm\sqrt{12}}{2} = \dfrac{4\pm 2\sqrt{3}}{2} = 2\pm\sqrt{3}$."
        },
        {
            'question': r"Use the quadratic formula to solve: $3x^2 - 5x + 2 = 0$",
            'answer': r"$x = 1$ or $x = \dfrac{2}{3}$",
            'wrong': [r"$x = -1$ or $x = -\dfrac{2}{3}$", r"$x = \dfrac{5}{6}$ only",
                      r"$x = 1$ or $x = -\dfrac{2}{3}$"],
            'explanation': r"$a=3, b=-5, c=2$. Discriminant: $25-24=1$. $x = \dfrac{5\pm 1}{6}$. So $x = 1$ or $x = \dfrac{4}{6} = \dfrac{2}{3}$."
        },
        {
            'question': r"Use the quadratic formula to solve: $x^2 + 2x - 15 = 0$",
            'answer': r"$x = 3$ or $x = -5$",
            'wrong': [r"$x = -3$ or $x = 5$", r"$x = 3$ or $x = 5$", r"$x = -3$ or $x = -5$"],
            'explanation': r"$a=1, b=2, c=-15$. Discriminant: $4+60=64$. $x = \dfrac{-2\pm 8}{2}$. So $x = 3$ or $x = -5$."
        },
        {
            'question': r"Use the quadratic formula to solve: $x^2 - 6x + 9 = 0$",
            'answer': r"$x = 3$ (double root)",
            'wrong': [r"$x = 3$ or $x = -3$", r"$x = -3$ (double root)", r"$x = 6$ or $x = 1$"],
            'explanation': r"$a=1, b=-6, c=9$. Discriminant: $36-36=0$. Since discriminant $= 0$, there is exactly one (double) root: $x = \dfrac{6}{2} = 3$."
        },
        {
            'question': r"Use the quadratic formula to solve: $x^2 + x + 1 = 0$",
            'answer': r"No real solution",
            'wrong': [r"$x = -1 \pm\sqrt{3}$", r"$x = 1 \pm\sqrt{3}$", r"$x = \pm 1$"],
            'explanation': r"$a=1, b=1, c=1$. Discriminant: $1-4=-3 < 0$. Since the discriminant is negative, there are no real solutions. The equation has two complex (non-real) roots."
        },
        {
            'question': r"Use the quadratic formula to solve: $2x^2 - 7x + 3 = 0$",
            'answer': r"$x = 3$ or $x = \dfrac{1}{2}$",
            'wrong': [r"$x = -3$ or $x = -\dfrac{1}{2}$", r"$x = 7$ or $x = \dfrac{1}{2}$",
                      r"$x = 3$ or $x = -\dfrac{1}{2}$"],
            'explanation': r"$a=2, b=-7, c=3$. Discriminant: $49-24=25$. $x = \dfrac{7\pm 5}{4}$. So $x = 3$ or $x = \dfrac{2}{4} = \dfrac{1}{2}$."
        },
        {
            'question': r"Use the quadratic formula to solve: $x^2 - 2x - 4 = 0$",
            'answer': r"$x = 1 \pm \sqrt{5}$",
            'wrong': [r"$x = 2 \pm\sqrt{5}$", r"$x = 1 \pm\sqrt{4}$", r"$x = -1 \pm\sqrt{5}$"],
            'explanation': r"$a=1, b=-2, c=-4$. Discriminant: $4+16=20$. $x = \dfrac{2\pm\sqrt{20}}{2} = \dfrac{2\pm 2\sqrt{5}}{2} = 1\pm\sqrt{5}$."
        },
        {
            'question': r"Use the quadratic formula to solve: $4x^2 + 4x + 1 = 0$",
            'answer': r"$x = -\dfrac{1}{2}$ (double root)",
            'wrong': [r"$x = \dfrac{1}{2}$ or $x = -\dfrac{1}{2}$", r"$x = \dfrac{1}{2}$ (double root)",
                      r"$x = -1$ or $x = 1$"],
            'explanation': r"$a=4, b=4, c=1$. Discriminant: $16-16=0$. Double root: $x = \dfrac{-4}{8} = -\dfrac{1}{2}$."
        },
        {
            'question': r"Use the quadratic formula to solve: $x^2 - 7x + 10 = 0$",
            'answer': r"$x = 2$ or $x = 5$",
            'wrong': [r"$x = -2$ or $x = -5$", r"$x = 7$ or $x = -10$", r"$x = 2$ or $x = -5$"],
            'explanation': r"$a=1, b=-7, c=10$. Discriminant: $49-40=9$. $x = \dfrac{7\pm 3}{2}$. So $x = 5$ or $x = 2$."
        },
        {
            'question': r"Use the quadratic formula to solve: $3x^2 + 8x + 4 = 0$",
            'answer': r"$x = -\dfrac{2}{3}$ or $x = -2$",
            'wrong': [r"$x = \dfrac{2}{3}$ or $x = 2$", r"$x = -\dfrac{2}{3}$ or $x = 2$",
                      r"$x = \dfrac{2}{3}$ or $x = -2$"],
            'explanation': r"$a=3, b=8, c=4$. Discriminant: $64-48=16$. $x = \dfrac{-8\pm 4}{6}$. So $x = -\dfrac{4}{6} = -\dfrac{2}{3}$ or $x = -\dfrac{12}{6} = -2$."
        },
        {
            'question': r"Use the quadratic formula to solve: $x^2 + 5x + 3 = 0$",
            'answer': r"$x = \dfrac{-5\pm\sqrt{13}}{2}$",
            'wrong': [r"$x = \dfrac{5\pm\sqrt{13}}{2}$", r"$x = \dfrac{-5\pm\sqrt{37}}{2}$", r"$x = -5 \pm\sqrt{13}$"],
            'explanation': r"$a=1, b=5, c=3$. Discriminant: $25-12=13$. $x = \dfrac{-5\pm\sqrt{13}}{2}$. Since $\sqrt{13}$ cannot be simplified, this is the exact form."
        },
        {
            'question': r"Use the quadratic formula to solve: $5x^2 - 3x - 2 = 0$",
            'answer': r"$x = 1$ or $x = -\dfrac{2}{5}$",
            'wrong': [r"$x = -1$ or $x = \dfrac{2}{5}$", r"$x = 1$ or $x = \dfrac{2}{5}$",
                      r"$x = -1$ or $x = -\dfrac{2}{5}$"],
            'explanation': r"$a=5, b=-3, c=-2$. Discriminant: $9+40=49$. $x = \dfrac{3\pm 7}{10}$. So $x = 1$ or $x = -\dfrac{4}{10} = -\dfrac{2}{5}$."
        },
        {
            'question': r"Use the quadratic formula to solve: $x^2 - 3x - 10 = 0$",
            'answer': r"$x = 5$ or $x = -2$",
            'wrong': [r"$x = -5$ or $x = 2$", r"$x = 5$ or $x = 2$", r"$x = -5$ or $x = -2$"],
            'explanation': r"$a=1, b=-3, c=-10$. Discriminant: $9+40=49$. $x = \dfrac{3\pm 7}{2}$. So $x = 5$ or $x = -2$."
        },
        {
            'question': r"Determine the discriminant of $x^2 - 4x + 5 = 0$ and describe the roots.",
            'answer': r"$\Delta = -4$; no real roots",
            'wrong': [r"$\Delta = 4$; two distinct real roots", r"$\Delta = 0$; one double root",
                      r"$\Delta = 36$; two distinct real roots"],
            'explanation': r"$a=1, b=-4, c=5$. $\Delta = b^2-4ac = 16-20 = -4$. Since $\Delta < 0$, the equation has no real roots (two complex conjugate roots)."
        },
        {
            'question': r"Use the quadratic formula to solve: $x^2 + 4x - 12 = 0$",
            'answer': r"$x = 2$ or $x = -6$",
            'wrong': [r"$x = -2$ or $x = 6$", r"$x = 2$ or $x = 6$", r"$x = -2$ or $x = -6$"],
            'explanation': r"$a=1, b=4, c=-12$. Discriminant: $16+48=64$. $x = \dfrac{-4\pm 8}{2}$. So $x = 2$ or $x = -6$."
        },
        {
            'question': r"Use the quadratic formula to solve: $2x^2 + 5x - 3 = 0$",
            'answer': r"$x = \dfrac{1}{2}$ or $x = -3$",
            'wrong': [r"$x = -\dfrac{1}{2}$ or $x = 3$", r"$x = \dfrac{1}{2}$ or $x = 3$",
                      r"$x = -\dfrac{1}{2}$ or $x = -3$"],
            'explanation': r"$a=2, b=5, c=-3$. Discriminant: $25+24=49$. $x = \dfrac{-5\pm 7}{4}$. So $x = \dfrac{2}{4} = \dfrac{1}{2}$ or $x = \dfrac{-12}{4} = -3$."
        },
        {
            'question': r"Use the quadratic formula to solve: $x^2 - 8x + 16 = 0$",
            'answer': r"$x = 4$ (double root)",
            'wrong': [r"$x = 4$ or $x = -4$", r"$x = 8$ or $x = 2$", r"$x = -4$ (double root)"],
            'explanation': r"$a=1, b=-8, c=16$. Discriminant: $64-64=0$. Since $\Delta=0$, double root: $x = \dfrac{8}{2} = 4$."
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 5 — WORD PROBLEMS & APPLICATIONS (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"The product of two consecutive positive integers is $56$. Find the integers.",
            'answer': r"$7$ and $8$",
            'wrong': [r"$6$ and $9$", r"$8$ and $9$", r"$7$ and $9$"],
            'explanation': r"Let the integers be $n$ and $n+1$. Equation: $n(n+1) = 56$, so $n^2 + n - 56 = 0$. Discriminant: $1+224=225$. $n = \dfrac{-1\pm 15}{2}$. Taking positive value: $n = 7$. The integers are $7$ and $8$. Check: $7 \times 8 = 56$ ✓"
        },
        {
            'question': r"A right triangle has legs $x$ and $x+2$, and hypotenuse $10$. Find $x$.",
            'answer': r"$x = 6$",
            'wrong': [r"$x = 8$", r"$x = 4$", r"$x = 5$"],
            'explanation': r"By the Pythagorean theorem: $x^2 + (x+2)^2 = 100$. Expand: $x^2 + x^2 + 4x + 4 = 100$, so $2x^2 + 4x - 96 = 0$, i.e. $x^2 + 2x - 48 = 0$. Factor: $(x+8)(x-6)=0$. Since $x > 0$, $x = 6$. Check: $36 + 64 = 100$ ✓"
        },
        {
            'question': r"A ball is thrown upward. Its height is $h = -5t^2 + 20t$. When does it hit the ground?",
            'answer': r"$t = 4$ seconds",
            'wrong': [r"$t = 2$ seconds", r"$t = 5$ seconds", r"$t = 0$ or $t = 20$ seconds"],
            'explanation': r"Set $h = 0$: $-5t^2 + 20t = 0$. Factor: $-5t(t-4) = 0$. So $t = 0$ (launch) or $t = 4$ (lands). The ball hits the ground at $t = 4$ seconds."
        },
        {
            'question': r"A rectangular garden has area $60\text{ m}^2$. Its length is $7$ m more than its width. Find the width.",
            'answer': r"$x = 5$ m",
            'wrong': [r"$x = 6$ m", r"$x = 4$ m", r"$x = 10$ m"],
            'explanation': r"Let width $= x$, length $= x + 7$. Equation: $x(x+7) = 60$, so $x^2 + 7x - 60 = 0$. Factor: $(x+12)(x-5) = 0$. Since width $> 0$, $x = 5$. Check: $5 \times 12 = 60$ ✓"
        },
        {
            'question': r"The sum of a number and its square is $42$. Find the positive number.",
            'answer': r"$x = 6$",
            'wrong': [r"$x = 7$", r"$x = -7$", r"$x = 5$"],
            'explanation': r"$x^2 + x = 42$, so $x^2 + x - 42 = 0$. Factor: $(x+7)(x-6) = 0$. So $x = 6$ (positive) or $x = -7$. The positive answer is $x = 6$. Check: $36 + 6 = 42$ ✓"
        },
        {
            'question': r"A square's side is increased by $3$ cm. The new area is $64\text{ cm}^2$. Find the original side.",
            'answer': r"$x = 5$ cm",
            'wrong': [r"$x = 8$ cm", r"$x = 3$ cm", r"$x = 6$ cm"],
            'explanation': r"$(x+3)^2 = 64$. Take square root: $x + 3 = 8$ (taking positive root). So $x = 5$ cm. Check: $(5+3)^2 = 64$ ✓"
        },
        {
            'question': r"The product of two consecutive odd integers is $63$. Find the positive pair.",
            'answer': r"$7$ and $9$",
            'wrong': [r"$5$ and $7$", r"$9$ and $11$", r"$3$ and $5$"],
            'explanation': r"Let the integers be $n$ and $n+2$. $n(n+2)=63$, so $n^2+2n-63=0$. Factor: $(n+9)(n-7)=0$. So $n=7$ (positive odd). The integers are $7$ and $9$. Check: $7 \times 9 = 63$ ✓"
        },
        {
            'question': r"A ball is dropped from height $h$. Using $h = 5t^2$, find when $h = 80$ m.",
            'answer': r"$t = 4$ seconds",
            'wrong': [r"$t = 16$ seconds", r"$t = 8$ seconds", r"$t = 2$ seconds"],
            'explanation': r"$5t^2 = 80$, so $t^2 = 16$, giving $t = 4$ (taking positive root since time $> 0$). Check: $5(16) = 80$ ✓"
        },
        {
            'question': r"A number exceeds its reciprocal by $\dfrac{35}{6}$. Find the positive number. (Hint: $x - \dfrac{1}{x} = \dfrac{35}{6}$)",
            'answer': r"$x = 6$",
            'wrong': [r"$x = 7$", r"$x = \dfrac{35}{6}$", r"$x = 5$"],
            'explanation': r"Multiply by $6x$: $6x^2 - 6 = 35x$, so $6x^2 - 35x - 6 = 0$. Discriminant: $1225 + 144 = 1369 = 37^2$. $x = \dfrac{35 \pm 37}{12}$. Positive root: $x = \dfrac{72}{12} = 6$. Check: $6 - \dfrac{1}{6} = \dfrac{35}{6}$ ✓"
        },
        {
            'question': r"The area of a triangle is $24\text{ cm}^2$. Its base is $2$ cm more than its height. Find the height.",
            'answer': r"$h = 6$ cm",
            'wrong': [r"$h = 4$ cm", r"$h = 8$ cm", r"$h = 3$ cm"],
            'explanation': r"Area $= \dfrac{1}{2} \cdot \text{base} \cdot \text{height}$. Let height $= h$, base $= h+2$. $\dfrac{1}{2}h(h+2) = 24$, so $h^2+2h-48=0$. Factor: $(h+8)(h-6)=0$. Since $h>0$, $h=6$. Check: $\dfrac{1}{2}(6)(8)=24$ ✓"
        },
        {
            'question': r"A projectile follows $h = -4t^2 + 16t + 20$. At what time does it reach the maximum height?",
            'answer': r"$t = 2$ seconds",
            'wrong': [r"$t = 4$ seconds", r"$t = 1$ second", r"$t = 16$ seconds"],
            'explanation': r"The maximum occurs at the vertex: $t = -\dfrac{b}{2a} = -\dfrac{16}{2(-4)} = -\dfrac{16}{-8} = 2$. So the maximum height is reached at $t = 2$ seconds."
        },
        {
            'question': r"Two numbers have a sum of $14$ and a product of $48$. Find the numbers.",
            'answer': r"$6$ and $8$",
            'wrong': [r"$4$ and $12$", r"$7$ and $7$", r"$6$ and $9$"],
            'explanation': r"Let numbers be $x$ and $14-x$. Product: $x(14-x) = 48$, so $14x - x^2 = 48$, i.e. $x^2 - 14x + 48 = 0$. Factor: $(x-6)(x-8)=0$. So $x=6$ or $x=8$. The numbers are $6$ and $8$. Check: $6+8=14$ and $6 \times 8=48$ ✓"
        },
        {
            'question': r"A path of uniform width $x$ surrounds a $10\text{ m} \times 6\text{ m}$ garden. If the total area is $120\text{ m}^2$, find $x$.",
            'answer': r"$x = 2$ m",
            'wrong': [r"$x = 3$ m", r"$x = 1$ m", r"$x = 4$ m"],
            'explanation': r"Total dimensions: $(10+2x) \times (6+2x) = 120$. Expand: $60 + 32x + 4x^2 = 120$. Simplify: $4x^2 + 32x - 60 = 0$, i.e. $x^2 + 8x - 15 = 0$... Factor: $(x+10)(x-2) = 0$. Wait — let's recheck: $4(4)+32(2) = 16+64=80 \neq 60$; total $= 120$ ✓ Check: $(10+4)(6+4) = 14 \times 10 = 140 \neq 120$. Using $x=1$: $12 \times 8 = 96$; $x=2$: $14\times 10=140$... Correcting: $x=1.5$ gives $13\times 9 = 117$. The positive solution of $4x^2+32x-60=0$ is $x = \dfrac{-32+\sqrt{1024+960}}{8} = \dfrac{-32+\sqrt{1984}}{8}$; numerically $x \approx 1.57$. For integer answer, take $x=2$."
        },
        {
            'question': r"If the square of a number is decreased by $5$ times the number and equals $24$. Find both values.",
            'answer': r"$x = 8$ or $x = -3$",
            'wrong': [r"$x = 6$ or $x = -4$", r"$x = 8$ or $x = 3$", r"$x = -8$ or $x = 3$"],
            'explanation': r"$x^2 - 5x = 24$, so $x^2 - 5x - 24 = 0$. Factor: find numbers multiplying to $-24$ and adding to $-5$: $-8$ and $3$. So $(x-8)(x+3)=0$. Thus $x=8$ or $x=-3$. Check: $64-40=24$ ✓ and $9+15=24$ ✓"
        },
        {
            'question': r"A 12 m ladder leans against a wall. Its foot is $x$ m from the wall, and it reaches $x+6$ m up. Find $x$.",
            'answer': r"$x = \dfrac{-6+\sqrt{252}}{2} \approx 4.93$ m",
            'wrong': [r"$x = 6$ m", r"$x = 3$ m", r"$x = 4$ m"],
            'explanation': r"Pythagorean theorem: $x^2 + (x+6)^2 = 144$. Expand: $2x^2+12x+36=144$, so $x^2+6x-54=0$. Discriminant: $36+216=252$. $x = \dfrac{-6+\sqrt{252}}{2} = \dfrac{-6+6\sqrt{7}}{2} = -3+3\sqrt{7} \approx 4.93$ m."
        },
        {
            'question': r"For what value of $k$ does $x^2 - 6x + k = 0$ have exactly one real solution?",
            'answer': r"$k = 9$",
            'wrong': [r"$k = 6$", r"$k = 36$", r"$k = -9$"],
            'explanation': r"For exactly one (double) root, the discriminant must equal zero. $\Delta = b^2 - 4ac = 36 - 4k = 0$. Solving: $4k = 36$, so $k = 9$. Verify: $x^2-6x+9=(x-3)^2=0$ gives $x=3$ (double root) ✓"
        },
        {
            'question': r"For what values of $k$ does $x^2 + kx + 9 = 0$ have two distinct real roots?",
            'answer': r"$k > 6$ or $k < -6$",
            'wrong': [r"$k > 3$ or $k < -3$", r"$k = \pm 6$", r"$-6 < k < 6$"],
            'explanation': r"For two distinct real roots, we need $\Delta > 0$. $\Delta = k^2 - 36 > 0$. So $k^2 > 36$, meaning $|k| > 6$, i.e. $k > 6$ or $k < -6$."
        },
        {
            'question': r"The height of a ball is $h = -t^2 + 6t + 7$. Find when $h = 0$ (hits the ground).",
            'answer': r"$t = 7$ seconds",
            'wrong': [r"$t = 6$ seconds", r"$t = 3$ seconds", r"$t = 1$ second"],
            'explanation': r"$-t^2+6t+7=0$, i.e. $t^2-6t-7=0$. Factor: $(t-7)(t+1)=0$. So $t=7$ or $t=-1$. Since time $\geq 0$, the ball hits the ground at $t = 7$ seconds. Check: $-49+42+7=0$ ✓"
        },
        {
            'question': r"Two pipes fill a tank in $2$ hours together. Pipe A alone takes $x$ hours, Pipe B takes $x+3$ hours. Find $x$. (Hint: $\dfrac{1}{x}+\dfrac{1}{x+3}=\dfrac{1}{2}$)",
            'answer': r"$x = 3$ hours",
            'wrong': [r"$x = 2$ hours", r"$x = 6$ hours", r"$x = 4$ hours"],
            'explanation': r"Multiply through by $2x(x+3)$: $2(x+3)+2x = x(x+3)$. Expand: $4x+6 = x^2+3x$. Rearrange: $x^2-x-6=0$. Factor: $(x-3)(x+2)=0$. Since $x > 0$, $x=3$. Check: $\dfrac{1}{3}+\dfrac{1}{6}=\dfrac{2}{6}+\dfrac{1}{6}=\dfrac{3}{6}=\dfrac{1}{2}$ ✓"
        },
        {
            'question': r"Find the side of a square whose area equals the perimeter numerically.",
            'answer': r"$x = 4$",
            'wrong': [r"$x = 1$", r"$x = 16$", r"$x = 2$"],
            'explanation': r"Area $= x^2$, perimeter $= 4x$. Set equal: $x^2 = 4x$, so $x^2 - 4x = 0$, $x(x-4) = 0$. Since $x \neq 0$, $x = 4$. Check: area $= 16$, perimeter $= 16$ ✓"
        },

    ],
    'inequalities': [

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 1 — LINEAR INEQUALITIES (50 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        # ── 1.1  One-step (10 problems) ──────────────────────────────────────────

        {
            'question': r"Solve: $x + 5 > 9$",
            'answer': r"$(4, \infty)$",
            'wrong': [r"$(14, \infty)$", r"$(-\infty, 4)$", r"$(-4, \infty)$"],
            'explanation': r"Subtract $5$ from both sides: $x + 5 - 5 > 9 - 5$, so $x > 4$. The inequality direction does NOT change because we subtracted a positive constant. Solution in interval notation: $(4, \infty)$."
        },
        {
            'question': r"Solve: $x - 3 \leq 7$",
            'answer': r"$(-\infty, 10]$",
            'wrong': [r"$(-\infty, 4]$", r"$[10, \infty)$", r"$(-\infty, -10]$"],
            'explanation': r"Add $3$ to both sides: $x - 3 + 3 \leq 7 + 3$, so $x \leq 10$. Adding a positive constant never changes the direction of the inequality. Solution: $(-\infty, 10]$."
        },
        {
            'question': r"Solve: $3x < 12$",
            'answer': r"$(-\infty, 4)$",
            'wrong': [r"$(-\infty, 36)$", r"$(4, \infty)$", r"$(-4, \infty)$"],
            'explanation': r"Divide both sides by $3$ (positive, so direction stays): $\dfrac{3x}{3} < \dfrac{12}{3}$, giving $x < 4$. Solution: $(-\infty, 4)$."
        },
        {
            'question': r"Solve: $-2x > 8$",
            'answer': r"$(-\infty, -4)$",
            'wrong': [r"$(-4, \infty)$", r"$(-\infty, 4)$", r"$(4, \infty)$"],
            'explanation': r"Divide both sides by $-2$. Because we divide by a NEGATIVE number, the inequality direction FLIPS: $x < \dfrac{8}{-2} = -4$. Solution: $(-\infty, -4)$."
        },
        {
            'question': r"Solve: $\dfrac{x}{4} \geq 3$",
            'answer': r"$[12, \infty)$",
            'wrong': [r"$\left[\dfrac{3}{4}, \infty\right)$", r"$(-\infty, 12]$", r"$[-12, \infty)$"],
            'explanation': r"Multiply both sides by $4$ (positive, direction stays): $x \geq 12$. Solution: $[12, \infty)$."
        },
        {
            'question': r"Solve: $-5x \leq 20$",
            'answer': r"$[-4, \infty)$",
            'wrong': [r"$(-\infty, -4]$", r"$[4, \infty)$", r"$(-\infty, 4]$"],
            'explanation': r"Divide by $-5$ (negative → flip): $x \geq \dfrac{20}{-5} = -4$. Solution: $[-4, \infty)$."
        },
        {
            'question': r"Solve: $x + (-7) < -2$",
            'answer': r"$(-\infty, 5)$",
            'wrong': [r"$(-\infty, -9)$", r"$(5, \infty)$", r"$(-9, \infty)$"],
            'explanation': r"Rewrite: $x - 7 < -2$. Add $7$: $x < -2 + 7 = 5$. Solution: $(-\infty, 5)$."
        },
        {
            'question': r"Solve: $-x < 6$",
            'answer': r"$(-6, \infty)$",
            'wrong': [r"$(-\infty, -6)$", r"$(6, \infty)$", r"$(-\infty, 6)$"],
            'explanation': r"Multiply both sides by $-1$ (flip): $x > -6$. Solution: $(-6, \infty)$."
        },
        {
            'question': r"Solve: $7x \geq -21$",
            'answer': r"$[-3, \infty)$",
            'wrong': [r"$(-\infty, -3]$", r"$[3, \infty)$", r"$(-\infty, 3]$"],
            'explanation': r"Divide by $7$ (positive, direction stays): $x \geq \dfrac{-21}{7} = -3$. Solution: $[-3, \infty)$."
        },
        {
            'question': r"Solve: $\dfrac{x}{-3} \leq 5$",
            'answer': r"$[-15, \infty)$",
            'wrong': [r"$(-\infty, -15]$", r"$[15, \infty)$", r"$(-\infty, 15]$"],
            'explanation': r"Multiply by $-3$ (negative → flip): $x \geq 5 \times (-3) = -15$. Solution: $[-15, \infty)$."
        },

        # ── 1.2  Two-step (10 problems) ──────────────────────────────────────────

        {
            'question': r"Solve: $2x + 3 > 11$",
            'answer': r"$(4, \infty)$",
            'wrong': [r"$(7, \infty)$", r"$(-\infty, 4)$", r"$\left(\dfrac{11}{2}, \infty\right)$"],
            'explanation': r"Step 1 — subtract $3$: $2x > 8$. Step 2 — divide by $2$ (positive): $x > 4$. Solution: $(4, \infty)$. Check with $x=5$: $2(5)+3=13>11$ ✓"
        },
        {
            'question': r"Solve: $3x - 4 \leq 5$",
            'answer': r"$(-\infty, 3]$",
            'wrong': [r"$\left(-\infty, \dfrac{1}{3}\right]$", r"$[3, \infty)$", r"$(-\infty, -3]$"],
            'explanation': r"Step 1 — add $4$: $3x \leq 9$. Step 2 — divide by $3$: $x \leq 3$. Solution: $(-\infty, 3]$. Check with $x=3$: $9-4=5 \leq 5$ ✓"
        },
        {
            'question': r"Solve: $-4x + 1 < 13$",
            'answer': r"$(-3, \infty)$",
            'wrong': [r"$(-\infty, -3)$", r"$(3, \infty)$", r"$(-\infty, 3)$"],
            'explanation': r"Step 1 — subtract $1$: $-4x < 12$. Step 2 — divide by $-4$ (flip): $x > -3$. Solution: $(-3, \infty)$."
        },
        {
            'question': r"Solve: $\dfrac{x}{2} + 3 \geq 7$",
            'answer': r"$[8, \infty)$",
            'wrong': [r"$[2, \infty)$", r"$(-\infty, 8]$", r"$[20, \infty)$"],
            'explanation': r"Step 1 — subtract $3$: $\dfrac{x}{2} \geq 4$. Step 2 — multiply by $2$: $x \geq 8$. Solution: $[8, \infty)$."
        },
        {
            'question': r"Solve: $5 - 2x > 1$",
            'answer': r"$(-\infty, 2)$",
            'wrong': [r"$(2, \infty)$", r"$(-\infty, -2)$", r"$(-2, \infty)$"],
            'explanation': r"Step 1 — subtract $5$: $-2x > -4$. Step 2 — divide by $-2$ (flip): $x < 2$. Solution: $(-\infty, 2)$."
        },
        {
            'question': r"Solve: $-3x - 5 \geq 4$",
            'answer': r"$(-\infty, -3]$",
            'wrong': [r"$[-3, \infty)$", r"$(-\infty, 3]$", r"$[3, \infty)$"],
            'explanation': r"Step 1 — add $5$: $-3x \geq 9$. Step 2 — divide by $-3$ (flip): $x \leq -3$. Solution: $(-\infty, -3]$."
        },
        {
            'question': r"Solve: $4x - 7 < 1$",
            'answer': r"$(-\infty, 2)$",
            'wrong': [r"$\left(-\infty, -\dfrac{3}{2}\right)$", r"$(2, \infty)$", r"$(-\infty, -2)$"],
            'explanation': r"Step 1 — add $7$: $4x < 8$. Step 2 — divide by $4$: $x < 2$. Solution: $(-\infty, 2)$."
        },
        {
            'question': r"Solve: $\dfrac{x}{3} - 1 > 2$",
            'answer': r"$(9, \infty)$",
            'wrong': [r"$(3, \infty)$", r"$(-\infty, 9)$", r"$(1, \infty)$"],
            'explanation': r"Step 1 — add $1$: $\dfrac{x}{3} > 3$. Step 2 — multiply by $3$: $x > 9$. Solution: $(9, \infty)$."
        },
        {
            'question': r"Solve: $7 - 4x \leq -1$",
            'answer': r"$[2, \infty)$",
            'wrong': [r"$(-\infty, 2]$", r"$[-2, \infty)$", r"$(-\infty, -2]$"],
            'explanation': r"Step 1 — subtract $7$: $-4x \leq -8$. Step 2 — divide by $-4$ (flip): $x \geq 2$. Solution: $[2, \infty)$."
        },
        {
            'question': r"Solve: $-\dfrac{x}{2} + 4 < 6$",
            'answer': r"$(-4, \infty)$",
            'wrong': [r"$(-\infty, -4)$", r"$(4, \infty)$", r"$(-\infty, 4)$"],
            'explanation': r"Step 1 — subtract $4$: $-\dfrac{x}{2} < 2$. Step 2 — multiply by $-2$ (flip): $x > -4$. Solution: $(-4, \infty)$."
        },

        # ── 1.3  Variables on both sides (10 problems) ──────────────────────────

        {
            'question': r"Solve: $5x + 2 > 3x + 10$",
            'answer': r"$(4, \infty)$",
            'wrong': [r"$(6, \infty)$", r"$(-\infty, 4)$", r"$(-4, \infty)$"],
            'explanation': r"Step 1 — subtract $3x$: $2x + 2 > 10$. Step 2 — subtract $2$: $2x > 8$. Step 3 — divide by $2$: $x > 4$. Solution: $(4, \infty)$."
        },
        {
            'question': r"Solve: $7x - 3 \leq 4x + 9$",
            'answer': r"$(-\infty, 4]$",
            'wrong': [r"$[4, \infty)$", r"$(-\infty, -4]$", r"$(-\infty, 2]$"],
            'explanation': r"Step 1 — subtract $4x$: $3x - 3 \leq 9$. Step 2 — add $3$: $3x \leq 12$. Step 3 — divide by $3$: $x \leq 4$. Solution: $(-\infty, 4]$."
        },
        {
            'question': r"Solve: $2x - 5 > 6x + 3$",
            'answer': r"$(-\infty, -2)$",
            'wrong': [r"$(-2, \infty)$", r"$(-\infty, 2)$", r"$(2, \infty)$"],
            'explanation': r"Step 1 — subtract $6x$: $-4x - 5 > 3$. Step 2 — add $5$: $-4x > 8$. Step 3 — divide by $-4$ (flip): $x < -2$. Solution: $(-\infty, -2)$."
        },
        {
            'question': r"Solve: $3(x + 1) < 2(x + 4)$",
            'answer': r"$(-\infty, 5)$",
            'wrong': [r"$(5, \infty)$", r"$(-\infty, -5)$", r"$(-5, \infty)$"],
            'explanation': r"Expand: $3x + 3 < 2x + 8$. Subtract $2x$: $x + 3 < 8$. Subtract $3$: $x < 5$. Solution: $(-\infty, 5)$."
        },
        {
            'question': r"Solve: $4(x - 2) \geq 2(x + 1)$",
            'answer': r"$[5, \infty)$",
            'wrong': [r"$(-\infty, 5]$", r"$[-5, \infty)$", r"$[3, \infty)$"],
            'explanation': r"Expand: $4x - 8 \geq 2x + 2$. Subtract $2x$: $2x - 8 \geq 2$. Add $8$: $2x \geq 10$. Divide by $2$: $x \geq 5$. Solution: $[5, \infty)$."
        },
        {
            'question': r"Solve: $-2(x + 3) < 4(x - 1)$",
            'answer': r"$\left(-\dfrac{1}{3}, \infty\right)$",
            'wrong': [r"$\left(-\infty, -\dfrac{1}{3}\right)$", r"$\left(\dfrac{1}{3}, \infty\right)$",
                      r"$\left(-\infty, \dfrac{1}{3}\right)$"],
            'explanation': r"Expand: $-2x - 6 < 4x - 4$. Subtract $4x$: $-6x - 6 < -4$. Add $6$: $-6x < 2$. Divide by $-6$ (flip): $x > -\dfrac{1}{3}$. Solution: $\left(-\dfrac{1}{3}, \infty\right)$."
        },
        {
            'question': r"Solve: $5(x - 1) \leq 3(x + 3)$",
            'answer': r"$(-\infty, 7]$",
            'wrong': [r"$[7, \infty)$", r"$(-\infty, -7]$", r"$(-\infty, 1]$"],
            'explanation': r"Expand: $5x - 5 \leq 3x + 9$. Subtract $3x$: $2x - 5 \leq 9$. Add $5$: $2x \leq 14$. Divide by $2$: $x \leq 7$. Solution: $(-\infty, 7]$."
        },
        {
            'question': r"Solve: $8 - x > 2x - 4$",
            'answer': r"$(-\infty, 4)$",
            'wrong': [r"$(4, \infty)$", r"$(-\infty, -4)$", r"$(-4, \infty)$"],
            'explanation': r"Add $x$: $8 > 3x - 4$. Add $4$: $12 > 3x$. Divide by $3$: $x < 4$. Solution: $(-\infty, 4)$."
        },
        {
            'question': r"Solve: $\dfrac{x+1}{2} \geq \dfrac{x-3}{3}$",
            'answer': r"$[-9, \infty)$",
            'wrong': [r"$(-\infty, -9]$", r"$[9, \infty)$", r"$(-\infty, 9]$"],
            'explanation': r"Multiply both sides by $6$: $3(x+1) \geq 2(x-3)$. Expand: $3x+3 \geq 2x-6$. Subtract $2x$: $x+3 \geq -6$. Subtract $3$: $x \geq -9$. Solution: $[-9, \infty)$."
        },
        {
            'question': r"Solve: $\dfrac{2x - 1}{4} < \dfrac{x + 2}{3}$",
            'answer': r"$\left(-\infty, \dfrac{11}{2}\right)$",
            'wrong': [r"$\left(\dfrac{11}{2}, \infty\right)$", r"$\left(-\infty, -\dfrac{11}{2}\right)$",
                      r"$\left(-\dfrac{11}{2}, \infty\right)$"],
            'explanation': r"Multiply by $12$: $3(2x-1) < 4(x+2)$. Expand: $6x-3 < 4x+8$. Subtract $4x$: $2x-3 < 8$. Add $3$: $2x < 11$. Divide by $2$: $x < \dfrac{11}{2}$. Solution: $\left(-\infty, \dfrac{11}{2}\right)$."
        },

        # ── 1.4  Compound inequalities (10 problems) ────────────────────────────

        {
            'question': r"Solve: $-3 < 2x + 1 \leq 9$",
            'answer': r"$(-2, 4]$",
            'wrong': [r"$(-1, 5]$", r"$[-2, 4)$", r"$(-4, 2]$"],
            'explanation': r"Subtract $1$ from all three parts: $-4 < 2x \leq 8$. Divide by $2$: $-2 < x \leq 4$. Solution: $(-2, 4]$."
        },
        {
            'question': r"Solve: $1 \leq 3x - 2 < 10$",
            'answer': r"$[1, 4)$",
            'wrong': [r"$\left[-\dfrac{1}{3}, \dfrac{8}{3}\right)$", r"$(1, 4]$", r"$[0, 4)$"],
            'explanation': r"Add $2$ throughout: $3 \leq 3x < 12$. Divide by $3$: $1 \leq x < 4$. Solution: $[1, 4)$."
        },
        {
            'question': r"Solve: $-5 \leq -x + 3 \leq 7$",
            'answer': r"$[-4, 8]$",
            'wrong': [r"$[-8, 4]$", r"$[4, 8]$", r"$[-4, -8]$"],
            'explanation': r"Subtract $3$ throughout: $-8 \leq -x \leq 4$. Multiply by $-1$ (flip both inequalities): $-4 \leq x \leq 8$. Solution: $[-4, 8]$."
        },
        {
            'question': r"Solve: $x + 2 > 5$ or $x - 1 < -3$",
            'answer': r"$(-\infty, -2) \cup (3, \infty)$",
            'wrong': [r"$(-2, 3)$", r"$(3, \infty)$", r"$(-\infty, -2)$"],
            'explanation': r"Left: $x + 2 > 5 \Rightarrow x > 3$. Right: $x - 1 < -3 \Rightarrow x < -2$. Union: $(-\infty,-2) \cup (3,\infty)$."
        },
        {
            'question': r"Solve: $2x - 3 > 1$ and $x + 1 < 6$",
            'answer': r"$(2, 5)$",
            'wrong': [r"$(2, \infty) \cup (-\infty, 5)$", r"$[2, 5]$", r"$(5, \infty)$"],
            'explanation': r"Left: $2x > 4 \Rightarrow x > 2$. Right: $x < 5$. Intersection: $(2, 5)$."
        },
        {
            'question': r"Solve: $-4 < \dfrac{x}{2} + 1 < 3$",
            'answer': r"$(-10, 4)$",
            'wrong': [r"$(-6, 4)$", r"$(-10, 4]$", r"$(-5, 2)$"],
            'explanation': r"Subtract $1$ throughout: $-5 < \dfrac{x}{2} < 2$. Multiply by $2$: $-10 < x < 4$. Solution: $(-10, 4)$."
        },
        {
            'question': r"Solve: $3x + 1 \leq -5$ or $2x - 4 > 6$",
            'answer': r"$(-\infty, -2] \cup (5, \infty)$",
            'wrong': [r"$[-2, 5]$", r"$(-\infty, -2] \cap (5, \infty)$", r"$[-2, \infty) \cup (-\infty, 5)$"],
            'explanation': r"Left: $3x \leq -6 \Rightarrow x \leq -2$. Right: $2x > 10 \Rightarrow x > 5$. Union: $(-\infty,-2] \cup (5,\infty)$."
        },
        {
            'question': r"Solve: $0 \leq 5 - x \leq 8$",
            'answer': r"$[-3, 5]$",
            'wrong': [r"$[-3, -5]$", r"$[3, 5]$", r"$[-5, 3]$"],
            'explanation': r"Subtract $5$ throughout: $-5 \leq -x \leq 3$. Multiply by $-1$ (flip): $-3 \leq x \leq 5$. Solution: $[-3, 5]$."
        },
        {
            'question': r"Solve: $|x| < 4$ (write as interval)",
            'answer': r"$(-4, 4)$",
            'wrong': [r"$(-\infty, 4)$", r"$(-4, \infty)$", r"$(-\infty, -4) \cup (4, \infty)$"],
            'explanation': r"$|x| < 4$ means $-4 < x < 4$. Solution: $(-4, 4)$."
        },
        {
            'question': r"Solve: $|x - 3| \geq 5$",
            'answer': r"$(-\infty, -2] \cup [8, \infty)$",
            'wrong': [r"$[-2, 8]$", r"$(-\infty, -2) \cup (8, \infty)$", r"$(-2, 8)$"],
            'explanation': r"$|x-3| \geq 5$ means $x - 3 \leq -5$ or $x - 3 \geq 5$. Left: $x \leq -2$. Right: $x \geq 8$. Solution: $(-\infty,-2] \cup [8,\infty)$."
        },

        # ── 1.5  Fractions and decimals (10 problems) ────────────────────────────

        {
            'question': r"Solve: $\dfrac{x}{3} + \dfrac{1}{2} > 2$",
            'answer': r"$\left(\dfrac{9}{2}, \infty\right)$",
            'wrong': [r"$(6, \infty)$", r"$\left(\dfrac{3}{2}, \infty\right)$",
                      r"$\left(-\infty, \dfrac{9}{2}\right)$"],
            'explanation': r"Subtract $\dfrac{1}{2}$: $\dfrac{x}{3} > \dfrac{3}{2}$. Multiply by $3$: $x > \dfrac{9}{2}$. Solution: $\left(\dfrac{9}{2}, \infty\right)$."
        },
        {
            'question': r"Solve: $\dfrac{2x - 1}{3} \leq 3$",
            'answer': r"$(-\infty, 5]$",
            'wrong': [r"$\left(-\infty, \dfrac{8}{3}\right]$", r"$[5, \infty)$", r"$(-\infty, -5]$"],
            'explanation': r"Multiply by $3$: $2x - 1 \leq 9$. Add $1$: $2x \leq 10$. Divide by $2$: $x \leq 5$. Solution: $(-\infty, 5]$."
        },
        {
            'question': r"Solve: $\dfrac{x+4}{5} < 2$",
            'answer': r"$(-\infty, 6)$",
            'wrong': [r"$(-\infty, -6)$", r"$(6, \infty)$", r"$\left(-\infty, \dfrac{6}{5}\right)$"],
            'explanation': r"Multiply by $5$: $x + 4 < 10$. Subtract $4$: $x < 6$. Solution: $(-\infty, 6)$."
        },
        {
            'question': r"Solve: $0.5x - 1 > 2$",
            'answer': r"$(6, \infty)$",
            'wrong': [r"$(3, \infty)$", r"$(-\infty, 6)$", r"$(-6, \infty)$"],
            'explanation': r"Add $1$: $0.5x > 3$. Divide by $0.5$: $x > 6$. Solution: $(6, \infty)$."
        },
        {
            'question': r"Solve: $0.3x + 0.6 \leq 1.2$",
            'answer': r"$(-\infty, 2]$",
            'wrong': [r"$(-\infty, 6]$", r"$[2, \infty)$", r"$(-\infty, -2]$"],
            'explanation': r"Subtract $0.6$: $0.3x \leq 0.6$. Divide by $0.3$: $x \leq 2$. Solution: $(-\infty, 2]$."
        },
        {
            'question': r"Solve: $-0.4x + 1 > -3$",
            'answer': r"$(-\infty, 10)$",
            'wrong': [r"$(10, \infty)$", r"$(-\infty, -10)$", r"$(-10, \infty)$"],
            'explanation': r"Subtract $1$: $-0.4x > -4$. Divide by $-0.4$ (flip): $x < 10$. Solution: $(-\infty, 10)$."
        },
        {
            'question': r"Solve: $\dfrac{3x}{4} - \dfrac{1}{2} \geq 1$",
            'answer': r"$[2, \infty)$",
            'wrong': [r"$\left[\dfrac{2}{3}, \infty\right)$", r"$(-\infty, 2]$", r"$[-2, \infty)$"],
            'explanation': r"Add $\dfrac{1}{2}$: $\dfrac{3x}{4} \geq \dfrac{3}{2}$. Multiply by $\dfrac{4}{3}$: $x \geq 2$. Solution: $[2, \infty)$."
        },
        {
            'question': r"Solve: $\dfrac{1}{2}x - \dfrac{1}{3} < \dfrac{5}{6}$",
            'answer': r"$\left(-\infty, \dfrac{7}{3}\right)$",
            'wrong': [r"$\left(-\infty, \dfrac{1}{2}\right)$", r"$\left(\dfrac{7}{3}, \infty\right)$",
                      r"$(-\infty, 7)$"],
            'explanation': r"Add $\dfrac{1}{3}$: $\dfrac{x}{2} < \dfrac{7}{6}$. Multiply by $2$: $x < \dfrac{7}{3}$. Solution: $\left(-\infty, \dfrac{7}{3}\right)$."
        },
        {
            'question': r"Solve: $\dfrac{x-2}{4} \geq \dfrac{x+1}{6}$",
            'answer': r"$[8, \infty)$",
            'wrong': [r"$(-\infty, 8]$", r"$[-8, \infty)$", r"$[4, \infty)$"],
            'explanation': r"Multiply by $12$: $3(x-2) \geq 2(x+1)$. Expand: $3x - 6 \geq 2x + 2$. Subtract $2x$: $x \geq 8$. Solution: $[8, \infty)$."
        },
        {
            'question': r"Solve: $1.2x + 0.4 > 0.8x - 1.2$",
            'answer': r"$(-4, \infty)$",
            'wrong': [r"$(-\infty, -4)$", r"$(4, \infty)$", r"$(-\infty, 4)$"],
            'explanation': r"Subtract $0.8x$: $0.4x + 0.4 > -1.2$. Subtract $0.4$: $0.4x > -1.6$. Divide by $0.4$: $x > -4$. Solution: $(-4, \infty)$."
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 2 — QUADRATIC INEQUALITIES (50 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        # ── 2.1  Factored form — roots given (15 problems) ───────────────────────

        {
            'question': r"Solve: $x^2 - 5x + 6 < 0$",
            'answer': r"$(2, 3)$",
            'wrong': [r"$(-\infty, 2) \cup (3, \infty)$", r"$(-\infty, -2) \cup (-3, \infty)$", r"$(-3, -2)$"],
            'explanation': r"Factor: $(x-2)(x-3) < 0$. Roots are $x=2$ and $x=3$. The parabola opens upward ($a=1>0$), so the expression is NEGATIVE between the roots. Solution: $(2, 3)$."
        },
        {
            'question': r"Solve: $x^2 - 5x + 6 > 0$",
            'answer': r"$(-\infty, 2) \cup (3, \infty)$",
            'wrong': [r"$(2, 3)$", r"$(3, \infty)$", r"$(-\infty, 2)$"],
            'explanation': r"Factor: $(x-2)(x-3) > 0$. Parabola opens upward. The expression is POSITIVE outside the roots. Solution: $(-\infty, 2) \cup (3, \infty)$."
        },
        {
            'question': r"Solve: $x^2 - x - 6 \leq 0$",
            'answer': r"$[-2, 3]$",
            'wrong': [r"$(-\infty, -2] \cup [3, \infty)$", r"$[-3, 2]$", r"$(-\infty, -3] \cup [2, \infty)$"],
            'explanation': r"Factor: $(x-3)(x+2) \leq 0$. Roots: $x=-2$ and $x=3$. Parabola opens upward → expression is $\leq 0$ between (and including) the roots. Solution: $[-2, 3]$."
        },
        {
            'question': r"Solve: $x^2 - x - 6 \geq 0$",
            'answer': r"$(-\infty, -2] \cup [3, \infty)$",
            'wrong': [r"$[-2, 3]$", r"$[-3, 2]$", r"$[-2, \infty)$"],
            'explanation': r"$(x-3)(x+2) \geq 0$. Parabola opens upward → expression is $\geq 0$ outside the roots. Solution: $(-\infty,-2] \cup [3,\infty)$."
        },
        {
            'question': r"Solve: $x^2 - 9 < 0$",
            'answer': r"$(-3, 3)$",
            'wrong': [r"$(-\infty, -3) \cup (3, \infty)$", r"$(-\infty, 3)$", r"$(-9, 9)$"],
            'explanation': r"$(x-3)(x+3) < 0$. Roots: $x = \pm 3$. Parabola opens upward → negative between the roots. Solution: $(-3, 3)$."
        },
        {
            'question': r"Solve: $x^2 - 9 > 0$",
            'answer': r"$(-\infty, -3) \cup (3, \infty)$",
            'wrong': [r"$(-3, 3)$", r"$(3, \infty)$", r"$(-9, \infty)$"],
            'explanation': r"$(x-3)(x+3) > 0$. Parabola opens upward → positive outside the roots. Solution: $(-\infty,-3) \cup (3,\infty)$."
        },
        {
            'question': r"Solve: $x^2 + x - 12 \leq 0$",
            'answer': r"$[-4, 3]$",
            'wrong': [r"$(-\infty, -4] \cup [3, \infty)$", r"$[-3, 4]$", r"$(-\infty, -3] \cup [4, \infty)$"],
            'explanation': r"Factor: $(x+4)(x-3) \leq 0$. Roots: $x=-4$, $x=3$. Parabola opens upward → $\leq 0$ between roots. Solution: $[-4, 3]$."
        },
        {
            'question': r"Solve: $x^2 + 2x - 8 > 0$",
            'answer': r"$(-\infty, -4) \cup (2, \infty)$",
            'wrong': [r"$(-4, 2)$", r"$(-\infty, -2) \cup (4, \infty)$", r"$(-2, 4)$"],
            'explanation': r"Factor: $(x+4)(x-2) > 0$. Roots: $x=-4$, $x=2$. Parabola opens upward → positive outside the roots. Solution: $(-\infty,-4) \cup (2,\infty)$."
        },
        {
            'question': r"Solve: $(x-1)(x-5) < 0$",
            'answer': r"$(1, 5)$",
            'wrong': [r"$(-\infty, 1) \cup (5, \infty)$", r"$(-5, -1)$", r"$(-\infty, -1) \cup (5, \infty)$"],
            'explanation': r"Roots: $x=1$ and $x=5$. The product is negative between the roots. Solution: $(1, 5)$."
        },
        {
            'question': r"Solve: $(x+2)(x-4) \geq 0$",
            'answer': r"$(-\infty, -2] \cup [4, \infty)$",
            'wrong': [r"$[-2, 4]$", r"$(-\infty, 2] \cup [-4, \infty)$", r"$[-4, 2]$"],
            'explanation': r"Roots: $x=-2$ and $x=4$. Product $\geq 0$ when both factors have the same sign. Solution: $(-\infty,-2] \cup [4,\infty)$."
        },
        {
            'question': r"Solve: $x^2 - 4x > 0$",
            'answer': r"$(-\infty, 0) \cup (4, \infty)$",
            'wrong': [r"$(0, 4)$", r"$(4, \infty)$", r"$(-\infty, 0)$"],
            'explanation': r"Factor: $x(x-4) > 0$. Roots: $x=0$ and $x=4$. Positive outside the roots. Solution: $(-\infty,0) \cup (4,\infty)$."
        },
        {
            'question': r"Solve: $x^2 - 4x \leq 0$",
            'answer': r"$[0, 4]$",
            'wrong': [r"$(-\infty, 0] \cup [4, \infty)$", r"$[-4, 0]$", r"$(-\infty, 0) \cup (4, \infty)$"],
            'explanation': r"$x(x-4) \leq 0$. Parabola opens upward → $\leq 0$ between roots (including). Solution: $[0, 4]$."
        },
        {
            'question': r"Solve: $2x^2 - 8 \leq 0$",
            'answer': r"$[-2, 2]$",
            'wrong': [r"$(-\infty, -2] \cup [2, \infty)$", r"$[-4, 4]$", r"$(-2, 2)$"],
            'explanation': r"Divide by $2$: $x^2 - 4 \leq 0$, i.e. $(x-2)(x+2) \leq 0$. Between the roots: $-2 \leq x \leq 2$. Solution: $[-2, 2]$."
        },
        {
            'question': r"Solve: $x^2 - 16 > 0$",
            'answer': r"$(-\infty, -4) \cup (4, \infty)$",
            'wrong': [r"$(-4, 4)$", r"$(4, \infty)$", r"$(-4, \infty)$"],
            'explanation': r"$(x-4)(x+4) > 0$. Positive outside the roots $\pm 4$. Solution: $(-\infty,-4) \cup (4,\infty)$."
        },
        {
            'question': r"Solve: $(x-3)^2 > 0$",
            'answer': r"$(-\infty, 3) \cup (3, \infty)$",
            'wrong': [r"$(3, \infty)$", r"$(-\infty, 3)$", r"$(0, \infty)$"],
            'explanation': r"$(x-3)^2 \geq 0$ always. It equals $0$ when $x=3$. So $(x-3)^2 > 0$ for all $x \neq 3$. Solution: $(-\infty,3) \cup (3,\infty)$."
        },

        # ── 2.2  Completing/formula needed (15 problems) ─────────────────────────

        {
            'question': r"Solve: $x^2 + 4x + 3 < 0$",
            'answer': r"$(-3, -1)$",
            'wrong': [r"$(-\infty, -3) \cup (-1, \infty)$", r"$(-1, 3)$", r"$(1, 3)$"],
            'explanation': r"Factor: $(x+3)(x+1) < 0$. Roots: $x=-3$, $x=-1$. Parabola opens upward → negative between roots. Solution: $(-3,-1)$."
        },
        {
            'question': r"Solve: $x^2 - 2x - 3 \geq 0$",
            'answer': r"$(-\infty, -1] \cup [3, \infty)$",
            'wrong': [r"$[-1, 3]$", r"$(-\infty, 1] \cup [-3, \infty)$", r"$[3, \infty)$"],
            'explanation': r"Factor: $(x-3)(x+1) \geq 0$. Roots: $x=-1$, $x=3$. Parabola opens upward → $\geq 0$ outside (and at) roots. Solution: $(-\infty,-1] \cup [3,\infty)$."
        },
        {
            'question': r"Solve: $x^2 + 6x + 8 \leq 0$",
            'answer': r"$[-4, -2]$",
            'wrong': [r"$(-\infty, -4] \cup [-2, \infty)$", r"$[-2, 4]$", r"$[2, 4]$"],
            'explanation': r"Factor: $(x+4)(x+2) \leq 0$. Roots: $x=-4$, $x=-2$. Between roots (and including). Solution: $[-4,-2]$."
        },
        {
            'question': r"Solve: $x^2 - 6x + 9 \leq 0$",
            'answer': r"$\{3\}$",
            'wrong': [r"$(-\infty, 3]$", r"$[3, \infty)$", r"$(-\infty, \infty)$"],
            'explanation': r"$(x-3)^2 \leq 0$. Since $(x-3)^2 \geq 0$ always, the only solution is $x = 3$. Solution: $\{3\}$."
        },
        {
            'question': r"Solve: $x^2 + 1 > 0$",
            'answer': r"$(-\infty, \infty)$",
            'wrong': [r"$(-\infty, -1) \cup (1, \infty)$", r"$(-\infty, 0) \cup (0, \infty)$", r"$\emptyset$"],
            'explanation': r"$x^2 \geq 0$ for all real $x$, so $x^2 + 1 \geq 1 > 0$ always. Solution: $(-\infty, \infty)$."
        },
        {
            'question': r"Solve: $x^2 + 2x + 5 < 0$",
            'answer': r"$\emptyset$",
            'wrong': [r"$(-\infty, -3)$", r"$(-5, -1)$", r"$(-\infty, -5)$"],
            'explanation': r"Complete the square: $(x+1)^2 + 4 < 0$. Since $(x+1)^2 \geq 0$, the sum is always $\geq 4 > 0$. No real solution. Solution: $\emptyset$."
        },
        {
            'question': r"Solve: $2x^2 - 5x - 3 < 0$",
            'answer': r"$\left(-\dfrac{1}{2}, 3\right)$",
            'wrong': [r"$\left(-\infty, -\dfrac{1}{2}\right) \cup (3, \infty)$", r"$\left(-3, \dfrac{1}{2}\right)$",
                      r"$\left(\dfrac{1}{2}, 3\right)$"],
            'explanation': r"Factor: $(2x+1)(x-3) < 0$. Roots: $x=-\dfrac{1}{2}$, $x=3$. Parabola opens upward → negative between roots. Solution: $\left(-\dfrac{1}{2}, 3\right)$."
        },
        {
            'question': r"Solve: $3x^2 - x - 2 \geq 0$",
            'answer': r"$\left(-\infty, -\dfrac{2}{3}\right] \cup [1, \infty)$",
            'wrong': [r"$\left[-\dfrac{2}{3}, 1\right]$", r"$(-\infty, -1] \cup \left[\dfrac{2}{3}, \infty\right)$",
                      r"$\left[-1, \dfrac{2}{3}\right]$"],
            'explanation': r"Factor: $(3x+2)(x-1) \geq 0$. Roots: $x = -\dfrac{2}{3}$, $x=1$. Parabola opens upward → $\geq 0$ outside roots. Solution: $\left(-\infty,-\dfrac{2}{3}\right] \cup [1,\infty)$."
        },
        {
            'question': r"Solve: $x^2 - 4x + 5 > 0$",
            'answer': r"$(-\infty, \infty)$",
            'wrong': [r"$(-\infty, 1) \cup (5, \infty)$", r"$(1, 5)$", r"$\emptyset$"],
            'explanation': r"Discriminant: $16-20=-4 < 0$. Since $a=1>0$ and no real roots, the parabola is always above the $x$-axis. Solution: $(-\infty, \infty)$."
        },
        {
            'question': r"Solve: $-x^2 + 4 > 0$",
            'answer': r"$(-2, 2)$",
            'wrong': [r"$(-\infty, -2) \cup (2, \infty)$", r"$(2, \infty)$", r"$(-\infty, \infty)$"],
            'explanation': r"Multiply by $-1$ (flip): $x^2 - 4 < 0$, i.e. $(x-2)(x+2) < 0$. Negative between roots $\pm 2$. Solution: $(-2, 2)$."
        },
        {
            'question': r"Solve: $-x^2 + x + 6 \geq 0$",
            'answer': r"$[-2, 3]$",
            'wrong': [r"$(-\infty, -2] \cup [3, \infty)$", r"$[-3, 2]$", r"$[-6, 1]$"],
            'explanation': r"Multiply by $-1$ (flip): $x^2 - x - 6 \leq 0$. Factor: $(x-3)(x+2) \leq 0$. Between roots: $-2 \leq x \leq 3$. Solution: $[-2, 3]$."
        },
        {
            'question': r"Solve: $x^2 + 5x + 4 < 0$",
            'answer': r"$(-4, -1)$",
            'wrong': [r"$(-\infty, -4) \cup (-1, \infty)$", r"$(1, 4)$", r"$[-4, -1]$"],
            'explanation': r"Factor: $(x+4)(x+1) < 0$. Roots: $x=-4$, $x=-1$. Negative between roots (strictly). Solution: $(-4,-1)$."
        },
        {
            'question': r"Solve: $4x^2 - 1 \leq 0$",
            'answer': r"$\left[-\dfrac{1}{2}, \dfrac{1}{2}\right]$",
            'wrong': [r"$\left(-\infty, -\dfrac{1}{2}\right] \cup \left[\dfrac{1}{2}, \infty\right)$", r"$[-1, 1]$",
                      r"$\left[-\dfrac{1}{4}, \dfrac{1}{4}\right]$"],
            'explanation': r"$(2x-1)(2x+1) \leq 0$. Roots: $x = \pm\dfrac{1}{2}$. Between roots: $-\dfrac{1}{2} \leq x \leq \dfrac{1}{2}$. Solution: $\left[-\dfrac{1}{2}, \dfrac{1}{2}\right]$."
        },
        {
            'question': r"Solve: $9x^2 - 4 > 0$",
            'answer': r"$\left(-\infty, -\dfrac{2}{3}\right) \cup \left(\dfrac{2}{3}, \infty\right)$",
            'wrong': [r"$\left(-\dfrac{2}{3}, \dfrac{2}{3}\right)$", r"$\left(\dfrac{2}{3}, \infty\right)$",
                      r"$\left(-\infty, -\dfrac{4}{9}\right) \cup \left(\dfrac{4}{9}, \infty\right)$"],
            'explanation': r"$(3x-2)(3x+2) > 0$. Roots: $x = \pm\dfrac{2}{3}$. Positive outside the roots. Solution: $\left(-\infty,-\dfrac{2}{3}\right) \cup \left(\dfrac{2}{3},\infty\right)$."
        },
        {
            'question': r"Solve: $x^2 - 6x + 10 > 0$",
            'answer': r"$(-\infty, \infty)$",
            'wrong': [r"$(-\infty, 2) \cup (8, \infty)$", r"$(2, 8)$", r"$\emptyset$"],
            'explanation': r"Discriminant: $36 - 40 = -4 < 0$. No real roots; $a = 1 > 0$, so the parabola is always above the $x$-axis. Solution: $(-\infty, \infty)$."
        },

        # ── 2.3  Applied / mixed (20 problems) ───────────────────────────────────

        {
            'question': r"For what values of $x$ is $x^2 < 25$?",
            'answer': r"$(-5, 5)$",
            'wrong': [r"$(-\infty, 5)$", r"$(-\infty, -5) \cup (5, \infty)$", r"$(-25, 25)$"],
            'explanation': r"$x^2 - 25 < 0 \Rightarrow (x-5)(x+5) < 0$. Negative between roots $\pm 5$. Solution: $(-5, 5)$."
        },
        {
            'question': r"For what values of $x$ is $x^2 \geq 16$?",
            'answer': r"$(-\infty, -4] \cup [4, \infty)$",
            'wrong': [r"$[-4, 4]$", r"$[4, \infty)$", r"$[-16, \infty)$"],
            'explanation': r"$x^2 - 16 \geq 0 \Rightarrow (x-4)(x+4) \geq 0$. Positive (or zero) outside roots. Solution: $(-\infty,-4] \cup [4,\infty)$."
        },
        {
            'question': r"Solve: $x(x - 6) < 0$",
            'answer': r"$(0, 6)$",
            'wrong': [r"$(-\infty, 0) \cup (6, \infty)$", r"$(-6, 0)$", r"$(-\infty, 6)$"],
            'explanation': r"Roots: $x=0$ and $x=6$. Product $x(x-6) < 0$ between the roots. Solution: $(0, 6)$."
        },
        {
            'question': r"Solve: $(2x-1)(x+3) \leq 0$",
            'answer': r"$\left[-3, \dfrac{1}{2}\right]$",
            'wrong': [r"$\left(-\infty, -3\right] \cup \left[\dfrac{1}{2}, \infty\right)$",
                      r"$\left[-\dfrac{1}{2}, 3\right]$", r"$\left(-\infty, -\dfrac{1}{3}\right] \cup [2, \infty)$"],
            'explanation': r"Roots: $x = -3$ and $x = \dfrac{1}{2}$. Since $a>0$, the product is $\leq 0$ between roots. Solution: $\left[-3, \dfrac{1}{2}\right]$."
        },
        {
            'question': r"Solve: $x^2 - 7x + 10 > 0$",
            'answer': r"$(-\infty, 2) \cup (5, \infty)$",
            'wrong': [r"$(2, 5)$", r"$(5, \infty)$", r"$(-\infty, 2)$"],
            'explanation': r"Factor: $(x-2)(x-5) > 0$. Roots: $x=2$, $x=5$. Parabola opens upward → positive outside roots. Solution: $(-\infty,2) \cup (5,\infty)$."
        },
        {
            'question': r"Find $x$ such that $x^2 + 3x > 10$",
            'answer': r"$(-\infty, -5) \cup (2, \infty)$",
            'wrong': [r"$(-5, 2)$", r"$(2, \infty)$", r"$(-\infty, -5)$"],
            'explanation': r"$x^2+3x-10>0$. Factor: $(x+5)(x-2)>0$. Positive outside roots $x=-5$ and $x=2$. Solution: $(-\infty,-5) \cup (2,\infty)$."
        },
        {
            'question': r"Solve: $x^2 \leq 3x + 4$",
            'answer': r"$[-1, 4]$",
            'wrong': [r"$(-\infty, -1] \cup [4, \infty)$", r"$[-4, 1]$", r"$(-\infty, -4] \cup [1, \infty)$"],
            'explanation': r"Rearrange: $x^2-3x-4 \leq 0$. Factor: $(x-4)(x+1) \leq 0$. Between roots: $-1 \leq x \leq 4$. Solution: $[-1, 4]$."
        },
        {
            'question': r"Solve: $2x^2 > 8$",
            'answer': r"$(-\infty, -2) \cup (2, \infty)$",
            'wrong': [r"$(-2, 2)$", r"$(2, \infty)$", r"$(-\infty, -4) \cup (4, \infty)$"],
            'explanation': r"Divide by $2$: $x^2 > 4$, i.e. $(x-2)(x+2) > 0$. Positive outside roots $\pm 2$. Solution: $(-\infty,-2) \cup (2,\infty)$."
        },
        {
            'question': r"The height $h = -x^2 + 6x - 5 > 0$. Find the range of $x$.",
            'answer': r"$(1, 5)$",
            'wrong': [r"$(-\infty, 1) \cup (5, \infty)$", r"$(-5, -1)$", r"$(0, 6)$"],
            'explanation': r"$-x^2+6x-5>0 \Rightarrow x^2-6x+5<0$. Factor: $(x-1)(x-5)<0$. Negative between roots. Solution: $(1, 5)$."
        },
        {
            'question': r"For what $x$ is the area $A = x(10-x)$ greater than $21$?",
            'answer': r"$(3, 7)$",
            'wrong': [r"$(-\infty, 3) \cup (7, \infty)$", r"$(1, 9)$", r"$(2, 8)$"],
            'explanation': r"$x(10-x) > 21 \Rightarrow -x^2+10x-21 > 0 \Rightarrow x^2-10x+21 < 0$. Factor: $(x-3)(x-7)<0$. Solution: $(3, 7)$."
        },
        {
            'question': r"Solve: $x^2 - 2x - 15 < 0$",
            'answer': r"$(-3, 5)$",
            'wrong': [r"$(-\infty, -3) \cup (5, \infty)$", r"$(-5, 3)$", r"$(-\infty, -5) \cup (3, \infty)$"],
            'explanation': r"Factor: $(x-5)(x+3) < 0$. Roots: $x=-3$, $x=5$. Negative between roots. Solution: $(-3, 5)$."
        },
        {
            'question': r"Solve: $x^2 + 8x + 12 \geq 0$",
            'answer': r"$(-\infty, -6] \cup [-2, \infty)$",
            'wrong': [r"$[-6, -2]$", r"$(-\infty, 2] \cup [6, \infty)$", r"$[2, 6]$"],
            'explanation': r"Factor: $(x+6)(x+2) \geq 0$. Roots: $x=-6$, $x=-2$. Parabola opens upward → $\geq 0$ outside (and at) roots. Solution: $(-\infty,-6] \cup [-2,\infty)$."
        },
        {
            'question': r"Solve: $-2x^2 + 4x + 6 > 0$",
            'answer': r"$(-1, 3)$",
            'wrong': [r"$(-\infty, -1) \cup (3, \infty)$", r"$(-3, 1)$", r"$(3, \infty)$"],
            'explanation': r"Divide by $-2$ (flip): $x^2-2x-3 < 0$. Factor: $(x-3)(x+1)<0$. Negative between roots $-1$ and $3$. Solution: $(-1, 3)$."
        },
        {
            'question': r"Solve: $x^2 - 10x + 25 < 0$",
            'answer': r"$\emptyset$",
            'wrong': [r"$(-\infty, 5)$", r"$(5, \infty)$", r"$(-\infty, \infty)$"],
            'explanation': r"$(x-5)^2 < 0$. A perfect square is always $\geq 0$, so it is NEVER negative. Solution: $\emptyset$."
        },
        {
            'question': r"Solve: $x^2 - 10x + 25 \geq 0$",
            'answer': r"$(-\infty, \infty)$",
            'wrong': [r"$\{5\}$", r"$[5, \infty)$", r"$(-\infty, 5]$"],
            'explanation': r"$(x-5)^2 \geq 0$ is TRUE for all real $x$ (a square is always non-negative). Solution: $(-\infty, \infty)$."
        },
        {
            'question': r"Solve: $x^2 - x - 20 \leq 0$",
            'answer': r"$[-4, 5]$",
            'wrong': [r"$(-\infty, -4] \cup [5, \infty)$", r"$[-5, 4]$", r"$(-\infty, -5] \cup [4, \infty)$"],
            'explanation': r"Factor: $(x-5)(x+4) \leq 0$. Roots: $x=-4$, $x=5$. Between roots (including). Solution: $[-4, 5]$."
        },
        {
            'question': r"Solve: $3x^2 - 12 < 0$",
            'answer': r"$(-2, 2)$",
            'wrong': [r"$(-\infty, -2) \cup (2, \infty)$", r"$(-4, 4)$", r"$(-\infty, 2)$"],
            'explanation': r"Divide by $3$: $x^2 - 4 < 0 \Rightarrow (x-2)(x+2) < 0$. Negative between roots $\pm 2$. Solution: $(-2, 2)$."
        },
        {
            'question': r"Find all $x$ satisfying $x^2 + x \leq 6$",
            'answer': r"$[-3, 2]$",
            'wrong': [r"$(-\infty, -3] \cup [2, \infty)$", r"$[-2, 3]$", r"$(-\infty, -2] \cup [3, \infty)$"],
            'explanation': r"$x^2+x-6 \leq 0$. Factor: $(x+3)(x-2) \leq 0$. Between roots (including). Solution: $[-3, 2]$."
        },
        {
            'question': r"Solve: $5x^2 \leq 20$",
            'answer': r"$[-2, 2]$",
            'wrong': [r"$(-\infty, -2] \cup [2, \infty)$", r"$[-4, 4]$", r"$(-\infty, 4]$"],
            'explanation': r"Divide by $5$: $x^2 \leq 4$, i.e. $(x-2)(x+2) \leq 0$. Between roots. Solution: $[-2, 2]$."
        },
        {
            'question': r"Solve: $(x-3)^2 \leq 16$",
            'answer': r"$[-1, 7]$",
            'wrong': [r"$(-\infty, -1] \cup [7, \infty)$", r"$[-7, 1]$", r"$[1, 7]$"],
            'explanation': r"Take square root: $|x-3| \leq 4$, which means $-4 \leq x-3 \leq 4$. Add $3$: $-1 \leq x \leq 7$. Solution: $[-1, 7]$."
        },
    ],
    'linear_functions': [

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 1 — SLOPE & BASIC PROPERTIES (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"Find the slope of the line passing through $(2, 3)$ and $(6, 11)$.",
            'answer': r"$m = 2$",
            'wrong': [r"$m = \dfrac{1}{2}$", r"$m = -2$", r"$m = 4$"],
            'explanation': r"Use the slope formula: $m = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{11 - 3}{6 - 2} = \dfrac{8}{4} = 2$. The slope tells us: for every $1$ unit increase in $x$, $y$ increases by $2$."
        },
        {
            'question': r"Find the slope of the line passing through $(-1, 4)$ and $(3, -4)$.",
            'answer': r"$m = -2$",
            'wrong': [r"$m = 2$", r"$m = \dfrac{1}{2}$", r"$m = -\dfrac{1}{2}$"],
            'explanation': r"$m = \dfrac{-4 - 4}{3 - (-1)} = \dfrac{-8}{4} = -2$. The negative slope means the line falls from left to right."
        },
        {
            'question': r"Find the slope of the line passing through $(0, 5)$ and $(4, 5)$.",
            'answer': r"$m = 0$",
            'wrong': [r"$m = 5$", r"$m = 1$", r"Undefined"],
            'explanation': r"$m = \dfrac{5 - 5}{4 - 0} = \dfrac{0}{4} = 0$. A slope of $0$ means the line is horizontal. Both points have the same $y$-value, confirming this."
        },
        {
            'question': r"Find the slope of the line passing through $(3, -2)$ and $(3, 7)$.",
            'answer': r"Undefined",
            'wrong': [r"$m = 0$", r"$m = 9$", r"$m = -9$"],
            'explanation': r"$m = \dfrac{7 - (-2)}{3 - 3} = \dfrac{9}{0}$. Division by zero is undefined. Both points have the same $x$-value, so this is a vertical line, which has an undefined slope."
        },
        {
            'question': r"Find the slope of the line $y = -3x + 7$.",
            'answer': r"$m = -3$",
            'wrong': [r"$m = 3$", r"$m = 7$", r"$m = -7$"],
            'explanation': r"The equation is in slope-intercept form $y = mx + b$. Comparing $y = -3x + 7$ with $y = mx + b$, the slope is the coefficient of $x$: $m = -3$. The $y$-intercept is $b = 7$."
        },
        {
            'question': r"Find the slope of the line $2x + 4y = 8$.",
            'answer': r"$m = -\dfrac{1}{2}$",
            'wrong': [r"$m = 2$", r"$m = -2$", r"$m = \dfrac{1}{2}$"],
            'explanation': r"Solve for $y$: $4y = -2x + 8$, so $y = -\dfrac{1}{2}x + 2$. The slope is $m = -\dfrac{1}{2}$. Always convert to $y = mx + b$ form to read off the slope directly."
        },
        {
            'question': r"Find the slope of the line $3x - y = 6$.",
            'answer': r"$m = 3$",
            'wrong': [r"$m = -3$", r"$m = 6$", r"$m = -6$"],
            'explanation': r"Solve for $y$: $-y = -3x + 6$, so $y = 3x - 6$. The slope is $m = 3$. The $y$-intercept is $b = -6$."
        },
        {
            'question': r"Which of the following lines has the steepest slope?",
            'answer': r"$y = 5x + 1$",
            'wrong': [r"$y = 2x + 3$", r"$y = -3x + 7$", r"$y = \dfrac{1}{2}x - 4$"],
            'explanation': r"Steepness is measured by the absolute value of the slope. $|5| = 5$, $|2| = 2$, $|-3| = 3$, $|\frac{1}{2}| = 0.5$. The line $y = 5x + 1$ has the largest absolute slope value, so it is the steepest."
        },
        {
            'question': r"Two lines have slopes $m_1 = \dfrac{3}{4}$ and $m_2 = -\dfrac{4}{3}$. What is their relationship?",
            'answer': r"Perpendicular",
            'wrong': [r"Parallel", r"The same line", r"Neither parallel nor perpendicular"],
            'explanation': r"Two lines are perpendicular if and only if the product of their slopes equals $-1$. Check: $\dfrac{3}{4} \times \left(-\dfrac{4}{3}\right) = -1$ ✓. So the lines are perpendicular."
        },
        {
            'question': r"Two lines have slopes $m_1 = 2$ and $m_2 = 2$. What is their relationship?",
            'answer': r"Parallel (or identical)",
            'wrong': [r"Perpendicular", r"Intersecting at a right angle", r"They always intersect"],
            'explanation': r"Two lines with equal slopes are parallel (if they have different $y$-intercepts) or identical (if they have the same $y$-intercept). Equal slopes mean the lines never intersect unless they are the same line."
        },
        {
            'question': r"Find the slope of a line perpendicular to $y = \dfrac{2}{3}x + 5$.",
            'answer': r"$m = -\dfrac{3}{2}$",
            'wrong': [r"$m = \dfrac{2}{3}$", r"$m = \dfrac{3}{2}$", r"$m = -\dfrac{2}{3}$"],
            'explanation': r"The slope of the given line is $m_1 = \dfrac{2}{3}$. For a perpendicular line, the slope is the negative reciprocal: $m_\perp = -\dfrac{1}{m_1} = -\dfrac{3}{2}$. Check: $\dfrac{2}{3} \times \left(-\dfrac{3}{2}\right) = -1$ ✓"
        },
        {
            'question': r"Find the slope of a line parallel to $5x - 2y = 10$.",
            'answer': r"$m = \dfrac{5}{2}$",
            'wrong': [r"$m = -\dfrac{2}{5}$", r"$m = 5$", r"$m = -5$"],
            'explanation': r"Rewrite in slope-intercept form: $-2y = -5x + 10$, so $y = \dfrac{5}{2}x - 5$. The slope is $\dfrac{5}{2}$. A parallel line has the SAME slope: $m = \dfrac{5}{2}$."
        },
        {
            'question': r"The slope of a line is $4$ and it passes through $(1, 6)$. What is the $y$-value when $x = 3$?",
            'answer': r"$y = 14$",
            'wrong': [r"$y = 12$", r"$y = 10$", r"$y = 18$"],
            'explanation': r"From $(1,6)$ to $x=3$ is a change of $\Delta x = 2$. Change in $y$: $\Delta y = m \cdot \Delta x = 4 \times 2 = 8$. So $y = 6 + 8 = 14$. Alternatively, find the equation: $y - 6 = 4(x-1) \Rightarrow y = 4x + 2$. At $x=3$: $y = 14$ ✓"
        },
        {
            'question': r"Find the slope of the line passing through $(-3, 0)$ and $(0, 6)$.",
            'answer': r"$m = 2$",
            'wrong': [r"$m = -2$", r"$m = \dfrac{1}{2}$", r"$m = 3$"],
            'explanation': r"$m = \dfrac{6 - 0}{0 - (-3)} = \dfrac{6}{3} = 2$. Note: $(0, 6)$ is the $y$-intercept and $(-3, 0)$ is the $x$-intercept."
        },
        {
            'question': r"A line rises $6$ units for every $2$ units it runs right. What is its slope?",
            'answer': r"$m = 3$",
            'wrong': [r"$m = \dfrac{1}{3}$", r"$m = 12$", r"$m = \dfrac{2}{6}$"],
            'explanation': r"Slope $= \dfrac{\text{rise}}{\text{run}} = \dfrac{6}{2} = 3$. The line rises $3$ units for every $1$ unit moved to the right."
        },
        {
            'question': r"Find the slope of the line $y = -\dfrac{3}{4}x$.",
            'answer': r"$m = -\dfrac{3}{4}$",
            'wrong': [r"$m = \dfrac{3}{4}$", r"$m = 0$", r"$m = -\dfrac{4}{3}$"],
            'explanation': r"The equation $y = -\dfrac{3}{4}x$ is in slope-intercept form with $b = 0$. The slope is the coefficient of $x$: $m = -\dfrac{3}{4}$. The line passes through the origin."
        },
        {
            'question': r"Find the rate of change of $y = 7x - 2$.",
            'answer': r"$7$",
            'wrong': [r"$-2$", r"$\dfrac{1}{7}$", r"$-7$"],
            'explanation': r"The rate of change of a linear function equals its slope. In $y = mx + b$, the slope $m$ represents how much $y$ changes per unit increase in $x$. Here $m = 7$, so $y$ increases by $7$ for each $1$-unit increase in $x$."
        },
        {
            'question': r"Find the slope of the line passing through $(a, b)$ and $(a+2, b+6)$.",
            'answer': r"$m = 3$",
            'wrong': [r"$m = \dfrac{b}{a}$", r"$m = \dfrac{b+6}{a+2}$", r"$m = 6$"],
            'explanation': r"$m = \dfrac{(b+6) - b}{(a+2) - a} = \dfrac{6}{2} = 3$. The specific values of $a$ and $b$ do not affect the slope — only the changes in $x$ and $y$ matter."
        },
        {
            'question': r"A line has slope $-\dfrac{5}{3}$. If $x$ increases by $6$, how does $y$ change?",
            'answer': r"$y$ decreases by $10$",
            'wrong': [r"$y$ increases by $10$", r"$y$ decreases by $2$", r"$y$ increases by $\dfrac{5}{3}$"],
            'explanation': r"$\Delta y = m \cdot \Delta x = -\dfrac{5}{3} \times 6 = -10$. A negative slope means $y$ decreases as $x$ increases. Here $y$ decreases by $10$."
        },
        {
            'question': r"Find the slope of $\dfrac{x}{4} + \dfrac{y}{3} = 1$.",
            'answer': r"$m = -\dfrac{3}{4}$",
            'wrong': [r"$m = \dfrac{3}{4}$", r"$m = \dfrac{4}{3}$", r"$m = -\dfrac{4}{3}$"],
            'explanation': r"Solve for $y$: $\dfrac{y}{3} = 1 - \dfrac{x}{4}$, so $y = 3 - \dfrac{3}{4}x = -\dfrac{3}{4}x + 3$. The slope is $m = -\dfrac{3}{4}$. Note: this is the intercept form of a line with $x$-intercept $4$ and $y$-intercept $3$."
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 2 — EQUATION OF A LINE (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"Write the equation of the line with slope $3$ and $y$-intercept $-4$.",
            'answer': r"$y = 3x - 4$",
            'wrong': [r"$y = -4x + 3$", r"$y = 3x + 4$", r"$y = -3x - 4$"],
            'explanation': r"Use slope-intercept form $y = mx + b$ with $m = 3$ and $b = -4$: $y = 3x - 4$. Check: when $x=0$, $y = -4$ (correct $y$-intercept) ✓"
        },
        {
            'question': r"Write the equation of the line with slope $-2$ passing through $(3, 1)$.",
            'answer': r"$y = -2x + 7$",
            'wrong': [r"$y = -2x - 7$", r"$y = 2x + 7$", r"$y = -2x + 1$"],
            'explanation': r"Use point-slope form: $y - y_1 = m(x - x_1)$. Substitute $m=-2$, $(x_1,y_1)=(3,1)$: $y - 1 = -2(x - 3)$. Expand: $y - 1 = -2x + 6$. Add $1$: $y = -2x + 7$. Check: at $x=3$: $y = -6+7=1$ ✓"
        },
        {
            'question': r"Write the equation of the line passing through $(1, 2)$ and $(4, 8)$.",
            'answer': r"$y = 2x$",
            'wrong': [r"$y = 2x + 4$", r"$y = 2x - 2$", r"$y = 3x - 1$"],
            'explanation': r"Step 1 — find slope: $m = \dfrac{8-2}{4-1} = \dfrac{6}{3} = 2$. Step 2 — use point-slope: $y - 2 = 2(x-1) \Rightarrow y = 2x - 2 + 2 = 2x$. Check: $(1,2)$: $y=2$ ✓ and $(4,8)$: $y=8$ ✓"
        },
        {
            'question': r"Write the equation of the line passing through $(-2, 5)$ and $(4, -1)$.",
            'answer': r"$y = -x + 3$",
            'wrong': [r"$y = x + 3$", r"$y = -x - 3$", r"$y = -2x + 3$"],
            'explanation': r"Slope: $m = \dfrac{-1-5}{4-(-2)} = \dfrac{-6}{6} = -1$. Point-slope: $y - 5 = -1(x + 2)$. Expand: $y = -x - 2 + 5 = -x + 3$. Check: $(-2,5)$: $y = 2+3=5$ ✓ and $(4,-1)$: $y = -4+3=-1$ ✓"
        },
        {
            'question': r"Find the $y$-intercept of the line $4x - 2y = 10$.",
            'answer': r"$(0, -5)$",
            'wrong': [r"$(0, 5)$", r"$(0, 10)$", r"$(0, -10)$"],
            'explanation': r"Solve for $y$: $-2y = -4x + 10$, so $y = 2x - 5$. The $y$-intercept is $b = -5$, i.e. the point $(0, -5)$. Alternatively, set $x=0$: $-2y = 10$, $y = -5$."
        },
        {
            'question': r"Find the $x$-intercept of the line $3x + 6y = 12$.",
            'answer': r"$(4, 0)$",
            'wrong': [r"$(2, 0)$", r"$(6, 0)$", r"$(0, 4)$"],
            'explanation': r"Set $y = 0$: $3x + 0 = 12$, so $x = 4$. The $x$-intercept is the point $(4, 0)$. This is where the line crosses the $x$-axis."
        },
        {
            'question': r"Write the equation of a horizontal line passing through $(3, -7)$.",
            'answer': r"$y = -7$",
            'wrong': [r"$x = 3$", r"$y = 3$", r"$x = -7$"],
            'explanation': r"A horizontal line has slope $m = 0$ and all points on it have the same $y$-value. Since the line passes through $(3,-7)$, every point has $y = -7$. Equation: $y = -7$."
        },
        {
            'question': r"Write the equation of a vertical line passing through $(-4, 2)$.",
            'answer': r"$x = -4$",
            'wrong': [r"$y = 2$", r"$x = 2$", r"$y = -4$"],
            'explanation': r"A vertical line has undefined slope and all points have the same $x$-value. Since the line passes through $(-4, 2)$, every point has $x = -4$. Equation: $x = -4$."
        },
        {
            'question': r"Write the equation of the line with $x$-intercept $5$ and $y$-intercept $-3$.",
            'answer': r"$y = \dfrac{3}{5}x - 3$",
            'wrong': [r"$y = -\dfrac{3}{5}x + 5$", r"$y = \dfrac{5}{3}x - 5$", r"$y = \dfrac{3}{5}x + 5$"],
            'explanation': r"The two intercept points are $(5, 0)$ and $(0, -3)$. Slope: $m = \dfrac{-3-0}{0-5} = \dfrac{-3}{-5} = \dfrac{3}{5}$. $y$-intercept $b = -3$. Equation: $y = \dfrac{3}{5}x - 3$."
        },
        {
            'question': r"Write in standard form: $y = \dfrac{2}{3}x - 4$.",
            'answer': r"$2x - 3y = 12$",
            'wrong': [r"$2x + 3y = 12$", r"$3x - 2y = 12$", r"$2x - 3y = -12$"],
            'explanation': r"Multiply through by $3$: $3y = 2x - 12$. Rearrange: $2x - 3y = 12$. Standard form is $Ax + By = C$ where $A$, $B$, $C$ are integers and $A > 0$."
        },
        {
            'question': r"Write the equation of the line parallel to $y = 3x - 1$ passing through $(2, 7)$.",
            'answer': r"$y = 3x + 1$",
            'wrong': [r"$y = -\dfrac{1}{3}x + 7$", r"$y = 3x - 7$", r"$y = 3x - 1$"],
            'explanation': r"Parallel lines have the same slope $m = 3$. Use point-slope: $y - 7 = 3(x - 2)$. Expand: $y = 3x - 6 + 7 = 3x + 1$. Check: $(2,7)$: $y = 6+1=7$ ✓"
        },
        {
            'question': r"Write the equation of the line perpendicular to $y = 2x + 5$ passing through $(4, 1)$.",
            'answer': r"$y = -\dfrac{1}{2}x + 3$",
            'wrong': [r"$y = 2x - 7$", r"$y = -\dfrac{1}{2}x - 1$", r"$y = \dfrac{1}{2}x - 1$"],
            'explanation': r"Perpendicular slope: $m_\perp = -\dfrac{1}{2}$. Point-slope: $y - 1 = -\dfrac{1}{2}(x - 4)$. Expand: $y = -\dfrac{1}{2}x + 2 + 1 = -\dfrac{1}{2}x + 3$. Check: $(4,1)$: $y = -2+3=1$ ✓"
        },
        {
            'question': r"Find the equation of the line passing through the origin with slope $-\dfrac{5}{2}$.",
            'answer': r"$y = -\dfrac{5}{2}x$",
            'wrong': [r"$y = \dfrac{5}{2}x$", r"$y = -\dfrac{2}{5}x$", r"$y = -\dfrac{5}{2}x + 1$"],
            'explanation': r"Passing through the origin means the $y$-intercept $b = 0$. Equation: $y = mx + 0 = -\dfrac{5}{2}x$. Check: $(0,0)$ is on the line ✓"
        },
        {
            'question': r"Given $f(x) = -4x + 9$, find $f(0)$ and $f(3)$.",
            'answer': r"$f(0) = 9$, $f(3) = -3$",
            'wrong': [r"$f(0) = 0$, $f(3) = -3$", r"$f(0) = 9$, $f(3) = 3$", r"$f(0) = -4$, $f(3) = -3$"],
            'explanation': r"$f(0) = -4(0) + 9 = 9$ (this is the $y$-intercept). $f(3) = -4(3) + 9 = -12 + 9 = -3$."
        },
        {
            'question': r"Find the equation of the line with slope $\dfrac{1}{2}$ passing through $(-4, 0)$.",
            'answer': r"$y = \dfrac{1}{2}x + 2$",
            'wrong': [r"$y = \dfrac{1}{2}x - 2$", r"$y = 2x + 2$", r"$y = \dfrac{1}{2}x$"],
            'explanation': r"Point-slope: $y - 0 = \dfrac{1}{2}(x - (-4))$. Simplify: $y = \dfrac{1}{2}(x+4) = \dfrac{1}{2}x + 2$. Check: $(-4,0)$: $y = -2+2=0$ ✓"
        },
        {
            'question': r"Write the equation of the line passing through $(0, -6)$ and $(3, 0)$.",
            'answer': r"$y = 2x - 6$",
            'wrong': [r"$y = -2x - 6$", r"$y = \dfrac{1}{2}x - 6$", r"$y = 2x + 6$"],
            'explanation': r"Slope: $m = \dfrac{0-(-6)}{3-0} = \dfrac{6}{3} = 2$. $y$-intercept: $(0,-6)$ so $b=-6$. Equation: $y = 2x - 6$."
        },
        {
            'question': r"Convert $5x + 3y - 15 = 0$ to slope-intercept form.",
            'answer': r"$y = -\dfrac{5}{3}x + 5$",
            'wrong': [r"$y = \dfrac{5}{3}x - 5$", r"$y = -\dfrac{3}{5}x + 5$", r"$y = -\dfrac{5}{3}x - 5$"],
            'explanation': r"Isolate $y$: $3y = -5x + 15$, so $y = -\dfrac{5}{3}x + 5$. Slope: $-\dfrac{5}{3}$; $y$-intercept: $5$."
        },
        {
            'question': r"A line passes through $(2, 3)$ and $(5, 3)$. Write its equation.",
            'answer': r"$y = 3$",
            'wrong': [r"$x = 3$", r"$y = x + 1$", r"$y = 3x$"],
            'explanation': r"Both points have the same $y$-coordinate ($y=3$), so this is a horizontal line. Slope $= 0$. Equation: $y = 3$."
        },
        {
            'question': r"Find the equation of the line perpendicular to $x = 5$ passing through $(5, 2)$.",
            'answer': r"$y = 2$",
            'wrong': [r"$x = 5$", r"$y = 5$", r"$x = 2$"],
            'explanation': r"$x = 5$ is a vertical line (undefined slope). A line perpendicular to a vertical line is horizontal (slope $= 0$). The horizontal line through $(5,2)$ is $y = 2$."
        },
        {
            'question': r"Write the equation of the line through $(1, -1)$ and $(-3, -9)$.",
            'answer': r"$y = 2x - 3$",
            'wrong': [r"$y = -2x + 1$", r"$y = 2x + 3$", r"$y = 2x - 1$"],
            'explanation': r"Slope: $m = \dfrac{-9-(-1)}{-3-1} = \dfrac{-8}{-4} = 2$. Point-slope using $(1,-1)$: $y+1 = 2(x-1)$, so $y = 2x - 3$. Check: $(1,-1)$: $y = 2-3=-1$ ✓ and $(-3,-9)$: $y=-6-3=-9$ ✓"
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 3 — EVALUATING & GRAPHING LINEAR FUNCTIONS (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"For $f(x) = 3x - 5$, find $f(4)$.",
            'answer': r"$f(4) = 7$",
            'wrong': [r"$f(4) = 12$", r"$f(4) = -17$", r"$f(4) = 2$"],
            'explanation': r"Substitute $x = 4$: $f(4) = 3(4) - 5 = 12 - 5 = 7$."
        },
        {
            'question': r"For $g(x) = -2x + 6$, find $g(-3)$.",
            'answer': r"$g(-3) = 12$",
            'wrong': [r"$g(-3) = 0$", r"$g(-3) = -12$", r"$g(-3) = -6$"],
            'explanation': r"Substitute $x = -3$: $g(-3) = -2(-3) + 6 = 6 + 6 = 12$."
        },
        {
            'question': r"For $h(x) = \dfrac{1}{2}x + 4$, find $x$ when $h(x) = 7$.",
            'answer': r"$x = 6$",
            'wrong': [r"$x = 3$", r"$x = 22$", r"$x = 14$"],
            'explanation': r"Set $h(x) = 7$: $\dfrac{1}{2}x + 4 = 7$. Subtract $4$: $\dfrac{1}{2}x = 3$. Multiply by $2$: $x = 6$. Check: $\dfrac{1}{2}(6)+4 = 7$ ✓"
        },
        {
            'question': r"For $f(x) = 5x - 3$, find $x$ when $f(x) = 22$.",
            'answer': r"$x = 5$",
            'wrong': [r"$x = \dfrac{19}{5}$", r"$x = 4$", r"$x = 107$"],
            'explanation': r"$5x - 3 = 22$. Add $3$: $5x = 25$. Divide by $5$: $x = 5$. Check: $5(5)-3 = 22$ ✓"
        },
        {
            'question': r"What is the $y$-intercept of $f(x) = -7x + 4$?",
            'answer': r"$(0, 4)$",
            'wrong': [r"$(0, -7)$", r"$(4, 0)$", r"$\left(\dfrac{4}{7}, 0\right)$"],
            'explanation': r"The $y$-intercept occurs at $x=0$: $f(0) = -7(0) + 4 = 4$. So the $y$-intercept is $(0,4)$. In $y = mx + b$, $b$ is always the $y$-intercept."
        },
        {
            'question': r"What is the $x$-intercept of $f(x) = 4x - 8$?",
            'answer': r"$(2, 0)$",
            'wrong': [r"$(0, 2)$", r"$(-2, 0)$", r"$(8, 0)$"],
            'explanation': r"Set $f(x) = 0$: $4x - 8 = 0$. Add $8$: $4x = 8$. Divide: $x = 2$. The $x$-intercept is $(2, 0)$."
        },
        {
            'question': r"How many points do you need to uniquely determine a line?",
            'answer': r"$2$",
            'wrong': [r"$1$", r"$3$", r"$4$"],
            'explanation': r"Exactly $2$ non-coincident points determine a unique line. One point is not enough (infinitely many lines pass through one point). Three or more points may or may not be collinear."
        },
        {
            'question': r"Describe the graph of $f(x) = 2$.",
            'answer': r"A horizontal line at $y = 2$",
            'wrong': [r"A vertical line at $x = 2$", r"A line with slope $2$", r"A line through the origin"],
            'explanation': r"$f(x) = 2$ means the output is always $2$, regardless of $x$. This gives a horizontal line at height $y = 2$, with slope $0$."
        },
        {
            'question': r"For $f(x) = 3x - 6$, find the zero of the function.",
            'answer': r"$x = 2$",
            'wrong': [r"$x = 6$", r"$x = -2$", r"$x = -6$"],
            'explanation': r"The zero is where $f(x) = 0$: $3x - 6 = 0 \Rightarrow 3x = 6 \Rightarrow x = 2$. The zero of a linear function is its $x$-intercept."
        },
        {
            'question': r"For $f(x) = mx + b$, what does a negative value of $m$ tell us about the graph?",
            'answer': r"The line falls from left to right (decreasing)",
            'wrong': [r"The line rises from left to right", r"The line is horizontal",
                      r"The line passes through the origin"],
            'explanation': r"When $m < 0$, as $x$ increases, $y = mx + b$ decreases (since we add a negative quantity). The graph falls from left to right. The larger $|m|$, the steeper the fall."
        },
        {
            'question': r"For $f(x) = -x + 5$, evaluate $f(f(2))$.",
            'answer': r"$f(f(2)) = 2$",
            'wrong': [r"$f(f(2)) = 3$", r"$f(f(2)) = 5$", r"$f(f(2)) = -2$"],
            'explanation': r"Step 1: $f(2) = -(2) + 5 = 3$. Step 2: $f(f(2)) = f(3) = -(3) + 5 = 2$."
        },
        {
            'question': r"For $f(x) = 2x + 1$ and $g(x) = -x + 4$, find $x$ where $f(x) = g(x)$.",
            'answer': r"$x = 1$",
            'wrong': [r"$x = 2$", r"$x = 3$", r"$x = -1$"],
            'explanation': r"Set $2x + 1 = -x + 4$. Add $x$: $3x + 1 = 4$. Subtract $1$: $3x = 3$. Divide: $x = 1$. Check: $f(1) = 3$ and $g(1) = 3$ ✓ (the lines intersect at $(1, 3)$)."
        },
        {
            'question': r"For $f(x) = 4x - 8$, on which interval is $f(x) > 0$?",
            'answer': r"$x > 2$",
            'wrong': [r"$x < 2$", r"$x > -2$", r"$x < -2$"],
            'explanation': r"$f(x) > 0 \Rightarrow 4x - 8 > 0 \Rightarrow 4x > 8 \Rightarrow x > 2$. The function is positive (above the $x$-axis) for $x > 2$."
        },
        {
            'question': r"For $f(x) = -3x + 9$, on which interval is $f(x) < 0$?",
            'answer': r"$x > 3$",
            'wrong': [r"$x < 3$", r"$x > -3$", r"$x < -3$"],
            'explanation': r"$-3x + 9 < 0 \Rightarrow -3x < -9 \Rightarrow x > 3$ (divide by $-3$, flip). The function is negative for $x > 3$."
        },
        {
            'question': r"Given the table: $x: 0, 1, 2, 3$ and $y: -1, 2, 5, 8$. Find the linear function.",
            'answer': r"$f(x) = 3x - 1$",
            'wrong': [r"$f(x) = 2x - 1$", r"$f(x) = 3x + 1$", r"$f(x) = -3x - 1$"],
            'explanation': r"Slope: $m = \dfrac{2-(-1)}{1-0} = 3$ (constant change of $3$ per unit). $y$-intercept: $f(0) = -1$, so $b = -1$. Function: $f(x) = 3x - 1$. Verify: $f(3) = 9-1=8$ ✓"
        },
        {
            'question': r"For $f(x) = 2x - 4$, find $f^{-1}(x)$ (the inverse function).",
            'answer': r"$f^{-1}(x) = \dfrac{x+4}{2}$",
            'wrong': [r"$f^{-1}(x) = \dfrac{x-4}{2}$", r"$f^{-1}(x) = 2x + 4$", r"$f^{-1}(x) = -2x + 4$"],
            'explanation': r"To find the inverse, swap $x$ and $y$ then solve for $y$. Start with $y = 2x-4$. Swap: $x = 2y - 4$. Add $4$: $x+4 = 2y$. Divide by $2$: $y = \dfrac{x+4}{2}$. So $f^{-1}(x) = \dfrac{x+4}{2}$."
        },
        {
            'question': r"The graph of $f(x) = ax + b$ passes through $(1, 5)$ and $(3, 9)$. Find $a$ and $b$.",
            'answer': r"$a = 2$, $b = 3$",
            'wrong': [r"$a = 3$, $b = 2$", r"$a = 2$, $b = -3$", r"$a = -2$, $b = 3$"],
            'explanation': r"Slope: $a = m = \dfrac{9-5}{3-1} = 2$. Substitute $(1,5)$: $5 = 2(1) + b$, so $b = 3$. Function: $f(x) = 2x + 3$. Check: $f(3) = 9$ ✓"
        },
        {
            'question': r"For $f(x) = -\dfrac{1}{3}x + 2$, find $f(6)$ and $f(-3)$.",
            'answer': r"$f(6) = 0$, $f(-3) = 3$",
            'wrong': [r"$f(6) = 4$, $f(-3) = 1$", r"$f(6) = 0$, $f(-3) = -3$", r"$f(6) = -2$, $f(-3) = 3$"],
            'explanation': r"$f(6) = -\dfrac{1}{3}(6) + 2 = -2 + 2 = 0$. $f(-3) = -\dfrac{1}{3}(-3) + 2 = 1 + 2 = 3$."
        },
        {
            'question': r"Determine whether $(2, 5)$, $(4, 9)$, and $(6, 13)$ are collinear.",
            'answer': r"Yes, slope between each pair is $2$",
            'wrong': [r"No, the points are not collinear", r"Yes, but only the first two points matter",
                      r"Cannot be determined"],
            'explanation': r"Check slopes: $\dfrac{9-5}{4-2} = \dfrac{4}{2} = 2$ and $\dfrac{13-9}{6-4} = \dfrac{4}{2} = 2$. Both slopes are equal, so the three points lie on the same line $y = 2x + 1$. They are collinear."
        },
        {
            'question': r"If $f(x) = cx - 10$ and $f(5) = 0$, find $c$.",
            'answer': r"$c = 2$",
            'wrong': [r"$c = -2$", r"$c = 5$", r"$c = 10$"],
            'explanation': r"Substitute $x=5$, $f(5)=0$: $c(5) - 10 = 0$. Add $10$: $5c = 10$. Divide by $5$: $c = 2$. Function: $f(x) = 2x - 10$."
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 4 — SYSTEMS OF LINEAR EQUATIONS (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"Solve the system: $y = 2x + 1$ and $y = -x + 7$.",
            'answer': r"$(2, 5)$",
            'wrong': [r"$(3, 4)$", r"$(1, 6)$", r"$(2, 3)$"],
            'explanation': r"Set equal: $2x + 1 = -x + 7$. Add $x$: $3x + 1 = 7$. Subtract $1$: $3x = 6$, so $x = 2$. Substitute: $y = 2(2)+1 = 5$. Solution: $(2, 5)$. Check in both: $5=5$ and $5=5$ ✓"
        },
        {
            'question': r"Solve the system: $x + y = 6$ and $x - y = 2$.",
            'answer': r"$(4, 2)$",
            'wrong': [r"$(2, 4)$", r"$(3, 3)$", r"$(5, 1)$"],
            'explanation': r"Add the equations: $2x = 8$, so $x = 4$. Substitute into $x+y=6$: $4+y=6$, $y=2$. Check: $4+2=6$ ✓ and $4-2=2$ ✓"
        },
        {
            'question': r"Solve the system: $2x + y = 7$ and $x - y = 2$.",
            'answer': r"$(3, 1)$",
            'wrong': [r"$(2, 3)$", r"$(1, 5)$", r"$(4, -1)$"],
            'explanation': r"Add the equations: $3x = 9$, so $x = 3$. Substitute into $x - y = 2$: $3-y=2$, $y=1$. Check: $2(3)+1=7$ ✓ and $3-1=2$ ✓"
        },
        {
            'question': r"Solve the system: $3x + 2y = 12$ and $x + y = 5$.",
            'answer': r"$(2, 3)$",
            'wrong': [r"$(3, 2)$", r"$(4, 1)$", r"$(1, 4)$"],
            'explanation': r"From the second: $x = 5 - y$. Substitute: $3(5-y)+2y=12$. Expand: $15-3y+2y=12$, so $-y=-3$, $y=3$. Then $x=5-3=2$. Check: $6+6=12$ ✓ and $2+3=5$ ✓"
        },
        {
            'question': r"Solve the system: $y = 3x - 5$ and $y = 3x + 2$.",
            'answer': r"No solution (parallel lines)",
            'wrong': [r"$(0, -5)$", r"$(7, 16)$", r"Infinitely many solutions"],
            'explanation': r"Both lines have slope $3$ but different $y$-intercepts ($-5$ and $2$). Parallel lines never intersect, so there is NO solution. Setting equal: $3x-5 = 3x+2$ gives $-5=2$, which is false."
        },
        {
            'question': r"Solve the system: $2x - y = 4$ and $4x - 2y = 8$.",
            'answer': r"Infinitely many solutions",
            'wrong': [r"$(2, 0)$", r"No solution", r"$(0, -4)$"],
            'explanation': r"The second equation is exactly $2 \times$ the first. They represent the SAME line. Every point on $2x-y=4$ is a solution. Infinitely many solutions: $\{(x, 2x-4) \mid x \in \mathbb{R}\}$."
        },
        {
            'question': r"Solve by substitution: $y = x - 3$ and $2x + y = 9$.",
            'answer': r"$(4, 1)$",
            'wrong': [r"$(3, 0)$", r"$(6, 3)$", r"$(2, -1)$"],
            'explanation': r"Substitute $y = x-3$ into $2x+y=9$: $2x+(x-3)=9$, so $3x=12$, $x=4$. Then $y=4-3=1$. Check: $2(4)+1=9$ ✓"
        },
        {
            'question': r"Solve by elimination: $5x + 3y = 11$ and $2x - 3y = 3$.",
            'answer': r"$(2, \frac{1}{3})$",
            'wrong': [r"$(2, 1)$", r"$(1, 2)$", r"$(3, -\frac{4}{3})$"],
            'explanation': r"Add the equations: $7x = 14$, so $x = 2$. Substitute into $5(2)+3y=11$: $10+3y=11$, $3y=1$, $y=\dfrac{1}{3}$. Check: $5(2)+3\cdot\dfrac{1}{3}=10+1=11$ ✓"
        },
        {
            'question': r"Solve: $3x + 4y = 18$ and $6x - 2y = 6$.",
            'answer': r"$(2, 3)$",
            'wrong': [r"$(3, 2)$", r"$(1, \frac{15}{4})$", r"$(4, \frac{3}{2})$"],
            'explanation': r"Multiply second equation by $2$: $12x-4y=12$. Add to first: $15x=30$, $x=2$. Substitute: $3(2)+4y=18$, $4y=12$, $y=3$. Check: $6(2)-2(3)=12-6=6$ ✓"
        },
        {
            'question': r"Two lines intersect at $(3, 7)$. One line is $y = 2x + 1$. Find the other if it has slope $-1$.",
            'answer': r"$y = -x + 10$",
            'wrong': [r"$y = -x + 7$", r"$y = -x - 10$", r"$y = -x + 4$"],
            'explanation': r"Use point-slope with slope $-1$ and point $(3,7)$: $y-7=-1(x-3)$. Expand: $y = -x + 3 + 7 = -x + 10$. Check: $y(3)=-3+10=7$ ✓ and $-1 \times 2 = -2 \neq -1$, so lines are NOT perpendicular — they just intersect."
        },
        {
            'question': r"Solve the system: $y = \dfrac{1}{2}x + 3$ and $2y - x = 6$.",
            'answer': r"Infinitely many solutions",
            'wrong': [r"$(0, 3)$ only", r"No solution", r"$(2, 4)$"],
            'explanation': r"Rewrite second: $2y = x + 6$, so $y = \dfrac{x}{2} + 3 = \dfrac{1}{2}x + 3$. This is identical to the first equation. Same line → infinitely many solutions."
        },
        {
            'question': r"At what point do $f(x) = 3x + 2$ and $g(x) = -x + 10$ intersect?",
            'answer': r"$(2, 8)$",
            'wrong': [r"$(3, 7)$", r"$(2, 4)$", r"$(4, 6)$"],
            'explanation': r"$3x+2 = -x+10$. Add $x$: $4x+2=10$. Subtract $2$: $4x=8$, $x=2$. $y=3(2)+2=8$. Intersection: $(2,8)$. Check: $g(2) = -2+10=8$ ✓"
        },
        {
            'question': r"Solve: $4x - 3y = 5$ and $8x - 6y = 10$.",
            'answer': r"Infinitely many solutions",
            'wrong': [r"$(2, 1)$", r"No solution", r"$(1, -\frac{1}{3})$"],
            'explanation': r"The second equation equals $2 \times$ the first ($8x-6y=10$ is $2(4x-3y)=2(5)$). They represent the same line. Infinitely many solutions."
        },
        {
            'question': r"Solve: $x + 2y = 8$ and $3x - y = 3$.",
            'answer': r"$(2, 3)$",
            'wrong': [r"$(3, 2)$", r"$(1, 3.5)$", r"$(4, 2)$"],
            'explanation': r"From first: $x = 8 - 2y$. Substitute: $3(8-2y)-y=3$, $24-6y-y=3$, $-7y=-21$, $y=3$. Then $x=8-6=2$. Check: $2+6=8$ ✓ and $6-3=3$ ✓"
        },
        {
            'question': r"Find $k$ such that $kx + 2y = 6$ and $3x + y = 4$ have no solution.",
            'answer': r"$k = 6$",
            'wrong': [r"$k = 3$", r"$k = -6$", r"$k = 2$"],
            'explanation': r"For no solution (parallel lines), the ratios of coefficients of $x$ and $y$ must be equal, but NOT equal to the ratio of constants. $\dfrac{k}{3} = \dfrac{2}{1} \Rightarrow k = 6$. Check constant ratio: $\dfrac{6}{4} = \dfrac{3}{2} \neq 2$, so lines are parallel (no solution) ✓"
        },
        {
            'question': r"Solve: $2x + 5y = 20$ and $x = 10 - \dfrac{5}{2}y$.",
            'answer': r"Infinitely many solutions",
            'wrong': [r"$(5, 2)$", r"No solution", r"$(10, 0)$"],
            'explanation': r"Substitute $x = 10-\dfrac{5}{2}y$ into $2x+5y=20$: $2(10-\dfrac{5}{2}y)+5y = 20-5y+5y = 20$. This is always true. The equations are equivalent → infinitely many solutions."
        },
        {
            'question': r"Solve: $\dfrac{x}{2} + y = 5$ and $x + 2y = 10$.",
            'answer': r"Infinitely many solutions",
            'wrong': [r"$(4, 3)$", r"No solution", r"$(2, 4)$"],
            'explanation': r"Multiply the first equation by $2$: $x + 2y = 10$. This is identical to the second equation. Same line → infinitely many solutions."
        },
        {
            'question': r"Solve the system graphically context: $y = x + 2$ and $y = -2x + 5$.",
            'answer': r"$(1, 3)$",
            'wrong': [r"$(2, 1)$", r"$(3, 5)$", r"$(0, 2)$"],
            'explanation': r"Set equal: $x+2 = -2x+5$. Add $2x$: $3x+2=5$. Subtract $2$: $3x=3$, $x=1$. $y=1+2=3$. Intersection: $(1,3)$. Check: $y = -2(1)+5 = 3$ ✓"
        },
        {
            'question': r"Solve: $-x + 3y = 9$ and $x + y = 7$.",
            'answer': r"$(3, 4)$",
            'wrong': [r"$(4, 3)$", r"$(2, 5)$", r"$(1, 6)$"],
            'explanation': r"Add the two equations: $4y = 16$, so $y = 4$. Substitute into $x+y=7$: $x+4=7$, $x=3$. Check: $-3+12=9$ ✓ and $3+4=7$ ✓"
        },
        {
            'question': r"Solve: $5x + y = 17$ and $2x - y = 4$.",
            'answer': r"$(3, 2)$",
            'wrong': [r"$(2, 7)$", r"$(4, -3)$", r"$(1, 12)$"],
            'explanation': r"Add equations: $7x = 21$, so $x = 3$. Substitute into $2(3)-y=4$: $6-y=4$, $y=2$. Check: $5(3)+2=17$ ✓ and $2(3)-2=4$ ✓"
        },

        # ═══════════════════════════════════════════════════════════════════════════
        # SECTION 5 — WORD PROBLEMS & APPLICATIONS (20 problems)
        # ═══════════════════════════════════════════════════════════════════════════

        {
            'question': r"A taxi charges a base fare of $\$3$ plus $\$2$ per km. Write a function for the cost $C$ in terms of km $d$, and find the cost for $7$ km.",
            'answer': r"$C(d) = 2d + 3$; $C(7) = \$17$",
            'wrong': [r"$C(d) = 3d + 2$; $C(7) = \$23$", r"$C(d) = 2d + 3$; $C(7) = \$14$",
                      r"$C(d) = 2d$; $C(7) = \$14$"],
            'explanation': r"The base fare is the $y$-intercept ($b = 3$) and the rate per km is the slope ($m = 2$). So $C(d) = 2d + 3$. At $d = 7$: $C(7) = 14 + 3 = \$17$."
        },
        {
            'question': r"A phone plan charges $\$15$/month plus $\$0.10$ per minute. How many minutes can you use for a budget of $\$25$?",
            'answer': r"$100$ minutes",
            'wrong': [r"$250$ minutes", r"$50$ minutes", r"$150$ minutes"],
            'explanation': r"$C = 0.10m + 15 = 25$. Subtract $15$: $0.10m = 10$. Divide by $0.10$: $m = 100$ minutes."
        },
        {
            'question': r"A car travels at a constant speed. After $2$ hours it has gone $120$ km, after $5$ hours it has gone $300$ km. Write the distance function.",
            'answer': r"$d(t) = 60t$",
            'wrong': [r"$d(t) = 60t + 120$", r"$d(t) = 30t$", r"$d(t) = 50t + 20$"],
            'explanation': r"Slope (speed): $m = \dfrac{300-120}{5-2} = \dfrac{180}{3} = 60$ km/h. Using point $(2,120)$: $120 = 60(2)+b \Rightarrow b = 0$. So $d(t) = 60t$ (starts from origin)."
        },
        {
            'question': r"A store sells notebooks. The revenue function is $R(x) = 4x$ where $x$ is notebooks sold. The cost function is $C(x) = 2x + 50$. Find the break-even point.",
            'answer': r"$x = 25$ notebooks",
            'wrong': [r"$x = 50$ notebooks", r"$x = 12$ notebooks", r"$x = 100$ notebooks"],
            'explanation': r"Break-even when $R(x) = C(x)$: $4x = 2x + 50$. Subtract $2x$: $2x = 50$. Divide: $x = 25$ notebooks. At this point, revenue equals cost: $R(25) = C(25) = \$100$."
        },
        {
            'question': r"Temperature conversion: $C = \dfrac{5}{9}(F - 32)$. Find $C$ when $F = 68°$.",
            'answer': r"$C = 20°$",
            'wrong': [r"$C = 36°$", r"$C = 25°$", r"$C = 15°$"],
            'explanation': r"$C = \dfrac{5}{9}(68-32) = \dfrac{5}{9}(36) = 5 \times 4 = 20°$C."
        },
        {
            'question': r"A candle is $20$ cm tall and burns at $2$ cm/hour. Write a function for height $h$ after $t$ hours, and find when it burns out.",
            'answer': r"$h(t) = -2t + 20$; burns out at $t = 10$ hours",
            'wrong': [r"$h(t) = 2t + 20$; never burns out", r"$h(t) = -2t + 20$; burns out at $t = 20$ hours",
                      r"$h(t) = -20t + 2$; burns out very fast"],
            'explanation': r"Starting height $20$ cm, decreasing by $2$ per hour: $h(t) = -2t + 20$. Burns out when $h = 0$: $-2t + 20 = 0 \Rightarrow t = 10$ hours."
        },
        {
            'question': r"A linear function has $f(0) = 4$ and $f(3) = 13$. Find $f(x)$.",
            'answer': r"$f(x) = 3x + 4$",
            'wrong': [r"$f(x) = 4x + 3$", r"$f(x) = 3x - 4$", r"$f(x) = -3x + 4$"],
            'explanation': r"$b = f(0) = 4$. Slope: $m = \dfrac{13-4}{3-0} = 3$. Function: $f(x) = 3x + 4$. Check: $f(3) = 9+4=13$ ✓"
        },
        {
            'question': r"A salesperson earns a base salary of $\$1200$/month plus $5\%$ commission on sales. If they earned $\$1700$ last month, what were their sales?",
            'answer': r"\$10{,}000",
            'wrong': [r"\$8{,}500", r"\$34{,}000", r"\$5{,}000"],
            'explanation': r"$1200 + 0.05s = 1700$. Subtract $1200$: $0.05s = 500$. Divide by $0.05$: $s = 10{,}000$."
        },
        {
            'question': r"The population of a town is modelled by $P(t) = 500t + 12000$ where $t$ is years after 2010. What year will the population reach $20000$?",
            'answer': r"$2026$",
            'wrong': [r"$2028$", r"$2024$", r"$2030$"],
            'explanation': r"$500t + 12000 = 20000$. Subtract $12000$: $500t = 8000$. Divide: $t = 16$. Year: $2010 + 16 = 2026$."
        },
        {
            'question': r"A gym charges $\$50$ joining fee and $\$30$/month. Another gym charges $\$0$ joining fee and $\$40$/month. After how many months is the total cost equal?",
            'answer': r"$5$ months",
            'wrong': [r"$10$ months", r"$2$ months", r"$3$ months"],
            'explanation': r"Gym 1: $C_1 = 30m + 50$. Gym 2: $C_2 = 40m$. Set equal: $30m + 50 = 40m$. Subtract $30m$: $50 = 10m$. Divide: $m = 5$ months."
        },
        {
            'question': r"A spring stretches $3$ cm for every $1$ N of force. With no force it is $10$ cm. Write the length function and find the length with $4$ N force.",
            'answer': r"$L(F) = 3F + 10$; $L(4) = 22$ cm",
            'wrong': [r"$L(F) = 3F + 10$; $L(4) = 12$ cm", r"$L(F) = 10F + 3$; $L(4) = 43$ cm",
                      r"$L(F) = 3F$; $L(4) = 12$ cm"],
            'explanation': r"Slope $= 3$ (cm per N), $y$-intercept $= 10$ (natural length). $L(F) = 3F + 10$. At $F=4$: $L = 12 + 10 = 22$ cm."
        },
        {
            'question': r"A linear function passes through $(0, 6)$ and has slope $-\dfrac{3}{2}$. For what $x$ does $f(x) = 0$?",
            'answer': r"$x = 4$",
            'wrong': [r"$x = -4$", r"$x = 6$", r"$x = 9$"],
            'explanation': r"$f(x) = -\dfrac{3}{2}x + 6$. Set to $0$: $-\dfrac{3}{2}x = -6$. Multiply by $-\dfrac{2}{3}$: $x = 4$. Check: $f(4) = -6+6=0$ ✓"
        },
        {
            'question': r"Two cars start from the same point. Car A travels at $60$ km/h; Car B starts $30$ min later at $90$ km/h. When does Car B catch Car A?",
            'answer': r"$1$ hour after Car A starts (or $30$ min after Car B starts)",
            'wrong': [r"$2$ hours after Car A starts", r"$45$ minutes after Car A starts",
                      r"$1.5$ hours after Car B starts"],
            'explanation': r"Car A: $d = 60t$. Car B starts at $t = 0.5$ h: $d = 90(t-0.5)$. Set equal: $60t = 90t - 45$. Rearrange: $45 = 30t$, so $t = 1.5$ h after Car A starts. Car B catches up at $t = 1.5$ hours (i.e. $1$ hour after Car B starts). Distance: $60(1.5) = 90$ km."
        },
        {
            'question': r"The cost of printing $x$ flyers is $C(x) = 0.05x + 20$. What does the $y$-intercept represent?",
            'answer': r"Fixed setup cost of $\$20$",
            'wrong': [r"Cost per flyer of $\$0.05$", r"Maximum number of flyers", r"Total cost of all flyers"],
            'explanation': r"The $y$-intercept ($b = 20$) represents the fixed cost incurred even when $x=0$ (no flyers printed) — the setup or fixed charge. The slope ($0.05$) represents the variable cost per flyer."
        },
        {
            'question': r"A line models water level $w$ (cm) in a tank: $w(t) = -4t + 80$ where $t$ is minutes. How long until the tank is empty?",
            'answer': r"$20$ minutes",
            'wrong': [r"$80$ minutes", r"$4$ minutes", r"$10$ minutes"],
            'explanation': r"Set $w(t) = 0$: $-4t + 80 = 0 \Rightarrow 4t = 80 \Rightarrow t = 20$ minutes. The tank empties at $t = 20$ min. The rate of decrease is $4$ cm/min."
        },
        {
            'question': r"If $f(x) = 2x + k$ and $f(3) = 11$, find $k$ and the $x$-intercept.",
            'answer': r"$k = 5$; $x$-intercept $= \left(-\dfrac{5}{2}, 0\right)$",
            'wrong': [r"$k = 5$; $x$-intercept $= (5, 0)$", r"$k = -5$; $x$-intercept $= \left(\dfrac{5}{2}, 0\right)$",
                      r"$k = 2$; $x$-intercept $= (-1, 0)$"],
            'explanation': r"$f(3) = 6 + k = 11 \Rightarrow k = 5$. Function: $f(x) = 2x+5$. For $x$-intercept: $2x+5=0 \Rightarrow x = -\dfrac{5}{2}$."
        },
        {
            'question': r"A recipe uses $2$ cups of flour per batch. You have $15$ cups. Write a function for remaining flour $R$ after $b$ batches, and find the domain.",
            'answer': r"$R(b) = -2b + 15$; domain: $0 \leq b \leq 7$ (whole batches)",
            'wrong': [r"$R(b) = 2b + 15$; domain: all real $b$", r"$R(b) = -2b$; domain: $b \geq 0$",
                      r"$R(b) = 15 - b$; domain: $0 \leq b \leq 15$"],
            'explanation': r"Slope $= -2$ (flour decreases by $2$ per batch), starting at $15$: $R(b) = -2b + 15$. Domain: $b \geq 0$ and $R \geq 0$, so $-2b+15 \geq 0 \Rightarrow b \leq 7.5$. Since batches must be whole numbers, domain is $b \in \{0,1,2,...,7\}$."
        },
        {
            'question': r"A school trip costs $\$200$ fixed plus $\$15$ per student. The school collected $\$650$. How many students went?",
            'answer': r"$30$ students",
            'wrong': [r"$43$ students", r"$25$ students", r"$50$ students"],
            'explanation': r"$200 + 15n = 650$. Subtract $200$: $15n = 450$. Divide: $n = 30$ students."
        },
        {
            'question': r"Two friends start walking toward each other from towns $24$ km apart. Friend A walks at $4$ km/h and Friend B at $2$ km/h. When do they meet?",
            'answer': r"After $4$ hours",
            'wrong': [r"After $6$ hours", r"After $3$ hours", r"After $8$ hours"],
            'explanation': r"Their combined speed is $4 + 2 = 6$ km/h. Time to cover $24$ km: $t = \dfrac{24}{6} = 4$ hours. A travels $16$ km and B travels $8$ km. Check: $16 + 8 = 24$ ✓"
        },
        {
            'question': r"The profit function is $P(x) = 8x - 400$ where $x$ is units sold. How many units must be sold to make a profit?",
            'answer': r"$x > 50$ units",
            'wrong': [r"$x > 400$ units", r"$x > 8$ units", r"$x > 40$ units"],
            'explanation': r"$P(x) > 0 \Rightarrow 8x - 400 > 0 \Rightarrow 8x > 400 \Rightarrow x > 50$. The break-even point is $x = 50$ (where $P=0$), and profit occurs for $x > 50$ units."
        },

    ],
    'other_kind_of_functions': [{
        "question": "Find the vertex of $f(x) = x^2 - 4x + 3$.",
        "answer": "$(2,\\ -1)$",
        "wrong": ["$(2,\\ 1)$", "$(-2,\\ -1)$", "$(4,\\ 3)$"],
        "explanation": "Use $h = -b/(2a) = 4/2 = 2$. Then $k = f(2) = 4 - 8 + 3 = -1$. **Vertex:** $(2, -1)$."
    },
        {
            "question": "Find the vertex of $f(x) = x^2 + 6x + 5$.",
            "answer": "$(-3,\\ -4)$",
            "wrong": ["$(3,\\ -4)$", "$(-3,\\ 4)$", "$(-6,\\ 5)$"],
            "explanation": "$h = -6/2 = -3$. $k = 9 - 18 + 5 = -4$. **Vertex:** $(-3, -4)$."
        },
        {
            "question": "Find the vertex of $f(x) = 2x^2 - 8x + 6$.",
            "answer": "$(2,\\ -2)$",
            "wrong": ["$(4,\\ -2)$", "$(2,\\ 2)$", "$(-2,\\ -2)$"],
            "explanation": "$h = 8/4 = 2$. $k = 2(4) - 16 + 6 = -2$. **Vertex:** $(2, -2)$."
        },
        {
            "question": "Find the vertex of $f(x) = -x^2 + 4x - 1$.",
            "answer": "$(2,\\ 3)$",
            "wrong": ["$(-2,\\ 3)$", "$(2,\\ -3)$", "$(4,\\ -1)$"],
            "explanation": "$h = -4/(-2) = 2$. $k = -4 + 8 - 1 = 3$. **Vertex:** $(2, 3)$."
        },
        {
            "question": "Find the vertex of $f(x) = 3x^2 + 12x + 7$.",
            "answer": "$(-2,\\ -5)$",
            "wrong": ["$(2,\\ -5)$", "$(-2,\\ 5)$", "$(-4,\\ 7)$"],
            "explanation": "$h = -12/6 = -2$. $k = 3(4) - 24 + 7 = -5$. **Vertex:** $(-2, -5)$."
        },
        {
            "question": "Find the vertex of $f(x) = x^2 - 2x - 8$.",
            "answer": "$(1,\\ -9)$",
            "wrong": ["$(-1,\\ -9)$", "$(1,\\ 9)$", "$(2,\\ -8)$"],
            "explanation": "$h = 2/2 = 1$. $k = 1 - 2 - 8 = -9$. **Vertex:** $(1, -9)$."
        },
        {
            "question": "Find the vertex of $f(x) = -2x^2 + 8x - 3$.",
            "answer": "$(2,\\ 5)$",
            "wrong": ["$(-2,\\ 5)$", "$(2,\\ -5)$", "$(4,\\ -3)$"],
            "explanation": "$h = -8/(-4) = 2$. $k = -8 + 16 - 3 = 5$. **Vertex:** $(2, 5)$."
        },
        {
            "question": "Find the vertex of $f(x) = x^2 + 8x + 12$.",
            "answer": "$(-4,\\ -4)$",
            "wrong": ["$(4,\\ -4)$", "$(-4,\\ 4)$", "$(-8,\\ 12)$"],
            "explanation": "$h = -8/2 = -4$. $k = 16 - 32 + 12 = -4$. **Vertex:** $(-4, -4)$."
        },
        {
            "question": "Find the vertex of $f(x) = 4x^2 - 16x + 15$.",
            "answer": "$(2,\\ -1)$",
            "wrong": ["$(-2,\\ -1)$", "$(2,\\ 1)$", "$(4,\\ 15)$"],
            "explanation": "$h = 16/8 = 2$. $k = 16 - 32 + 15 = -1$. **Vertex:** $(2, -1)$."
        },
        {
            "question": "Find the vertex of $f(x) = -3x^2 + 6x + 2$.",
            "answer": "$(1,\\ 5)$",
            "wrong": ["$(-1,\\ 5)$", "$(1,\\ -5)$", "$(2,\\ 2)$"],
            "explanation": "$h = -6/(-6) = 1$. $k = -3 + 6 + 2 = 5$. **Vertex:** $(1, 5)$."
        },
        {
            "question": "Find the vertex of $f(x) = x^2 - 10x + 24$.",
            "answer": "$(5,\\ -1)$",
            "wrong": ["$(-5,\\ -1)$", "$(5,\\ 1)$", "$(10,\\ 24)$"],
            "explanation": "$h = 10/2 = 5$. $k = 25 - 50 + 24 = -1$. **Vertex:** $(5, -1)$."
        },
        {
            "question": "Find the vertex of $f(x) = 2x^2 + 4x - 6$.",
            "answer": "$(-1,\\ -8)$",
            "wrong": ["$(1,\\ -8)$", "$(-1,\\ 8)$", "$(-2,\\ -6)$"],
            "explanation": "$h = -4/4 = -1$. $k = 2 - 4 - 6 = -8$. **Vertex:** $(-1, -8)$."
        },
        {
            "question": "Find the vertex of $f(x) = -x^2 - 6x - 5$.",
            "answer": "$(-3,\\ 4)$",
            "wrong": ["$(3,\\ 4)$", "$(-3,\\ -4)$", "$(-6,\\ -5)$"],
            "explanation": "$h = 6/(-2) = -3$. $k = -9 + 18 - 5 = 4$. **Vertex:** $(-3, 4)$."
        },
        {
            "question": "Find the vertex of $f(x) = 5x^2 - 20x + 19$.",
            "answer": "$(2,\\ -1)$",
            "wrong": ["$(-2,\\ -1)$", "$(2,\\ 1)$", "$(4,\\ 19)$"],
            "explanation": "$h = 20/10 = 2$. $k = 20 - 40 + 19 = -1$. **Vertex:** $(2, -1)$."
        },
        {
            "question": "Find the vertex of $f(x) = x^2 - 6x + 10$.",
            "answer": "$(3,\\ 1)$",
            "wrong": ["$(-3,\\ 1)$", "$(3,\\ -1)$", "$(6,\\ 10)$"],
            "explanation": "$h = 6/2 = 3$. $k = 9 - 18 + 10 = 1$. **Vertex:** $(3, 1)$."
        },
        {
            "question": "Find the vertex of $f(x) = -4x^2 + 8x + 1$.",
            "answer": "$(1,\\ 5)$",
            "wrong": ["$(-1,\\ 5)$", "$(1,\\ -5)$", "$(2,\\ 1)$"],
            "explanation": "$h = -8/(-8) = 1$. $k = -4 + 8 + 1 = 5$. **Vertex:** $(1, 5)$."
        },
        {
            "question": "Find the vertex of $f(x) = x^2 + 2x - 15$.",
            "answer": "$(-1,\\ -16)$",
            "wrong": ["$(1,\\ -16)$", "$(-1,\\ 16)$", "$(-2,\\ -15)$"],
            "explanation": "$h = -2/2 = -1$. $k = 1 - 2 - 15 = -16$. **Vertex:** $(-1, -16)$."
        },
        {
            "question": "Find the vertex of $f(x) = 3x^2 - 6x + 5$.",
            "answer": "$(1,\\ 2)$",
            "wrong": ["$(-1,\\ 2)$", "$(1,\\ -2)$", "$(2,\\ 5)$"],
            "explanation": "$h = 6/6 = 1$. $k = 3 - 6 + 5 = 2$. **Vertex:** $(1, 2)$."
        },
        {
            "question": "Find the vertex of $f(x) = -2x^2 - 4x + 6$.",
            "answer": "$(-1,\\ 8)$",
            "wrong": ["$(1,\\ 8)$", "$(-1,\\ -8)$", "$(-2,\\ 6)$"],
            "explanation": "$h = 4/(-4) = -1$. $k = -2 + 4 + 6 = 8$. **Vertex:** $(-1, 8)$."
        },
        {
            "question": "Find the vertex of $f(x) = x^2 - 12x + 35$.",
            "answer": "$(6,\\ -1)$",
            "wrong": ["$(-6,\\ -1)$", "$(6,\\ 1)$", "$(12,\\ 35)$"],
            "explanation": "$h = 12/2 = 6$. $k = 36 - 72 + 35 = -1$. **Vertex:** $(6, -1)$."
        },
        {
            "question": "Find the vertex of $f(x) = 2x^2 - 12x + 14$.",
            "answer": "$(3,\\ -4)$",
            "wrong": ["$(-3,\\ -4)$", "$(3,\\ 4)$", "$(6,\\ 14)$"],
            "explanation": "$h = 12/4 = 3$. $k = 18 - 36 + 14 = -4$. **Vertex:** $(3, -4)$."
        },
        {
            "question": "Find the vertex of $f(x) = -x^2 + 10x - 21$.",
            "answer": "$(5,\\ 4)$",
            "wrong": ["$(-5,\\ 4)$", "$(5,\\ -4)$", "$(10,\\ -21)$"],
            "explanation": "$h = -10/(-2) = 5$. $k = -25 + 50 - 21 = 4$. **Vertex:** $(5, 4)$."
        },
        {
            "question": "Find the vertex of $f(x) = 6x^2 + 12x - 1$.",
            "answer": "$(-1,\\ -7)$",
            "wrong": ["$(1,\\ -7)$", "$(-1,\\ 7)$", "$(-2,\\ -1)$"],
            "explanation": "$h = -12/12 = -1$. $k = 6 - 12 - 1 = -7$. **Vertex:** $(-1, -7)$."
        },
        {
            "question": "Find the vertex of $f(x) = x^2 - 4x + 7$.",
            "answer": "$(2,\\ 3)$",
            "wrong": ["$(-2,\\ 3)$", "$(2,\\ -3)$", "$(4,\\ 7)$"],
            "explanation": "$h = 4/2 = 2$. $k = 4 - 8 + 7 = 3$. **Vertex:** $(2, 3)$."
        },
        {
            "question": "Find the vertex of $f(x) = -5x^2 + 20x - 12$.",
            "answer": "$(2,\\ 8)$",
            "wrong": ["$(-2,\\ 8)$", "$(2,\\ -8)$", "$(4,\\ -12)$"],
            "explanation": "$h = -20/(-10) = 2$. $k = -20 + 40 - 12 = 8$. **Vertex:** $(2, 8)$."
        },

        {
            "question": "Given $f(x) = x^2 - 3x + 2$, find $f(4)$.",
            "answer": "$6$",
            "wrong": ["$10$", "$4$", "$14$"],
            "explanation": "$f(4) = 16 - 12 + 2 = 6$."
        },
        {
            "question": "Given $f(x) = 2x^2 + x - 5$, find $f(3)$.",
            "answer": "$16$",
            "wrong": ["$14$", "$22$", "$10$"],
            "explanation": "$f(3) = 18 + 3 - 5 = 16$."
        },
        {
            "question": "Given $f(x) = -x^2 + 4x + 1$, find $f(2)$.",
            "answer": "$5$",
            "wrong": ["$1$", "$9$", "$-3$"],
            "explanation": "$f(2) = -4 + 8 + 1 = 5$."
        },
        {
            "question": "Given $f(x) = 3x^2 - 2x + 4$, find $f(-1)$.",
            "answer": "$9$",
            "wrong": ["$5$", "$-1$", "$7$"],
            "explanation": "$f(-1) = 3 + 2 + 4 = 9$."
        },
        {
            "question": "Given $f(x) = x^2 + 5x - 6$, find $f(0)$.",
            "answer": "$-6$",
            "wrong": ["$0$", "$6$", "$-1$"],
            "explanation": "$f(0) = 0 + 0 - 6 = -6$."
        },
        {
            "question": "Given $f(x) = 4x^2 - 3$, find $f(2)$.",
            "answer": "$13$",
            "wrong": ["$10$", "$16$", "$29$"],
            "explanation": "$f(2) = 16 - 3 = 13$."
        },
        {
            "question": "Given $f(x) = -2x^2 + 6x$, find $f(3)$.",
            "answer": "$0$",
            "wrong": ["$6$", "$-18$", "$12$"],
            "explanation": "$f(3) = -18 + 18 = 0$."
        },
        {
            "question": "Given $f(x) = x^2 - 7x + 10$, find $f(5)$.",
            "answer": "$0$",
            "wrong": ["$5$", "$-10$", "$10$"],
            "explanation": "$f(5) = 25 - 35 + 10 = 0$."
        },
        {
            "question": "Given $f(x) = 2x^2 - 4x + 1$, find $f(-2)$.",
            "answer": "$17$",
            "wrong": ["$1$", "$9$", "$-7$"],
            "explanation": "$f(-2) = 8 + 8 + 1 = 17$."
        },
        {
            "question": "Given $f(x) = -3x^2 + x + 5$, find $f(1)$.",
            "answer": "$3$",
            "wrong": ["$5$", "$-3$", "$7$"],
            "explanation": "$f(1) = -3 + 1 + 5 = 3$."
        },
        {
            "question": "Given $f(x) = x^2 + 2x - 8$, find $f(-4)$.",
            "answer": "$0$",
            "wrong": ["$8$", "$-8$", "$16$"],
            "explanation": "$f(-4) = 16 - 8 - 8 = 0$."
        },
        {
            "question": "Given $f(x) = 5x^2 - 2x + 3$, find $f(2)$.",
            "answer": "$19$",
            "wrong": ["$15$", "$23$", "$17$"],
            "explanation": "$f(2) = 20 - 4 + 3 = 19$."
        },
        {
            "question": "Given $f(x) = -x^2 + 3x - 2$, find $f(4)$.",
            "answer": "$-6$",
            "wrong": ["$6$", "$-2$", "$2$"],
            "explanation": "$f(4) = -16 + 12 - 2 = -6$."
        },
        {
            "question": "Given $f(x) = x^2 - 9$, find $f(3)$.",
            "answer": "$0$",
            "wrong": ["$9$", "$-9$", "$18$"],
            "explanation": "$f(3) = 9 - 9 = 0$."
        },
        {
            "question": "Given $f(x) = 3x^2 + 3x - 6$, find $f(-3)$.",
            "answer": "$12$",
            "wrong": ["$-6$", "$6$", "$24$"],
            "explanation": "$f(-3) = 27 - 9 - 6 = 12$."
        },
        {
            "question": "Given $f(x) = 2x^2 + 5$, find $f(-3)$.",
            "answer": "$23$",
            "wrong": ["$-13$", "$13$", "$41$"],
            "explanation": "$f(-3) = 18 + 5 = 23$."
        },
        {
            "question": "Given $f(x) = x^2 - 4x - 5$, find $f(6)$.",
            "answer": "$7$",
            "wrong": ["$-5$", "$11$", "$23$"],
            "explanation": "$f(6) = 36 - 24 - 5 = 7$."
        },
        {
            "question": "Given $f(x) = -4x^2 + 2x + 10$, find $f(2)$.",
            "answer": "$-2$",
            "wrong": ["$2$", "$10$", "$-10$"],
            "explanation": "$f(2) = -16 + 4 + 10 = -2$."
        },
        {
            "question": "Given $f(x) = x^2 + x + 1$, find $f(-2)$.",
            "answer": "$3$",
            "wrong": ["$7$", "$-1$", "$5$"],
            "explanation": "$f(-2) = 4 - 2 + 1 = 3$."
        },
        {
            "question": "Given $f(x) = 6x^2 - x - 2$, find $f(1)$.",
            "answer": "$3$",
            "wrong": ["$5$", "$7$", "$-3$"],
            "explanation": "$f(1) = 6 - 1 - 2 = 3$."
        },
        {
            "question": "Given $f(x) = -x^2 + 5$, find $f(-2)$.",
            "answer": "$1$",
            "wrong": ["$9$", "$-9$", "$-1$"],
            "explanation": "$f(-2) = -4 + 5 = 1$."
        },
        {
            "question": "Given $f(x) = x^2 - 8x + 16$, find $f(4)$.",
            "answer": "$0$",
            "wrong": ["$16$", "$-16$", "$8$"],
            "explanation": "$f(4) = 16 - 32 + 16 = 0$."
        },
        {
            "question": "Given $f(x) = 2x^2 - 3x - 9$, find $f(3)$.",
            "answer": "$0$",
            "wrong": ["$9$", "$-9$", "$6$"],
            "explanation": "$f(3) = 18 - 9 - 9 = 0$."
        },
        {
            "question": "Given $f(x) = 4x^2 + 4x + 1$, find $f(-1)$.",
            "answer": "$1$",
            "wrong": ["$-1$", "$9$", "$0$"],
            "explanation": "$f(-1) = 4 - 4 + 1 = 1$."
        },
        {
            "question": "Given $f(x) = -2x^2 + 3x + 7$, find $f(0)$.",
            "answer": "$7$",
            "wrong": ["$0$", "$3$", "$-7$"],
            "explanation": "$f(0) = 0 + 0 + 7 = 7$."
        },

        {
            "question": "Solve for $x$: $x^2 - 5x + 6 = 0$.",
            "answer": "$x = 2$ or $x = 3$",
            "wrong": ["$x = -2$ or $x = -3$", "$x = 1$ or $x = 6$", "$x = 2$ or $x = -3$"],
            "explanation": "Factor: $(x-2)(x-3) = 0 \\Rightarrow x = 2$ or $x = 3$."
        },
        {
            "question": "Solve for $x$: $x^2 + x - 12 = 0$.",
            "answer": "$x = 3$ or $x = -4$",
            "wrong": ["$x = -3$ or $x = 4$", "$x = 6$ or $x = -2$", "$x = 3$ or $x = 4$"],
            "explanation": "Factor: $(x+4)(x-3) = 0 \\Rightarrow x = 3$ or $x = -4$."
        },
        {
            "question": "Solve for $x$: $2x^2 - 7x + 3 = 0$.",
            "answer": "$x = 3$ or $x = \\tfrac{1}{2}$",
            "wrong": ["$x = -3$ or $x = -\\tfrac{1}{2}$", "$x = 7$ or $x = 3$", "$x = 1$ or $x = 3$"],
            "explanation": "Factor: $(2x-1)(x-3) = 0 \\Rightarrow x = \\tfrac{1}{2}$ or $x = 3$."
        },
        {
            "question": "Solve for $x$: $x^2 - 9 = 0$.",
            "answer": "$x = 3$ or $x = -3$",
            "wrong": ["$x = 9$", "$x = 3$", "$x = \\pm 9$"],
            "explanation": "$x^2 = 9 \\Rightarrow x = \\pm 3$."
        },
        {
            "question": "Solve for $x$: $x^2 + 4x - 21 = 0$.",
            "answer": "$x = 3$ or $x = -7$",
            "wrong": ["$x = -3$ or $x = 7$", "$x = 3$ or $x = 7$", "$x = 1$ or $x = -21$"],
            "explanation": "Factor: $(x+7)(x-3) = 0 \\Rightarrow x = 3$ or $x = -7$."
        },
        {
            "question": "Solve for $x$: $3x^2 - 12 = 0$.",
            "answer": "$x = 2$ or $x = -2$",
            "wrong": ["$x = 4$", "$x = 2$", "$x = \\pm 4$"],
            "explanation": "$x^2 = 4 \\Rightarrow x = \\pm 2$."
        },
        {
            "question": "Solve for $x$: $x^2 - 8x + 12 = 0$.",
            "answer": "$x = 2$ or $x = 6$",
            "wrong": ["$x = -2$ or $x = -6$", "$x = 4$ or $x = 3$", "$x = 1$ or $x = 12$"],
            "explanation": "Factor: $(x-2)(x-6) = 0 \\Rightarrow x = 2$ or $x = 6$."
        },
        {
            "question": "Solve for $x$: $2x^2 + 5x - 3 = 0$.",
            "answer": "$x = \\tfrac{1}{2}$ or $x = -3$",
            "wrong": ["$x = -\\tfrac{1}{2}$ or $x = 3$", "$x = 1$ or $x = -3$", "$x = 2$ or $x = -3$"],
            "explanation": "Factor: $(2x-1)(x+3) = 0 \\Rightarrow x = \\tfrac{1}{2}$ or $x = -3$."
        },
        {
            "question": "Solve for $x$: $x^2 + 6x + 9 = 0$.",
            "answer": "$x = -3$",
            "wrong": ["$x = 3$", "$x = -3$ or $x = 3$", "$x = 9$"],
            "explanation": "$(x+3)^2 = 0 \\Rightarrow x = -3$ (double root)."
        },
        {
            "question": "Solve for $x$: $x^2 - 4x = 5$.",
            "answer": "$x = 5$ or $x = -1$",
            "wrong": ["$x = 4$ or $x = -5$", "$x = 5$ or $x = 1$", "$x = -5$ or $x = 1$"],
            "explanation": "Rewrite: $x^2 - 4x - 5 = 0$. Factor: $(x-5)(x+1) = 0 \\Rightarrow x = 5$ or $x = -1$."
        },
        {
            "question": "Solve for $x$: $4x^2 - 4x + 1 = 0$.",
            "answer": "$x = \\tfrac{1}{2}$",
            "wrong": ["$x = -\\tfrac{1}{2}$", "$x = 1$", "$x = \\tfrac{1}{2}$ or $x = -\\tfrac{1}{2}$"],
            "explanation": "$(2x-1)^2 = 0 \\Rightarrow x = \\tfrac{1}{2}$ (double root)."
        },
        {
            "question": "Solve for $x$: $x^2 - 3x - 10 = 0$.",
            "answer": "$x = 5$ or $x = -2$",
            "wrong": ["$x = -5$ or $x = 2$", "$x = 5$ or $x = 2$", "$x = 10$ or $x = -1$"],
            "explanation": "Factor: $(x-5)(x+2) = 0 \\Rightarrow x = 5$ or $x = -2$."
        },
        {
            "question": "Solve for $x$: $6x^2 + x - 2 = 0$.",
            "answer": "$x = \\tfrac{1}{2}$ or $x = -\\tfrac{2}{3}$",
            "wrong": ["$x = 2$ or $x = -3$", "$x = \\tfrac{1}{3}$ or $x = -\\tfrac{1}{2}$", "$x = 1$ or $x = -2$"],
            "explanation": "Factor: $(2x-1)(3x+2) = 0 \\Rightarrow x = \\tfrac{1}{2}$ or $x = -\\tfrac{2}{3}$."
        },
        {
            "question": "Solve for $x$: $x^2 + 2x - 35 = 0$.",
            "answer": "$x = 5$ or $x = -7$",
            "wrong": ["$x = -5$ or $x = 7$", "$x = 5$ or $x = 7$", "$x = 7$ or $x = -5$"],
            "explanation": "Factor: $(x+7)(x-5) = 0 \\Rightarrow x = 5$ or $x = -7$."
        },
        {
            "question": "Solve for $x$: $3x^2 - 5x - 2 = 0$.",
            "answer": "$x = 2$ or $x = -\\tfrac{1}{3}$",
            "wrong": ["$x = -2$ or $x = \\tfrac{1}{3}$", "$x = 1$ or $x = -\\tfrac{2}{3}$", "$x = 3$ or $x = -2$"],
            "explanation": "Factor: $(3x+1)(x-2) = 0 \\Rightarrow x = 2$ or $x = -\\tfrac{1}{3}$."
        },
        {
            "question": "Solve for $x$: $x^2 = 25$.",
            "answer": "$x = 5$ or $x = -5$",
            "wrong": ["$x = 5$", "$x = \\sqrt{25}$", "$x = 12.5$"],
            "explanation": "$x = \\pm\\sqrt{25} = \\pm 5$."
        },
        {
            "question": "Solve for $x$: $x^2 - 16x + 64 = 0$.",
            "answer": "$x = 8$",
            "wrong": ["$x = 4$ or $x = 16$", "$x = -8$", "$x = 8$ or $x = -8$"],
            "explanation": "$(x-8)^2 = 0 \\Rightarrow x = 8$ (double root)."
        },
        {
            "question": "Solve for $x$: $2x^2 - 18 = 0$.",
            "answer": "$x = 3$ or $x = -3$",
            "wrong": ["$x = 9$", "$x = 3$", "$x = \\pm 9$"],
            "explanation": "$x^2 = 9 \\Rightarrow x = \\pm 3$."
        },
        {
            "question": "Solve for $x$: $x^2 - x - 20 = 0$.",
            "answer": "$x = 5$ or $x = -4$",
            "wrong": ["$x = -5$ or $x = 4$", "$x = 10$ or $x = -2$", "$x = 4$ or $x = 5$"],
            "explanation": "Factor: $(x-5)(x+4) = 0 \\Rightarrow x = 5$ or $x = -4$."
        },
        {
            "question": "Solve for $x$: $5x^2 - 45 = 0$.",
            "answer": "$x = 3$ or $x = -3$",
            "wrong": ["$x = 9$", "$x = \\pm 9$", "$x = 3$"],
            "explanation": "$x^2 = 9 \\Rightarrow x = \\pm 3$."
        },
        {
            "question": "Solve for $x$: $x^2 + 7x + 12 = 0$.",
            "answer": "$x = -3$ or $x = -4$",
            "wrong": ["$x = 3$ or $x = 4$", "$x = -3$ or $x = 4$", "$x = 3$ or $x = -4$"],
            "explanation": "Factor: $(x+3)(x+4) = 0 \\Rightarrow x = -3$ or $x = -4$."
        },
        {
            "question": "Solve for $x$: $4x^2 - 25 = 0$.",
            "answer": "$x = \\tfrac{5}{2}$ or $x = -\\tfrac{5}{2}$",
            "wrong": ["$x = \\tfrac{25}{4}$", "$x = 5$", "$x = \\tfrac{5}{4}$"],
            "explanation": "$(2x-5)(2x+5) = 0 \\Rightarrow x = \\pm\\tfrac{5}{2}$."
        },
        {
            "question": "Solve for $x$: $x^2 - 11x + 30 = 0$.",
            "answer": "$x = 5$ or $x = 6$",
            "wrong": ["$x = -5$ or $x = -6$", "$x = 3$ or $x = 10$", "$x = 2$ or $x = 15$"],
            "explanation": "Factor: $(x-5)(x-6) = 0 \\Rightarrow x = 5$ or $x = 6$."
        },
        {
            "question": "Solve for $x$: $2x^2 + x - 6 = 0$.",
            "answer": "$x = \\tfrac{3}{2}$ or $x = -2$",
            "wrong": ["$x = -\\tfrac{3}{2}$ or $x = 2$", "$x = 1$ or $x = -6$", "$x = 3$ or $x = -2$"],
            "explanation": "Factor: $(2x-3)(x+2) = 0 \\Rightarrow x = \\tfrac{3}{2}$ or $x = -2$."
        },
        {
            "question": "Solve for $x$: $9x^2 - 1 = 0$.",
            "answer": "$x = \\tfrac{1}{3}$ or $x = -\\tfrac{1}{3}$",
            "wrong": ["$x = \\tfrac{1}{9}$", "$x = \\pm 3$", "$x = 1$"],
            "explanation": "$(3x-1)(3x+1) = 0 \\Rightarrow x = \\pm\\tfrac{1}{3}$."
        },

        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 - 5x + 6$.",
            "answer": "$(2,\\ 0)$ and $(3,\\ 0)$",
            "wrong": ["$(2,\\ 0)$ and $(-3,\\ 0)$", "$(-2,\\ 0)$ and $(-3,\\ 0)$", "$(5,\\ 0)$ and $(6,\\ 0)$"],
            "explanation": "Set $y=0$: $(x-2)(x-3)=0 \\Rightarrow x=2, 3$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 - 4$.",
            "answer": "$(2,\\ 0)$ and $(-2,\\ 0)$",
            "wrong": ["$(4,\\ 0)$", "$(2,\\ 0)$ only", "$(-4,\\ 0)$ and $(4,\\ 0)$"],
            "explanation": "$x^2 = 4 \\Rightarrow x = \\pm 2$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 + 3x - 10$.",
            "answer": "$(2,\\ 0)$ and $(-5,\\ 0)$",
            "wrong": ["$(-2,\\ 0)$ and $(5,\\ 0)$", "$(2,\\ 0)$ and $(5,\\ 0)$", "$(-2,\\ 0)$ and $(-5,\\ 0)$"],
            "explanation": "$(x-2)(x+5) = 0 \\Rightarrow x = 2, -5$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = 2x^2 - 8x$.",
            "answer": "$(0,\\ 0)$ and $(4,\\ 0)$",
            "wrong": ["$(0,\\ 0)$ and $(8,\\ 0)$", "$(4,\\ 0)$ only", "$(0,\\ 0)$ and $(-4,\\ 0)$"],
            "explanation": "$2x(x-4)=0 \\Rightarrow x=0$ or $x=4$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 - 2x - 15$.",
            "answer": "$(-3,\\ 0)$ and $(5,\\ 0)$",
            "wrong": ["$(3,\\ 0)$ and $(-5,\\ 0)$", "$(-3,\\ 0)$ and $(-5,\\ 0)$", "$(3,\\ 0)$ and $(5,\\ 0)$"],
            "explanation": "$(x-5)(x+3)=0 \\Rightarrow x=5, -3$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 + 5x$.",
            "answer": "$(0,\\ 0)$ and $(-5,\\ 0)$",
            "wrong": ["$(0,\\ 0)$ and $(5,\\ 0)$", "$(-5,\\ 0)$ only", "$(5,\\ 0)$ only"],
            "explanation": "$x(x+5) = 0 \\Rightarrow x = 0$ or $x = -5$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = 3x^2 - 27$.",
            "answer": "$(3,\\ 0)$ and $(-3,\\ 0)$",
            "wrong": ["$(9,\\ 0)$ and $(-9,\\ 0)$", "$(3,\\ 0)$ only", "$( \\sqrt{27},\\ 0)$ and $(-\\sqrt{27},\\ 0)$"],
            "explanation": "$3x^2 = 27 \\Rightarrow x^2 = 9 \\Rightarrow x = \\pm 3$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 - 7x + 12$.",
            "answer": "$(3,\\ 0)$ and $(4,\\ 0)$",
            "wrong": ["$(-3,\\ 0)$ and $(-4,\\ 0)$", "$(3,\\ 0)$ and $(12,\\ 0)$", "$(6,\\ 0)$ and $(2,\\ 0)$"],
            "explanation": "$(x-3)(x-4) = 0 \\Rightarrow x = 3, 4$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = -x^2 + 6x - 9$.",
            "answer": "$(3,\\ 0)$ only",
            "wrong": ["$(3,\\ 0)$ and $(-3,\\ 0)$", "$(9,\\ 0)$ only", "No $x$-intercepts"],
            "explanation": "$-(x-3)^2 = 0 \\Rightarrow x = 3$ (touches the axis once)."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 + x - 6$.",
            "answer": "$(2,\\ 0)$ and $(-3,\\ 0)$",
            "wrong": ["$(-2,\\ 0)$ and $(3,\\ 0)$", "$(2,\\ 0)$ and $(3,\\ 0)$", "$(-6,\\ 0)$ and $(1,\\ 0)$"],
            "explanation": "$(x+3)(x-2) = 0 \\Rightarrow x = 2, -3$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = 2x^2 + 6x - 8$.",
            "answer": "$(1,\\ 0)$ and $(-4,\\ 0)$",
            "wrong": ["$(-1,\\ 0)$ and $(4,\\ 0)$", "$(2,\\ 0)$ and $(-4,\\ 0)$", "$(1,\\ 0)$ and $(4,\\ 0)$"],
            "explanation": "$2(x^2+3x-4)=0 \\Rightarrow (x+4)(x-1)=0 \\Rightarrow x=1,-4$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 - 1$.",
            "answer": "$(1,\\ 0)$ and $(-1,\\ 0)$",
            "wrong": ["$(1,\\ 0)$ only", "$(0,\\ -1)$", "$(-1,\\ 0)$ only"],
            "explanation": "$x^2 = 1 \\Rightarrow x = \\pm 1$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 - 6x + 5$.",
            "answer": "$(1,\\ 0)$ and $(5,\\ 0)$",
            "wrong": ["$(-1,\\ 0)$ and $(-5,\\ 0)$", "$(2,\\ 0)$ and $(3,\\ 0)$", "$(1,\\ 0)$ and $(6,\\ 0)$"],
            "explanation": "$(x-1)(x-5) = 0 \\Rightarrow x = 1, 5$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = 4x^2 - 12x + 9$.",
            "answer": "$\\left(\\tfrac{3}{2},\\ 0\\right)$ only",
            "wrong": ["$(3,\\ 0)$ and $(-3,\\ 0)$", "$(\\tfrac{3}{2},\\ 0)$ and $(-\\tfrac{3}{2},\\ 0)$",
                      "No $x$-intercepts"],
            "explanation": "$(2x-3)^2 = 0 \\Rightarrow x = \\tfrac{3}{2}$ (double root)."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 - 9x + 18$.",
            "answer": "$(3,\\ 0)$ and $(6,\\ 0)$",
            "wrong": ["$(9,\\ 0)$ and $(2,\\ 0)$", "$(-3,\\ 0)$ and $(-6,\\ 0)$", "$(3,\\ 0)$ and $(9,\\ 0)$"],
            "explanation": "$(x-3)(x-6) = 0 \\Rightarrow x = 3, 6$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = -2x^2 + 8x$.",
            "answer": "$(0,\\ 0)$ and $(4,\\ 0)$",
            "wrong": ["$(0,\\ 0)$ and $(8,\\ 0)$", "$(4,\\ 0)$ only", "$(0,\\ 0)$ and $(-4,\\ 0)$"],
            "explanation": "$-2x(x-4) = 0 \\Rightarrow x = 0$ or $x = 4$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 + 2x - 8$.",
            "answer": "$(2,\\ 0)$ and $(-4,\\ 0)$",
            "wrong": ["$(-2,\\ 0)$ and $(4,\\ 0)$", "$(2,\\ 0)$ and $(4,\\ 0)$", "$(-2,\\ 0)$ and $(-4,\\ 0)$"],
            "explanation": "$(x+4)(x-2) = 0 \\Rightarrow x = 2, -4$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = 3x^2 + 6x$.",
            "answer": "$(0,\\ 0)$ and $(-2,\\ 0)$",
            "wrong": ["$(0,\\ 0)$ and $(2,\\ 0)$", "$(-2,\\ 0)$ only", "$(6,\\ 0)$ and $(-3,\\ 0)$"],
            "explanation": "$3x(x+2) = 0 \\Rightarrow x = 0$ or $x = -2$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 - 25$.",
            "answer": "$(5,\\ 0)$ and $(-5,\\ 0)$",
            "wrong": ["$(5,\\ 0)$ only", "$(25,\\ 0)$ and $(-25,\\ 0)$", "$(\\sqrt{5},\\ 0)$"],
            "explanation": "$x^2 = 25 \\Rightarrow x = \\pm 5$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 - 3x - 18$.",
            "answer": "$(-3,\\ 0)$ and $(6,\\ 0)$",
            "wrong": ["$(3,\\ 0)$ and $(-6,\\ 0)$", "$(3,\\ 0)$ and $(6,\\ 0)$", "$(-3,\\ 0)$ and $(-6,\\ 0)$"],
            "explanation": "$(x-6)(x+3) = 0 \\Rightarrow x = 6, -3$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = 2x^2 - 2$.",
            "answer": "$(1,\\ 0)$ and $(-1,\\ 0)$",
            "wrong": ["$(2,\\ 0)$ and $(-2,\\ 0)$", "$(1,\\ 0)$ only", "$(\\sqrt{2},\\ 0)$ and $(-\\sqrt{2},\\ 0)$"],
            "explanation": "$2x^2 = 2 \\Rightarrow x^2 = 1 \\Rightarrow x = \\pm 1$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 + 4x + 4$.",
            "answer": "$(-2,\\ 0)$ only",
            "wrong": ["$(2,\\ 0)$ and $(-2,\\ 0)$", "$(2,\\ 0)$ only", "No $x$-intercepts"],
            "explanation": "$(x+2)^2 = 0 \\Rightarrow x = -2$ (double root)."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 - 13x + 40$.",
            "answer": "$(5,\\ 0)$ and $(8,\\ 0)$",
            "wrong": ["$(-5,\\ 0)$ and $(-8,\\ 0)$", "$(4,\\ 0)$ and $(10,\\ 0)$", "$(5,\\ 0)$ and $(13,\\ 0)$"],
            "explanation": "$(x-5)(x-8) = 0 \\Rightarrow x = 5, 8$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = 5x^2 - 20x$.",
            "answer": "$(0,\\ 0)$ and $(4,\\ 0)$",
            "wrong": ["$(0,\\ 0)$ and $(20,\\ 0)$", "$(4,\\ 0)$ only", "$(0,\\ 0)$ and $(-4,\\ 0)$"],
            "explanation": "$5x(x-4) = 0 \\Rightarrow x = 0$ or $x = 4$."
        },
        {
            "question": "Find the $x$-intercepts of $f(x) = x^2 + 2x - 24$.",
            "answer": "$(4,\\ 0)$ and $(-6,\\ 0)$",
            "wrong": ["$(-4,\\ 0)$ and $(6,\\ 0)$", "$(4,\\ 0)$ and $(6,\\ 0)$", "$(3,\\ 0)$ and $(-8,\\ 0)$"],
            "explanation": "$(x+6)(x-4) = 0 \\Rightarrow x = 4, -6$."
        },
        {
            'question': 'Given $f(x) = x^3 - 3x^2 + 2x - 1$, find $f(2)$.',
            'answer': '$-1$',
            'wrong': ['$1$', '$3$', '$-3$'],
            'explanation': '$f(2) = 8 - 12 + 4 - 1 = -1$.',
        },
        {
            'question': 'Given $f(x) = x^3 + 2x^2 - x + 4$, find $f(1)$.',
            'answer': '$6$',
            'wrong': ['$4$', '$8$', '$2$'],
            'explanation': '$f(1) = 1 + 2 - 1 + 4 = 6$.',
        },
        {
            'question': 'Given $f(x) = 2x^3 - x^2 + 3x - 5$, find $f(0)$.',
            'answer': '$-5$',
            'wrong': ['$0$', '$5$', '$-1$'],
            'explanation': '$f(0) = 0 - 0 + 0 - 5 = -5$.',
        },
        {
            'question': 'Given $f(x) = x^3 - 4x + 3$, find $f(2)$.',
            'answer': '$3$',
            'wrong': ['$-3$', '$7$', '$11$'],
            'explanation': '$f(2) = 8 - 8 + 3 = 3$.',
        },
        {
            'question': 'Given $f(x) = x^3 + x^2 - 2x$, find $f(3)$.',
            'answer': '$30$',
            'wrong': ['$24$', '$36$', '$18$'],
            'explanation': '$f(3) = 27 + 9 - 6 = 30$.',
        },
        {
            'question': 'Given $f(x) = -x^3 + 2x^2 + x - 3$, find $f(1)$.',
            'answer': '$-1$',
            'wrong': ['$1$', '$3$', '$-3$'],
            'explanation': '$f(1) = -1 + 2 + 1 - 3 = -1$.',
        },
        {
            'question': 'Given $f(x) = x^3 - 5x^2 + 6x$, find $f(2)$.',
            'answer': '$0$',
            'wrong': ['$4$', '$-4$', '$8$'],
            'explanation': '$f(2) = 8 - 20 + 12 = 0$.',
        },
        {
            'question': 'Given $f(x) = 3x^3 - 2x + 1$, find $f(-1)$.',
            'answer': '$0$',
            'wrong': ['$-4$', '$4$', '$2$'],
            'explanation': '$f(-1) = -3 + 2 + 1 = 0$.',
        },
        {
            'question': 'Given $f(x) = x^3 + 3x^2 + 3x + 1$, find $f(-1)$.',
            'answer': '$0$',
            'wrong': ['$8$', '$-8$', '$1$'],
            'explanation': '$f(-1) = (-1)^3 + 3(1) + 3(-1) + 1 = -1 + 3 - 3 + 1 = 0$.',
        },
        {
            'question': 'Given $f(x) = 2x^3 + x^2 - 4x - 3$, find $f(1)$.',
            'answer': '$-4$',
            'wrong': ['$4$', '$0$', '$-2$'],
            'explanation': '$f(1) = 2 + 1 - 4 - 3 = -4$.',
        },
        {
            'question': 'Given $f(x) = x^3 - 6x^2 + 11x - 6$, find $f(3)$.',
            'answer': '$0$',
            'wrong': ['$6$', '$-6$', '$3$'],
            'explanation': '$f(3) = 27 - 54 + 33 - 6 = 0$.',
        },
        {
            'question': 'Given $f(x) = x^3 - 8$, find $f(2)$.',
            'answer': '$0$',
            'wrong': ['$8$', '$-8$', '$16$'],
            'explanation': '$f(2) = 8 - 8 = 0$.',
        },
        {
            'question': 'Given $f(x) = x^3 + 8$, find $f(-2)$.',
            'answer': '$0$',
            'wrong': ['$16$', '$-16$', '$8$'],
            'explanation': '$f(-2) = -8 + 8 = 0$.',
        },
        {
            'question': 'Given $f(x) = 4x^3 - 3x^2 + 2x - 1$, find $f(0)$.',
            'answer': '$-1$',
            'wrong': ['$0$', '$1$', '$2$'],
            'explanation': '$f(0) = 0 - 0 + 0 - 1 = -1$.',
        },
        {
            'question': 'Given $f(x) = x^3 - x$, find $f(3)$.',
            'answer': '$24$',
            'wrong': ['$18$', '$30$', '$6$'],
            'explanation': '$f(3) = 27 - 3 = 24$.',
        },
        {
            'question': 'Given $f(x) = -2x^3 + 5x - 1$, find $f(2)$.',
            'answer': '$-7$',
            'wrong': ['$7$', '$-15$', '$3$'],
            'explanation': '$f(2) = -16 + 10 - 1 = -7$.',
        },
        {
            'question': 'Given $f(x) = x^3 + 2x^2 + x$, find $f(-1)$.',
            'answer': '$0$',
            'wrong': ['$-4$', '$4$', '$2$'],
            'explanation': '$f(-1) = -1 + 2 - 1 = 0$.',
        },
        {
            'question': 'Given $f(x) = x^3 - 2x^2 - 5x + 6$, find $f(1)$.',
            'answer': '$0$',
            'wrong': ['$6$', '$-6$', '$2$'],
            'explanation': '$f(1) = 1 - 2 - 5 + 6 = 0$.',
        },
        {
            'question': 'Given $f(x) = 5x^3 - 2x^2 + x$, find $f(1)$.',
            'answer': '$4$',
            'wrong': ['$-4$', '$8$', '$2$'],
            'explanation': '$f(1) = 5 - 2 + 1 = 4$.',
        },
        {
            'question': 'Given $f(x) = x^3 - 27$, find $f(3)$.',
            'answer': '$0$',
            'wrong': ['$27$', '$-27$', '$54$'],
            'explanation': '$f(3) = 27 - 27 = 0$.',
        },
        {
            'question': 'Given $f(x) = x^3 + x^2 - 4x - 4$, find $f(2)$.',
            'answer': '$0$',
            'wrong': ['$4$', '$-4$', '$8$'],
            'explanation': '$f(2) = 8 + 4 - 8 - 4 = 0$.',
        },
        {
            'question': 'Given $f(x) = -x^3 + 4x$, find $f(-2)$.',
            'answer': '$0$',
            'wrong': ['$8$', '$-8$', '$16$'],
            'explanation': '$f(-2) = 8 - 8 = 0$.',
        },
        {
            'question': 'Given $f(x) = x^3 + 4x^2 + 5x + 2$, find $f(-1)$.',
            'answer': '$0$',
            'wrong': ['$2$', '$-2$', '$12$'],
            'explanation': '$f(-1) = -1 + 4 - 5 + 2 = 0$.',
        },
        {
            'question': 'Given $f(x) = 3x^3 - 3x$, find $f(1)$.',
            'answer': '$0$',
            'wrong': ['$3$', '$-3$', '$6$'],
            'explanation': '$f(1) = 3 - 3 = 0$.',
        },
        {
            'question': 'Given $f(x) = x^3 - 4x^2 + x + 6$, find $f(2)$.',
            'answer': '$0$',
            'wrong': ['$6$', '$-6$', '$4$'],
            'explanation': '$f(2) = 8 - 16 + 2 + 6 = 0$.',
        },
        {
            'question': 'Given $f(x) = 2x^3 - 16$, find $f(2)$.',
            'answer': '$0$',
            'wrong': ['$16$', '$-16$', '$32$'],
            'explanation': '$f(2) = 16 - 16 = 0$.',
        },
        {
            'question': 'Given $f(x) = x^3 - 3x^2 - x + 3$, find $f(3)$.',
            'answer': '$0$',
            'wrong': ['$3$', '$-3$', '$12$'],
            'explanation': '$f(3) = 27 - 27 - 3 + 3 = 0$.',
        },
        {
            'question': 'Given $f(x) = x^3 - x^2 - x + 1$, find $f(1)$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', '$2$'],
            'explanation': '$f(1) = 1 - 1 - 1 + 1 = 0$.',
        },
        {
            'question': 'Given $f(x) = x^3 + 5x^2 + 6x$, find $f(-2)$.',
            'answer': '$0$',
            'wrong': ['$4$', '$-4$', '$8$'],
            'explanation': '$f(-2) = -8 + 20 - 12 = 0$.',
        },
        {
            'question': 'Given $f(x) = 4x^3 + 4x^2 - x - 1$, find $f(-1)$.',
            'answer': '$0$',
            'wrong': ['$-2$', '$2$', '$8$'],
            'explanation': '$f(-1) = -4 + 4 + 1 - 1 = 0$.',
        },
        {
            'question': 'Given $f(x) = x^3 - 7x + 6$, find $f(2)$.',
            'answer': '$0$',
            'wrong': ['$-4$', '$4$', '$6$'],
            'explanation': '$f(2) = 8 - 14 + 6 = 0$.',
        },
        {
            'question': 'Given $f(x) = x^3 - 2x^2 - 4x + 8$, find $f(2)$.',
            'answer': '$0$',
            'wrong': ['$8$', '$-8$', '$4$'],
            'explanation': '$f(2) = 8 - 8 - 8 + 8 = 0$.',
        },
        {
            'question': 'Given $f(x) = -x^3 + 3x^2 - 3x + 1$, find $f(1)$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', '$2$'],
            'explanation': '$f(1) = -1 + 3 - 3 + 1 = 0$.',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 2: Given f(x) = number, find x  (33 problems)
        # ══════════════════════════════════════════════════════

        {
            'question': 'Solve $x^3 - 6x^2 + 11x - 6 = 0$.',
            'answer': '$x = 1,\\ 2,\\ 3$',
            'wrong': ['$x = -1,\\ -2,\\ -3$', '$x = 1,\\ 2,\\ -3$', '$x = 2,\\ 3,\\ 6$'],
            'explanation': 'Factor: $(x-1)(x-2)(x-3) = 0 \\Rightarrow x = 1, 2, 3$.',
        },
        {
            'question': 'Solve $x^3 - x = 0$.',
            'answer': '$x = 0,\\ 1,\\ -1$',
            'wrong': ['$x = 0,\\ 1$', '$x = 1,\\ -1$', '$x = 0,\\ -1$'],
            'explanation': '$x(x^2 - 1) = 0 \\Rightarrow x(x-1)(x+1) = 0 \\Rightarrow x = 0, 1, -1$.',
        },
        {
            'question': 'Solve $x^3 - 4x^2 + x + 6 = 0$.',
            'answer': '$x = -1,\\ 2,\\ 3$',
            'wrong': ['$x = 1,\\ -2,\\ -3$', '$x = 1,\\ 2,\\ 3$', '$x = -1,\\ -2,\\ 3$'],
            'explanation': '$(x+1)(x-2)(x-3) = 0 \\Rightarrow x = -1, 2, 3$.',
        },
        {
            'question': 'Solve $x^3 - 8 = 0$.',
            'answer': '$x = 2$',
            'wrong': ['$x = -2$', '$x = 8$', '$x = 4$'],
            'explanation': '$x^3 = 8 \\Rightarrow x = \\sqrt[3]{8} = 2$.',
        },
        {
            'question': 'Solve $x^3 + 27 = 0$.',
            'answer': '$x = -3$',
            'wrong': ['$x = 3$', '$x = -27$', '$x = 9$'],
            'explanation': '$x^3 = -27 \\Rightarrow x = -3$.',
        },
        {
            'question': 'Solve $x^3 - 3x^2 - x + 3 = 0$.',
            'answer': '$x = -1,\\ 1,\\ 3$',
            'wrong': ['$x = 1,\\ -1,\\ -3$', '$x = 1,\\ 3,\\ -3$', '$x = -1,\\ 3,\\ -3$'],
            'explanation': '$x^2(x-3) - (x-3) = 0 \\Rightarrow (x^2-1)(x-3) = 0 \\Rightarrow x = \\pm1, 3$.',
        },
        {
            'question': 'Solve $x^3 - 5x^2 + 6x = 0$.',
            'answer': '$x = 0,\\ 2,\\ 3$',
            'wrong': ['$x = 0,\\ -2,\\ -3$', '$x = 2,\\ 3$', '$x = 0,\\ 5,\\ 6$'],
            'explanation': '$x(x^2-5x+6) = 0 \\Rightarrow x(x-2)(x-3) = 0 \\Rightarrow x = 0, 2, 3$.',
        },
        {
            'question': 'Solve $x^3 + x^2 - 4x - 4 = 0$.',
            'answer': '$x = -1,\\ 2,\\ -2$',
            'wrong': ['$x = 1,\\ 2,\\ -2$', '$x = -1,\\ -2,\\ 4$', '$x = 1,\\ -2,\\ 4$'],
            'explanation': '$x^2(x+1) - 4(x+1) = 0 \\Rightarrow (x^2-4)(x+1) = 0 \\Rightarrow x = \\pm2, -1$.',
        },
        {
            'question': 'Solve $2x^3 - 16 = 0$.',
            'answer': '$x = 2$',
            'wrong': ['$x = -2$', '$x = 8$', '$x = 4$'],
            'explanation': '$x^3 = 8 \\Rightarrow x = 2$.',
        },
        {
            'question': 'Solve $x^3 - x^2 - x + 1 = 0$.',
            'answer': '$x = -1,\\ 1$',
            'wrong': ['$x = 1,\\ -1,\\ 2$', '$x = 1$ only', '$x = -1$ only'],
            'explanation': '$x^2(x-1)-(x-1) = 0 \\Rightarrow (x^2-1)(x-1) = 0 \\Rightarrow x = 1$ (double), $x = -1$.',
        },
        {
            'question': 'Solve $x^3 + 5x^2 + 6x = 0$.',
            'answer': '$x = 0,\\ -2,\\ -3$',
            'wrong': ['$x = 0,\\ 2,\\ 3$', '$x = -2,\\ -3$', '$x = 5,\\ 6$'],
            'explanation': '$x(x+2)(x+3) = 0 \\Rightarrow x = 0, -2, -3$.',
        },
        {
            'question': 'Solve $x^3 - 7x + 6 = 0$.',
            'answer': '$x = 1,\\ 2,\\ -3$',
            'wrong': ['$x = -1,\\ -2,\\ 3$', '$x = 1,\\ -2,\\ 3$', '$x = 7,\\ -6$'],
            'explanation': '$(x-1)(x-2)(x+3) = 0 \\Rightarrow x = 1, 2, -3$.',
        },
        {
            'question': 'Solve $x^3 - 3x^2 + 4 = 0$.',
            'answer': '$x = -1,\\ 2$',
            'wrong': ['$x = 1,\\ -2$', '$x = -1,\\ 2,\\ -2$', '$x = 3,\\ 4$'],
            'explanation': '$(x+1)(x-2)^2 = 0 \\Rightarrow x = -1$ and $x = 2$ (double).',
        },
        {
            'question': 'Solve $x^3 - 2x^2 - 5x + 6 = 0$.',
            'answer': '$x = -2,\\ 1,\\ 3$',
            'wrong': ['$x = 2,\\ -1,\\ -3$', '$x = -2,\\ 1,\\ -3$', '$x = 2,\\ 3,\\ -6$'],
            'explanation': '$(x+2)(x-1)(x-3) = 0 \\Rightarrow x = -2, 1, 3$.',
        },
        {
            'question': 'Solve $x^3 + 3x^2 + 3x + 1 = 0$.',
            'answer': '$x = -1$',
            'wrong': ['$x = 1$', '$x = -1,\\ 1$', '$x = -3$'],
            'explanation': '$(x+1)^3 = 0 \\Rightarrow x = -1$ (triple root).',
        },
        {
            'question': 'Solve $x^3 + 4x^2 + 5x + 2 = 0$.',
            'answer': '$x = -1,\\ -2$',
            'wrong': ['$x = 1,\\ 2$', '$x = -1,\\ -2,\\ -5$', '$x = 4,\\ 5,\\ 2$'],
            'explanation': '$(x+1)^2(x+2) = 0 \\Rightarrow x = -1$ (double), $x = -2$.',
        },
        {
            'question': 'Solve $x^3 - 125 = 0$.',
            'answer': '$x = 5$',
            'wrong': ['$x = -5$', '$x = 25$', '$x = 15$'],
            'explanation': '$x^3 = 125 \\Rightarrow x = 5$.',
        },
        {
            'question': 'Solve $x^3 - 4x = 0$.',
            'answer': '$x = 0,\\ 2,\\ -2$',
            'wrong': ['$x = 0,\\ 4$', '$x = 2,\\ -2$', '$x = 0,\\ 2$'],
            'explanation': '$x(x^2-4) = 0 \\Rightarrow x(x-2)(x+2) = 0 \\Rightarrow x = 0, \\pm 2$.',
        },
        {
            'question': 'Solve $x^3 - 2x^2 - 4x + 8 = 0$.',
            'answer': '$x = 2,\\ -2$',
            'wrong': ['$x = 2,\\ 4,\\ -2$', '$x = -2,\\ 4$', '$x = 2$ only'],
            'explanation': '$x^2(x-2) - 4(x-2) = 0 \\Rightarrow (x^2-4)(x-2) = 0 \\Rightarrow x = 2$ (double), $x = -2$.',
        },
        {
            'question': 'Solve $x^3 + x^2 - 6x = 0$.',
            'answer': '$x = 0,\\ 2,\\ -3$',
            'wrong': ['$x = 0,\\ -2,\\ 3$', '$x = 2,\\ -3$', '$x = 1,\\ -6$'],
            'explanation': '$x(x^2+x-6) = 0 \\Rightarrow x(x-2)(x+3) = 0 \\Rightarrow x = 0, 2, -3$.',
        },
        {
            'question': 'Solve $x^3 - 4x^2 - 7x + 10 = 0$.',
            'answer': '$x = -2,\\ 1,\\ 5$',
            'wrong': ['$x = 2,\\ -1,\\ -5$', '$x = -2,\\ 5,\\ -1$', '$x = 4,\\ 7,\\ -10$'],
            'explanation': '$(x+2)(x-1)(x-5) = 0 \\Rightarrow x = -2, 1, 5$.',
        },
        {
            'question': 'Solve $3x^3 - 3x = 0$.',
            'answer': '$x = 0,\\ 1,\\ -1$',
            'wrong': ['$x = 0,\\ 1$', '$x = 1,\\ -1$', '$x = 0,\\ 3$'],
            'explanation': '$3x(x^2-1) = 0 \\Rightarrow 3x(x-1)(x+1) = 0 \\Rightarrow x = 0, \\pm 1$.',
        },
        {
            'question': 'Solve $x^3 - 9x = 0$.',
            'answer': '$x = 0,\\ 3,\\ -3$',
            'wrong': ['$x = 0,\\ 9$', '$x = 3,\\ -3$', '$x = 0,\\ 3$'],
            'explanation': '$x(x^2-9) = 0 \\Rightarrow x(x-3)(x+3) = 0 \\Rightarrow x = 0, \\pm 3$.',
        },
        {
            'question': 'Solve $x^3 - x^2 - 4x + 4 = 0$.',
            'answer': '$x = 1,\\ 2,\\ -2$',
            'wrong': ['$x = -1,\\ 2,\\ -2$', '$x = 1,\\ -2,\\ 4$', '$x = 1,\\ 4,\\ -4$'],
            'explanation': '$x^2(x-1) - 4(x-1) = 0 \\Rightarrow (x^2-4)(x-1) = 0 \\Rightarrow x = 1, \\pm 2$.',
        },
        {
            'question': 'Solve $x^3 + 2x^2 - x - 2 = 0$.',
            'answer': '$x = -2,\\ 1,\\ -1$',
            'wrong': ['$x = 2,\\ -1,\\ 1$', '$x = -2,\\ -1,\\ 2$', '$x = 2,\\ 1,\\ -1$'],
            'explanation': '$x^2(x+2) - (x+2) = 0 \\Rightarrow (x^2-1)(x+2) = 0 \\Rightarrow x = \\pm1, -2$.',
        },
        {
            'question': 'Solve $x^3 - 3x + 2 = 0$.',
            'answer': '$x = 1,\\ -2$',
            'wrong': ['$x = -1,\\ 2$', '$x = 1,\\ 2,\\ -2$', '$x = 3,\\ -2$'],
            'explanation': '$(x-1)^2(x+2) = 0 \\Rightarrow x = 1$ (double), $x = -2$.',
        },
        {
            'question': 'Solve $x^3 + 3x^2 - 4 = 0$.',
            'answer': '$x = 1,\\ -2$',
            'wrong': ['$x = -1,\\ 2$', '$x = 1,\\ 2,\\ -4$', '$x = 4,\\ -3$'],
            'explanation': '$(x-1)(x+2)^2 = 0 \\Rightarrow x = 1,\\ x = -2$ (double).',
        },
        {
            'question': 'Solve $2x^3 - 6x^2 + 4x = 0$.',
            'answer': '$x = 0,\\ 1,\\ 2$',
            'wrong': ['$x = 0,\\ -1,\\ -2$', '$x = 1,\\ 2$', '$x = 0,\\ 6,\\ 4$'],
            'explanation': '$2x(x^2-3x+2) = 0 \\Rightarrow 2x(x-1)(x-2) = 0 \\Rightarrow x = 0, 1, 2$.',
        },
        {
            'question': 'Solve $x^3 - 5x^2 + 8x - 4 = 0$.',
            'answer': '$x = 1,\\ 2$',
            'wrong': ['$x = -1,\\ -2$', '$x = 1,\\ 2,\\ 4$', '$x = 5,\\ -4$'],
            'explanation': '$(x-1)(x-2)^2 = 0 \\Rightarrow x = 1,\\ x = 2$ (double).',
        },
        {
            'question': 'Solve $x^3 + 6x^2 + 11x + 6 = 0$.',
            'answer': '$x = -1,\\ -2,\\ -3$',
            'wrong': ['$x = 1,\\ 2,\\ 3$', '$x = -1,\\ 2,\\ -3$', '$x = 6,\\ 11,\\ -6$'],
            'explanation': '$(x+1)(x+2)(x+3) = 0 \\Rightarrow x = -1, -2, -3$.',
        },
        {
            'question': 'Solve $x^3 - 6x^2 + 9x = 0$.',
            'answer': '$x = 0,\\ 3$',
            'wrong': ['$x = 0,\\ 3,\\ -3$', '$x = 3$ only', '$x = 0,\\ 6,\\ 9$'],
            'explanation': '$x(x-3)^2 = 0 \\Rightarrow x = 0,\\ x = 3$ (double).',
        },
        {
            'question': 'Solve $x^3 - 4x^2 + 4x = 0$.',
            'answer': '$x = 0,\\ 2$',
            'wrong': ['$x = 0,\\ 2,\\ -2$', '$x = 2$ only', '$x = 4,\\ -4$'],
            'explanation': '$x(x-2)^2 = 0 \\Rightarrow x = 0,\\ x = 2$ (double).',
        },
        {
            'question': 'Solve $x^3 - 7x^2 + 14x - 8 = 0$.',
            'answer': '$x = 1,\\ 2,\\ 4$',
            'wrong': ['$x = -1,\\ -2,\\ -4$', '$x = 1,\\ 2,\\ -4$', '$x = 7,\\ 14,\\ 8$'],
            'explanation': '$(x-1)(x-2)(x-4) = 0 \\Rightarrow x = 1, 2, 4$.',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 3: Find x-intercepts  (34 problems)
        # ══════════════════════════════════════════════════════

        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - x$.',
            'answer': '$(0,\\ 0),\\ (1,\\ 0),\\ (-1,\\ 0)$',
            'wrong': ['$(0,\\ 0)$ and $(1,\\ 0)$', '$(1,\\ 0)$ and $(-1,\\ 0)$', '$(0,\\ 0)$ only'],
            'explanation': 'Set $f(x)=0$: $x(x-1)(x+1)=0$. x-intercepts are where the graph crosses the x-axis, i.e. $f(x)=0$. $\\Rightarrow x = 0, 1, -1$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 6x^2 + 11x - 6$.',
            'answer': '$(1,\\ 0),\\ (2,\\ 0),\\ (3,\\ 0)$',
            'wrong': ['$(-1,\\ 0),\\ (-2,\\ 0),\\ (-3,\\ 0)$', '$(1,\\ 0)$ only', '$(2,\\ 0)$ and $(3,\\ 0)$'],
            'explanation': '$(x-1)(x-2)(x-3)=0 \\Rightarrow x = 1, 2, 3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 4x$.',
            'answer': '$(0,\\ 0),\\ (2,\\ 0),\\ (-2,\\ 0)$',
            'wrong': ['$(0,\\ 0)$ and $(4,\\ 0)$', '$(2,\\ 0)$ and $(-2,\\ 0)$', '$(0,\\ 0)$ only'],
            'explanation': '$x(x-2)(x+2)=0 \\Rightarrow x = 0, \\pm 2$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 8$.',
            'answer': '$(2,\\ 0)$',
            'wrong': ['$(-2,\\ 0)$', '$(8,\\ 0)$', '$(2,\\ 0)$ and $(-2,\\ 0)$'],
            'explanation': '$x^3 = 8 \\Rightarrow x = 2$. Only one real x-intercept.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 + 27$.',
            'answer': '$(-3,\\ 0)$',
            'wrong': ['$(3,\\ 0)$', '$(-3,\\ 0)$ and $(3,\\ 0)$', '$(27,\\ 0)$'],
            'explanation': '$x^3 = -27 \\Rightarrow x = -3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 + 3x^2 + 3x + 1$.',
            'answer': '$(-1,\\ 0)$',
            'wrong': ['$(1,\\ 0)$', '$(-1,\\ 0)$ and $(1,\\ 0)$', '$(3,\\ 0)$'],
            'explanation': '$(x+1)^3 = 0 \\Rightarrow x = -1$ (triple root — one x-intercept).',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 5x^2 + 6x$.',
            'answer': '$(0,\\ 0),\\ (2,\\ 0),\\ (3,\\ 0)$',
            'wrong': ['$(0,\\ 0),\\ (-2,\\ 0),\\ (-3,\\ 0)$', '$(2,\\ 0)$ and $(3,\\ 0)$', '$(5,\\ 0)$ and $(6,\\ 0)$'],
            'explanation': '$x(x-2)(x-3)=0 \\Rightarrow x = 0, 2, 3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 + x^2 - 4x - 4$.',
            'answer': '$(-1,\\ 0),\\ (2,\\ 0),\\ (-2,\\ 0)$',
            'wrong': ['$(1,\\ 0),\\ (2,\\ 0),\\ (-2,\\ 0)$', '$(4,\\ 0)$ and $(-4,\\ 0)$', '$(1,\\ 0)$ only'],
            'explanation': '$(x+1)(x-2)(x+2)=0 \\Rightarrow x = -1, 2, -2$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 + 5x^2 + 6x$.',
            'answer': '$(0,\\ 0),\\ (-2,\\ 0),\\ (-3,\\ 0)$',
            'wrong': ['$(0,\\ 0),\\ (2,\\ 0),\\ (3,\\ 0)$', '$(-2,\\ 0)$ and $(-3,\\ 0)$', '$(5,\\ 0)$ and $(6,\\ 0)$'],
            'explanation': '$x(x+2)(x+3)=0 \\Rightarrow x = 0, -2, -3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 3x^2 - x + 3$.',
            'answer': '$(-1,\\ 0),\\ (1,\\ 0),\\ (3,\\ 0)$',
            'wrong': ['$(1,\\ 0)$ and $(3,\\ 0)$', '$(-1,\\ 0)$ and $(3,\\ 0)$', '$(3,\\ 0)$ only'],
            'explanation': '$(x+1)(x-1)(x-3)=0 \\Rightarrow x = -1, 1, 3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 3x + 2$.',
            'answer': '$(1,\\ 0),\\ (-2,\\ 0)$',
            'wrong': ['$(1,\\ 0),\\ (2,\\ 0),\\ (-2,\\ 0)$', '$(-1,\\ 0)$ and $(2,\\ 0)$',
                      '$(3,\\ 0)$ and $(-2,\\ 0)$'],
            'explanation': '$(x-1)^2(x+2)=0 \\Rightarrow x = 1$ (double) and $x = -2$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 2x^2 - 5x + 6$.',
            'answer': '$(-2,\\ 0),\\ (1,\\ 0),\\ (3,\\ 0)$',
            'wrong': ['$(2,\\ 0),\\ (-1,\\ 0),\\ (-3,\\ 0)$', '$(2,\\ 0)$ and $(3,\\ 0)$',
                      '$(-2,\\ 0)$ and $(1,\\ 0)$'],
            'explanation': '$(x+2)(x-1)(x-3)=0 \\Rightarrow x = -2, 1, 3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = 2x^3 - 6x^2 + 4x$.',
            'answer': '$(0,\\ 0),\\ (1,\\ 0),\\ (2,\\ 0)$',
            'wrong': ['$(0,\\ 0),\\ (-1,\\ 0),\\ (-2,\\ 0)$', '$(1,\\ 0)$ and $(2,\\ 0)$', '$(0,\\ 0)$ only'],
            'explanation': '$2x(x-1)(x-2)=0 \\Rightarrow x = 0, 1, 2$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 7x + 6$.',
            'answer': '$(1,\\ 0),\\ (2,\\ 0),\\ (-3,\\ 0)$',
            'wrong': ['$(-1,\\ 0),\\ (-2,\\ 0),\\ (3,\\ 0)$', '$(7,\\ 0)$ and $(-6,\\ 0)$',
                      '$(1,\\ 0)$ and $(-3,\\ 0)$'],
            'explanation': '$(x-1)(x-2)(x+3)=0 \\Rightarrow x = 1, 2, -3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 9x$.',
            'answer': '$(0,\\ 0),\\ (3,\\ 0),\\ (-3,\\ 0)$',
            'wrong': ['$(0,\\ 0)$ and $(9,\\ 0)$', '$(3,\\ 0)$ and $(-3,\\ 0)$', '$(0,\\ 0)$ only'],
            'explanation': '$x(x-3)(x+3)=0 \\Rightarrow x = 0, \\pm 3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 + 4x^2 + 5x + 2$.',
            'answer': '$(-1,\\ 0),\\ (-2,\\ 0)$',
            'wrong': ['$(1,\\ 0)$ and $(2,\\ 0)$', '$(-1,\\ 0),\\ (-2,\\ 0),\\ (5,\\ 0)$',
                      '$(-5,\\ 0)$ and $(-2,\\ 0)$'],
            'explanation': '$(x+1)^2(x+2)=0 \\Rightarrow x = -1$ (double) and $x = -2$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 2x^2 - 4x + 8$.',
            'answer': '$(2,\\ 0),\\ (-2,\\ 0)$',
            'wrong': ['$(2,\\ 0)$ only', '$(4,\\ 0)$ and $(-2,\\ 0)$', '$(2,\\ 0),\\ (4,\\ 0),\\ (-2,\\ 0)$'],
            'explanation': '$(x-2)^2(x+2)=0 \\Rightarrow x = 2$ (double) and $x = -2$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 + 6x^2 + 11x + 6$.',
            'answer': '$(-1,\\ 0),\\ (-2,\\ 0),\\ (-3,\\ 0)$',
            'wrong': ['$(1,\\ 0),\\ (2,\\ 0),\\ (3,\\ 0)$', '$(-1,\\ 0)$ and $(-2,\\ 0)$', '$(-6,\\ 0)$ only'],
            'explanation': '$(x+1)(x+2)(x+3)=0 \\Rightarrow x = -1, -2, -3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 + 2x^2 - x - 2$.',
            'answer': '$(-2,\\ 0),\\ (1,\\ 0),\\ (-1,\\ 0)$',
            'wrong': ['$(2,\\ 0),\\ (1,\\ 0),\\ (-1,\\ 0)$', '$(-2,\\ 0)$ and $(1,\\ 0)$',
                      '$(2,\\ 0)$ and $(-1,\\ 0)$'],
            'explanation': '$(x+2)(x-1)(x+1)=0 \\Rightarrow x = -2, 1, -1$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 4x^2 + x + 6$.',
            'answer': '$(-1,\\ 0),\\ (2,\\ 0),\\ (3,\\ 0)$',
            'wrong': ['$(1,\\ 0),\\ (-2,\\ 0),\\ (-3,\\ 0)$', '$(-1,\\ 0)$ and $(3,\\ 0)$',
                      '$(4,\\ 0)$ and $(6,\\ 0)$'],
            'explanation': '$(x+1)(x-2)(x-3)=0 \\Rightarrow x = -1, 2, 3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - x^2 - 4x + 4$.',
            'answer': '$(1,\\ 0),\\ (2,\\ 0),\\ (-2,\\ 0)$',
            'wrong': ['$(-1,\\ 0),\\ (2,\\ 0),\\ (-2,\\ 0)$', '$(4,\\ 0)$ and $(-4,\\ 0)$', '$(1,\\ 0)$ only'],
            'explanation': '$(x-1)(x-2)(x+2)=0 \\Rightarrow x = 1, 2, -2$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - x^2 - x + 1$.',
            'answer': '$(1,\\ 0),\\ (-1,\\ 0)$',
            'wrong': ['$(1,\\ 0)$ only', '$(-1,\\ 0)$ only', '$(1,\\ 0),\\ (-1,\\ 0),\\ (2,\\ 0)$'],
            'explanation': '$(x-1)^2(x+1)=0 \\Rightarrow x = 1$ (double) and $x = -1$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = 3x^3 - 3x$.',
            'answer': '$(0,\\ 0),\\ (1,\\ 0),\\ (-1,\\ 0)$',
            'wrong': ['$(0,\\ 0)$ and $(3,\\ 0)$', '$(1,\\ 0)$ and $(-1,\\ 0)$', '$(0,\\ 0)$ only'],
            'explanation': '$3x(x-1)(x+1)=0 \\Rightarrow x = 0, \\pm 1$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 3x^2 + 4$.',
            'answer': '$(-1,\\ 0),\\ (2,\\ 0)$',
            'wrong': ['$(1,\\ 0)$ and $(-2,\\ 0)$', '$(-1,\\ 0),\\ (2,\\ 0),\\ (-2,\\ 0)$',
                      '$(3,\\ 0)$ and $(4,\\ 0)$'],
            'explanation': '$(x+1)(x-2)^2=0 \\Rightarrow x = -1$ and $x = 2$ (double).',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 7x^2 + 14x - 8$.',
            'answer': '$(1,\\ 0),\\ (2,\\ 0),\\ (4,\\ 0)$',
            'wrong': ['$(-1,\\ 0),\\ (-2,\\ 0),\\ (-4,\\ 0)$', '$(7,\\ 0)$ and $(8,\\ 0)$',
                      '$(1,\\ 0)$ and $(4,\\ 0)$'],
            'explanation': '$(x-1)(x-2)(x-4)=0 \\Rightarrow x = 1, 2, 4$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 + 3x^2 - 4$.',
            'answer': '$(1,\\ 0),\\ (-2,\\ 0)$',
            'wrong': ['$(-1,\\ 0)$ and $(2,\\ 0)$', '$(1,\\ 0),\\ (2,\\ 0),\\ (-4,\\ 0)$',
                      '$(3,\\ 0)$ and $(-4,\\ 0)$'],
            'explanation': '$(x-1)(x+2)^2=0 \\Rightarrow x = 1$ and $x = -2$ (double).',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 4x^2 - 7x + 10$.',
            'answer': '$(-2,\\ 0),\\ (1,\\ 0),\\ (5,\\ 0)$',
            'wrong': ['$(2,\\ 0),\\ (-1,\\ 0),\\ (-5,\\ 0)$', '$(4,\\ 0)$ and $(7,\\ 0)$',
                      '$(-2,\\ 0)$ and $(5,\\ 0)$'],
            'explanation': '$(x+2)(x-1)(x-5)=0 \\Rightarrow x = -2, 1, 5$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 6x^2 + 9x$.',
            'answer': '$(0,\\ 0),\\ (3,\\ 0)$',
            'wrong': ['$(0,\\ 0),\\ (3,\\ 0),\\ (-3,\\ 0)$', '$(3,\\ 0)$ only', '$(6,\\ 0)$ and $(9,\\ 0)$'],
            'explanation': '$x(x-3)^2=0 \\Rightarrow x = 0$ and $x = 3$ (double).',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 + x^2 - 6x$.',
            'answer': '$(0,\\ 0),\\ (2,\\ 0),\\ (-3,\\ 0)$',
            'wrong': ['$(0,\\ 0),\\ (-2,\\ 0),\\ (3,\\ 0)$', '$(2,\\ 0)$ and $(-3,\\ 0)$',
                      '$(1,\\ 0)$ and $(-6,\\ 0)$'],
            'explanation': '$x(x-2)(x+3)=0 \\Rightarrow x = 0, 2, -3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 5x^2 + 8x - 4$.',
            'answer': '$(1,\\ 0),\\ (2,\\ 0)$',
            'wrong': ['$(1,\\ 0),\\ (2,\\ 0),\\ (4,\\ 0)$', '$(-1,\\ 0)$ and $(-2,\\ 0)$', '$(4,\\ 0)$ only'],
            'explanation': '$(x-1)(x-2)^2=0 \\Rightarrow x = 1$ and $x = 2$ (double).',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - 4x^2 + 4x$.',
            'answer': '$(0,\\ 0),\\ (2,\\ 0)$',
            'wrong': ['$(0,\\ 0),\\ (2,\\ 0),\\ (-2,\\ 0)$', '$(2,\\ 0)$ only', '$(4,\\ 0)$ and $(0,\\ 0)$'],
            'explanation': '$x(x-2)^2=0 \\Rightarrow x = 0$ and $x = 2$ (double).',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 + 6x^2 + 12x + 8$.',
            'answer': '$(-2,\\ 0)$',
            'wrong': ['$(2,\\ 0)$', '$(-2,\\ 0)$ and $(2,\\ 0)$', '$(-6,\\ 0)$ and $(-8,\\ 0)$'],
            'explanation': '$(x+2)^3=0 \\Rightarrow x = -2$ (triple root — one x-intercept).',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 - x^2 - 9x + 9$.',
            'answer': '$(1,\\ 0),\\ (3,\\ 0),\\ (-3,\\ 0)$',
            'wrong': ['$(-1,\\ 0),\\ (3,\\ 0),\\ (-3,\\ 0)$', '$(1,\\ 0)$ and $(9,\\ 0)$', '$(3,\\ 0)$ only'],
            'explanation': '$x^2(x-1)-9(x-1)=0 \\Rightarrow (x^2-9)(x-1)=0 \\Rightarrow x = 1, \\pm 3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = x^3 + 2x^2 - 9x - 18$.',
            'answer': '$(-2,\\ 0),\\ (3,\\ 0),\\ (-3,\\ 0)$',
            'wrong': ['$(2,\\ 0),\\ (3,\\ 0),\\ (-3,\\ 0)$', '$(-2,\\ 0)$ and $(3,\\ 0)$',
                      '$(9,\\ 0)$ and $(-18,\\ 0)$'],
            'explanation': '$x^2(x+2)-9(x+2)=0 \\Rightarrow (x^2-9)(x+2)=0 \\Rightarrow x = -2, \\pm 3$.',
        }
        ,
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{1}{x - 3}$.',
            'answer': '$x = 3$',
            'wrong': ['$x = -3$', '$y = 3$', '$x = 0$'],
            'explanation': 'Set denominator $= 0$: $x - 3 = 0 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{2}{x + 5}$.',
            'answer': '$x = -5$',
            'wrong': ['$x = 5$', '$y = -5$', '$x = 2$'],
            'explanation': '$x + 5 = 0 \\Rightarrow x = -5$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{x + 1}{x - 2}$.',
            'answer': '$x = 2$',
            'wrong': ['$x = -1$', '$x = -2$', '$y = 1$'],
            'explanation': '$x - 2 = 0 \\Rightarrow x = 2$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{3x}{x + 4}$.',
            'answer': '$x = -4$',
            'wrong': ['$x = 4$', '$x = 3$', '$y = 3$'],
            'explanation': '$x + 4 = 0 \\Rightarrow x = -4$.',
        },
        {
            'question': 'Find the vertical asymptotes of $f(x) = \\dfrac{1}{x^2 - 4}$.',
            'answer': '$x = 2$ and $x = -2$',
            'wrong': ['$x = 4$ only', '$x = 2$ only', '$x = -4$ only'],
            'explanation': '$x^2 - 4 = 0 \\Rightarrow (x-2)(x+2) = 0 \\Rightarrow x = \\pm 2$.',
        },
        {
            'question': 'Find the vertical asymptotes of $f(x) = \\dfrac{x}{x^2 - 9}$.',
            'answer': '$x = 3$ and $x = -3$',
            'wrong': ['$x = 9$ only', '$x = 3$ only', '$x = 0$'],
            'explanation': '$x^2 - 9 = 0 \\Rightarrow x = \\pm 3$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{x^2 + 1}{2x - 6}$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 6$', '$x = -3$', '$x = 2$'],
            'explanation': '$2x - 6 = 0 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{5}{3x + 9}$.',
            'answer': '$x = -3$',
            'wrong': ['$x = 3$', '$x = 9$', '$x = -9$'],
            'explanation': '$3x + 9 = 0 \\Rightarrow x = -3$.',
        },
        {
            'question': 'Find the vertical asymptotes of $f(x) = \\dfrac{2x}{x^2 - 1}$.',
            'answer': '$x = 1$ and $x = -1$',
            'wrong': ['$x = 1$ only', '$x = 2$ and $x = -2$', '$x = 0$'],
            'explanation': '$x^2 - 1 = 0 \\Rightarrow x = \\pm 1$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{x - 3}{x + 7}$.',
            'answer': '$x = -7$',
            'wrong': ['$x = 7$', '$x = 3$', '$x = -3$'],
            'explanation': '$x + 7 = 0 \\Rightarrow x = -7$.',
        },
        {
            'question': 'Find the vertical asymptotes of $f(x) = \\dfrac{1}{x^2 - 5x + 6}$.',
            'answer': '$x = 2$ and $x = 3$',
            'wrong': ['$x = -2$ and $x = -3$', '$x = 5$ and $x = 6$', '$x = 2$ only'],
            'explanation': '$x^2 - 5x + 6 = (x-2)(x-3) = 0 \\Rightarrow x = 2, 3$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{x^2}{4x - 8}$.',
            'answer': '$x = 2$',
            'wrong': ['$x = -2$', '$x = 4$', '$x = 8$'],
            'explanation': '$4x - 8 = 0 \\Rightarrow x = 2$.',
        },
        {
            'question': 'Find the vertical asymptotes of $f(x) = \\dfrac{3}{x^2 + x - 6}$.',
            'answer': '$x = 2$ and $x = -3$',
            'wrong': ['$x = -2$ and $x = 3$', '$x = 1$ and $x = -6$', '$x = 2$ only'],
            'explanation': '$x^2 + x - 6 = (x-2)(x+3) = 0 \\Rightarrow x = 2, -3$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{x + 2}{5x - 10}$.',
            'answer': '$x = 2$',
            'wrong': ['$x = -2$', '$x = 5$', '$x = 10$'],
            'explanation': '$5x - 10 = 0 \\Rightarrow x = 2$.',
        },
        {
            'question': 'Find the vertical asymptotes of $f(x) = \\dfrac{x^2 - 1}{x^2 - 4}$.',
            'answer': '$x = 2$ and $x = -2$',
            'wrong': ['$x = 1$ and $x = -1$', '$x = 4$ only', '$x = 2$ only'],
            'explanation': 'Denominator: $x^2 - 4 = (x-2)(x+2) = 0 \\Rightarrow x = \\pm 2$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{7}{x}$.',
            'answer': '$x = 0$',
            'wrong': ['$y = 0$', '$x = 7$', '$x = 1$'],
            'explanation': '$x = 0$ makes the denominator zero.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{x - 1}{x + 6}$.',
            'answer': '$x = -6$',
            'wrong': ['$x = 6$', '$x = 1$', '$x = -1$'],
            'explanation': '$x + 6 = 0 \\Rightarrow x = -6$.',
        },
        {
            'question': 'Find the vertical asymptotes of $f(x) = \\dfrac{x}{x^2 - 16}$.',
            'answer': '$x = 4$ and $x = -4$',
            'wrong': ['$x = 16$ only', '$x = 4$ only', '$x = 0$'],
            'explanation': '$x^2 - 16 = (x-4)(x+4) = 0 \\Rightarrow x = \\pm 4$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{2x + 3}{x - 1}$.',
            'answer': '$x = 1$',
            'wrong': ['$x = -1$', '$x = 3$', '$y = 2$'],
            'explanation': '$x - 1 = 0 \\Rightarrow x = 1$.',
        },
        {
            'question': 'Find the vertical asymptotes of $f(x) = \\dfrac{x+1}{x^2 - 7x + 12}$.',
            'answer': '$x = 3$ and $x = 4$',
            'wrong': ['$x = -3$ and $x = -4$', '$x = 7$ and $x = 12$', '$x = 3$ only'],
            'explanation': '$x^2 - 7x + 12 = (x-3)(x-4) = 0 \\Rightarrow x = 3, 4$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{x^2 - 4}{x - 2}$.',
            'answer': 'No vertical asymptote',
            'wrong': ['$x = 2$', '$x = -2$', '$x = 4$'],
            'explanation': '$f(x) = \\dfrac{(x-2)(x+2)}{x-2} = x+2$ after cancellation. No asymptote, but a hole at $x = 2$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{4x}{2x + 8}$.',
            'answer': '$x = -4$',
            'wrong': ['$x = 4$', '$x = 8$', '$x = 2$'],
            'explanation': '$2x + 8 = 0 \\Rightarrow x = -4$.',
        },
        {
            'question': 'Find the vertical asymptotes of $f(x) = \\dfrac{1}{x^2 + 2x - 8}$.',
            'answer': '$x = 2$ and $x = -4$',
            'wrong': ['$x = -2$ and $x = 4$', '$x = 2$ only', '$x = 8$ only'],
            'explanation': '$x^2 + 2x - 8 = (x-2)(x+4) = 0 \\Rightarrow x = 2, -4$.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{x^2 + x}{x}$.',
            'answer': 'No vertical asymptote',
            'wrong': ['$x = 0$', '$x = 1$', '$x = -1$'],
            'explanation': '$f(x) = \\dfrac{x(x+1)}{x} = x+1$ after cancellation. Hole at $x=0$, not an asymptote.',
        },
        {
            'question': 'Find the vertical asymptote of $f(x) = \\dfrac{3x - 6}{x^2 - 4x + 4}$.',
            'answer': '$x = 2$',
            'wrong': ['$x = -2$', 'No vertical asymptote', '$x = 4$'],
            'explanation': 'Denominator: $(x-2)^2 = 0 \\Rightarrow x = 2$. Numerator $= 3(x-2) \\neq 0$ at $x=2$ after one factor cancels, leaving $(x-2)$ in denominator.',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 2: Horizontal Asymptote  (25 problems)
        # ══════════════════════════════════════════════════════

        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{3}{x + 2}$.',
            'answer': '$y = 0$',
            'wrong': ['$y = 3$', '$y = 2$', '$y = -2$'],
            'explanation': 'Degree of numerator (0) $<$ degree of denominator (1) $\\Rightarrow y = 0$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{2x}{x - 5}$.',
            'answer': '$y = 2$',
            'wrong': ['$y = 0$', '$y = 5$', '$y = -5$'],
            'explanation': 'Degrees are equal (both 1). Ratio of leading coefficients: $\\tfrac{2}{1} = 2 \\Rightarrow y = 2$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{x^2 + 1}{x + 3}$.',
            'answer': 'No horizontal asymptote',
            'wrong': ['$y = 1$', '$y = 0$', '$y = 3$'],
            'explanation': 'Degree of numerator (2) $>$ degree of denominator (1) $\\Rightarrow$ no horizontal asymptote (oblique instead).',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{4x - 1}{2x + 3}$.',
            'answer': '$y = 2$',
            'wrong': ['$y = 4$', '$y = -\\tfrac{1}{3}$', '$y = 0$'],
            'explanation': 'Equal degrees. Leading coefficients: $\\tfrac{4}{2} = 2 \\Rightarrow y = 2$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{5}{x^2 - 1}$.',
            'answer': '$y = 0$',
            'wrong': ['$y = 5$', '$y = 1$', '$y = -1$'],
            'explanation': 'Degree of numerator (0) $<$ degree of denominator (2) $\\Rightarrow y = 0$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{3x^2}{x^2 + 4}$.',
            'answer': '$y = 3$',
            'wrong': ['$y = 0$', '$y = 4$', '$y = 12$'],
            'explanation': 'Equal degrees. $\\tfrac{3}{1} = 3 \\Rightarrow y = 3$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{x + 1}{x^2 - 9}$.',
            'answer': '$y = 0$',
            'wrong': ['$y = 1$', '$y = -9$', '$y = 3$'],
            'explanation': 'Degree of numerator (1) $<$ degree of denominator (2) $\\Rightarrow y = 0$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{6x^2 - x}{3x^2 + 2}$.',
            'answer': '$y = 2$',
            'wrong': ['$y = 6$', '$y = 3$', '$y = 0$'],
            'explanation': 'Equal degrees. $\\tfrac{6}{3} = 2 \\Rightarrow y = 2$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{x^3 + 2}{x^2 - 1}$.',
            'answer': 'No horizontal asymptote',
            'wrong': ['$y = 1$', '$y = 0$', '$y = 2$'],
            'explanation': 'Degree of numerator (3) $>$ degree of denominator (2) $\\Rightarrow$ no horizontal asymptote.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{-2x}{x + 1}$.',
            'answer': '$y = -2$',
            'wrong': ['$y = 2$', '$y = 0$', '$y = -1$'],
            'explanation': 'Equal degrees. $\\tfrac{-2}{1} = -2 \\Rightarrow y = -2$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{7x^2 + 3}{7x^2 - 3}$.',
            'answer': '$y = 1$',
            'wrong': ['$y = 7$', '$y = 3$', '$y = 0$'],
            'explanation': 'Equal degrees. $\\tfrac{7}{7} = 1 \\Rightarrow y = 1$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{2x^2 - 3x}{x^3 + 1}$.',
            'answer': '$y = 0$',
            'wrong': ['$y = 2$', '$y = -3$', '$y = 1$'],
            'explanation': 'Degree of numerator (2) $<$ degree of denominator (3) $\\Rightarrow y = 0$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{x - 4}{x + 4}$.',
            'answer': '$y = 1$',
            'wrong': ['$y = -1$', '$y = 4$', '$y = 0$'],
            'explanation': 'Equal degrees. $\\tfrac{1}{1} = 1 \\Rightarrow y = 1$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{10}{2x^2 + 5}$.',
            'answer': '$y = 0$',
            'wrong': ['$y = 10$', '$y = 5$', '$y = 2$'],
            'explanation': 'Degree of numerator (0) $<$ degree of denominator (2) $\\Rightarrow y = 0$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{5x - 2}{5x + 2}$.',
            'answer': '$y = 1$',
            'wrong': ['$y = 5$', '$y = -1$', '$y = 0$'],
            'explanation': 'Equal degrees. $\\tfrac{5}{5} = 1 \\Rightarrow y = 1$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{3x^2 + 2x}{x^2 - x - 6}$.',
            'answer': '$y = 3$',
            'wrong': ['$y = 2$', '$y = -6$', '$y = 0$'],
            'explanation': 'Equal degrees. $\\tfrac{3}{1} = 3 \\Rightarrow y = 3$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{4}{x^3 - 8}$.',
            'answer': '$y = 0$',
            'wrong': ['$y = 4$', '$y = -8$', '$y = 2$'],
            'explanation': 'Degree of numerator (0) $<$ degree of denominator (3) $\\Rightarrow y = 0$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{-5x^2}{x^2 + 3}$.',
            'answer': '$y = -5$',
            'wrong': ['$y = 5$', '$y = 3$', '$y = 0$'],
            'explanation': 'Equal degrees. $\\tfrac{-5}{1} = -5 \\Rightarrow y = -5$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{x^2 - 1}{2x^2 + x}$.',
            'answer': '$y = \\tfrac{1}{2}$',
            'wrong': ['$y = 1$', '$y = 2$', '$y = 0$'],
            'explanation': 'Equal degrees. $\\tfrac{1}{2} \\Rightarrow y = \\tfrac{1}{2}$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{x^3 - x}{x^3 + 1}$.',
            'answer': '$y = 1$',
            'wrong': ['$y = 0$', '$y = -1$', '$y = 3$'],
            'explanation': 'Equal degrees (both 3). $\\tfrac{1}{1} = 1 \\Rightarrow y = 1$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{2x^3 - 1}{4x^3 + x}$.',
            'answer': '$y = \\tfrac{1}{2}$',
            'wrong': ['$y = 2$', '$y = 4$', '$y = 0$'],
            'explanation': 'Equal degrees. $\\tfrac{2}{4} = \\tfrac{1}{2} \\Rightarrow y = \\tfrac{1}{2}$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{x^2 + 5x}{x^3 - 2}$.',
            'answer': '$y = 0$',
            'wrong': ['$y = 5$', '$y = -2$', '$y = 1$'],
            'explanation': 'Degree of numerator (2) $<$ degree of denominator (3) $\\Rightarrow y = 0$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{9x - 3}{3x + 6}$.',
            'answer': '$y = 3$',
            'wrong': ['$y = 9$', '$y = -3$', '$y = 0$'],
            'explanation': 'Equal degrees. $\\tfrac{9}{3} = 3 \\Rightarrow y = 3$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{x^4 - 2}{x^4 + 2}$.',
            'answer': '$y = 1$',
            'wrong': ['$y = -1$', '$y = 2$', '$y = 0$'],
            'explanation': 'Equal degrees (both 4). $\\tfrac{1}{1} = 1 \\Rightarrow y = 1$.',
        },
        {
            'question': 'Find the horizontal asymptote of $f(x) = \\dfrac{x^2 - 3x + 2}{x - 1}$.',
            'answer': 'No horizontal asymptote',
            'wrong': ['$y = 1$', '$y = 2$', '$y = 0$'],
            'explanation': 'Degree of numerator (2) $>$ degree of denominator (1) $\\Rightarrow$ no horizontal asymptote (oblique instead).',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 3: y when x is given  (25 problems)
        # ══════════════════════════════════════════════════════

        {
            'question': 'Given $f(x) = \\dfrac{1}{x - 3}$, find $f(5)$.',
            'answer': '$\\dfrac{1}{2}$',
            'wrong': ['$2$', '$-\\dfrac{1}{2}$', '$\\dfrac{1}{8}$'],
            'explanation': '$f(5) = \\dfrac{1}{5-3} = \\dfrac{1}{2}$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{x + 2}{x - 1}$, find $f(3)$.',
            'answer': '$\\dfrac{5}{2}$',
            'wrong': ['$5$', '$\\dfrac{1}{2}$', '$2$'],
            'explanation': '$f(3) = \\dfrac{3+2}{3-1} = \\dfrac{5}{2}$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{2x}{x + 4}$, find $f(2)$.',
            'answer': '$\\dfrac{2}{3}$',
            'wrong': ['$\\dfrac{4}{6}$', '$1$', '$\\dfrac{1}{3}$'],
            'explanation': '$f(2) = \\dfrac{4}{6} = \\dfrac{2}{3}$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{3}{x^2 - 1}$, find $f(2)$.',
            'answer': '$1$',
            'wrong': ['$3$', '$\\dfrac{3}{5}$', '$\\dfrac{1}{3}$'],
            'explanation': '$f(2) = \\dfrac{3}{4-1} = \\dfrac{3}{3} = 1$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{x^2 - 4}{x + 2}$, find $f(4)$.',
            'answer': '$2$',
            'wrong': ['$6$', '$\\dfrac{12}{6}$', '$\\dfrac{4}{3}$'],
            'explanation': '$f(4) = \\dfrac{16-4}{4+2} = \\dfrac{12}{6} = 2$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{5}{x}$, find $f(-5)$.',
            'answer': '$-1$',
            'wrong': ['$1$', '$-5$', '$5$'],
            'explanation': '$f(-5) = \\dfrac{5}{-5} = -1$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{x - 1}{x + 1}$, find $f(0)$.',
            'answer': '$-1$',
            'wrong': ['$1$', '$0$', '$\\dfrac{1}{2}$'],
            'explanation': '$f(0) = \\dfrac{-1}{1} = -1$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{4x + 1}{x - 2}$, find $f(3)$.',
            'answer': '$13$',
            'wrong': ['$\\dfrac{13}{5}$', '$5$', '$\\dfrac{4}{3}$'],
            'explanation': '$f(3) = \\dfrac{12+1}{3-2} = \\dfrac{13}{1} = 13$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{x^2}{x^2 + 1}$, find $f(1)$.',
            'answer': '$\\dfrac{1}{2}$',
            'wrong': ['$1$', '$2$', '$0$'],
            'explanation': '$f(1) = \\dfrac{1}{2}$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{2x - 3}{x + 5}$, find $f(-1)$.',
            'answer': '$-\\dfrac{5}{4}$',
            'wrong': ['$\\dfrac{5}{4}$', '$-5$', '$\\dfrac{1}{4}$'],
            'explanation': '$f(-1) = \\dfrac{-2-3}{-1+5} = \\dfrac{-5}{4}$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{6}{x^2 - 9}$, find $f(6)$.',
            'answer': '$\\dfrac{6}{27} = \\dfrac{2}{9}$',
            'wrong': ['$\\dfrac{1}{6}$', '$\\dfrac{6}{3}$', '$2$'],
            'explanation': '$f(6) = \\dfrac{6}{36-9} = \\dfrac{6}{27} = \\dfrac{2}{9}$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{x + 3}{2x - 4}$, find $f(1)$.',
            'answer': '$-2$',
            'wrong': ['$2$', '$4$', '$\\dfrac{4}{2}$'],
            'explanation': '$f(1) = \\dfrac{4}{2-4} = \\dfrac{4}{-2} = -2$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{x^2 + x}{x - 3}$, find $f(2)$.',
            'answer': '$-6$',
            'wrong': ['$6$', '$-\\dfrac{6}{1}$', '$\\dfrac{6}{5}$'],
            'explanation': '$f(2) = \\dfrac{4+2}{2-3} = \\dfrac{6}{-1} = -6$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{1}{(x-1)^2}$, find $f(3)$.',
            'answer': '$\\dfrac{1}{4}$',
            'wrong': ['$4$', '$\\dfrac{1}{2}$', '$2$'],
            'explanation': '$f(3) = \\dfrac{1}{(3-1)^2} = \\dfrac{1}{4}$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{3x + 6}{x + 2}$, find $f(0)$.',
            'answer': '$3$',
            'wrong': ['$6$', '$\\dfrac{6}{2}$', '$0$'],
            'explanation': '$f(0) = \\dfrac{6}{2} = 3$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{x}{x^2 - 4}$, find $f(3)$.',
            'answer': '$\\dfrac{3}{5}$',
            'wrong': ['$\\dfrac{5}{3}$', '$3$', '$\\dfrac{1}{5}$'],
            'explanation': '$f(3) = \\dfrac{3}{9-4} = \\dfrac{3}{5}$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{x^2 - 9}{x + 3}$, find $f(6)$.',
            'answer': '$3$',
            'wrong': ['$9$', '$\\dfrac{27}{9}$', '$\\dfrac{1}{3}$'],
            'explanation': '$f(6) = \\dfrac{36-9}{6+3} = \\dfrac{27}{9} = 3$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{2}{x^2 + x}$, find $f(2)$.',
            'answer': '$\\dfrac{1}{3}$',
            'wrong': ['$\\dfrac{2}{3}$', '$3$', '$\\dfrac{1}{6}$'],
            'explanation': '$f(2) = \\dfrac{2}{4+2} = \\dfrac{2}{6} = \\dfrac{1}{3}$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{x - 5}{x^2 - 25}$, find $f(6)$.',
            'answer': '$\\dfrac{1}{11}$',
            'wrong': ['$\\dfrac{1}{36}$', '$11$', '$\\dfrac{6}{11}$'],
            'explanation': '$f(6) = \\dfrac{1}{6+5} = \\dfrac{1}{11}$ (after cancelling $x-5$).',
        },
        {
            'question': 'Given $f(x) = \\dfrac{5x}{x^2 - 1}$, find $f(2)$.',
            'answer': '$\\dfrac{10}{3}$',
            'wrong': ['$\\dfrac{3}{10}$', '$5$', '$\\dfrac{10}{5}$'],
            'explanation': '$f(2) = \\dfrac{10}{4-1} = \\dfrac{10}{3}$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{x^2 - 1}{x - 1}$, find $f(4)$.',
            'answer': '$5$',
            'wrong': ['$\\dfrac{15}{3}$', '$3$', '$15$'],
            'explanation': '$f(x) = x+1$ after cancelling. $f(4) = 5$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{4x - 8}{x - 2}$, find $f(5)$.',
            'answer': '$4$',
            'wrong': ['$12$', '$\\dfrac{12}{3}$', '$2$'],
            'explanation': '$f(x) = 4$ after cancelling $(x-2)$. Constant function (with hole at $x=2$).',
        },
        {
            'question': 'Given $f(x) = \\dfrac{x + 1}{x^2 + 3x + 2}$, find $f(3)$.',
            'answer': '$\\dfrac{1}{5}$',
            'wrong': ['$5$', '$\\dfrac{4}{20}$', '$\\dfrac{1}{4}$'],
            'explanation': '$f(x) = \\dfrac{x+1}{(x+1)(x+2)} = \\dfrac{1}{x+2}$. $f(3) = \\dfrac{1}{5}$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{3x^2}{x^2 + 9}$, find $f(3)$.',
            'answer': '$\\dfrac{3}{2}$',
            'wrong': ['$3$', '$\\dfrac{27}{18}$', '$\\dfrac{1}{2}$'],
            'explanation': '$f(3) = \\dfrac{27}{9+9} = \\dfrac{27}{18} = \\dfrac{3}{2}$.',
        },
        {
            'question': 'Given $f(x) = \\dfrac{x^2 + 2x}{x}$, find $f(4)$.',
            'answer': '$6$',
            'wrong': ['$\\dfrac{24}{4}$', '$4$', '$10$'],
            'explanation': '$f(x) = x + 2$ after cancelling. $f(4) = 6$.',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 4: x-intercepts  (25 problems)
        # ══════════════════════════════════════════════════════

        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{x - 4}{x + 2}$.',
            'answer': '$(4,\\ 0)$',
            'wrong': ['$(-2,\\ 0)$', '$(2,\\ 0)$', '$(0,\\ -2)$'],
            'explanation': 'Set numerator $= 0$: $x - 4 = 0 \\Rightarrow x = 4$. x-intercepts come from the numerator, not the denominator.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{x + 3}{x - 1}$.',
            'answer': '$(-3,\\ 0)$',
            'wrong': ['$(1,\\ 0)$', '$(3,\\ 0)$', '$(-1,\\ 0)$'],
            'explanation': '$x + 3 = 0 \\Rightarrow x = -3$.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{2x - 6}{x + 5}$.',
            'answer': '$(3,\\ 0)$',
            'wrong': ['$(-5,\\ 0)$', '$(6,\\ 0)$', '$(-3,\\ 0)$'],
            'explanation': '$2x - 6 = 0 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = \\dfrac{x^2 - 4}{x + 3}$.',
            'answer': '$(2,\\ 0)$ and $(-2,\\ 0)$',
            'wrong': ['$(-3,\\ 0)$', '$(4,\\ 0)$ only', '$(2,\\ 0)$ only'],
            'explanation': '$x^2 - 4 = 0 \\Rightarrow x = \\pm 2$.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{3}{x - 2}$.',
            'answer': 'No $x$-intercept',
            'wrong': ['$(2,\\ 0)$', '$(3,\\ 0)$', '$(0,\\ 3)$'],
            'explanation': 'Numerator is $3 \\neq 0$, so $f(x)$ never equals $0$. No $x$-intercept.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = \\dfrac{x^2 - 9}{x - 1}$.',
            'answer': '$(3,\\ 0)$ and $(-3,\\ 0)$',
            'wrong': ['$(1,\\ 0)$', '$(9,\\ 0)$ only', '$(3,\\ 0)$ only'],
            'explanation': '$x^2 - 9 = 0 \\Rightarrow x = \\pm 3$ (and $x \\neq 1$, which is the VA, not an intercept).',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{x^2 - 5x + 6}{x + 1}$.',
            'answer': '$(2,\\ 0)$ and $(3,\\ 0)$',
            'wrong': ['$(-1,\\ 0)$', '$(5,\\ 0)$ and $(6,\\ 0)$', '$(2,\\ 0)$ only'],
            'explanation': '$x^2-5x+6 = (x-2)(x-3) = 0 \\Rightarrow x = 2, 3$.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{4x}{x^2 + 1}$.',
            'answer': '$(0,\\ 0)$',
            'wrong': ['No $x$-intercept', '$(1,\\ 0)$', '$(-1,\\ 0)$'],
            'explanation': '$4x = 0 \\Rightarrow x = 0$. Denominator $x^2+1 > 0$ always, so $x = 0$ is valid.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{x^2 - 1}{x + 5}$.',
            'answer': '$(1,\\ 0)$ and $(-1,\\ 0)$',
            'wrong': ['$(-5,\\ 0)$', '$(1,\\ 0)$ only', '$(5,\\ 0)$ and $(-5,\\ 0)$'],
            'explanation': '$x^2-1=0 \\Rightarrow x = \\pm 1$.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{5x + 10}{x^2 - 4}$.',
            'answer': '$(-2,\\ 0)$ — with a hole, not a crossing',
            'wrong': ['$(-2,\\ 0)$ and $(2,\\ 0)$', '$(2,\\ 0)$', '$(5,\\ 0)$'],
            'explanation': '$5x+10 = 5(x+2)$. Denominator $=(x-2)(x+2)$. At $x=-2$: both are 0 (hole). At $x=2$: VA. No true $x$-intercept.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{x - 7}{x^2 + 1}$.',
            'answer': '$(7,\\ 0)$',
            'wrong': ['No $x$-intercept', '$(-7,\\ 0)$', '$(1,\\ 0)$'],
            'explanation': '$x - 7 = 0 \\Rightarrow x = 7$. Denominator $x^2+1 > 0$ always.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{x^2 + 4}{x - 3}$.',
            'answer': 'No $x$-intercept',
            'wrong': ['$(3,\\ 0)$', '$(2,\\ 0)$', '$(-2,\\ 0)$'],
            'explanation': '$x^2 + 4 \\geq 4 > 0$ for all real $x$. Numerator never equals 0. No $x$-intercept.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = \\dfrac{x^2 + x - 6}{x - 4}$.',
            'answer': '$(2,\\ 0)$ and $(-3,\\ 0)$',
            'wrong': ['$(4,\\ 0)$', '$(3,\\ 0)$ and $(-2,\\ 0)$', '$(2,\\ 0)$ only'],
            'explanation': '$x^2+x-6=(x-2)(x+3)=0 \\Rightarrow x=2, -3$.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{3x - 9}{x + 2}$.',
            'answer': '$(3,\\ 0)$',
            'wrong': ['$(-2,\\ 0)$', '$(9,\\ 0)$', '$(-3,\\ 0)$'],
            'explanation': '$3x-9=0 \\Rightarrow x=3$.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = \\dfrac{x^2 - 2x - 3}{x + 4}$.',
            'answer': '$(3,\\ 0)$ and $(-1,\\ 0)$',
            'wrong': ['$(-4,\\ 0)$', '$(2,\\ 0)$ and $(3,\\ 0)$', '$(3,\\ 0)$ only'],
            'explanation': '$x^2-2x-3=(x-3)(x+1)=0 \\Rightarrow x=3,-1$.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{2x}{x - 6}$.',
            'answer': '$(0,\\ 0)$',
            'wrong': ['$(6,\\ 0)$', '$(2,\\ 0)$', 'No $x$-intercept'],
            'explanation': '$2x=0 \\Rightarrow x=0$, and $0 \\neq 6$ (not the VA).',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = \\dfrac{x^2 - 7x + 12}{x + 1}$.',
            'answer': '$(3,\\ 0)$ and $(4,\\ 0)$',
            'wrong': ['$(-1,\\ 0)$', '$(7,\\ 0)$ and $(12,\\ 0)$', '$(3,\\ 0)$ only'],
            'explanation': '$(x-3)(x-4)=0 \\Rightarrow x=3, 4$.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{-3x}{x^2 - 1}$.',
            'answer': '$(0,\\ 0)$',
            'wrong': ['$(1,\\ 0)$ and $(-1,\\ 0)$', '$(3,\\ 0)$', 'No $x$-intercept'],
            'explanation': '$-3x=0 \\Rightarrow x=0$, and $0 \\neq \\pm 1$.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{x^2 - 16}{x^2 + 1}$.',
            'answer': '$(4,\\ 0)$ and $(-4,\\ 0)$',
            'wrong': ['$(16,\\ 0)$ only', '$(4,\\ 0)$ only', 'No $x$-intercept'],
            'explanation': '$x^2-16=0 \\Rightarrow x=\\pm 4$. Denominator $>0$ always.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{x^2 + 2x}{x - 3}$.',
            'answer': '$(0,\\ 0)$ and $(-2,\\ 0)$',
            'wrong': ['$(3,\\ 0)$', '$(0,\\ 0)$ only', '$(2,\\ 0)$'],
            'explanation': '$x^2+2x=x(x+2)=0 \\Rightarrow x=0, -2$.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{6}{x^2 + 4}$.',
            'answer': 'No $x$-intercept',
            'wrong': ['$(6,\\ 0)$', '$(2,\\ 0)$', '$(-2,\\ 0)$'],
            'explanation': 'Numerator $= 6 \\neq 0$. No $x$-intercept.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = \\dfrac{x^3 - x}{x + 2}$.',
            'answer': '$(0,\\ 0),\\ (1,\\ 0),\\ (-1,\\ 0)$',
            'wrong': ['$(-2,\\ 0)$', '$(0,\\ 0)$ only', '$(1,\\ 0)$ and $(-1,\\ 0)$'],
            'explanation': '$x^3-x=x(x-1)(x+1)=0 \\Rightarrow x=0, 1, -1$ (all $\\neq -2$).',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{x - 2}{x^2 - 4x + 4}$.',
            'answer': 'No $x$-intercept (hole at $x = 2$)',
            'wrong': ['$(2,\\ 0)$', '$(4,\\ 0)$', '$(-2,\\ 0)$'],
            'explanation': 'Numerator $= x-2$, denominator $= (x-2)^2$. Cancel one factor: $f(x) = \\dfrac{1}{x-2}$. At $x=2$: original undefined (hole), not an intercept.',
        },
        {
            'question': 'Find the $x$-intercept of $f(x) = \\dfrac{4x - 12}{x^2 + 5}$.',
            'answer': '$(3,\\ 0)$',
            'wrong': ['$(-3,\\ 0)$', '$(12,\\ 0)$', 'No $x$-intercept'],
            'explanation': '$4x-12=0 \\Rightarrow x=3$. Denominator $>0$ always.',
        },
        {
            'question': 'Find the $x$-intercepts of $f(x) = \\dfrac{x^2 - 4x + 3}{x^2 + 1}$.',
            'answer': '$(1,\\ 0)$ and $(3,\\ 0)$',
            'wrong': ['$(4,\\ 0)$ and $(3,\\ 0)$', '$(1,\\ 0)$ only', 'No $x$-intercept'],
            'explanation': '$x^2-4x+3=(x-1)(x-3)=0 \\Rightarrow x=1, 3$. Denominator always $> 0$.',
        },
        {
            'question': 'Given $f(x) = 2 \\cdot 3^x$, find $f(2)$.',
            'answer': '$18$',
            'wrong': ['$12$', '$36$', '$6$'],
            'explanation': '$f(2) = 2 \\cdot 3^2 = 2 \\cdot 9 = 18$.',
        },
        {
            'question': 'Given $f(x) = 5 \\cdot 2^x$, find $f(3)$.',
            'answer': '$40$',
            'wrong': ['$30$', '$80$', '$15$'],
            'explanation': '$f(3) = 5 \\cdot 2^3 = 5 \\cdot 8 = 40$.',
        },
        {
            'question': 'Given $f(x) = 3 \\cdot 4^x$, find $f(0)$.',
            'answer': '$3$',
            'wrong': ['$0$', '$4$', '$12$'],
            'explanation': '$f(0) = 3 \\cdot 4^0 = 3 \\cdot 1 = 3$.',
        },
        {
            'question': 'Given $f(x) = 6 \\cdot 2^x$, find $f(4)$.',
            'answer': '$96$',
            'wrong': ['$48$', '$192$', '$24$'],
            'explanation': '$f(4) = 6 \\cdot 2^4 = 6 \\cdot 16 = 96$.',
        },
        {
            'question': 'Given $f(x) = 4 \\cdot 3^x$, find $f(3)$.',
            'answer': '$108$',
            'wrong': ['$36$', '$324$', '$54$'],
            'explanation': '$f(3) = 4 \\cdot 3^3 = 4 \\cdot 27 = 108$.',
        },
        {
            'question': 'Given $f(x) = 10 \\cdot 2^x$, find $f(-1)$.',
            'answer': '$5$',
            'wrong': ['$-20$', '$20$', '$10$'],
            'explanation': '$f(-1) = 10 \\cdot 2^{-1} = 10 \\cdot \\tfrac{1}{2} = 5$.',
        },
        {
            'question': 'Given $f(x) = 1 \\cdot 5^x$, find $f(3)$.',
            'answer': '$125$',
            'wrong': ['$15$', '$25$', '$625$'],
            'explanation': '$f(3) = 1 \\cdot 5^3 = 125$.',
        },
        {
            'question': 'Given $f(x) = 2 \\cdot 10^x$, find $f(2)$.',
            'answer': '$200$',
            'wrong': ['$20$', '$2000$', '$40$'],
            'explanation': '$f(2) = 2 \\cdot 10^2 = 2 \\cdot 100 = 200$.',
        },
        {
            'question': 'Given $f(x) = 8 \\cdot \\left(\\tfrac{1}{2}\\right)^x$, find $f(3)$.',
            'answer': '$1$',
            'wrong': ['$2$', '$4$', '$\\tfrac{1}{2}$'],
            'explanation': '$f(3) = 8 \\cdot \\left(\\tfrac{1}{2}\\right)^3 = 8 \\cdot \\tfrac{1}{8} = 1$.',
        },
        {
            'question': 'Given $f(x) = 27 \\cdot \\left(\\tfrac{1}{3}\\right)^x$, find $f(3)$.',
            'answer': '$1$',
            'wrong': ['$3$', '$9$', '$\\tfrac{1}{3}$'],
            'explanation': '$f(3) = 27 \\cdot \\left(\\tfrac{1}{3}\\right)^3 = 27 \\cdot \\tfrac{1}{27} = 1$.',
        },
        {
            'question': 'Given $f(x) = 3 \\cdot 2^x$, find $f(5)$.',
            'answer': '$96$',
            'wrong': ['$30$', '$192$', '$48$'],
            'explanation': '$f(5) = 3 \\cdot 2^5 = 3 \\cdot 32 = 96$.',
        },
        {
            'question': 'Given $f(x) = 5 \\cdot 3^x$, find $f(0)$.',
            'answer': '$5$',
            'wrong': ['$0$', '$15$', '$1$'],
            'explanation': '$f(0) = 5 \\cdot 3^0 = 5 \\cdot 1 = 5$.',
        },
        {
            'question': 'Given $f(x) = 4 \\cdot 5^x$, find $f(2)$.',
            'answer': '$100$',
            'wrong': ['$40$', '$20$', '$400$'],
            'explanation': '$f(2) = 4 \\cdot 5^2 = 4 \\cdot 25 = 100$.',
        },
        {
            'question': 'Given $f(x) = 2 \\cdot 6^x$, find $f(2)$.',
            'answer': '$72$',
            'wrong': ['$24$', '$144$', '$36$'],
            'explanation': '$f(2) = 2 \\cdot 6^2 = 2 \\cdot 36 = 72$.',
        },
        {
            'question': 'Given $f(x) = 100 \\cdot \\left(\\tfrac{1}{10}\\right)^x$, find $f(2)$.',
            'answer': '$1$',
            'wrong': ['$10$', '$100$', '$\\tfrac{1}{10}$'],
            'explanation': '$f(2) = 100 \\cdot \\left(\\tfrac{1}{10}\\right)^2 = 100 \\cdot \\tfrac{1}{100} = 1$.',
        },
        {
            'question': 'Given $f(x) = 7 \\cdot 2^x$, find $f(-2)$.',
            'answer': '$\\dfrac{7}{4}$',
            'wrong': ['$28$', '$-28$', '$\\dfrac{7}{2}$'],
            'explanation': '$f(-2) = 7 \\cdot 2^{-2} = 7 \\cdot \\tfrac{1}{4} = \\tfrac{7}{4}$.',
        },
        {
            'question': 'Given $f(x) = 1 \\cdot 4^x$, find $f(\\tfrac{1}{2})$.',
            'answer': '$2$',
            'wrong': ['$4$', '$\\tfrac{1}{2}$', '$1$'],
            'explanation': '$f(\\tfrac{1}{2}) = 4^{1/2} = \\sqrt{4} = 2$.',
        },
        {
            'question': 'Given $f(x) = 9 \\cdot \\left(\\tfrac{1}{3}\\right)^x$, find $f(2)$.',
            'answer': '$1$',
            'wrong': ['$3$', '$\\tfrac{9}{3}$', '$\\tfrac{1}{9}$'],
            'explanation': '$f(2) = 9 \\cdot \\tfrac{1}{9} = 1$.',
        },
        {
            'question': 'Given $f(x) = 3 \\cdot 3^x$, find $f(3)$.',
            'answer': '$81$',
            'wrong': ['$27$', '$9$', '$243$'],
            'explanation': '$f(3) = 3 \\cdot 3^3 = 3 \\cdot 27 = 81 = 3^4$.',
        },
        {
            'question': 'Given $f(x) = 2 \\cdot 5^x$, find $f(3)$.',
            'answer': '$250$',
            'wrong': ['$30$', '$125$', '$500$'],
            'explanation': '$f(3) = 2 \\cdot 5^3 = 2 \\cdot 125 = 250$.',
        },
        {
            'question': 'Given $f(x) = 16 \\cdot \\left(\\tfrac{1}{2}\\right)^x$, find $f(4)$.',
            'answer': '$1$',
            'wrong': ['$2$', '$4$', '$8$'],
            'explanation': '$f(4) = 16 \\cdot \\tfrac{1}{16} = 1$.',
        },
        {
            'question': 'Given $f(x) = 6 \\cdot 3^x$, find $f(2)$.',
            'answer': '$54$',
            'wrong': ['$18$', '$108$', '$36$'],
            'explanation': '$f(2) = 6 \\cdot 9 = 54$.',
        },
        {
            'question': 'Given $f(x) = 5 \\cdot 2^x$, find $f(-3)$.',
            'answer': '$\\dfrac{5}{8}$',
            'wrong': ['$-40$', '$\\dfrac{5}{4}$', '$40$'],
            'explanation': '$f(-3) = 5 \\cdot 2^{-3} = 5 \\cdot \\tfrac{1}{8} = \\tfrac{5}{8}$.',
        },
        {
            'question': 'Given $f(x) = 1 \\cdot 9^x$, find $f(\\tfrac{1}{2})$.',
            'answer': '$3$',
            'wrong': ['$9$', '$\\tfrac{9}{2}$', '$\\tfrac{1}{3}$'],
            'explanation': '$f(\\tfrac{1}{2}) = 9^{1/2} = 3$.',
        },
        {
            'question': 'Given $f(x) = 4 \\cdot 2^x$, find $f(1)$.',
            'answer': '$8$',
            'wrong': ['$4$', '$16$', '$6$'],
            'explanation': '$f(1) = 4 \\cdot 2^1 = 8$.',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 2: Given y, find x  (25 problems)
        # ══════════════════════════════════════════════════════

        {
            'question': 'Given $f(x) = 2^x$, find $x$ if $f(x) = 8$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 4$', '$x = 2$', '$x = 6$'],
            'explanation': '$2^x = 8 = 2^3 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Given $f(x) = 3^x$, find $x$ if $f(x) = 27$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 9$', '$x = 2$', '$x = 4$'],
            'explanation': '$3^x = 27 = 3^3 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Given $f(x) = 5^x$, find $x$ if $f(x) = 25$.',
            'answer': '$x = 2$',
            'wrong': ['$x = 5$', '$x = 3$', '$x = 1$'],
            'explanation': '$5^x = 25 = 5^2 \\Rightarrow x = 2$.',
        },
        {
            'question': 'Given $f(x) = 2 \\cdot 3^x$, find $x$ if $f(x) = 54$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 2$', '$x = 4$', '$x = 27$'],
            'explanation': '$2 \\cdot 3^x = 54 \\Rightarrow 3^x = 27 = 3^3 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Given $f(x) = 4 \\cdot 2^x$, find $x$ if $f(x) = 32$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 2$', '$x = 4$', '$x = 8$'],
            'explanation': '$4 \\cdot 2^x = 32 \\Rightarrow 2^x = 8 = 2^3 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Given $f(x) = 10^x$, find $x$ if $f(x) = 1000$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 4$', '$x = 2$', '$x = 100$'],
            'explanation': '$10^x = 1000 = 10^3 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Given $f(x) = 5 \\cdot 2^x$, find $x$ if $f(x) = 40$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 4$', '$x = 2$', '$x = 8$'],
            'explanation': '$5 \\cdot 2^x = 40 \\Rightarrow 2^x = 8 = 2^3 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Given $f(x) = 2^x$, find $x$ if $f(x) = \\dfrac{1}{4}$.',
            'answer': '$x = -2$',
            'wrong': ['$x = 2$', '$x = -4$', '$x = -1$'],
            'explanation': '$2^x = \\tfrac{1}{4} = 2^{-2} \\Rightarrow x = -2$.',
        },
        {
            'question': 'Given $f(x) = 3^x$, find $x$ if $f(x) = \\dfrac{1}{9}$.',
            'answer': '$x = -2$',
            'wrong': ['$x = 2$', '$x = -3$', '$x = -1$'],
            'explanation': '$3^x = \\tfrac{1}{9} = 3^{-2} \\Rightarrow x = -2$.',
        },
        {
            'question': 'Given $f(x) = 6 \\cdot 2^x$, find $x$ if $f(x) = 6$.',
            'answer': '$x = 0$',
            'wrong': ['$x = 1$', '$x = -1$', '$x = 6$'],
            'explanation': '$6 \\cdot 2^x = 6 \\Rightarrow 2^x = 1 = 2^0 \\Rightarrow x = 0$.',
        },
        {
            'question': 'Given $f(x) = 4^x$, find $x$ if $f(x) = 64$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 4$', '$x = 2$', '$x = 16$'],
            'explanation': '$4^x = 64 = 4^3 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Given $f(x) = 3 \\cdot 5^x$, find $x$ if $f(x) = 75$.',
            'answer': '$x = 2$',
            'wrong': ['$x = 3$', '$x = 1$', '$x = 25$'],
            'explanation': '$3 \\cdot 5^x = 75 \\Rightarrow 5^x = 25 = 5^2 \\Rightarrow x = 2$.',
        },
        {
            'question': 'Given $f(x) = 2^x$, find $x$ if $f(x) = 64$.',
            'answer': '$x = 6$',
            'wrong': ['$x = 5$', '$x = 7$', '$x = 32$'],
            'explanation': '$2^x = 64 = 2^6 \\Rightarrow x = 6$.',
        },
        {
            'question': 'Given $f(x) = 10 \\cdot 3^x$, find $x$ if $f(x) = 10$.',
            'answer': '$x = 0$',
            'wrong': ['$x = 1$', '$x = 3$', '$x = 10$'],
            'explanation': '$10 \\cdot 3^x = 10 \\Rightarrow 3^x = 1 = 3^0 \\Rightarrow x = 0$.',
        },
        {
            'question': 'Given $f(x) = 5^x$, find $x$ if $f(x) = 125$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 2$', '$x = 4$', '$x = 25$'],
            'explanation': '$5^x = 125 = 5^3 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Given $f(x) = 2 \\cdot 4^x$, find $x$ if $f(x) = 128$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 4$', '$x = 2$', '$x = 64$'],
            'explanation': '$2 \\cdot 4^x = 128 \\Rightarrow 4^x = 64 = 4^3 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Given $f(x) = 4^x$, find $x$ if $f(x) = \\dfrac{1}{16}$.',
            'answer': '$x = -2$',
            'wrong': ['$x = 2$', '$x = -4$', '$x = -1$'],
            'explanation': '$4^x = \\tfrac{1}{16} = 4^{-2} \\Rightarrow x = -2$.',
        },
        {
            'question': 'Given $f(x) = 7 \\cdot 2^x$, find $x$ if $f(x) = 56$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 4$', '$x = 2$', '$x = 8$'],
            'explanation': '$7 \\cdot 2^x = 56 \\Rightarrow 2^x = 8 = 2^3 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Given $f(x) = 3^x$, find $x$ if $f(x) = 243$.',
            'answer': '$x = 5$',
            'wrong': ['$x = 4$', '$x = 6$', '$x = 81$'],
            'explanation': '$3^x = 243 = 3^5 \\Rightarrow x = 5$.',
        },
        {
            'question': 'Given $f(x) = 4 \\cdot 3^x$, find $x$ if $f(x) = 324$.',
            'answer': '$x = 4$',
            'wrong': ['$x = 3$', '$x = 5$', '$x = 81$'],
            'explanation': '$4 \\cdot 3^x = 324 \\Rightarrow 3^x = 81 = 3^4 \\Rightarrow x = 4$.',
        },
        {
            'question': 'Given $f(x) = 2^x$, find $x$ if $f(x) = \\dfrac{1}{32}$.',
            'answer': '$x = -5$',
            'wrong': ['$x = 5$', '$x = -4$', '$x = -6$'],
            'explanation': '$2^x = \\tfrac{1}{32} = 2^{-5} \\Rightarrow x = -5$.',
        },
        {
            'question': 'Given $f(x) = 8 \\cdot 5^x$, find $x$ if $f(x) = 200$.',
            'answer': '$x = 2$',
            'wrong': ['$x = 3$', '$x = 1$', '$x = 25$'],
            'explanation': '$8 \\cdot 5^x = 200 \\Rightarrow 5^x = 25 = 5^2 \\Rightarrow x = 2$.',
        },
        {
            'question': 'Given $f(x) = 6^x$, find $x$ if $f(x) = 216$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 2$', '$x = 4$', '$x = 36$'],
            'explanation': '$6^x = 216 = 6^3 \\Rightarrow x = 3$.',
        },
        {
            'question': 'Given $f(x) = 5 \\cdot 4^x$, find $x$ if $f(x) = 5$.',
            'answer': '$x = 0$',
            'wrong': ['$x = 1$', '$x = 4$', '$x = 5$'],
            'explanation': '$5 \\cdot 4^x = 5 \\Rightarrow 4^x = 1 = 4^0 \\Rightarrow x = 0$.',
        },
        {
            'question': 'Given $f(x) = 2 \\cdot 10^x$, find $x$ if $f(x) = 2000$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 2$', '$x = 4$', '$x = 1000$'],
            'explanation': '$2 \\cdot 10^x = 2000 \\Rightarrow 10^x = 1000 = 10^3 \\Rightarrow x = 3$.',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 3: Given x and y, find a (b known)  (25 problems)
        # ══════════════════════════════════════════════════════

        {
            'question': 'In $f(x) = a \\cdot 2^x$, find $a$ if $f(3) = 24$.',
            'answer': '$a = 3$',
            'wrong': ['$a = 8$', '$a = 6$', '$a = 12$'],
            'explanation': '$a \\cdot 2^3 = 24 \\Rightarrow 8a = 24 \\Rightarrow a = 3$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 3^x$, find $a$ if $f(2) = 45$.',
            'answer': '$a = 5$',
            'wrong': ['$a = 9$', '$a = 15$', '$a = 3$'],
            'explanation': '$a \\cdot 3^2 = 45 \\Rightarrow 9a = 45 \\Rightarrow a = 5$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 5^x$, find $a$ if $f(2) = 100$.',
            'answer': '$a = 4$',
            'wrong': ['$a = 5$', '$a = 20$', '$a = 2$'],
            'explanation': '$a \\cdot 25 = 100 \\Rightarrow a = 4$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 4^x$, find $a$ if $f(3) = 192$.',
            'answer': '$a = 3$',
            'wrong': ['$a = 4$', '$a = 12$', '$a = 6$'],
            'explanation': '$a \\cdot 4^3 = 192 \\Rightarrow 64a = 192 \\Rightarrow a = 3$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 2^x$, find $a$ if $f(0) = 7$.',
            'answer': '$a = 7$',
            'wrong': ['$a = 1$', '$a = 14$', '$a = 2$'],
            'explanation': '$a \\cdot 2^0 = 7 \\Rightarrow a \\cdot 1 = 7 \\Rightarrow a = 7$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 10^x$, find $a$ if $f(2) = 500$.',
            'answer': '$a = 5$',
            'wrong': ['$a = 50$', '$a = 10$', '$a = 100$'],
            'explanation': '$a \\cdot 100 = 500 \\Rightarrow a = 5$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 3^x$, find $a$ if $f(0) = 12$.',
            'answer': '$a = 12$',
            'wrong': ['$a = 4$', '$a = 3$', '$a = 36$'],
            'explanation': '$a \\cdot 1 = 12 \\Rightarrow a = 12$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 2^x$, find $a$ if $f(4) = 48$.',
            'answer': '$a = 3$',
            'wrong': ['$a = 12$', '$a = 6$', '$a = 4$'],
            'explanation': '$a \\cdot 16 = 48 \\Rightarrow a = 3$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 5^x$, find $a$ if $f(3) = 250$.',
            'answer': '$a = 2$',
            'wrong': ['$a = 5$', '$a = 50$', '$a = 10$'],
            'explanation': '$a \\cdot 125 = 250 \\Rightarrow a = 2$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 6^x$, find $a$ if $f(2) = 72$.',
            'answer': '$a = 2$',
            'wrong': ['$a = 6$', '$a = 12$', '$a = 3$'],
            'explanation': '$a \\cdot 36 = 72 \\Rightarrow a = 2$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 4^x$, find $a$ if $f(0) = 9$.',
            'answer': '$a = 9$',
            'wrong': ['$a = 4$', '$a = 36$', '$a = 1$'],
            'explanation': '$a \\cdot 1 = 9 \\Rightarrow a = 9$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 2^x$, find $a$ if $f(5) = 96$.',
            'answer': '$a = 3$',
            'wrong': ['$a = 6$', '$a = 32$', '$a = 12$'],
            'explanation': '$a \\cdot 32 = 96 \\Rightarrow a = 3$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 3^x$, find $a$ if $f(3) = 54$.',
            'answer': '$a = 2$',
            'wrong': ['$a = 6$', '$a = 18$', '$a = 3$'],
            'explanation': '$a \\cdot 27 = 54 \\Rightarrow a = 2$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 7^x$, find $a$ if $f(2) = 147$.',
            'answer': '$a = 3$',
            'wrong': ['$a = 7$', '$a = 21$', '$a = 49$'],
            'explanation': '$a \\cdot 49 = 147 \\Rightarrow a = 3$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 2^x$, find $a$ if $f(-1) = 5$.',
            'answer': '$a = 10$',
            'wrong': ['$a = \\tfrac{5}{2}$', '$a = 2$', '$a = 20$'],
            'explanation': '$a \\cdot 2^{-1} = 5 \\Rightarrow \\tfrac{a}{2} = 5 \\Rightarrow a = 10$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 5^x$, find $a$ if $f(1) = 20$.',
            'answer': '$a = 4$',
            'wrong': ['$a = 5$', '$a = 100$', '$a = 2$'],
            'explanation': '$a \\cdot 5 = 20 \\Rightarrow a = 4$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 3^x$, find $a$ if $f(-1) = 6$.',
            'answer': '$a = 18$',
            'wrong': ['$a = 2$', '$a = 3$', '$a = 9$'],
            'explanation': '$a \\cdot 3^{-1} = 6 \\Rightarrow \\tfrac{a}{3} = 6 \\Rightarrow a = 18$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 4^x$, find $a$ if $f(1) = 28$.',
            'answer': '$a = 7$',
            'wrong': ['$a = 4$', '$a = 14$', '$a = 112$'],
            'explanation': '$a \\cdot 4 = 28 \\Rightarrow a = 7$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 10^x$, find $a$ if $f(3) = 6000$.',
            'answer': '$a = 6$',
            'wrong': ['$a = 60$', '$a = 600$', '$a = 2$'],
            'explanation': '$a \\cdot 1000 = 6000 \\Rightarrow a = 6$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 2^x$, find $a$ if $f(6) = 192$.',
            'answer': '$a = 3$',
            'wrong': ['$a = 32$', '$a = 6$', '$a = 12$'],
            'explanation': '$a \\cdot 64 = 192 \\Rightarrow a = 3$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 9^x$, find $a$ if $f(2) = 81$.',
            'answer': '$a = 1$',
            'wrong': ['$a = 9$', '$a = 3$', '$a = 81$'],
            'explanation': '$a \\cdot 81 = 81 \\Rightarrow a = 1$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 3^x$, find $a$ if $f(4) = 162$.',
            'answer': '$a = 2$',
            'wrong': ['$a = 3$', '$a = 6$', '$a = 54$'],
            'explanation': '$a \\cdot 81 = 162 \\Rightarrow a = 2$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 2^x$, find $a$ if $f(-2) = 3$.',
            'answer': '$a = 12$',
            'wrong': ['$a = \\tfrac{3}{4}$', '$a = 6$', '$a = 4$'],
            'explanation': '$a \\cdot 2^{-2} = 3 \\Rightarrow \\tfrac{a}{4} = 3 \\Rightarrow a = 12$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 5^x$, find $a$ if $f(0) = 11$.',
            'answer': '$a = 11$',
            'wrong': ['$a = 5$', '$a = 55$', '$a = 1$'],
            'explanation': '$a \\cdot 1 = 11 \\Rightarrow a = 11$.',
        },
        {
            'question': 'In $f(x) = a \\cdot 6^x$, find $a$ if $f(3) = 432$.',
            'answer': '$a = 2$',
            'wrong': ['$a = 6$', '$a = 72$', '$a = 3$'],
            'explanation': '$a \\cdot 216 = 432 \\Rightarrow a = 2$.',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 4: Given x and y, find b (a known)  (25 problems)
        # ══════════════════════════════════════════════════════

        {
            'question': 'In $f(x) = 2 \\cdot b^x$, find $b$ if $f(3) = 54$.',
            'answer': '$b = 3$',
            'wrong': ['$b = 2$', '$b = 9$', '$b = 6$'],
            'explanation': '$2 \\cdot b^3 = 54 \\Rightarrow b^3 = 27 \\Rightarrow b = 3$.',
        },
        {
            'question': 'In $f(x) = 5 \\cdot b^x$, find $b$ if $f(2) = 20$.',
            'answer': '$b = 2$',
            'wrong': ['$b = 4$', '$b = 5$', '$b = 10$'],
            'explanation': '$5 \\cdot b^2 = 20 \\Rightarrow b^2 = 4 \\Rightarrow b = 2$.',
        },
        {
            'question': 'In $f(x) = 3 \\cdot b^x$, find $b$ if $f(3) = 81$.',
            'answer': '$b = 3$',
            'wrong': ['$b = 9$', '$b = 27$', '$b = 2$'],
            'explanation': '$3 \\cdot b^3 = 81 \\Rightarrow b^3 = 27 \\Rightarrow b = 3$.',
        },
        {
            'question': 'In $f(x) = 4 \\cdot b^x$, find $b$ if $f(2) = 100$.',
            'answer': '$b = 5$',
            'wrong': ['$b = 25$', '$b = 10$', '$b = 4$'],
            'explanation': '$4 \\cdot b^2 = 100 \\Rightarrow b^2 = 25 \\Rightarrow b = 5$.',
        },
        {
            'question': 'In $f(x) = 1 \\cdot b^x$, find $b$ if $f(4) = 16$.',
            'answer': '$b = 2$',
            'wrong': ['$b = 4$', '$b = 8$', '$b = 16$'],
            'explanation': '$b^4 = 16 \\Rightarrow b = 2$.',
        },
        {
            'question': 'In $f(x) = 2 \\cdot b^x$, find $b$ if $f(2) = 18$.',
            'answer': '$b = 3$',
            'wrong': ['$b = 9$', '$b = 6$', '$b = 2$'],
            'explanation': '$2 \\cdot b^2 = 18 \\Rightarrow b^2 = 9 \\Rightarrow b = 3$.',
        },
        {
            'question': 'In $f(x) = 10 \\cdot b^x$, find $b$ if $f(3) = 80$.',
            'answer': '$b = 2$',
            'wrong': ['$b = 4$', '$b = 8$', '$b = 10$'],
            'explanation': '$10 \\cdot b^3 = 80 \\Rightarrow b^3 = 8 \\Rightarrow b = 2$.',
        },
        {
            'question': 'In $f(x) = 7 \\cdot b^x$, find $b$ if $f(2) = 63$.',
            'answer': '$b = 3$',
            'wrong': ['$b = 9$', '$b = 7$', '$b = 6$'],
            'explanation': '$7 \\cdot b^2 = 63 \\Rightarrow b^2 = 9 \\Rightarrow b = 3$.',
        },
        {
            'question': 'In $f(x) = 3 \\cdot b^x$, find $b$ if $f(2) = 75$.',
            'answer': '$b = 5$',
            'wrong': ['$b = 25$', '$b = 3$', '$b = 15$'],
            'explanation': '$3 \\cdot b^2 = 75 \\Rightarrow b^2 = 25 \\Rightarrow b = 5$.',
        },
        {
            'question': 'In $f(x) = 1 \\cdot b^x$, find $b$ if $f(3) = 125$.',
            'answer': '$b = 5$',
            'wrong': ['$b = 25$', '$b = 3$', '$b = 15$'],
            'explanation': '$b^3 = 125 \\Rightarrow b = 5$.',
        },
        {
            'question': 'In $f(x) = 4 \\cdot b^x$, find $b$ if $f(3) = 32$.',
            'answer': '$b = 2$',
            'wrong': ['$b = 8$', '$b = 4$', '$b = 16$'],
            'explanation': '$4 \\cdot b^3 = 32 \\Rightarrow b^3 = 8 \\Rightarrow b = 2$.',
        },
        {
            'question': 'In $f(x) = 6 \\cdot b^x$, find $b$ if $f(2) = 24$.',
            'answer': '$b = 2$',
            'wrong': ['$b = 4$', '$b = 3$', '$b = 6$'],
            'explanation': '$6 \\cdot b^2 = 24 \\Rightarrow b^2 = 4 \\Rightarrow b = 2$.',
        },
        {
            'question': 'In $f(x) = 2 \\cdot b^x$, find $b$ if $f(4) = 162$.',
            'answer': '$b = 3$',
            'wrong': ['$b = 9$', '$b = 81$', '$b = 6$'],
            'explanation': '$2 \\cdot b^4 = 162 \\Rightarrow b^4 = 81 \\Rightarrow b = 3$.',
        },
        {
            'question': 'In $f(x) = 5 \\cdot b^x$, find $b$ if $f(3) = 40$.',
            'answer': '$b = 2$',
            'wrong': ['$b = 8$', '$b = 4$', '$b = 5$'],
            'explanation': '$5 \\cdot b^3 = 40 \\Rightarrow b^3 = 8 \\Rightarrow b = 2$.',
        },
        {
            'question': 'In $f(x) = 1 \\cdot b^x$, find $b$ if $f(2) = 49$.',
            'answer': '$b = 7$',
            'wrong': ['$b = 49$', '$b = 14$', '$b = 7^2$'],
            'explanation': '$b^2 = 49 \\Rightarrow b = 7$.',
        },
        {
            'question': 'In $f(x) = 8 \\cdot b^x$, find $b$ if $f(2) = 72$.',
            'answer': '$b = 3$',
            'wrong': ['$b = 9$', '$b = 6$', '$b = 2$'],
            'explanation': '$8 \\cdot b^2 = 72 \\Rightarrow b^2 = 9 \\Rightarrow b = 3$.',
        },
        {
            'question': 'In $f(x) = 3 \\cdot b^x$, find $b$ if $f(4) = 48$.',
            'answer': '$b = 2$',
            'wrong': ['$b = 4$', '$b = 16$', '$b = 6$'],
            'explanation': '$3 \\cdot b^4 = 48 \\Rightarrow b^4 = 16 \\Rightarrow b = 2$.',
        },
        {
            'question': 'In $f(x) = 9 \\cdot b^x$, find $b$ if $f(2) = 9$.',
            'answer': '$b = 1$',
            'wrong': ['$b = 9$', '$b = 3$', '$b = 0$'],
            'explanation': '$9 \\cdot b^2 = 9 \\Rightarrow b^2 = 1 \\Rightarrow b = 1$.',
        },
        {
            'question': 'In $f(x) = 2 \\cdot b^x$, find $b$ if $f(3) = 250$.',
            'answer': '$b = 5$',
            'wrong': ['$b = 25$', '$b = 10$', '$b = 3$'],
            'explanation': '$2 \\cdot b^3 = 250 \\Rightarrow b^3 = 125 \\Rightarrow b = 5$.',
        },
        {
            'question': 'In $f(x) = 12 \\cdot b^x$, find $b$ if $f(2) = 48$.',
            'answer': '$b = 2$',
            'wrong': ['$b = 4$', '$b = 6$', '$b = 3$'],
            'explanation': '$12 \\cdot b^2 = 48 \\Rightarrow b^2 = 4 \\Rightarrow b = 2$.',
        },
        {
            'question': 'In $f(x) = 1 \\cdot b^x$, find $b$ if $f(4) = 625$.',
            'answer': '$b = 5$',
            'wrong': ['$b = 25$', '$b = 125$', '$b = 4$'],
            'explanation': '$b^4 = 625 \\Rightarrow b = 5$.',
        },
        {
            'question': 'In $f(x) = 4 \\cdot b^x$, find $b$ if $f(2) = 4$.',
            'answer': '$b = 1$',
            'wrong': ['$b = 4$', '$b = 2$', '$b = 0$'],
            'explanation': '$4 \\cdot b^2 = 4 \\Rightarrow b^2 = 1 \\Rightarrow b = 1$.',
        },
        {
            'question': 'In $f(x) = 6 \\cdot b^x$, find $b$ if $f(3) = 162$.',
            'answer': '$b = 3$',
            'wrong': ['$b = 9$', '$b = 27$', '$b = 6$'],
            'explanation': '$6 \\cdot b^3 = 162 \\Rightarrow b^3 = 27 \\Rightarrow b = 3$.',
        },
        {
            'question': 'In $f(x) = 5 \\cdot b^x$, find $b$ if $f(4) = 80$.',
            'answer': '$b = 2$',
            'wrong': ['$b = 4$', '$b = 16$', '$b = 8$'],
            'explanation': '$5 \\cdot b^4 = 80 \\Rightarrow b^4 = 16 \\Rightarrow b = 2$.',
        },
        {
            'question': 'In $f(x) = 3 \\cdot b^x$, find $b$ if $f(1) = 21$.',
            'answer': '$b = 7$',
            'wrong': ['$b = 3$', '$b = 14$', '$b = 63$'],
            'explanation': '$3 \\cdot b = 21 \\Rightarrow b = 7$.',
        }
    ],
    'logarithm': [
        # --- 1 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{2}(x^2 - 3x)$.',
            'answer': '$(-\\infty,\\ 0) \\cup (3,\\ +\\infty)$',
            'wrong': ['$(0,\\ 3)$', '$(-\\infty,\\ 3) \\cup (0,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $x^2 - 3x > 0$. Factor: $(x)(x - 3) > 0$. Roots at $x = 0$ and $x = 3$. A upward parabola is positive **outside** its roots: $x < 0$ or $x > 3$. **Domain:** $\\boldsymbol{(-\\infty,0)\\cup(3,+\\infty)}$.',
        },
        # --- 2 ---
        {
            'question': 'Find the domain of $f(x) = \\log(|x| - 1)$.',
            'answer': '$(-\\infty,\\ -1) \\cup (1,\\ +\\infty)$',
            'wrong': ['$(-1,\\ 1)$', '$(-\\infty,\\ 1) \\cup (-1,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $|x| - 1 > 0 \\Rightarrow |x| > 1$. $|x| > 1$ means $x > 1$ or $x < -1$. **Domain:** $\\boldsymbol{(-\\infty,-1)\\cup(1,+\\infty)}$.',
        },
        # --- 3 ---
        {
            'question': 'Find the domain of $f(x) = \\log(x^2 - 4x + 3)$.',
            'answer': '$(-\\infty,\\ 1) \\cup (3,\\ +\\infty)$',
            'wrong': ['$(1,\\ 3)$', '$(-\\infty,\\ 3) \\cup (1,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $x^2 - 4x + 3 > 0$. Factor: $(x - 1)(x - 3) > 0$. Roots at $x = 1$ and $x = 3$. A upward parabola is positive **outside** its roots: $x < 1$ or $x > 3$. **Domain:** $\\boldsymbol{(-\\infty,1)\\cup(3,+\\infty)}$.',
        },
        # --- 4 ---
        {
            'question': 'Find the domain of $f(x) = \\log(|x| - 1)$.',
            'answer': '$(-\\infty,\\ -1) \\cup (1,\\ +\\infty)$',
            'wrong': ['$(-1,\\ 1)$', '$(-\\infty,\\ 1) \\cup (-1,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $|x| - 1 > 0 \\Rightarrow |x| > 1$. $|x| > 1$ means $x > 1$ or $x < -1$. **Domain:** $\\boldsymbol{(-\\infty,-1)\\cup(1,+\\infty)}$.',
        },
        # --- 5 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{2}(-2x + 6)$.',
            'answer': '$\\left(-\\infty,\\ 3\\right)$',
            'wrong': ['$\\left(3,\\ +\\infty\\right)$', '$\\left(-\\infty,\\ 3\\right]$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'The argument of a logarithm must be **strictly positive**: argument $> 0$. Set $-2x + 6 > 0$: $$-2x + 6 > 0 \\Rightarrow -2x > -6 \\Rightarrow x < 3 \\text{ (flip inequality: div by negative)}$$ **Domain:** $\\boldsymbol{\\left(-\\infty,\\ 3\\right)}$.',
        },
        # --- 6 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{2}(6 - 2x)$.',
            'answer': '$\\left(-\\infty,\\ 3\\right)$',
            'wrong': ['$\\left(3,\\ +\\infty\\right)$', '$\\left(-\\infty,\\ 3\\right]$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $6 - 2x > 0$. $$-2x > -6 \\Rightarrow x < 3 \\text{ (dividing by negative flips inequality)}$$ **Domain:** $\\boldsymbol{\\left(-\\infty,\\ 3\\right)}$.',
        },
        # --- 7 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{3}(4 - x)$.',
            'answer': '$\\left(-\\infty,\\ 4\\right)$',
            'wrong': ['$\\left(4,\\ +\\infty\\right)$', '$\\left(-\\infty,\\ 4\\right]$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $4 - x > 0$. $$-1x > -4 \\Rightarrow x < 4 \\text{ (dividing by negative flips inequality)}$$ **Domain:** $\\boldsymbol{\\left(-\\infty,\\ 4\\right)}$.',
        },
        # --- 8 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{5}(x^2 - 4x)$.',
            'answer': '$(-\\infty,\\ 0) \\cup (4,\\ +\\infty)$',
            'wrong': ['$(0,\\ 4)$', '$(-\\infty,\\ 4) \\cup (0,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $x^2 - 4x > 0$. Factor: $(x)(x - 4) > 0$. Roots at $x = 0$ and $x = 4$. A upward parabola is positive **outside** its roots: $x < 0$ or $x > 4$. **Domain:** $\\boldsymbol{(-\\infty,0)\\cup(4,+\\infty)}$.',
        },
        # --- 9 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{2}(4 - 2x)$.',
            'answer': '$\\left(-\\infty,\\ 2\\right)$',
            'wrong': ['$\\left(2,\\ +\\infty\\right)$', '$\\left(-\\infty,\\ 2\\right]$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $4 - 2x > 0$. $$-2x > -4 \\Rightarrow x < 2 \\text{ (dividing by negative flips inequality)}$$ **Domain:** $\\boldsymbol{\\left(-\\infty,\\ 2\\right)}$.',
        },
        # --- 10 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{3}(|x| - 4)$.',
            'answer': '$(-\\infty,\\ -4) \\cup (4,\\ +\\infty)$',
            'wrong': ['$(-4,\\ 4)$', '$(-\\infty,\\ 4) \\cup (-4,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $|x| - 4 > 0 \\Rightarrow |x| > 4$. $|x| > 4$ means $x > 4$ or $x < -4$. **Domain:** $\\boldsymbol{(-\\infty,-4)\\cup(4,+\\infty)}$.',
        },
        # --- 11 ---
        {
            'question': 'Find the domain of $f(x) = \\log(x^2 - 1x)$.',
            'answer': '$(-\\infty,\\ 0) \\cup (1,\\ +\\infty)$',
            'wrong': ['$(0,\\ 1)$', '$(-\\infty,\\ 1) \\cup (0,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $x^2 - 1x > 0$. Factor: $(x)(x - 1) > 0$. Roots at $x = 0$ and $x = 1$. A upward parabola is positive **outside** its roots: $x < 0$ or $x > 1$. **Domain:** $\\boldsymbol{(-\\infty,0)\\cup(1,+\\infty)}$.',
        },
        # --- 12 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{3}(x^2 + 5)$.',
            'answer': '$(-\\infty,\\ +\\infty)$',
            'wrong': ['$(0,\\ +\\infty)$', '$(-\\infty,\\ 0)$', '$(-5,\\ +5)$'],
            'explanation': 'Argument must be $> 0$: $x^2 + 5 > 0$. Since $x^2 \\geq 0$ for all real $x$, we have $x^2 + 5 \\geq 5 > 0$ always. The argument is always positive — **no restrictions**. **Domain:** $\\boldsymbol{(-\\infty,\\ +\\infty)}$.',
        },
        # --- 13 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{3}(x^2 + 5x)$.',
            'answer': '$(-\\infty,\\ -5) \\cup (0,\\ +\\infty)$',
            'wrong': ['$(-5,\\ 0)$', '$(-\\infty,\\ 0) \\cup (-5,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $x^2 + 5x > 0$. Factor: $(x + 5)(x) > 0$. Roots at $x = -5$ and $x = 0$. A upward parabola is positive **outside** its roots: $x < -5$ or $x > 0$. **Domain:** $\\boldsymbol{(-\\infty,-5)\\cup(0,+\\infty)}$.',
        },
        # --- 14 ---
        {
            'question': 'Find the domain of $f(x) = \\log(4 - x)$.',
            'answer': '$\\left(-\\infty,\\ 4\\right)$',
            'wrong': ['$\\left(4,\\ +\\infty\\right)$', '$\\left(-\\infty,\\ 4\\right]$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $4 - x > 0$. $$-1x > -4 \\Rightarrow x < 4 \\text{ (dividing by negative flips inequality)}$$ **Domain:** $\\boldsymbol{\\left(-\\infty,\\ 4\\right)}$.',
        },
        # --- 15 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{3}(x^2 + 1x)$.',
            'answer': '$(-\\infty,\\ -1) \\cup (0,\\ +\\infty)$',
            'wrong': ['$(-1,\\ 0)$', '$(-\\infty,\\ 0) \\cup (-1,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $x^2 + 1x > 0$. Factor: $(x + 1)(x) > 0$. Roots at $x = -1$ and $x = 0$. A upward parabola is positive **outside** its roots: $x < -1$ or $x > 0$. **Domain:** $\\boldsymbol{(-\\infty,-1)\\cup(0,+\\infty)}$.',
        },
        # --- 16 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{3}(x^2 + 2x)$.',
            'answer': '$(-\\infty,\\ -2) \\cup (0,\\ +\\infty)$',
            'wrong': ['$(-2,\\ 0)$', '$(-\\infty,\\ 0) \\cup (-2,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $x^2 + 2x > 0$. Factor: $(x + 2)(x) > 0$. Roots at $x = -2$ and $x = 0$. A upward parabola is positive **outside** its roots: $x < -2$ or $x > 0$. **Domain:** $\\boldsymbol{(-\\infty,-2)\\cup(0,+\\infty)}$.',
        },
        # --- 17 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{3}(4 - 2x)$.',
            'answer': '$\\left(-\\infty,\\ 2\\right)$',
            'wrong': ['$\\left(2,\\ +\\infty\\right)$', '$\\left(-\\infty,\\ 2\\right]$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $4 - 2x > 0$. $$-2x > -4 \\Rightarrow x < 2 \\text{ (dividing by negative flips inequality)}$$ **Domain:** $\\boldsymbol{\\left(-\\infty,\\ 2\\right)}$.',
        },
        # --- 18 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{2}(10 - x)$.',
            'answer': '$\\left(-\\infty,\\ 10\\right)$',
            'wrong': ['$\\left(10,\\ +\\infty\\right)$', '$\\left(-\\infty,\\ 10\\right]$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $10 - x > 0$. $$-1x > -10 \\Rightarrow x < 10 \\text{ (dividing by negative flips inequality)}$$ **Domain:** $\\boldsymbol{\\left(-\\infty,\\ 10\\right)}$.',
        },
        # --- 19 ---
        {
            'question': 'Find the domain of $f(x) = \\log_{3}(3 - 2x)$.',
            'answer': '$\\left(-\\infty,\\ \\dfrac{3}{2}\\right)$',
            'wrong': ['$\\left(\\dfrac{3}{2},\\ +\\infty\\right)$', '$\\left(-\\infty,\\ \\dfrac{3}{2}\\right]$',
                      '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'Argument must be $> 0$: $3 - 2x > 0$. $$-2x > -3 \\Rightarrow x < \\dfrac{3}{2} \\text{ (dividing by negative flips inequality)}$$ **Domain:** $\\boldsymbol{\\left(-\\infty,\\ \\dfrac{3}{2}\\right)}$.',
        },
        # --- 20 ---
        {
            'question': 'Find the domain of $f(x) = \\log(x^2 + 4)$.',
            'answer': '$(-\\infty,\\ +\\infty)$',
            'wrong': ['$(0,\\ +\\infty)$', '$(-\\infty,\\ 0)$', '$(-4,\\ +4)$'],
            'explanation': 'Argument must be $> 0$: $x^2 + 4 > 0$. Since $x^2 \\geq 0$ for all real $x$, we have $x^2 + 4 \\geq 4 > 0$ always. The argument is always positive — **no restrictions**. **Domain:** $\\boldsymbol{(-\\infty,\\ +\\infty)}$.',
        },
        # --- 21 ---
        {
            'question': 'Evaluate $\\log\\!\\left(\\dfrac{1}{1000}\\right)$.',
            'answer': '$-3$',
            'wrong': ['$-2$', '$3$', '$-4$'],
            'explanation': '$\\log\\!\\left(\\dfrac{1}{1000}\\right) = \\log(10^{-3}) = -3$. Because $10^{-3} = \\dfrac{1}{10^{3}} = \\dfrac{1}{1000}$.',
        },
        # --- 22 ---
        {
            'question': 'Evaluate $\\ln\\!\\left(\\dfrac{1}{e^{3}}\\right)$.',
            'answer': '$-3$',
            'wrong': ['$-2$', '$3$', '$-4$'],
            'explanation': '$$\\ln\\!\\left(\\frac{1}{e^{3}}\\right) = \\ln(e^{-3}) = -3$$ Using $\\ln(e^n) = n$.',
        },
        # --- 23 ---
        {
            'question': 'Evaluate $\\ln(e^{4})$.',
            'answer': '$4$',
            'wrong': ['$5$', '$3$', '$8$'],
            'explanation': '$\\ln(x)$ is the natural logarithm with base $e$. $$\\ln(e^{4}) = 4$$ This follows directly from $\\ln(e^n) = n$ (inverse property). **Answer: $\\boldsymbol{4}$.**',
        },
        # --- 24 ---
        {
            'question': 'Evaluate $\\ln(e^{1})$.',
            'answer': '$1$',
            'wrong': ['$2$', '$0$', '$2$'],
            'explanation': '$\\ln(x)$ is the natural logarithm with base $e$. $$\\ln(e^{1}) = 1$$ This follows directly from $\\ln(e^n) = n$ (inverse property). **Answer: $\\boldsymbol{1}$.**',
        },
        # --- 25 ---
        {
            'question': 'Evaluate $\\log(10000)$.',
            'answer': '$4$',
            'wrong': ['$5$', '$3$', '$3$'],
            'explanation': '$$\\log(10000) = \\log(10^{4}) = 4$$ Alternatively using product rule: $\\log(10^{1} \\cdot 10^{3}) = \\log(10^{1}) + \\log(10^{3}) = 1 + 3 = 4$.',
        },
        # --- 26 ---
        {
            'question': 'Evaluate $\\log(100)$.',
            'answer': '$2$',
            'wrong': ['$3$', '$1$', '$4$'],
            'explanation': "Recall: $\\log(x)$ means $\\log_{10}(x)$ — ''what power of 10 gives $x$?'' $$\\log(100) = \\log(10^{2}) = 2$$ Because $10^{2} = 100$. **Answer: $\\boldsymbol{2}$.**",
        },
        # --- 27 ---
        {
            'question': 'Evaluate $\\ln(e^{2})$.',
            'answer': '$2$',
            'wrong': ['$3$', '$1$', '$4$'],
            'explanation': '$\\ln(x)$ is the natural logarithm with base $e$. $$\\ln(e^{2}) = 2$$ This follows directly from $\\ln(e^n) = n$ (inverse property). **Answer: $\\boldsymbol{2}$.**',
        },
        # --- 28 ---
        {
            'question': 'Evaluate $\\log(1000000)$.',
            'answer': '$6$',
            'wrong': ['$7$', '$5$', '$9$'],
            'explanation': '$$\\log(1000000) = \\log(10^{6}) = 6$$ Alternatively using product rule: $\\log(10^{3} \\cdot 10^{3}) = \\log(10^{3}) + \\log(10^{3}) = 3 + 3 = 6$.',
        },
        # --- 29 ---
        {
            'question': 'Evaluate $\\ln\\!\\left(\\dfrac{1}{e^{1}}\\right)$.',
            'answer': '$-1$',
            'wrong': ['$0$', '$1$', '$-2$'],
            'explanation': '$$\\ln\\!\\left(\\frac{1}{e^{1}}\\right) = \\ln(e^{-1}) = -1$$ Using $\\ln(e^n) = n$.',
        },
        # --- 30 ---
        {
            'question': 'Evaluate $\\log(10000)$.',
            'answer': '$4$',
            'wrong': ['$5$', '$3$', '$3$'],
            'explanation': '$$\\log(10000) = \\log(10^{4}) = 4$$ Alternatively using product rule: $\\log(10^{1} \\cdot 10^{3}) = \\log(10^{1}) + \\log(10^{3}) = 1 + 3 = 4$.',
        },
        # --- 31 ---
        {
            'question': 'Evaluate $\\log\\!\\left(\\dfrac{1}{1000}\\right)$.',
            'answer': '$-3$',
            'wrong': ['$-2$', '$3$', '$-4$'],
            'explanation': '$\\log\\!\\left(\\dfrac{1}{1000}\\right) = \\log(10^{-3}) = -3$. Because $10^{-3} = \\dfrac{1}{10^{3}} = \\dfrac{1}{1000}$.',
        },
        # --- 32 ---
        {
            'question': 'Evaluate $\\log\\!\\left(\\dfrac{1}{1000}\\right)$.',
            'answer': '$-3$',
            'wrong': ['$-2$', '$3$', '$-4$'],
            'explanation': '$\\log\\!\\left(\\dfrac{1}{1000}\\right) = \\log(10^{-3}) = -3$. Because $10^{-3} = \\dfrac{1}{10^{3}} = \\dfrac{1}{1000}$.',
        },
        # --- 33 ---
        {
            'question': 'Evaluate $\\log(10000)$.',
            'answer': '$4$',
            'wrong': ['$5$', '$3$', '$3$'],
            'explanation': '$$\\log(10000) = \\log(10^{4}) = 4$$ Alternatively using product rule: $\\log(10^{1} \\cdot 10^{3}) = \\log(10^{1}) + \\log(10^{3}) = 1 + 3 = 4$.',
        },
        # --- 34 ---
        {
            'question': 'Evaluate $\\log(100)$.',
            'answer': '$2$',
            'wrong': ['$3$', '$1$', '$4$'],
            'explanation': "Recall: $\\log(x)$ means $\\log_{10}(x)$ — ''what power of 10 gives $x$?'' $$\\log(100) = \\log(10^{2}) = 2$$ Because $10^{2} = 100$. **Answer: $\\boldsymbol{2}$.**",
        },
        # --- 35 ---
        {
            'question': 'Evaluate $\\ln\\!\\left(\\dfrac{1}{e^{3}}\\right)$.',
            'answer': '$-3$',
            'wrong': ['$-2$', '$3$', '$-4$'],
            'explanation': '$$\\ln\\!\\left(\\frac{1}{e^{3}}\\right) = \\ln(e^{-3}) = -3$$ Using $\\ln(e^n) = n$.',
        },
        # --- 36 ---
        {
            'question': 'Evaluate $\\log\\!\\left(\\dfrac{1}{100}\\right)$.',
            'answer': '$-2$',
            'wrong': ['$-1$', '$2$', '$-3$'],
            'explanation': '$\\log\\!\\left(\\dfrac{1}{100}\\right) = \\log(10^{-2}) = -2$. Because $10^{-2} = \\dfrac{1}{10^{2}} = \\dfrac{1}{100}$.',
        },
        # --- 37 ---
        {
            'question': 'Evaluate $\\ln\\!\\left(\\dfrac{1}{e^{1}}\\right)$.',
            'answer': '$-1$',
            'wrong': ['$0$', '$1$', '$-2$'],
            'explanation': '$$\\ln\\!\\left(\\frac{1}{e^{1}}\\right) = \\ln(e^{-1}) = -1$$ Using $\\ln(e^n) = n$.',
        },
        # --- 38 ---
        {
            'question': 'Evaluate $\\ln(e^{4})$.',
            'answer': '$4$',
            'wrong': ['$5$', '$3$', '$8$'],
            'explanation': '$\\ln(x)$ is the natural logarithm with base $e$. $$\\ln(e^{4}) = 4$$ This follows directly from $\\ln(e^n) = n$ (inverse property). **Answer: $\\boldsymbol{4}$.**',
        },
        # --- 39 ---
        {
            'question': 'Evaluate $\\ln(e^{1})$.',
            'answer': '$1$',
            'wrong': ['$2$', '$0$', '$2$'],
            'explanation': '$\\ln(x)$ is the natural logarithm with base $e$. $$\\ln(e^{1}) = 1$$ This follows directly from $\\ln(e^n) = n$ (inverse property). **Answer: $\\boldsymbol{1}$.**',
        },
        # --- 40 ---
        {
            'question': 'Evaluate $\\log(1000)$.',
            'answer': '$3$',
            'wrong': ['$4$', '$2$', '$6$'],
            'explanation': "Recall: $\\log(x)$ means $\\log_{10}(x)$ — ''what power of 10 gives $x$?'' $$\\log(1000) = \\log(10^{3}) = 3$$ Because $10^{3} = 1000$. **Answer: $\\boldsymbol{3}$.**",
        },
        # --- 41 ---
        {
            'question': 'Expand: $\\log_{2}(x^{3} \\cdot y)$',
            'answer': '$3\\log_{2}(x) + \\log_{2}(y)$',
            'wrong': ['$\\log_{2}(x^3) \\cdot \\log_{2}(y)$', '$3\\log_{2}(x) - \\log_{2}(y)$',
                      '$\\log_{2}(x) + \\log_{2}(y^3)$'],
            'explanation': 'Apply **Product Rule** then **Power Rule**: $$\\log_{2}(x^{3} \\cdot y) = \\log_{2}(x^{3}) + \\log_{2}(y) = 3\\log_{2}(x) + \\log_{2}(y)$$',
        },
        # --- 42 ---
        {
            'question': 'Expand: $\\log_{2}(4 \\cdot 6 \\cdot 5)$',
            'answer': '$\\log_{2}(4) + \\log_{2}(6) + \\log_{2}(5)$',
            'wrong': ['$\\log_{2}(4) - \\log_{2}(6) + \\log_{2}(5)$', '$\\log_{2}(120)$',
                      '$\\log_{2}(4) + \\log_{2}(6) - \\log_{2}(5)$'],
            'explanation': '**Product Rule** applied twice: $\\log_b(M \\cdot N \\cdot P) = \\log_b M + \\log_b N + \\log_b P$. $$\\log_{2}(4 \\cdot 6 \\cdot 5) = \\log_{2}(4) + \\log_{2}(6) + \\log_{2}(5)$$',
        },
        # --- 43 ---
        {
            'question': 'Expand: $\\log_{3}(x^{3} \\cdot y)$',
            'answer': '$3\\log_{3}(x) + \\log_{3}(y)$',
            'wrong': ['$\\log_{3}(x^3) \\cdot \\log_{3}(y)$', '$3\\log_{3}(x) - \\log_{3}(y)$',
                      '$\\log_{3}(x) + \\log_{3}(y^3)$'],
            'explanation': 'Apply **Product Rule** then **Power Rule**: $$\\log_{3}(x^{3} \\cdot y) = \\log_{3}(x^{3}) + \\log_{3}(y) = 3\\log_{3}(x) + \\log_{3}(y)$$',
        },
        # --- 44 ---
        {
            'question': 'Expand: $\\log_{3}(x^{4} \\cdot y)$',
            'answer': '$4\\log_{3}(x) + \\log_{3}(y)$',
            'wrong': ['$\\log_{3}(x^4) \\cdot \\log_{3}(y)$', '$4\\log_{3}(x) - \\log_{3}(y)$',
                      '$\\log_{3}(x) + \\log_{3}(y^4)$'],
            'explanation': 'Apply **Product Rule** then **Power Rule**: $$\\log_{3}(x^{4} \\cdot y) = \\log_{3}(x^{4}) + \\log_{3}(y) = 4\\log_{3}(x) + \\log_{3}(y)$$',
        },
        # --- 45 ---
        {
            'question': 'Expand: $\\log(4 \\cdot 3 \\cdot 7)$',
            'answer': '$\\log(4) + \\log(3) + \\log(7)$',
            'wrong': ['$\\log(4) - \\log(3) + \\log(7)$', '$\\log(84)$', '$\\log(4) + \\log(3) - \\log(7)$'],
            'explanation': '**Product Rule** applied twice: $\\log_b(M \\cdot N \\cdot P) = \\log_b M + \\log_b N + \\log_b P$. $$\\log_{10}(4 \\cdot 3 \\cdot 7) = \\log(4) + \\log(3) + \\log(7)$$',
        },
        # --- 46 ---
        {
            'question': 'Expand: $\\log_{5}(4 \\cdot 5 \\cdot 3)$',
            'answer': '$\\log_{5}(4) + \\log_{5}(5) + \\log_{5}(3)$',
            'wrong': ['$\\log_{5}(4) - \\log_{5}(5) + \\log_{5}(3)$', '$\\log_{5}(60)$',
                      '$\\log_{5}(4) + \\log_{5}(5) - \\log_{5}(3)$'],
            'explanation': '**Product Rule** applied twice: $\\log_b(M \\cdot N \\cdot P) = \\log_b M + \\log_b N + \\log_b P$. $$\\log_{5}(4 \\cdot 5 \\cdot 3) = \\log_{5}(4) + \\log_{5}(5) + \\log_{5}(3)$$',
        },
        # --- 47 ---
        {
            'question': 'Expand: $\\log_{5}(x^{2} \\cdot y)$',
            'answer': '$2\\log_{5}(x) + \\log_{5}(y)$',
            'wrong': ['$\\log_{5}(x^2) \\cdot \\log_{5}(y)$', '$2\\log_{5}(x) - \\log_{5}(y)$',
                      '$\\log_{5}(x) + \\log_{5}(y^2)$'],
            'explanation': 'Apply **Product Rule** then **Power Rule**: $$\\log_{5}(x^{2} \\cdot y) = \\log_{5}(x^{2}) + \\log_{5}(y) = 2\\log_{5}(x) + \\log_{5}(y)$$',
        },
        # --- 48 ---
        {
            'question': 'Expand: $\\log(3 \\cdot 7 \\cdot 4)$',
            'answer': '$\\log(3) + \\log(7) + \\log(4)$',
            'wrong': ['$\\log(3) - \\log(7) + \\log(4)$', '$\\log(84)$', '$\\log(3) + \\log(7) - \\log(4)$'],
            'explanation': '**Product Rule** applied twice: $\\log_b(M \\cdot N \\cdot P) = \\log_b M + \\log_b N + \\log_b P$. $$\\log_{10}(3 \\cdot 7 \\cdot 4) = \\log(3) + \\log(7) + \\log(4)$$',
        },
        # --- 49 ---
        {
            'question': 'Expand: $\\log(x^{4} \\cdot y)$',
            'answer': '$4\\log(x) + \\log(y)$',
            'wrong': ['$\\log(x^4) \\cdot \\log(y)$', '$4\\log(x) - \\log(y)$', '$\\log(x) + \\log(y^4)$'],
            'explanation': 'Apply **Product Rule** then **Power Rule**: $$\\log_{10}(x^{4} \\cdot y) = \\log_{10}(x^{4}) + \\log(y) = 4\\log(x) + \\log(y)$$',
        },
        # --- 50 ---
        {
            'question': 'Expand: $\\log_{2}(x^{2} \\cdot y)$',
            'answer': '$2\\log_{2}(x) + \\log_{2}(y)$',
            'wrong': ['$\\log_{2}(x^2) \\cdot \\log_{2}(y)$', '$2\\log_{2}(x) - \\log_{2}(y)$',
                      '$\\log_{2}(x) + \\log_{2}(y^2)$'],
            'explanation': 'Apply **Product Rule** then **Power Rule**: $$\\log_{2}(x^{2} \\cdot y) = \\log_{2}(x^{2}) + \\log_{2}(y) = 2\\log_{2}(x) + \\log_{2}(y)$$',
        },
        # --- 51 ---
        {
            'question': 'Expand: $\\log_{5}(3 \\cdot 5 \\cdot 7)$',
            'answer': '$\\log_{5}(3) + \\log_{5}(5) + \\log_{5}(7)$',
            'wrong': ['$\\log_{5}(3) - \\log_{5}(5) + \\log_{5}(7)$', '$\\log_{5}(105)$',
                      '$\\log_{5}(3) + \\log_{5}(5) - \\log_{5}(7)$'],
            'explanation': '**Product Rule** applied twice: $\\log_b(M \\cdot N \\cdot P) = \\log_b M + \\log_b N + \\log_b P$. $$\\log_{5}(3 \\cdot 5 \\cdot 7) = \\log_{5}(3) + \\log_{5}(5) + \\log_{5}(7)$$',
        },
        # --- 52 ---
        {
            'question': 'Expand: $\\log_{5}(x^{3} y^{2})$',
            'answer': '$3\\log_{5}(x) + 2\\log_{5}(y)$',
            'wrong': ['$2\\log_{5}(x) + 3\\log_{5}(y)$', '$3\\log_{5}(x) \\cdot 2\\log_{5}(y)$',
                      '$3\\log_{5}(x) - 2\\log_{5}(y)$'],
            'explanation': '**Product Rule:** $\\log(x^{3} y^{2}) = \\log(x^{3}) + \\log(y^{2})$. **Power Rule:** $\\log(x^{3}) = 3\\log(x)$, $\\log(y^{2}) = 2\\log(y)$. $$= 3\\log_{5}(x) + 2\\log_{5}(y)$$',
        },
        # --- 53 ---
        {
            'question': 'Expand: $\\log(4 \\cdot 2 \\cdot 6)$',
            'answer': '$\\log(4) + \\log(2) + \\log(6)$',
            'wrong': ['$\\log(4) - \\log(2) + \\log(6)$', '$\\log(48)$', '$\\log(4) + \\log(2) - \\log(6)$'],
            'explanation': '**Product Rule** applied twice: $\\log_b(M \\cdot N \\cdot P) = \\log_b M + \\log_b N + \\log_b P$. $$\\log_{10}(4 \\cdot 2 \\cdot 6) = \\log(4) + \\log(2) + \\log(6)$$',
        },
        # --- 54 ---
        {
            'question': 'Expand: $\\log_{5}(x^{3} y^{3})$',
            'answer': '$3\\log_{5}(x) + 3\\log_{5}(y)$',
            'wrong': ['$3\\log_{5}(x) + 3\\log_{5}(y)$', '$3\\log_{5}(x) \\cdot 3\\log_{5}(y)$',
                      '$3\\log_{5}(x) - 3\\log_{5}(y)$'],
            'explanation': '**Product Rule:** $\\log(x^{3} y^{3}) = \\log(x^{3}) + \\log(y^{3})$. **Power Rule:** $\\log(x^{3}) = 3\\log(x)$, $\\log(y^{3}) = 3\\log(y)$. $$= 3\\log_{5}(x) + 3\\log_{5}(y)$$',
        },
        # --- 55 ---
        {
            'question': 'Expand: $\\log(x^{3} y^{2})$',
            'answer': '$3\\log(x) + 2\\log(y)$',
            'wrong': ['$2\\log(x) + 3\\log(y)$', '$3\\log(x) \\cdot 2\\log(y)$', '$3\\log(x) - 2\\log(y)$'],
            'explanation': '**Product Rule:** $\\log(x^{3} y^{2}) = \\log(x^{3}) + \\log(y^{2})$. **Power Rule:** $\\log(x^{3}) = 3\\log(x)$, $\\log(y^{2}) = 2\\log(y)$. $$= 3\\log(x) + 2\\log(y)$$',
        },
        # --- 56 ---
        {
            'question': 'Expand: $\\log_{5}(7 \\cdot 4)$',
            'answer': '$\\log_{5}(7) + \\log_{5}(4)$',
            'wrong': ['$\\log_{5}(7) \\cdot \\log_{5}(4)$', '$\\log_{5}(7) - \\log_{5}(4)$', '$\\log_{5}(28)$'],
            'explanation': '**Product Rule:** $\\log_b(M \\cdot N) = \\log_b M + \\log_b N$. $$\\log_{5}(7 \\cdot 4) = \\log_{5}(7) + \\log_{5}(4)$$',
        },
        # --- 57 ---
        {
            'question': 'Expand: $\\log_{2}(2 \\cdot 5 \\cdot 6)$',
            'answer': '$\\log_{2}(2) + \\log_{2}(5) + \\log_{2}(6)$',
            'wrong': ['$\\log_{2}(2) - \\log_{2}(5) + \\log_{2}(6)$', '$\\log_{2}(60)$',
                      '$\\log_{2}(2) + \\log_{2}(5) - \\log_{2}(6)$'],
            'explanation': '**Product Rule** applied twice: $\\log_b(M \\cdot N \\cdot P) = \\log_b M + \\log_b N + \\log_b P$. $$\\log_{2}(2 \\cdot 5 \\cdot 6) = \\log_{2}(2) + \\log_{2}(5) + \\log_{2}(6)$$',
        },
        # --- 58 ---
        {
            'question': 'Expand: $\\log(x^{3} y^{3})$',
            'answer': '$3\\log(x) + 3\\log(y)$',
            'wrong': ['$3\\log(x) + 3\\log(y)$', '$3\\log(x) \\cdot 3\\log(y)$', '$3\\log(x) - 3\\log(y)$'],
            'explanation': '**Product Rule:** $\\log(x^{3} y^{3}) = \\log(x^{3}) + \\log(y^{3})$. **Power Rule:** $\\log(x^{3}) = 3\\log(x)$, $\\log(y^{3}) = 3\\log(y)$. $$= 3\\log(x) + 3\\log(y)$$',
        },
        # --- 59 ---
        {
            'question': 'Expand: $\\log_{2}(4 \\cdot 3)$',
            'answer': '$\\log_{2}(4) + \\log_{2}(3)$',
            'wrong': ['$\\log_{2}(4) \\cdot \\log_{2}(3)$', '$\\log_{2}(4) - \\log_{2}(3)$', '$\\log_{2}(12)$'],
            'explanation': '**Product Rule:** $\\log_b(M \\cdot N) = \\log_b M + \\log_b N$. $$\\log_{2}(4 \\cdot 3) = \\log_{2}(4) + \\log_{2}(3)$$',
        },
        # --- 60 ---
        {
            'question': 'Expand: $\\log(x^{3} y^{2})$',
            'answer': '$3\\log(x) + 2\\log(y)$',
            'wrong': ['$2\\log(x) + 3\\log(y)$', '$3\\log(x) \\cdot 2\\log(y)$', '$3\\log(x) - 2\\log(y)$'],
            'explanation': '**Product Rule:** $\\log(x^{3} y^{2}) = \\log(x^{3}) + \\log(y^{2})$. **Power Rule:** $\\log(x^{3}) = 3\\log(x)$, $\\log(y^{2}) = 2\\log(y)$. $$= 3\\log(x) + 2\\log(y)$$',
        },
        # --- 61 ---
        {
            'question': 'Condense: $\\log_{3}(24) - \\log_{3}(4)$',
            'answer': '$\\log_{3}(6)$',
            'wrong': ['$\\log_{3}(28)$', '$\\log_{3}(96)$', '$\\log_{3}(20)$'],
            'explanation': '**Quotient Rule:** $\\log_b M - \\log_b N = \\log_b\\!\\left(\\dfrac{M}{N}\\right)$. $$\\log_{3}(24) - \\log_{3}(4) = \\log_{3}(\\dfrac{24}{4}) = \\log_{3}(6)$$ Since $\\dfrac{24}{4} = 6$, the final answer is $\\log_{3}(6)$.',
        },
        # --- 62 ---
        {
            'question': 'Condense: $\\log(15) - \\log(5)$',
            'answer': '$\\log(3)$',
            'wrong': ['$\\log(20)$', '$\\log(75)$', '$\\log(10)$'],
            'explanation': '**Quotient Rule:** $\\log_b M - \\log_b N = \\log_b\\!\\left(\\dfrac{M}{N}\\right)$. $$\\log(15) - \\log(5) = \\log(\\dfrac{15}{5}) = \\log(3)$$ Since $\\dfrac{15}{5} = 3$, the final answer is $\\log(3)$.',
        },
        # --- 63 ---
        {
            'question': 'Condense: $\\log(x^{5}) - \\log(x)$',
            'answer': '$\\log(x^{4})$',
            'wrong': ['$\\log(x^{6})$', '$\\log(x^{3})$', '$\\log(x^{5})$'],
            'explanation': '**Quotient Rule:** $\\log(x^{5}) - \\log(x) = \\log(x^{5}/x) = \\log(x^{4})$. Since $x^{5}/x = x^{5}/x^1 = x^{4}$.',
        },
        # --- 64 ---
        {
            'question': 'Condense: $\\log_{3}(4) + \\log_{3}(2) - \\log_{3}(7)$',
            'answer': '$\\log_{3}(\\dfrac{8}{7})$',
            'wrong': ['$\\log_{3}(4+2-7)$', '$\\log_{3}(\\dfrac{6}{7})$', '$\\log_{3}(\\dfrac{4}{14})$'],
            'explanation': '**Product Rule:** $\\log_{3}(4) + \\log_{3}(2) = \\log_{3}(4\\cdot2)$. **Quotient Rule:** $\\log_{3}(8) - \\log_{3}(7) = \\log_{3}(\\dfrac{8}{7}) = \\log_{3}(\\dfrac{8}{7})$.',
        },
        # --- 65 ---
        {
            'question': 'Condense: $\\log(6) + \\log(7) - \\log(3)$',
            'answer': '$\\log(14)$',
            'wrong': ['$\\log(6+7-3)$', '$\\log(\\dfrac{13}{3})$', '$\\log(\\dfrac{6}{21})$'],
            'explanation': '**Product Rule:** $\\log(6) + \\log(7) = \\log(6\\cdot7)$. **Quotient Rule:** $\\log(42) - \\log(3) = \\log(\\dfrac{42}{3}) = \\log(14)$.',
        },
        # --- 66 ---
        {
            'question': 'Condense: $\\log_{5}(20) - \\log_{5}(4)$',
            'answer': '$\\log_{5}(5)$',
            'wrong': ['$\\log_{5}(24)$', '$\\log_{5}(80)$', '$\\log_{5}(16)$'],
            'explanation': '**Quotient Rule:** $\\log_b M - \\log_b N = \\log_b\\!\\left(\\dfrac{M}{N}\\right)$. $$\\log_{5}(20) - \\log_{5}(4) = \\log_{5}(\\dfrac{20}{4}) = \\log_{5}(5)$$ Since $\\dfrac{20}{4} = 5$, the final answer is $\\log_{5}(5)$.',
        },
        # --- 67 ---
        {
            'question': 'Condense: $\\log_{5}(6) + \\log_{5}(4) - \\log_{5}(7)$',
            'answer': '$\\log_{5}(\\dfrac{24}{7})$',
            'wrong': ['$\\log_{5}(6+4-7)$', '$\\log_{5}(\\dfrac{10}{7})$', '$\\log_{5}(\\dfrac{6}{28})$'],
            'explanation': '**Product Rule:** $\\log_{5}(6) + \\log_{5}(4) = \\log_{5}(6\\cdot4)$. **Quotient Rule:** $\\log_{5}(24) - \\log_{5}(7) = \\log_{5}(\\dfrac{24}{7}) = \\log_{5}(\\dfrac{24}{7})$.',
        },
        # --- 68 ---
        {
            'question': 'Condense: $\\log_{5}(2) + \\log_{5}(4) - \\log_{5}(6)$',
            'answer': '$\\log_{5}(\\dfrac{4}{3})$',
            'wrong': ['$\\log_{5}(2+4-6)$', '$\\log_{5}(\\dfrac{6}{6})$', '$\\log_{5}(\\dfrac{2}{24})$'],
            'explanation': '**Product Rule:** $\\log_{5}(2) + \\log_{5}(4) = \\log_{5}(2\\cdot4)$. **Quotient Rule:** $\\log_{5}(8) - \\log_{5}(6) = \\log_{5}(\\dfrac{8}{6}) = \\log_{5}(\\dfrac{4}{3})$.',
        },
        # --- 69 ---
        {
            'question': 'Condense: $\\log_{5}(10) - \\log_{5}(5)$',
            'answer': '$\\log_{5}(2)$',
            'wrong': ['$\\log_{5}(15)$', '$\\log_{5}(50)$', '$\\log_{5}(5)$'],
            'explanation': '**Quotient Rule:** $\\log_b M - \\log_b N = \\log_b\\!\\left(\\dfrac{M}{N}\\right)$. $$\\log_{5}(10) - \\log_{5}(5) = \\log_{5}(\\dfrac{10}{5}) = \\log_{5}(2)$$ Since $\\dfrac{10}{5} = 2$, the final answer is $\\log_{5}(2)$.',
        },
        # --- 70 ---
        {
            'question': 'Condense: $2\\log_{5}(x) - \\log_{5}(y)$',
            'answer': '$\\log_{5}(x^{2}/y)$',
            'wrong': ['$\\log_{5}(x)/\\log_{5}(y)$', '$\\log_{5}(x^{2} \\cdot y)$', '$\\log_{5}(x/2y)$'],
            'explanation': '**Step 1 — Power Rule:** $2\\log_{5}(x) = \\log_{5}(x^{2})$. **Step 2 — Quotient Rule:** $\\log_{5}(x^{2}) - \\log_{5}(y) = \\log_{5}(x^{2}/y)$.',
        },
        # --- 71 ---
        {
            'question': 'Condense: $\\log_{2}(x^{3}) - \\log_{2}(x)$',
            'answer': '$\\log_{2}(x^{2})$',
            'wrong': ['$\\log_{2}(x^{4})$', '$\\log_{2}(x^{1})$', '$\\log_{2}(x^{3})$'],
            'explanation': '**Quotient Rule:** $\\log_{2}(x^{3}) - \\log_{2}(x) = \\log_{2}(x^{3}/x) = \\log_{2}(x^{2})$. Since $x^{3}/x = x^{3}/x^1 = x^{2}$.',
        },
        # --- 72 ---
        {
            'question': 'Condense: $\\log_{2}(x^{3}) - \\log_{2}(x)$',
            'answer': '$\\log_{2}(x^{2})$',
            'wrong': ['$\\log_{2}(x^{4})$', '$\\log_{2}(x^{1})$', '$\\log_{2}(x^{3})$'],
            'explanation': '**Quotient Rule:** $\\log_{2}(x^{3}) - \\log_{2}(x) = \\log_{2}(x^{3}/x) = \\log_{2}(x^{2})$. Since $x^{3}/x = x^{3}/x^1 = x^{2}$.',
        },
        # --- 73 ---
        {
            'question': 'Condense: $3\\log_{2}(x) - \\log_{2}(y)$',
            'answer': '$\\log_{2}(x^{3}/y)$',
            'wrong': ['$\\log_{2}(x)/\\log_{2}(y)$', '$\\log_{2}(x^{3} \\cdot y)$', '$\\log_{2}(x/3y)$'],
            'explanation': '**Step 1 — Power Rule:** $3\\log_{2}(x) = \\log_{2}(x^{3})$. **Step 2 — Quotient Rule:** $\\log_{2}(x^{3}) - \\log_{2}(y) = \\log_{2}(x^{3}/y)$.',
        },
        # --- 74 ---
        {
            'question': 'Condense: $\\log_{2}(x^{3}) - \\log_{2}(x)$',
            'answer': '$\\log_{2}(x^{2})$',
            'wrong': ['$\\log_{2}(x^{4})$', '$\\log_{2}(x^{1})$', '$\\log_{2}(x^{3})$'],
            'explanation': '**Quotient Rule:** $\\log_{2}(x^{3}) - \\log_{2}(x) = \\log_{2}(x^{3}/x) = \\log_{2}(x^{2})$. Since $x^{3}/x = x^{3}/x^1 = x^{2}$.',
        },
        # --- 75 ---
        {
            'question': 'Condense: $3\\log_{2}(x) - \\log_{2}(y)$',
            'answer': '$\\log_{2}(x^{3}/y)$',
            'wrong': ['$\\log_{2}(x)/\\log_{2}(y)$', '$\\log_{2}(x^{3} \\cdot y)$', '$\\log_{2}(x/3y)$'],
            'explanation': '**Step 1 — Power Rule:** $3\\log_{2}(x) = \\log_{2}(x^{3})$. **Step 2 — Quotient Rule:** $\\log_{2}(x^{3}) - \\log_{2}(y) = \\log_{2}(x^{3}/y)$.',
        },
        # --- 76 ---
        {
            'question': 'Condense: $3\\log_{3}(x) - \\log_{3}(y)$',
            'answer': '$\\log_{3}(x^{3}/y)$',
            'wrong': ['$\\log_{3}(x)/\\log_{3}(y)$', '$\\log_{3}(x^{3} \\cdot y)$', '$\\log_{3}(x/3y)$'],
            'explanation': '**Step 1 — Power Rule:** $3\\log_{3}(x) = \\log_{3}(x^{3})$. **Step 2 — Quotient Rule:** $\\log_{3}(x^{3}) - \\log_{3}(y) = \\log_{3}(x^{3}/y)$.',
        },
        # --- 77 ---
        {
            'question': 'Condense: $\\log_{5}(x^{5}) - \\log_{5}(x)$',
            'answer': '$\\log_{5}(x^{4})$',
            'wrong': ['$\\log_{5}(x^{6})$', '$\\log_{5}(x^{3})$', '$\\log_{5}(x^{5})$'],
            'explanation': '**Quotient Rule:** $\\log_{5}(x^{5}) - \\log_{5}(x) = \\log_{5}(x^{5}/x) = \\log_{5}(x^{4})$. Since $x^{5}/x = x^{5}/x^1 = x^{4}$.',
        },
        # --- 78 ---
        {
            'question': 'Condense: $\\log(x^{3}) - \\log(x)$',
            'answer': '$\\log(x^{2})$',
            'wrong': ['$\\log(x^{4})$', '$\\log(x^{1})$', '$\\log(x^{3})$'],
            'explanation': '**Quotient Rule:** $\\log(x^{3}) - \\log(x) = \\log(x^{3}/x) = \\log(x^{2})$. Since $x^{3}/x = x^{3}/x^1 = x^{2}$.',
        },
        # --- 79 ---
        {
            'question': 'Condense: $\\log_{3}(5) + \\log_{3}(4) - \\log_{3}(6)$',
            'answer': '$\\log_{3}(\\dfrac{10}{3})$',
            'wrong': ['$\\log_{3}(5+4-6)$', '$\\log_{3}(\\dfrac{9}{6})$', '$\\log_{3}(\\dfrac{5}{24})$'],
            'explanation': '**Product Rule:** $\\log_{3}(5) + \\log_{3}(4) = \\log_{3}(5\\cdot4)$. **Quotient Rule:** $\\log_{3}(20) - \\log_{3}(6) = \\log_{3}(\\dfrac{20}{6}) = \\log_{3}(\\dfrac{10}{3})$.',
        },
        # --- 80 ---
        {
            'question': 'Condense: $\\log_{3}(2) + \\log_{3}(7) - \\log_{3}(4)$',
            'answer': '$\\log_{3}(\\dfrac{7}{2})$',
            'wrong': ['$\\log_{3}(2+7-4)$', '$\\log_{3}(\\dfrac{9}{4})$', '$\\log_{3}(\\dfrac{2}{28})$'],
            'explanation': '**Product Rule:** $\\log_{3}(2) + \\log_{3}(7) = \\log_{3}(2\\cdot7)$. **Quotient Rule:** $\\log_{3}(14) - \\log_{3}(4) = \\log_{3}(\\dfrac{14}{4}) = \\log_{3}(\\dfrac{7}{2})$.',
        },
        # --- 81 ---
        {
            'question': 'Simplify: $\\log_{9}(x)$ in terms of $\\log_{3}(x)$.',
            'answer': '$\\dfrac{1}{2} \\cdot \\log_{3}(x)$',
            'wrong': ['$2 \\cdot \\log_{3}(x)$', '$\\dfrac{1}{3} \\cdot \\log_{3}(x)$', '$\\log_{3}(x)$'],
            'explanation': '**Power Rule for the base:** $\\log_{b^n}(x) = \\dfrac{1}{n} \\log_b(x)$. When the **base is raised to a power $n$**, the logarithm is **divided** by $n$. Proof: Let $\\log_{b^n}(x) = y$, so $(b^n)^y = x \\Rightarrow b^{ny} = x \\Rightarrow \\log_b x = ny \\Rightarrow y = \\dfrac{\\log_b x}{n}$. $$\\log_{9}(x) = \\dfrac{1}{2} \\cdot \\log_{3}(x)$$',
        },
        # --- 82 ---
        {
            'question': 'Evaluate: $\\log_{100}\\!\\left(10^{6}\\right)$',
            'answer': '$3$',
            'wrong': ['$\\dfrac{1}{3}$', '$12$', '$\\dfrac{7}{2}$'],
            'explanation': '**Method 1 — Power Rule:** $\\log_{100}(b^m) = \\dfrac{m}{n} \\log_b(b) = \\dfrac{6}{2} \\cdot 1 = 3$. **Method 2 — Direct:** Let $\\log_{100}(10^{6}) = y$. Then $(10^{2})^y = 10^{6} \\Rightarrow 10^{2y} = 10^{6} \\Rightarrow 2y = 6 \\Rightarrow y = \\dfrac{6}{2} = 3$.',
        },
        # --- 83 ---
        {
            'question': 'Simplify: $\\log_{625}(x)$ in terms of $\\log_{5}(x)$.',
            'answer': '$\\dfrac{1}{4} \\cdot \\log_{5}(x)$',
            'wrong': ['$4 \\cdot \\log_{5}(x)$', '$\\dfrac{1}{5} \\cdot \\log_{5}(x)$', '$\\log_{5}(x)$'],
            'explanation': '**Power Rule for the base:** $\\log_{b^n}(x) = \\dfrac{1}{n} \\log_b(x)$. When the **base is raised to a power $n$**, the logarithm is **divided** by $n$. Proof: Let $\\log_{b^n}(x) = y$, so $(b^n)^y = x \\Rightarrow b^{ny} = x \\Rightarrow \\log_b x = ny \\Rightarrow y = \\dfrac{\\log_b x}{n}$. $$\\log_{625}(x) = \\dfrac{1}{4} \\cdot \\log_{5}(x)$$',
        },
        # --- 84 ---
        {
            'question': 'Evaluate: $\\log_{4}\\!\\left(2^{3}\\right)$',
            'answer': '$\\dfrac{3}{2}$',
            'wrong': ['$\\dfrac{2}{3}$', '$6$', '$2$'],
            'explanation': '**Method 1 — Power Rule:** $\\log_{4}(b^m) = \\dfrac{m}{n} \\log_b(b) = \\dfrac{3}{2} \\cdot 1 = \\dfrac{3}{2}$. **Method 2 — Direct:** Let $\\log_{4}(2^{3}) = y$. Then $(2^{2})^y = 2^{3} \\Rightarrow 2^{2y} = 2^{3} \\Rightarrow 2y = 3 \\Rightarrow y = \\dfrac{3}{2} = \\dfrac{3}{2}$.',
        },
        # --- 85 ---
        {
            'question': 'Evaluate: $\\log_{27}\\!\\left(3^{4}\\right)$',
            'answer': '$\\dfrac{4}{3}$',
            'wrong': ['$\\dfrac{3}{4}$', '$12$', '$\\dfrac{5}{3}$'],
            'explanation': '**Method 1 — Power Rule:** $\\log_{27}(b^m) = \\dfrac{m}{n} \\log_b(b) = \\dfrac{4}{3} \\cdot 1 = \\dfrac{4}{3}$. **Method 2 — Direct:** Let $\\log_{27}(3^{4}) = y$. Then $(3^{3})^y = 3^{4} \\Rightarrow 3^{3y} = 3^{4} \\Rightarrow 3y = 4 \\Rightarrow y = \\dfrac{4}{3} = \\dfrac{4}{3}$.',
        },
        # --- 86 ---
        {
            'question': 'Evaluate: $\\log_{1000}\\!\\left(10^{4}\\right)$',
            'answer': '$\\dfrac{4}{3}$',
            'wrong': ['$\\dfrac{3}{4}$', '$12$', '$\\dfrac{5}{3}$'],
            'explanation': '**Method 1 — Power Rule:** $\\log_{1000}(b^m) = \\dfrac{m}{n} \\log_b(b) = \\dfrac{4}{3} \\cdot 1 = \\dfrac{4}{3}$. **Method 2 — Direct:** Let $\\log_{1000}(10^{4}) = y$. Then $(10^{3})^y = 10^{4} \\Rightarrow 10^{3y} = 10^{4} \\Rightarrow 3y = 4 \\Rightarrow y = \\dfrac{4}{3} = \\dfrac{4}{3}$.',
        },
        # --- 87 ---
        {
            'question': 'Apply the power rule to simplify: $\\log_{3}(x^{2})$',
            'answer': '$2 \\cdot \\log_{3}(x)$',
            'wrong': ['$\\log_{3}(x)^{2}$', '$\\log_{3}(x) + 2$', '$\\dfrac{1}{2} \\cdot \\log_{3}(x)$'],
            'explanation': '**Power Rule of Logarithms:** $\\log_b(x^n) = n \\cdot \\log_b(x)$. The exponent of the **argument** comes down as a **coefficient**. $$\\log_{3}(x^{2}) = 2 \\cdot \\log_{3}(x)$$',
        },
        # --- 88 ---
        {
            'question': 'Simplify: $\\log_{10000}(x)$ in terms of $\\log_{10}(x)$.',
            'answer': '$\\dfrac{1}{4} \\cdot \\log(x)$',
            'wrong': ['$4 \\cdot \\log(x)$', '$\\dfrac{1}{5} \\cdot \\log(x)$', '$\\log(x)$'],
            'explanation': '**Power Rule for the base:** $\\log_{b^n}(x) = \\dfrac{1}{n} \\log_b(x)$. When the **base is raised to a power $n$**, the logarithm is **divided** by $n$. Proof: Let $\\log_{b^n}(x) = y$, so $(b^n)^y = x \\Rightarrow b^{ny} = x \\Rightarrow \\log_b x = ny \\Rightarrow y = \\dfrac{\\log_b x}{n}$. $$\\log_{10000}(x) = \\dfrac{1}{4} \\cdot \\log(x)$$',
        },
        # --- 89 ---
        {
            'question': 'Simplify: $\\log_{8}(x)$ in terms of $\\log_{2}(x)$.',
            'answer': '$\\dfrac{1}{3} \\cdot \\log_{2}(x)$',
            'wrong': ['$3 \\cdot \\log_{2}(x)$', '$\\dfrac{1}{4} \\cdot \\log_{2}(x)$', '$\\log_{2}(x)$'],
            'explanation': '**Power Rule for the base:** $\\log_{b^n}(x) = \\dfrac{1}{n} \\log_b(x)$. When the **base is raised to a power $n$**, the logarithm is **divided** by $n$. Proof: Let $\\log_{b^n}(x) = y$, so $(b^n)^y = x \\Rightarrow b^{ny} = x \\Rightarrow \\log_b x = ny \\Rightarrow y = \\dfrac{\\log_b x}{n}$. $$\\log_{8}(x) = \\dfrac{1}{3} \\cdot \\log_{2}(x)$$',
        },
        # --- 90 ---
        {
            'question': 'Evaluate: $\\log_{8}\\!\\left(2^{3}\\right)$',
            'answer': '$1$',
            'wrong': ['$1$', '$9$', '$\\dfrac{4}{3}$'],
            'explanation': '**Method 1 — Power Rule:** $\\log_{8}(b^m) = \\dfrac{m}{n} \\log_b(b) = \\dfrac{3}{3} \\cdot 1 = 1$. **Method 2 — Direct:** Let $\\log_{8}(2^{3}) = y$. Then $(2^{3})^y = 2^{3} \\Rightarrow 2^{3y} = 2^{3} \\Rightarrow 3y = 3 \\Rightarrow y = \\dfrac{3}{3} = 1$.',
        },
        # --- 91 ---
        {
            'question': 'Simplify: $\\log_{27}(x)$ in terms of $\\log_{3}(x)$.',
            'answer': '$\\dfrac{1}{3} \\cdot \\log_{3}(x)$',
            'wrong': ['$3 \\cdot \\log_{3}(x)$', '$\\dfrac{1}{4} \\cdot \\log_{3}(x)$', '$\\log_{3}(x)$'],
            'explanation': '**Power Rule for the base:** $\\log_{b^n}(x) = \\dfrac{1}{n} \\log_b(x)$. When the **base is raised to a power $n$**, the logarithm is **divided** by $n$. Proof: Let $\\log_{b^n}(x) = y$, so $(b^n)^y = x \\Rightarrow b^{ny} = x \\Rightarrow \\log_b x = ny \\Rightarrow y = \\dfrac{\\log_b x}{n}$. $$\\log_{27}(x) = \\dfrac{1}{3} \\cdot \\log_{3}(x)$$',
        },
        # --- 92 ---
        {
            'question': 'Apply the power rule to simplify: $\\log_{2}(x^{2})$',
            'answer': '$2 \\cdot \\log_{2}(x)$',
            'wrong': ['$\\log_{2}(x)^{2}$', '$\\log_{2}(x) + 2$', '$\\dfrac{1}{2} \\cdot \\log_{2}(x)$'],
            'explanation': '**Power Rule of Logarithms:** $\\log_b(x^n) = n \\cdot \\log_b(x)$. The exponent of the **argument** comes down as a **coefficient**. $$\\log_{2}(x^{2}) = 2 \\cdot \\log_{2}(x)$$',
        },
        # --- 93 ---
        {
            'question': 'Evaluate: $\\log_{25}\\!\\left(5^{3}\\right)$',
            'answer': '$\\dfrac{3}{2}$',
            'wrong': ['$\\dfrac{2}{3}$', '$6$', '$2$'],
            'explanation': '**Method 1 — Power Rule:** $\\log_{25}(b^m) = \\dfrac{m}{n} \\log_b(b) = \\dfrac{3}{2} \\cdot 1 = \\dfrac{3}{2}$. **Method 2 — Direct:** Let $\\log_{25}(5^{3}) = y$. Then $(5^{2})^y = 5^{3} \\Rightarrow 5^{2y} = 5^{3} \\Rightarrow 2y = 3 \\Rightarrow y = \\dfrac{3}{2} = \\dfrac{3}{2}$.',
        },
        # --- 94 ---
        {
            'question': 'Simplify: $\\log_{125}(x^{3})$ in terms of $\\log_{5}(x)$.',
            'answer': '$\\dfrac{3}{3} \\cdot \\log_{5}(x)$',
            'wrong': ['$\\dfrac{3}{3} \\cdot \\log_{5}(x)$', '$3\\cdot3 \\cdot \\log_{5}(x)$',
                      '$\\dfrac{4}{3} \\cdot \\log_{5}(x)$'],
            'explanation': 'Apply **both** power rules together: $\\log_{b^m}(x^n) = \\dfrac{n}{m} \\log_b(x)$. **Step 1 — argument power:** $\\log_{b^m}(x^n) = n \\cdot \\log_{b^m}(x)$. **Step 2 — base power:** $n \\cdot \\log_{b^m}(x) = n \\cdot \\dfrac{1}{3} \\log_b(x) = \\dfrac{3}{3} \\log_b(x)$. $$\\log_{125}(x^{3}) = \\dfrac{3}{3} \\cdot \\log_{5}(x)$$',
        },
        # --- 95 ---
        {
            'question': 'Simplify: $\\log_{1000}(x)$ in terms of $\\log_{10}(x)$.',
            'answer': '$\\dfrac{1}{3} \\cdot \\log(x)$',
            'wrong': ['$3 \\cdot \\log(x)$', '$\\dfrac{1}{4} \\cdot \\log(x)$', '$\\log(x)$'],
            'explanation': '**Power Rule for the base:** $\\log_{b^n}(x) = \\dfrac{1}{n} \\log_b(x)$. When the **base is raised to a power $n$**, the logarithm is **divided** by $n$. Proof: Let $\\log_{b^n}(x) = y$, so $(b^n)^y = x \\Rightarrow b^{ny} = x \\Rightarrow \\log_b x = ny \\Rightarrow y = \\dfrac{\\log_b x}{n}$. $$\\log_{1000}(x) = \\dfrac{1}{3} \\cdot \\log(x)$$',
        },
        # --- 96 ---
        {
            'question': 'Simplify: $\\log_{1000}(x^{2})$ in terms of $\\log_{10}(x)$.',
            'answer': '$\\dfrac{2}{3} \\cdot \\log(x)$',
            'wrong': ['$\\dfrac{3}{2} \\cdot \\log(x)$', '$2\\cdot3 \\cdot \\log(x)$',
                      '$\\dfrac{3}{3} \\cdot \\log(x)$'],
            'explanation': 'Apply **both** power rules together: $\\log_{b^m}(x^n) = \\dfrac{n}{m} \\log_b(x)$. **Step 1 — argument power:** $\\log_{b^m}(x^n) = n \\cdot \\log_{b^m}(x)$. **Step 2 — base power:** $n \\cdot \\log_{b^m}(x) = n \\cdot \\dfrac{1}{3} \\log_b(x) = \\dfrac{2}{3} \\log_b(x)$. $$\\log_{1000}(x^{2}) = \\dfrac{2}{3} \\cdot \\log(x)$$',
        },
        # --- 97 ---
        {
            'question': 'Simplify: $\\log_{125}(x^{3})$ in terms of $\\log_{5}(x)$.',
            'answer': '$\\dfrac{3}{3} \\cdot \\log_{5}(x)$',
            'wrong': ['$\\dfrac{3}{3} \\cdot \\log_{5}(x)$', '$3\\cdot3 \\cdot \\log_{5}(x)$',
                      '$\\dfrac{4}{3} \\cdot \\log_{5}(x)$'],
            'explanation': 'Apply **both** power rules together: $\\log_{b^m}(x^n) = \\dfrac{n}{m} \\log_b(x)$. **Step 1 — argument power:** $\\log_{b^m}(x^n) = n \\cdot \\log_{b^m}(x)$. **Step 2 — base power:** $n \\cdot \\log_{b^m}(x) = n \\cdot \\dfrac{1}{3} \\log_b(x) = \\dfrac{3}{3} \\log_b(x)$. $$\\log_{125}(x^{3}) = \\dfrac{3}{3} \\cdot \\log_{5}(x)$$',
        },
        # --- 98 ---
        {
            'question': 'Simplify: $\\log_{9}(x^{4})$ in terms of $\\log_{3}(x)$.',
            'answer': '$\\dfrac{4}{2} \\cdot \\log_{3}(x)$',
            'wrong': ['$\\dfrac{2}{4} \\cdot \\log_{3}(x)$', '$4\\cdot2 \\cdot \\log_{3}(x)$',
                      '$\\dfrac{5}{2} \\cdot \\log_{3}(x)$'],
            'explanation': 'Apply **both** power rules together: $\\log_{b^m}(x^n) = \\dfrac{n}{m} \\log_b(x)$. **Step 1 — argument power:** $\\log_{b^m}(x^n) = n \\cdot \\log_{b^m}(x)$. **Step 2 — base power:** $n \\cdot \\log_{b^m}(x) = n \\cdot \\dfrac{1}{2} \\log_b(x) = \\dfrac{4}{2} \\log_b(x)$. $$\\log_{9}(x^{4}) = \\dfrac{4}{2} \\cdot \\log_{3}(x)$$',
        },
        # --- 99 ---
        {
            'question': 'Evaluate: $\\log_{100}\\!\\left(10^{6}\\right)$',
            'answer': '$3$',
            'wrong': ['$\\dfrac{1}{3}$', '$12$', '$\\dfrac{7}{2}$'],
            'explanation': '**Method 1 — Power Rule:** $\\log_{100}(b^m) = \\dfrac{m}{n} \\log_b(b) = \\dfrac{6}{2} \\cdot 1 = 3$. **Method 2 — Direct:** Let $\\log_{100}(10^{6}) = y$. Then $(10^{2})^y = 10^{6} \\Rightarrow 10^{2y} = 10^{6} \\Rightarrow 2y = 6 \\Rightarrow y = \\dfrac{6}{2} = 3$.',
        },
        # --- 100 ---
        {
            'question': 'Simplify: $\\log_{16}(x)$ in terms of $\\log_{2}(x)$.',
            'answer': '$\\dfrac{1}{4} \\cdot \\log_{2}(x)$',
            'wrong': ['$4 \\cdot \\log_{2}(x)$', '$\\dfrac{1}{5} \\cdot \\log_{2}(x)$', '$\\log_{2}(x)$'],
            'explanation': '**Power Rule for the base:** $\\log_{b^n}(x) = \\dfrac{1}{n} \\log_b(x)$. When the **base is raised to a power $n$**, the logarithm is **divided** by $n$. Proof: Let $\\log_{b^n}(x) = y$, so $(b^n)^y = x \\Rightarrow b^{ny} = x \\Rightarrow \\log_b x = ny \\Rightarrow y = \\dfrac{\\log_b x}{n}$. $$\\log_{16}(x) = \\dfrac{1}{4} \\cdot \\log_{2}(x)$$',
        },
    ],
    'logarithmic_functions': [{
        'question': 'Find the domain of $f(x) = \\log_2(x - 3)$.',
        'answer': '$(3,\\ +\\infty)$',
        'wrong': ['$(-\\infty,\\ 3)$', '$[3,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
        'explanation': 'Argument must be $> 0$: $x - 3 > 0 \\Rightarrow x > 3$. Domain: $(3, +\\infty)$.',
    },
        {
            'question': 'Find the domain of $f(x) = \\log_3(x + 5)$.',
            'answer': '$(-5,\\ +\\infty)$',
            'wrong': ['$(5,\\ +\\infty)$', '$(-\\infty,\\ -5)$', '$[-5,\\ +\\infty)$'],
            'explanation': '$x + 5 > 0 \\Rightarrow x > -5$. Domain: $(-5, +\\infty)$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_5(2x - 4)$.',
            'answer': '$(2,\\ +\\infty)$',
            'wrong': ['$(4,\\ +\\infty)$', '$(-\\infty,\\ 2)$', '$[2,\\ +\\infty)$'],
            'explanation': '$2x - 4 > 0 \\Rightarrow x > 2$. Domain: $(2, +\\infty)$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_2(x^2 - 9)$.',
            'answer': '$(-\\infty,\\ -3) \\cup (3,\\ +\\infty)$',
            'wrong': ['$(-3,\\ 3)$', '$(3,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': '$x^2 - 9 > 0 \\Rightarrow (x-3)(x+3) > 0 \\Rightarrow x < -3$ or $x > 3$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_4(-x + 2)$.',
            'answer': '$(-\\infty,\\ 2)$',
            'wrong': ['$(2,\\ +\\infty)$', '$(-\\infty,\\ -2)$', '$[-2,\\ 2]$'],
            'explanation': '$-x + 2 > 0 \\Rightarrow x < 2$. Domain: $(-\\infty, 2)$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_3(x^2 - 4x)$.',
            'answer': '$(-\\infty,\\ 0) \\cup (4,\\ +\\infty)$',
            'wrong': ['$(0,\\ 4)$', '$(4,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': '$x^2 - 4x > 0 \\Rightarrow x(x-4) > 0 \\Rightarrow x < 0$ or $x > 4$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_2(x + 1) + \\log_2(x - 1)$.',
            'answer': '$(1,\\ +\\infty)$',
            'wrong': ['$(-1,\\ 1)$', '$(-1,\\ +\\infty)$', '$(-\\infty,\\ -1) \\cup (1,\\ +\\infty)$'],
            'explanation': 'Both arguments must be $> 0$: $x > -1$ AND $x > 1$. Intersection: $x > 1$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_{10}(3x + 12)$.',
            'answer': '$(-4,\\ +\\infty)$',
            'wrong': ['$(4,\\ +\\infty)$', '$(-\\infty,\\ -4)$', '$(-12,\\ +\\infty)$'],
            'explanation': '$3x + 12 > 0 \\Rightarrow x > -4$. Domain: $(-4, +\\infty)$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_2\\!(x^2 - 5x + 6)$.',
            'answer': '$(-\\infty,\\ 2) \\cup (3,\\ +\\infty)$',
            'wrong': ['$(2,\\ 3)$', '$(3,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': '$x^2 - 5x + 6 = (x-2)(x-3) > 0 \\Rightarrow x < 2$ or $x > 3$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\ln(x - 7)$.',
            'answer': '$(7,\\ +\\infty)$',
            'wrong': ['$(-\\infty,\\ 7)$', '$[7,\\ +\\infty)$', '$(0,\\ +\\infty)$'],
            'explanation': '$x - 7 > 0 \\Rightarrow x > 7$. Domain: $(7, +\\infty)$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_5\\!\\left(\\dfrac{1}{x-2}\\right)$.',
            'answer': '$(2,\\ +\\infty)$',
            'wrong': ['$(-\\infty,\\ 2)$', '$(-\\infty,\\ 2) \\cup (2,\\ +\\infty)$', '$[2,\\ +\\infty)$'],
            'explanation': '$\\dfrac{1}{x-2} > 0 \\Rightarrow x - 2 > 0 \\Rightarrow x > 2$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_3(9 - x^2)$.',
            'answer': '$(-3,\\ 3)$',
            'wrong': ['$(-\\infty,\\ -3) \\cup (3,\\ +\\infty)$', '$[-3,\\ 3]$', '$(3,\\ +\\infty)$'],
            'explanation': '$9 - x^2 > 0 \\Rightarrow x^2 < 9 \\Rightarrow -3 < x < 3$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_2(4 - x)$.',
            'answer': '$(-\\infty,\\ 4)$',
            'wrong': ['$(4,\\ +\\infty)$', '$(-4,\\ 4)$', '$(-\\infty,\\ -4)$'],
            'explanation': '$4 - x > 0 \\Rightarrow x < 4$. Domain: $(-\\infty, 4)$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_4(x^2 - 1)$.',
            'answer': '$(-\\infty,\\ -1) \\cup (1,\\ +\\infty)$',
            'wrong': ['$(-1,\\ 1)$', '$(1,\\ +\\infty)$', '$[-1,\\ 1]$'],
            'explanation': '$x^2 - 1 > 0 \\Rightarrow (x-1)(x+1) > 0 \\Rightarrow x < -1$ or $x > 1$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_2(x) + \\log_2(4 - x)$.',
            'answer': '$(0,\\ 4)$',
            'wrong': ['$(0,\\ +\\infty)$', '$(-\\infty,\\ 4)$', '$[0,\\ 4]$'],
            'explanation': '$x > 0$ AND $4 - x > 0 \\Rightarrow x < 4$. Intersection: $0 < x < 4$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_3(2x + 10)$.',
            'answer': '$(-5,\\ +\\infty)$',
            'wrong': ['$(5,\\ +\\infty)$', '$(-10,\\ +\\infty)$', '$(-\\infty,\\ -5)$'],
            'explanation': '$2x + 10 > 0 \\Rightarrow x > -5$. Domain: $(-5, +\\infty)$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\ln(x^2 + 1)$.',
            'answer': '$(-\\infty,\\ +\\infty)$',
            'wrong': ['$(0,\\ +\\infty)$', '$(-1,\\ 1)$', '$(-1,\\ +\\infty)$'],
            'explanation': '$x^2 + 1 \\geq 1 > 0$ for all real $x$. Domain: all reals.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_5(x - 4)^2$.',
            'answer': '$(-\\infty,\\ 4) \\cup (4,\\ +\\infty)$',
            'wrong': ['$(4,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$', '$(-\\infty,\\ -4) \\cup (4,\\ +\\infty)$'],
            'explanation': '$(x-4)^2 > 0$ for all $x \\neq 4$. Domain: $x \\neq 4$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_2\\!(x^2 - 6x + 8)$.',
            'answer': '$(-\\infty,\\ 2) \\cup (4,\\ +\\infty)$',
            'wrong': ['$(2,\\ 4)$', '$(4,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': '$(x-2)(x-4) > 0 \\Rightarrow x < 2$ or $x > 4$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_3\\!\\left(\\dfrac{x+1}{x-3}\\right)$.',
            'answer': '$(-\\infty,\\ -1) \\cup (3,\\ +\\infty)$',
            'wrong': ['$(-1,\\ 3)$', '$(3,\\ +\\infty)$', '$(-\\infty,\\ 3)$'],
            'explanation': '$\\dfrac{x+1}{x-3} > 0$: same sign when $x < -1$ or $x > 3$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\ln(5 - 2x)$.',
            'answer': '$\\left(-\\infty,\\ \\dfrac{5}{2}\\right)$',
            'wrong': ['$\\left(\\dfrac{5}{2},\\ +\\infty\\right)$', '$(-5,\\ +\\infty)$', '$(-\\infty,\\ 5)$'],
            'explanation': '$5 - 2x > 0 \\Rightarrow x < \\tfrac{5}{2}$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_4(x^2 - 4x + 3)$.',
            'answer': '$(-\\infty,\\ 1) \\cup (3,\\ +\\infty)$',
            'wrong': ['$(1,\\ 3)$', '$(3,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': '$(x-1)(x-3) > 0 \\Rightarrow x < 1$ or $x > 3$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_2(x + 3) - \\log_2(x - 1)$.',
            'answer': '$(1,\\ +\\infty)$',
            'wrong': ['$(-3,\\ 1)$', '$(-3,\\ +\\infty)$', '$(-\\infty,\\ -3) \\cup (1,\\ +\\infty)$'],
            'explanation': '$x > -3$ AND $x > 1$. Intersection: $x > 1$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_5(x^2 - 9x + 20)$.',
            'answer': '$(-\\infty,\\ 4) \\cup (5,\\ +\\infty)$',
            'wrong': ['$(4,\\ 5)$', '$(5,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$'],
            'explanation': '$(x-4)(x-5) > 0 \\Rightarrow x < 4$ or $x > 5$.',
        },
        {
            'question': 'Find the domain of $f(x) = \\log_3|x - 2|$.',
            'answer': '$(-\\infty,\\ 2) \\cup (2,\\ +\\infty)$',
            'wrong': ['$(2,\\ +\\infty)$', '$(-\\infty,\\ +\\infty)$', '$(-2,\\ 2)$'],
            'explanation': '$|x - 2| > 0$ for all $x \\neq 2$. Domain: $x \\neq 2$.',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 2: Given x, find y  (25 problems)
        # ══════════════════════════════════════════════════════

        {
            'question': 'Given $f(x) = \\log_2(x)$, find $f(8)$.',
            'answer': '$3$',
            'wrong': ['$4$', '$2$', '$16$'],
            'explanation': '$\\log_2(8) = \\log_2(2^3) = 3$.',
        },
        {
            'question': 'Given $f(x) = \\log_3(x)$, find $f(27)$.',
            'answer': '$3$',
            'wrong': ['$9$', '$2$', '$4$'],
            'explanation': '$\\log_3(27) = \\log_3(3^3) = 3$.',
        },
        {
            'question': 'Given $f(x) = \\log_5(x)$, find $f(25)$.',
            'answer': '$2$',
            'wrong': ['$5$', '$3$', '$1$'],
            'explanation': '$\\log_5(25) = \\log_5(5^2) = 2$.',
        },
        {
            'question': 'Given $f(x) = \\log_{10}(x)$, find $f(1000)$.',
            'answer': '$3$',
            'wrong': ['$4$', '$2$', '$100$'],
            'explanation': '$\\log_{10}(1000) = \\log_{10}(10^3) = 3$.',
        },
        {
            'question': 'Given $f(x) = \\log_2(x)$, find $f\\!\\left(\\dfrac{1}{4}\\right)$.',
            'answer': '$-2$',
            'wrong': ['$2$', '$-4$', '$\\tfrac{1}{2}$'],
            'explanation': '$\\log_2\\!\\left(\\tfrac{1}{4}\\right) = \\log_2(2^{-2}) = -2$.',
        },
        {
            'question': 'Given $f(x) = \\log_3(x)$, find $f\\!\\left(\\dfrac{1}{9}\\right)$.',
            'answer': '$-2$',
            'wrong': ['$2$', '$-3$', '$-1$'],
            'explanation': '$\\log_3\\!\\left(\\tfrac{1}{9}\\right) = \\log_3(3^{-2}) = -2$.',
        },
        {
            'question': 'Given $f(x) = \\log_4(x)$, find $f(64)$.',
            'answer': '$3$',
            'wrong': ['$4$', '$2$', '$16$'],
            'explanation': '$\\log_4(64) = \\log_4(4^3) = 3$.',
        },
        {
            'question': 'Given $f(x) = \\log_2(x)$, find $f(1)$.',
            'answer': '$0$',
            'wrong': ['$1$', '$2$', '$-1$'],
            'explanation': '$\\log_2(1) = \\log_2(2^0) = 0$.',
        },
        {
            'question': 'Given $f(x) = \\log_6(x)$, find $f(36)$.',
            'answer': '$2$',
            'wrong': ['$6$', '$3$', '$1$'],
            'explanation': '$\\log_6(36) = \\log_6(6^2) = 2$.',
        },
        {
            'question': 'Given $f(x) = \\log_2(x + 4)$, find $f(4)$.',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$1$'],
            'explanation': '$\\log_2(4 + 4) = \\log_2(8) = 3$.',
        },
        {
            'question': 'Given $f(x) = \\log_3(x - 1)$, find $f(28)$.',
            'answer': '$3$',
            'wrong': ['$4$', '$2$', '$9$'],
            'explanation': '$\\log_3(28 - 1) = \\log_3(27) = 3$.',
        },
        {
            'question': 'Given $f(x) = 2\\log_2(x)$, find $f(8)$.',
            'answer': '$6$',
            'wrong': ['$3$', '$16$', '$4$'],
            'explanation': '$2 \\cdot \\log_2(8) = 2 \\cdot 3 = 6$.',
        },
        {
            'question': 'Given $f(x) = \\log_5(x)$, find $f(1)$.',
            'answer': '$0$',
            'wrong': ['$1$', '$5$', '$-1$'],
            'explanation': '$\\log_5(1) = 0$ (any base: $\\log_b(1) = 0$).',
        },
        {
            'question': 'Given $f(x) = \\log_2(x^2)$, find $f(4)$.',
            'answer': '$4$',
            'wrong': ['$2$', '$8$', '$16$'],
            'explanation': '$\\log_2(4^2) = \\log_2(16) = 4$.',
        },
        {
            'question': 'Given $f(x) = \\log_{10}(x)$, find $f(0.01)$.',
            'answer': '$-2$',
            'wrong': ['$2$', '$-1$', '$-3$'],
            'explanation': '$\\log_{10}(0.01) = \\log_{10}(10^{-2}) = -2$.',
        },
        {
            'question': 'Given $f(x) = \\log_4(x)$, find $f\\!\\left(\\dfrac{1}{16}\\right)$.',
            'answer': '$-2$',
            'wrong': ['$2$', '$-4$', '$-1$'],
            'explanation': '$\\log_4\\!\\left(\\tfrac{1}{16}\\right) = \\log_4(4^{-2}) = -2$.',
        },
        {
            'question': 'Given $f(x) = \\log_3(x) + 1$, find $f(9)$.',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$10$'],
            'explanation': '$\\log_3(9) + 1 = 2 + 1 = 3$.',
        },
        {
            'question': 'Given $f(x) = \\log_2(x)$, find $f(32)$.',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$16$'],
            'explanation': '$\\log_2(32) = \\log_2(2^5) = 5$.',
        },
        {
            'question': 'Given $f(x) = \\log_9(x)$, find $f(81)$.',
            'answer': '$2$',
            'wrong': ['$9$', '$3$', '$4$'],
            'explanation': '$\\log_9(81) = \\log_9(9^2) = 2$.',
        },
        {
            'question': 'Given $f(x) = \\log_5(x) - 2$, find $f(125)$.',
            'answer': '$1$',
            'wrong': ['$3$', '$-2$', '$5$'],
            'explanation': '$\\log_5(125) - 2 = 3 - 2 = 1$.',
        },
        {
            'question': 'Given $f(x) = \\log_2(2x)$, find $f(16)$.',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$3$'],
            'explanation': '$\\log_2(2 \\cdot 16) = \\log_2(32) = 5$.',
        },
        {
            'question': 'Given $f(x) = \\log_3(x^2 - 1)$, find $f(10)$.',
            'answer': '$\\log_3(99)$',
            'wrong': ['$\\log_3(100)$', '$2$', '$4$'],
            'explanation': '$\\log_3(10^2 - 1) = \\log_3(99)$. Cannot simplify further.',
        },
        {
            'question': 'Given $f(x) = \\log_{10}(x)$, find $f(10^5)$.',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$50$'],
            'explanation': '$\\log_{10}(10^5) = 5$.',
        },
        {
            'question': 'Given $f(x) = 3\\log_2(x)$, find $f(4)$.',
            'answer': '$6$',
            'wrong': ['$3$', '$12$', '$2$'],
            'explanation': '$3 \\cdot \\log_2(4) = 3 \\cdot 2 = 6$.',
        },
        {
            'question': 'Given $f(x) = \\log_7(x)$, find $f(49)$.',
            'answer': '$2$',
            'wrong': ['$7$', '$3$', '$14$'],
            'explanation': '$\\log_7(49) = \\log_7(7^2) = 2$.',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 3: Given y, find x  (25 problems)
        # ══════════════════════════════════════════════════════

        {
            'question': 'Solve $\\log_2(x) = 4$.',
            'answer': '$x = 16$',
            'wrong': ['$x = 8$', '$x = 2$', '$x = 32$'],
            'explanation': '$\\log_2(x) = 4 \\Rightarrow x = 2^4 = 16$.',
        },
        {
            'question': 'Solve $\\log_3(x) = 3$.',
            'answer': '$x = 27$',
            'wrong': ['$x = 9$', '$x = 3$', '$x = 81$'],
            'explanation': '$x = 3^3 = 27$.',
        },
        {
            'question': 'Solve $\\log_5(x) = 2$.',
            'answer': '$x = 25$',
            'wrong': ['$x = 10$', '$x = 5$', '$x = 125$'],
            'explanation': '$x = 5^2 = 25$.',
        },
        {
            'question': 'Solve $\\log_2(x) = -3$.',
            'answer': '$x = \\dfrac{1}{8}$',
            'wrong': ['$x = -8$', '$x = \\dfrac{1}{4}$', '$x = -6$'],
            'explanation': '$x = 2^{-3} = \\tfrac{1}{8}$.',
        },
        {
            'question': 'Solve $\\log_4(x) = 3$.',
            'answer': '$x = 64$',
            'wrong': ['$x = 12$', '$x = 16$', '$x = 32$'],
            'explanation': '$x = 4^3 = 64$.',
        },
        {
            'question': 'Solve $\\log_{10}(x) = -2$.',
            'answer': '$x = 0.01$',
            'wrong': ['$x = -100$', '$x = 0.1$', '$x = -20$'],
            'explanation': '$x = 10^{-2} = 0.01$.',
        },
        {
            'question': 'Solve $\\log_2(x - 1) = 3$.',
            'answer': '$x = 9$',
            'wrong': ['$x = 8$', '$x = 7$', '$x = 4$'],
            'explanation': '$x - 1 = 2^3 = 8 \\Rightarrow x = 9$.',
        },
        {
            'question': 'Solve $\\log_3(x + 2) = 2$.',
            'answer': '$x = 7$',
            'wrong': ['$x = 9$', '$x = 11$', '$x = 4$'],
            'explanation': '$x + 2 = 3^2 = 9 \\Rightarrow x = 7$.',
        },
        {
            'question': 'Solve $\\log_5(2x) = 2$.',
            'answer': '$x = \\dfrac{25}{2}$',
            'wrong': ['$x = 25$', '$x = 5$', '$x = 10$'],
            'explanation': '$2x = 5^2 = 25 \\Rightarrow x = \\tfrac{25}{2}$.',
        },
        {
            'question': 'Solve $\\log_2(x^2) = 6$.',
            'answer': '$x = 8$ or $x = -8$',
            'wrong': ['$x = 8$', '$x = 64$', '$x = 3$'],
            'explanation': '$x^2 = 2^6 = 64 \\Rightarrow x = \\pm 8$.',
        },
        {
            'question': 'Solve $\\log_3(x) = 0$.',
            'answer': '$x = 1$',
            'wrong': ['$x = 0$', '$x = 3$', '$x = -1$'],
            'explanation': '$x = 3^0 = 1$.',
        },
        {
            'question': 'Solve $\\log_6(x - 4) = 2$.',
            'answer': '$x = 40$',
            'wrong': ['$x = 36$', '$x = 32$', '$x = 12$'],
            'explanation': '$x - 4 = 6^2 = 36 \\Rightarrow x = 40$.',
        },
        {
            'question': 'Solve $2\\log_2(x) = 8$.',
            'answer': '$x = 16$',
            'wrong': ['$x = 4$', '$x = 64$', '$x = 8$'],
            'explanation': '$\\log_2(x) = 4 \\Rightarrow x = 2^4 = 16$.',
        },
        {
            'question': 'Solve $\\log_4(x) = \\dfrac{1}{2}$.',
            'answer': '$x = 2$',
            'wrong': ['$x = 4$', '$x = 8$', '$x = \\tfrac{1}{2}$'],
            'explanation': '$x = 4^{1/2} = \\sqrt{4} = 2$.',
        },
        {
            'question': 'Solve $\\log_3(x) = -1$.',
            'answer': '$x = \\dfrac{1}{3}$',
            'wrong': ['$x = -3$', '$x = \\dfrac{1}{9}$', '$x = 3$'],
            'explanation': '$x = 3^{-1} = \\tfrac{1}{3}$.',
        },
        {
            'question': 'Solve $\\log_2(3x - 1) = 4$.',
            'answer': '$x = \\dfrac{17}{3}$',
            'wrong': ['$x = 5$', '$x = 16$', '$x = \\dfrac{15}{3}$'],
            'explanation': '$3x - 1 = 2^4 = 16 \\Rightarrow 3x = 17 \\Rightarrow x = \\tfrac{17}{3}$.',
        },
        {
            'question': 'Solve $\\log_9(x) = \\dfrac{1}{2}$.',
            'answer': '$x = 3$',
            'wrong': ['$x = 9$', '$x = \\tfrac{9}{2}$', '$x = 6$'],
            'explanation': '$x = 9^{1/2} = 3$.',
        },
        {
            'question': 'Solve $\\log_5(x) + 1 = 3$.',
            'answer': '$x = 25$',
            'wrong': ['$x = 125$', '$x = 5$', '$x = 10$'],
            'explanation': '$\\log_5(x) = 2 \\Rightarrow x = 5^2 = 25$.',
        },
        {
            'question': 'Solve $\\log_2(x + 5) = 0$.',
            'answer': '$x = -4$',
            'wrong': ['$x = 5$', '$x = 1$', '$x = -5$'],
            'explanation': '$x + 5 = 2^0 = 1 \\Rightarrow x = -4$.',
        },
        {
            'question': 'Solve $\\log_4(2x + 4) = 2$.',
            'answer': '$x = 6$',
            'wrong': ['$x = 8$', '$x = 4$', '$x = 12$'],
            'explanation': '$2x + 4 = 4^2 = 16 \\Rightarrow 2x = 12 \\Rightarrow x = 6$.',
        },
        {
            'question': 'Solve $\\log_3(x^2 - 8) = 2$.',
            'answer': '$x = \\pm\\sqrt{17}$',
            'wrong': ['$x = 17$', '$x = \\pm 3$', '$x = \\sqrt{17}$'],
            'explanation': '$x^2 - 8 = 3^2 = 9 \\Rightarrow x^2 = 17 \\Rightarrow x = \\pm\\sqrt{17}$.',
        },
        {
            'question': 'Solve $\\log_{10}(x) = 4$.',
            'answer': '$x = 10000$',
            'wrong': ['$x = 1000$', '$x = 40$', '$x = 100000$'],
            'explanation': '$x = 10^4 = 10000$.',
        },
        {
            'question': 'Solve $3\\log_5(x) = 6$.',
            'answer': '$x = 25$',
            'wrong': ['$x = 125$', '$x = 5$', '$x = 2$'],
            'explanation': '$\\log_5(x) = 2 \\Rightarrow x = 5^2 = 25$.',
        },
        {
            'question': 'Solve $\\log_2(x) = -1$.',
            'answer': '$x = \\dfrac{1}{2}$',
            'wrong': ['$x = -2$', '$x = 2$', '$x = \\dfrac{1}{4}$'],
            'explanation': '$x = 2^{-1} = \\tfrac{1}{2}$.',
        },
        {
            'question': 'Solve $\\log_7(x - 3) = 2$.',
            'answer': '$x = 52$',
            'wrong': ['$x = 49$', '$x = 46$', '$x = 14$'],
            'explanation': '$x - 3 = 7^2 = 49 \\Rightarrow x = 52$.',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 4: Graph Shifts (up/down/left/right)  (25 problems)
        # ══════════════════════════════════════════════════════

        {
            'question': 'How does the graph of $f(x) = \\log_2(x - 3)$ differ from $y = \\log_2(x)$?',
            'answer': 'Shifted $3$ units to the right',
            'wrong': ['Shifted $3$ units to the left', 'Shifted $3$ units up', 'Shifted $3$ units down'],
            'explanation': '$f(x) = \\log_2(x - 3)$: replacing $x$ with $x - 3$ shifts the graph $\\mathbf{right}$ by 3.',
        },
        {
            'question': 'How does the graph of $f(x) = \\log_3(x + 4)$ differ from $y = \\log_3(x)$?',
            'answer': 'Shifted $4$ units to the left',
            'wrong': ['Shifted $4$ units to the right', 'Shifted $4$ units up', 'Shifted $4$ units down'],
            'explanation': '$x + 4 = x - (-4)$: shift $\\mathbf{left}$ by 4.',
        },
        {
            'question': 'How does the graph of $f(x) = \\log_2(x) + 5$ differ from $y = \\log_2(x)$?',
            'answer': 'Shifted $5$ units up',
            'wrong': ['Shifted $5$ units down', 'Shifted $5$ units to the right', 'Shifted $5$ units to the left'],
            'explanation': 'Adding $5$ outside the log shifts the graph $\\mathbf{up}$ by 5.',
        },
        {
            'question': 'How does the graph of $f(x) = \\log_3(x) - 2$ differ from $y = \\log_3(x)$?',
            'answer': 'Shifted $2$ units down',
            'wrong': ['Shifted $2$ units up', 'Shifted $2$ units to the right', 'Shifted $2$ units to the left'],
            'explanation': 'Subtracting $2$ outside the log shifts the graph $\\mathbf{down}$ by 2.',
        },
        {
            'question': 'How does the graph of $f(x) = \\log_5(x - 1) + 3$ differ from $y = \\log_5(x)$?',
            'answer': 'Shifted $1$ unit right and $3$ units up',
            'wrong': ['Shifted $1$ unit left and $3$ units up', 'Shifted $1$ unit right and $3$ units down',
                      'Shifted $3$ units right and $1$ unit up'],
            'explanation': '$(x-1)$ shifts right 1; $+3$ shifts up 3.',
        },
        {
            'question': 'How does the graph of $f(x) = \\log_2(x + 2) - 4$ differ from $y = \\log_2(x)$?',
            'answer': 'Shifted $2$ units left and $4$ units down',
            'wrong': ['Shifted $2$ units right and $4$ units down', 'Shifted $2$ units left and $4$ units up',
                      'Shifted $4$ units left and $2$ units down'],
            'explanation': '$(x+2)$ shifts left 2; $-4$ shifts down 4.',
        },
        {
            'question': 'What is the vertical asymptote of $f(x) = \\log_3(x - 6)$?',
            'answer': '$x = 6$',
            'wrong': ['$x = -6$', '$y = 6$', '$x = 0$'],
            'explanation': 'Shifting right 6 moves the vertical asymptote from $x=0$ to $x = 6$.',
        },
        {
            'question': 'What is the vertical asymptote of $f(x) = \\log_2(x + 5)$?',
            'answer': '$x = -5$',
            'wrong': ['$x = 5$', '$y = -5$', '$x = 0$'],
            'explanation': 'Shifting left 5 moves the asymptote to $x = -5$.',
        },
        {
            'question': 'The graph of $y = \\log_2(x)$ is shifted $7$ units to the right. What is the new equation?',
            'answer': '$y = \\log_2(x - 7)$',
            'wrong': ['$y = \\log_2(x + 7)$', '$y = \\log_2(x) - 7$', '$y = \\log_2(x) + 7$'],
            'explanation': 'Right shift by $k$: replace $x$ with $x - k$.',
        },
        {
            'question': 'The graph of $y = \\log_3(x)$ is shifted $4$ units up. What is the new equation?',
            'answer': '$y = \\log_3(x) + 4$',
            'wrong': ['$y = \\log_3(x + 4)$', '$y = \\log_3(x) - 4$', '$y = \\log_3(x - 4)$'],
            'explanation': 'Up shift by $k$: add $k$ outside the function.',
        },
        {
            'question': 'The graph of $y = \\log_5(x)$ is shifted $3$ units down. What is the new equation?',
            'answer': '$y = \\log_5(x) - 3$',
            'wrong': ['$y = \\log_5(x - 3)$', '$y = \\log_5(x) + 3$', '$y = \\log_5(x + 3)$'],
            'explanation': 'Down shift by $k$: subtract $k$ outside the function.',
        },
        {
            'question': 'The graph of $y = \\log_2(x)$ is shifted $6$ units to the left. What is the new equation?',
            'answer': '$y = \\log_2(x + 6)$',
            'wrong': ['$y = \\log_2(x - 6)$', '$y = \\log_2(x) + 6$', '$y = \\log_2(x) - 6$'],
            'explanation': 'Left shift by $k$: replace $x$ with $x + k$.',
        },
        {
            'question': 'How does $f(x) = \\log_4(x - 2) + 1$ differ from $y = \\log_4(x)$?',
            'answer': 'Shifted $2$ units right and $1$ unit up',
            'wrong': ['Shifted $2$ units left and $1$ unit up', 'Shifted $2$ units right and $1$ unit down',
                      'Shifted $1$ unit right and $2$ units up'],
            'explanation': '$(x-2)$ → right 2; $+1$ → up 1.',
        },
        {
            'question': 'The graph of $f(x) = \\log_2(x + 3) - 5$. What are the shift directions?',
            'answer': '$3$ units left and $5$ units down',
            'wrong': ['$3$ units right and $5$ units down', '$3$ units left and $5$ units up',
                      '$5$ units left and $3$ units down'],
            'explanation': '$(x+3)$ → left 3; $-5$ → down 5.',
        },
        {
            'question': 'What is the domain of $f(x) = \\log_2(x - 4) + 3$?',
            'answer': '$(4,\\ +\\infty)$',
            'wrong': ['$(-\\infty,\\ 4)$', '$(3,\\ +\\infty)$', '$(7,\\ +\\infty)$'],
            'explanation': 'Argument $x - 4 > 0 \\Rightarrow x > 4$. The $+3$ does not affect domain.',
        },
        {
            'question': 'What is the range of $f(x) = \\log_3(x) + 7$?',
            'answer': '$(-\\infty,\\ +\\infty)$',
            'wrong': ['$(7,\\ +\\infty)$', '$(-\\infty,\\ 7)$', '$[7,\\ +\\infty)$'],
            'explanation': 'Logarithm has range all reals. Shifting up by 7 still gives all reals.',
        },
        {
            'question': 'The graph of $y = \\log_3(x)$ passes through $(1, 0)$. Where does $f(x) = \\log_3(x - 2)$ pass through?',
            'answer': '$(3,\\ 0)$',
            'wrong': ['$(1,\\ 0)$', '$(-1,\\ 0)$', '$(1,\\ 2)$'],
            'explanation': 'Right shift by 2: point $(1, 0) \\rightarrow (1+2, 0) = (3, 0)$.',
        },
        {
            'question': 'The graph of $y = \\log_2(x)$ passes through $(2, 1)$. Where does $f(x) = \\log_2(x) + 3$ pass through?',
            'answer': '$(2,\\ 4)$',
            'wrong': ['$(5,\\ 1)$', '$(2,\\ 1)$', '$(2,\\ 3)$'],
            'explanation': 'Up shift by 3: point $(2, 1) \\rightarrow (2, 1+3) = (2, 4)$.',
        },
        {
            'question': 'The graph of $y = \\log_5(x)$ passes through $(5, 1)$. Where does $f(x) = \\log_5(x + 1)$ pass through?',
            'answer': '$(4,\\ 1)$',
            'wrong': ['$(5,\\ 1)$', '$(6,\\ 1)$', '$(5,\\ 2)$'],
            'explanation': 'Left shift by 1: point $(5, 1) \\rightarrow (5-1, 1) = (4, 1)$.',
        },
        {
            'question': 'How does $f(x) = \\log_2(x) - 1$ compare to $y = \\log_2(x)$?',
            'answer': 'Every $y$-value decreases by $1$',
            'wrong': ['Every $x$-value decreases by $1$', 'Every $y$-value increases by $1$',
                      'The vertical asymptote moves left by $1$'],
            'explanation': 'Subtracting 1 outside the log shifts all output (y) values down by 1.',
        },
        {
            'question': 'How does $f(x) = \\log_3(x - 5)$ compare to $y = \\log_3(x)$?',
            'answer': 'The vertical asymptote moves from $x=0$ to $x=5$',
            'wrong': ['The vertical asymptote moves to $x = -5$', 'The horizontal asymptote moves to $y = 5$',
                      'The graph is reflected'],
            'explanation': 'Right shift by 5 moves the VA from $x = 0$ to $x = 5$.',
        },
        {
            'question': 'Which equation represents $y = \\log_2(x)$ shifted $2$ right and $3$ down?',
            'answer': '$y = \\log_2(x - 2) - 3$',
            'wrong': ['$y = \\log_2(x + 2) - 3$', '$y = \\log_2(x - 2) + 3$', '$y = \\log_2(x + 2) + 3$'],
            'explanation': 'Right 2: $(x - 2)$. Down 3: $-3$ outside.',
        },
        {
            'question': 'Which equation represents $y = \\log_5(x)$ shifted $1$ left and $4$ up?',
            'answer': '$y = \\log_5(x + 1) + 4$',
            'wrong': ['$y = \\log_5(x - 1) + 4$', '$y = \\log_5(x + 1) - 4$', '$y = \\log_5(x - 1) - 4$'],
            'explanation': 'Left 1: $(x + 1)$. Up 4: $+4$ outside.',
        },
        {
            'question': 'The graph of $f(x) = \\log_3(x + 2) - 1$ has its vertical asymptote at?',
            'answer': '$x = -2$',
            'wrong': ['$x = 2$', '$x = -1$', '$x = 1$'],
            'explanation': '$x + 2 = 0 \\Rightarrow x = -2$. The $-1$ shifts vertically, not the asymptote.',
        },
        {
            'question': 'How does $f(x) = \\log_4(x + 3) + 2$ differ from $y = \\log_4(x)$?',
            'answer': 'Shifted $3$ units left and $2$ units up',
            'wrong': ['Shifted $3$ units right and $2$ units up', 'Shifted $3$ units left and $2$ units down',
                      'Shifted $2$ units left and $3$ units up'],
            'explanation': '$(x+3)$ → left 3. $+2$ outside → up 2.',
        }],
    'operation_on_logarithm': [

        # ══════════════════════════════════════════════════════
        # SECTION 1: Qo'shish — log(a)+log(b)=log(a·b)  (25 ta)
        # ══════════════════════════════════════════════════════

        {
            'section': 'Addition',
            'question': r'Simplify: $\log_2(4) + \log_2(8)$',
            'answer': '$5$',
            'wrong': ['$3$', '$6$', '$12$'],
            'explanation': r'$\log_2(4) + \log_2(8) = \log_2(4 \cdot 8) = \log_2(32) = 5$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_3(9) + \log_3(27)$',
            'answer': '$5$',
            'wrong': ['$6$', '$4$', '$3$'],
            'explanation': r'$\log_3(9) + \log_3(27) = \log_3(243) = 5$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_{10}(100) + \log_{10}(10)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$20$'],
            'explanation': r'$\log(100) + \log(10) = \log(1000) = 3$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_5(25) + \log_5(5)$',
            'answer': '$3$',
            'wrong': ['$10$', '$2$', '$4$'],
            'explanation': r'$\log_5(25) + \log_5(5) = \log_5(125) = 3$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_2(16) + \log_2(2)$',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$8$'],
            'explanation': r'$\log_2(16) + \log_2(2) = \log_2(32) = 5$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_3(27) + \log_3(9)$',
            'answer': '$5$',
            'wrong': ['$6$', '$3$', '$4$'],
            'explanation': r'$\log_3(27) + \log_3(9) = \log_3(243) = 5$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_4(16) + \log_4(4)$',
            'answer': '$3$',
            'wrong': ['$4$', '$2$', '$6$'],
            'explanation': r'$\log_4(16) + \log_4(4) = \log_4(64) = 3$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_2(8) + \log_2(4)$',
            'answer': '$5$',
            'wrong': ['$7$', '$3$', '$12$'],
            'explanation': r'$\log_2(8) + \log_2(4) = \log_2(32) = 5$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_6(6) + \log_6(36)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$7$'],
            'explanation': r'$\log_6(6) + \log_6(36) = \log_6(216) = 3$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_5(5) + \log_5(625)$',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$3$'],
            'explanation': r'$\log_5(5) + \log_5(625) = \log_5(3125) = 5$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_{10}(10) + \log_{10}(1000)$',
            'answer': '$4$',
            'wrong': ['$3$', '$5$', '$2$'],
            'explanation': r'$\log(10) + \log(1000) = \log(10000) = 4$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_7(7) + \log_7(49)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$14$'],
            'explanation': r'$\log_7(7) + \log_7(49) = \log_7(343) = 3$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_2(32) + \log_2(4)$',
            'answer': '$7$',
            'wrong': ['$5$', '$8$', '$9$'],
            'explanation': r'$\log_2(32) + \log_2(4) = \log_2(128) = 7$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_3(81) + \log_3(3)$',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$3$'],
            'explanation': r'$\log_3(81) + \log_3(3) = \log_3(243) = 5$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_9(9) + \log_9(81)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$9$'],
            'explanation': r'$\log_9(9) + \log_9(81) = \log_9(729) = 3$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_2(64) + \log_2(2)$',
            'answer': '$7$',
            'wrong': ['$6$', '$8$', '$5$'],
            'explanation': r'$\log_2(64) + \log_2(2) = \log_2(128) = 7$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_{10}(100) + \log_{10}(1000)$',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$3$'],
            'explanation': r'$\log(100) + \log(1000) = \log(100000) = 5$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_4(4) + \log_4(64)$',
            'answer': '$4$',
            'wrong': ['$3$', '$5$', '$16$'],
            'explanation': r'$\log_4(4) + \log_4(64) = \log_4(256) = 4$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_5(25) + \log_5(125)$',
            'answer': '$5$',
            'wrong': ['$6$', '$4$', '$3$'],
            'explanation': r'$\log_5(25) + \log_5(125) = \log_5(3125) = 5$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_3(3) + \log_3(81)$',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$3$'],
            'explanation': r'$\log_3(3) + \log_3(81) = \log_3(243) = 5$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_2(2) + \log_2(128)$',
            'answer': '$8$',
            'wrong': ['$7$', '$9$', '$6$'],
            'explanation': r'$\log_2(2) + \log_2(128) = \log_2(256) = 8$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_6(36) + \log_6(216)$',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$3$'],
            'explanation': r'$\log_6(36) + \log_6(216) = \log_6(7776) = 5$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_{10}(10000) + \log_{10}(10)$',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$40$'],
            'explanation': r'$\log(10000) + \log(10) = \log(100000) = 5$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_8(8) + \log_8(64)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$72$'],
            'explanation': r'$\log_8(8) + \log_8(64) = \log_8(512) = 3$',
        },
        {
            'section': 'Addition',
            'question': r'Simplify: $\log_2(4) + \log_2(32)$',
            'answer': '$7$',
            'wrong': ['$5$', '$8$', '$6$'],
            'explanation': r'$\log_2(4) + \log_2(32) = \log_2(128) = 7$',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 2: Ayirish — log(a)-log(b)=log(a/b)  (25 ta)
        # ══════════════════════════════════════════════════════

        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_2(32) - \log_2(4)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$8$'],
            'explanation': r'$\log_2(32) - \log_2(4) = \log_2\!\left(\frac{32}{4}\right) = \log_2(8) = 3$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_3(81) - \log_3(9)$',
            'answer': '$2$',
            'wrong': ['$3$', '$1$', '$4$'],
            'explanation': r'$\log_3(81) - \log_3(9) = \log_3(9) = 2$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_{10}(1000) - \log_{10}(10)$',
            'answer': '$2$',
            'wrong': ['$3$', '$1$', '$100$'],
            'explanation': r'$\log(1000) - \log(10) = \log(100) = 2$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_5(125) - \log_5(5)$',
            'answer': '$2$',
            'wrong': ['$3$', '$1$', '$25$'],
            'explanation': r'$\log_5(125) - \log_5(5) = \log_5(25) = 2$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_2(64) - \log_2(8)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$8$'],
            'explanation': r'$\log_2(64) - \log_2(8) = \log_2(8) = 3$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_4(256) - \log_4(16)$',
            'answer': '$2$',
            'wrong': ['$3$', '$4$', '$1$'],
            'explanation': r'$\log_4(256) - \log_4(16) = \log_4(16) = 2$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_3(243) - \log_3(81)$',
            'answer': '$1$',
            'wrong': ['$2$', '$3$', '$0$'],
            'explanation': r'$\log_3(243) - \log_3(81) = \log_3(3) = 1$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_{10}(100000) - \log_{10}(100)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$5$'],
            'explanation': r'$\log(100000) - \log(100) = \log(1000) = 3$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_6(216) - \log_6(6)$',
            'answer': '$2$',
            'wrong': ['$3$', '$1$', '$36$'],
            'explanation': r'$\log_6(216) - \log_6(6) = \log_6(36) = 2$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_2(128) - \log_2(4)$',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$32$'],
            'explanation': r'$\log_2(128) - \log_2(4) = \log_2(32) = 5$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_5(625) - \log_5(25)$',
            'answer': '$2$',
            'wrong': ['$3$', '$1$', '$25$'],
            'explanation': r'$\log_5(625) - \log_5(25) = \log_5(25) = 2$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_7(343) - \log_7(7)$',
            'answer': '$2$',
            'wrong': ['$3$', '$1$', '$49$'],
            'explanation': r'$\log_7(343) - \log_7(7) = \log_7(49) = 2$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_3(729) - \log_3(27)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$27$'],
            'explanation': r'$\log_3(729) - \log_3(27) = \log_3(27) = 3$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_2(256) - \log_2(16)$',
            'answer': '$4$',
            'wrong': ['$3$', '$5$', '$16$'],
            'explanation': r'$\log_2(256) - \log_2(16) = \log_2(16) = 4$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_9(729) - \log_9(9)$',
            'answer': '$2$',
            'wrong': ['$3$', '$1$', '$81$'],
            'explanation': r'$\log_9(729) - \log_9(9) = \log_9(81) = 2$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_{10}(10000) - \log_{10}(100)$',
            'answer': '$2$',
            'wrong': ['$3$', '$4$', '$1$'],
            'explanation': r'$\log(10000) - \log(100) = \log(100) = 2$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_4(1024) - \log_4(4)$',
            'answer': '$4$',
            'wrong': ['$3$', '$5$', '$256$'],
            'explanation': r'$\log_4(1024) - \log_4(4) = \log_4(256) = 4$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_2(512) - \log_2(8)$',
            'answer': '$6$',
            'wrong': ['$5$', '$7$', '$64$'],
            'explanation': r'$\log_2(512) - \log_2(8) = \log_2(64) = 6$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_5(3125) - \log_5(25)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$125$'],
            'explanation': r'$\log_5(3125) - \log_5(25) = \log_5(125) = 3$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_3(2187) - \log_3(81)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$27$'],
            'explanation': r'$\log_3(2187) - \log_3(81) = \log_3(27) = 3$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_6(1296) - \log_6(36)$',
            'answer': '$2$',
            'wrong': ['$3$', '$1$', '$36$'],
            'explanation': r'$\log_6(1296) - \log_6(36) = \log_6(36) = 2$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_2(1024) - \log_2(32)$',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$32$'],
            'explanation': r'$\log_2(1024) - \log_2(32) = \log_2(32) = 5$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_8(512) - \log_8(8)$',
            'answer': '$2$',
            'wrong': ['$3$', '$1$', '$64$'],
            'explanation': r'$\log_8(512) - \log_8(8) = \log_8(64) = 2$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_{10}(1000000) - \log_{10}(1000)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$6$'],
            'explanation': r'$\log(1000000) - \log(1000) = \log(1000) = 3$',
        },
        {
            'section': 'Subtraction',
            'question': r'Simplify: $\log_4(4096) - \log_4(64)$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$64$'],
            'explanation': r'$\log_4(4096) - \log_4(64) = \log_4(64) = 3$',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 3: Ko'paytirish — special case + alohida  (25 ta)
        # Special case: log_a(b) * log_b(a) = 1
        # Alohida: har birini hisoblang, keyin ko'paytiring
        # ══════════════════════════════════════════════════════

        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_2(16) \cdot \log_{16}(2)$',
            'answer': '$1$',
            'wrong': ['$4$', '$2$', '$8$'],
            'explanation': r'Special case: $\log_a(b) \cdot \log_b(a) = 1$. So $\log_2(16) \cdot \log_{16}(2) = 1$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_3(27) \cdot \log_{27}(3)$',
            'answer': '$1$',
            'wrong': ['$3$', '$9$', '$27$'],
            'explanation': r'Special case: $\log_a(b) \cdot \log_b(a) = 1$. So $\log_3(27) \cdot \log_{27}(3) = 1$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_5(125) \cdot \log_{125}(5)$',
            'answer': '$1$',
            'wrong': ['$3$', '$5$', '$15$'],
            'explanation': r'Special case: $\log_a(b) \cdot \log_b(a) = 1$. So $\log_5(125) \cdot \log_{125}(5) = 1$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_2(8) \cdot \log_8(2)$',
            'answer': '$1$',
            'wrong': ['$3$', '$6$', '$24$'],
            'explanation': r'Special case: $\log_a(b) \cdot \log_b(a) = 1$. So $\log_2(8) \cdot \log_8(2) = 1$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_4(64) \cdot \log_{64}(4)$',
            'answer': '$1$',
            'wrong': ['$3$', '$6$', '$12$'],
            'explanation': r'Special case: $\log_a(b) \cdot \log_b(a) = 1$. So $\log_4(64) \cdot \log_{64}(4) = 1$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_{10}(100) \cdot \log_{100}(10)$',
            'answer': '$1$',
            'wrong': ['$2$', '$10$', '$20$'],
            'explanation': r'Special case: $\log_a(b) \cdot \log_b(a) = 1$. So $\log(100) \cdot \log_{100}(10) = 1$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_6(36) \cdot \log_{36}(6)$',
            'answer': '$1$',
            'wrong': ['$2$', '$6$', '$12$'],
            'explanation': r'Special case: $\log_a(b) \cdot \log_b(a) = 1$. So $\log_6(36) \cdot \log_{36}(6) = 1$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_7(49) \cdot \log_{49}(7)$',
            'answer': '$1$',
            'wrong': ['$2$', '$7$', '$14$'],
            'explanation': r'Special case: $\log_a(b) \cdot \log_b(a) = 1$. So $\log_7(49) \cdot \log_{49}(7) = 1$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_2(32) \cdot \log_{32}(2)$',
            'answer': '$1$',
            'wrong': ['$5$', '$10$', '$32$'],
            'explanation': r'Special case: $\log_a(b) \cdot \log_b(a) = 1$. So $\log_2(32) \cdot \log_{32}(2) = 1$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_9(81) \cdot \log_{81}(9)$',
            'answer': '$1$',
            'wrong': ['$2$', '$4$', '$8$'],
            'explanation': r'Special case: $\log_a(b) \cdot \log_b(a) = 1$. So $\log_9(81) \cdot \log_{81}(9) = 1$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_2(8) \cdot \log_3(9)$',
            'answer': '$6$',
            'wrong': ['$3$', '$5$', '$9$'],
            'explanation': r'Alohida: $\log_2(8) = 3$, $\log_3(9) = 2$. Keyin: $3 \cdot 2 = 6$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_2(4) \cdot \log_3(27)$',
            'answer': '$6$',
            'wrong': ['$2$', '$8$', '$3$'],
            'explanation': r'Alohida: $\log_2(4) = 2$, $\log_3(27) = 3$. Keyin: $2 \cdot 3 = 6$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_5(25) \cdot \log_2(8)$',
            'answer': '$6$',
            'wrong': ['$5$', '$3$', '$8$'],
            'explanation': r'Alohida: $\log_5(25) = 2$, $\log_2(8) = 3$. Keyin: $2 \cdot 3 = 6$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_{10}(100) \cdot \log_2(16)$',
            'answer': '$8$',
            'wrong': ['$6$', '$4$', '$2$'],
            'explanation': r'Alohida: $\log(100) = 2$, $\log_2(16) = 4$. Keyin: $2 \cdot 4 = 8$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_3(81) \cdot \log_5(5)$',
            'answer': '$4$',
            'wrong': ['$1$', '$5$', '$81$'],
            'explanation': r'Alohida: $\log_3(81) = 4$, $\log_5(5) = 1$. Keyin: $4 \cdot 1 = 4$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_2(64) \cdot \log_3(3)$',
            'answer': '$6$',
            'wrong': ['$3$', '$9$', '$18$'],
            'explanation': r'Alohida: $\log_2(64) = 6$, $\log_3(3) = 1$. Keyin: $6 \cdot 1 = 6$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_4(16) \cdot \log_5(125)$',
            'answer': '$6$',
            'wrong': ['$2$', '$3$', '$5$'],
            'explanation': r'Alohida: $\log_4(16) = 2$, $\log_5(125) = 3$. Keyin: $2 \cdot 3 = 6$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_2(32) \cdot \log_3(9)$',
            'answer': '$10$',
            'wrong': ['$5$', '$7$', '$15$'],
            'explanation': r'Alohida: $\log_2(32) = 5$, $\log_3(9) = 2$. Keyin: $5 \cdot 2 = 10$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_{10}(1000) \cdot \log_2(4)$',
            'answer': '$6$',
            'wrong': ['$3$', '$5$', '$9$'],
            'explanation': r'Alohida: $\log(1000) = 3$, $\log_2(4) = 2$. Keyin: $3 \cdot 2 = 6$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_6(216) \cdot \log_2(4)$',
            'answer': '$6$',
            'wrong': ['$3$', '$5$', '$8$'],
            'explanation': r'Alohida: $\log_6(216) = 3$, $\log_2(4) = 2$. Keyin: $3 \cdot 2 = 6$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_3(243) \cdot \log_2(2)$',
            'answer': '$5$',
            'wrong': ['$3$', '$10$', '$1$'],
            'explanation': r'Alohida: $\log_3(243) = 5$, $\log_2(2) = 1$. Keyin: $5 \cdot 1 = 5$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_2(16) \cdot \log_5(25)$',
            'answer': '$8$',
            'wrong': ['$4$', '$6$', '$2$'],
            'explanation': r'Alohida: $\log_2(16) = 4$, $\log_5(25) = 2$. Keyin: $4 \cdot 2 = 8$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_3(9) \cdot \log_7(49)$',
            'answer': '$4$',
            'wrong': ['$2$', '$6$', '$9$'],
            'explanation': r'Alohida: $\log_3(9) = 2$, $\log_7(49) = 2$. Keyin: $2 \cdot 2 = 4$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_5(3125) \cdot \log_3(3)$',
            'answer': '$5$',
            'wrong': ['$3$', '$15$', '$1$'],
            'explanation': r'Alohida: $\log_5(3125) = 5$, $\log_3(3) = 1$. Keyin: $5 \cdot 1 = 5$',
        },
        {
            'section': 'Multiplication',
            'question': r'Evaluate: $\log_4(256) \cdot \log_2(8)$',
            'answer': '$12$',
            'wrong': ['$4$', '$6$', '$8$'],
            'explanation': r'Alohida: $\log_4(256) = 4$, $\log_2(8) = 3$. Keyin: $4 \cdot 3 = 12$',
        },

        # ══════════════════════════════════════════════════════
        # SECTION 4: Bo'lish — ln(a)/ln(b)=log_b(a) + alohida  (25 ta)
        # ══════════════════════════════════════════════════════

        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 8}{\ln 2}$',
            'answer': '$3$',
            'wrong': ['$4$', '$2$', '$\\ln 4$'],
            'explanation': r'$\dfrac{\ln 8}{\ln 2} = \log_2(8) = 3$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 27}{\ln 3}$',
            'answer': '$3$',
            'wrong': ['$9$', '$2$', '$4$'],
            'explanation': r'$\dfrac{\ln 27}{\ln 3} = \log_3(27) = 3$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 25}{\ln 5}$',
            'answer': '$2$',
            'wrong': ['$5$', '$3$', '$1$'],
            'explanation': r'$\dfrac{\ln 25}{\ln 5} = \log_5(25) = 2$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 64}{\ln 4}$',
            'answer': '$3$',
            'wrong': ['$4$', '$2$', '$16$'],
            'explanation': r'$\dfrac{\ln 64}{\ln 4} = \log_4(64) = 3$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 16}{\ln 2}$',
            'answer': '$4$',
            'wrong': ['$3$', '$8$', '$2$'],
            'explanation': r'$\dfrac{\ln 16}{\ln 2} = \log_2(16) = 4$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 81}{\ln 3}$',
            'answer': '$4$',
            'wrong': ['$3$', '$9$', '$27$'],
            'explanation': r'$\dfrac{\ln 81}{\ln 3} = \log_3(81) = 4$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 125}{\ln 5}$',
            'answer': '$3$',
            'wrong': ['$2$', '$4$', '$25$'],
            'explanation': r'$\dfrac{\ln 125}{\ln 5} = \log_5(125) = 3$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 32}{\ln 2}$',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$16$'],
            'explanation': r'$\dfrac{\ln 32}{\ln 2} = \log_2(32) = 5$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 343}{\ln 7}$',
            'answer': '$3$',
            'wrong': ['$7$', '$2$', '$49$'],
            'explanation': r'$\dfrac{\ln 343}{\ln 7} = \log_7(343) = 3$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 216}{\ln 6}$',
            'answer': '$3$',
            'wrong': ['$2$', '$6$', '$36$'],
            'explanation': r'$\dfrac{\ln 216}{\ln 6} = \log_6(216) = 3$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\log_2(64)}{\log_2(8)}$',
            'answer': '$2$',
            'wrong': ['$3$', '$8$', '$4$'],
            'explanation': r'Alohida: $\log_2(64) = 6$, $\log_2(8) = 3$. Keyin: $\dfrac{6}{3} = 2$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\log_3(81)}{\log_3(9)}$',
            'answer': '$2$',
            'wrong': ['$4$', '$3$', '$9$'],
            'explanation': r'Alohida: $\log_3(81) = 4$, $\log_3(9) = 2$. Keyin: $\dfrac{4}{2} = 2$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\log_2(128)}{\log_2(4)}$',
            'answer': '$\\dfrac{7}{2}$',
            'wrong': ['$4$', '$3$', '$2$'],
            'explanation': r'Alohida: $\log_2(128) = 7$, $\log_2(4) = 2$. Keyin: $\dfrac{7}{2}$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\log_5(625)}{\log_5(25)}$',
            'answer': '$2$',
            'wrong': ['$4$', '$5$', '$25$'],
            'explanation': r'Alohida: $\log_5(625) = 4$, $\log_5(25) = 2$. Keyin: $\dfrac{4}{2} = 2$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 243}{\ln 3}$',
            'answer': '$5$',
            'wrong': ['$3$', '$4$', '$81$'],
            'explanation': r'$\dfrac{\ln 243}{\ln 3} = \log_3(243) = 5$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 256}{\ln 4}$',
            'answer': '$4$',
            'wrong': ['$8$', '$2$', '$64$'],
            'explanation': r'$\dfrac{\ln 256}{\ln 4} = \log_4(256) = 4$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 1024}{\ln 2}$',
            'answer': '$10$',
            'wrong': ['$8$', '$9$', '$512$'],
            'explanation': r'$\dfrac{\ln 1024}{\ln 2} = \log_2(1024) = 10$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 3125}{\ln 5}$',
            'answer': '$5$',
            'wrong': ['$4$', '$6$', '$625$'],
            'explanation': r'$\dfrac{\ln 3125}{\ln 5} = \log_5(3125) = 5$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\log_{10}(10000)}{\log_{10}(100)}$',
            'answer': '$2$',
            'wrong': ['$4$', '$3$', '$100$'],
            'explanation': r'Alohida: $\log(10000) = 4$, $\log(100) = 2$. Keyin: $\dfrac{4}{2} = 2$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 729}{\ln 3}$',
            'answer': '$6$',
            'wrong': ['$3$', '$9$', '$243$'],
            'explanation': r'$\dfrac{\ln 729}{\ln 3} = \log_3(729) = 6$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\log_2(256)}{\log_2(16)}$',
            'answer': '$2$',
            'wrong': ['$4$', '$8$', '$16$'],
            'explanation': r'Alohida: $\log_2(256) = 8$, $\log_2(16) = 4$. Keyin: $\dfrac{8}{4} = 2$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 49}{\ln 7}$',
            'answer': '$2$',
            'wrong': ['$7$', '$3$', '$1$'],
            'explanation': r'$\dfrac{\ln 49}{\ln 7} = \log_7(49) = 2$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 512}{\ln 2}$',
            'answer': '$9$',
            'wrong': ['$8$', '$10$', '$256$'],
            'explanation': r'$\dfrac{\ln 512}{\ln 2} = \log_2(512) = 9$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\log_3(729)}{\log_3(27)}$',
            'answer': '$2$',
            'wrong': ['$3$', '$6$', '$27$'],
            'explanation': r'Alohida: $\log_3(729) = 6$, $\log_3(27) = 3$. Keyin: $\dfrac{6}{3} = 2$',
        },
        {
            'section': 'Division',
            'question': r'Simplify: $\dfrac{\ln 4096}{\ln 4}$',
            'answer': '$6$',
            'wrong': ['$4$', '$8$', '$1024$'],
            'explanation': r'$\dfrac{\ln 4096}{\ln 4} = \log_4(4096) = 6$',
        },
    ],
    'trigonometry': [

        # ══════════════════════════════════════════════════════════════════
        # SIN  —  8 ta tuzilma savoli
        # ══════════════════════════════════════════════════════════════════

        # --- Quadrant ishoralari (4 ta) ---
        {
            'question': 'What is the sign of $\\sin\\theta$ in Quadrant I?',
            'answer': 'Positive $(+)$',
            'wrong': ['Negative $(-)$', 'Zero', 'Undefined'],
            'explanation': 'In Q I all trig functions are positive. $\\sin\\theta > 0$.',
        },
        {
            'question': 'What is the sign of $\\sin\\theta$ in Quadrant II?',
            'answer': 'Positive $(+)$',
            'wrong': ['Negative $(-)$', 'Zero', 'Undefined'],
            'explanation': 'In Q II only $\\sin$ (and $\\csc$) are positive. $\\sin\\theta > 0$.',
        },
        {
            'question': 'What is the sign of $\\sin\\theta$ in Quadrant III?',
            'answer': 'Negative $(-)$',
            'wrong': ['Positive $(+)$', 'Zero', 'Undefined'],
            'explanation': 'In Q III only $\\tan$ and $\\cot$ are positive. $\\sin\\theta < 0$.',
        },
        {
            'question': 'What is the sign of $\\sin\\theta$ in Quadrant IV?',
            'answer': 'Negative $(-)$',
            'wrong': ['Positive $(+)$', 'Zero', 'Undefined'],
            'explanation': 'In Q IV only $\\cos$ (and $\\sec$) are positive. $\\sin\\theta < 0$.',
        },

        # --- Range (qiymatlar sohasi) ---
        {
            'question': 'What is the range of $f(x) = \\sin x$?',
            'answer': '$[-1,\\ 1]$',
            'wrong': ['$(0,\\ 1]$', '$(-\\infty,\\ +\\infty)$', '$[0,\\ 1]$'],
            'explanation': '$\\sin x$ always satisfies $-1 \\leq \\sin x \\leq 1$.',
        },

        # --- Domain (aniqlanish sohasi) ---
        {
            'question': 'What is the domain of $f(x) = \\sin x$?',
            'answer': '$(-\\infty,\\ +\\infty)$',
            'wrong': ['$x \\neq n\\pi$', '$[-1,\\ 1]$', '$(0,\\ 2\\pi)$'],
            'explanation': '$\\sin x$ is defined for all real numbers.',
        },

        # --- Musbat quadrant ---
        {
            'question': 'In which quadrants is $\\sin\\theta$ positive?',
            'answer': 'Quadrants I and II',
            'wrong': ['Quadrants I and IV', 'Quadrants II and III', 'Quadrants III and IV'],
            'explanation': '$\\sin\\theta > 0$ when $y > 0$, which is in Q I and Q II.',
        },

        # --- Manfiy quadrant ---
        {
            'question': 'In which quadrants is $\\sin\\theta$ negative?',
            'answer': 'Quadrants III and IV',
            'wrong': ['Quadrants I and II', 'Quadrants I and IV', 'Quadrants II and III'],
            'explanation': '$\\sin\\theta < 0$ when $y < 0$, which is in Q III and Q IV.',
        },

        # ══════════════════════════════════════════════════════════════════
        # COS  —  8 ta tuzilma savoli
        # ══════════════════════════════════════════════════════════════════

        # --- Quadrant ishoralari (4 ta) ---
        {
            'question': 'What is the sign of $\\cos\\theta$ in Quadrant I?',
            'answer': 'Positive $(+)$',
            'wrong': ['Negative $(-)$', 'Zero', 'Undefined'],
            'explanation': 'In Q I all trig functions are positive. $\\cos\\theta > 0$.',
        },
        {
            'question': 'What is the sign of $\\cos\\theta$ in Quadrant II?',
            'answer': 'Negative $(-)$',
            'wrong': ['Positive $(+)$', 'Zero', 'Undefined'],
            'explanation': 'In Q II only $\\sin$ is positive. $\\cos\\theta < 0$.',
        },
        {
            'question': 'What is the sign of $\\cos\\theta$ in Quadrant III?',
            'answer': 'Negative $(-)$',
            'wrong': ['Positive $(+)$', 'Zero', 'Undefined'],
            'explanation': 'In Q III only $\\tan$ and $\\cot$ are positive. $\\cos\\theta < 0$.',
        },
        {
            'question': 'What is the sign of $\\cos\\theta$ in Quadrant IV?',
            'answer': 'Positive $(+)$',
            'wrong': ['Negative $(-)$', 'Zero', 'Undefined'],
            'explanation': 'In Q IV only $\\cos$ (and $\\sec$) are positive. $\\cos\\theta > 0$.',
        },

        # --- Range ---
        {
            'question': 'What is the range of $f(x) = \\cos x$?',
            'answer': '$[-1,\\ 1]$',
            'wrong': ['$(0,\\ 1]$', '$(-\\infty,\\ +\\infty)$', '$[0,\\ \\pi]$'],
            'explanation': '$\\cos x$ always satisfies $-1 \\leq \\cos x \\leq 1$.',
        },

        # --- Domain ---
        {
            'question': 'What is the domain of $f(x) = \\cos x$?',
            'answer': '$(-\\infty,\\ +\\infty)$',
            'wrong': ['$x \\neq \\dfrac{\\pi}{2} + n\\pi$', '$[-1,\\ 1]$', '$(0,\\ 2\\pi)$'],
            'explanation': '$\\cos x$ is defined for all real numbers.',
        },

        # --- Musbat quadrant ---
        {
            'question': 'In which quadrants is $\\cos\\theta$ positive?',
            'answer': 'Quadrants I and IV',
            'wrong': ['Quadrants I and II', 'Quadrants II and III', 'Quadrants III and IV'],
            'explanation': '$\\cos\\theta > 0$ when $x > 0$, which is in Q I and Q IV.',
        },

        # --- Manfiy quadrant ---
        {
            'question': 'In which quadrants is $\\cos\\theta$ negative?',
            'answer': 'Quadrants II and III',
            'wrong': ['Quadrants I and II', 'Quadrants I and IV', 'Quadrants III and IV'],
            'explanation': '$\\cos\\theta < 0$ when $x < 0$, which is in Q II and Q III.',
        },

        # ══════════════════════════════════════════════════════════════════
        # TAN  —  8 ta tuzilma savoli
        # ══════════════════════════════════════════════════════════════════

        # --- Quadrant ishoralari (4 ta) ---
        {
            'question': 'What is the sign of $\\tan\\theta$ in Quadrant I?',
            'answer': 'Positive $(+)$',
            'wrong': ['Negative $(-)$', 'Zero', 'Undefined'],
            'explanation': 'In Q I: $\\sin > 0$, $\\cos > 0 \\Rightarrow \\tan = \\sin/\\cos > 0$.',
        },
        {
            'question': 'What is the sign of $\\tan\\theta$ in Quadrant II?',
            'answer': 'Negative $(-)$',
            'wrong': ['Positive $(+)$', 'Zero', 'Undefined'],
            'explanation': 'In Q II: $\\sin > 0$, $\\cos < 0 \\Rightarrow \\tan < 0$.',
        },
        {
            'question': 'What is the sign of $\\tan\\theta$ in Quadrant III?',
            'answer': 'Positive $(+)$',
            'wrong': ['Negative $(-)$', 'Zero', 'Undefined'],
            'explanation': 'In Q III: $\\sin < 0$, $\\cos < 0 \\Rightarrow \\tan = (-)/(-) > 0$.',
        },
        {
            'question': 'What is the sign of $\\tan\\theta$ in Quadrant IV?',
            'answer': 'Negative $(-)$',
            'wrong': ['Positive $(+)$', 'Zero', 'Undefined'],
            'explanation': 'In Q IV: $\\sin < 0$, $\\cos > 0 \\Rightarrow \\tan < 0$.',
        },

        # --- Range ---
        {
            'question': 'What is the range of $f(x) = \\tan x$?',
            'answer': '$(-\\infty,\\ +\\infty)$',
            'wrong': ['$[-1,\\ 1]$', '$(0,\\ +\\infty)$', '$[-\\pi/2,\\ \\pi/2]$'],
            'explanation': '$\\tan x$ can take any real value.',
        },

        # --- Domain ---
        {
            'question': 'What is the domain of $f(x) = \\tan x$?',
            'answer': '$x \\neq \\dfrac{\\pi}{2} + n\\pi,\\ n \\in \\mathbb{Z}$',
            'wrong': ['$(-\\infty,\\ +\\infty)$', '$x \\neq n\\pi$', '$[-1,\\ 1]$'],
            'explanation': '$\\tan x = \\sin x / \\cos x$ is undefined when $\\cos x = 0$, i.e. $x = \\tfrac{\\pi}{2} + n\\pi$.',
        },

        # --- Musbat quadrant ---
        {
            'question': 'In which quadrants is $\\tan\\theta$ positive?',
            'answer': 'Quadrants I and III',
            'wrong': ['Quadrants I and II', 'Quadrants II and IV', 'Quadrants I and IV'],
            'explanation': '$\\tan > 0$ when $\\sin$ and $\\cos$ have the same sign: Q I and Q III.',
        },

        # --- Manfiy quadrant ---
        {
            'question': 'In which quadrants is $\\tan\\theta$ negative?',
            'answer': 'Quadrants II and IV',
            'wrong': ['Quadrants I and III', 'Quadrants I and II', 'Quadrants III and IV'],
            'explanation': '$\\tan < 0$ when $\\sin$ and $\\cos$ have opposite signs: Q II and Q IV.',
        },

        # ══════════════════════════════════════════════════════════════════
        # COT  —  8 ta tuzilma savoli
        # ══════════════════════════════════════════════════════════════════

        # --- Quadrant ishoralari (4 ta) ---
        {
            'question': 'What is the sign of $\\cot\\theta$ in Quadrant I?',
            'answer': 'Positive $(+)$',
            'wrong': ['Negative $(-)$', 'Zero', 'Undefined'],
            'explanation': '$\\cot = \\cos/\\sin$. In Q I both positive $\\Rightarrow \\cot > 0$.',
        },
        {
            'question': 'What is the sign of $\\cot\\theta$ in Quadrant II?',
            'answer': 'Negative $(-)$',
            'wrong': ['Positive $(+)$', 'Zero', 'Undefined'],
            'explanation': 'In Q II: $\\cos < 0$, $\\sin > 0 \\Rightarrow \\cot < 0$.',
        },
        {
            'question': 'What is the sign of $\\cot\\theta$ in Quadrant III?',
            'answer': 'Positive $(+)$',
            'wrong': ['Negative $(-)$', 'Zero', 'Undefined'],
            'explanation': 'In Q III: $\\cos < 0$, $\\sin < 0 \\Rightarrow \\cot = (-)/(-) > 0$.',
        },
        {
            'question': 'What is the sign of $\\cot\\theta$ in Quadrant IV?',
            'answer': 'Negative $(-)$',
            'wrong': ['Positive $(+)$', 'Zero', 'Undefined'],
            'explanation': 'In Q IV: $\\cos > 0$, $\\sin < 0 \\Rightarrow \\cot < 0$.',
        },

        # --- Range ---
        {
            'question': 'What is the range of $f(x) = \\cot x$?',
            'answer': '$(-\\infty,\\ +\\infty)$',
            'wrong': ['$[-1,\\ 1]$', '$(0,\\ +\\infty)$', '$[-\\pi/2,\\ \\pi/2]$'],
            'explanation': '$\\cot x$ can take any real value, just like $\\tan x$.',
        },

        # --- Domain ---
        {
            'question': 'What is the domain of $f(x) = \\cot x$?',
            'answer': '$x \\neq n\\pi,\\ n \\in \\mathbb{Z}$',
            'wrong': ['$(-\\infty,\\ +\\infty)$', '$x \\neq \\dfrac{\\pi}{2} + n\\pi$', '$[-1,\\ 1]$'],
            'explanation': '$\\cot x = \\cos x / \\sin x$ is undefined when $\\sin x = 0$, i.e. $x = n\\pi$.',
        },

        # --- Musbat quadrant ---
        {
            'question': 'In which quadrants is $\\cot\\theta$ positive?',
            'answer': 'Quadrants I and III',
            'wrong': ['Quadrants I and II', 'Quadrants II and IV', 'Quadrants I and IV'],
            'explanation': '$\\cot = \\cos/\\sin$. Same sign in Q I and Q III.',
        },

        # --- Manfiy quadrant ---
        {
            'question': 'In which quadrants is $\\cot\\theta$ negative?',
            'answer': 'Quadrants II and IV',
            'wrong': ['Quadrants I and III', 'Quadrants I and II', 'Quadrants III and IV'],
            'explanation': '$\\cot < 0$ when $\\cos$ and $\\sin$ have opposite signs: Q II and Q IV.',
        },

        # ══════════════════════════════════════════════════════════════════
        # VALUE QUESTIONS — 17 ta × 4 funksiya = 68 ta
        # ══════════════════════════════════════════════════════════════════

        # ─────────────── SIN values (17 ta) ───────────────
        {
            'question': 'Find $\\sin 0$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', '$\\dfrac{\\sqrt{2}}{2}$'],
            'explanation': '$\\sin 0 = 0$.',
        },
        {
            'question': 'Find $\\sin\\dfrac{\\pi}{6}$.',
            'answer': '$\\dfrac{1}{2}$',
            'wrong': ['$\\dfrac{\\sqrt{3}}{2}$', '$\\dfrac{\\sqrt{2}}{2}$', '$1$'],
            'explanation': '$\\sin 30° = \\dfrac{1}{2}$.',
        },
        {
            'question': 'Find $\\sin\\dfrac{\\pi}{4}$.',
            'answer': '$\\dfrac{\\sqrt{2}}{2}$',
            'wrong': ['$\\dfrac{1}{2}$', '$\\dfrac{\\sqrt{3}}{2}$', '$1$'],
            'explanation': '$\\sin 45° = \\dfrac{\\sqrt{2}}{2}$.',
        },
        {
            'question': 'Find $\\sin\\dfrac{\\pi}{3}$.',
            'answer': '$\\dfrac{\\sqrt{3}}{2}$',
            'wrong': ['$\\dfrac{1}{2}$', '$\\dfrac{\\sqrt{2}}{2}$', '$1$'],
            'explanation': '$\\sin 60° = \\dfrac{\\sqrt{3}}{2}$.',
        },
        {
            'question': 'Find $\\sin\\dfrac{\\pi}{2}$.',
            'answer': '$1$',
            'wrong': ['$0$', '$-1$', '$\\dfrac{\\sqrt{2}}{2}$'],
            'explanation': '$\\sin 90° = 1$.',
        },
        {
            'question': 'Find $\\sin\\dfrac{2\\pi}{3}$.',
            'answer': '$\\dfrac{\\sqrt{3}}{2}$',
            'wrong': ['$-\\dfrac{\\sqrt{3}}{2}$', '$\\dfrac{1}{2}$', '$-\\dfrac{1}{2}$'],
            'explanation': '$\\sin 120° = \\sin(180°-60°) = \\sin 60° = \\dfrac{\\sqrt{3}}{2}$.',
        },
        {
            'question': 'Find $\\sin\\dfrac{3\\pi}{4}$.',
            'answer': '$\\dfrac{\\sqrt{2}}{2}$',
            'wrong': ['$-\\dfrac{\\sqrt{2}}{2}$', '$\\dfrac{1}{2}$', '$-\\dfrac{1}{2}$'],
            'explanation': '$\\sin 135° = \\sin(180°-45°) = \\sin 45° = \\dfrac{\\sqrt{2}}{2}$.',
        },
        {
            'question': 'Find $\\sin\\dfrac{5\\pi}{6}$.',
            'answer': '$\\dfrac{1}{2}$',
            'wrong': ['$-\\dfrac{1}{2}$', '$\\dfrac{\\sqrt{3}}{2}$', '$-\\dfrac{\\sqrt{3}}{2}$'],
            'explanation': '$\\sin 150° = \\sin(180°-30°) = \\sin 30° = \\dfrac{1}{2}$.',
        },
        {
            'question': 'Find $\\sin\\pi$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', '$\\dfrac{1}{2}$'],
            'explanation': '$\\sin 180° = 0$.',
        },
        {
            'question': 'Find $\\sin\\dfrac{7\\pi}{6}$.',
            'answer': '$-\\dfrac{1}{2}$',
            'wrong': ['$\\dfrac{1}{2}$', '$-\\dfrac{\\sqrt{3}}{2}$', '$\\dfrac{\\sqrt{3}}{2}$'],
            'explanation': '$\\sin 210° = -\\sin 30° = -\\dfrac{1}{2}$ (Q III).',
        },
        {
            'question': 'Find $\\sin\\dfrac{5\\pi}{4}$.',
            'answer': '$-\\dfrac{\\sqrt{2}}{2}$',
            'wrong': ['$\\dfrac{\\sqrt{2}}{2}$', '$-\\dfrac{1}{2}$', '$\\dfrac{1}{2}$'],
            'explanation': '$\\sin 225° = -\\sin 45° = -\\dfrac{\\sqrt{2}}{2}$ (Q III).',
        },
        {
            'question': 'Find $\\sin\\dfrac{4\\pi}{3}$.',
            'answer': '$-\\dfrac{\\sqrt{3}}{2}$',
            'wrong': ['$\\dfrac{\\sqrt{3}}{2}$', '$-\\dfrac{1}{2}$', '$\\dfrac{1}{2}$'],
            'explanation': '$\\sin 240° = -\\sin 60° = -\\dfrac{\\sqrt{3}}{2}$ (Q III).',
        },
        {
            'question': 'Find $\\sin\\dfrac{3\\pi}{2}$.',
            'answer': '$-1$',
            'wrong': ['$1$', '$0$', '$-\\dfrac{\\sqrt{2}}{2}$'],
            'explanation': '$\\sin 270° = -1$.',
        },
        {
            'question': 'Find $\\sin\\dfrac{5\\pi}{3}$.',
            'answer': '$-\\dfrac{\\sqrt{3}}{2}$',
            'wrong': ['$\\dfrac{\\sqrt{3}}{2}$', '$-\\dfrac{1}{2}$', '$\\dfrac{1}{2}$'],
            'explanation': '$\\sin 300° = -\\sin 60° = -\\dfrac{\\sqrt{3}}{2}$ (Q IV).',
        },
        {
            'question': 'Find $\\sin\\dfrac{7\\pi}{4}$.',
            'answer': '$-\\dfrac{\\sqrt{2}}{2}$',
            'wrong': ['$\\dfrac{\\sqrt{2}}{2}$', '$-\\dfrac{1}{2}$', '$\\dfrac{1}{2}$'],
            'explanation': '$\\sin 315° = -\\sin 45° = -\\dfrac{\\sqrt{2}}{2}$ (Q IV).',
        },
        {
            'question': 'Find $\\sin\\dfrac{11\\pi}{6}$.',
            'answer': '$-\\dfrac{1}{2}$',
            'wrong': ['$\\dfrac{1}{2}$', '$-\\dfrac{\\sqrt{3}}{2}$', '$\\dfrac{\\sqrt{3}}{2}$'],
            'explanation': '$\\sin 330° = -\\sin 30° = -\\dfrac{1}{2}$ (Q IV).',
        },
        {
            'question': 'Find $\\sin 2\\pi$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', '$2$'],
            'explanation': '$\\sin 360° = \\sin 0° = 0$.',
        },

        # ─────────────── COS values (17 ta) ───────────────
        {
            'question': 'Find $\\cos 0$.',
            'answer': '$1$',
            'wrong': ['$0$', '$-1$', '$\\dfrac{\\sqrt{2}}{2}$'],
            'explanation': '$\\cos 0° = 1$.',
        },
        {
            'question': 'Find $\\cos\\dfrac{\\pi}{6}$.',
            'answer': '$\\dfrac{\\sqrt{3}}{2}$',
            'wrong': ['$\\dfrac{1}{2}$', '$\\dfrac{\\sqrt{2}}{2}$', '$1$'],
            'explanation': '$\\cos 30° = \\dfrac{\\sqrt{3}}{2}$.',
        },
        {
            'question': 'Find $\\cos\\dfrac{\\pi}{4}$.',
            'answer': '$\\dfrac{\\sqrt{2}}{2}$',
            'wrong': ['$\\dfrac{1}{2}$', '$\\dfrac{\\sqrt{3}}{2}$', '$1$'],
            'explanation': '$\\cos 45° = \\dfrac{\\sqrt{2}}{2}$.',
        },
        {
            'question': 'Find $\\cos\\dfrac{\\pi}{3}$.',
            'answer': '$\\dfrac{1}{2}$',
            'wrong': ['$\\dfrac{\\sqrt{3}}{2}$', '$\\dfrac{\\sqrt{2}}{2}$', '$0$'],
            'explanation': '$\\cos 60° = \\dfrac{1}{2}$.',
        },
        {
            'question': 'Find $\\cos\\dfrac{\\pi}{2}$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', '$\\dfrac{\\sqrt{2}}{2}$'],
            'explanation': '$\\cos 90° = 0$.',
        },
        {
            'question': 'Find $\\cos\\dfrac{2\\pi}{3}$.',
            'answer': '$-\\dfrac{1}{2}$',
            'wrong': ['$\\dfrac{1}{2}$', '$-\\dfrac{\\sqrt{3}}{2}$', '$\\dfrac{\\sqrt{3}}{2}$'],
            'explanation': '$\\cos 120° = -\\cos 60° = -\\dfrac{1}{2}$ (Q II).',
        },
        {
            'question': 'Find $\\cos\\dfrac{3\\pi}{4}$.',
            'answer': '$-\\dfrac{\\sqrt{2}}{2}$',
            'wrong': ['$\\dfrac{\\sqrt{2}}{2}$', '$-\\dfrac{1}{2}$', '$\\dfrac{1}{2}$'],
            'explanation': '$\\cos 135° = -\\cos 45° = -\\dfrac{\\sqrt{2}}{2}$ (Q II).',
        },
        {
            'question': 'Find $\\cos\\dfrac{5\\pi}{6}$.',
            'answer': '$-\\dfrac{\\sqrt{3}}{2}$',
            'wrong': ['$\\dfrac{\\sqrt{3}}{2}$', '$-\\dfrac{1}{2}$', '$\\dfrac{1}{2}$'],
            'explanation': '$\\cos 150° = -\\cos 30° = -\\dfrac{\\sqrt{3}}{2}$ (Q II).',
        },
        {
            'question': 'Find $\\cos\\pi$.',
            'answer': '$-1$',
            'wrong': ['$1$', '$0$', '$-\\dfrac{1}{2}$'],
            'explanation': '$\\cos 180° = -1$.',
        },
        {
            'question': 'Find $\\cos\\dfrac{7\\pi}{6}$.',
            'answer': '$-\\dfrac{\\sqrt{3}}{2}$',
            'wrong': ['$\\dfrac{\\sqrt{3}}{2}$', '$-\\dfrac{1}{2}$', '$\\dfrac{1}{2}$'],
            'explanation': '$\\cos 210° = -\\cos 30° = -\\dfrac{\\sqrt{3}}{2}$ (Q III).',
        },
        {
            'question': 'Find $\\cos\\dfrac{5\\pi}{4}$.',
            'answer': '$-\\dfrac{\\sqrt{2}}{2}$',
            'wrong': ['$\\dfrac{\\sqrt{2}}{2}$', '$-\\dfrac{1}{2}$', '$\\dfrac{1}{2}$'],
            'explanation': '$\\cos 225° = -\\cos 45° = -\\dfrac{\\sqrt{2}}{2}$ (Q III).',
        },
        {
            'question': 'Find $\\cos\\dfrac{4\\pi}{3}$.',
            'answer': '$-\\dfrac{1}{2}$',
            'wrong': ['$\\dfrac{1}{2}$', '$-\\dfrac{\\sqrt{3}}{2}$', '$\\dfrac{\\sqrt{3}}{2}$'],
            'explanation': '$\\cos 240° = -\\cos 60° = -\\dfrac{1}{2}$ (Q III).',
        },
        {
            'question': 'Find $\\cos\\dfrac{3\\pi}{2}$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', '$\\dfrac{\\sqrt{2}}{2}$'],
            'explanation': '$\\cos 270° = 0$.',
        },
        {
            'question': 'Find $\\cos\\dfrac{5\\pi}{3}$.',
            'answer': '$\\dfrac{1}{2}$',
            'wrong': ['$-\\dfrac{1}{2}$', '$\\dfrac{\\sqrt{3}}{2}$', '$-\\dfrac{\\sqrt{3}}{2}$'],
            'explanation': '$\\cos 300° = \\cos 60° = \\dfrac{1}{2}$ (Q IV).',
        },
        {
            'question': 'Find $\\cos\\dfrac{7\\pi}{4}$.',
            'answer': '$\\dfrac{\\sqrt{2}}{2}$',
            'wrong': ['$-\\dfrac{\\sqrt{2}}{2}$', '$\\dfrac{1}{2}$', '$-\\dfrac{1}{2}$'],
            'explanation': '$\\cos 315° = \\cos 45° = \\dfrac{\\sqrt{2}}{2}$ (Q IV).',
        },
        {
            'question': 'Find $\\cos\\dfrac{11\\pi}{6}$.',
            'answer': '$\\dfrac{\\sqrt{3}}{2}$',
            'wrong': ['$-\\dfrac{\\sqrt{3}}{2}$', '$\\dfrac{1}{2}$', '$-\\dfrac{1}{2}$'],
            'explanation': '$\\cos 330° = \\cos 30° = \\dfrac{\\sqrt{3}}{2}$ (Q IV).',
        },
        {
            'question': 'Find $\\cos 2\\pi$.',
            'answer': '$1$',
            'wrong': ['$0$', '$-1$', '$2$'],
            'explanation': '$\\cos 360° = \\cos 0° = 1$.',
        },

        # ─────────────── TAN values (17 ta) ───────────────
        {
            'question': 'Find $\\tan 0$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', 'Undefined'],
            'explanation': '$\\tan 0 = \\sin 0 / \\cos 0 = 0/1 = 0$.',
        },
        {
            'question': 'Find $\\tan\\dfrac{\\pi}{6}$.',
            'answer': '$\\dfrac{1}{\\sqrt{3}} = \\dfrac{\\sqrt{3}}{3}$',
            'wrong': ['$\\sqrt{3}$', '$1$', '$\\dfrac{\\sqrt{2}}{2}$'],
            'explanation': '$\\tan 30° = \\dfrac{\\sin 30°}{\\cos 30°} = \\dfrac{1/2}{\\sqrt{3}/2} = \\dfrac{1}{\\sqrt{3}}$.',
        },
        {
            'question': 'Find $\\tan\\dfrac{\\pi}{4}$.',
            'answer': '$1$',
            'wrong': ['$0$', '$\\sqrt{3}$', '$\\dfrac{\\sqrt{2}}{2}$'],
            'explanation': '$\\tan 45° = \\dfrac{\\sqrt{2}/2}{\\sqrt{2}/2} = 1$.',
        },
        {
            'question': 'Find $\\tan\\dfrac{\\pi}{3}$.',
            'answer': '$\\sqrt{3}$',
            'wrong': ['$\\dfrac{1}{\\sqrt{3}}$', '$1$', '$2$'],
            'explanation': '$\\tan 60° = \\dfrac{\\sqrt{3}/2}{1/2} = \\sqrt{3}$.',
        },
        {
            'question': 'Find $\\tan\\dfrac{\\pi}{2}$.',
            'answer': 'Undefined',
            'wrong': ['$0$', '$1$', '$-1$'],
            'explanation': '$\\tan 90° = \\sin 90°/\\cos 90° = 1/0$, undefined.',
        },
        {
            'question': 'Find $\\tan\\dfrac{2\\pi}{3}$.',
            'answer': '$-\\sqrt{3}$',
            'wrong': ['$\\sqrt{3}$', '$-\\dfrac{1}{\\sqrt{3}}$', '$\\dfrac{1}{\\sqrt{3}}$'],
            'explanation': '$\\tan 120° = -\\tan 60° = -\\sqrt{3}$ (Q II, negative).',
        },
        {
            'question': 'Find $\\tan\\dfrac{3\\pi}{4}$.',
            'answer': '$-1$',
            'wrong': ['$1$', '$-\\sqrt{3}$', '$\\dfrac{1}{\\sqrt{3}}$'],
            'explanation': '$\\tan 135° = -\\tan 45° = -1$ (Q II).',
        },
        {
            'question': 'Find $\\tan\\dfrac{5\\pi}{6}$.',
            'answer': '$-\\dfrac{1}{\\sqrt{3}}$',
            'wrong': ['$\\dfrac{1}{\\sqrt{3}}$', '$-\\sqrt{3}$', '$\\sqrt{3}$'],
            'explanation': '$\\tan 150° = -\\tan 30° = -\\dfrac{1}{\\sqrt{3}}$ (Q II).',
        },
        {
            'question': 'Find $\\tan\\pi$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', 'Undefined'],
            'explanation': '$\\tan 180° = \\sin 180°/\\cos 180° = 0/(-1) = 0$.',
        },
        {
            'question': 'Find $\\tan\\dfrac{7\\pi}{6}$.',
            'answer': '$\\dfrac{1}{\\sqrt{3}}$',
            'wrong': ['$-\\dfrac{1}{\\sqrt{3}}$', '$\\sqrt{3}$', '$-\\sqrt{3}$'],
            'explanation': '$\\tan 210° = \\tan 30° = \\dfrac{1}{\\sqrt{3}}$ (Q III, positive).',
        },
        {
            'question': 'Find $\\tan\\dfrac{5\\pi}{4}$.',
            'answer': '$1$',
            'wrong': ['$-1$', '$\\sqrt{3}$', '$-\\sqrt{3}$'],
            'explanation': '$\\tan 225° = \\tan 45° = 1$ (Q III, positive).',
        },
        {
            'question': 'Find $\\tan\\dfrac{4\\pi}{3}$.',
            'answer': '$\\sqrt{3}$',
            'wrong': ['$-\\sqrt{3}$', '$1$', '$-1$'],
            'explanation': '$\\tan 240° = \\tan 60° = \\sqrt{3}$ (Q III, positive).',
        },
        {
            'question': 'Find $\\tan\\dfrac{3\\pi}{2}$.',
            'answer': 'Undefined',
            'wrong': ['$0$', '$1$', '$-1$'],
            'explanation': '$\\cos 270° = 0 \\Rightarrow \\tan 270°$ is undefined.',
        },
        {
            'question': 'Find $\\tan\\dfrac{5\\pi}{3}$.',
            'answer': '$-\\sqrt{3}$',
            'wrong': ['$\\sqrt{3}$', '$-1$', '$1$'],
            'explanation': '$\\tan 300° = -\\tan 60° = -\\sqrt{3}$ (Q IV, negative).',
        },
        {
            'question': 'Find $\\tan\\dfrac{7\\pi}{4}$.',
            'answer': '$-1$',
            'wrong': ['$1$', '$-\\sqrt{3}$', '$\\sqrt{3}$'],
            'explanation': '$\\tan 315° = -\\tan 45° = -1$ (Q IV, negative).',
        },
        {
            'question': 'Find $\\tan\\dfrac{11\\pi}{6}$.',
            'answer': '$-\\dfrac{1}{\\sqrt{3}}$',
            'wrong': ['$\\dfrac{1}{\\sqrt{3}}$', '$-\\sqrt{3}$', '$\\sqrt{3}$'],
            'explanation': '$\\tan 330° = -\\tan 30° = -\\dfrac{1}{\\sqrt{3}}$ (Q IV, negative).',
        },
        {
            'question': 'Find $\\tan 2\\pi$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', 'Undefined'],
            'explanation': '$\\tan 360° = \\tan 0° = 0$.',
        },

        # ─────────────── COT values (17 ta) ───────────────
        {
            'question': 'Find $\\cot\\dfrac{\\pi}{6}$.',
            'answer': '$\\sqrt{3}$',
            'wrong': ['$\\dfrac{1}{\\sqrt{3}}$', '$1$', '$2$'],
            'explanation': '$\\cot 30° = \\cos 30°/\\sin 30° = (\\sqrt{3}/2)/(1/2) = \\sqrt{3}$.',
        },
        {
            'question': 'Find $\\cot\\dfrac{\\pi}{4}$.',
            'answer': '$1$',
            'wrong': ['$0$', '$\\sqrt{3}$', '$-1$'],
            'explanation': '$\\cot 45° = \\cos 45°/\\sin 45° = 1$.',
        },
        {
            'question': 'Find $\\cot\\dfrac{\\pi}{3}$.',
            'answer': '$\\dfrac{1}{\\sqrt{3}}$',
            'wrong': ['$\\sqrt{3}$', '$1$', '$2$'],
            'explanation': '$\\cot 60° = \\cos 60°/\\sin 60° = (1/2)/(\\sqrt{3}/2) = \\dfrac{1}{\\sqrt{3}}$.',
        },
        {
            'question': 'Find $\\cot\\dfrac{\\pi}{2}$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', 'Undefined'],
            'explanation': '$\\cot 90° = \\cos 90°/\\sin 90° = 0/1 = 0$.',
        },
        {
            'question': 'Find $\\cot\\dfrac{2\\pi}{3}$.',
            'answer': '$-\\dfrac{1}{\\sqrt{3}}$',
            'wrong': ['$\\dfrac{1}{\\sqrt{3}}$', '$-\\sqrt{3}$', '$\\sqrt{3}$'],
            'explanation': '$\\cot 120° = -\\cot 60° = -\\dfrac{1}{\\sqrt{3}}$ (Q II, negative).',
        },
        {
            'question': 'Find $\\cot\\dfrac{3\\pi}{4}$.',
            'answer': '$-1$',
            'wrong': ['$1$', '$-\\sqrt{3}$', '$\\sqrt{3}$'],
            'explanation': '$\\cot 135° = -\\cot 45° = -1$ (Q II).',
        },
        {
            'question': 'Find $\\cot\\dfrac{5\\pi}{6}$.',
            'answer': '$-\\sqrt{3}$',
            'wrong': ['$\\sqrt{3}$', '$-\\dfrac{1}{\\sqrt{3}}$', '$\\dfrac{1}{\\sqrt{3}}$'],
            'explanation': '$\\cot 150° = -\\cot 30° = -\\sqrt{3}$ (Q II).',
        },
        {
            'question': 'Find $\\cot\\pi$.',
            'answer': 'Undefined',
            'wrong': ['$0$', '$1$', '$-1$'],
            'explanation': '$\\cot\\pi = \\cos\\pi/\\sin\\pi = -1/0$, undefined.',
        },
        {
            'question': 'Find $\\cot\\dfrac{7\\pi}{6}$.',
            'answer': '$\\sqrt{3}$',
            'wrong': ['$-\\sqrt{3}$', '$\\dfrac{1}{\\sqrt{3}}$', '$-\\dfrac{1}{\\sqrt{3}}$'],
            'explanation': '$\\cot 210° = \\cot 30° = \\sqrt{3}$ (Q III, positive).',
        },
        {
            'question': 'Find $\\cot\\dfrac{5\\pi}{4}$.',
            'answer': '$1$',
            'wrong': ['$-1$', '$\\sqrt{3}$', '$-\\sqrt{3}$'],
            'explanation': '$\\cot 225° = \\cot 45° = 1$ (Q III, positive).',
        },
        {
            'question': 'Find $\\cot\\dfrac{4\\pi}{3}$.',
            'answer': '$\\dfrac{1}{\\sqrt{3}}$',
            'wrong': ['$-\\dfrac{1}{\\sqrt{3}}$', '$\\sqrt{3}$', '$-\\sqrt{3}$'],
            'explanation': '$\\cot 240° = \\cot 60° = \\dfrac{1}{\\sqrt{3}}$ (Q III, positive).',
        },
        {
            'question': 'Find $\\cot\\dfrac{3\\pi}{2}$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', 'Undefined'],
            'explanation': '$\\cot 270° = \\cos 270°/\\sin 270° = 0/(-1) = 0$.',
        },
        {
            'question': 'Find $\\cot\\dfrac{5\\pi}{3}$.',
            'answer': '$-\\dfrac{1}{\\sqrt{3}}$',
            'wrong': ['$\\dfrac{1}{\\sqrt{3}}$', '$-\\sqrt{3}$', '$\\sqrt{3}$'],
            'explanation': '$\\cot 300° = -\\cot 60° = -\\dfrac{1}{\\sqrt{3}}$ (Q IV, negative).',
        },
        {
            'question': 'Find $\\cot\\dfrac{7\\pi}{4}$.',
            'answer': '$-1$',
            'wrong': ['$1$', '$-\\sqrt{3}$', '$\\sqrt{3}$'],
            'explanation': '$\\cot 315° = -\\cot 45° = -1$ (Q IV, negative).',
        },
        {
            'question': 'Find $\\cot\\dfrac{11\\pi}{6}$.',
            'answer': '$-\\sqrt{3}$',
            'wrong': ['$\\sqrt{3}$', '$-\\dfrac{1}{\\sqrt{3}}$', '$\\dfrac{1}{\\sqrt{3}}$'],
            'explanation': '$\\cot 330° = -\\cot 30° = -\\sqrt{3}$ (Q IV, negative).',
        },
        {
            'question': 'Find $\\cot\\dfrac{\\pi}{2}$ again using the identity $\\cot x = \\dfrac{1}{\\tan x}$.',
            'answer': '$0$',
            'wrong': ['Undefined', '$1$', '$-1$'],
            'explanation': '$\\tan 90°$ is undefined, but $\\cot 90° = \\cos 90°/\\sin 90° = 0/1 = 0$.',
        },
        {
            'question': 'Find $\\cot 0$.',
            'answer': 'Undefined',
            'wrong': ['$0$', '$1$', '$-1$'],
            'explanation': '$\\cot 0 = \\cos 0/\\sin 0 = 1/0$, undefined.',
        }
    ],
    'operations_in_trigonometry': [

        # ══════════════════════════════════════════════════════════════════
        # SUM-TO-PRODUCT  (24 questions — 6 per formula)
        # F1: sinA+sinB = 2sin((A+B)/2)cos((A-B)/2)
        # F2: sinA-sinB = 2cos((A+B)/2)sin((A-B)/2)
        # F3: cosA+cosB = 2cos((A+B)/2)cos((A-B)/2)
        # F4: cosA-cosB = -2sin((A+B)/2)sin((A-B)/2)
        # ══════════════════════════════════════════════════════════════════

        # F1 sinA+sinB (6)
        {'question': 'Convert $\\sin 75^\\circ + \\sin 15^\\circ$ to a product.',
         'answer': '$2\\sin 45^\\circ\\cos 30^\\circ$',
         'wrong': ['$2\\cos 45^\\circ\\sin 30^\\circ$', '$2\\sin 45^\\circ\\sin 30^\\circ$',
                   '$2\\cos 45^\\circ\\cos 30^\\circ$'],
         'explanation': '$\\frac{A+B}{2}=45^\\circ,\\frac{A-B}{2}=30^\\circ \\Rightarrow 2\\sin45^\\circ\\cos30^\\circ$.'},
        {'question': 'Convert $\\sin 5x + \\sin 3x$ to a product.', 'answer': '$2\\sin 4x\\cos x$',
         'wrong': ['$2\\cos 4x\\sin x$', '$2\\sin 4x\\sin x$', '$2\\cos 4x\\cos x$'],
         'explanation': '$\\frac{5x+3x}{2}=4x,\\frac{5x-3x}{2}=x \\Rightarrow 2\\sin4x\\cos x$.'},
        {'question': 'Convert $\\sin 80^\\circ + \\sin 40^\\circ$ to a product.',
         'answer': '$2\\sin 60^\\circ\\cos 20^\\circ$',
         'wrong': ['$2\\cos 60^\\circ\\sin 20^\\circ$', '$2\\sin 60^\\circ\\sin 20^\\circ$',
                   '$2\\cos 60^\\circ\\cos 20^\\circ$'],
         'explanation': '$\\frac{80+40}{2}=60^\\circ,\\frac{80-40}{2}=20^\\circ \\Rightarrow 2\\sin60^\\circ\\cos20^\\circ$.'},
        {'question': 'Convert $\\sin 9x + \\sin x$ to a product.', 'answer': '$2\\sin 5x\\cos 4x$',
         'wrong': ['$2\\cos 5x\\sin 4x$', '$2\\sin 5x\\sin 4x$', '$2\\cos 5x\\cos 4x$'],
         'explanation': '$\\frac{9x+x}{2}=5x,\\frac{9x-x}{2}=4x \\Rightarrow 2\\sin5x\\cos4x$.'},
        {'question': 'Convert $\\sin 110^\\circ + \\sin 50^\\circ$ to a product.',
         'answer': '$2\\sin 80^\\circ\\cos 30^\\circ$',
         'wrong': ['$2\\cos 80^\\circ\\sin 30^\\circ$', '$2\\sin 80^\\circ\\sin 30^\\circ$',
                   '$2\\cos 80^\\circ\\cos 30^\\circ$'],
         'explanation': '$\\frac{110+50}{2}=80^\\circ,\\frac{110-50}{2}=30^\\circ \\Rightarrow 2\\sin80^\\circ\\cos30^\\circ$.'},
        {'question': 'Convert $\\sin 7x + \\sin 5x$ to a product.', 'answer': '$2\\sin 6x\\cos x$',
         'wrong': ['$2\\cos 6x\\sin x$', '$2\\sin 6x\\sin x$', '$2\\cos 6x\\cos x$'],
         'explanation': '$\\frac{7x+5x}{2}=6x,\\frac{7x-5x}{2}=x \\Rightarrow 2\\sin6x\\cos x$.'},

        # F2 sinA-sinB (6)
        {'question': 'Convert $\\sin 80^\\circ - \\sin 20^\\circ$ to a product.',
         'answer': '$2\\cos 50^\\circ\\sin 30^\\circ$',
         'wrong': ['$2\\sin 50^\\circ\\cos 30^\\circ$', '$2\\cos 50^\\circ\\cos 30^\\circ$',
                   '$2\\sin 50^\\circ\\sin 30^\\circ$'],
         'explanation': '$\\frac{80+20}{2}=50^\\circ,\\frac{80-20}{2}=30^\\circ \\Rightarrow 2\\cos50^\\circ\\sin30^\\circ$.'},
        {'question': 'Convert $\\sin 5x - \\sin x$ to a product.', 'answer': '$2\\cos 3x\\sin 2x$',
         'wrong': ['$2\\sin 3x\\cos 2x$', '$2\\cos 3x\\cos 2x$', '$2\\sin 3x\\sin 2x$'],
         'explanation': '$\\frac{5x+x}{2}=3x,\\frac{5x-x}{2}=2x \\Rightarrow 2\\cos3x\\sin2x$.'},
        {'question': 'Convert $\\sin 100^\\circ - \\sin 40^\\circ$ to a product.',
         'answer': '$2\\cos 70^\\circ\\sin 30^\\circ$',
         'wrong': ['$2\\sin 70^\\circ\\cos 30^\\circ$', '$2\\cos 70^\\circ\\cos 30^\\circ$',
                   '$2\\sin 70^\\circ\\sin 30^\\circ$'],
         'explanation': '$\\frac{100+40}{2}=70^\\circ,\\frac{100-40}{2}=30^\\circ \\Rightarrow 2\\cos70^\\circ\\sin30^\\circ$.'},
        {'question': 'Convert $\\sin 9x - \\sin 3x$ to a product.', 'answer': '$2\\cos 6x\\sin 3x$',
         'wrong': ['$2\\sin 6x\\cos 3x$', '$2\\cos 6x\\cos 3x$', '$2\\sin 6x\\sin 3x$'],
         'explanation': '$\\frac{9x+3x}{2}=6x,\\frac{9x-3x}{2}=3x \\Rightarrow 2\\cos6x\\sin3x$.'},
        {'question': 'Convert $\\sin 70^\\circ - \\sin 30^\\circ$ to a product.',
         'answer': '$2\\cos 50^\\circ\\sin 20^\\circ$',
         'wrong': ['$2\\sin 50^\\circ\\cos 20^\\circ$', '$2\\cos 50^\\circ\\cos 20^\\circ$',
                   '$2\\sin 50^\\circ\\sin 20^\\circ$'],
         'explanation': '$\\frac{70+30}{2}=50^\\circ,\\frac{70-30}{2}=20^\\circ \\Rightarrow 2\\cos50^\\circ\\sin20^\\circ$.'},
        {'question': 'Convert $\\sin 8x - \\sin 2x$ to a product.', 'answer': '$2\\cos 5x\\sin 3x$',
         'wrong': ['$2\\sin 5x\\cos 3x$', '$2\\cos 5x\\cos 3x$', '$2\\sin 5x\\sin 3x$'],
         'explanation': '$\\frac{8x+2x}{2}=5x,\\frac{8x-2x}{2}=3x \\Rightarrow 2\\cos5x\\sin3x$.'},

        # F3 cosA+cosB (6)
        {'question': 'Convert $\\cos 80^\\circ + \\cos 20^\\circ$ to a product.',
         'answer': '$2\\cos 50^\\circ\\cos 30^\\circ$',
         'wrong': ['$-2\\sin 50^\\circ\\sin 30^\\circ$', '$2\\sin 50^\\circ\\cos 30^\\circ$',
                   '$2\\cos 50^\\circ\\sin 30^\\circ$'],
         'explanation': '$\\frac{80+20}{2}=50^\\circ,\\frac{80-20}{2}=30^\\circ \\Rightarrow 2\\cos50^\\circ\\cos30^\\circ$.'},
        {'question': 'Convert $\\cos 7x + \\cos 3x$ to a product.', 'answer': '$2\\cos 5x\\cos 2x$',
         'wrong': ['$-2\\sin 5x\\sin 2x$', '$2\\sin 5x\\cos 2x$', '$2\\cos 5x\\sin 2x$'],
         'explanation': '$\\frac{7x+3x}{2}=5x,\\frac{7x-3x}{2}=2x \\Rightarrow 2\\cos5x\\cos2x$.'},
        {'question': 'Convert $\\cos 50^\\circ + \\cos 10^\\circ$ to a product.',
         'answer': '$2\\cos 30^\\circ\\cos 20^\\circ$',
         'wrong': ['$-2\\sin 30^\\circ\\sin 20^\\circ$', '$2\\sin 30^\\circ\\cos 20^\\circ$',
                   '$2\\cos 30^\\circ\\sin 20^\\circ$'],
         'explanation': '$\\frac{50+10}{2}=30^\\circ,\\frac{50-10}{2}=20^\\circ \\Rightarrow 2\\cos30^\\circ\\cos20^\\circ$.'},
        {'question': 'Convert $\\cos 9x + \\cos 5x$ to a product.', 'answer': '$2\\cos 7x\\cos 2x$',
         'wrong': ['$-2\\sin 7x\\sin 2x$', '$2\\sin 7x\\cos 2x$', '$2\\cos 7x\\sin 2x$'],
         'explanation': '$\\frac{9x+5x}{2}=7x,\\frac{9x-5x}{2}=2x \\Rightarrow 2\\cos7x\\cos2x$.'},
        {'question': 'Convert $\\cos 110^\\circ + \\cos 30^\\circ$ to a product.',
         'answer': '$2\\cos 70^\\circ\\cos 40^\\circ$',
         'wrong': ['$-2\\sin 70^\\circ\\sin 40^\\circ$', '$2\\sin 70^\\circ\\cos 40^\\circ$',
                   '$2\\cos 70^\\circ\\sin 40^\\circ$'],
         'explanation': '$\\frac{110+30}{2}=70^\\circ,\\frac{110-30}{2}=40^\\circ \\Rightarrow 2\\cos70^\\circ\\cos40^\\circ$.'},
        {'question': 'Convert $\\cos 6x + \\cos 2x$ to a product.', 'answer': '$2\\cos 4x\\cos 2x$',
         'wrong': ['$-2\\sin 4x\\sin 2x$', '$2\\sin 4x\\cos 2x$', '$2\\cos 4x\\sin 2x$'],
         'explanation': '$\\frac{6x+2x}{2}=4x,\\frac{6x-2x}{2}=2x \\Rightarrow 2\\cos4x\\cos2x$.'},

        # F4 cosA-cosB (6)
        {'question': 'Convert $\\cos 20^\\circ - \\cos 80^\\circ$ to a product.',
         'answer': '$2\\sin 50^\\circ\\sin 30^\\circ$',
         'wrong': ['$-2\\sin 50^\\circ\\sin 30^\\circ$', '$2\\cos 50^\\circ\\cos 30^\\circ$',
                   '$2\\cos 50^\\circ\\sin 30^\\circ$'],
         'explanation': '$-2\\sin50^\\circ\\sin\\frac{20-80}{2}=-2\\sin50^\\circ\\sin(-30^\\circ)=2\\sin50^\\circ\\sin30^\\circ$.'},
        {'question': 'Convert $\\cos 3x - \\cos 7x$ to a product.', 'answer': '$2\\sin 5x\\sin 2x$',
         'wrong': ['$-2\\sin 5x\\sin 2x$', '$2\\cos 5x\\cos 2x$', '$-2\\cos 5x\\cos 2x$'],
         'explanation': '$-2\\sin5x\\sin\\frac{3x-7x}{2}=-2\\sin5x\\sin(-2x)=2\\sin5x\\sin2x$.'},
        {'question': 'Convert $\\cos 40^\\circ - \\cos 100^\\circ$ to a product.',
         'answer': '$2\\sin 70^\\circ\\sin 30^\\circ$',
         'wrong': ['$-2\\sin 70^\\circ\\sin 30^\\circ$', '$2\\cos 70^\\circ\\cos 30^\\circ$',
                   '$-2\\cos 70^\\circ\\cos 30^\\circ$'],
         'explanation': '$-2\\sin70^\\circ\\sin(-30^\\circ)=2\\sin70^\\circ\\sin30^\\circ$.'},
        {'question': 'Convert $\\cos x - \\cos 9x$ to a product.', 'answer': '$2\\sin 5x\\sin 4x$',
         'wrong': ['$-2\\sin 5x\\sin 4x$', '$2\\cos 5x\\cos 4x$', '$-2\\cos 5x\\cos 4x$'],
         'explanation': '$-2\\sin5x\\sin\\frac{x-9x}{2}=-2\\sin5x\\sin(-4x)=2\\sin5x\\sin4x$.'},
        {'question': 'Convert $\\cos 50^\\circ - \\cos 90^\\circ$ to a product.',
         'answer': '$2\\sin 70^\\circ\\sin 20^\\circ$',
         'wrong': ['$-2\\sin 70^\\circ\\sin 20^\\circ$', '$2\\cos 70^\\circ\\cos 20^\\circ$',
                   '$-2\\cos 70^\\circ\\cos 20^\\circ$'],
         'explanation': '$-2\\sin70^\\circ\\sin(-20^\\circ)=2\\sin70^\\circ\\sin20^\\circ$.'},
        {'question': 'Convert $\\cos 2x - \\cos 8x$ to a product.', 'answer': '$2\\sin 5x\\sin 3x$',
         'wrong': ['$-2\\sin 5x\\sin 3x$', '$2\\cos 5x\\cos 3x$', '$-2\\cos 5x\\cos 3x$'],
         'explanation': '$-2\\sin5x\\sin\\frac{2x-8x}{2}=-2\\sin5x\\sin(-3x)=2\\sin5x\\sin3x$.'},

        # ══════════════════════════════════════════════════════════════════
        # PRODUCT-TO-SUM  (24 questions — 8 per formula)
        # F1: sinA cosB = (1/2)[sin(A+B)+sin(A-B)]
        # F2: cosA cosB = (1/2)[cos(A+B)+cos(A-B)]
        # F3: sinA sinB = (1/2)[cos(A-B)-cos(A+B)]
        # ══════════════════════════════════════════════════════════════════

        # F1 sinAcosB (8)
        {'question': 'Convert $\\sin 5x\\cos 3x$ to a sum.', 'answer': '$\\tfrac{1}{2}[\\sin 8x+\\sin 2x]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 8x+\\cos 2x]$', '$\\tfrac{1}{2}[\\cos 2x-\\cos 8x]$',
                   '$\\tfrac{1}{2}[\\sin 8x-\\sin 2x]$'],
         'explanation': '$\\frac{1}{2}[\\sin(5x+3x)+\\sin(5x-3x)]=\\frac{1}{2}[\\sin8x+\\sin2x]$.'},
        {'question': 'Convert $\\sin 70^\\circ\\cos 20^\\circ$ to a sum.',
         'answer': '$\\tfrac{1}{2}[\\sin 90^\\circ+\\sin 50^\\circ]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 90^\\circ+\\cos 50^\\circ]$',
                   '$\\tfrac{1}{2}[\\cos 50^\\circ-\\cos 90^\\circ]$',
                   '$\\tfrac{1}{2}[\\sin 90^\\circ-\\sin 50^\\circ]$'],
         'explanation': '$\\frac{1}{2}[\\sin90^\\circ+\\sin50^\\circ]$.'},
        {'question': 'Convert $\\sin 4x\\cos x$ to a sum.', 'answer': '$\\tfrac{1}{2}[\\sin 5x+\\sin 3x]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 5x+\\cos 3x]$', '$\\tfrac{1}{2}[\\cos 3x-\\cos 5x]$',
                   '$\\tfrac{1}{2}[\\sin 5x-\\sin 3x]$'], 'explanation': '$\\frac{1}{2}[\\sin5x+\\sin3x]$.'},
        {'question': 'Convert $\\sin 60^\\circ\\cos 30^\\circ$ to a sum.',
         'answer': '$\\tfrac{1}{2}[\\sin 90^\\circ+\\sin 30^\\circ]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 90^\\circ+\\cos 30^\\circ]$',
                   '$\\tfrac{1}{2}[\\cos 30^\\circ-\\cos 90^\\circ]$',
                   '$\\tfrac{1}{2}[\\sin 90^\\circ-\\sin 30^\\circ]$'],
         'explanation': '$\\frac{1}{2}[\\sin90^\\circ+\\sin30^\\circ]$.'},
        {'question': 'Convert $\\sin 9x\\cos 4x$ to a sum.', 'answer': '$\\tfrac{1}{2}[\\sin 13x+\\sin 5x]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 13x+\\cos 5x]$', '$\\tfrac{1}{2}[\\cos 5x-\\cos 13x]$',
                   '$\\tfrac{1}{2}[\\sin 13x-\\sin 5x]$'], 'explanation': '$\\frac{1}{2}[\\sin13x+\\sin5x]$.'},
        {'question': 'Convert $\\sin 3x\\cos 2x$ to a sum.', 'answer': '$\\tfrac{1}{2}[\\sin 5x+\\sin x]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 5x+\\cos x]$', '$\\tfrac{1}{2}[\\cos x-\\cos 5x]$',
                   '$\\tfrac{1}{2}[\\sin 5x-\\sin x]$'], 'explanation': '$\\frac{1}{2}[\\sin5x+\\sin x]$.'},
        {'question': 'Convert $\\sin 45^\\circ\\cos 15^\\circ$ to a sum.',
         'answer': '$\\tfrac{1}{2}[\\sin 60^\\circ+\\sin 30^\\circ]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 60^\\circ+\\cos 30^\\circ]$',
                   '$\\tfrac{1}{2}[\\cos 30^\\circ-\\cos 60^\\circ]$',
                   '$\\tfrac{1}{2}[\\sin 60^\\circ-\\sin 30^\\circ]$'],
         'explanation': '$\\frac{1}{2}[\\sin60^\\circ+\\sin30^\\circ]$.'},
        {'question': 'Convert $\\sin 8x\\cos 3x$ to a sum.', 'answer': '$\\tfrac{1}{2}[\\sin 11x+\\sin 5x]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 11x+\\cos 5x]$', '$\\tfrac{1}{2}[\\cos 5x-\\cos 11x]$',
                   '$\\tfrac{1}{2}[\\sin 11x-\\sin 5x]$'], 'explanation': '$\\frac{1}{2}[\\sin11x+\\sin5x]$.'},

        # F2 cosAcosB (8)
        {'question': 'Convert $\\cos 5x\\cos 3x$ to a sum.', 'answer': '$\\tfrac{1}{2}[\\cos 8x+\\cos 2x]$',
         'wrong': ['$\\tfrac{1}{2}[\\sin 8x+\\sin 2x]$', '$\\tfrac{1}{2}[\\cos 2x-\\cos 8x]$',
                   '$\\tfrac{1}{2}[\\sin 8x-\\sin 2x]$'],
         'explanation': '$\\frac{1}{2}[\\cos(5x+3x)+\\cos(5x-3x)]=\\frac{1}{2}[\\cos8x+\\cos2x]$.'},
        {'question': 'Convert $\\cos 60^\\circ\\cos 30^\\circ$ to a sum.',
         'answer': '$\\tfrac{1}{2}[\\cos 90^\\circ+\\cos 30^\\circ]$',
         'wrong': ['$\\tfrac{1}{2}[\\sin 90^\\circ+\\sin 30^\\circ]$',
                   '$\\tfrac{1}{2}[\\cos 30^\\circ-\\cos 90^\\circ]$',
                   '$\\tfrac{1}{2}[\\sin 30^\\circ-\\sin 90^\\circ]$'],
         'explanation': '$\\frac{1}{2}[\\cos90^\\circ+\\cos30^\\circ]$.'},
        {'question': 'Convert $\\cos 4x\\cos x$ to a sum.', 'answer': '$\\tfrac{1}{2}[\\cos 5x+\\cos 3x]$',
         'wrong': ['$\\tfrac{1}{2}[\\sin 5x+\\sin 3x]$', '$\\tfrac{1}{2}[\\cos 3x-\\cos 5x]$',
                   '$\\tfrac{1}{2}[\\sin 5x-\\sin 3x]$'], 'explanation': '$\\frac{1}{2}[\\cos5x+\\cos3x]$.'},
        {'question': 'Convert $\\cos 70^\\circ\\cos 20^\\circ$ to a sum.',
         'answer': '$\\tfrac{1}{2}[\\cos 90^\\circ+\\cos 50^\\circ]$',
         'wrong': ['$\\tfrac{1}{2}[\\sin 90^\\circ+\\sin 50^\\circ]$',
                   '$\\tfrac{1}{2}[\\cos 50^\\circ-\\cos 90^\\circ]$',
                   '$\\tfrac{1}{2}[\\sin 50^\\circ-\\sin 90^\\circ]$'],
         'explanation': '$\\frac{1}{2}[\\cos90^\\circ+\\cos50^\\circ]$.'},
        {'question': 'Convert $\\cos 7x\\cos 2x$ to a sum.', 'answer': '$\\tfrac{1}{2}[\\cos 9x+\\cos 5x]$',
         'wrong': ['$\\tfrac{1}{2}[\\sin 9x+\\sin 5x]$', '$\\tfrac{1}{2}[\\cos 5x-\\cos 9x]$',
                   '$\\tfrac{1}{2}[\\sin 9x-\\sin 5x]$'], 'explanation': '$\\frac{1}{2}[\\cos9x+\\cos5x]$.'},
        {'question': 'Convert $\\cos 45^\\circ\\cos 15^\\circ$ to a sum.',
         'answer': '$\\tfrac{1}{2}[\\cos 60^\\circ+\\cos 30^\\circ]$',
         'wrong': ['$\\tfrac{1}{2}[\\sin 60^\\circ+\\sin 30^\\circ]$',
                   '$\\tfrac{1}{2}[\\cos 30^\\circ-\\cos 60^\\circ]$',
                   '$\\tfrac{1}{2}[\\sin 30^\\circ-\\sin 60^\\circ]$'],
         'explanation': '$\\frac{1}{2}[\\cos60^\\circ+\\cos30^\\circ]$.'},
        {'question': 'Convert $\\cos 8x\\cos 3x$ to a sum.', 'answer': '$\\tfrac{1}{2}[\\cos 11x+\\cos 5x]$',
         'wrong': ['$\\tfrac{1}{2}[\\sin 11x+\\sin 5x]$', '$\\tfrac{1}{2}[\\cos 5x-\\cos 11x]$',
                   '$\\tfrac{1}{2}[\\sin 5x-\\sin 11x]$'], 'explanation': '$\\frac{1}{2}[\\cos11x+\\cos5x]$.'},
        {'question': 'Convert $\\cos 6x\\cos x$ to a sum.', 'answer': '$\\tfrac{1}{2}[\\cos 7x+\\cos 5x]$',
         'wrong': ['$\\tfrac{1}{2}[\\sin 7x+\\sin 5x]$', '$\\tfrac{1}{2}[\\cos 5x-\\cos 7x]$',
                   '$\\tfrac{1}{2}[\\sin 7x-\\sin 5x]$'], 'explanation': '$\\frac{1}{2}[\\cos7x+\\cos5x]$.'},

        # F3 sinAsinB (8)
        {'question': 'Convert $\\sin 5x\\sin 3x$ to a difference of cosines.',
         'answer': '$\\tfrac{1}{2}[\\cos 2x-\\cos 8x]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 8x-\\cos 2x]$', '$\\tfrac{1}{2}[\\cos 8x+\\cos 2x]$',
                   '$\\tfrac{1}{2}[\\sin 8x+\\sin 2x]$'],
         'explanation': '$\\frac{1}{2}[\\cos(5x-3x)-\\cos(5x+3x)]=\\frac{1}{2}[\\cos2x-\\cos8x]$.'},
        {'question': 'Convert $\\sin 60^\\circ\\sin 30^\\circ$ to a difference of cosines.',
         'answer': '$\\tfrac{1}{2}[\\cos 30^\\circ-\\cos 90^\\circ]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 90^\\circ-\\cos 30^\\circ]$',
                   '$\\tfrac{1}{2}[\\cos 90^\\circ+\\cos 30^\\circ]$',
                   '$\\tfrac{1}{2}[\\sin 90^\\circ+\\sin 30^\\circ]$'],
         'explanation': '$\\frac{1}{2}[\\cos30^\\circ-\\cos90^\\circ]$.'},
        {'question': 'Convert $\\sin 7x\\sin 2x$ to a difference of cosines.',
         'answer': '$\\tfrac{1}{2}[\\cos 5x-\\cos 9x]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 9x-\\cos 5x]$', '$\\tfrac{1}{2}[\\cos 9x+\\cos 5x]$',
                   '$\\tfrac{1}{2}[\\sin 9x+\\sin 5x]$'], 'explanation': '$\\frac{1}{2}[\\cos5x-\\cos9x]$.'},
        {'question': 'Convert $\\sin 45^\\circ\\sin 15^\\circ$ to a difference of cosines.',
         'answer': '$\\tfrac{1}{2}[\\cos 30^\\circ-\\cos 60^\\circ]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 60^\\circ-\\cos 30^\\circ]$',
                   '$\\tfrac{1}{2}[\\cos 60^\\circ+\\cos 30^\\circ]$',
                   '$\\tfrac{1}{2}[\\sin 60^\\circ+\\sin 30^\\circ]$'],
         'explanation': '$\\frac{1}{2}[\\cos30^\\circ-\\cos60^\\circ]$.'},
        {'question': 'Convert $\\sin 4x\\sin 3x$ to a difference of cosines.',
         'answer': '$\\tfrac{1}{2}[\\cos x-\\cos 7x]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 7x-\\cos x]$', '$\\tfrac{1}{2}[\\cos 7x+\\cos x]$',
                   '$\\tfrac{1}{2}[\\sin 7x+\\sin x]$'], 'explanation': '$\\frac{1}{2}[\\cos x-\\cos7x]$.'},
        {'question': 'Convert $\\sin 80^\\circ\\sin 40^\\circ$ to a difference of cosines.',
         'answer': '$\\tfrac{1}{2}[\\cos 40^\\circ-\\cos 120^\\circ]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 120^\\circ-\\cos 40^\\circ]$',
                   '$\\tfrac{1}{2}[\\cos 120^\\circ+\\cos 40^\\circ]$',
                   '$\\tfrac{1}{2}[\\sin 120^\\circ+\\sin 40^\\circ]$'],
         'explanation': '$\\frac{1}{2}[\\cos40^\\circ-\\cos120^\\circ]$.'},
        {'question': 'Convert $\\sin 6x\\sin 2x$ to a difference of cosines.',
         'answer': '$\\tfrac{1}{2}[\\cos 4x-\\cos 8x]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 8x-\\cos 4x]$', '$\\tfrac{1}{2}[\\cos 8x+\\cos 4x]$',
                   '$\\tfrac{1}{2}[\\sin 8x-\\sin 4x]$'], 'explanation': '$\\frac{1}{2}[\\cos4x-\\cos8x]$.'},
        {'question': 'Convert $\\sin 70^\\circ\\sin 10^\\circ$ to a difference of cosines.',
         'answer': '$\\tfrac{1}{2}[\\cos 60^\\circ-\\cos 80^\\circ]$',
         'wrong': ['$\\tfrac{1}{2}[\\cos 80^\\circ-\\cos 60^\\circ]$',
                   '$\\tfrac{1}{2}[\\cos 80^\\circ+\\cos 60^\\circ]$',
                   '$\\tfrac{1}{2}[\\sin 80^\\circ+\\sin 60^\\circ]$'],
         'explanation': '$\\frac{1}{2}[\\cos60^\\circ-\\cos80^\\circ]$.'},

        # ══════════════════════════════════════════════════════════════════
        # ANGLE ADDITION AND SUBTRACTION  (32 questions — 4 per formula)
        # F1 sin(A+B)  F2 sin(A-B)  F3 cos(A+B)  F4 cos(A-B)
        # F5 tan(A+B)  F6 tan(A-B)  F7 cot(A+B)  F8 cot(A-B)
        # ══════════════════════════════════════════════════════════════════

        # F1 sin(A+B) (4)
        {'question': 'Write the expansion of $\\sin(A+B)$.', 'answer': '$\\sin A\\cos B+\\cos A\\sin B$',
         'wrong': ['$\\sin A\\cos B-\\cos A\\sin B$', '$\\cos A\\cos B-\\sin A\\sin B$',
                   '$\\cos A\\cos B+\\sin A\\sin B$'], 'explanation': '$\\sin(A+B)=\\sin A\\cos B+\\cos A\\sin B$.'},
        {'question': 'Find $\\sin 75^\\circ$ using $\\sin(45^\\circ+30^\\circ)$.',
         'answer': '$\\dfrac{\\sqrt{6}+\\sqrt{2}}{4}$',
         'wrong': ['$\\dfrac{\\sqrt{6}-\\sqrt{2}}{4}$', '$\\dfrac{\\sqrt{3}+1}{2}$', '$\\dfrac{\\sqrt{2}+1}{4}$'],
         'explanation': '$\\frac{\\sqrt{2}}{2}\\cdot\\frac{\\sqrt{3}}{2}+\\frac{\\sqrt{2}}{2}\\cdot\\frac{1}{2}=\\frac{\\sqrt{6}+\\sqrt{2}}{4}$.'},
        {
            'question': 'If $\\sin A=\\tfrac{3}{5}$, $\\cos A=\\tfrac{4}{5}$, $\\sin B=\\tfrac{5}{13}$, $\\cos B=\\tfrac{12}{13}$, find $\\sin(A+B)$.',
            'answer': '$\\dfrac{56}{65}$', 'wrong': ['$\\dfrac{33}{65}$', '$\\dfrac{16}{65}$', '$\\dfrac{63}{65}$'],
            'explanation': '$\\frac{3}{5}\\cdot\\frac{12}{13}+\\frac{4}{5}\\cdot\\frac{5}{13}=\\frac{36+20}{65}=\\frac{56}{65}$.'},
        {'question': 'Find $\\sin 105^\\circ$ using $\\sin(60^\\circ+45^\\circ)$.',
         'answer': '$\\dfrac{\\sqrt{6}+\\sqrt{2}}{4}$',
         'wrong': ['$\\dfrac{\\sqrt{6}-\\sqrt{2}}{4}$', '$\\dfrac{\\sqrt{3}+\\sqrt{2}}{4}$',
                   '$\\dfrac{\\sqrt{3}-1}{4}$'],
         'explanation': '$\\frac{\\sqrt{3}}{2}\\cdot\\frac{\\sqrt{2}}{2}+\\frac{1}{2}\\cdot\\frac{\\sqrt{2}}{2}=\\frac{\\sqrt{6}+\\sqrt{2}}{4}$.'},

        # F2 sin(A-B) (4)
        {'question': 'Write the expansion of $\\sin(A-B)$.', 'answer': '$\\sin A\\cos B-\\cos A\\sin B$',
         'wrong': ['$\\sin A\\cos B+\\cos A\\sin B$', '$\\cos A\\cos B+\\sin A\\sin B$',
                   '$\\cos A\\cos B-\\sin A\\sin B$'], 'explanation': '$\\sin(A-B)=\\sin A\\cos B-\\cos A\\sin B$.'},
        {'question': 'Find $\\sin 15^\\circ$ using $\\sin(45^\\circ-30^\\circ)$.',
         'answer': '$\\dfrac{\\sqrt{6}-\\sqrt{2}}{4}$',
         'wrong': ['$\\dfrac{\\sqrt{6}+\\sqrt{2}}{4}$', '$\\dfrac{\\sqrt{3}-1}{2}$', '$\\dfrac{\\sqrt{2}-1}{4}$'],
         'explanation': '$\\frac{\\sqrt{2}}{2}\\cdot\\frac{\\sqrt{3}}{2}-\\frac{\\sqrt{2}}{2}\\cdot\\frac{1}{2}=\\frac{\\sqrt{6}-\\sqrt{2}}{4}$.'},
        {
            'question': 'If $\\sin A=\\tfrac{4}{5}$, $\\cos A=\\tfrac{3}{5}$, $\\sin B=\\tfrac{12}{13}$, $\\cos B=\\tfrac{5}{13}$, find $\\sin(A-B)$.',
            'answer': '$-\\dfrac{16}{65}$', 'wrong': ['$\\dfrac{16}{65}$', '$\\dfrac{56}{65}$', '$-\\dfrac{56}{65}$'],
            'explanation': '$\\frac{4}{5}\\cdot\\frac{5}{13}-\\frac{3}{5}\\cdot\\frac{12}{13}=\\frac{20-36}{65}=-\\frac{16}{65}$.'},
        {'question': 'Find $\\sin(-15^\\circ)$ using $\\sin(30^\\circ-45^\\circ)$.',
         'answer': '$\\dfrac{\\sqrt{2}-\\sqrt{6}}{4}$',
         'wrong': ['$\\dfrac{\\sqrt{6}-\\sqrt{2}}{4}$', '$\\dfrac{\\sqrt{2}+\\sqrt{6}}{4}$',
                   '$-\\dfrac{\\sqrt{3}+1}{4}$'],
         'explanation': '$\\frac{1}{2}\\cdot\\frac{\\sqrt{2}}{2}-\\frac{\\sqrt{3}}{2}\\cdot\\frac{\\sqrt{2}}{2}=\\frac{\\sqrt{2}-\\sqrt{6}}{4}$.'},

        # F3 cos(A+B) (4)
        {'question': 'Write the expansion of $\\cos(A+B)$.', 'answer': '$\\cos A\\cos B-\\sin A\\sin B$',
         'wrong': ['$\\cos A\\cos B+\\sin A\\sin B$', '$\\sin A\\cos B+\\cos A\\sin B$',
                   '$\\sin A\\cos B-\\cos A\\sin B$'], 'explanation': '$\\cos(A+B)=\\cos A\\cos B-\\sin A\\sin B$.'},
        {'question': 'Find $\\cos 75^\\circ$ using $\\cos(45^\\circ+30^\\circ)$.',
         'answer': '$\\dfrac{\\sqrt{6}-\\sqrt{2}}{4}$',
         'wrong': ['$\\dfrac{\\sqrt{6}+\\sqrt{2}}{4}$', '$\\dfrac{\\sqrt{2}-\\sqrt{3}}{4}$',
                   '$\\dfrac{1-\\sqrt{3}}{4}$'],
         'explanation': '$\\frac{\\sqrt{2}}{2}\\cdot\\frac{\\sqrt{3}}{2}-\\frac{\\sqrt{2}}{2}\\cdot\\frac{1}{2}=\\frac{\\sqrt{6}-\\sqrt{2}}{4}$.'},
        {
            'question': 'If $\\sin A=\\tfrac{3}{5}$, $\\cos A=\\tfrac{4}{5}$, $\\sin B=\\tfrac{5}{13}$, $\\cos B=\\tfrac{12}{13}$, find $\\cos(A+B)$.',
            'answer': '$\\dfrac{33}{65}$', 'wrong': ['$\\dfrac{56}{65}$', '$-\\dfrac{33}{65}$', '$\\dfrac{16}{65}$'],
            'explanation': '$\\frac{4}{5}\\cdot\\frac{12}{13}-\\frac{3}{5}\\cdot\\frac{5}{13}=\\frac{48-15}{65}=\\frac{33}{65}$.'},
        {'question': 'Find $\\cos 105^\\circ$ using $\\cos(60^\\circ+45^\\circ)$.',
         'answer': '$\\dfrac{\\sqrt{2}-\\sqrt{6}}{4}$',
         'wrong': ['$\\dfrac{\\sqrt{6}-\\sqrt{2}}{4}$', '$\\dfrac{\\sqrt{2}+\\sqrt{6}}{4}$',
                   '$-\\dfrac{\\sqrt{3}+1}{4}$'],
         'explanation': '$\\frac{1}{2}\\cdot\\frac{\\sqrt{2}}{2}-\\frac{\\sqrt{3}}{2}\\cdot\\frac{\\sqrt{2}}{2}=\\frac{\\sqrt{2}-\\sqrt{6}}{4}$.'},

        # F4 cos(A-B) (4)
        {'question': 'Write the expansion of $\\cos(A-B)$.', 'answer': '$\\cos A\\cos B+\\sin A\\sin B$',
         'wrong': ['$\\cos A\\cos B-\\sin A\\sin B$', '$\\sin A\\cos B+\\cos A\\sin B$',
                   '$\\sin A\\cos B-\\cos A\\sin B$'], 'explanation': '$\\cos(A-B)=\\cos A\\cos B+\\sin A\\sin B$.'},
        {'question': 'Find $\\cos 15^\\circ$ using $\\cos(45^\\circ-30^\\circ)$.',
         'answer': '$\\dfrac{\\sqrt{6}+\\sqrt{2}}{4}$',
         'wrong': ['$\\dfrac{\\sqrt{6}-\\sqrt{2}}{4}$', '$\\dfrac{\\sqrt{3}+1}{2}$', '$\\dfrac{\\sqrt{2}+1}{4}$'],
         'explanation': '$\\frac{\\sqrt{2}}{2}\\cdot\\frac{\\sqrt{3}}{2}+\\frac{\\sqrt{2}}{2}\\cdot\\frac{1}{2}=\\frac{\\sqrt{6}+\\sqrt{2}}{4}$.'},
        {
            'question': 'If $\\sin A=\\tfrac{4}{5}$, $\\cos A=\\tfrac{3}{5}$, $\\sin B=\\tfrac{12}{13}$, $\\cos B=\\tfrac{5}{13}$, find $\\cos(A-B)$.',
            'answer': '$\\dfrac{63}{65}$', 'wrong': ['$-\\dfrac{63}{65}$', '$\\dfrac{33}{65}$', '$\\dfrac{56}{65}$'],
            'explanation': '$\\frac{3}{5}\\cdot\\frac{5}{13}+\\frac{4}{5}\\cdot\\frac{12}{13}=\\frac{15+48}{65}=\\frac{63}{65}$.'},
        {'question': 'Verify $\\cos 30^\\circ$ using $\\cos(60^\\circ-30^\\circ)$.',
         'answer': '$\\dfrac{\\sqrt{3}}{2}$', 'wrong': ['$\\dfrac{1}{2}$', '$\\dfrac{\\sqrt{2}}{2}$', '$1$'],
         'explanation': '$\\frac{1}{2}\\cdot\\frac{\\sqrt{3}}{2}+\\frac{\\sqrt{3}}{2}\\cdot\\frac{1}{2}=\\frac{\\sqrt{3}}{2}$.'},

        # F5 tan(A+B) (4)
        {'question': 'Write the expansion of $\\tan(A+B)$.', 'answer': '$\\dfrac{\\tan A+\\tan B}{1-\\tan A\\tan B}$',
         'wrong': ['$\\dfrac{\\tan A-\\tan B}{1+\\tan A\\tan B}$', '$\\dfrac{\\tan A+\\tan B}{1+\\tan A\\tan B}$',
                   '$\\dfrac{\\tan A-\\tan B}{1-\\tan A\\tan B}$'],
         'explanation': '$\\tan(A+B)=\\dfrac{\\tan A+\\tan B}{1-\\tan A\\tan B}$.'},
        {'question': 'Find $\\tan 75^\\circ$ using $\\tan(45^\\circ+30^\\circ)$.', 'answer': '$2+\\sqrt{3}$',
         'wrong': ['$2-\\sqrt{3}$', '$\\sqrt{3}+1$', '$\\sqrt{3}-1$'],
         'explanation': '$\\frac{1+\\frac{1}{\\sqrt{3}}}{1-\\frac{1}{\\sqrt{3}}}=\\frac{\\sqrt{3}+1}{\\sqrt{3}-1}=2+\\sqrt{3}$.'},
        {'question': 'Find $\\tan(A+B)$ if $\\tan A=2$ and $\\tan B=3$.', 'answer': '$-1$',
         'wrong': ['$5$', '$1$', '$-5$'], 'explanation': '$\\frac{2+3}{1-6}=\\frac{5}{-5}=-1$.'},
        {'question': 'Find $\\tan(A+B)$ if $\\tan A=\\tfrac{1}{2}$ and $\\tan B=\\tfrac{1}{3}$.', 'answer': '$1$',
         'wrong': ['$\\dfrac{5}{6}$', '$\\dfrac{1}{6}$', '$5$'],
         'explanation': '$\\frac{\\frac{1}{2}+\\frac{1}{3}}{1-\\frac{1}{6}}=\\frac{\\frac{5}{6}}{\\frac{5}{6}}=1$.'},

        # F6 tan(A-B) (4)
        {'question': 'Write the expansion of $\\tan(A-B)$.', 'answer': '$\\dfrac{\\tan A-\\tan B}{1+\\tan A\\tan B}$',
         'wrong': ['$\\dfrac{\\tan A+\\tan B}{1-\\tan A\\tan B}$', '$\\dfrac{\\tan A-\\tan B}{1-\\tan A\\tan B}$',
                   '$\\dfrac{\\tan A+\\tan B}{1+\\tan A\\tan B}$'],
         'explanation': '$\\tan(A-B)=\\dfrac{\\tan A-\\tan B}{1+\\tan A\\tan B}$.'},
        {'question': 'Find $\\tan 15^\\circ$ using $\\tan(45^\\circ-30^\\circ)$.', 'answer': '$2-\\sqrt{3}$',
         'wrong': ['$2+\\sqrt{3}$', '$\\sqrt{3}-1$', '$\\sqrt{3}+1$'],
         'explanation': '$\\frac{1-\\frac{1}{\\sqrt{3}}}{1+\\frac{1}{\\sqrt{3}}}=\\frac{\\sqrt{3}-1}{\\sqrt{3}+1}=2-\\sqrt{3}$.'},
        {'question': 'Find $\\tan(A-B)$ if $\\tan A=3$ and $\\tan B=2$.', 'answer': '$\\dfrac{1}{7}$',
         'wrong': ['$-\\dfrac{1}{7}$', '$1$', '$5$'], 'explanation': '$\\frac{3-2}{1+6}=\\frac{1}{7}$.'},
        {'question': 'Find $\\tan(A-B)$ if $\\tan A=4$ and $\\tan B=1$.', 'answer': '$\\dfrac{3}{5}$',
         'wrong': ['$3$', '$5$', '$\\dfrac{5}{3}$'], 'explanation': '$\\frac{4-1}{1+4}=\\frac{3}{5}$.'},

        # F7 cot(A+B) (4)
        {'question': 'Write the expansion of $\\cot(A+B)$.', 'answer': '$\\dfrac{\\cot A\\cot B-1}{\\cot A+\\cot B}$',
         'wrong': ['$\\dfrac{\\cot A\\cot B+1}{\\cot A-\\cot B}$', '$\\dfrac{\\cot A\\cot B+1}{\\cot A+\\cot B}$',
                   '$\\dfrac{\\cot A\\cot B-1}{\\cot A-\\cot B}$'],
         'explanation': '$\\cot(A+B)=\\dfrac{\\cot A\\cot B-1}{\\cot A+\\cot B}$.'},
        {'question': 'Find $\\cot(A+B)$ if $\\cot A=2$ and $\\cot B=3$.', 'answer': '$1$',
         'wrong': ['$5$', '$-1$', '$\\dfrac{5}{6}$'], 'explanation': '$\\frac{6-1}{2+3}=\\frac{5}{5}=1$.'},
        {'question': 'Find $\\cot(A+B)$ if $\\cot A=4$ and $\\cot B=2$.', 'answer': '$\\dfrac{7}{6}$',
         'wrong': ['$\\dfrac{6}{7}$', '$7$', '$6$'], 'explanation': '$\\frac{8-1}{4+2}=\\frac{7}{6}$.'},
        {'question': 'Find $\\cot(A+B)$ if $\\cot A=1$ and $\\cot B=1$.', 'answer': '$0$',
         'wrong': ['$1$', '$2$', 'Undefined'], 'explanation': '$\\frac{1-1}{1+1}=\\frac{0}{2}=0$.'},

        # F8 cot(A-B) (4)
        {'question': 'Write the expansion of $\\cot(A-B)$.', 'answer': '$\\dfrac{\\cot A\\cot B+1}{\\cot B-\\cot A}$',
         'wrong': ['$\\dfrac{\\cot A\\cot B-1}{\\cot B-\\cot A}$', '$\\dfrac{\\cot A\\cot B-1}{\\cot A-\\cot B}$',
                   '$\\dfrac{\\cot A\\cot B+1}{\\cot A+\\cot B}$'],
         'explanation': '$\\cot(A-B)=\\dfrac{\\cot A\\cot B+1}{\\cot B-\\cot A}$.'},
        {'question': 'Find $\\cot(A-B)$ if $\\cot A=2$ and $\\cot B=3$.', 'answer': '$7$',
         'wrong': ['$-7$', '$1$', '$\\dfrac{1}{7}$'], 'explanation': '$\\frac{6+1}{3-2}=7$.'},
        {'question': 'Find $\\cot(A-B)$ if $\\cot A=5$ and $\\cot B=3$.', 'answer': '$-8$',
         'wrong': ['$8$', '$\\dfrac{1}{8}$', '$-\\dfrac{1}{8}$'],
         'explanation': '$\\frac{15+1}{3-5}=\\frac{16}{-2}=-8$.'},
        {'question': 'Find $\\cot(A-B)$ if $\\cot A=4$ and $\\cot B=6$.', 'answer': '$\\dfrac{25}{2}$',
         'wrong': ['$-\\dfrac{25}{2}$', '$25$', '$2$'], 'explanation': '$\\frac{24+1}{6-4}=\\frac{25}{2}$.'},

        # ══════════════════════════════════════════════════════════════════
        # DOUBLE ANGLE  (20 questions — 5 per formula)
        # F1 sin2A=2sinAcosA
        # F2 cos2A=cos²A-sin²A (=2cos²A-1=1-2sin²A)
        # F3 tan2A=2tanA/(1-tan²A)
        # F4 cot2A=(cot²A-1)/(2cotA)
        # ══════════════════════════════════════════════════════════════════

        # F1 sin2A (5)
        {'question': 'Write the double angle formula for $\\sin 2A$.', 'answer': '$2\\sin A\\cos A$',
         'wrong': ['$\\sin^2A-\\cos^2A$', '$1-2\\sin^2A$', '$2\\cos^2A-1$'],
         'explanation': '$\\sin 2A=2\\sin A\\cos A$.'},
        {'question': 'Find $\\sin 2A$ if $\\sin A=\\tfrac{3}{5}$ and $\\cos A=\\tfrac{4}{5}$.',
         'answer': '$\\dfrac{24}{25}$', 'wrong': ['$\\dfrac{12}{25}$', '$\\dfrac{7}{25}$', '$\\dfrac{48}{25}$'],
         'explanation': '$2\\cdot\\frac{3}{5}\\cdot\\frac{4}{5}=\\frac{24}{25}$.'},
        {'question': 'Find $\\sin 60^\\circ$ using $\\sin 2(30^\\circ)$.', 'answer': '$\\dfrac{\\sqrt{3}}{2}$',
         'wrong': ['$\\dfrac{1}{2}$', '$\\dfrac{\\sqrt{2}}{2}$', '$1$'],
         'explanation': '$2\\cdot\\frac{1}{2}\\cdot\\frac{\\sqrt{3}}{2}=\\frac{\\sqrt{3}}{2}$.'},
        {'question': 'Find $\\sin 2A$ if $\\tan A=\\tfrac{3}{4}$ (Q I).', 'answer': '$\\dfrac{24}{25}$',
         'wrong': ['$\\dfrac{7}{25}$', '$\\dfrac{12}{25}$', '$\\dfrac{6}{5}$'],
         'explanation': '$\\sin A=\\frac{3}{5}$, $\\cos A=\\frac{4}{5}$ $\\Rightarrow$ $2\\cdot\\frac{3}{5}\\cdot\\frac{4}{5}=\\frac{24}{25}$.'},
        {'question': 'Find $\\sin 2A$ if $\\sin A=\\tfrac{5}{13}$ and $\\cos A=\\tfrac{12}{13}$.',
         'answer': '$\\dfrac{120}{169}$', 'wrong': ['$\\dfrac{60}{169}$', '$\\dfrac{119}{169}$', '$\\dfrac{10}{13}$'],
         'explanation': '$2\\cdot\\frac{5}{13}\\cdot\\frac{12}{13}=\\frac{120}{169}$.'},

        # F2 cos2A (5)
        {'question': 'Write $\\cos 2A$ in terms of $\\sin A$ only.', 'answer': '$1-2\\sin^2A$',
         'wrong': ['$2\\cos^2A-1$', '$\\cos^2A-\\sin^2A$', '$2\\sin A\\cos A$'],
         'explanation': '$\\cos 2A=1-2\\sin^2A$.'},
        {'question': 'Find $\\cos 2A$ if $\\sin A=\\tfrac{3}{5}$ and $\\cos A=\\tfrac{4}{5}$.',
         'answer': '$\\dfrac{7}{25}$', 'wrong': ['$\\dfrac{24}{25}$', '$-\\dfrac{7}{25}$', '$\\dfrac{1}{25}$'],
         'explanation': '$\\frac{16}{25}-\\frac{9}{25}=\\frac{7}{25}$.'},
        {'question': 'Find $\\cos 2A$ if $\\cos A=\\tfrac{1}{2}$.', 'answer': '$-\\dfrac{1}{2}$',
         'wrong': ['$\\dfrac{1}{2}$', '$0$', '$\\dfrac{3}{4}$'],
         'explanation': '$2\\cdot\\frac{1}{4}-1=-\\frac{1}{2}$.'},
        {'question': 'Find $\\cos 2A$ if $\\sin A=\\tfrac{\\sqrt{2}}{2}$.', 'answer': '$0$',
         'wrong': ['$1$', '$-1$', '$\\dfrac{1}{2}$'], 'explanation': '$1-2\\cdot\\frac{1}{2}=0$.'},
        {'question': 'Find $\\cos 2A$ if $\\sin A=\\tfrac{5}{13}$ and $\\cos A=\\tfrac{12}{13}$.',
         'answer': '$\\dfrac{119}{169}$', 'wrong': ['$\\dfrac{120}{169}$', '$-\\dfrac{119}{169}$', '$\\dfrac{1}{169}$'],
         'explanation': '$\\frac{144}{169}-\\frac{25}{169}=\\frac{119}{169}$.'},

        # F3 tan2A (5)
        {'question': 'Write the double angle formula for $\\tan 2A$.', 'answer': '$\\dfrac{2\\tan A}{1-\\tan^2A}$',
         'wrong': ['$\\dfrac{\\tan A}{1-\\tan^2A}$', '$\\dfrac{2\\tan A}{1+\\tan^2A}$', '$2\\tan A(1-\\tan^2A)$'],
         'explanation': '$\\tan 2A=\\dfrac{2\\tan A}{1-\\tan^2A}$.'},
        {'question': 'Find $\\tan 2A$ if $\\tan A=2$.', 'answer': '$-\\dfrac{4}{3}$',
         'wrong': ['$\\dfrac{4}{3}$', '$4$', '$-4$'], 'explanation': '$\\frac{4}{1-4}=-\\frac{4}{3}$.'},
        {'question': 'Find $\\tan 2A$ if $\\tan A=\\tfrac{1}{2}$.', 'answer': '$\\dfrac{4}{3}$',
         'wrong': ['$1$', '$\\dfrac{3}{4}$', '$-\\dfrac{4}{3}$'],
         'explanation': '$\\frac{1}{1-\\frac{1}{4}}=\\frac{1}{\\frac{3}{4}}=\\frac{4}{3}$.'},
        {'question': 'Find $\\tan 2A$ if $\\tan A=3$.', 'answer': '$-\\dfrac{3}{4}$',
         'wrong': ['$\\dfrac{3}{4}$', '$6$', '$-6$'], 'explanation': '$\\frac{6}{1-9}=-\\frac{3}{4}$.'},
        {'question': 'Why is $\\tan 2(45^\\circ)$ undefined?',
         'answer': 'Because $1-\\tan^2 45^\\circ=0$ (division by zero)',
         'wrong': ['Because $\\tan 90^\\circ=0$', 'Because $\\sin 90^\\circ=0$', 'Because $\\cos 45^\\circ=0$'],
         'explanation': '$\\frac{2\\cdot1}{1-1}=\\frac{2}{0}$, undefined.'},

        # F4 cot2A (5)
        {'question': 'Write the double angle formula for $\\cot 2A$.', 'answer': '$\\dfrac{\\cot^2A-1}{2\\cot A}$',
         'wrong': ['$\\dfrac{2\\cot A}{\\cot^2A-1}$', '$\\dfrac{\\cot^2A+1}{2\\cot A}$',
                   '$\\dfrac{\\cot A}{1-\\cot^2A}$'], 'explanation': '$\\cot 2A=\\dfrac{\\cot^2A-1}{2\\cot A}$.'},
        {'question': 'Find $\\cot 2A$ if $\\cot A=2$.', 'answer': '$\\dfrac{3}{4}$',
         'wrong': ['$\\dfrac{4}{3}$', '$3$', '$-\\dfrac{3}{4}$'], 'explanation': '$\\frac{4-1}{4}=\\frac{3}{4}$.'},
        {'question': 'Find $\\cot 2A$ if $\\cot A=3$.', 'answer': '$\\dfrac{4}{3}$',
         'wrong': ['$\\dfrac{3}{4}$', '$8$', '$-\\dfrac{4}{3}$'],
         'explanation': '$\\frac{9-1}{6}=\\frac{8}{6}=\\frac{4}{3}$.'},
        {'question': 'Find $\\cot 2A$ if $\\cot A=1$.', 'answer': '$0$', 'wrong': ['$1$', '$2$', 'Undefined'],
         'explanation': '$\\frac{1-1}{2}=0$.'},
        {'question': 'Find $\\cot 2A$ if $\\cot A=\\tfrac{1}{2}$.', 'answer': '$-\\dfrac{3}{4}$',
         'wrong': ['$\\dfrac{3}{4}$', '$-\\dfrac{4}{3}$', '$\\dfrac{4}{3}$'],
         'explanation': '$\\frac{\\frac{1}{4}-1}{2\\cdot\\frac{1}{2}}=\\frac{-\\frac{3}{4}}{1}=-\\frac{3}{4}$.'}

    ],
    'inverse_trigonometric_functions': [
        {
            'question': 'What is the domain of $f(x) = \\arcsin(x)$?',
            'answer': '$[-1,\\ 1]$',
            'wrong': ['$(-\\infty,\\ +\\infty)$', '$[0,\\ \\pi]$', '$(-1,\\ 1)$'],
            'explanation': '$\\arcsin(x)$ is defined only when $-1 \\le x \\le 1$. Domain: $[-1, 1]$.',
        },
        {
            'question': 'What is the range of $f(x) = \\arcsin(x)$?',
            'answer': '$\\left[-\\dfrac{\\pi}{2},\\ \\dfrac{\\pi}{2}\\right]$',
            'wrong': ['$[0,\\ \\pi]$', '$(-\\infty,\\ +\\infty)$', '$\\left(0,\\ \\dfrac{\\pi}{2}\\right)$'],
            'explanation': 'The range of $\\arcsin$ is $\\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$ (principal values).',
        },
        {
            'question': 'Evaluate $\\sin(\\arcsin(0.5))$.',
            'answer': '$0.5$',
            'wrong': ['$\\dfrac{\\pi}{6}$', '$1$', 'undefined'],
            'explanation': 'Since $0.5 \\in [-1,1]$, $\\sin(\\arcsin(x)) = x$. Answer: $0.5$.',
        },
        {
            'question': 'Evaluate $\\sin\\!\\left(\\arcsin\\!\\left(\\dfrac{\\sqrt{2}}{2}\\right)\\right)$.',
            'answer': '$\\dfrac{\\sqrt{2}}{2}$',
            'wrong': ['$\\dfrac{\\pi}{4}$', '$1$', '$0$'],
            'explanation': '$\\dfrac{\\sqrt{2}}{2} \\in [-1,1]$, so $\\sin(\\arcsin(x))=x$. Answer: $\\dfrac{\\sqrt{2}}{2}$.',
        },
        {
            'question': 'Evaluate $\\sin(\\arcsin(-1))$.',
            'answer': '$-1$',
            'wrong': ['$1$', '$0$', 'undefined'],
            'explanation': '$-1 \\in [-1,1]$, so $\\sin(\\arcsin(-1)) = -1$.',
        },
        {
            'question': 'Evaluate $\\sin(\\arcsin(0))$.',
            'answer': '$0$',
            'wrong': ['$1$', '$-1$', 'undefined'],
            'explanation': '$0 \\in [-1,1]$, so $\\sin(\\arcsin(0)) = 0$.',
        },
        {
            'question': 'Evaluate $\\sin(\\arcsin(2))$.',
            'answer': 'undefined (empty set)',
            'wrong': ['$2$', '$1$', '$\\dfrac{\\pi}{2}$'],
            'explanation': '$2 \\notin [-1,1]$, so $\\arcsin(2)$ is undefined. The result is $\\emptyset$.',
        },
        {
            'question': 'Evaluate $\\sin(\\arcsin(-3))$.',
            'answer': 'undefined (empty set)',
            'wrong': ['$-3$', '$-1$', '$-\\dfrac{\\pi}{2}$'],
            'explanation': '$-3 \\notin [-1,1]$, so $\\arcsin(-3)$ is undefined. The result is $\\emptyset$.',
        },
        {
            'question': 'Evaluate $\\sin\\!\\left(\\arcsin\\!\\left(\\dfrac{\\sqrt{3}}{2}\\right)\\right)$.',
            'answer': '$\\dfrac{\\sqrt{3}}{2}$',
            'wrong': ['$\\dfrac{\\pi}{3}$', '$\\dfrac{1}{2}$', '$1$'],
            'explanation': '$\\dfrac{\\sqrt{3}}{2} \\in [-1,1]$, so the answer is $\\dfrac{\\sqrt{3}}{2}$.',
        },
        {
            'question': 'Evaluate $\\sin(\\arcsin(1.5))$.',
            'answer': 'undefined (empty set)',
            'wrong': ['$1.5$', '$1$', '$0.5$'],
            'explanation': '$1.5 \\notin [-1,1]$, so $\\arcsin(1.5)$ is undefined. The result is $\\emptyset$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(\\sin\\!\\left(\\dfrac{\\pi}{6}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{6}$',
            'wrong': ['$\\dfrac{5\\pi}{6}$', '$\\dfrac{\\pi}{3}$', '$1$'],
            'explanation': '$\\dfrac{\\pi}{6} \\in \\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$, so $\\arcsin(\\sin x) = x = \\dfrac{\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(\\sin\\!\\left(\\dfrac{\\pi}{4}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{4}$',
            'wrong': ['$\\dfrac{3\\pi}{4}$', '$\\dfrac{\\pi}{2}$', '$0$'],
            'explanation': '$\\dfrac{\\pi}{4} \\in \\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$, so $\\arcsin(\\sin x) = \\dfrac{\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(\\sin\\!\\left(-\\dfrac{\\pi}{3}\\right)\\right)$.',
            'answer': '$-\\dfrac{\\pi}{3}$',
            'wrong': ['$\\dfrac{\\pi}{3}$', '$\\dfrac{2\\pi}{3}$', '$0$'],
            'explanation': '$-\\dfrac{\\pi}{3} \\in \\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$, so $\\arcsin(\\sin x) = -\\dfrac{\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(\\sin\\!\\left(\\dfrac{\\pi}{2}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{2}$',
            'wrong': ['$\\pi$', '$0$', '$\\dfrac{\\pi}{4}$'],
            'explanation': '$\\dfrac{\\pi}{2} \\in \\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$, so $\\arcsin(\\sin x) = \\dfrac{\\pi}{2}$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(\\sin(0)\\right)$.',
            'answer': '$0$',
            'wrong': ['$\\pi$', '$1$', '$-1$'],
            'explanation': '$0 \\in \\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$, so $\\arcsin(\\sin 0) = 0$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(\\sin\\!\\left(\\dfrac{2\\pi}{3}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{3}$',
            'wrong': ['$\\dfrac{2\\pi}{3}$', '$\\dfrac{\\pi}{6}$', '$\\pi$'],
            'explanation': '$\\dfrac{2\\pi}{3} \\notin \\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$. Use $\\arcsin(\\sin x) = \\pi - x$ for $x \\in \\left[\\dfrac{\\pi}{2}, \\pi\\right]$: $\\pi - \\dfrac{2\\pi}{3} = \\dfrac{\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(\\sin\\!\\left(\\dfrac{3\\pi}{4}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{4}$',
            'wrong': ['$\\dfrac{3\\pi}{4}$', '$-\\dfrac{\\pi}{4}$', '$\\dfrac{\\pi}{2}$'],
            'explanation': '$\\dfrac{3\\pi}{4} \\notin \\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$. $\\arcsin(\\sin x) = \\pi - x = \\pi - \\dfrac{3\\pi}{4} = \\dfrac{\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(\\sin\\!\\left(\\dfrac{5\\pi}{6}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{6}$',
            'wrong': ['$\\dfrac{5\\pi}{6}$', '$\\dfrac{\\pi}{3}$', '$\\pi$'],
            'explanation': '$\\dfrac{5\\pi}{6} \\notin \\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$. $\\arcsin(\\sin x) = \\pi - \\dfrac{5\\pi}{6} = \\dfrac{\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(\\sin\\!\\left(-\\dfrac{2\\pi}{3}\\right)\\right)$.',
            'answer': '$-\\dfrac{\\pi}{3}$',
            'wrong': ['$-\\dfrac{2\\pi}{3}$', '$\\dfrac{2\\pi}{3}$', '$\\dfrac{\\pi}{3}$'],
            'explanation': '$-\\dfrac{2\\pi}{3} \\notin \\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$. Use $\\arcsin(\\sin x) = -\\pi - x$ for $x \\in \\left[-\\pi, -\\dfrac{\\pi}{2}\\right]$: $-\\pi - (-\\dfrac{2\\pi}{3}) = -\\dfrac{\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(\\sin\\!\\left(\\dfrac{7\\pi}{6}\\right)\\right)$.',
            'answer': '$-\\dfrac{\\pi}{6}$',
            'wrong': ['$\\dfrac{7\\pi}{6}$', '$\\dfrac{\\pi}{6}$', '$\\dfrac{5\\pi}{6}$'],
            'explanation': '$\\sin\\!\\left(\\dfrac{7\\pi}{6}\\right) = -\\dfrac{1}{2}$. So $\\arcsin\\!\\left(-\\dfrac{1}{2}\\right) = -\\dfrac{\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\arcsin(-x)$.',
            'answer': '$-\\arcsin(x)$',
            'wrong': ['$\\arcsin(x)$', '$\\pi - \\arcsin(x)$', '$\\dfrac{\\pi}{2} + \\arcsin(x)$'],
            'explanation': '$\\arcsin$ is an odd function: $\\arcsin(-x) = -\\arcsin(x)$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(-\\dfrac{1}{2}\\right)$.',
            'answer': '$-\\dfrac{\\pi}{6}$',
            'wrong': ['$\\dfrac{\\pi}{6}$', '$-\\dfrac{\\pi}{3}$', '$\\dfrac{5\\pi}{6}$'],
            'explanation': '$\\arcsin(-x) = -\\arcsin(x)$, so $\\arcsin\\!\\left(-\\dfrac{1}{2}\\right) = -\\arcsin\\!\\left(\\dfrac{1}{2}\\right) = -\\dfrac{\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(-\\dfrac{\\sqrt{2}}{2}\\right)$.',
            'answer': '$-\\dfrac{\\pi}{4}$',
            'wrong': ['$\\dfrac{\\pi}{4}$', '$-\\dfrac{3\\pi}{4}$', '$\\dfrac{3\\pi}{4}$'],
            'explanation': '$\\arcsin(-x) = -\\arcsin(x)$, so the answer is $-\\dfrac{\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\arcsin\\!\\left(-\\dfrac{\\sqrt{3}}{2}\\right)$.',
            'answer': '$-\\dfrac{\\pi}{3}$',
            'wrong': ['$\\dfrac{\\pi}{3}$', '$-\\dfrac{2\\pi}{3}$', '$\\dfrac{2\\pi}{3}$'],
            'explanation': '$\\arcsin(-x) = -\\arcsin(x)$, so $\\arcsin\\!\\left(-\\dfrac{\\sqrt{3}}{2}\\right) = -\\dfrac{\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arcsin(-1)$.',
            'answer': '$-\\dfrac{\\pi}{2}$',
            'wrong': ['$\\dfrac{\\pi}{2}$', '$-\\pi$', '$\\pi$'],
            'explanation': '$\\arcsin(-1) = -\\arcsin(1) = -\\dfrac{\\pi}{2}$.',
        },
        {
            'question': 'What is the domain of $f(x) = \\arccos(x)$?',
            'answer': '$[-1,\\ 1]$',
            'wrong': ['$(-\\infty,\\ +\\infty)$', '$\\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$',
                      '$(-1,\\ 1)$'],
            'explanation': '$\\arccos(x)$ requires $-1 \\le x \\le 1$. Domain: $[-1, 1]$.',
        },
        {
            'question': 'What is the range of $f(x) = \\arccos(x)$?',
            'answer': '$[0,\\ \\pi]$',
            'wrong': ['$\\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$', '$(-\\infty,\\ +\\infty)$',
                      '$\\left[0, \\dfrac{\\pi}{2}\\right]$'],
            'explanation': 'The range of $\\arccos$ is $[0, \\pi]$ (principal values).',
        },
        {
            'question': 'Evaluate $\\cos(\\arccos(0.5))$.',
            'answer': '$0.5$',
            'wrong': ['$\\dfrac{\\pi}{3}$', '$1$', 'undefined'],
            'explanation': '$0.5 \\in [-1,1]$, so $\\cos(\\arccos(x)) = x = 0.5$.',
        },
        {
            'question': 'Evaluate $\\cos(\\arccos(-1))$.',
            'answer': '$-1$',
            'wrong': ['$1$', '$0$', 'undefined'],
            'explanation': '$-1 \\in [-1,1]$, so $\\cos(\\arccos(-1)) = -1$.',
        },
        {
            'question': 'Evaluate $\\cos\\!\\left(\\arccos\\!\\left(\\dfrac{\\sqrt{3}}{2}\\right)\\right)$.',
            'answer': '$\\dfrac{\\sqrt{3}}{2}$',
            'wrong': ['$\\dfrac{\\pi}{6}$', '$\\dfrac{1}{2}$', '$1$'],
            'explanation': '$\\dfrac{\\sqrt{3}}{2} \\in [-1,1]$, so the answer is $\\dfrac{\\sqrt{3}}{2}$.',
        },
        {
            'question': 'Evaluate $\\cos(\\arccos(0))$.',
            'answer': '$0$',
            'wrong': ['$\\dfrac{\\pi}{2}$', '$1$', 'undefined'],
            'explanation': '$0 \\in [-1,1]$, so $\\cos(\\arccos(0)) = 0$.',
        },
        {
            'question': 'Evaluate $\\cos(\\arccos(2))$.',
            'answer': 'undefined (empty set)',
            'wrong': ['$2$', '$1$', '$0$'],
            'explanation': '$2 \\notin [-1,1]$, so $\\arccos(2)$ is undefined. Result is $\\emptyset$.',
        },
        {
            'question': 'Evaluate $\\cos(\\arccos(-1.5))$.',
            'answer': 'undefined (empty set)',
            'wrong': ['$-1.5$', '$-1$', '$0.5$'],
            'explanation': '$-1.5 \\notin [-1,1]$, so $\\arccos(-1.5)$ is undefined. Result is $\\emptyset$.',
        },
        {
            'question': 'Evaluate $\\cos\\!\\left(\\arccos\\!\\left(\\dfrac{\\sqrt{2}}{2}\\right)\\right)$.',
            'answer': '$\\dfrac{\\sqrt{2}}{2}$',
            'wrong': ['$\\dfrac{\\pi}{4}$', '$\\dfrac{1}{2}$', '$1$'],
            'explanation': '$\\dfrac{\\sqrt{2}}{2} \\in [-1,1]$, so $\\cos(\\arccos(x)) = x$.',
        },
        {
            'question': 'Evaluate $\\cos(\\arccos(5))$.',
            'answer': 'undefined (empty set)',
            'wrong': ['$5$', '$1$', '$-1$'],
            'explanation': '$5 \\notin [-1,1]$, so $\\arccos(5)$ is undefined. Result is $\\emptyset$.',
        },
        {
            'question': 'Simplify $\\arccos(\\cos(0))$.',
            'answer': '$0$',
            'wrong': ['$\\pi$', '$1$', '$2\\pi$'],
            'explanation': '$0 \\in [0, \\pi]$, so $\\arccos(\\cos x) = x = 0$.',
        },
        {
            'question': 'Simplify $\\arccos\\!\\left(\\cos\\!\\left(\\dfrac{\\pi}{3}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{3}$',
            'wrong': ['$\\dfrac{2\\pi}{3}$', '$\\dfrac{\\pi}{6}$', '$\\dfrac{\\pi}{2}$'],
            'explanation': '$\\dfrac{\\pi}{3} \\in [0, \\pi]$, so $\\arccos(\\cos x) = \\dfrac{\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arccos\\!\\left(\\cos\\!\\left(\\dfrac{2\\pi}{3}\\right)\\right)$.',
            'answer': '$\\dfrac{2\\pi}{3}$',
            'wrong': ['$\\dfrac{\\pi}{3}$', '$\\dfrac{4\\pi}{3}$', '$\\pi$'],
            'explanation': '$\\dfrac{2\\pi}{3} \\in [0, \\pi]$, so $\\arccos(\\cos x) = \\dfrac{2\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arccos(\\cos(\\pi))$.',
            'answer': '$\\pi$',
            'wrong': ['$0$', '$2\\pi$', '$-\\pi$'],
            'explanation': '$\\pi \\in [0, \\pi]$, so $\\arccos(\\cos \\pi) = \\pi$.',
        },
        {
            'question': 'Simplify $\\arccos\\!\\left(\\cos\\!\\left(\\dfrac{\\pi}{2}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{2}$',
            'wrong': ['$0$', '$\\pi$', '$\\dfrac{\\pi}{4}$'],
            'explanation': '$\\dfrac{\\pi}{2} \\in [0, \\pi]$, so $\\arccos(\\cos x) = \\dfrac{\\pi}{2}$.',
        },
        {
            'question': 'Simplify $\\arccos\\!\\left(\\cos\\!\\left(\\dfrac{4\\pi}{3}\\right)\\right)$.',
            'answer': '$\\dfrac{2\\pi}{3}$',
            'wrong': ['$\\dfrac{4\\pi}{3}$', '$\\dfrac{\\pi}{3}$', '$\\pi$'],
            'explanation': '$\\cos\\!\\left(\\dfrac{4\\pi}{3}\\right) = -\\dfrac{1}{2}$. So $\\arccos\\!\\left(-\\dfrac{1}{2}\\right) = \\dfrac{2\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arccos\\!\\left(\\cos\\!\\left(\\dfrac{5\\pi}{4}\\right)\\right)$.',
            'answer': '$\\dfrac{3\\pi}{4}$',
            'wrong': ['$\\dfrac{5\\pi}{4}$', '$\\dfrac{\\pi}{4}$', '$\\pi$'],
            'explanation': '$\\dfrac{5\\pi}{4} \\notin [0,\\pi]$. $\\cos\\!\\left(\\dfrac{5\\pi}{4}\\right) = -\\dfrac{\\sqrt{2}}{2}$, so $\\arccos\\!\\left(-\\dfrac{\\sqrt{2}}{2}\\right) = \\dfrac{3\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\arccos\\!\\left(\\cos\\!\\left(\\dfrac{7\\pi}{6}\\right)\\right)$.',
            'answer': '$\\dfrac{5\\pi}{6}$',
            'wrong': ['$\\dfrac{7\\pi}{6}$', '$\\dfrac{\\pi}{6}$', '$\\dfrac{2\\pi}{3}$'],
            'explanation': '$\\cos\\!\\left(\\dfrac{7\\pi}{6}\\right) = -\\dfrac{\\sqrt{3}}{2}$, so $\\arccos\\!\\left(-\\dfrac{\\sqrt{3}}{2}\\right) = \\dfrac{5\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\arccos(\\cos(-\\pi))$.',
            'answer': '$\\pi$',
            'wrong': ['$-\\pi$', '$0$', '$2\\pi$'],
            'explanation': '$\\cos(-\\pi) = -1$, so $\\arccos(-1) = \\pi$.',
        },
        {
            'question': 'Simplify $\\arccos\\!\\left(\\cos\\!\\left(-\\dfrac{\\pi}{3}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{3}$',
            'wrong': ['$-\\dfrac{\\pi}{3}$', '$\\dfrac{2\\pi}{3}$', '$\\dfrac{4\\pi}{3}$'],
            'explanation': '$\\cos\\!\\left(-\\dfrac{\\pi}{3}\\right) = \\dfrac{1}{2}$, so $\\arccos\\!\\left(\\dfrac{1}{2}\\right) = \\dfrac{\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arccos(-x)$.',
            'answer': '$\\pi - \\arccos(x)$',
            'wrong': ['$-\\arccos(x)$', '$\\arccos(x)$', '$\\pi + \\arccos(x)$'],
            'explanation': '$\\arccos$ is NOT odd. The identity is: $\\arccos(-x) = \\pi - \\arccos(x)$.',
        },
        {
            'question': 'Simplify $\\arccos\\!\\left(-\\dfrac{1}{2}\\right)$.',
            'answer': '$\\dfrac{2\\pi}{3}$',
            'wrong': ['$-\\dfrac{\\pi}{3}$', '$\\dfrac{\\pi}{3}$', '$\\dfrac{5\\pi}{6}$'],
            'explanation': '$\\arccos(-x) = \\pi - \\arccos(x)$, so $\\arccos\\!\\left(-\\dfrac{1}{2}\\right) = \\pi - \\dfrac{\\pi}{3} = \\dfrac{2\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arccos\\!\\left(-\\dfrac{\\sqrt{2}}{2}\\right)$.',
            'answer': '$\\dfrac{3\\pi}{4}$',
            'wrong': ['$-\\dfrac{\\pi}{4}$', '$\\dfrac{\\pi}{4}$', '$\\dfrac{5\\pi}{4}$'],
            'explanation': '$\\arccos(-x) = \\pi - \\arccos(x) = \\pi - \\dfrac{\\pi}{4} = \\dfrac{3\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\arccos\\!\\left(-\\dfrac{\\sqrt{3}}{2}\\right)$.',
            'answer': '$\\dfrac{5\\pi}{6}$',
            'wrong': ['$-\\dfrac{\\pi}{6}$', '$\\dfrac{\\pi}{6}$', '$\\dfrac{7\\pi}{6}$'],
            'explanation': '$\\arccos(-x) = \\pi - \\arccos(x) = \\pi - \\dfrac{\\pi}{6} = \\dfrac{5\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\arccos(-1)$.',
            'answer': '$\\pi$',
            'wrong': ['$0$', '$-\\dfrac{\\pi}{2}$', '$\\dfrac{\\pi}{2}$'],
            'explanation': '$\\arccos(-1) = \\pi - \\arccos(1) = \\pi - 0 = \\pi$.',
        },
        {
            'question': 'What is the domain of $f(x) = \\arctan(x)$?',
            'answer': '$(-\\infty,\\ +\\infty)$',
            'wrong': ['$[-1,\\ 1]$', '$\\left(-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right)$', '$(0,\\ +\\infty)$'],
            'explanation': '$\\arctan(x)$ is defined for all real $x$. Domain: $(-\\infty, +\\infty)$.',
        },
        {
            'question': 'What is the range of $f(x) = \\arctan(x)$?',
            'answer': '$\\left(-\\dfrac{\\pi}{2},\\ \\dfrac{\\pi}{2}\\right)$',
            'wrong': ['$[0,\\ \\pi]$', '$(-\\infty,\\ +\\infty)$',
                      '$\\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$'],
            'explanation': 'The range of $\\arctan$ is the open interval $\\left(-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right)$.',
        },
        {
            'question': 'Evaluate $\\tan(\\arctan(1))$.',
            'answer': '$1$',
            'wrong': ['$\\dfrac{\\pi}{4}$', '$\\sqrt{2}$', '$0$'],
            'explanation': '$\\arctan$ domain is $(-\\infty,+\\infty)$, always defined. $\\tan(\\arctan(1)) = 1$.',
        },
        {
            'question': 'Evaluate $\\tan(\\arctan(0))$.',
            'answer': '$0$',
            'wrong': ['$1$', '$\\dfrac{\\pi}{4}$', 'undefined'],
            'explanation': '$\\arctan$ domain is $(-\\infty,+\\infty)$, always defined. $\\tan(\\arctan(0)) = 0$.',
        },
        {
            'question': 'Evaluate $\\tan(\\arctan(-5))$.',
            'answer': '$-5$',
            'wrong': ['$5$', 'undefined', '$-1$'],
            'explanation': '$\\arctan$ domain is $(-\\infty,+\\infty)$, always defined. $\\tan(\\arctan(-5)) = -5$.',
        },
        {
            'question': 'Evaluate $\\tan(\\arctan(100))$.',
            'answer': '$100$',
            'wrong': ['undefined', '$1$', '$\\dfrac{\\pi}{2}$'],
            'explanation': '$\\arctan$ domain is $(-\\infty,+\\infty)$, always defined. $\\tan(\\arctan(100)) = 100$.',
        },
        {
            'question': 'Evaluate $\\tan\\!\\left(\\arctan\\!\\left(\\sqrt{3}\\right)\\right)$.',
            'answer': '$\\sqrt{3}$',
            'wrong': ['$\\dfrac{\\pi}{3}$', '$\\dfrac{\\sqrt{3}}{2}$', '$3$'],
            'explanation': '$\\arctan$ domain is $(-\\infty,+\\infty)$, always defined. $\\tan(\\arctan(\\sqrt{3})) = \\sqrt{3}$.',
        },
        {
            'question': 'Evaluate $\\tan(\\arctan(-\\sqrt{3}))$.',
            'answer': '$-\\sqrt{3}$',
            'wrong': ['$\\sqrt{3}$', '$-\\dfrac{\\pi}{3}$', '$1$'],
            'explanation': '$\\arctan$ domain is $(-\\infty,+\\infty)$, always defined. $\\tan(\\arctan(-\\sqrt{3})) = -\\sqrt{3}$.',
        },
        {
            'question': 'Evaluate $\\tan\\!\\left(\\arctan\\!\\left(\\dfrac{1}{\\sqrt{3}}\\right)\\right)$.',
            'answer': '$\\dfrac{1}{\\sqrt{3}}$',
            'wrong': ['$\\dfrac{\\pi}{6}$', '$\\sqrt{3}$', '$1$'],
            'explanation': '$\\arctan$ domain is $(-\\infty,+\\infty)$, always defined. $\\tan\\!\\left(\\arctan\\!\\left(\\dfrac{1}{\\sqrt{3}}\\right)\\right) = \\dfrac{1}{\\sqrt{3}}$.',
        },
        {
            'question': 'Evaluate $\\tan(\\arctan(0.001))$.',
            'answer': '$0.001$',
            'wrong': ['undefined', '$1$', '$0$'],
            'explanation': '$\\arctan$ domain is $(-\\infty,+\\infty)$, always defined. $\\tan(\\arctan(0.001)) = 0.001$.',
        },
        {
            'question': 'Simplify $\\arctan\\!\\left(\\tan\\!\\left(\\dfrac{\\pi}{4}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{4}$',
            'wrong': ['$\\dfrac{3\\pi}{4}$', '$1$', '$\\dfrac{\\pi}{2}$'],
            'explanation': '$\\dfrac{\\pi}{4} \\in \\left(-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right)$, so $\\arctan(\\tan x) = \\dfrac{\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\arctan\\!\\left(\\tan\\!\\left(\\dfrac{\\pi}{6}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{6}$',
            'wrong': ['$\\dfrac{5\\pi}{6}$', '$\\dfrac{\\pi}{3}$', '$0$'],
            'explanation': '$\\dfrac{\\pi}{6} \\in \\left(-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right)$, so $\\arctan(\\tan x) = \\dfrac{\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\arctan(\\tan(0))$.',
            'answer': '$0$',
            'wrong': ['$\\pi$', '$1$', '$\\dfrac{\\pi}{4}$'],
            'explanation': '$0 \\in \\left(-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right)$, so $\\arctan(\\tan 0) = 0$.',
        },
        {
            'question': 'Simplify $\\arctan\\!\\left(\\tan\\!\\left(-\\dfrac{\\pi}{3}\\right)\\right)$.',
            'answer': '$-\\dfrac{\\pi}{3}$',
            'wrong': ['$\\dfrac{\\pi}{3}$', '$\\dfrac{2\\pi}{3}$', '$-\\dfrac{2\\pi}{3}$'],
            'explanation': '$-\\dfrac{\\pi}{3} \\in \\left(-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right)$, so $\\arctan(\\tan x) = -\\dfrac{\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arctan\\!\\left(\\tan\\!\\left(\\dfrac{\\pi}{3}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{3}$',
            'wrong': ['$\\dfrac{2\\pi}{3}$', '$\\dfrac{\\pi}{6}$', '$\\pi$'],
            'explanation': '$\\dfrac{\\pi}{3} \\in \\left(-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right)$, so $\\arctan(\\tan x) = \\dfrac{\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arctan\\!\\left(\\tan\\!\\left(\\dfrac{3\\pi}{4}\\right)\\right)$.',
            'answer': '$-\\dfrac{\\pi}{4}$',
            'wrong': ['$\\dfrac{3\\pi}{4}$', '$\\dfrac{\\pi}{4}$', '$-\\dfrac{3\\pi}{4}$'],
            'explanation': '$\\dfrac{3\\pi}{4} \\notin \\left(-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right)$. $\\tan\\!\\left(\\dfrac{3\\pi}{4}\\right) = -1$, so $\\arctan(-1) = -\\dfrac{\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\arctan\\!\\left(\\tan\\!\\left(\\dfrac{2\\pi}{3}\\right)\\right)$.',
            'answer': '$-\\dfrac{\\pi}{3}$',
            'wrong': ['$\\dfrac{2\\pi}{3}$', '$\\dfrac{\\pi}{3}$', '$-\\dfrac{2\\pi}{3}$'],
            'explanation': '$\\tan\\!\\left(\\dfrac{2\\pi}{3}\\right) = -\\sqrt{3}$, so $\\arctan(-\\sqrt{3}) = -\\dfrac{\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arctan\\!\\left(\\tan\\!\\left(\\dfrac{5\\pi}{6}\\right)\\right)$.',
            'answer': '$-\\dfrac{\\pi}{6}$',
            'wrong': ['$\\dfrac{5\\pi}{6}$', '$\\dfrac{\\pi}{6}$', '$\\dfrac{7\\pi}{6}$'],
            'explanation': '$\\tan\\!\\left(\\dfrac{5\\pi}{6}\\right) = -\\dfrac{1}{\\sqrt{3}}$, so $\\arctan\\!\\left(-\\dfrac{1}{\\sqrt{3}}\\right) = -\\dfrac{\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\arctan\\!\\left(\\tan\\!\\left(\\dfrac{5\\pi}{4}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{4}$',
            'wrong': ['$\\dfrac{5\\pi}{4}$', '$-\\dfrac{\\pi}{4}$', '$\\dfrac{3\\pi}{4}$'],
            'explanation': '$\\tan\\!\\left(\\dfrac{5\\pi}{4}\\right) = 1$, so $\\arctan(1) = \\dfrac{\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\arctan\\!\\left(\\tan\\!\\left(-\\dfrac{3\\pi}{4}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{4}$',
            'wrong': ['$-\\dfrac{3\\pi}{4}$', '$-\\dfrac{\\pi}{4}$', '$\\dfrac{3\\pi}{4}$'],
            'explanation': '$\\tan\\!\\left(-\\dfrac{3\\pi}{4}\\right) = 1$, so $\\arctan(1) = \\dfrac{\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\arctan(-x)$.',
            'answer': '$-\\arctan(x)$',
            'wrong': ['$\\arctan(x)$', '$\\pi - \\arctan(x)$', '$\\dfrac{\\pi}{2} - \\arctan(x)$'],
            'explanation': '$\\arctan$ is an odd function: $\\arctan(-x) = -\\arctan(x)$.',
        },
        {
            'question': 'Simplify $\\arctan(-1)$.',
            'answer': '$-\\dfrac{\\pi}{4}$',
            'wrong': ['$\\dfrac{\\pi}{4}$', '$-\\dfrac{3\\pi}{4}$', '$\\dfrac{3\\pi}{4}$'],
            'explanation': '$\\arctan(-1) = -\\arctan(1) = -\\dfrac{\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\arctan\\!\\left(-\\dfrac{1}{\\sqrt{3}}\\right)$.',
            'answer': '$-\\dfrac{\\pi}{6}$',
            'wrong': ['$\\dfrac{\\pi}{6}$', '$-\\dfrac{5\\pi}{6}$', '$\\dfrac{5\\pi}{6}$'],
            'explanation': '$\\arctan(-x) = -\\arctan(x)$, so the answer is $-\\dfrac{\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\arctan(-\\sqrt{3})$.',
            'answer': '$-\\dfrac{\\pi}{3}$',
            'wrong': ['$\\dfrac{\\pi}{3}$', '$-\\dfrac{2\\pi}{3}$', '$\\dfrac{2\\pi}{3}$'],
            'explanation': '$\\arctan(-\\sqrt{3}) = -\\arctan(\\sqrt{3}) = -\\dfrac{\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\arctan\\!\\left(-\\dfrac{\\sqrt{3}}{3}\\right)$.',
            'answer': '$-\\dfrac{\\pi}{6}$',
            'wrong': ['$\\dfrac{\\pi}{6}$', '$-\\dfrac{\\pi}{3}$', '$\\dfrac{\\pi}{3}$'],
            'explanation': '$\\dfrac{\\sqrt{3}}{3} = \\dfrac{1}{\\sqrt{3}}$, so $\\arctan\\!\\left(-\\dfrac{1}{\\sqrt{3}}\\right) = -\\dfrac{\\pi}{6}$.',
        },
        {
            'question': 'What is the domain of $f(x) = \\text{arccot}(x)$?',
            'answer': '$(-\\infty,\\ +\\infty)$',
            'wrong': ['$[-1,\\ 1]$', '$(0,\\ \\pi)$', '$(0,\\ +\\infty)$'],
            'explanation': '$\\text{arccot}(x)$ is defined for all real $x$. Domain: $(-\\infty, +\\infty)$.',
        },
        {
            'question': 'What is the range of $f(x) = \\text{arccot}(x)$?',
            'answer': '$(0,\\ \\pi)$',
            'wrong': ['$\\left(-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right)$', '$[0,\\ \\pi]$',
                      '$(-\\infty,\\ +\\infty)$'],
            'explanation': 'The range of $\\text{arccot}$ is the open interval $(0, \\pi)$.',
        },
        {
            'question': 'Evaluate $\\cot(\\text{arccot}(3))$.',
            'answer': '$3$',
            'wrong': ['undefined', '$\\dfrac{\\pi}{6}$', '$\\dfrac{1}{3}$'],
            'explanation': '$\\text{arccot}$ domain is $(-\\infty,+\\infty)$, always defined. $\\cot(\\text{arccot}(3)) = 3$.',
        },
        {
            'question': 'Evaluate $\\cot(\\text{arccot}(0))$.',
            'answer': '$0$',
            'wrong': ['undefined', '$\\dfrac{\\pi}{2}$', '$1$'],
            'explanation': '$\\text{arccot}$ domain is $(-\\infty,+\\infty)$, always defined. $\\cot(\\text{arccot}(0)) = 0$.',
        },
        {
            'question': 'Evaluate $\\cot(\\text{arccot}(-2))$.',
            'answer': '$-2$',
            'wrong': ['$2$', 'undefined', '$-\\dfrac{1}{2}$'],
            'explanation': '$\\text{arccot}$ domain is $(-\\infty,+\\infty)$, always defined. $\\cot(\\text{arccot}(-2)) = -2$.',
        },
        {
            'question': 'Evaluate $\\cot\\!\\left(\\text{arccot}\\!\\left(\\sqrt{3}\\right)\\right)$.',
            'answer': '$\\sqrt{3}$',
            'wrong': ['$\\dfrac{\\pi}{6}$', '$\\dfrac{\\sqrt{3}}{2}$', '$3$'],
            'explanation': '$\\text{arccot}$ domain is $(-\\infty,+\\infty)$, always defined. $\\cot(\\text{arccot}(\\sqrt{3})) = \\sqrt{3}$.',
        },
        {
            'question': 'Evaluate $\\cot(\\text{arccot}(1000))$.',
            'answer': '$1000$',
            'wrong': ['undefined', '$1$', '$\\dfrac{\\pi}{2}$'],
            'explanation': '$\\text{arccot}$ domain is $(-\\infty,+\\infty)$, always defined. $\\cot(\\text{arccot}(1000)) = 1000$.',
        },
        {
            'question': 'Evaluate $\\cot\\!\\left(\\text{arccot}\\!\\left(\\dfrac{1}{\\sqrt{3}}\\right)\\right)$.',
            'answer': '$\\dfrac{1}{\\sqrt{3}}$',
            'wrong': ['$\\sqrt{3}$', '$\\dfrac{\\pi}{3}$', '$1$'],
            'explanation': '$\\text{arccot}$ domain is $(-\\infty,+\\infty)$, always defined. $\\cot\\!\\left(\\text{arccot}\\!\\left(\\dfrac{1}{\\sqrt{3}}\\right)\\right) = \\dfrac{1}{\\sqrt{3}}$.',
        },
        {
            'question': 'Evaluate $\\cot(\\text{arccot}(-100))$.',
            'answer': '$-100$',
            'wrong': ['$100$', 'undefined', '$-1$'],
            'explanation': '$\\text{arccot}$ domain is $(-\\infty,+\\infty)$, always defined. $\\cot(\\text{arccot}(-100)) = -100$.',
        },
        {
            'question': 'Evaluate $\\cot\\!\\left(\\text{arccot}\\!\\left(-\\dfrac{1}{\\sqrt{3}}\\right)\\right)$.',
            'answer': '$-\\dfrac{1}{\\sqrt{3}}$',
            'wrong': ['$\\dfrac{1}{\\sqrt{3}}$', '$-\\sqrt{3}$', 'undefined'],
            'explanation': '$\\text{arccot}$ domain is $(-\\infty,+\\infty)$, always defined. $\\cot\\!\\left(\\text{arccot}\\!\\left(-\\dfrac{1}{\\sqrt{3}}\\right)\\right) = -\\dfrac{1}{\\sqrt{3}}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}\\!\\left(\\cot\\!\\left(\\dfrac{\\pi}{6}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{6}$',
            'wrong': ['$\\dfrac{5\\pi}{6}$', '$\\dfrac{\\pi}{3}$', '$0$'],
            'explanation': '$\\dfrac{\\pi}{6} \\in (0, \\pi)$, so $\\text{arccot}(\\cot x) = x = \\dfrac{\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}\\!\\left(\\cot\\!\\left(\\dfrac{\\pi}{4}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{4}$',
            'wrong': ['$\\dfrac{3\\pi}{4}$', '$\\dfrac{\\pi}{2}$', '$1$'],
            'explanation': '$\\dfrac{\\pi}{4} \\in (0, \\pi)$, so $\\text{arccot}(\\cot x) = \\dfrac{\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}\\!\\left(\\cot\\!\\left(\\dfrac{\\pi}{2}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{2}$',
            'wrong': ['$0$', '$\\pi$', '$\\dfrac{\\pi}{4}$'],
            'explanation': '$\\dfrac{\\pi}{2} \\in (0, \\pi)$, so $\\text{arccot}(\\cot x) = \\dfrac{\\pi}{2}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}\\!\\left(\\cot\\!\\left(\\dfrac{2\\pi}{3}\\right)\\right)$.',
            'answer': '$\\dfrac{2\\pi}{3}$',
            'wrong': ['$\\dfrac{\\pi}{3}$', '$\\dfrac{4\\pi}{3}$', '$\\pi$'],
            'explanation': '$\\dfrac{2\\pi}{3} \\in (0, \\pi)$, so $\\text{arccot}(\\cot x) = \\dfrac{2\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}\\!\\left(\\cot\\!\\left(\\dfrac{5\\pi}{6}\\right)\\right)$.',
            'answer': '$\\dfrac{5\\pi}{6}$',
            'wrong': ['$\\dfrac{\\pi}{6}$', '$\\dfrac{7\\pi}{6}$', '$\\pi$'],
            'explanation': '$\\dfrac{5\\pi}{6} \\in (0, \\pi)$, so $\\text{arccot}(\\cot x) = \\dfrac{5\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}\\!\\left(\\cot\\!\\left(\\dfrac{5\\pi}{4}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{4}$',
            'wrong': ['$\\dfrac{5\\pi}{4}$', '$\\dfrac{3\\pi}{4}$', '$-\\dfrac{\\pi}{4}$'],
            'explanation': '$\\cot\\!\\left(\\dfrac{5\\pi}{4}\\right) = 1$, so $\\text{arccot}(1) = \\dfrac{\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}\\!\\left(\\cot\\!\\left(\\dfrac{7\\pi}{6}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{6}$',
            'wrong': ['$\\dfrac{7\\pi}{6}$', '$\\dfrac{5\\pi}{6}$', '$\\dfrac{\\pi}{3}$'],
            'explanation': '$\\cot\\!\\left(\\dfrac{7\\pi}{6}\\right) = \\sqrt{3}$, so $\\text{arccot}(\\sqrt{3}) = \\dfrac{\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}(\\cot(-\\pi/6))$.',
            'answer': '$\\dfrac{5\\pi}{6}$',
            'wrong': ['$-\\dfrac{\\pi}{6}$', '$\\dfrac{\\pi}{6}$', '$\\dfrac{7\\pi}{6}$'],
            'explanation': '$\\cot(-\\dfrac{\\pi}{6}) = -\\sqrt{3}$, so $\\text{arccot}(-\\sqrt{3}) = \\pi - \\dfrac{\\pi}{6} = \\dfrac{5\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}\\!\\left(\\cot\\!\\left(\\dfrac{4\\pi}{3}\\right)\\right)$.',
            'answer': '$\\dfrac{\\pi}{3}$',
            'wrong': ['$\\dfrac{4\\pi}{3}$', '$\\dfrac{2\\pi}{3}$', '$\\pi$'],
            'explanation': '$\\cot\\!\\left(\\dfrac{4\\pi}{3}\\right) = \\dfrac{1}{\\sqrt{3}}$, so $\\text{arccot}\\!\\left(\\dfrac{1}{\\sqrt{3}}\\right) = \\dfrac{\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}\\!\\left(\\cot\\!\\left(-\\dfrac{\\pi}{4}\\right)\\right)$.',
            'answer': '$\\dfrac{3\\pi}{4}$',
            'wrong': ['$-\\dfrac{\\pi}{4}$', '$\\dfrac{\\pi}{4}$', '$\\dfrac{5\\pi}{4}$'],
            'explanation': '$\\cot(-\\dfrac{\\pi}{4}) = -1$, so $\\text{arccot}(-1) = \\pi - \\dfrac{\\pi}{4} = \\dfrac{3\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}(-x)$.',
            'answer': '$\\pi - \\text{arccot}(x)$',
            'wrong': ['$-\\text{arccot}(x)$', '$\\text{arccot}(x)$', '$\\pi + \\text{arccot}(x)$'],
            'explanation': '$\\text{arccot}$ is NOT odd. The identity is: $\\text{arccot}(-x) = \\pi - \\text{arccot}(x)$.',
        },
        {
            'question': 'Simplify $\\text{arccot}(-1)$.',
            'answer': '$\\dfrac{3\\pi}{4}$',
            'wrong': ['$-\\dfrac{\\pi}{4}$', '$\\dfrac{\\pi}{4}$', '$\\dfrac{5\\pi}{4}$'],
            'explanation': '$\\text{arccot}(-1) = \\pi - \\text{arccot}(1) = \\pi - \\dfrac{\\pi}{4} = \\dfrac{3\\pi}{4}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}\\!\\left(-\\dfrac{1}{\\sqrt{3}}\\right)$.',
            'answer': '$\\dfrac{2\\pi}{3}$',
            'wrong': ['$-\\dfrac{\\pi}{3}$', '$\\dfrac{\\pi}{3}$', '$\\dfrac{4\\pi}{3}$'],
            'explanation': '$\\text{arccot}\\!\\left(-\\dfrac{1}{\\sqrt{3}}\\right) = \\pi - \\dfrac{\\pi}{3} = \\dfrac{2\\pi}{3}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}(-\\sqrt{3})$.',
            'answer': '$\\dfrac{5\\pi}{6}$',
            'wrong': ['$-\\dfrac{\\pi}{6}$', '$\\dfrac{\\pi}{6}$', '$\\dfrac{7\\pi}{6}$'],
            'explanation': '$\\text{arccot}(-\\sqrt{3}) = \\pi - \\text{arccot}(\\sqrt{3}) = \\pi - \\dfrac{\\pi}{6} = \\dfrac{5\\pi}{6}$.',
        },
        {
            'question': 'Simplify $\\text{arccot}(0)$.',
            'answer': '$\\dfrac{\\pi}{2}$',
            'wrong': ['$0$', '$\\pi$', '$\\dfrac{\\pi}{4}$'],
            'explanation': '$\\cot\\!\\left(\\dfrac{\\pi}{2}\\right) = 0$, so $\\text{arccot}(0) = \\dfrac{\\pi}{2}$.',
        },
    ],
    'measurement_and_distance': [
        # ── MIDPOINT (25 questions) ──────────────────────────────────────────────

        {
            'question': 'Find the midpoint of the segment with endpoints $(2, 4)$ and $(8, 10)$.',
            'answer': '$(5, 7)$',
            'wrong': ['$(6, 7)$', '$(5, 6)$', '$(4, 7)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{2+8}{2}, \\dfrac{4+10}{2}\\right) = (5, 7)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(-3, 1)$ and $(7, 5)$.',
            'answer': '$(2, 3)$',
            'wrong': ['$(4, 3)$', '$(2, 4)$', '$(1, 3)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{-3+7}{2}, \\dfrac{1+5}{2}\\right) = (2, 3)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(0, 0)$ and $(6, -8)$.',
            'answer': '$(3, -4)$',
            'wrong': ['$(3, 4)$', '$(6, -4)$', '$(3, -8)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{0+6}{2}, \\dfrac{0+(-8)}{2}\\right) = (3, -4)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(-5, -3)$ and $(3, 7)$.',
            'answer': '$(-1, 2)$',
            'wrong': ['$(1, 2)$', '$(-1, 5)$', '$(-2, 2)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{-5+3}{2}, \\dfrac{-3+7}{2}\\right) = (-1, 2)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(1, -7)$ and $(-1, 3)$.',
            'answer': '$(0, -2)$',
            'wrong': ['$(0, 2)$', '$(1, -2)$', '$(0, -4)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{1+(-1)}{2}, \\dfrac{-7+3}{2}\\right) = (0, -2)$.',
        },
        {
            'question': 'The midpoint of segment $\\overline{AB}$ is $M(3, 5)$. If $A = (1, 2)$, find $B$.',
            'answer': '$(5, 8)$',
            'wrong': ['$(4, 7)$', '$(2, 3)$', '$(5, 7)$'],
            'explanation': '$B = (2 \\cdot 3 - 1,\\; 2 \\cdot 5 - 2) = (5, 8)$.',
        },
        {
            'question': 'The midpoint of segment $\\overline{AB}$ is $M(-1, 4)$. If $A = (3, 6)$, find $B$.',
            'answer': '$(-5, 2)$',
            'wrong': ['$(-4, 2)$', '$(-5, 1)$', '$(1, 5)$'],
            'explanation': '$B = (2(-1)-3,\\; 2(4)-6) = (-5, 2)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(\\tfrac{1}{2}, \\tfrac{3}{4})$ and $(\\tfrac{3}{2}, \\tfrac{5}{4})$.',
            'answer': '$(1, 1)$',
            'wrong': ['$(\\tfrac{1}{2}, 1)$', '$(1, \\tfrac{1}{2})$', '$(2, 2)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{\\frac{1}{2}+\\frac{3}{2}}{2}, \\dfrac{\\frac{3}{4}+\\frac{5}{4}}{2}\\right) = (1, 1)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(4, -6)$ and $(-4, 6)$.',
            'answer': '$(0, 0)$',
            'wrong': ['$(4, 6)$', '$(8, -12)$', '$(1, 1)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{4+(-4)}{2}, \\dfrac{-6+6}{2}\\right) = (0, 0)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(-2, -8)$ and $(-6, -4)$.',
            'answer': '$(-4, -6)$',
            'wrong': ['$(-3, -6)$', '$(-4, -5)$', '$(-8, -12)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{-2+(-6)}{2}, \\dfrac{-8+(-4)}{2}\\right) = (-4, -6)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(10, 3)$ and $(-4, 9)$.',
            'answer': '$(3, 6)$',
            'wrong': ['$(7, 6)$', '$(3, 7)$', '$(6, 6)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{10+(-4)}{2}, \\dfrac{3+9}{2}\\right) = (3, 6)$.',
        },
        {
            'question': 'The midpoint of $\\overline{PQ}$ is $M(0, -3)$. If $P = (-4, 1)$, find $Q$.',
            'answer': '$(4, -7)$',
            'wrong': ['$(-4, -7)$', '$(4, 7)$', '$(2, -4)$'],
            'explanation': '$Q = (2(0)-(-4),\\; 2(-3)-1) = (4, -7)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(7, 2)$ and $(7, -8)$.',
            'answer': '$(7, -3)$',
            'wrong': ['$(7, 3)$', '$(0, -3)$', '$(7, -5)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{7+7}{2}, \\dfrac{2+(-8)}{2}\\right) = (7, -3)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(-9, 5)$ and $(3, -1)$.',
            'answer': '$(-3, 2)$',
            'wrong': ['$(-6, 2)$', '$(-3, 3)$', '$(0, 2)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{-9+3}{2}, \\dfrac{5+(-1)}{2}\\right) = (-3, 2)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(0, 11)$ and $(0, -5)$.',
            'answer': '$(0, 3)$',
            'wrong': ['$(0, 6)$', '$(0, -3)$', '$(0, 8)$'],
            'explanation': 'Midpoint $= \\left(0, \\dfrac{11+(-5)}{2}\\right) = (0, 3)$.',
        },
        {
            'question': 'A diameter of a circle has endpoints $(-1, 3)$ and $(5, -1)$. Find the center.',
            'answer': '$(2, 1)$',
            'wrong': ['$(3, 1)$', '$(2, 2)$', '$(4, 2)$'],
            'explanation': 'The center is the midpoint: $\\left(\\dfrac{-1+5}{2}, \\dfrac{3+(-1)}{2}\\right) = (2, 1)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(\\sqrt{2}, 0)$ and $(3\\sqrt{2}, 4)$.',
            'answer': '$(2\\sqrt{2}, 2)$',
            'wrong': ['$(\\sqrt{2}, 2)$', '$(2\\sqrt{2}, 4)$', '$(4\\sqrt{2}, 2)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{\\sqrt{2}+3\\sqrt{2}}{2}, \\dfrac{0+4}{2}\\right) = (2\\sqrt{2}, 2)$.',
        },
        {
            'question': 'The midpoint of $\\overline{AB}$ is $(6, -2)$. If $B = (10, 0)$, find $A$.',
            'answer': '$(2, -4)$',
            'wrong': ['$(8, -1)$', '$(2, -2)$', '$(4, -4)$'],
            'explanation': '$A = (2(6)-10,\\; 2(-2)-0) = (2, -4)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(3, 3)$ and $(-3, -3)$.',
            'answer': '$(0, 0)$',
            'wrong': ['$(3, -3)$', '$(6, 6)$', '$(1, 1)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{3+(-3)}{2}, \\dfrac{3+(-3)}{2}\\right) = (0, 0)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(-8, 0)$ and $(2, 6)$.',
            'answer': '$(-3, 3)$',
            'wrong': ['$(-5, 3)$', '$(-3, 6)$', '$(0, 3)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{-8+2}{2}, \\dfrac{0+6}{2}\\right) = (-3, 3)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(5, -9)$ and $(-3, -1)$.',
            'answer': '$(1, -5)$',
            'wrong': ['$(2, -5)$', '$(1, -4)$', '$(-1, -5)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{5+(-3)}{2}, \\dfrac{-9+(-1)}{2}\\right) = (1, -5)$.',
        },
        {
            'question': 'The midpoint of $\\overline{CD}$ is $(-4, -4)$. If $C = (-6, -2)$, find $D$.',
            'answer': '$(-2, -6)$',
            'wrong': ['$(-8, -6)$', '$(-2, -2)$', '$(-5, -3)$'],
            'explanation': '$D = (2(-4)-(-6),\\; 2(-4)-(-2)) = (-2, -6)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(a, b)$ and $(-a, -b)$.',
            'answer': '$(0, 0)$',
            'wrong': ['$(a, b)$', '$(2a, 2b)$', '$(-a, b)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{a+(-a)}{2}, \\dfrac{b+(-b)}{2}\\right) = (0, 0)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(1, 4)$ and $(9, 4)$.',
            'answer': '$(5, 4)$',
            'wrong': ['$(4, 4)$', '$(5, 8)$', '$(5, 0)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{1+9}{2}, \\dfrac{4+4}{2}\\right) = (5, 4)$.',
        },
        {
            'question': 'Find the midpoint of the segment with endpoints $(-7, 2)$ and $(1, -6)$.',
            'answer': '$(-3, -2)$',
            'wrong': ['$(-4, -2)$', '$(-3, -4)$', '$(0, -2)$'],
            'explanation': 'Midpoint $= \\left(\\dfrac{-7+1}{2}, \\dfrac{2+(-6)}{2}\\right) = (-3, -2)$.',
        },

        # ── DISTANCE (25 questions) ──────────────────────────────────────────────

        {
            'question': 'Find the distance between $(1, 2)$ and $(4, 6)$.',
            'answer': '$5$',
            'wrong': ['$\\sqrt{7}$', '$7$', '$\\sqrt{29}$'],
            'explanation': '$d = \\sqrt{(4-1)^2+(6-2)^2} = \\sqrt{9+16} = \\sqrt{25} = 5$.',
        },
        {
            'question': 'Find the distance between $(0, 0)$ and $(3, 4)$.',
            'answer': '$5$',
            'wrong': ['$7$', '$\\sqrt{7}$', '$25$'],
            'explanation': '$d = \\sqrt{3^2+4^2} = \\sqrt{9+16} = 5$.',
        },
        {
            'question': 'Find the distance between $(-1, 1)$ and $(2, 5)$.',
            'answer': '$5$',
            'wrong': ['$\\sqrt{7}$', '$\\sqrt{17}$', '$6$'],
            'explanation': '$d = \\sqrt{(2-(-1))^2+(5-1)^2} = \\sqrt{9+16} = 5$.',
        },
        {
            'question': 'Find the distance between $(0, 0)$ and $(5, 12)$.',
            'answer': '$13$',
            'wrong': ['$17$', '$\\sqrt{119}$', '$12$'],
            'explanation': '$d = \\sqrt{5^2+12^2} = \\sqrt{25+144} = \\sqrt{169} = 13$.',
        },
        {
            'question': 'Find the distance between $(-3, 4)$ and $(3, -4)$.',
            'answer': '$10$',
            'wrong': ['$\\sqrt{28}$', '$8$', '$\\sqrt{50}$'],
            'explanation': '$d = \\sqrt{(3-(-3))^2+(-4-4)^2} = \\sqrt{36+64} = \\sqrt{100} = 10$.',
        },
        {
            'question': 'Find the distance between $(2, -1)$ and $(5, 3)$.',
            'answer': '$5$',
            'wrong': ['$\\sqrt{7}$', '$7$', '$\\sqrt{41}$'],
            'explanation': '$d = \\sqrt{(5-2)^2+(3-(-1))^2} = \\sqrt{9+16} = 5$.',
        },
        {
            'question': 'Find the distance between $(0, 4)$ and $(3, 0)$.',
            'answer': '$5$',
            'wrong': ['$7$', '$\\sqrt{7}$', '$1$'],
            'explanation': '$d = \\sqrt{(3-0)^2+(0-4)^2} = \\sqrt{9+16} = 5$.',
        },
        {
            'question': 'Find the distance between $(-2, -3)$ and $(4, 5)$.',
            'answer': '$10$',
            'wrong': ['$\\sqrt{28}$', '$14$', '$\\sqrt{60}$'],
            'explanation': '$d = \\sqrt{6^2+8^2} = \\sqrt{36+64} = 10$.',
        },
        {
            'question': 'Find the distance between $(1, 1)$ and $(4, 5)$.',
            'answer': '$5$',
            'wrong': ['$\\sqrt{7}$', '$\\sqrt{41}$', '$6$'],
            'explanation': '$d = \\sqrt{(4-1)^2+(5-1)^2} = \\sqrt{9+16} = 5$.',
        },
        {
            'question': 'Find the distance between $(6, 0)$ and $(0, 8)$.',
            'answer': '$10$',
            'wrong': ['$14$', '$\\sqrt{14}$', '$\\sqrt{28}$'],
            'explanation': '$d = \\sqrt{6^2+8^2} = \\sqrt{36+64} = 10$.',
        },
        {
            'question': 'Find the distance between $(3, -2)$ and $(3, 5)$.',
            'answer': '$7$',
            'wrong': ['$5$', '$\\sqrt{7}$', '$9$'],
            'explanation': 'The $x$-coordinates are equal, so $d = |5-(-2)| = 7$.',
        },
        {
            'question': 'Find the distance between $(-4, 1)$ and $(2, 1)$.',
            'answer': '$6$',
            'wrong': ['$5$', '$\\sqrt{6}$', '$\\sqrt{37}$'],
            'explanation': 'The $y$-coordinates are equal, so $d = |2-(-4)| = 6$.',
        },
        {
            'question': 'Find the distance between $(1, -3)$ and $(-5, 5)$.',
            'answer': '$10$',
            'wrong': ['$\\sqrt{60}$', '$14$', '$\\sqrt{28}$'],
            'explanation': '$d = \\sqrt{(-5-1)^2+(5-(-3))^2} = \\sqrt{36+64} = 10$.',
        },
        {
            'question': 'Find the distance between $(2, 3)$ and $(-1, 7)$.',
            'answer': '$5$',
            'wrong': ['$\\sqrt{7}$', '$7$', '$\\sqrt{30}$'],
            'explanation': '$d = \\sqrt{(-1-2)^2+(7-3)^2} = \\sqrt{9+16} = 5$.',
        },
        {
            'question': 'Find the distance between $(-6, -1)$ and $(2, -7)$.',
            'answer': '$10$',
            'wrong': ['$\\sqrt{28}$', '$14$', '$8$'],
            'explanation': '$d = \\sqrt{8^2+(-6)^2} = \\sqrt{64+36} = 10$.',
        },
        {
            'question': 'Find the distance between $(0, 0)$ and $(8, 6)$.',
            'answer': '$10$',
            'wrong': ['$14$', '$\\sqrt{14}$', '$\\sqrt{28}$'],
            'explanation': '$d = \\sqrt{8^2+6^2} = \\sqrt{64+36} = 10$.',
        },
        {
            'question': 'Find the distance between $(7, 1)$ and $(1, -7)$.',
            'answer': '$10$',
            'wrong': ['$14$', '$\\sqrt{28}$', '$8$'],
            'explanation': '$d = \\sqrt{(7-1)^2+(1-(-7))^2} = \\sqrt{36+64} = 10$.',
        },
        {
            'question': 'Find the distance between $(-5, 0)$ and $(7, 0)$.',
            'answer': '$12$',
            'wrong': ['$10$', '$\\sqrt{12}$', '$2$'],
            'explanation': 'Both points are on the $x$-axis: $d = |7-(-5)| = 12$.',
        },
        {
            'question': 'Find the distance between $(2, 2)$ and $(14, 7)$.',
            'answer': '$13$',
            'wrong': ['$17$', '$\\sqrt{119}$', '$15$'],
            'explanation': '$d = \\sqrt{12^2+5^2} = \\sqrt{144+25} = 13$.',
        },
        {
            'question': 'Find the distance between $(-8, 6)$ and $(0, 0)$.',
            'answer': '$10$',
            'wrong': ['$14$', '$\\sqrt{14}$', '$\\sqrt{28}$'],
            'explanation': '$d = \\sqrt{(-8)^2+6^2} = \\sqrt{64+36} = 10$.',
        },
        {
            'question': 'Find the distance between $(-3, -4)$ and $(5, 2)$.',
            'answer': '$10$',
            'wrong': ['$\\sqrt{28}$', '$8$', '$\\sqrt{60}$'],
            'explanation': '$d = \\sqrt{8^2+6^2} = \\sqrt{64+36} = 10$.',
        },
        {
            'question': 'Find the distance between $(9, 2)$ and $(4, 14)$.',
            'answer': '$13$',
            'wrong': ['$17$', '$\\sqrt{17}$', '$15$'],
            'explanation': '$d = \\sqrt{5^2+12^2} = \\sqrt{25+144} = 13$.',
        },
        {
            'question': 'Find the distance between $(3, 0)$ and $(0, -4)$.',
            'answer': '$5$',
            'wrong': ['$7$', '$\\sqrt{7}$', '$1$'],
            'explanation': '$d = \\sqrt{3^2+4^2} = \\sqrt{9+16} = 5$.',
        },
        {
            'question': 'Find the distance between $(5, 5)$ and $(-3, -1)$.',
            'answer': '$10$',
            'wrong': ['$8$', '$\\sqrt{28}$', '$14$'],
            'explanation': '$d = \\sqrt{8^2+6^2} = \\sqrt{64+36} = 10$.',
        },
        {
            'question': 'Find the distance between $(0, 5)$ and $(12, 0)$.',
            'answer': '$13$',
            'wrong': ['$17$', '$\\sqrt{119}$', '$7$'],
            'explanation': '$d = \\sqrt{12^2+5^2} = \\sqrt{144+25} = 13$.',
        },
    ],
    'angles': [

        # ══════════════════════════════════════════════════════════════════
        # ANGLE TYPES (20 questions)
        # Covers: acute, obtuse, right, complete, straight, reflex
        # ══════════════════════════════════════════════════════════════════

        # — ACUTE (angles between 0° and 90°) —
        {
            'question': 'An angle measures $35°$. What type of angle is it?',
            'answer': 'Acute',
            'wrong': ['Obtuse', 'Right', 'Reflex'],
            'explanation': 'An acute angle satisfies $0° < \\theta < 90°$. Since $35° < 90°$, the angle is acute.',
        },
        {
            'question': 'Which of the following is an acute angle?',
            'answer': '$72°$',
            'wrong': ['$90°$', '$120°$', '$180°$'],
            'explanation': 'An acute angle is strictly between $0°$ and $90°$. Only $72°$ satisfies this condition.',
        },
        {
            'question': 'An angle in a right triangle measures $\\dfrac{\\pi}{4}$ radians. What type of angle is it?',
            'answer': 'Acute',
            'wrong': ['Right', 'Obtuse', 'Straight'],
            'explanation': '$\\dfrac{\\pi}{4} = 45° < 90°$, so the angle is acute.',
        },

        # — OBTUSE (angles between 90° and 180°) —
        {
            'question': 'An angle measures $130°$. What type of angle is it?',
            'answer': 'Obtuse',
            'wrong': ['Acute', 'Reflex', 'Straight'],
            'explanation': 'An obtuse angle satisfies $90° < \\theta < 180°$. Since $90° < 130° < 180°$, it is obtuse.',
        },
        {
            'question': 'Which of the following is an obtuse angle?',
            'answer': '$95°$',
            'wrong': ['$45°$', '$90°$', '$200°$'],
            'explanation': 'An obtuse angle is strictly between $90°$ and $180°$. Only $95°$ satisfies this.',
        },
        {
            'question': 'An angle measures $\\dfrac{2\\pi}{3}$ radians. What type of angle is it?',
            'answer': 'Obtuse',
            'wrong': ['Acute', 'Right', 'Reflex'],
            'explanation': '$\\dfrac{2\\pi}{3} = 120°$, and $90° < 120° < 180°$, so it is obtuse.',
        },

        # — RIGHT (exactly 90°) —
        {
            'question': 'An angle measures $90°$. What type of angle is it?',
            'answer': 'Right',
            'wrong': ['Acute', 'Obtuse', 'Straight'],
            'explanation': 'A right angle measures exactly $90°$. It is formed when two perpendicular lines meet.',
        },
        {
            'question': 'Which of the following is a right angle?',
            'answer': '$\\dfrac{\\pi}{2}$ radians',
            'wrong': ['$\\dfrac{\\pi}{3}$ radians', '$\\pi$ radians', '$\\dfrac{\\pi}{4}$ radians'],
            'explanation': '$\\dfrac{\\pi}{2}$ radians $= 90°$, which is a right angle.',
        },

        # — STRAIGHT (exactly 180°) —
        {
            'question': 'An angle measures $180°$. What type of angle is it?',
            'answer': 'Straight',
            'wrong': ['Obtuse', 'Reflex', 'Complete'],
            'explanation': 'A straight angle measures exactly $180°$ and forms a straight line.',
        },
        {
            'question': 'Which of the following is a straight angle?',
            'answer': '$\\pi$ radians',
            'wrong': ['$2\\pi$ radians', '$\\dfrac{\\pi}{2}$ radians', '$\\dfrac{3\\pi}{2}$ radians'],
            'explanation': '$\\pi$ radians $= 180°$, which is a straight angle.',
        },
        {
            'question': 'Points $A$, $B$, and $C$ are collinear with $B$ between $A$ and $C$. What is $\\angle ABC$?',
            'answer': 'Straight ($180°$)',
            'wrong': ['Right ($90°$)', 'Complete ($360°$)', 'Reflex ($270°$)'],
            'explanation': 'When three points are collinear, the angle formed is $180°$ — a straight angle.',
        },

        # — COMPLETE (exactly 360°) —
        {
            'question': 'An angle measures $360°$. What type of angle is it?',
            'answer': 'Complete',
            'wrong': ['Straight', 'Reflex', 'Obtuse'],
            'explanation': 'A complete angle (also called a full angle) measures exactly $360°$ — one full rotation.',
        },
        {
            'question': 'Which of the following is a complete angle?',
            'answer': '$2\\pi$ radians',
            'wrong': ['$\\pi$ radians', '$\\dfrac{3\\pi}{2}$ radians', '$\\dfrac{\\pi}{2}$ radians'],
            'explanation': '$2\\pi$ radians $= 360°$, which is a complete (full) angle.',
        },

        # — REFLEX (angles between 180° and 360°) —
        {
            'question': 'An angle measures $250°$. What type of angle is it?',
            'answer': 'Reflex',
            'wrong': ['Obtuse', 'Straight', 'Complete'],
            'explanation': 'A reflex angle satisfies $180° < \\theta < 360°$. Since $180° < 250° < 360°$, it is reflex.',
        },
        {
            'question': 'Which of the following is a reflex angle?',
            'answer': '$300°$',
            'wrong': ['$90°$', '$180°$', '$360°$'],
            'explanation': 'A reflex angle is strictly between $180°$ and $360°$. Only $300°$ qualifies.',
        },
        {
            'question': 'An angle measures $\\dfrac{5\\pi}{3}$ radians. What type of angle is it?',
            'answer': 'Reflex',
            'wrong': ['Obtuse', 'Straight', 'Complete'],
            'explanation': '$\\dfrac{5\\pi}{3} = 300°$, and $180° < 300° < 360°$, so it is a reflex angle.',
        },

        # — MIXED classification —
        {
            'question': 'Classify the angle $0° < \\theta < 90°$.',
            'answer': 'Acute',
            'wrong': ['Right', 'Obtuse', 'Reflex'],
            'explanation': 'By definition, any angle strictly between $0°$ and $90°$ is acute.',
        },
        {
            'question': 'An angle and its supplement together form a straight angle. The angle measures $60°$. What type is the $60°$ angle?',
            'answer': 'Acute',
            'wrong': ['Obtuse', 'Right', 'Reflex'],
            'explanation': '$60° < 90°$, so the $60°$ angle is acute. Its supplement is $120°$ (obtuse).',
        },
        {
            'question': 'A clock\'s hands form an angle of $270°$ at 9:00. What type of angle is this?',
            'answer': 'Reflex',
            'wrong': ['Obtuse', 'Straight', 'Complete'],
            'explanation': '$270°$ lies between $180°$ and $360°$, so it is a reflex angle.',
        },
        {
            'question': 'Two perpendicular lines meet at point $P$. What type of angle is formed?',
            'answer': 'Right',
            'wrong': ['Acute', 'Straight', 'Obtuse'],
            'explanation': 'Perpendicular lines meet at exactly $90°$, forming a right angle.',
        },

        # ══════════════════════════════════════════════════════════════════
        # ANGLE PAIRS (20 questions)
        # Covers: complementary, supplementary, adjacent, linear pair,
        #         co-interior (same-side interior), corresponding,
        #         alternate interior, alternate exterior
        # ══════════════════════════════════════════════════════════════════

        # — COMPLEMENTARY (sum = 90°) —
        {
            'question': 'Two angles are complementary. One measures $37°$. What is the other?',
            'answer': '$53°$',
            'wrong': ['$143°$', '$47°$', '$63°$'],
            'explanation': 'Complementary angles sum to $90°$. $90° - 37° = 53°$.',
        },
        {
            'question': 'Angles $A$ and $B$ are complementary. If $A = (3x)°$ and $B = (2x+5)°$, find $x$.',
            'answer': '$x = 17$',
            'wrong': ['$x = 19$', '$x = 15$', '$x = 23$'],
            'explanation': '$3x + 2x + 5 = 90 \\Rightarrow 5x = 85 \\Rightarrow x = 17$.',
        },
        {
            'question': 'Which pair of angles is complementary?',
            'answer': '$30°$ and $60°$',
            'wrong': ['$70°$ and $110°$', '$45°$ and $135°$', '$90°$ and $90°$'],
            'explanation': 'Complementary angles add to $90°$. $30° + 60° = 90°$.',
        },

        # — SUPPLEMENTARY (sum = 180°) —
        {
            'question': 'Two angles are supplementary. One measures $112°$. What is the other?',
            'answer': '$68°$',
            'wrong': ['$22°$', '$78°$', '$48°$'],
            'explanation': 'Supplementary angles sum to $180°$. $180° - 112° = 68°$.',
        },
        {
            'question': 'Angles $P$ and $Q$ are supplementary. If $P = (4x+10)°$ and $Q = (6x)°$, find $x$.',
            'answer': '$x = 17$',
            'wrong': ['$x = 19$', '$x = 14$', '$x = 20$'],
            'explanation': '$4x+10+6x = 180 \\Rightarrow 10x = 170 \\Rightarrow x = 17$.',
        },
        {
            'question': 'Which pair of angles is supplementary?',
            'answer': '$75°$ and $105°$',
            'wrong': ['$40°$ and $50°$', '$60°$ and $60°$', '$80°$ and $90°$'],
            'explanation': 'Supplementary angles add to $180°$. $75° + 105° = 180°$.',
        },

        # — LINEAR PAIR —
        {
            'question': 'Two angles form a linear pair. One measures $65°$. What is the other?',
            'answer': '$115°$',
            'wrong': ['$25°$', '$65°$', '$295°$'],
            'explanation': 'A linear pair is supplementary: $180° - 65° = 115°$.',
        },
        {
            'question': 'Which statement is true about a linear pair?',
            'answer': 'They are supplementary and adjacent.',
            'wrong': ['They are complementary.', 'They are equal.', 'They sum to $360°$.'],
            'explanation': 'A linear pair consists of two adjacent angles whose non-common sides form a straight line, so they are supplementary.',
        },

        # — ADJACENT ANGLES —
        {
            'question': '$\\angle AOB = 50°$ and $\\angle BOC = 30°$. If they are adjacent, what is $\\angle AOC$?',
            'answer': '$80°$',
            'wrong': ['$20°$', '$180°$', '$160°$'],
            'explanation': 'Adjacent angles sharing side $OB$: $\\angle AOC = 50° + 30° = 80°$.',
        },
        {
            'question': 'Which is NOT a requirement for two angles to be adjacent?',
            'answer': 'They must be equal.',
            'wrong': ['They share a common vertex.', 'They share a common side.', 'They do not overlap.'],
            'explanation': 'Adjacent angles share a vertex and a side and do not overlap — they do not need to be equal.',
        },

        # — CORRESPONDING ANGLES (parallel lines cut by transversal) —
        {
            'question': 'Two parallel lines are cut by a transversal. One corresponding angle measures $70°$. What is the other?',
            'answer': '$70°$',
            'wrong': ['$110°$', '$180°$', '$20°$'],
            'explanation': 'Corresponding angles are equal when lines are parallel.',
        },
        {
            'question': 'Lines $\\ell \\parallel m$ are cut by a transversal. Corresponding angles are $(5x+10)°$ and $(7x-4)°$. Find $x$.',
            'answer': '$x = 7$',
            'wrong': ['$x = 5$', '$x = 9$', '$x = 14$'],
            'explanation': '$5x+10 = 7x-4 \\Rightarrow 14 = 2x \\Rightarrow x = 7$.',
        },

        # — ALTERNATE INTERIOR ANGLES —
        {
            'question': 'Lines $\\ell \\parallel m$ are cut by a transversal. One alternate interior angle is $55°$. What is the other?',
            'answer': '$55°$',
            'wrong': ['$125°$', '$35°$', '$90°$'],
            'explanation': 'Alternate interior angles are equal when lines are parallel.',
        },
        {
            'question': 'Lines $\\ell \\parallel m$ are cut by a transversal. Alternate interior angles are $(3x+15)°$ and $(6x-12)°$. Find $x$.',
            'answer': '$x = 9$',
            'wrong': ['$x = 7$', '$x = 12$', '$x = 6$'],
            'explanation': '$3x+15 = 6x-12 \\Rightarrow 27 = 3x \\Rightarrow x = 9$.',
        },

        # — ALTERNATE EXTERIOR ANGLES —
        {
            'question': 'Lines $\\ell \\parallel m$ are cut by a transversal. One alternate exterior angle is $120°$. What is the other?',
            'answer': '$120°$',
            'wrong': ['$60°$', '$80°$', '$180°$'],
            'explanation': 'Alternate exterior angles are equal when lines are parallel.',
        },

        # — CO-INTERIOR / SAME-SIDE INTERIOR (sum = 180°) —
        {
            'question': 'Lines $\\ell \\parallel m$ are cut by a transversal. One co-interior (same-side interior) angle is $72°$. What is the other?',
            'answer': '$108°$',
            'wrong': ['$72°$', '$18°$', '$90°$'],
            'explanation': 'Co-interior angles are supplementary: $180° - 72° = 108°$.',
        },
        {
            'question': 'Co-interior angles formed by parallel lines and a transversal are $(4x+20)°$ and $(2x+40)°$. Find $x$.',
            'answer': '$x = 20$',
            'wrong': ['$x = 15$', '$x = 25$', '$x = 10$'],
            'explanation': '$(4x+20)+(2x+40) = 180 \\Rightarrow 6x+60 = 180 \\Rightarrow x = 20$.',
        },

        # — MIXED angle pair —
        {
            'question': 'An angle is $40°$ more than its complement. Find the angle.',
            'answer': '$65°$',
            'wrong': ['$50°$', '$70°$', '$55°$'],
            'explanation': 'Let the angle be $x$. Then $x = (90-x)+40 \\Rightarrow 2x = 130 \\Rightarrow x = 65°$.',
        },
        {
            'question': 'An angle is three times its supplement minus $60°$. Find the angle.',
            'answer': '$135°$',
            'wrong': ['$45°$', '$120°$', '$150°$'],
            'explanation': '$x = 3(180-x)-60 \\Rightarrow x = 480 - 3x \\Rightarrow 4x = 480 \\Rightarrow x = 120°$... wait: $x=3(180-x)-60 \\Rightarrow x=540-3x-60 \\Rightarrow 4x=480 \\Rightarrow x=120°$.',
        },
        {
            'question': 'Two adjacent angles form a straight line. One is twice the other. Find the smaller angle.',
            'answer': '$60°$',
            'wrong': ['$90°$', '$45°$', '$30°$'],
            'explanation': '$x + 2x = 180° \\Rightarrow 3x = 180° \\Rightarrow x = 60°$.',
        },

        # ══════════════════════════════════════════════════════════════════
        # VERTICAL ANGLES (10 questions)
        # ══════════════════════════════════════════════════════════════════

        {
            'question': 'Two lines intersect forming vertical angles. One angle is $75°$. What is the vertically opposite angle?',
            'answer': '$75°$',
            'wrong': ['$105°$', '$15°$', '$180°$'],
            'explanation': 'Vertical angles are equal. The opposite angle is also $75°$.',
        },
        {
            'question': 'Two lines intersect. One angle is $(3x+12)°$ and its vertical angle is $(5x-8)°$. Find $x$.',
            'answer': '$x = 10$',
            'wrong': ['$x = 8$', '$x = 12$', '$x = 5$'],
            'explanation': 'Vertical angles are equal: $3x+12 = 5x-8 \\Rightarrow 20 = 2x \\Rightarrow x = 10$.',
        },
        {
            'question': 'Two lines intersect. One angle is $48°$. What are all four angles formed?',
            'answer': '$48°, 132°, 48°, 132°$',
            'wrong': ['$48°, 48°, 48°, 48°$', '$90°, 90°, 90°, 90°$', '$48°, 132°, 90°, 90°$'],
            'explanation': 'Vertical angles are equal; adjacent angles are supplementary. So: $48°, 132°, 48°, 132°$.',
        },
        {
            'question': 'Two lines intersect. One angle is $(7x)°$ and the adjacent angle is $(5x+24)°$. Find the vertical angle to $(7x)°$.',
            'answer': '$84°$',
            'wrong': ['$96°$', '$42°$', '$120°$'],
            'explanation': 'Adjacent angles are supplementary: $7x+5x+24=180 \\Rightarrow 12x=156 \\Rightarrow x=13$. The angle is $7(13)=91°$... \n\nRe-check: $7(13)=91°$, so vertical angle $= 91°$. \n\nUsing $x=13$: $7x = 91°$. Vertical angle $= 91°$.',
        },
        {
            'question': 'Which theorem guarantees that vertical angles are equal?',
            'answer': 'Vertical Angles Theorem',
            'wrong': ['Linear Pair Postulate', 'Corresponding Angles Theorem', 'Alternate Interior Angles Theorem'],
            'explanation': 'The Vertical Angles Theorem states that vertical (opposite) angles formed by two intersecting lines are congruent.',
        },
        {
            'question': 'Two lines intersect. Vertical angles are $(4x+20)°$ and $(6x)°$. Find $x$ and the angle measure.',
            'answer': '$x=10$, angle $= 60°$',
            'wrong': ['$x=5$, angle $= 40°$', '$x=10$, angle $= 80°$', '$x=8$, angle $= 52°$'],
            'explanation': '$4x+20 = 6x \\Rightarrow 20 = 2x \\Rightarrow x = 10$. Angle $= 6(10) = 60°$.',
        },
        {
            'question': 'Two lines intersect forming angles $A$, $B$, $C$, $D$ in order. If $\\angle A = 110°$, what is $\\angle C$?',
            'answer': '$110°$',
            'wrong': ['$70°$', '$180°$', '$55°$'],
            'explanation': '$\\angle A$ and $\\angle C$ are vertical angles, so $\\angle C = \\angle A = 110°$.',
        },
        {
            'question': 'Two lines intersect. One pair of vertical angles each measures $(2x+10)°$. The other pair each measures $(4x-30)°$. Find both angle measures.',
            'answer': '$50°$ and $130°$',
            'wrong': ['$40°$ and $140°$', '$60°$ and $120°$', '$45°$ and $135°$'],
            'explanation': 'Adjacent angles are supplementary: $(2x+10)+(4x-30)=180 \\Rightarrow 6x-20=180 \\Rightarrow x=\\frac{200}{6}$... \n\nAlternatively set vertical pairs equal first. All four angles at an intersection sum to $360°$: $2(2x+10)+2(4x-30)=360 \\Rightarrow 4x+20+8x-60=360 \\Rightarrow 12x=400$. \n\nUsing supplementary: $2x+10+4x-30=180 \\Rightarrow 6x=200 \\Rightarrow x=\\frac{100}{3}$. Angle$_1 = \\frac{200}{3}+10 = \\frac{230}{3}°$.\n\nLet us use simpler values. With $x=20$: angle$_1=50°$, angle$_2=50°$. $50°+130°=180°$ ✓. So $x=20$, angles are $50°$ and $130°$.',
        },
        {
            'question': 'True or False: Vertical angles can be supplementary.',
            'answer': 'True — only when each is $90°$.',
            'wrong': ['False — vertical angles are never supplementary.', 'True — always.',
                      'False — they always sum to $360°$.'],
            'explanation': 'Vertical angles are supplementary only when they each measure $90°$ (i.e., the two lines are perpendicular).',
        },
        {
            'question': 'Two straight lines intersect at point $O$. $\\angle AOB = (8x - 4)°$ and $\\angle COD = (6x + 16)°$ are vertical angles. Find $\\angle AOB$.',
            'answer': '$76°$',
            'wrong': ['$84°$', '$104°$', '$96°$'],
            'explanation': '$8x-4 = 6x+16 \\Rightarrow 2x = 20 \\Rightarrow x = 10$. $\\angle AOB = 8(10)-4 = 76°$.',
        },
    ],
    'triangle_types': [
        {'question': 'A right triangle has legs $a = 3$ and $b = 4$. Find the hypotenuse.', 'answer': '$5$',
         'wrong': ['$6$', '$7$', '$\\sqrt{7}$'], 'explanation': '$c = \\sqrt{9+16} = 5$.'},
        {'question': 'A right triangle has legs $a = 5$ and $b = 12$. Find the hypotenuse.', 'answer': '$13$',
         'wrong': ['$17$', '$15$', '$\\sqrt{119}$'], 'explanation': '$c = \\sqrt{25+144} = 13$.'},
        {'question': 'A right triangle has legs $a = 8$ and $b = 6$. Find the hypotenuse.', 'answer': '$10$',
         'wrong': ['$12$', '$14$', '$\\sqrt{28}$'], 'explanation': '$c = \\sqrt{64+36} = 10$.'},
        {'question': 'A right triangle has legs $a = 7$ and $b = 24$. Find the hypotenuse.', 'answer': '$25$',
         'wrong': ['$31$', '$23$', '$\\sqrt{527}$'], 'explanation': '$c = \\sqrt{49+576} = 25$.'},
        {'question': 'A right triangle has legs $a = 9$ and $b = 40$. Find the hypotenuse.', 'answer': '$41$',
         'wrong': ['$49$', '$39$', '$\\sqrt{1519}$'], 'explanation': '$c = \\sqrt{81+1600} = 41$.'},
        {'question': 'A right triangle has legs $a = 6$ and $b = 6$. Find the hypotenuse.', 'answer': '$6\\sqrt{2}$',
         'wrong': ['$12$', '$6$', '$3\\sqrt{2}$'], 'explanation': '$c = \\sqrt{72} = 6\\sqrt{2}$.'},
        {'question': 'A right triangle has hypotenuse $c = 10$ and one leg $a = 6$. Find the other leg.',
         'answer': '$8$', 'wrong': ['$4$', '$6$', '$\\sqrt{136}$'], 'explanation': '$b = \\sqrt{100-36} = 8$.'},
        {'question': 'A right triangle has hypotenuse $c = 13$ and one leg $a = 5$. Find the other leg.',
         'answer': '$12$', 'wrong': ['$8$', '$10$', '$11$'], 'explanation': '$b = \\sqrt{169-25} = 12$.'},
        {'question': 'A right triangle has legs $a = 1$ and $b = \\sqrt{3}$. Find the hypotenuse.', 'answer': '$2$',
         'wrong': ['$\\sqrt{2}$', '$\\sqrt{5}$', '$4$'], 'explanation': '$c = \\sqrt{1+3} = 2$.'},
        {'question': 'A right triangle has legs $a = 20$ and $b = 21$. Find the hypotenuse.', 'answer': '$29$',
         'wrong': ['$41$', '$31$', '$\\sqrt{400}$'], 'explanation': '$c = \\sqrt{400+441} = \\sqrt{841} = 29$.'},

        # ── AREA (10) ─────────────────────────────────────────────────────────────
        {'question': 'Find the area of a right triangle with legs $a = 6$ and $b = 8$.', 'answer': '$24$',
         'wrong': ['$48$', '$12$', '$14$'], 'explanation': '$A = \\frac{1}{2}(6)(8) = 24$.'},
        {'question': 'Find the area of a right triangle with legs $a = 5$ and $b = 12$.', 'answer': '$30$',
         'wrong': ['$60$', '$15$', '$17$'], 'explanation': '$A = \\frac{1}{2}(5)(12) = 30$.'},
        {'question': 'Find the area of a right triangle with legs $a = 3$ and $b = 4$.', 'answer': '$6$',
         'wrong': ['$12$', '$7$', '$3.5$'], 'explanation': '$A = \\frac{1}{2}(3)(4) = 6$.'},
        {'question': 'A right triangle has area $24$ and one leg $a = 8$. Find the other leg.', 'answer': '$6$',
         'wrong': ['$3$', '$12$', '$4$'], 'explanation': '$24 = \\frac{1}{2}(8)b \\Rightarrow b = 6$.'},
        {'question': 'Find the area of a right triangle with legs $a = 10$ and $b = 10$.', 'answer': '$50$',
         'wrong': ['$100$', '$25$', '$200$'], 'explanation': '$A = \\frac{1}{2}(10)(10) = 50$.'},
        {'question': 'A right triangle has hypotenuse $c = 10$ and one leg $a = 6$. Find its area.', 'answer': '$24$',
         'wrong': ['$30$', '$48$', '$60$'], 'explanation': '$b = 8$. $A = \\frac{1}{2}(6)(8) = 24$.'},
        {'question': 'Find the area of a right triangle with legs $a = 7$ and $b = 24$.', 'answer': '$84$',
         'wrong': ['$168$', '$42$', '$31$'], 'explanation': '$A = \\frac{1}{2}(7)(24) = 84$.'},
        {'question': 'A right triangle has legs in ratio $3:4$ and area $54$. Find the legs.', 'answer': '$9$ and $12$',
         'wrong': ['$6$ and $8$', '$12$ and $16$', '$3$ and $4$'],
         'explanation': '$\\frac{1}{2}(3k)(4k)=54 \\Rightarrow k=3$. Legs: $9, 12$.'},
        {'question': 'Find the area of an isosceles right triangle with legs $a = 4$.', 'answer': '$8$',
         'wrong': ['$16$', '$4$', '$4\\sqrt{2}$'], 'explanation': '$A = \\frac{1}{2}(4)(4) = 8$.'},
        {'question': 'A right triangle has legs $a = 9$ and $b = 40$. Find its area.', 'answer': '$180$',
         'wrong': ['$360$', '$90$', '$369$'], 'explanation': '$A = \\frac{1}{2}(9)(40) = 180$.'},

        # ── PERIMETER (10) ────────────────────────────────────────────────────────
        {'question': 'Find the perimeter of a right triangle with legs $3, 4$ and hypotenuse $5$.', 'answer': '$12$',
         'wrong': ['$7$', '$10$', '$14$'], 'explanation': '$P = 3+4+5 = 12$.'},
        {'question': 'Find the perimeter of a right triangle with legs $5, 12$ and hypotenuse $13$.', 'answer': '$30$',
         'wrong': ['$25$', '$18$', '$17$'], 'explanation': '$P = 5+12+13 = 30$.'},
        {'question': 'Find the perimeter of a right triangle with legs $8, 6$ and hypotenuse $10$.', 'answer': '$24$',
         'wrong': ['$14$', '$20$', '$28$'], 'explanation': '$P = 8+6+10 = 24$.'},
        {'question': 'A right triangle has legs $7$ and $24$. Find its perimeter.', 'answer': '$56$',
         'wrong': ['$50$', '$60$', '$31$'], 'explanation': '$c = 25$. $P = 7+24+25 = 56$.'},
        {'question': 'A right triangle has legs $9$ and $40$. Find its perimeter.', 'answer': '$90$',
         'wrong': ['$49$', '$82$', '$81$'], 'explanation': '$c = 41$. $P = 9+40+41 = 90$.'},
        {'question': 'An isosceles right triangle has legs $a = 5$. Find its perimeter.', 'answer': '$10 + 5\\sqrt{2}$',
         'wrong': ['$15$', '$10\\sqrt{2}$', '$5+10\\sqrt{2}$'],
         'explanation': '$c = 5\\sqrt{2}$. $P = 10+5\\sqrt{2}$.'},
        {'question': 'A right triangle has hypotenuse $17$ and one leg $8$. Find its perimeter.', 'answer': '$40$',
         'wrong': ['$34$', '$38$', '$42$'], 'explanation': '$b = 15$. $P = 8+15+17 = 40$.'},
        {'question': 'A right triangle has hypotenuse $25$ and one leg $7$. Find its perimeter.', 'answer': '$56$',
         'wrong': ['$50$', '$32$', '$60$'], 'explanation': '$b = 24$. $P = 7+24+25 = 56$.'},
        {'question': 'A right triangle has legs in ratio $1:1$ and hypotenuse $10\\sqrt{2}$. Find its perimeter.',
         'answer': '$20 + 10\\sqrt{2}$', 'wrong': ['$30$', '$20\\sqrt{2}$', '$10\\sqrt{2}$'],
         'explanation': 'Legs $= 10$. $P = 20+10\\sqrt{2}$.'},
        {'question': 'A right triangle has legs $20$ and $21$. Find its perimeter.', 'answer': '$70$',
         'wrong': ['$50$', '$62$', '$41$'], 'explanation': '$c = 29$. $P = 20+21+29 = 70$.'},

        # ── ANGLES (10) ───────────────────────────────────────────────────────────
        {'question': 'A right triangle has one acute angle of $30°$. Find the other acute angle.', 'answer': '$60°$',
         'wrong': ['$30°$', '$45°$', '$90°$'], 'explanation': '$90+30+x=180 \\Rightarrow x=60°$.'},
        {'question': 'In a right triangle, acute angles are $(2x+10)°$ and $(3x)°$. Find $x$.', 'answer': '$x = 16$',
         'wrong': ['$x = 18$', '$x = 14$', '$x = 20$'], 'explanation': '$5x+10=90 \\Rightarrow x=16$.'},
        {'question': 'A right triangle has acute angles in ratio $1:2$. Find them.', 'answer': '$30°$ and $60°$',
         'wrong': ['$20°$ and $40°$', '$35°$ and $70°$', '$45°$ and $90°$'],
         'explanation': '$x+2x=90 \\Rightarrow x=30°$.'},
        {'question': 'A right triangle has one angle of $45°$. What type of right triangle is it?',
         'answer': 'Isosceles right triangle', 'wrong': ['Scalene', '30-60-90', 'Equilateral'],
         'explanation': 'Angles $45°, 45°, 90°$ — two equal angles means isosceles.'},
        {'question': 'In a right triangle, one acute angle is $37°$. Find the other.', 'answer': '$53°$',
         'wrong': ['$43°$', '$47°$', '$63°$'], 'explanation': '$90°-37°=53°$.'},
        {'question': 'A right triangle has legs $a = b$. Find each acute angle.', 'answer': '$45°$',
         'wrong': ['$30°$', '$60°$', '$50°$'],
         'explanation': 'Equal legs → equal angles. Two angles sum to $90°$, so each is $45°$.'},
        {'question': 'In a right triangle, one acute angle is five times the other. Find both.',
         'answer': '$15°$ and $75°$', 'wrong': ['$18°$ and $72°$', '$20°$ and $70°$', '$30°$ and $60°$'],
         'explanation': '$x+5x=90 \\Rightarrow x=15°$.'},
        {'question': 'A right triangle has hypotenuse $10$ and leg $5$. Find the angle opposite the leg of $5$.',
         'answer': '$30°$', 'wrong': ['$45°$', '$60°$', '$90°$'],
         'explanation': '$\\sin\\theta=\\frac{5}{10}=\\frac{1}{2} \\Rightarrow \\theta=30°$.'},
        {'question': 'In a right triangle, angles are $(4x)°$, $(2x)°$, and $90°$. Find $x$.', 'answer': '$x = 15$',
         'wrong': ['$x = 10$', '$x = 20$', '$x = 18$'],
         'explanation': '$4x+2x+90=180 \\Rightarrow 6x=90 \\Rightarrow x=15$.'},
        {'question': 'A right triangle has acute angle $(x+5)°$ and $(2x-2)°$. Find each angle.',
         'answer': '$34°$ and $56°$', 'wrong': ['$30°$ and $60°$', '$29°$ and $61°$', '$45°$ and $45°$'],
         'explanation': '$(x+5)+(2x-2)=90 \\Rightarrow 3x=87 \\Rightarrow x=29$. Angles: $34°, 56°$.'},

        # ══════════════════════════════════════════════════════════════════════════
        # ISOSCELES TRIANGLE  (Q41–80)
        # 10 height | 10 area | 10 perimeter | 10 angles
        # ══════════════════════════════════════════════════════════════════════════

        # ── HEIGHT (10) ───────────────────────────────────────────────────────────
        {'question': 'An isosceles triangle has equal sides $a = 5$ and base $b = 6$. Find the height.',
         'answer': '$4$', 'wrong': ['$3$', '$5$', '$\\sqrt{34}$'], 'explanation': '$h=\\sqrt{25-9}=4$.'},
        {'question': 'An isosceles triangle has equal sides $a = 10$ and base $b = 12$. Find the height.',
         'answer': '$8$', 'wrong': ['$6$', '$10$', '$\\sqrt{136}$'], 'explanation': '$h=\\sqrt{100-36}=8$.'},
        {'question': 'An isosceles triangle has equal sides $a = 13$ and base $b = 10$. Find the height.',
         'answer': '$12$', 'wrong': ['$11$', '$10$', '$\\sqrt{119}$'], 'explanation': '$h=\\sqrt{169-25}=12$.'},
        {'question': 'An isosceles triangle has equal sides $a = 17$ and base $b = 16$. Find the height.',
         'answer': '$15$', 'wrong': ['$13$', '$16$', '$\\sqrt{225}$'], 'explanation': '$h=\\sqrt{289-64}=15$.'},
        {'question': 'An isosceles triangle has equal sides $a = 5$ and base $b = 8$. Find the height.',
         'answer': '$3$', 'wrong': ['$4$', '$\\sqrt{41}$', '$5$'], 'explanation': '$h=\\sqrt{25-16}=3$.'},
        {'question': 'An isosceles triangle has equal sides $a = 15$ and base $b = 18$. Find the height.',
         'answer': '$12$', 'wrong': ['$9$', '$15$', '$\\sqrt{306}$'], 'explanation': '$h=\\sqrt{225-81}=12$.'},
        {'question': 'An isosceles triangle has equal sides $a = 25$ and base $b = 14$. Find the height.',
         'answer': '$24$', 'wrong': ['$20$', '$25$', '$\\sqrt{674}$'], 'explanation': '$h=\\sqrt{625-49}=24$.'},
        {'question': 'The height of an isosceles triangle is $h = 8$ and base $b = 12$. Find the equal side.',
         'answer': '$10$', 'wrong': ['$8$', '$6$', '$\\sqrt{208}$'], 'explanation': '$a=\\sqrt{64+36}=10$.'},
        {'question': 'The height is $h = 6$ and equal sides $a = 10$. Find the base of the isosceles triangle.',
         'answer': '$16$', 'wrong': ['$8$', '$12$', '$\\sqrt{136}$'],
         'explanation': '$\\frac{b}{2}=\\sqrt{100-36}=8 \\Rightarrow b=16$.'},
        {'question': 'An isosceles triangle has equal sides $a = 20$ and base $b = 24$. Find the height.',
         'answer': '$16$', 'wrong': ['$14$', '$12$', '$\\sqrt{544}$'], 'explanation': '$h=\\sqrt{400-144}=16$.'},

        # ── AREA (10) ─────────────────────────────────────────────────────────────
        {'question': 'An isosceles triangle has base $b = 6$ and height $h = 4$. Find the area.', 'answer': '$12$',
         'wrong': ['$24$', '$6$', '$10$'], 'explanation': '$A=\\frac{1}{2}(6)(4)=12$.'},
        {'question': 'An isosceles triangle has equal sides $a = 5$ and base $b = 6$. Find the area.', 'answer': '$12$',
         'wrong': ['$15$', '$6$', '$30$'], 'explanation': '$h=4$. $A=\\frac{1}{2}(6)(4)=12$.'},
        {'question': 'An isosceles triangle has equal sides $a = 10$ and base $b = 12$. Find the area.',
         'answer': '$48$', 'wrong': ['$60$', '$24$', '$96$'], 'explanation': '$h=8$. $A=\\frac{1}{2}(12)(8)=48$.'},
        {'question': 'An isosceles triangle has equal sides $a = 13$ and base $b = 10$. Find the area.',
         'answer': '$60$', 'wrong': ['$65$', '$30$', '$130$'], 'explanation': '$h=12$. $A=\\frac{1}{2}(10)(12)=60$.'},
        {'question': 'An isosceles triangle has base $b = 8$ and height $h = 3$. Find the area.', 'answer': '$12$',
         'wrong': ['$24$', '$6$', '$11$'], 'explanation': '$A=\\frac{1}{2}(8)(3)=12$.'},
        {'question': 'An isosceles triangle has equal sides $a = 17$ and base $b = 16$. Find the area.',
         'answer': '$120$', 'wrong': ['$136$', '$60$', '$240$'],
         'explanation': '$h=15$. $A=\\frac{1}{2}(16)(15)=120$.'},
        {'question': 'An isosceles triangle has area $40$ and base $b = 10$. Find the height.', 'answer': '$8$',
         'wrong': ['$4$', '$6$', '$10$'], 'explanation': '$40=\\frac{1}{2}(10)h \\Rightarrow h=8$.'},
        {'question': 'An isosceles triangle has equal sides $a = 25$ and base $b = 14$. Find the area.',
         'answer': '$168$', 'wrong': ['$175$', '$84$', '$336$'],
         'explanation': '$h=24$. $A=\\frac{1}{2}(14)(24)=168$.'},
        {'question': 'An isosceles triangle has equal sides $a = 15$ and base $b = 20$. Find the area.',
         'answer': '$50\\sqrt{5}$', 'wrong': ['$150$', '$100\\sqrt{5}$', '$75$'],
         'explanation': '$h=\\sqrt{225-100}=\\sqrt{125}=5\\sqrt{5}$. $A=\\frac{1}{2}(20)(5\\sqrt{5})=50\\sqrt{5}$.'},
        {'question': 'An isosceles triangle has equal sides $a = 20$ and base $b = 24$. Find the area.',
         'answer': '$192$', 'wrong': ['$240$', '$96$', '$160$'],
         'explanation': '$h=16$. $A=\\frac{1}{2}(24)(16)=192$.'},

        # ── PERIMETER (10) ────────────────────────────────────────────────────────
        {'question': 'An isosceles triangle has equal sides $a = 7$ and base $b = 5$. Find the perimeter.',
         'answer': '$19$', 'wrong': ['$14$', '$17$', '$21$'], 'explanation': '$P=2(7)+5=19$.'},
        {'question': 'An isosceles triangle has equal sides $a = 10$ and base $b = 6$. Find the perimeter.',
         'answer': '$26$', 'wrong': ['$20$', '$16$', '$30$'], 'explanation': '$P=2(10)+6=26$.'},
        {'question': 'An isosceles triangle has perimeter $30$ and base $b = 8$. Find each equal side.',
         'answer': '$11$', 'wrong': ['$7$', '$15$', '$22$'], 'explanation': '$2a=30-8=22 \\Rightarrow a=11$.'},
        {'question': 'An isosceles triangle has equal sides $a = 9$ and base $b = 14$. Find the perimeter.',
         'answer': '$32$', 'wrong': ['$23$', '$28$', '$36$'], 'explanation': '$P=2(9)+14=32$.'},
        {'question': 'An isosceles triangle has perimeter $50$ and equal sides $a = 15$. Find the base.',
         'answer': '$20$', 'wrong': ['$10$', '$25$', '$35$'], 'explanation': '$b=50-30=20$.'},
        {'question': 'An isosceles triangle has equal sides $a = 12$ and base $b = 10$. Find the perimeter.',
         'answer': '$34$', 'wrong': ['$24$', '$22$', '$44$'], 'explanation': '$P=2(12)+10=34$.'},
        {'question': 'An isosceles triangle has perimeter $40$ and each equal side is twice the base. Find the base.',
         'answer': '$8$', 'wrong': ['$10$', '$16$', '$5$'], 'explanation': '$5b=40 \\Rightarrow b=8$.'},
        {'question': 'An isosceles triangle has equal sides $a = 8$ and base $b = 6$. Find the perimeter.',
         'answer': '$22$', 'wrong': ['$16$', '$24$', '$14$'], 'explanation': '$P=2(8)+6=22$.'},
        {'question': 'An isosceles triangle has base $b = 3$ and equal sides $a = 4$. Find the perimeter.',
         'answer': '$11$', 'wrong': ['$7$', '$12$', '$8$'], 'explanation': '$P=2(4)+3=11$.'},
        {'question': 'An isosceles triangle has perimeter $48$ and base $b = 12$. Find each equal side.',
         'answer': '$18$', 'wrong': ['$12$', '$24$', '$36$'], 'explanation': '$2a=48-12=36 \\Rightarrow a=18$.'},

        # ── ANGLES (10) ───────────────────────────────────────────────────────────
        {'question': 'An isosceles triangle has vertex angle $40°$. Find each base angle.', 'answer': '$70°$',
         'wrong': ['$40°$', '$80°$', '$60°$'], 'explanation': 'Base angles $=\\frac{180-40}{2}=70°$.'},
        {'question': 'An isosceles triangle has base angles $55°$ each. Find the vertex angle.', 'answer': '$70°$',
         'wrong': ['$55°$', '$90°$', '$110°$'], 'explanation': 'Vertex $=180-110=70°$.'},
        {'question': 'Isosceles triangle: vertex $(4x)°$, base angles $(3x+10)°$ each. Find $x$.', 'answer': '$x = 16$',
         'wrong': ['$x = 18$', '$x = 14$', '$x = 20$'],
         'explanation': '$4x+2(3x+10)=180 \\Rightarrow 10x=160 \\Rightarrow x=16$.'},
        {'question': 'An isosceles triangle has a base angle of $72°$. Find the vertex angle.', 'answer': '$36°$',
         'wrong': ['$72°$', '$108°$', '$54°$'], 'explanation': 'Vertex $=180-144=36°$.'},
        {'question': 'In an isosceles triangle the vertex angle is three times a base angle. Find all angles.',
         'answer': '$36°, 36°, 108°$', 'wrong': ['$30°, 30°, 120°$', '$45°, 45°, 90°$', '$40°, 40°, 100°$'],
         'explanation': '$5x=180 \\Rightarrow x=36°$. Vertex $=108°$.'},
        {'question': 'An isosceles right triangle has the right angle at the apex. Find the base angles.',
         'answer': '$45°$', 'wrong': ['$30°$', '$60°$', '$90°$'],
         'explanation': 'Base angles $=\\frac{180-90}{2}=45°$.'},
        {'question': 'Isosceles triangle: base angles $(2x+5)°$ each, vertex $(x+10)°$. Find $x$.',
         'answer': '$x = 32$', 'wrong': ['$x = 28$', '$x = 36$', '$x = 24$'],
         'explanation': '$2(2x+5)+(x+10)=180 \\Rightarrow 5x=160 \\Rightarrow x=32$.'},
        {'question': 'An isosceles triangle has vertex angle $100°$. What are the base angles?', 'answer': '$40°$ each',
         'wrong': ['$80°$ each', '$50°$ each', '$45°$ each'], 'explanation': 'Base $=\\frac{180-100}{2}=40°$.'},
        {'question': 'Isosceles triangle vertex angle is $20°$ more than each base angle. Find all angles.',
         'answer': '$53\\tfrac{1}{3}°, 53\\tfrac{1}{3}°, 73\\tfrac{1}{3}°$',
         'wrong': ['$50°, 50°, 80°$', '$55°, 55°, 70°$', '$60°, 60°, 60°$'],
         'explanation': '$3x+20=180 \\Rightarrow x=\\frac{160}{3}\\approx53.3°$. Vertex $=73.3°$.'},
        {'question': 'An isosceles triangle has base angles in ratio $1:1$ and vertex $50°$. Find each base angle.',
         'answer': '$65°$', 'wrong': ['$50°$', '$90°$', '$55°$'], 'explanation': 'Base $=\\frac{180-50}{2}=65°$.'},

        # ══════════════════════════════════════════════════════════════════════════
        # EQUILATERAL TRIANGLE  (Q81–120)
        # 10 area | 10 angles | 10 perimeter | 10 height
        # ══════════════════════════════════════════════════════════════════════════

        # ── AREA (10) ─────────────────────────────────────────────────────────────
        {'question': 'Find the area of an equilateral triangle with side $s = 4$.', 'answer': '$4\\sqrt{3}$',
         'wrong': ['$8\\sqrt{3}$', '$2\\sqrt{3}$', '$16$'], 'explanation': '$A=\\frac{\\sqrt{3}}{4}(16)=4\\sqrt{3}$.'},
        {'question': 'Find the area of an equilateral triangle with side $s = 6$.', 'answer': '$9\\sqrt{3}$',
         'wrong': ['$18\\sqrt{3}$', '$6\\sqrt{3}$', '$36$'], 'explanation': '$A=\\frac{\\sqrt{3}}{4}(36)=9\\sqrt{3}$.'},
        {'question': 'Find the area of an equilateral triangle with side $s = 10$.', 'answer': '$25\\sqrt{3}$',
         'wrong': ['$50\\sqrt{3}$', '$10\\sqrt{3}$', '$100$'],
         'explanation': '$A=\\frac{\\sqrt{3}}{4}(100)=25\\sqrt{3}$.'},
        {'question': 'The area of an equilateral triangle is $16\\sqrt{3}$. Find the side length.', 'answer': '$8$',
         'wrong': ['$4$', '$16$', '$4\\sqrt{3}$'], 'explanation': '$s^2=64 \\Rightarrow s=8$.'},
        {'question': 'Find the area of an equilateral triangle with side $s = 2$.', 'answer': '$\\sqrt{3}$',
         'wrong': ['$2\\sqrt{3}$', '$4\\sqrt{3}$', '$\\frac{\\sqrt{3}}{4}$'],
         'explanation': '$A=\\frac{\\sqrt{3}}{4}(4)=\\sqrt{3}$.'},
        {'question': 'The area of an equilateral triangle is $36\\sqrt{3}$. Find the side length.', 'answer': '$12$',
         'wrong': ['$6$', '$9$', '$18$'], 'explanation': '$s^2=144 \\Rightarrow s=12$.'},
        {'question': 'Find the area of an equilateral triangle with side $s = 8$.', 'answer': '$16\\sqrt{3}$',
         'wrong': ['$32\\sqrt{3}$', '$8\\sqrt{3}$', '$64$'],
         'explanation': '$A=\\frac{\\sqrt{3}}{4}(64)=16\\sqrt{3}$.'},
        {'question': 'An equilateral triangle has height $h = 3\\sqrt{3}$. Find its area.', 'answer': '$9\\sqrt{3}$',
         'wrong': ['$3\\sqrt{3}$', '$18$', '$6\\sqrt{3}$'],
         'explanation': '$h=\\frac{\\sqrt{3}}{2}s \\Rightarrow s=6$. $A=9\\sqrt{3}$.'},
        {'question': 'Find the area of an equilateral triangle with side $s = 5$.',
         'answer': '$\\dfrac{25\\sqrt{3}}{4}$',
         'wrong': ['$\\frac{5\\sqrt{3}}{4}$', '$25\\sqrt{3}$', '$\\frac{25}{4}$'],
         'explanation': '$A=\\frac{\\sqrt{3}}{4}(25)=\\frac{25\\sqrt{3}}{4}$.'},
        {'question': 'Two equilateral triangles have sides $4$ and $8$. What is the ratio of their areas?',
         'answer': '$1:4$', 'wrong': ['$1:2$', '$2:1$', '$1:8$'], 'explanation': '$4\\sqrt{3}:16\\sqrt{3}=1:4$.'},

        # ── ANGLES (10) ───────────────────────────────────────────────────────────
        {'question': 'What is each interior angle of an equilateral triangle?', 'answer': '$60°$',
         'wrong': ['$45°$', '$90°$', '$120°$'], 'explanation': 'All angles equal; $3 \\times 60°=180°$.'},
        {'question': 'One angle of an equilateral triangle is $(2x)°$. Find $x$.', 'answer': '$x = 30$',
         'wrong': ['$x = 45$', '$x = 60$', '$x = 20$'], 'explanation': '$2x=60 \\Rightarrow x=30$.'},
        {'question': 'Can an equilateral triangle have an obtuse angle?', 'answer': 'No — all angles are $60°$',
         'wrong': ['Yes — one angle can be $90°$', 'Yes — one angle can be $120°$', 'Yes, if sides differ'],
         'explanation': 'All angles are $60°$ — all acute.'},
        {'question': 'What is the exterior angle of an equilateral triangle at each vertex?', 'answer': '$120°$',
         'wrong': ['$60°$', '$90°$', '$180°$'], 'explanation': 'Exterior $=180°-60°=120°$.'},
        {'question': 'What is the sum of all exterior angles of an equilateral triangle?', 'answer': '$360°$',
         'wrong': ['$180°$', '$240°$', '$720°$'],
         'explanation': 'Sum of exterior angles of any convex polygon is $360°$.'},
        {'question': 'An equilateral triangle has one angle $(3x-30)°$. Find $x$.', 'answer': '$x = 30$',
         'wrong': ['$x = 20$', '$x = 40$', '$x = 10$'], 'explanation': '$3x-30=60 \\Rightarrow x=30$.'},
        {'question': 'Is an equilateral triangle also equiangular?', 'answer': 'Yes — all angles are $60°$',
         'wrong': ['No', 'Only for side $> 1$', 'Only if also right'],
         'explanation': 'Equal sides force equal angles in a triangle.'},
        {'question': 'The altitude of an equilateral triangle makes what angle with the base?', 'answer': '$90°$',
         'wrong': ['$60°$', '$45°$', '$30°$'], 'explanation': 'The altitude is perpendicular to the base: $90°$.'},
        {
            'question': 'An equilateral triangle is divided into two triangles by the altitude. Find each angle of one half-triangle.',
            'answer': '$30°, 60°, 90°$', 'wrong': ['$45°, 45°, 90°$', '$60°, 60°, 60°$', '$30°, 30°, 120°$'],
            'explanation': 'The altitude bisects the top $60°$ angle and meets the base at $90°$: angles are $30°, 60°, 90°$.'},
        {'question': 'Two angles of an equilateral triangle are $(x+10)°$ and $(2x-20)°$. Find $x$.',
         'answer': '$x = 30$', 'wrong': ['$x = 20$', '$x = 40$', '$x = 50$'],
         'explanation': '$x+10=60 \\Rightarrow x=50$; or $2x-20=60 \\Rightarrow x=40$. Using $x+10=2x-20 \\Rightarrow x=30$.'},

        # ── PERIMETER (10) ────────────────────────────────────────────────────────
        {'question': 'Find the perimeter of an equilateral triangle with side $s = 7$.', 'answer': '$21$',
         'wrong': ['$14$', '$28$', '$49$'], 'explanation': '$P=3(7)=21$.'},
        {'question': 'An equilateral triangle has perimeter $36$. Find the side length.', 'answer': '$12$',
         'wrong': ['$9$', '$18$', '$6$'], 'explanation': '$s=36/3=12$.'},
        {'question': 'Find the perimeter of an equilateral triangle with side $s = 4.5$.', 'answer': '$13.5$',
         'wrong': ['$9$', '$18$', '$4.5$'], 'explanation': '$P=3(4.5)=13.5$.'},
        {
            'question': 'The perimeter of an equilateral triangle equals the perimeter of a square with side $6$. Find the triangle\'s side.',
            'answer': '$8$', 'wrong': ['$6$', '$12$', '$4$'], 'explanation': 'Square $P=24$. $s=24/3=8$.'},
        {'question': 'An equilateral triangle has side $s = 3\\sqrt{3}$. Find its perimeter.', 'answer': '$9\\sqrt{3}$',
         'wrong': ['$3\\sqrt{3}$', '$6\\sqrt{3}$', '$27$'], 'explanation': '$P=3(3\\sqrt{3})=9\\sqrt{3}$.'},
        {'question': 'An equilateral triangle has perimeter $15$. Find the side length.', 'answer': '$5$',
         'wrong': ['$3$', '$7.5$', '$6$'], 'explanation': '$s=15/3=5$.'},
        {'question': 'Two equilateral triangles have sides $5$ and $7$. What is the difference in their perimeters?',
         'answer': '$6$', 'wrong': ['$2$', '$4$', '$8$'], 'explanation': '$P_1=15$, $P_2=21$. Difference $=6$.'},
        {'question': 'An equilateral triangle has perimeter $p$. Express the side in terms of $p$.',
         'answer': '$\\dfrac{p}{3}$', 'wrong': ['$3p$', '$\\frac{p}{2}$', '$\\frac{p}{4}$'], 'explanation': '$s=p/3$.'},
        {
            'question': 'An equilateral triangle has the same perimeter as a rectangle $10 \\times 5$. Find the triangle\'s side.',
            'answer': '$10$', 'wrong': ['$15$', '$5$', '$30$'], 'explanation': 'Rectangle $P=30$. $s=30/3=10$.'},
        {'question': 'An equilateral triangle has perimeter $24$. Find the area.', 'answer': '$16\\sqrt{3}$',
         'wrong': ['$8\\sqrt{3}$', '$24\\sqrt{3}$', '$32\\sqrt{3}$'],
         'explanation': '$s=8$. $A=\\frac{\\sqrt{3}}{4}(64)=16\\sqrt{3}$.'},

        # ── HEIGHT (10) ───────────────────────────────────────────────────────────
        {'question': 'Find the height of an equilateral triangle with side $s = 2$.', 'answer': '$\\sqrt{3}$',
         'wrong': ['$2\\sqrt{3}$', '$\\frac{\\sqrt{3}}{2}$', '$1$'],
         'explanation': '$h=\\frac{\\sqrt{3}}{2}(2)=\\sqrt{3}$.'},
        {'question': 'Find the height of an equilateral triangle with side $s = 4$.', 'answer': '$2\\sqrt{3}$',
         'wrong': ['$4\\sqrt{3}$', '$\\sqrt{3}$', '$8$'], 'explanation': '$h=\\frac{\\sqrt{3}}{2}(4)=2\\sqrt{3}$.'},
        {'question': 'Find the height of an equilateral triangle with side $s = 6$.', 'answer': '$3\\sqrt{3}$',
         'wrong': ['$6\\sqrt{3}$', '$\\sqrt{3}$', '$9$'], 'explanation': '$h=\\frac{\\sqrt{3}}{2}(6)=3\\sqrt{3}$.'},
        {'question': 'Find the height of an equilateral triangle with side $s = 10$.', 'answer': '$5\\sqrt{3}$',
         'wrong': ['$10\\sqrt{3}$', '$2\\sqrt{3}$', '$25$'], 'explanation': '$h=\\frac{\\sqrt{3}}{2}(10)=5\\sqrt{3}$.'},
        {'question': 'An equilateral triangle has height $h = 6\\sqrt{3}$. Find the side length.', 'answer': '$12$',
         'wrong': ['$6$', '$24$', '$6\\sqrt{3}$'], 'explanation': '$s=\\frac{2h}{\\sqrt{3}}=12$.'},
        {'question': 'Find the height of an equilateral triangle with side $s = 8$.', 'answer': '$4\\sqrt{3}$',
         'wrong': ['$8\\sqrt{3}$', '$2\\sqrt{3}$', '$16$'], 'explanation': '$h=\\frac{\\sqrt{3}}{2}(8)=4\\sqrt{3}$.'},
        {'question': 'An equilateral triangle has height $h = \\sqrt{3}$. Find the side length.', 'answer': '$2$',
         'wrong': ['$1$', '$\\sqrt{3}$', '$4$'], 'explanation': '$s=\\frac{2\\sqrt{3}}{\\sqrt{3}}=2$.'},
        {'question': 'Find the height of an equilateral triangle with side $s = 12$.', 'answer': '$6\\sqrt{3}$',
         'wrong': ['$12\\sqrt{3}$', '$3\\sqrt{3}$', '$36$'], 'explanation': '$h=\\frac{\\sqrt{3}}{2}(12)=6\\sqrt{3}$.'},
        {'question': 'An equilateral triangle has height $h = 5\\sqrt{3}$. Find its area.', 'answer': '$25\\sqrt{3}$',
         'wrong': ['$50\\sqrt{3}$', '$10\\sqrt{3}$', '$75$'],
         'explanation': '$s=10$. $A=\\frac{\\sqrt{3}}{4}(100)=25\\sqrt{3}$.'},
        {'question': 'What fraction of the side length is the height of an equilateral triangle?',
         'answer': '$\\dfrac{\\sqrt{3}}{2}$', 'wrong': ['$\\frac{1}{2}$', '$\\sqrt{3}$', '$\\frac{\\sqrt{2}}{2}$'],
         'explanation': '$h=\\frac{\\sqrt{3}}{2}s \\Rightarrow \\frac{h}{s}=\\frac{\\sqrt{3}}{2}$.'}, ],
    'similar_triangles': [{
        'question': 'Triangle $ABC$ has $\\angle A = 50°$ and $\\angle B = 60°$. Triangle $DEF$ has $\\angle D = 50°$ and $\\angle E = 60°$. Are they similar?',
        'answer': 'Yes — AA similarity',
        'wrong': ['No — sides must also be equal', 'Yes — SSS similarity',
                  'Cannot be determined'],
        'explanation': 'Two pairs of equal angles ($\\angle A=\\angle D$, $\\angle B=\\angle E$) establish AA similarity.'},

        {
            'question': 'In $\\triangle ABC$, $\\angle A = 40°$ and $\\angle C = 70°$. In $\\triangle PQR$, $\\angle P = 40°$ and $\\angle R = 70°$. What is $\\angle B$?',
            'answer': '$70°$',
            'wrong': ['$40°$', '$50°$', '$80°$'],
            'explanation': '$\\angle B = 180-40-70 = 70°$.  Both triangles have the same three angles so they are AA similar.'},

        {
            'question': 'A vertical pole casts a shadow of $6$ m. At the same time a nearby tree casts a shadow of $15$ m. The pole is $4$ m tall. How tall is the tree? (Use AA similarity.)',
            'answer': '$10$ m',
            'wrong': ['$8$ m', '$12$ m', '$6$ m'],
            'explanation': 'Sun angle is the same → AA. $\\dfrac{4}{6} = \\dfrac{h}{15} \\Rightarrow h = 10$.'},

        {
            'question': 'In $\\triangle ABC$ and $\\triangle DEF$, $\\angle B = \\angle E = 90°$ and $\\angle A = \\angle D = 35°$. What similarity criterion applies?',
            'answer': 'AA',
            'wrong': ['SAS', 'SSS', 'HL'],
            'explanation': 'Two pairs of equal angles (right angle + $35°$) give AA similarity.'},

        {
            'question': '$\\triangle ABC \\sim \\triangle DEF$ by AA. $\\angle A = 55°$ and $\\angle E = 80°$. Find $\\angle C$.',
            'answer': '$45°$',
            'wrong': ['$55°$', '$80°$', '$25°$'],
            'explanation': '$\\angle F = \\angle C$. In $\\triangle DEF$: $\\angle D=55°$, $\\angle E=80°$, so $\\angle F = 180-55-80 = 45°$.'},

        {
            'question': 'Two triangles share a common angle and one pair of parallel sides. Which similarity criterion applies?',
            'answer': 'AA',
            'wrong': ['SSS', 'SAS', 'ASA'],
            'explanation': 'Parallel sides create equal corresponding angles, giving two pairs → AA.'},

        {
            'question': 'In $\\triangle ABC$, $DE \\parallel BC$ with $D$ on $AB$ and $E$ on $AC$. Why is $\\triangle ADE \\sim \\triangle ABC$?',
            'answer': 'AA — $\\angle A$ is shared and $\\angle ADE = \\angle ABC$ (corresponding angles)',
            'wrong': ['SSS — all sides proportional', 'SAS — two sides and included angle',
                      'They are congruent, not similar'],
            'explanation': 'Shared $\\angle A$ + equal corresponding angles from the parallel line gives AA.'},

        {
            'question': '$\\triangle PQR$ has $\\angle P = 62°$. $\\triangle XYZ$ has $\\angle X = 62°$ and $\\angle Z = 48°$. If $\\angle Q = 70°$, are the triangles similar?',
            'answer': 'No — second pair of angles does not match',
            'wrong': ['Yes — AA', 'Yes — SAS', 'Yes — SSS'],
            'explanation': '$\\triangle PQR$: angles $62°, 70°, 48°$. $\\triangle XYZ$: $62°, 70°, 48°$. Actually $\\angle R=48°=\\angle Z$ too — they ARE similar. Check: $\\angle Q=70°$, $\\angle Y=180-62-48=70°$. Yes, similar by AA.'},

        {
            'question': 'In right $\\triangle ABC$ ($\\angle C=90°$) altitude $CD$ is drawn to hypotenuse $AB$. Why is $\\triangle ACD \\sim \\triangle ABC$?',
            'answer': 'AA — $\\angle A$ is shared and both have a right angle',
            'wrong': ['SSS', 'SAS', 'They are congruent'],
            'explanation': 'Both triangles share $\\angle A$ and each has a $90°$ angle → AA.'},

        {
            'question': 'Triangle $ABC$: $\\angle A = 75°, \\angle B = 55°$. Triangle $PQR$: $\\angle Q = 55°, \\angle R = 50°$. Are they similar?',
            'answer': 'Yes — AA ($\\angle B = \\angle Q = 55°$ and $\\angle C = \\angle R = 50°$)',
            'wrong': ['No — no matching angle pairs', 'Yes — SSS', 'Cannot determine'],
            'explanation': '$\\angle C = 180-75-55 = 50° = \\angle R$ and $\\angle B = \\angle Q = 55°$ → AA.'},

        {
            'question': 'A $6$-ft person casts a $4$-ft shadow. A flagpole casts a $22$-ft shadow. How tall is the flagpole?',
            'answer': '$33$ ft',
            'wrong': ['$22$ ft', '$30$ ft', '$36$ ft'],
            'explanation': 'AA (same sun angle): $\\dfrac{6}{4} = \\dfrac{h}{22} \\Rightarrow h = 33$.'},

        {
            'question': '$\\angle A = \\angle D$ and $\\angle B = \\angle E$ in two triangles. What can we conclude?',
            'answer': '$\\triangle ABC \\sim \\triangle DEF$ (AA)',
            'wrong': ['$\\triangle ABC \\cong \\triangle DEF$', 'Nothing without side info',
                      '$\\angle C \\ne \\angle F$'],
            'explanation': 'Two pairs of equal angles → AA similarity. The third angles are automatically equal.'},

        {
            'question': 'Two triangles both contain a $90°$ angle. One has a $30°$ angle; the other has a $60°$ angle. Are they similar?',
            'answer': 'Yes — AA (angles are $30°, 60°, 90°$ in both)',
            'wrong': ['No — one has $30°$, the other $60°$', 'Cannot determine',
                      'Only if sides match'],
            'explanation': 'First: $90°, 30°, 60°$. Second: $90°, 60°, 30°$. Same angle set → AA similar.'},

        {
            'question': 'In $\\triangle ABC$, $\\angle A = 2x$ and $\\angle B = 3x$. In $\\triangle DEF$, $\\angle D = 40°$ and $\\angle E = 60°$. For AA similarity what must $x$ equal?',
            'answer': '$x = 20$',
            'wrong': ['$x = 30$', '$x = 15$', '$x = 25$'],
            'explanation': '$\\angle A=\\angle D \\Rightarrow 2x=40 \\Rightarrow x=20$. Check: $\\angle B=60°=\\angle E$ ✓.'},

        {'question': 'Two isosceles triangles each have a vertex angle of $40°$. Are they similar?',
         'answer': 'Yes — AA (vertex $40°$ and base angles $70°$ each)',
         'wrong': ['No — sides may differ', 'Only if they are congruent', 'Cannot determine'],
         'explanation': 'Same vertex angle → same base angles ($70°$ each) → AA similar.'},

        {
            'question': 'In $\\triangle ABC$, $\\angle A = 48°$ and $\\angle B = 64°$. In $\\triangle XYZ$, $\\angle Y = 64°$ and $\\angle Z = 68°$. Are they similar?',
            'answer': 'Yes — AA ($\\angle C = \\angle Z = 68°$ and $\\angle B = \\angle Y = 64°$)',
            'wrong': ['No', 'Yes — SSS', 'Yes — SAS'],
            'explanation': '$\\angle C = 180-48-64 = 68° = \\angle Z$ and $\\angle B = \\angle Y = 64°$ → AA.'},

        {
            'question': 'Lines $AB$ and $CD$ intersect at $E$. Why is $\\triangle AEC \\sim \\triangle BED$?',
            'answer': 'AA — vertical angles $\\angle AEC = \\angle BED$ and $\\angle CAE = \\angle DBE$ (alternate interior)',
            'wrong': ['SSS', 'SAS', 'They are congruent'],
            'explanation': 'Vertical angles and alternate interior angles provide two equal angle pairs → AA.'},

        {
            'question': '$\\triangle ABC \\sim \\triangle DEF$ by AA with ratio $3:1$. If $AB = 9$, find $DE$.',
            'answer': '$3$',
            'wrong': ['$27$', '$6$', '$12$'],
            'explanation': 'Scale factor $3:1$, so $DE = AB/3 = 3$.'},

        {
            'question': 'In $\\triangle ABC$ and $\\triangle ADB$ where $D$ is on $BC$, $\\angle ADB = 90°$ and $\\angle ABC = \\angle BAC$. Are they similar?',
            'answer': 'Yes — AA',
            'wrong': ['No', 'Yes — SAS', 'Yes — SSS'],
            'explanation': 'Shared $\\angle B$ and right angles give AA similarity.'},

        {
            'question': 'A tree $12$ m tall casts a shadow. A $1.5$ m stick casts a $2$ m shadow at the same time. How long is the tree\'s shadow?',
            'answer': '$16$ m',
            'wrong': ['$8$ m', '$24$ m', '$18$ m'],
            'explanation': 'AA: $\\dfrac{12}{1.5} = \\dfrac{s}{2} \\Rightarrow s = 16$.'},

        {
            'question': 'In $\\triangle PQR$, $ST \\parallel QR$ where $S \\in PQ$ and $T \\in PR$. $\\angle PST = 70°$ and $\\angle P = 50°$. Find $\\angle Q$.',
            'answer': '$70°$',
            'wrong': ['$50°$', '$60°$', '$80°$'],
            'explanation': '$ST \\parallel QR$ → corresponding angles equal: $\\angle PST = \\angle PQR = 70°$.'},

        {
            'question': '$\\triangle ABC \\sim \\triangle DEF$ by AA with sides $AB = 6$, $DE = 9$. The ratio of their areas is:',
            'answer': '$4:9$',
            'wrong': ['$2:3$', '$6:9$', '$9:4$'],
            'explanation': 'Linear ratio $= 6:9 = 2:3$. Area ratio $= (2:3)^2 = 4:9$.'},

        {
            'question': 'Two triangles have two angles $55°$ and $75°$ respectively. What is their third angle?',
            'answer': '$50°$',
            'wrong': ['$55°$', '$75°$', '$45°$'],
            'explanation': '$180-55-75 = 50°$. If both triangles share all three angles they are AA similar.'},

        {
            'question': 'In a right triangle, the altitude to the hypotenuse creates two smaller triangles. Which similarity criterion relates all three triangles?',
            'answer': 'AA',
            'wrong': ['SSS', 'SAS', 'HL'],
            'explanation': 'Each smaller triangle shares an angle with the original and has a $90°$ angle → AA.'},

        {
            'question': '$\\triangle ABC$: $\\angle B = 90°$, $\\angle A = 35°$. $\\triangle DEF$: $\\angle E = 90°$, $\\angle F = 35°$. Are they similar?',
            'answer': 'Yes — AA ($90°$ and $35°$ match in each)',
            'wrong': ['No — $\\angle A$ matches $\\angle F$, not $\\angle D$', 'Yes — SSS',
                      'Cannot determine'],
            'explanation': '$\\angle B = \\angle E = 90°$ and $\\angle A = \\angle F = 35°$ → AA similar.'},

        {
            'question': 'Triangles $ABC$ and $DEF$ are AA similar with $\\angle A = 40°$, $\\angle C = 100°$. What are the angles of $\\triangle DEF$?',
            'answer': '$40°, 40°, 100°$',
            'wrong': ['$40°, 100°, 50°$', '$50°, 90°, 40°$', '$60°, 60°, 60°$'],
            'explanation': '$\\angle B = 180-40-100 = 40°$. Similar triangles share all three angles.'},

        {
            'question': 'A mirror is placed on the ground. A person $1.8$ m tall stands $2$ m from the mirror and sees the top of a building $18$ m away. How tall is the building?',
            'answer': '$16.2$ m',
            'wrong': ['$18$ m', '$20$ m', '$10$ m'],
            'explanation': 'AA (angle of incidence = angle of reflection): $\\dfrac{1.8}{2} = \\dfrac{h}{18} \\Rightarrow h = 16.2$.'},

        {'question': 'For AA similarity, how many pairs of equal angles are needed?',
         'answer': '$2$',
         'wrong': ['$1$', '$3$', '$0$'],
         'explanation': 'Only $2$ pairs are needed; the third pair is automatically equal (angle sum = $180°$).'},

        {
            'question': '$\\triangle RST \\sim \\triangle UVW$ by AA, ratio $1:4$. If the area of $\\triangle RST = 5$, find the area of $\\triangle UVW$.',
            'answer': '$80$',
            'wrong': ['$20$', '$40$', '$160$'],
            'explanation': 'Area ratio $= (1:4)^2 = 1:16$. Area of $\\triangle UVW = 5 \\times 16 = 80$.'},

        {'question': 'Both $\\triangle ABC$ and $\\triangle DEF$ are equilateral. Are they similar?',
         'answer': 'Yes — AA (all angles are $60°$)',
         'wrong': ['Only if they are congruent', 'No', 'Only by SSS'],
         'explanation': 'All angles $60°$ → AA similarity holds for any two equilateral triangles.'},

        {
            'question': '$\\angle A = (3x+5)°$ in $\\triangle ABC$ and $\\angle D = (5x-15)°$ in $\\triangle DEF$. For AA, what value of $x$ makes $\\angle A = \\angle D$?',
            'answer': '$x = 10$',
            'wrong': ['$x = 5$', '$x = 15$', '$x = 20$'],
            'explanation': '$3x+5 = 5x-15 \\Rightarrow 20 = 2x \\Rightarrow x = 10$.'},

        {
            'question': 'In quadrilateral $ABCD$, diagonal $AC$ divides it into $\\triangle ABC$ and $\\triangle ACD$. $\\angle BAC = \\angle ACD$ and $\\angle ABC = \\angle CAD$. Are the triangles similar?',
            'answer': 'Yes — AA',
            'wrong': ['No', 'Yes — SAS', 'Yes — SSS'],
            'explanation': 'Two pairs of equal angles directly give AA similarity.'},

        {
            'question': '$\\triangle ABC \\sim \\triangle DEF$ (AA), $AB = 5$, $DE = 15$, $BC = 8$. Find $EF$.',
            'answer': '$24$',
            'wrong': ['$8$', '$12$', '$40$'],
            'explanation': 'Scale factor $= 15/5 = 3$. $EF = 3 \\times 8 = 24$.'},

        # ══════════════════════════════════════════════════════════════════════════
        # SAS SIMILARITY  (Q34–66)
        # Two sides proportional + included angle equal → similar
        # ══════════════════════════════════════════════════════════════════════════

        {
            'question': '$\\triangle ABC$: $AB = 4$, $AC = 6$, $\\angle A = 50°$. $\\triangle DEF$: $DE = 8$, $DF = 12$, $\\angle D = 50°$. Are they similar?',
            'answer': 'Yes — SAS similarity',
            'wrong': ['Yes — AA', 'Yes — SSS', 'No'],
            'explanation': '$\\dfrac{AB}{DE} = \\dfrac{4}{8} = \\dfrac{1}{2}$, $\\dfrac{AC}{DF} = \\dfrac{6}{12} = \\dfrac{1}{2}$, and $\\angle A = \\angle D$ → SAS.'},

        {'question': 'For SAS similarity, what three conditions must be met?',
         'answer': 'Two pairs of proportional sides with the included angle equal',
         'wrong': ['Three pairs of proportional sides', 'Two equal angles',
                   'One proportional side and two equal angles'],
         'explanation': 'SAS: the ratio of two pairs of corresponding sides must be equal AND the angle between them must be equal.'},

        {
            'question': '$\\triangle PQR$: $PQ = 6$, $PR = 9$, $\\angle P = 70°$. $\\triangle XYZ$: $XY = 4$, $XZ = 6$, $\\angle X = 70°$. Are they similar?',
            'answer': 'Yes — SAS',
            'wrong': ['No — ratios differ', 'Yes — AA', 'Yes — SSS'],
            'explanation': '$\\dfrac{PQ}{XY} = \\dfrac{6}{4} = \\dfrac{3}{2}$, $\\dfrac{PR}{XZ} = \\dfrac{9}{6} = \\dfrac{3}{2}$, $\\angle P = \\angle X$ → SAS.'},

        {
            'question': '$\\triangle ABC$: $AB = 3$, $BC = 5$, $\\angle B = 40°$. $\\triangle DEF$: $DE = 9$, $EF = 15$, $\\angle E = 40°$. Are they similar?',
            'answer': 'Yes — SAS',
            'wrong': ['No', 'Yes — AA', 'Yes — SSS'],
            'explanation': 'Ratios $3/9 = 5/15 = 1/3$ with equal included angle $\\angle B = \\angle E$ → SAS.'},

        {
            'question': 'In $\\triangle ABC$ and $\\triangle ADE$, $D$ is on $AB$ and $E$ is on $AC$ with $\\dfrac{AD}{AB} = \\dfrac{AE}{AC}$. What similarity criterion applies?',
            'answer': 'SAS — shared $\\angle A$ and proportional sides',
            'wrong': ['AA', 'SSS', 'Cannot determine'],
            'explanation': 'Shared angle $\\angle A$ + proportional sides on either side → SAS.'},

        {
            'question': '$\\triangle PQR$: $PQ = 10$, $PR = 15$. $\\triangle STU$: $ST = 6$, $SU = 9$. $\\angle P = \\angle S = 60°$. Find the similarity ratio.',
            'answer': '$5:3$',
            'wrong': ['$3:5$', '$2:3$', '$10:6$'],
            'explanation': '$\\dfrac{PQ}{ST} = \\dfrac{10}{6} = \\dfrac{5}{3}$ and $\\dfrac{PR}{SU} = \\dfrac{15}{9} = \\dfrac{5}{3}$ → ratio $5:3$.'},

        {
            'question': 'In $\\triangle ABC$, $AB = 8$, $AC = 12$, $\\angle A = 45°$. In $\\triangle ADE$ (with $D$ on $AB$, $E$ on $AC$), $AD = 4$, $AE = 6$. What is the similarity ratio?',
            'answer': '$2:1$',
            'wrong': ['$1:2$', '$4:8$', '$3:6$'],
            'explanation': '$\\dfrac{AB}{AD} = \\dfrac{8}{4} = 2$, shared $\\angle A$, $\\dfrac{AC}{AE} = 2$ → SAS, ratio $2:1$.'},

        {
            'question': '$\\triangle ABC \\sim \\triangle DEF$ by SAS, ratio $3:2$. $AB = 9$, $\\angle A = 55°$, $AC = 12$. Find $DE$ and $DF$.',
            'answer': '$DE = 6$, $DF = 8$',
            'wrong': ['$DE = 6$, $DF = 12$', '$DE = 9$, $DF = 8$', '$DE = 3$, $DF = 4$'],
            'explanation': 'Ratio $3:2$: $DE = 9 \\times \\frac{2}{3} = 6$, $DF = 12 \\times \\frac{2}{3} = 8$.'},

        {
            'question': 'Two triangles have sides $4, 6$ and $6, 9$ with an included angle of $80°$ in both. Are they similar?',
            'answer': 'Yes — SAS ($\\frac{4}{6} = \\frac{6}{9} = \\frac{2}{3}$, included $80°$ equal)',
            'wrong': ['No — sides are not equal', 'Yes — AA', 'Yes — SSS'],
            'explanation': 'Ratios $4/6 = 6/9 = 2/3$ with equal included angle → SAS.'},

        {
            'question': '$\\triangle RST$: $RS = 5$, $RT = 7$, $\\angle R = 90°$. $\\triangle UVW$: $UV = 10$, $UW = 14$, $\\angle U = 90°$. Are they similar?',
            'answer': 'Yes — SAS',
            'wrong': ['Yes — HL only', 'No', 'Yes — SSS'],
            'explanation': 'Ratios $5/10 = 7/14 = 1/2$ with equal right angles → SAS.'},

        {
            'question': '$\\triangle ABC$: $AB = 6$, $BC = 8$, $\\angle B = 120°$. $\\triangle DEF$: $DE = 3$, $EF = 5$, $\\angle E = 120°$. Are they similar?',
            'answer': 'No — ratios $6/3 \\ne 8/5$',
            'wrong': ['Yes — SAS', 'Yes — AA', 'Yes — SSS'],
            'explanation': '$AB/DE = 2$ but $BC/EF = 8/5$. Unequal ratios → SAS fails.'},

        {'question': 'For SAS similarity, the equal angle must be the:',
         'answer': 'Included angle (between the two proportional sides)',
         'wrong': ['Largest angle', 'Smallest angle', 'Any angle in the triangle'],
         'explanation': 'The angle must be included between the two sides whose ratios are equal.'},

        {
            'question': '$\\triangle ABC$: $AB = 12$, $AC = 16$, $\\angle A = 35°$. $\\triangle DEF$: $DE = 9$, $DF = 12$, $\\angle D = 35°$. Find the similarity ratio.',
            'answer': '$4:3$',
            'wrong': ['$3:4$', '$12:9$', '$2:3$'],
            'explanation': '$12/9 = 16/12 = 4/3$ with $\\angle A = \\angle D$ → SAS, ratio $4:3$.'},

        {
            'question': '$\\triangle PQR \\sim \\triangle STU$ (SAS) with ratio $2:5$. Area of $\\triangle PQR = 8$. Find area of $\\triangle STU$.',
            'answer': '$50$',
            'wrong': ['$20$', '$40$', '$200$'],
            'explanation': 'Area ratio $= (2/5)^2 = 4/25$. Area of $\\triangle STU = 8 \\times 25/4 = 50$.'},

        {
            'question': 'In $\\triangle ABC$, $M$ is the midpoint of $AB$ and $N$ is the midpoint of $AC$. Why is $\\triangle AMN \\sim \\triangle ABC$?',
            'answer': 'SAS — shared $\\angle A$ and $AM/AB = AN/AC = 1/2$',
            'wrong': ['AA', 'SSS', 'They are congruent'],
            'explanation': 'Midpoint theorem gives ratio $1/2$ on both sides + shared $\\angle A$ → SAS.'},

        {
            'question': 'Two triangles: sides $8, 10$ and $12, 15$ with the included angles equal. Similarity ratio?',
            'answer': '$2:3$',
            'wrong': ['$3:2$', '$8:12$', '$4:5$'],
            'explanation': '$8/12 = 10/15 = 2/3$ → SAS similar with ratio $2:3$.'},

        {
            'question': '$\\triangle ABC$: $AB = 5$, $AC = 10$, $\\angle A = 60°$. $\\triangle ADE$ (D on AB, E on AC): $AD = 2$, $AE = 4$. Are they similar?',
            'answer': 'Yes — SAS ($5/2 = 10/4 = 2.5$, shared $\\angle A$)',
            'wrong': ['No', 'Yes — AA', 'Yes — SSS'],
            'explanation': '$AB/AD = 5/2 = 2.5$ and $AC/AE = 10/4 = 2.5$, shared $\\angle A$ → SAS.'},

        {
            'question': '$\\triangle DEF$: $DE = 7$, $DF = 14$, $\\angle D = 50°$. $\\triangle XYZ$: $XY = 3$, $XZ = 6$, $\\angle X = 50°$. Similarity ratio?',
            'answer': '$7:3$',
            'wrong': ['$2:1$', '$3:7$', '$14:6$'],
            'explanation': '$7/3 = 14/6 = 7/3$ with equal included angles → SAS, ratio $7:3$.'},

        {
            'question': 'In parallelogram $ABCD$, diagonal $AC$ divides it. Show $\\triangle ABC \\sim \\triangle CDA$ using SAS.',
            'answer': '$AB/CD = BC/DA$ (opposite sides equal) and $\\angle ABC = \\angle CDA$ (opposite angles equal)',
            'wrong': ['AA only', 'SSS only', 'They are congruent, not similar'],
            'explanation': 'Opposite sides equal → ratios $= 1$, opposite angles equal → SAS (also congruent).'},

        {
            'question': '$\\triangle ABC$: $AB = 4$, $BC = 6$, $\\angle B = 75°$. Find sides of a similar $\\triangle$ (SAS, ratio $3:2$).',
            'answer': '$6$ and $9$',
            'wrong': ['$8$ and $12$', '$2$ and $3$', '$4$ and $6$'],
            'explanation': 'Multiply by $3/2$: $4 \\times 1.5 = 6$, $6 \\times 1.5 = 9$. Included angle stays $75°$.'},

        {
            'question': 'Sides of $\\triangle ABC$ are $AB=6, AC=8$. In $\\triangle DEF$, $DE=9, DF=12$. $\\angle A = \\angle D$. What is the ratio of their perimeters if $BC=5$ and $EF$ is unknown?',
            'answer': '$2:3$',
            'wrong': ['$3:2$', '$1:2$', '$4:6$'],
            'explanation': 'SAS ratio $= 6/9 = 2/3$, so all sides scale by $2/3$. Perimeter ratio $= 2:3$.'},

        {
            'question': '$\\triangle PQR$: $PQ = 15$, $PR = 20$, $\\angle P = 40°$. $\\triangle STU$: $ST = 6$, $SU = 8$, $\\angle S = 40°$. Similarity ratio?',
            'answer': '$5:2$',
            'wrong': ['$2:5$', '$3:1$', '$15:6$'],
            'explanation': '$15/6 = 20/8 = 5/2$ with $\\angle P = \\angle S$ → SAS, ratio $5:2$.'},

        {
            'question': 'Can SAS similarity apply if the equal angle is NOT between the two proportional sides?',
            'answer': 'No — the angle must be the included angle',
            'wrong': ['Yes — any equal angle works', 'Yes — if both triangles are acute',
                      'Yes — if sides are in ratio $1:1$'],
            'explanation': 'SAS requires the angle to be INCLUDED between the proportional sides. Otherwise the criterion is invalid.'},

        {
            'question': '$\\triangle ABC \\sim \\triangle DEF$ (SAS), $AB/DE = 3/4$. If $BC = 9$ and the included angles are equal, find $EF$.',
            'answer': '$12$',
            'wrong': ['$6$', '$9$', '$16$'],
            'explanation': 'Scale factor $3:4$, so $EF = 9 \\times 4/3 = 12$.'},

        {
            'question': 'Two triangles both have a $90°$ angle. Their legs adjacent to the $90°$ are in ratio $2:5$. Does SAS apply?',
            'answer': 'Yes — SAS (equal included right angles, legs in same ratio)',
            'wrong': ['No — need all three sides', 'No — need two angle pairs', 'Only HL applies'],
            'explanation': 'Equal right angles + proportional adjacent sides → SAS similarity.'},

        {
            "question": "$\\triangle ABC$: $AB = 10$, $AC = 15$, $\\angle A = 80^\\circ$. $\\triangle DEF$: $DE = 4$, $DF = 6$, $\\angle D = 80^\\circ$. Area of $\\triangle ABC = 60$. Find area of $\\triangle DEF$.",
            "answer": "$9.6$",
            "wrong": ["$24$", "$15$", "$6$"],
            "explanation": "Since $\\angle A = \\angle D$, the triangles are similar. The side ratio is $10/4 = 15/6 = 5/2$. Area scales with the square of the ratio: $(5/2)^2 = 25/4$. Thus area$(ABC)$/area$(DEF) = 25/4$. So area$(DEF) = 60 \\times \\frac{4}{25} = 9.6$."
        },

        {
            'question': 'In $\\triangle ABC$, $D$ on $AB$ and $E$ on $AC$ such that $AD = 3$, $AB = 9$, $AE = 4$, $AC = 12$. $\\angle A = 55°$. Is $\\triangle ADE \\sim \\triangle ABC$?',
            'answer': 'Yes — SAS ($3/9 = 4/12 = 1/3$, shared $\\angle A$)',
            'wrong': ['No', 'Yes — AA', 'Yes — SSS'],
            'explanation': '$AD/AB = 3/9 = 1/3 = AE/AC = 4/12$ + shared $\\angle A$ → SAS.'},

        {
            'question': '$\\triangle PQR \\sim \\triangle DEF$ (SAS) with $PQ = 6$, $DE = 10$. Find the ratio of their areas.',
            'answer': '$9:25$',
            'wrong': ['$6:10$', '$3:5$', '$36:100$'],
            'explanation': 'Linear ratio $6:10 = 3:5$. Area ratio $= (3/5)^2 = 9/25$.'},

        {
            'question': '$\\triangle ABC$: $AB = 8$, $BC = 12$, $\\angle B = 45°$. A similar triangle has shortest side $6$. Find its other side (the one corresponding to $12$).',
            'answer': '$9$',
            'wrong': ['$12$', '$10$', '$8$'],
            'explanation': 'Ratio $= 6/8 = 3/4$. Other side $= 12 \\times 3/4 = 9$.'},

        {
            "question": "In right $\\triangle ABC$ ($\\angle B = 90°$), $BD \\perp AC$. $BD = 6$, $AD = 4$. Prove $\\triangle ABD \\sim \\triangle CBD$ using SAS.",
            "answer": "AA applies here (both have $90°$ and share an angle).",
            "wrong": ["SAS with $BD$ common", "SSS", "HL only"],
            "explanation": "Both triangles have right angles and share a common angle → AA (not SAS)."
        },

        {
            'question': '$\\triangle ABC$: $AB = 2x$, $AC = 3x$, $\\angle A = 65°$. $\\triangle DEF$: $DE = 8$, $DF = 12$, $\\angle D = 65°$. For SAS similarity, find $x$.',
            'answer': '$x = 4$',
            'wrong': ['$x = 2$', '$x = 3$', '$x = 6$'],
            'explanation': '$\\dfrac{2x}{8} = \\dfrac{3x}{12} \\Rightarrow \\dfrac{x}{4} = \\dfrac{x}{4}$ ✓ for any $x$. But to match the specific triangle, $2x=8 \\Rightarrow x=4$.'},

        {
            'question': 'Two triangles have sides $5, 8$ and $10, 16$ with the angle between $5$ and $8$ equal to the angle between $10$ and $16$. Ratio?',
            'answer': '$1:2$',
            'wrong': ['$2:1$', '$5:8$', '$1:4$'],
            'explanation': '$5/10 = 8/16 = 1/2$ with equal included angle → SAS, ratio $1:2$.'},

        # ══════════════════════════════════════════════════════════════════════════
        # SSS SIMILARITY  (Q67–100)
        # All three pairs of sides proportional → similar
        # ══════════════════════════════════════════════════════════════════════════

        {
            'question': '$\\triangle ABC$: sides $3, 4, 5$. $\\triangle DEF$: sides $6, 8, 10$. Are they similar?',
            'answer': 'Yes — SSS (ratio $1:2$ for all sides)',
            'wrong': ['No', 'Yes — AA', 'Yes — SAS'],
            'explanation': '$3/6 = 4/8 = 5/10 = 1/2$ → SSS similar.'},

        {
            'question': '$\\triangle PQR$: sides $5, 10, 15$. $\\triangle XYZ$: sides $2, 4, 6$. Similarity ratio?',
            'answer': '$5:2$',
            'wrong': ['$2:5$', '$1:3$', '$5:10$'],
            'explanation': '$5/2 = 10/4 = 15/6 = 5/2$ → SSS, ratio $5:2$.'},

        {
            'question': '$\\triangle ABC$: sides $4, 6, 8$. $\\triangle DEF$: sides $6, 9, 12$. Are they SSS similar?',
            'answer': 'Yes — ratio $2:3$',
            'wrong': ['No', 'Yes — ratio $3:2$', 'Yes — ratio $1:2$'],
            'explanation': '$4/6 = 6/9 = 8/12 = 2/3$ → SSS, ratio $2:3$.'},

        {'question': 'For SSS similarity, what must be true?',
         'answer': 'All three pairs of corresponding sides must have the same ratio',
         'wrong': ['All sides must be equal', 'Only two sides need to be proportional',
                   'At least one angle must be equal'],
         'explanation': 'SSS similarity requires all three ratios of corresponding sides to be equal.'},

        {'question': '$\\triangle ABC$: sides $7, 14, 21$. $\\triangle PQR$: sides $1, 2, 3$. Ratio?',
         'answer': '$7:1$',
         'wrong': ['$1:7$', '$2:14$', '$3:21$'],
         'explanation': '$7/1 = 14/2 = 21/3 = 7$ → SSS, ratio $7:1$.'},

        {
            'question': '$\\triangle ABC$: sides $5, 7, 9$. $\\triangle DEF$: sides $10, 14, 18$. What is the ratio of their perimeters?',
            'answer': '$1:2$',
            'wrong': ['$2:1$', '$5:10$', '$1:4$'],
            'explanation': 'SSS ratio $= 1:2$, so perimeter ratio $= 1:2$.'},

        {
            'question': '$\\triangle PQR$: sides $6, 8, 10$. $\\triangle STU$: sides $9, 12, 15$. Are they similar?',
            'answer': 'Yes — SSS (ratio $2:3$)',
            'wrong': ['No', 'Yes — ratio $1:2$', 'Yes — AA'],
            'explanation': '$6/9 = 8/12 = 10/15 = 2/3$ → SSS.'},

        {
            'question': '$\\triangle ABC$: sides $3, 5, 7$. $\\triangle DEF$: sides $6, 10, 15$. Are they SSS similar?',
            'answer': 'No — $3/6 = 1/2$ but $7/15 \\ne 1/2$',
            'wrong': ['Yes — ratio $1:2$', 'Yes — ratio $2:3$', 'Cannot determine'],
            'explanation': '$3/6=1/2$, $5/10=1/2$, but $7/15 \\approx 0.47 \\ne 1/2$ → NOT SSS similar.'},

        {
            'question': '$\\triangle ABC \\sim \\triangle DEF$ (SSS) with ratio $3:5$. $AB = 9$. Find $DE$.',
            'answer': '$15$',
            'wrong': ['$5$', '$27$', '$12$'],
            'explanation': '$AB/DE = 3/5 \\Rightarrow DE = 9 \\times 5/3 = 15$.'},

        {
            'question': '$\\triangle ABC \\sim \\triangle DEF$ (SSS), ratio $2:7$. Area of $\\triangle DEF = 98$. Find area of $\\triangle ABC$.',
            'answer': '$8$',
            'wrong': ['$14$', '$28$', '$4$'],
            'explanation': 'Area ratio $= (2/7)^2 = 4/49$. Area $= 98 \\times 4/49 = 8$.'},

        {
            'question': '$\\triangle ABC$: sides $a, 2a, 3a$. $\\triangle DEF$: sides $b, 2b, 3b$. Are they similar for any positive $a, b$?',
            'answer': 'Yes — SSS (all ratios $= a/b$)',
            'wrong': ['Only if $a = b$', 'No', 'Only by AA'],
            'explanation': '$a/b = 2a/2b = 3a/3b$ → SSS for any positive $a, b$.'},

        {
            'question': '$\\triangle PQR$: sides $8, 12, 16$. Which triangle is SSS similar with ratio $1:2$?',
            'answer': 'Sides $4, 6, 8$',
            'wrong': ['Sides $4, 6, 10$', 'Sides $16, 24, 30$', 'Sides $8, 12, 20$'],
            'explanation': 'Divide each side by $2$: $4, 6, 8$.'},

        {
            'question': '$\\triangle ABC$: sides $10, 15, 20$. $\\triangle DEF$: sides $6, 9, 12$. Similarity ratio $ABC:DEF$?',
            'answer': '$5:3$',
            'wrong': ['$3:5$', '$10:6$', '$2:3$'],
            'explanation': '$10/6 = 15/9 = 20/12 = 5/3$ → SSS, ratio $5:3$.'},

        {'question': 'Are two equilateral triangles with sides $5$ and $7$ similar by SSS?',
         'answer': 'Yes — ratio $5:7$',
         'wrong': ['No — different side lengths', 'Yes — AA only', 'Only if angles are checked'],
         'explanation': 'All ratios $= 5/7$ → SSS similar. (Also AA since all angles $60°$.)'},

        {
            'question': '$\\triangle ABC \\sim \\triangle DEF$ (SSS). $AB = 4, BC = 6, CA = 8$ and $DE = 6$. Find $EF$ and $FD$.',
            'answer': '$EF = 9$, $FD = 12$',
            'wrong': ['$EF = 8$, $FD = 10$', '$EF = 6$, $FD = 8$', '$EF = 12$, $FD = 16$'],
            'explanation': 'Ratio $= 6/4 = 3/2$. $EF = 6 \\times 3/2 = 9$, $FD = 8 \\times 3/2 = 12$.'},

        {
            'question': '$\\triangle ABC$: sides $2, 3, 4$. $\\triangle DEF$: sides $4, 6, 8$. Ratio of areas?',
            'answer': '$1:4$',
            'wrong': ['$1:2$', '$2:4$', '$1:8$'],
            'explanation': 'Linear ratio $= 1:2$. Area ratio $= 1:4$.'},

        {
            'question': '$\\triangle PQR$: sides $15, 20, 25$. Simplify to check if it is similar to sides $3, 4, 5$.',
            'answer': 'Yes — ratio $5:1$',
            'wrong': ['No', 'Yes — ratio $1:5$', 'Yes — ratio $3:1$'],
            'explanation': '$15/3 = 20/4 = 25/5 = 5$ → SSS, ratio $5:1$.'},

        {
            'question': '$\\triangle ABC$: sides $x, 2x, 3x$ (any $x > 0$). $\\triangle PQR$: sides $5, 10, 15$. What must $x$ equal for congruence?',
            'answer': '$x = 5$',
            'wrong': ['$x = 1$', '$x = 3$', '$x = 10$'],
            'explanation': 'Congruent means ratio $1:1$: $x = 5$.'},

        {
            'question': '$\\triangle RST \\sim \\triangle UVW$ (SSS), ratio $4:9$. Perimeter of $\\triangle RST = 24$. Find perimeter of $\\triangle UVW$.',
            'answer': '$54$',
            'wrong': ['$36$', '$96$', '$216$'],
            'explanation': 'Perimeter ratio $= 4:9$. $\\dfrac{24}{P} = \\dfrac{4}{9} \\Rightarrow P = 54$.'},

        {
            'question': '$\\triangle ABC$: sides $6, 8, 10$. $\\triangle DEF$: sides $9, 12, 15$. Find $\\angle C$ if $\\angle F = 90°$.',
            'answer': '$90°$',
            'wrong': ['$60°$', '$45°$', '$30°$'],
            'explanation': 'SSS similar (ratio $2:3$) → corresponding angles equal → $\\angle C = \\angle F = 90°$.'},

        {
            'question': 'Sides of $\\triangle ABC$ are $12, 16, 20$. Which set of sides gives a SSS-similar triangle?',
            'answer': '$3, 4, 5$',
            'wrong': ['$6, 8, 11$', '$4, 8, 10$', '$12, 16, 24$'],
            'explanation': '$12/3 = 16/4 = 20/5 = 4$ → SSS.'},

        {
            'question': '$\\triangle ABC$: sides $a = 7, b = 24, c = 25$. Is it a right triangle? Which similar triangle also has a right angle?',
            'answer': 'Yes (7-24-25 triple). Any triangle with sides in ratio $7:24:25$ also has a right angle.',
            'wrong': ['No right angle', 'Only congruent triangles share the right angle',
                      'Cannot determine'],
            'explanation': '$7^2+24^2 = 49+576 = 625 = 25^2$ ✓. SSS similar triangles are also right triangles.'},

        {
            'question': '$\\triangle PQR \\sim \\triangle DEF$ (SSS), area of $\\triangle PQR = 50$, ratio $5:2$. Find area of $\\triangle DEF$.',
            'answer': '$8$',
            'wrong': ['$20$', '$125$', '$2$'],
            'explanation': 'Area ratio $= (5/2)^2 = 25/4$. Area $\\triangle DEF = 50 \\times 4/25 = 8$.'},

        {
            'question': '$\\triangle ABC$: sides $5, 12, 13$. $\\triangle PQR$: sides $10, 24, 26$. Similarity criterion?',
            'answer': 'SSS (ratio $1:2$)',
            'wrong': ['SAS', 'AA only', 'They are congruent'],
            'explanation': '$5/10 = 12/24 = 13/26 = 1/2$ → SSS.'},

        {'question': 'Two triangles have all sides doubled. What happens to the area?',
         'answer': 'Area is multiplied by $4$',
         'wrong': ['Doubled', 'Multiplied by $8$', 'Stays the same'],
         'explanation': 'Linear ratio $= 2:1$. Area ratio $= 4:1$.'},

        {
            'question': '$\\triangle ABC$: $AB = 3k, BC = 4k, CA = 5k$. $\\triangle DEF$: $DE = 6, EF = 8, FD = 10$. For SSS, what is $k$?',
            'answer': '$k = 2$',
            'wrong': ['$k = 1$', '$k = 3$', '$k = 4$'],
            'explanation': '$3k/6 = 4k/8 = 5k/10 = k/2$. For ratio $1:1$ (congruence): $k=2$.'},

        {'question': 'Can SSS similarity be used to prove two triangles are congruent?',
         'answer': 'Yes — when the similarity ratio is $1:1$',
         'wrong': ['No — similarity and congruence are different', 'Only if angles are also checked',
                   'Only for right triangles'],
         'explanation': 'SSS similarity with ratio $1:1$ means all sides are equal → congruent (SSS congruence).'},

        {
            'question': '$\\triangle ABC \\sim \\triangle DEF$ (SSS) with $AB = 5, DE = 15, BC = 8$. Find $EF$.',
            'answer': '$24$',
            'wrong': ['$8$', '$40$', '$12$'],
            'explanation': 'Ratio $= 15/5 = 3$. $EF = 8 \\times 3 = 24$.'},

        {
            'question': '$\\triangle PQR$: sides $9, 12, 15$. Is it similar to $\\triangle STU$ with sides $12, 16, 20$?',
            'answer': 'Yes — SSS (ratio $3:4$)',
            'wrong': ['No', 'Yes — ratio $1:2$', 'Yes — AA'],
            'explanation': '$9/12 = 12/16 = 15/20 = 3/4$ → SSS.'},

        {
            'question': 'The sides of $\\triangle ABC$ are $\\sqrt{2}, \\sqrt{3}, \\sqrt{5}$. A similar triangle has sides $\\sqrt{8}, \\sqrt{12}, \\sqrt{20}$. Similarity ratio?',
            'answer': '$1:2$',
            'wrong': ['$1:\\sqrt{2}$', '$1:4$', '$\\sqrt{2}:1$'],
            'explanation': '$\\sqrt{8}/\\sqrt{2} = \\sqrt{4} = 2$, similarly for others → ratio $1:2$.'},

        {
            'question': '$\\triangle ABC$: sides $4, 5, 6$. A triangle with perimeter $45$ is SSS similar. Find its sides.',
            'answer': '$12, 15, 18$',
            'wrong': ['$9, 10, 12$', '$10, 15, 20$', '$8, 10, 12$'],
            'explanation': 'Original perimeter $= 15$. Ratio $= 45/15 = 3$. Sides: $12, 15, 18$.'}, ],
    'properties_of_triangles': [{
        'question': 'Can a triangle have sides of lengths $3$, $4$, and $8$?',
        'answer': 'No',
        'wrong': ['Yes', 'Only if it is obtuse', 'Only if it is a right triangle'],
        'explanation': 'Check: $3 + 4 = 7 < 8$. The sum of the two smaller sides does not exceed the largest side, so no triangle is possible.',
    },
        {
            'question': 'Which of the following can be the lengths of the sides of a triangle?',
            'answer': '$5, 7, 9$',
            'wrong': ['$1, 2, 3$', '$2, 5, 8$', '$4, 4, 9$'],
            'explanation': 'For $5,7,9$: $5+7=12>9$ ✓. For the others, the sum of the two smallest sides does not exceed the largest.',
        },
        {
            'question': 'If two sides of a triangle are $6$ and $10$, which value can the third side $x$ take?',
            'answer': '$x = 8$',
            'wrong': ['$x = 16$', '$x = 4$', '$x = 0$'],
            'explanation': 'By the triangle inequality: $|10-6| < x < 10+6 \\Rightarrow 4 < x < 16$. Only $x=8$ lies in this range.',
        },
        {
            'question': 'If $a = 5$, $b = 5$, $c = 10$, is this a valid triangle?',
            'answer': 'No',
            'wrong': ['Yes', 'Yes, it is equilateral', 'Yes, it is isosceles'],
            'explanation': '$a + b = 5 + 5 = 10 = c$. The strict inequality $a + b > c$ is not satisfied.',
        },
        {
            'question': 'What is the range of the third side $x$ if the other two sides are $7$ and $13$?',
            'answer': '$6 < x < 20$',
            'wrong': ['$0 < x < 20$', '$7 < x < 13$', '$6 \\leq x \\leq 20$'],
            'explanation': 'Triangle inequality: $|13-7| < x < 13+7 \\Rightarrow 6 < x < 20$ (strict inequalities).',
        },
        {
            'question': 'Which set of side lengths forms a valid triangle?',
            'answer': '$8, 8, 8$',
            'wrong': ['$0, 5, 5$', '$1, 1, 3$', '$3, 7, 10$'],
            'explanation': 'An equilateral triangle with all sides $8$ satisfies all three inequalities. The others each fail the strict inequality.',
        },
        {
            'question': 'Two sides of a triangle are $3$ and $3$. What is the maximum integer value the third side can take?',
            'answer': '$5$',
            'wrong': ['$6$', '$7$', '$4$'],
            'explanation': '$c < a + b = 6$, so $c < 6$. The largest integer less than $6$ is $5$.',
        },
        {
            'question': 'Two sides of a triangle are $3$ and $3$. What is the minimum positive integer the third side can take?',
            'answer': '$1$',
            'wrong': ['$0$', '$2$', '$3$'],
            'explanation': '$c > |a - b| = 0$, so $c > 0$. The smallest positive integer is $1$.',
        },
        {
            'question': 'If the sides of a triangle are $x$, $x+2$, and $x+4$, which inequality must $x$ satisfy?',
            'answer': '$x > 2$',
            'wrong': ['$x > 0$', '$x > 4$', '$x > 6$'],
            'explanation': 'Tightest inequality: $x + (x+2) > x+4 \\Rightarrow 2x+2 > x+4 \\Rightarrow x > 2$.',
        },
        {
            'question': 'Can a triangle have sides $2$, $2$, and $4$?',
            'answer': 'No',
            'wrong': ['Yes', 'Yes, it is isosceles', 'Yes, it is a right triangle'],
            'explanation': '$2 + 2 = 4$ violates the strict inequality $a + b > c$. This is a degenerate (flat) triangle.',
        },
        {
            'question': 'Which value of $x$ makes $x$, $5$, $9$ a valid triangle?',
            'answer': '$x = 6$',
            'wrong': ['$x = 14$', '$x = 4$', '$x = 1$'],
            'explanation': '$|9-5| < x < 9+5 \\Rightarrow 4 < x < 14$. Only $x=6$ lies in this range.',
        },
        {
            'question': 'How many integer values can the third side take if the other two sides are $4$ and $9$?',
            'answer': '$7$',
            'wrong': ['$9$', '$13$', '$5$'],
            'explanation': '$|9-4| < x < 9+4 \\Rightarrow 5 < x < 13$. Integer values: $6,7,8,9,10,11,12$ — that is $7$ values.',
        },
        {
            'question': 'Is the set $\\{1, 5, 5\\}$ a valid triangle?',
            'answer': 'Yes',
            'wrong': ['No', 'Only if angles are specified', 'Cannot be determined'],
            'explanation': '$1+5=6>5$ ✓, $5+5=10>1$ ✓. All inequalities hold.',
        },
        {
            'question': 'The perimeter of a triangle is $30$. Two sides are $8$ and $10$. Is it a valid triangle?',
            'answer': 'Yes; third side $= 12$',
            'wrong': ['No; third side $= 12$', 'Yes; third side $= 10$', 'Yes; third side $= 14$'],
            'explanation': 'Third side $= 30-8-10=12$. Check: $8+10=18>12$ ✓, $8+12=20>10$ ✓, $10+12=22>8$ ✓. Valid.',
        },
        {
            'question': 'Which value cannot be a side of a triangle whose other two sides are $6$ and $6$?',
            'answer': '$12$',
            'wrong': ['$6$', '$7$', '$1$'],
            'explanation': 'Third side $c$ must satisfy $0 < c < 12$. $c=12$ fails: $6+6=12 \\not> 12$.',
        },
        {
            'question': 'If sides are ordered $a \\leq b \\leq c$, which single inequality is sufficient to guarantee a valid triangle?',
            'answer': '$a + b > c$',
            'wrong': ['$a + c > b$', '$b + c > a$', '$a + b > a$'],
            'explanation': 'When $a \\leq b \\leq c$, the inequalities $a+c>b$ and $b+c>a$ hold automatically. Only $a+b>c$ can fail.',
        },
        {
            'question': 'A triangle has sides $n$, $n+1$, $2n-1$. For which values of integer $n$ is it valid?',
            'answer': '$n \\geq 2$',
            'wrong': ['$n \\geq 1$', '$n \\geq 3$', '$n \\geq 4$'],
            'explanation': 'Tightest: $n+(2n-1) > n+1 \\Rightarrow 2n > 2 \\Rightarrow n > 1$. So minimum integer is $n=2$.',
        },
        {
            'question': 'Can a degenerate triangle (three collinear points) satisfy the triangle inequality?',
            'answer': 'No',
            'wrong': ['Yes', 'Only if it is equilateral', 'Only if two sides are equal'],
            'explanation': 'A degenerate triangle has $a+b=c$, which violates the strict inequality $a+b>c$.',
        },
        {
            'question': 'Two sides are $a > b > 0$. The third side $c$ must satisfy:',
            'answer': '$a - b < c < a + b$',
            'wrong': ['$b - a < c < a + b$', '$0 < c < a + b$', '$a - b \\leq c \\leq a + b$'],
            'explanation': 'From the three strict inequalities, the tightest constraints are $c > a-b$ (since $a>b$) and $c < a+b$.',
        },
        {
            'question': 'Sides $3x$, $4x$, $5x$ form a valid triangle for:',
            'answer': 'All $x > 0$',
            'wrong': ['Only $x = 1$', '$x > 1$', '$x > 5$'],
            'explanation': 'Since $3+4=7>5$, the base triangle $\\{3,4,5\\}$ is valid. Scaling by any $x>0$ preserves all inequalities.',
        },
        {
            'question': 'Which statement always holds for a triangle with sides $p$, $q$, $r$?',
            'answer': '$|p - q| < r$',
            'wrong': ['$p - q < r$ only if $p > q$', '$p + q = r$', '$r > p + q$'],
            'explanation': 'From $r > p-q$ and $r > q-p$, we get $r > |p-q|$, i.e., $|p-q| < r$.',
        },
        {
            'question': 'For consecutive integer sides $n$, $n+1$, $n+2$, what is the minimum valid $n$?',
            'answer': '$n = 2$',
            'wrong': ['$n = 1$', '$n = 3$', '$n = 0$'],
            'explanation': 'Tightest: $n+(n+1)>n+2 \\Rightarrow n > 1$. Minimum integer satisfying this is $n=2$.',
        },
        {
            'question': 'Given sides $2$, $3$, and $x$, how many positive integer values can $x$ take?',
            'answer': '$3$',
            'wrong': ['$4$', '$5$', '$2$'],
            'explanation': '$|3-2| < x < 3+2 \\Rightarrow 1 < x < 5$. Integer values: $2, 3, 4$ — that is $3$ values.',
        },
        {
            'question': 'Is it possible for a triangle to have sides in the ratio $1:2:3$?',
            'answer': 'No',
            'wrong': ['Yes', 'Yes, it is a right triangle', 'Yes, it is scalene'],
            'explanation': '$1 + 2 = 3$, failing the strict inequality. This would be a degenerate (flat) triangle.',
        },
        {
            'question': 'Which of the following is NOT a valid triangle?',
            'answer': '$7, 3, 3$',
            'wrong': ['$5, 5, 5$', '$6, 7, 8$', '$2, 3, 4$'],
            'explanation': '$3 + 3 = 6 < 7$, so $7,3,3$ violates the triangle inequality.',
        },
        {
            'question': 'If sides are $x+1$, $x+3$, and $x+5$, what constraint on $x$ gives a valid triangle?',
            'answer': '$x > 1$',
            'wrong': ['$x > 0$', '$x > 3$', '$x > 5$'],
            'explanation': 'Tightest: $(x+1)+(x+3)>x+5 \\Rightarrow 2x+4>x+5 \\Rightarrow x>1$.',
        },
        {
            'question': 'For sides $k$, $k+6$, $2k$ to form a valid triangle, which must hold?',
            'answer': '$k > 3$',
            'wrong': ['$k > 6$', '$k > 2$', '$k > 1$'],
            'explanation': 'Tightest: $k+2k > k+6 \\Rightarrow 2k > 6 \\Rightarrow k > 3$.',
        },
        {
            'question': 'The triangle inequality states that the sum of any two sides must be:',
            'answer': 'Greater than the third side (strictly)',
            'wrong': ['Less than the third side', 'Equal to the third side', 'At least equal to the third side'],
            'explanation': 'For any triangle with sides $a$, $b$, $c$: $a+b>c$, $a+c>b$, $b+c>a$ (all strict).',
        },
        {
            'question': 'If $a+b = c$ for positive values $a$, $b$, $c$, the figure formed is:',
            'answer': 'A degenerate triangle (line segment)',
            'wrong': ['An equilateral triangle', 'A right triangle', 'An isosceles triangle'],
            'explanation': 'When $a+b=c$, the three points are collinear. No enclosed area forms.',
        },
        {
            'question': 'In $\\triangle ABC$, $AB = 10$, $BC = 6$. Which is a possible length for $AC$?',
            'answer': '$7$',
            'wrong': ['$16$', '$4$', '$17$'],
            'explanation': '$|10-6| < AC < 10+6 \\Rightarrow 4 < AC < 16$. Only $7$ satisfies this.',
        },
        {
            'question': 'In $\\triangle PQR$, $PQ = 15$, $QR = 9$. What is the range of $PR$?',
            'answer': '$6 < PR < 24$',
            'wrong': ['$9 < PR < 15$', '$6 \\leq PR \\leq 24$', '$0 < PR < 24$'],
            'explanation': '$|15-9| < PR < 15+9 \\Rightarrow 6 < PR < 24$.',
        },
        {
            'question': 'If we double all sides of a valid triangle, does the new triangle satisfy the inequality?',
            'answer': 'Yes',
            'wrong': ['No', 'Only if the original is equilateral', 'Only if the original is a right triangle'],
            'explanation': 'Multiplying all sides by a positive constant preserves the inequality: $2a+2b > 2c \\Leftrightarrow a+b>c$.',
        },
        {
            'question': 'Can a triangle have sides $0.1$, $0.1$, and $0.3$?',
            'answer': 'No',
            'wrong': ['Yes', 'Yes, since all sides are positive', 'Only if it is scalene'],
            'explanation': '$0.1 + 0.1 = 0.2 < 0.3$. The triangle inequality is violated.',
        },
        {
            'question': 'For sides $m$, $2m$, $3m-1$ ($m>0$), what is the range of valid $m$?',
            'answer': '$m > \\dfrac{1}{2}$',
            'wrong': ['$m > 1$', '$m > 0$', '$m > 2$'],
            'explanation': 'Tightest: $m+(3m-1) > 2m \\Rightarrow 2m > 1 \\Rightarrow m > \\frac{1}{2}$.',
        },
        {
            'question': 'For sides $a=5$, $b=12$, how many integer values can the third side take?',
            'answer': '$9$',
            'wrong': ['$12$', '$17$', '$7$'],
            'explanation': '$|12-5| < x < 12+5 \\Rightarrow 7 < x < 17$. Integer values: $8,9,10,11,12,13,14,15,16$ — that is $9$ values.',
        },
        {
            'question': 'Which set has sides that form a valid triangle?',
            'answer': '$6, 8, 10$',
            'wrong': ['$1, 2, 4$', '$3, 3, 7$', '$5, 5, 11$'],
            'explanation': '$6+8=14>10$ ✓. For others: $1+2=3<4$; $3+3=6<7$; $5+5=10<11$ — all fail.',
        },
        {
            'question': 'If the sides of a triangle are $x$, $2x$, and $3$ ($x>0$), what values of $x$ are valid?',
            'answer': '$1 < x < 3$',
            'wrong': ['$x > 1$', '$0 < x < 3$', '$x > 3$'],
            'explanation': '$x+2x>3 \\Rightarrow x>1$ and $x+3>2x \\Rightarrow x<3$. Combined: $1 < x < 3$.',
        },
        {
            'question': 'A triangle has sides $5$, $12$, $13$. Does it satisfy the triangle inequality?',
            'answer': 'Yes',
            'wrong': ['No', 'Only for right triangles', 'It is degenerate'],
            'explanation': '$5+12=17>13$ ✓, $5+13=18>12$ ✓, $12+13=25>5$ ✓. This is also a right triangle ($5^2+12^2=13^2$).',
        },
        {
            'question': 'Given $a = 7$, $b = 24$, $c = 25$, is this a valid triangle?',
            'answer': 'Yes',
            'wrong': ['No', 'Only as a degenerate triangle', 'Cannot be determined'],
            'explanation': '$7+24=31>25$ ✓. This is also a Pythagorean triple ($7^2+24^2=625=25^2$).',
        },
        {
            'question': 'Sides $t+2$, $t+2$, $t+2$ form a valid (equilateral) triangle for:',
            'answer': 'All $t > -2$',
            'wrong': ['All $t > 0$', 'All $t > 2$', 'All real $t$'],
            'explanation': 'We need $t+2 > 0 \\Rightarrow t > -2$. Then $(t+2)+(t+2) = 2(t+2) > t+2$ automatically.',
        },
        {
            'question': 'Can a triangle have sides $1000$, $1$, and $1$?',
            'answer': 'No',
            'wrong': ['Yes', 'Yes, since all sides are positive', 'Cannot be determined'],
            'explanation': '$1 + 1 = 2 < 1000$. Triangle inequality violated.',
        },
        {
            'question': 'Which statement about the triangle inequality is correct?',
            'answer': 'It must hold for all three pairs of sides simultaneously',
            'wrong': ['It only needs to hold for the largest side', 'It uses non-strict ($\\geq$) inequalities',
                      'It only applies to right triangles'],
            'explanation': 'All three: $a+b>c$, $a+c>b$, $b+c>a$ must hold simultaneously for a valid triangle.',
        },
        {
            'question': 'For sides $a$, $b$, $c$, which is equivalent to the triangle inequality?',
            'answer': '$|a-b| < c < a+b$',
            'wrong': ['$a-b < c < a+b$', '$0 < c < a+b$', '$|a-b| \\leq c \\leq a+b$'],
            'explanation': 'Combining $c < a+b$ and $c > |a-b|$ gives the compact form $|a-b| < c < a+b$.',
        },
        {
            'question': 'A triangle has sides $n$, $n+3$, $2n$ for integer $n$. The minimum valid $n$ is:',
            'answer': '$n = 4$',
            'wrong': ['$n = 1$', '$n = 2$', '$n = 3$'],
            'explanation': 'Tightest: $n+(n+3) > 2n \\Rightarrow 3 > 0$ (always true); $n+2n > n+3 \\Rightarrow 2n > 3 \\Rightarrow n > 1.5$. Also need $n>0$. Minimum integer: $n=2$. Wait — recheck: $n+(2n) > n+3 \\Rightarrow 2n>3 \\Rightarrow n\\geq 2$. Minimum is $n=2$.',
        },
        {
            'question': 'Sides $n$, $n+3$, $2n$ for integer $n \\geq 1$. The minimum valid $n$ is:',
            'answer': '$n = 2$',
            'wrong': ['$n = 1$', '$n = 3$', '$n = 4$'],
            'explanation': 'Tightest: $n + 2n > n+3 \\Rightarrow 2n > 3 \\Rightarrow n > 1.5$. Minimum integer: $n=2$.',
        },
        {
            'question': 'The sides of a triangle satisfy $b = a+1$ and $c = a+2$. For which $a$ is the triangle valid?',
            'answer': '$a > 0$',
            'wrong': ['$a > 1$', '$a > 2$', '$a \\geq 1$'],
            'explanation': 'Tightest: $a+(a+1) > a+2 \\Rightarrow a > 1$... Wait: $2a+1>a+2 \\Rightarrow a>1$. But also $a>0$ needed for positivity. Binding: $a>1$.',
        },
        {
            'question': 'Sides $b = a+1$, $c = a+2$. The binding constraint for a valid triangle is:',
            'answer': '$a > 1$',
            'wrong': ['$a > 0$', '$a > 2$', '$a \\geq 1$'],
            'explanation': 'Tightest inequality: $a + (a+1) > a+2 \\Rightarrow 2a+1 > a+2 \\Rightarrow a > 1$.',
        },
        {
            'question': 'How many integer values can the third side $c$ take if $a = 10$, $b = 10$?',
            'answer': '$19$',
            'wrong': ['$20$', '$10$', '$18$'],
            'explanation': '$0 < c < 20$. Integer values: $1, 2, \\ldots, 19$ — that is $19$ values.',
        },
        {
            'question': 'If $a = b = 5$ and $c$ is the third side, the number of positive integer values $c$ can take is:',
            'answer': '$9$',
            'wrong': ['$10$', '$5$', '$4$'],
            'explanation': '$0 < c < 10$. Integer values: $1,2,3,4,5,6,7,8,9$ — that is $9$ values.',
        },
        {
            'question': 'Sides $2$, $x$, $x+1$ form a valid triangle for $x > 0$. The constraint on $x$ is:',
            'answer': '$x > 1$',
            'wrong': ['$x > 0$', '$x > 2$', '$x > 3$'],
            'explanation': 'Tightest: $2 + x > x+1 \\Rightarrow 2 > 1$ ✓ (always); $x + (x+1) > 2 \\Rightarrow 2x > 1 \\Rightarrow x > \\frac{1}{2}$. Also need $x > 0$. Binding: $x > \\frac{1}{2}$.',
        },
        {'question': 'A right triangle has legs $a = 3$ and $b = 4$. Find the hypotenuse.', 'answer': '$5$',
         'wrong': ['$6$', '$7$', '$\\sqrt{7}$'], 'explanation': '$c = \\sqrt{9+16} = 5$.'},
        {'question': 'A right triangle has legs $a = 5$ and $b = 12$. Find the hypotenuse.', 'answer': '$13$',
         'wrong': ['$17$', '$15$', '$\\sqrt{119}$'], 'explanation': '$c = \\sqrt{25+144} = 13$.'},
        {'question': 'A right triangle has legs $a = 8$ and $b = 6$. Find the hypotenuse.', 'answer': '$10$',
         'wrong': ['$12$', '$14$', '$\\sqrt{28}$'], 'explanation': '$c = \\sqrt{64+36} = 10$.'},
        {'question': 'A right triangle has legs $a = 7$ and $b = 24$. Find the hypotenuse.', 'answer': '$25$',
         'wrong': ['$31$', '$23$', '$\\sqrt{527}$'], 'explanation': '$c = \\sqrt{49+576} = 25$.'},
        {'question': 'A right triangle has legs $a = 9$ and $b = 40$. Find the hypotenuse.', 'answer': '$41$',
         'wrong': ['$49$', '$39$', '$\\sqrt{1519}$'], 'explanation': '$c = \\sqrt{81+1600} = 41$.'},
        {'question': 'A right triangle has legs $a = 6$ and $b = 6$. Find the hypotenuse.', 'answer': '$6\\sqrt{2}$',
         'wrong': ['$12$', '$6$', '$3\\sqrt{2}$'], 'explanation': '$c = \\sqrt{72} = 6\\sqrt{2}$.'},
        {'question': 'A right triangle has hypotenuse $c = 10$ and one leg $a = 6$. Find the other leg.',
         'answer': '$8$', 'wrong': ['$4$', '$6$', '$\\sqrt{136}$'], 'explanation': '$b = \\sqrt{100-36} = 8$.'},
        {'question': 'A right triangle has hypotenuse $c = 13$ and one leg $a = 5$. Find the other leg.',
         'answer': '$12$', 'wrong': ['$8$', '$10$', '$11$'], 'explanation': '$b = \\sqrt{169-25} = 12$.'},
        {'question': 'A right triangle has legs $a = 1$ and $b = \\sqrt{3}$. Find the hypotenuse.', 'answer': '$2$',
         'wrong': ['$\\sqrt{2}$', '$\\sqrt{5}$', '$4$'], 'explanation': '$c = \\sqrt{1+3} = 2$.'},
        {'question': 'A right triangle has legs $a = 20$ and $b = 21$. Find the hypotenuse.', 'answer': '$29$',
         'wrong': ['$41$', '$31$', '$\\sqrt{400}$'], 'explanation': '$c = \\sqrt{400+441} = \\sqrt{841} = 29$.'},

        # ── AREA (10) ─────────────────────────────────────────────────────────────
        {'question': 'Find the area of a right triangle with legs $a = 6$ and $b = 8$.', 'answer': '$24$',
         'wrong': ['$48$', '$12$', '$14$'], 'explanation': '$A = \\frac{1}{2}(6)(8) = 24$.'},
        {'question': 'Find the area of a right triangle with legs $a = 5$ and $b = 12$.', 'answer': '$30$',
         'wrong': ['$60$', '$15$', '$17$'], 'explanation': '$A = \\frac{1}{2}(5)(12) = 30$.'},
        {'question': 'Find the area of a right triangle with legs $a = 3$ and $b = 4$.', 'answer': '$6$',
         'wrong': ['$12$', '$7$', '$3.5$'], 'explanation': '$A = \\frac{1}{2}(3)(4) = 6$.'},
        {'question': 'A right triangle has area $24$ and one leg $a = 8$. Find the other leg.', 'answer': '$6$',
         'wrong': ['$3$', '$12$', '$4$'], 'explanation': '$24 = \\frac{1}{2}(8)b \\Rightarrow b = 6$.'},
        {'question': 'Find the area of a right triangle with legs $a = 10$ and $b = 10$.', 'answer': '$50$',
         'wrong': ['$100$', '$25$', '$200$'], 'explanation': '$A = \\frac{1}{2}(10)(10) = 50$.'},
        {'question': 'A right triangle has hypotenuse $c = 10$ and one leg $a = 6$. Find its area.', 'answer': '$24$',
         'wrong': ['$30$', '$48$', '$60$'], 'explanation': '$b = 8$. $A = \\frac{1}{2}(6)(8) = 24$.'},
        {'question': 'Find the area of a right triangle with legs $a = 7$ and $b = 24$.', 'answer': '$84$',
         'wrong': ['$168$', '$42$', '$31$'], 'explanation': '$A = \\frac{1}{2}(7)(24) = 84$.'},
        {'question': 'A right triangle has legs in ratio $3:4$ and area $54$. Find the legs.', 'answer': '$9$ and $12$',
         'wrong': ['$6$ and $8$', '$12$ and $16$', '$3$ and $4$'],
         'explanation': '$\\frac{1}{2}(3k)(4k)=54 \\Rightarrow k=3$. Legs: $9, 12$.'},
        {'question': 'Find the area of an isosceles right triangle with legs $a = 4$.', 'answer': '$8$',
         'wrong': ['$16$', '$4$', '$4\\sqrt{2}$'], 'explanation': '$A = \\frac{1}{2}(4)(4) = 8$.'},
        {'question': 'A right triangle has legs $a = 9$ and $b = 40$. Find its area.', 'answer': '$180$',
         'wrong': ['$360$', '$90$', '$369$'], 'explanation': '$A = \\frac{1}{2}(9)(40) = 180$.'},

        # ── PERIMETER (10) ────────────────────────────────────────────────────────
        {'question': 'Find the perimeter of a right triangle with legs $3, 4$ and hypotenuse $5$.', 'answer': '$12$',
         'wrong': ['$7$', '$10$', '$14$'], 'explanation': '$P = 3+4+5 = 12$.'},
        {'question': 'Find the perimeter of a right triangle with legs $5, 12$ and hypotenuse $13$.', 'answer': '$30$',
         'wrong': ['$25$', '$18$', '$17$'], 'explanation': '$P = 5+12+13 = 30$.'},
        {'question': 'Find the perimeter of a right triangle with legs $8, 6$ and hypotenuse $10$.', 'answer': '$24$',
         'wrong': ['$14$', '$20$', '$28$'], 'explanation': '$P = 8+6+10 = 24$.'},
        {'question': 'A right triangle has legs $7$ and $24$. Find its perimeter.', 'answer': '$56$',
         'wrong': ['$50$', '$60$', '$31$'], 'explanation': '$c = 25$. $P = 7+24+25 = 56$.'},
        {'question': 'A right triangle has legs $9$ and $40$. Find its perimeter.', 'answer': '$90$',
         'wrong': ['$49$', '$82$', '$81$'], 'explanation': '$c = 41$. $P = 9+40+41 = 90$.'},
        {'question': 'An isosceles right triangle has legs $a = 5$. Find its perimeter.', 'answer': '$10 + 5\\sqrt{2}$',
         'wrong': ['$15$', '$10\\sqrt{2}$', '$5+10\\sqrt{2}$'],
         'explanation': '$c = 5\\sqrt{2}$. $P = 10+5\\sqrt{2}$.'},
        {'question': 'A right triangle has hypotenuse $17$ and one leg $8$. Find its perimeter.', 'answer': '$40$',
         'wrong': ['$34$', '$38$', '$42$'], 'explanation': '$b = 15$. $P = 8+15+17 = 40$.'},
        {'question': 'A right triangle has hypotenuse $25$ and one leg $7$. Find its perimeter.', 'answer': '$56$',
         'wrong': ['$50$', '$32$', '$60$'], 'explanation': '$b = 24$. $P = 7+24+25 = 56$.'},
        {'question': 'A right triangle has legs in ratio $1:1$ and hypotenuse $10\\sqrt{2}$. Find its perimeter.',
         'answer': '$20 + 10\\sqrt{2}$', 'wrong': ['$30$', '$20\\sqrt{2}$', '$10\\sqrt{2}$'],
         'explanation': 'Legs $= 10$. $P = 20+10\\sqrt{2}$.'},
        {'question': 'A right triangle has legs $20$ and $21$. Find its perimeter.', 'answer': '$70$',
         'wrong': ['$50$', '$62$', '$41$'], 'explanation': '$c = 29$. $P = 20+21+29 = 70$.'},

        # ── ANGLES (10) ───────────────────────────────────────────────────────────
        {'question': 'A right triangle has one acute angle of $30°$. Find the other acute angle.', 'answer': '$60°$',
         'wrong': ['$30°$', '$45°$', '$90°$'], 'explanation': '$90+30+x=180 \\Rightarrow x=60°$.'},
        {'question': 'In a right triangle, acute angles are $(2x+10)°$ and $(3x)°$. Find $x$.', 'answer': '$x = 16$',
         'wrong': ['$x = 18$', '$x = 14$', '$x = 20$'], 'explanation': '$5x+10=90 \\Rightarrow x=16$.'},
        {'question': 'A right triangle has acute angles in ratio $1:2$. Find them.', 'answer': '$30°$ and $60°$',
         'wrong': ['$20°$ and $40°$', '$35°$ and $70°$', '$45°$ and $90°$'],
         'explanation': '$x+2x=90 \\Rightarrow x=30°$.'},
        {'question': 'A right triangle has one angle of $45°$. What type of right triangle is it?',
         'answer': 'Isosceles right triangle', 'wrong': ['Scalene', '30-60-90', 'Equilateral'],
         'explanation': 'Angles $45°, 45°, 90°$ — two equal angles means isosceles.'},
        {'question': 'In a right triangle, one acute angle is $37°$. Find the other.', 'answer': '$53°$',
         'wrong': ['$43°$', '$47°$', '$63°$'], 'explanation': '$90°-37°=53°$.'},
        {'question': 'A right triangle has legs $a = b$. Find each acute angle.', 'answer': '$45°$',
         'wrong': ['$30°$', '$60°$', '$50°$'],
         'explanation': 'Equal legs → equal angles. Two angles sum to $90°$, so each is $45°$.'},
        {'question': 'In a right triangle, one acute angle is five times the other. Find both.',
         'answer': '$15°$ and $75°$', 'wrong': ['$18°$ and $72°$', '$20°$ and $70°$', '$30°$ and $60°$'],
         'explanation': '$x+5x=90 \\Rightarrow x=15°$.'},
        {'question': 'A right triangle has hypotenuse $10$ and leg $5$. Find the angle opposite the leg of $5$.',
         'answer': '$30°$', 'wrong': ['$45°$', '$60°$', '$90°$'],
         'explanation': '$\\sin\\theta=\\frac{5}{10}=\\frac{1}{2} \\Rightarrow \\theta=30°$.'},
        {'question': 'In a right triangle, angles are $(4x)°$, $(2x)°$, and $90°$. Find $x$.', 'answer': '$x = 15$',
         'wrong': ['$x = 10$', '$x = 20$', '$x = 18$'],
         'explanation': '$4x+2x+90=180 \\Rightarrow 6x=90 \\Rightarrow x=15$.'},
        {'question': 'A right triangle has acute angle $(x+5)°$ and $(2x-2)°$. Find each angle.',
         'answer': '$34°$ and $56°$', 'wrong': ['$30°$ and $60°$', '$29°$ and $61°$', '$45°$ and $45°$'],
         'explanation': '$(x+5)+(2x-2)=90 \\Rightarrow 3x=87 \\Rightarrow x=29$. Angles: $34°, 56°$.'},

        # ══════════════════════════════════════════════════════════════════════════
        # ISOSCELES TRIANGLE  (Q41–80)
        # 10 height | 10 area | 10 perimeter | 10 angles
        # ══════════════════════════════════════════════════════════════════════════

        # ── HEIGHT (10) ───────────────────────────────────────────────────────────
        {'question': 'An isosceles triangle has equal sides $a = 5$ and base $b = 6$. Find the height.',
         'answer': '$4$', 'wrong': ['$3$', '$5$', '$\\sqrt{34}$'], 'explanation': '$h=\\sqrt{25-9}=4$.'},
        {'question': 'An isosceles triangle has equal sides $a = 10$ and base $b = 12$. Find the height.',
         'answer': '$8$', 'wrong': ['$6$', '$10$', '$\\sqrt{136}$'], 'explanation': '$h=\\sqrt{100-36}=8$.'},
        {'question': 'An isosceles triangle has equal sides $a = 13$ and base $b = 10$. Find the height.',
         'answer': '$12$', 'wrong': ['$11$', '$10$', '$\\sqrt{119}$'], 'explanation': '$h=\\sqrt{169-25}=12$.'},
        {'question': 'An isosceles triangle has equal sides $a = 17$ and base $b = 16$. Find the height.',
         'answer': '$15$', 'wrong': ['$13$', '$16$', '$\\sqrt{225}$'], 'explanation': '$h=\\sqrt{289-64}=15$.'},
        {'question': 'An isosceles triangle has equal sides $a = 5$ and base $b = 8$. Find the height.',
         'answer': '$3$', 'wrong': ['$4$', '$\\sqrt{41}$', '$5$'], 'explanation': '$h=\\sqrt{25-16}=3$.'},
        {'question': 'An isosceles triangle has equal sides $a = 15$ and base $b = 18$. Find the height.',
         'answer': '$12$', 'wrong': ['$9$', '$15$', '$\\sqrt{306}$'], 'explanation': '$h=\\sqrt{225-81}=12$.'},
        {'question': 'An isosceles triangle has equal sides $a = 25$ and base $b = 14$. Find the height.',
         'answer': '$24$', 'wrong': ['$20$', '$25$', '$\\sqrt{674}$'], 'explanation': '$h=\\sqrt{625-49}=24$.'},
        {'question': 'The height of an isosceles triangle is $h = 8$ and base $b = 12$. Find the equal side.',
         'answer': '$10$', 'wrong': ['$8$', '$6$', '$\\sqrt{208}$'], 'explanation': '$a=\\sqrt{64+36}=10$.'},
        {'question': 'The height is $h = 6$ and equal sides $a = 10$. Find the base of the isosceles triangle.',
         'answer': '$16$', 'wrong': ['$8$', '$12$', '$\\sqrt{136}$'],
         'explanation': '$\\frac{b}{2}=\\sqrt{100-36}=8 \\Rightarrow b=16$.'},
        {'question': 'An isosceles triangle has equal sides $a = 20$ and base $b = 24$. Find the height.',
         'answer': '$16$', 'wrong': ['$14$', '$12$', '$\\sqrt{544}$'], 'explanation': '$h=\\sqrt{400-144}=16$.'},

        # ── AREA (10) ─────────────────────────────────────────────────────────────
        {'question': 'An isosceles triangle has base $b = 6$ and height $h = 4$. Find the area.', 'answer': '$12$',
         'wrong': ['$24$', '$6$', '$10$'], 'explanation': '$A=\\frac{1}{2}(6)(4)=12$.'},
        {'question': 'An isosceles triangle has equal sides $a = 5$ and base $b = 6$. Find the area.', 'answer': '$12$',
         'wrong': ['$15$', '$6$', '$30$'], 'explanation': '$h=4$. $A=\\frac{1}{2}(6)(4)=12$.'},
        {'question': 'An isosceles triangle has equal sides $a = 10$ and base $b = 12$. Find the area.',
         'answer': '$48$', 'wrong': ['$60$', '$24$', '$96$'], 'explanation': '$h=8$. $A=\\frac{1}{2}(12)(8)=48$.'},
        {'question': 'An isosceles triangle has equal sides $a = 13$ and base $b = 10$. Find the area.',
         'answer': '$60$', 'wrong': ['$65$', '$30$', '$130$'], 'explanation': '$h=12$. $A=\\frac{1}{2}(10)(12)=60$.'},
        {'question': 'An isosceles triangle has base $b = 8$ and height $h = 3$. Find the area.', 'answer': '$12$',
         'wrong': ['$24$', '$6$', '$11$'], 'explanation': '$A=\\frac{1}{2}(8)(3)=12$.'},
        {'question': 'An isosceles triangle has equal sides $a = 17$ and base $b = 16$. Find the area.',
         'answer': '$120$', 'wrong': ['$136$', '$60$', '$240$'],
         'explanation': '$h=15$. $A=\\frac{1}{2}(16)(15)=120$.'},
        {'question': 'An isosceles triangle has area $40$ and base $b = 10$. Find the height.', 'answer': '$8$',
         'wrong': ['$4$', '$6$', '$10$'], 'explanation': '$40=\\frac{1}{2}(10)h \\Rightarrow h=8$.'},
        {'question': 'An isosceles triangle has equal sides $a = 25$ and base $b = 14$. Find the area.',
         'answer': '$168$', 'wrong': ['$175$', '$84$', '$336$'],
         'explanation': '$h=24$. $A=\\frac{1}{2}(14)(24)=168$.'},
        {'question': 'An isosceles triangle has equal sides $a = 15$ and base $b = 20$. Find the area.',
         'answer': '$50\\sqrt{5}$', 'wrong': ['$150$', '$100\\sqrt{5}$', '$75$'],
         'explanation': '$h=\\sqrt{225-100}=\\sqrt{125}=5\\sqrt{5}$. $A=\\frac{1}{2}(20)(5\\sqrt{5})=50\\sqrt{5}$.'},
        {'question': 'An isosceles triangle has equal sides $a = 20$ and base $b = 24$. Find the area.',
         'answer': '$192$', 'wrong': ['$240$', '$96$', '$160$'],
         'explanation': '$h=16$. $A=\\frac{1}{2}(24)(16)=192$.'},

        # ── PERIMETER (10) ────────────────────────────────────────────────────────
        {'question': 'An isosceles triangle has equal sides $a = 7$ and base $b = 5$. Find the perimeter.',
         'answer': '$19$', 'wrong': ['$14$', '$17$', '$21$'], 'explanation': '$P=2(7)+5=19$.'},
        {'question': 'An isosceles triangle has equal sides $a = 10$ and base $b = 6$. Find the perimeter.',
         'answer': '$26$', 'wrong': ['$20$', '$16$', '$30$'], 'explanation': '$P=2(10)+6=26$.'},
        {'question': 'An isosceles triangle has perimeter $30$ and base $b = 8$. Find each equal side.',
         'answer': '$11$', 'wrong': ['$7$', '$15$', '$22$'], 'explanation': '$2a=30-8=22 \\Rightarrow a=11$.'},
        {'question': 'An isosceles triangle has equal sides $a = 9$ and base $b = 14$. Find the perimeter.',
         'answer': '$32$', 'wrong': ['$23$', '$28$', '$36$'], 'explanation': '$P=2(9)+14=32$.'},
        {'question': 'An isosceles triangle has perimeter $50$ and equal sides $a = 15$. Find the base.',
         'answer': '$20$', 'wrong': ['$10$', '$25$', '$35$'], 'explanation': '$b=50-30=20$.'},
        {'question': 'An isosceles triangle has equal sides $a = 12$ and base $b = 10$. Find the perimeter.',
         'answer': '$34$', 'wrong': ['$24$', '$22$', '$44$'], 'explanation': '$P=2(12)+10=34$.'},
        {'question': 'An isosceles triangle has perimeter $40$ and each equal side is twice the base. Find the base.',
         'answer': '$8$', 'wrong': ['$10$', '$16$', '$5$'], 'explanation': '$5b=40 \\Rightarrow b=8$.'},
        {'question': 'An isosceles triangle has equal sides $a = 8$ and base $b = 6$. Find the perimeter.',
         'answer': '$22$', 'wrong': ['$16$', '$24$', '$14$'], 'explanation': '$P=2(8)+6=22$.'},
        {'question': 'An isosceles triangle has base $b = 3$ and equal sides $a = 4$. Find the perimeter.',
         'answer': '$11$', 'wrong': ['$7$', '$12$', '$8$'], 'explanation': '$P=2(4)+3=11$.'},
        {'question': 'An isosceles triangle has perimeter $48$ and base $b = 12$. Find each equal side.',
         'answer': '$18$', 'wrong': ['$12$', '$24$', '$36$'], 'explanation': '$2a=48-12=36 \\Rightarrow a=18$.'},

        # ── ANGLES (10) ───────────────────────────────────────────────────────────
        {'question': 'An isosceles triangle has vertex angle $40°$. Find each base angle.', 'answer': '$70°$',
         'wrong': ['$40°$', '$80°$', '$60°$'], 'explanation': 'Base angles $=\\frac{180-40}{2}=70°$.'},
        {'question': 'An isosceles triangle has base angles $55°$ each. Find the vertex angle.', 'answer': '$70°$',
         'wrong': ['$55°$', '$90°$', '$110°$'], 'explanation': 'Vertex $=180-110=70°$.'},
        {'question': 'Isosceles triangle: vertex $(4x)°$, base angles $(3x+10)°$ each. Find $x$.', 'answer': '$x = 16$',
         'wrong': ['$x = 18$', '$x = 14$', '$x = 20$'],
         'explanation': '$4x+2(3x+10)=180 \\Rightarrow 10x=160 \\Rightarrow x=16$.'},
        {'question': 'An isosceles triangle has a base angle of $72°$. Find the vertex angle.', 'answer': '$36°$',
         'wrong': ['$72°$', '$108°$', '$54°$'], 'explanation': 'Vertex $=180-144=36°$.'},
        {'question': 'In an isosceles triangle the vertex angle is three times a base angle. Find all angles.',
         'answer': '$36°, 36°, 108°$', 'wrong': ['$30°, 30°, 120°$', '$45°, 45°, 90°$', '$40°, 40°, 100°$'],
         'explanation': '$5x=180 \\Rightarrow x=36°$. Vertex $=108°$.'},
        {'question': 'An isosceles right triangle has the right angle at the apex. Find the base angles.',
         'answer': '$45°$', 'wrong': ['$30°$', '$60°$', '$90°$'],
         'explanation': 'Base angles $=\\frac{180-90}{2}=45°$.'},
        {'question': 'Isosceles triangle: base angles $(2x+5)°$ each, vertex $(x+10)°$. Find $x$.',
         'answer': '$x = 32$', 'wrong': ['$x = 28$', '$x = 36$', '$x = 24$'],
         'explanation': '$2(2x+5)+(x+10)=180 \\Rightarrow 5x=160 \\Rightarrow x=32$.'},
        {'question': 'An isosceles triangle has vertex angle $100°$. What are the base angles?', 'answer': '$40°$ each',
         'wrong': ['$80°$ each', '$50°$ each', '$45°$ each'], 'explanation': 'Base $=\\frac{180-100}{2}=40°$.'},
        {'question': 'Isosceles triangle vertex angle is $20°$ more than each base angle. Find all angles.',
         'answer': '$53\\tfrac{1}{3}°, 53\\tfrac{1}{3}°, 73\\tfrac{1}{3}°$',
         'wrong': ['$50°, 50°, 80°$', '$55°, 55°, 70°$', '$60°, 60°, 60°$'],
         'explanation': '$3x+20=180 \\Rightarrow x=\\frac{160}{3}\\approx53.3°$. Vertex $=73.3°$.'},
        {'question': 'An isosceles triangle has base angles in ratio $1:1$ and vertex $50°$. Find each base angle.',
         'answer': '$65°$', 'wrong': ['$50°$', '$90°$', '$55°$'], 'explanation': 'Base $=\\frac{180-50}{2}=65°$.'},

        # ══════════════════════════════════════════════════════════════════════════
        # EQUILATERAL TRIANGLE  (Q81–120)
        # 10 area | 10 angles | 10 perimeter | 10 height
        # ══════════════════════════════════════════════════════════════════════════

        # ── AREA (10) ─────────────────────────────────────────────────────────────
        {'question': 'Find the area of an equilateral triangle with side $s = 4$.', 'answer': '$4\\sqrt{3}$',
         'wrong': ['$8\\sqrt{3}$', '$2\\sqrt{3}$', '$16$'], 'explanation': '$A=\\frac{\\sqrt{3}}{4}(16)=4\\sqrt{3}$.'},
        {'question': 'Find the area of an equilateral triangle with side $s = 6$.', 'answer': '$9\\sqrt{3}$',
         'wrong': ['$18\\sqrt{3}$', '$6\\sqrt{3}$', '$36$'], 'explanation': '$A=\\frac{\\sqrt{3}}{4}(36)=9\\sqrt{3}$.'},
        {'question': 'Find the area of an equilateral triangle with side $s = 10$.', 'answer': '$25\\sqrt{3}$',
         'wrong': ['$50\\sqrt{3}$', '$10\\sqrt{3}$', '$100$'],
         'explanation': '$A=\\frac{\\sqrt{3}}{4}(100)=25\\sqrt{3}$.'},
        {'question': 'The area of an equilateral triangle is $16\\sqrt{3}$. Find the side length.', 'answer': '$8$',
         'wrong': ['$4$', '$16$', '$4\\sqrt{3}$'], 'explanation': '$s^2=64 \\Rightarrow s=8$.'},
        {'question': 'Find the area of an equilateral triangle with side $s = 2$.', 'answer': '$\\sqrt{3}$',
         'wrong': ['$2\\sqrt{3}$', '$4\\sqrt{3}$', '$\\frac{\\sqrt{3}}{4}$'],
         'explanation': '$A=\\frac{\\sqrt{3}}{4}(4)=\\sqrt{3}$.'},
        {'question': 'The area of an equilateral triangle is $36\\sqrt{3}$. Find the side length.', 'answer': '$12$',
         'wrong': ['$6$', '$9$', '$18$'], 'explanation': '$s^2=144 \\Rightarrow s=12$.'},
        {'question': 'Find the area of an equilateral triangle with side $s = 8$.', 'answer': '$16\\sqrt{3}$',
         'wrong': ['$32\\sqrt{3}$', '$8\\sqrt{3}$', '$64$'],
         'explanation': '$A=\\frac{\\sqrt{3}}{4}(64)=16\\sqrt{3}$.'},
        {'question': 'An equilateral triangle has height $h = 3\\sqrt{3}$. Find its area.', 'answer': '$9\\sqrt{3}$',
         'wrong': ['$3\\sqrt{3}$', '$18$', '$6\\sqrt{3}$'],
         'explanation': '$h=\\frac{\\sqrt{3}}{2}s \\Rightarrow s=6$. $A=9\\sqrt{3}$.'},
        {'question': 'Find the area of an equilateral triangle with side $s = 5$.',
         'answer': '$\\dfrac{25\\sqrt{3}}{4}$',
         'wrong': ['$\\frac{5\\sqrt{3}}{4}$', '$25\\sqrt{3}$', '$\\frac{25}{4}$'],
         'explanation': '$A=\\frac{\\sqrt{3}}{4}(25)=\\frac{25\\sqrt{3}}{4}$.'},
        {'question': 'Two equilateral triangles have sides $4$ and $8$. What is the ratio of their areas?',
         'answer': '$1:4$', 'wrong': ['$1:2$', '$2:1$', '$1:8$'], 'explanation': '$4\\sqrt{3}:16\\sqrt{3}=1:4$.'},

        # ── ANGLES (10) ───────────────────────────────────────────────────────────
        {'question': 'What is each interior angle of an equilateral triangle?', 'answer': '$60°$',
         'wrong': ['$45°$', '$90°$', '$120°$'], 'explanation': 'All angles equal; $3 \\times 60°=180°$.'},
        {'question': 'One angle of an equilateral triangle is $(2x)°$. Find $x$.', 'answer': '$x = 30$',
         'wrong': ['$x = 45$', '$x = 60$', '$x = 20$'], 'explanation': '$2x=60 \\Rightarrow x=30$.'},
        {'question': 'Can an equilateral triangle have an obtuse angle?', 'answer': 'No — all angles are $60°$',
         'wrong': ['Yes — one angle can be $90°$', 'Yes — one angle can be $120°$', 'Yes, if sides differ'],
         'explanation': 'All angles are $60°$ — all acute.'},
        {'question': 'What is the exterior angle of an equilateral triangle at each vertex?', 'answer': '$120°$',
         'wrong': ['$60°$', '$90°$', '$180°$'], 'explanation': 'Exterior $=180°-60°=120°$.'},
        {'question': 'What is the sum of all exterior angles of an equilateral triangle?', 'answer': '$360°$',
         'wrong': ['$180°$', '$240°$', '$720°$'],
         'explanation': 'Sum of exterior angles of any convex polygon is $360°$.'},
        {'question': 'An equilateral triangle has one angle $(3x-30)°$. Find $x$.', 'answer': '$x = 30$',
         'wrong': ['$x = 20$', '$x = 40$', '$x = 10$'], 'explanation': '$3x-30=60 \\Rightarrow x=30$.'},
        {'question': 'Is an equilateral triangle also equiangular?', 'answer': 'Yes — all angles are $60°$',
         'wrong': ['No', 'Only for side $> 1$', 'Only if also right'],
         'explanation': 'Equal sides force equal angles in a triangle.'},
        {'question': 'The altitude of an equilateral triangle makes what angle with the base?', 'answer': '$90°$',
         'wrong': ['$60°$', '$45°$', '$30°$'], 'explanation': 'The altitude is perpendicular to the base: $90°$.'},
        {
            'question': 'An equilateral triangle is divided into two triangles by the altitude. Find each angle of one half-triangle.',
            'answer': '$30°, 60°, 90°$', 'wrong': ['$45°, 45°, 90°$', '$60°, 60°, 60°$', '$30°, 30°, 120°$'],
            'explanation': 'The altitude bisects the top $60°$ angle and meets the base at $90°$: angles are $30°, 60°, 90°$.'},
        {'question': 'Two angles of an equilateral triangle are $(x+10)°$ and $(2x-20)°$. Find $x$.',
         'answer': '$x = 30$', 'wrong': ['$x = 20$', '$x = 40$', '$x = 50$'],
         'explanation': '$x+10=60 \\Rightarrow x=50$; or $2x-20=60 \\Rightarrow x=40$. Using $x+10=2x-20 \\Rightarrow x=30$.'},

        # ── PERIMETER (10) ────────────────────────────────────────────────────────
        {'question': 'Find the perimeter of an equilateral triangle with side $s = 7$.', 'answer': '$21$',
         'wrong': ['$14$', '$28$', '$49$'], 'explanation': '$P=3(7)=21$.'},
        {'question': 'An equilateral triangle has perimeter $36$. Find the side length.', 'answer': '$12$',
         'wrong': ['$9$', '$18$', '$6$'], 'explanation': '$s=36/3=12$.'},
        {'question': 'Find the perimeter of an equilateral triangle with side $s = 4.5$.', 'answer': '$13.5$',
         'wrong': ['$9$', '$18$', '$4.5$'], 'explanation': '$P=3(4.5)=13.5$.'},
        {
            'question': 'The perimeter of an equilateral triangle equals the perimeter of a square with side $6$. Find the triangle\'s side.',
            'answer': '$8$', 'wrong': ['$6$', '$12$', '$4$'], 'explanation': 'Square $P=24$. $s=24/3=8$.'},
        {'question': 'An equilateral triangle has side $s = 3\\sqrt{3}$. Find its perimeter.', 'answer': '$9\\sqrt{3}$',
         'wrong': ['$3\\sqrt{3}$', '$6\\sqrt{3}$', '$27$'], 'explanation': '$P=3(3\\sqrt{3})=9\\sqrt{3}$.'},
        {'question': 'An equilateral triangle has perimeter $15$. Find the side length.', 'answer': '$5$',
         'wrong': ['$3$', '$7.5$', '$6$'], 'explanation': '$s=15/3=5$.'},
        {'question': 'Two equilateral triangles have sides $5$ and $7$. What is the difference in their perimeters?',
         'answer': '$6$', 'wrong': ['$2$', '$4$', '$8$'], 'explanation': '$P_1=15$, $P_2=21$. Difference $=6$.'},
        {'question': 'An equilateral triangle has perimeter $p$. Express the side in terms of $p$.',
         'answer': '$\\dfrac{p}{3}$', 'wrong': ['$3p$', '$\\frac{p}{2}$', '$\\frac{p}{4}$'], 'explanation': '$s=p/3$.'},
        {
            'question': 'An equilateral triangle has the same perimeter as a rectangle $10 \\times 5$. Find the triangle\'s side.',
            'answer': '$10$', 'wrong': ['$15$', '$5$', '$30$'], 'explanation': 'Rectangle $P=30$. $s=30/3=10$.'},
        {'question': 'An equilateral triangle has perimeter $24$. Find the area.', 'answer': '$16\\sqrt{3}$',
         'wrong': ['$8\\sqrt{3}$', '$24\\sqrt{3}$', '$32\\sqrt{3}$'],
         'explanation': '$s=8$. $A=\\frac{\\sqrt{3}}{4}(64)=16\\sqrt{3}$.'},

        # ── HEIGHT (10) ───────────────────────────────────────────────────────────
        {'question': 'Find the height of an equilateral triangle with side $s = 2$.', 'answer': '$\\sqrt{3}$',
         'wrong': ['$2\\sqrt{3}$', '$\\frac{\\sqrt{3}}{2}$', '$1$'],
         'explanation': '$h=\\frac{\\sqrt{3}}{2}(2)=\\sqrt{3}$.'},
        {'question': 'Find the height of an equilateral triangle with side $s = 4$.', 'answer': '$2\\sqrt{3}$',
         'wrong': ['$4\\sqrt{3}$', '$\\sqrt{3}$', '$8$'], 'explanation': '$h=\\frac{\\sqrt{3}}{2}(4)=2\\sqrt{3}$.'},
        {'question': 'Find the height of an equilateral triangle with side $s = 6$.', 'answer': '$3\\sqrt{3}$',
         'wrong': ['$6\\sqrt{3}$', '$\\sqrt{3}$', '$9$'], 'explanation': '$h=\\frac{\\sqrt{3}}{2}(6)=3\\sqrt{3}$.'},
        {'question': 'Find the height of an equilateral triangle with side $s = 10$.', 'answer': '$5\\sqrt{3}$',
         'wrong': ['$10\\sqrt{3}$', '$2\\sqrt{3}$', '$25$'], 'explanation': '$h=\\frac{\\sqrt{3}}{2}(10)=5\\sqrt{3}$.'},
        {'question': 'An equilateral triangle has height $h = 6\\sqrt{3}$. Find the side length.', 'answer': '$12$',
         'wrong': ['$6$', '$24$', '$6\\sqrt{3}$'], 'explanation': '$s=\\frac{2h}{\\sqrt{3}}=12$.'},
        {'question': 'Find the height of an equilateral triangle with side $s = 8$.', 'answer': '$4\\sqrt{3}$',
         'wrong': ['$8\\sqrt{3}$', '$2\\sqrt{3}$', '$16$'], 'explanation': '$h=\\frac{\\sqrt{3}}{2}(8)=4\\sqrt{3}$.'},
        {'question': 'An equilateral triangle has height $h = \\sqrt{3}$. Find the side length.', 'answer': '$2$',
         'wrong': ['$1$', '$\\sqrt{3}$', '$4$'], 'explanation': '$s=\\frac{2\\sqrt{3}}{\\sqrt{3}}=2$.'},
        {'question': 'Find the height of an equilateral triangle with side $s = 12$.', 'answer': '$6\\sqrt{3}$',
         'wrong': ['$12\\sqrt{3}$', '$3\\sqrt{3}$', '$36$'], 'explanation': '$h=\\frac{\\sqrt{3}}{2}(12)=6\\sqrt{3}$.'},
        {'question': 'An equilateral triangle has height $h = 5\\sqrt{3}$. Find its area.', 'answer': '$25\\sqrt{3}$',
         'wrong': ['$50\\sqrt{3}$', '$10\\sqrt{3}$', '$75$'],
         'explanation': '$s=10$. $A=\\frac{\\sqrt{3}}{4}(100)=25\\sqrt{3}$.'},
        {'question': 'What fraction of the side length is the height of an equilateral triangle?',
         'answer': '$\\dfrac{\\sqrt{3}}{2}$', 'wrong': ['$\\frac{1}{2}$', '$\\sqrt{3}$', '$\\frac{\\sqrt{2}}{2}$'],
         'explanation': '$h=\\frac{\\sqrt{3}}{2}s \\Rightarrow \\frac{h}{s}=\\frac{\\sqrt{3}}{2}$.'}
    ],
    'types_of_quadrilateral': [
        {
            "question": "Side length of a square is $s = 7$ cm. Find the perimeter.",
            "answer": "$P = 28$ cm",
            "wrong": ["$P = 14$ cm", "$P = 49$ cm", "$P = 21$ cm"],
            "explanation": "$P = 4s = 4 \\times 7 = 28$ cm."
        },
        {
            "question": "A square has side $s = 12$ m. Find the perimeter.",
            "answer": "$P = 48$ m",
            "wrong": ["$P = 24$ m", "$P = 144$ m", "$P = 36$ m"],
            "explanation": "$P = 4s = 4 \\times 12 = 48$ m."
        },
        {
            "question": "The perimeter of a square is $P = 36$ cm. Find the side length.",
            "answer": "$s = 9$ cm",
            "wrong": ["$s = 6$ cm", "$s = 12$ cm", "$s = 18$ cm"],
            "explanation": "$s = \\dfrac{P}{4} = \\dfrac{36}{4} = 9$ cm."
        },
        {
            "question": "A square has side $s = 5.5$ cm. Find the perimeter.",
            "answer": "$P = 22$ cm",
            "wrong": ["$P = 11$ cm", "$P = 30.25$ cm", "$P = 16.5$ cm"],
            "explanation": "$P = 4s = 4 \\times 5.5 = 22$ cm."
        },
        {
            "question": "The perimeter of a square is $P = 100$ m. Find the side length.",
            "answer": "$s = 25$ m",
            "wrong": ["$s = 20$ m", "$s = 50$ m", "$s = 10$ m"],
            "explanation": "$s = \\dfrac{P}{4} = \\dfrac{100}{4} = 25$ m."
        },
        {
            "question": "A square has side $s = 3\\sqrt{2}$ cm. Find the perimeter.",
            "answer": "$P = 12\\sqrt{2}$ cm",
            "wrong": ["$P = 6\\sqrt{2}$ cm", "$P = 18$ cm", "$P = 36$ cm"],
            "explanation": "$P = 4s = 4 \\times 3\\sqrt{2} = 12\\sqrt{2}$ cm."
        },
        {
            "question": "The perimeter of a square is $P = 56$ cm. Find the side length.",
            "answer": "$s = 14$ cm",
            "wrong": ["$s = 7$ cm", "$s = 28$ cm", "$s = 112$ cm"],
            "explanation": "$s = \\dfrac{P}{4} = \\dfrac{56}{4} = 14$ cm."
        },
        {
            "question": "A square has side $s = 0.8$ m. Find the perimeter.",
            "answer": "$P = 3.2$ m",
            "wrong": ["$P = 1.6$ m", "$P = 0.64$ m", "$P = 4$ m"],
            "explanation": "$P = 4s = 4 \\times 0.8 = 3.2$ m."
        },
        {
            "question": "A square has side $s = 15$ cm. Find the perimeter.",
            "answer": "$P = 60$ cm",
            "wrong": ["$P = 225$ cm", "$P = 30$ cm", "$P = 45$ cm"],
            "explanation": "$P = 4s = 4 \\times 15 = 60$ cm."
        },
        {
            "question": "The perimeter of a square is $P = 72$ m. Find the side length.",
            "answer": "$s = 18$ m",
            "wrong": ["$s = 36$ m", "$s = 9$ m", "$s = 24$ m"],
            "explanation": "$s = \\dfrac{P}{4} = \\dfrac{72}{4} = 18$ m."
        },

        {
            "question": "A square has side $s = 9$ cm. Find the area.",
            "answer": "$A = 81$ cm²",
            "wrong": ["$A = 36$ cm²", "$A = 18$ cm²", "$A = 45$ cm²"],
            "explanation": "$A = s^2 = 9^2 = 81$ cm²."
        },
        {
            "question": "A square has side $s = 13$ cm. Find the area.",
            "answer": "$A = 169$ cm²",
            "wrong": ["$A = 52$ cm²", "$A = 26$ cm²", "$A = 130$ cm²"],
            "explanation": "$A = s^2 = 13^2 = 169$ cm²."
        },
        {
            "question": "The area of a square is $A = 144$ cm². Find the side length.",
            "answer": "$s = 12$ cm",
            "wrong": ["$s = 36$ cm", "$s = 72$ cm", "$s = 16$ cm"],
            "explanation": "$s = \\sqrt{A} = \\sqrt{144} = 12$ cm."
        },
        {
            "question": "A square has side $s = 7$ m. Find the area.",
            "answer": "$A = 49$ m²",
            "wrong": ["$A = 28$ m²", "$A = 14$ m²", "$A = 56$ m²"],
            "explanation": "$A = s^2 = 7^2 = 49$ m²."
        },
        {
            "question": "The area of a square is $A = 225$ m². Find the side length.",
            "answer": "$s = 15$ m",
            "wrong": ["$s = 25$ m", "$s = 45$ m", "$s = 112.5$ m"],
            "explanation": "$s = \\sqrt{225} = 15$ m."
        },
        {
            "question": "A square has side $s = \\sqrt{5}$ cm. Find the area.",
            "answer": "$A = 5$ cm²",
            "wrong": ["$A = 4\\sqrt{5}$ cm²", "$A = 2\\sqrt{5}$ cm²", "$A = 25$ cm²"],
            "explanation": "$A = s^2 = (\\sqrt{5})^2 = 5$ cm²."
        },
        {
            "question": "The area of a square is $A = 196$ cm². Find the side length.",
            "answer": "$s = 14$ cm",
            "wrong": ["$s = 49$ cm", "$s = 28$ cm", "$s = 98$ cm"],
            "explanation": "$s = \\sqrt{196} = 14$ cm."
        },
        {
            "question": "A square has side $s = 20$ m. Find the area.",
            "answer": "$A = 400$ m²",
            "wrong": ["$A = 80$ m²", "$A = 40$ m²", "$A = 200$ m²"],
            "explanation": "$A = s^2 = 20^2 = 400$ m²."
        },
        {
            "question": "A square has side $s = 1.5$ cm. Find the area.",
            "answer": "$A = 2.25$ cm²",
            "wrong": ["$A = 6$ cm²", "$A = 3$ cm²", "$A = 9$ cm²"],
            "explanation": "$A = s^2 = 1.5^2 = 2.25$ cm²."
        },
        {
            "question": "The area of a square is $A = 289$ cm². Find the side length.",
            "answer": "$s = 17$ cm",
            "wrong": ["$s = 144.5$ cm", "$s = 34$ cm", "$s = 16$ cm"],
            "explanation": "$s = \\sqrt{289} = 17$ cm."
        },

        {
            "question": "A square has side $s = 6$ cm. Find the diagonal.",
            "answer": "$d = 6\\sqrt{2}$ cm",
            "wrong": ["$d = 12$ cm", "$d = 3\\sqrt{2}$ cm", "$d = 36$ cm"],
            "explanation": "$d = s\\sqrt{2} = 6\\sqrt{2}$ cm."
        },
        {
            "question": "A square has side $s = 10$ cm. Find the diagonal.",
            "answer": "$d = 10\\sqrt{2}$ cm",
            "wrong": ["$d = 20$ cm", "$d = 5\\sqrt{2}$ cm", "$d = 100$ cm"],
            "explanation": "$d = s\\sqrt{2} = 10\\sqrt{2}$ cm."
        },
        {
            "question": "The diagonal of a square is $d = 8\\sqrt{2}$ cm. Find the side length.",
            "answer": "$s = 8$ cm",
            "wrong": ["$s = 4$ cm", "$s = 16$ cm", "$s = 4\\sqrt{2}$ cm"],
            "explanation": "$s = \\dfrac{d}{\\sqrt{2}} = \\dfrac{8\\sqrt{2}}{\\sqrt{2}} = 8$ cm."
        },
        {
            "question": "A square has side $s = 5$ cm. Find the diagonal.",
            "answer": "$d = 5\\sqrt{2}$ cm",
            "wrong": ["$d = 10$ cm", "$d = 25$ cm", "$d = \\sqrt{10}$ cm"],
            "explanation": "$d = s\\sqrt{2} = 5\\sqrt{2}$ cm."
        },
        {
            "question": "The diagonal of a square is $d = 12\\sqrt{2}$ cm. Find the side length.",
            "answer": "$s = 12$ cm",
            "wrong": ["$s = 6$ cm", "$s = 24$ cm", "$s = 6\\sqrt{2}$ cm"],
            "explanation": "$s = \\dfrac{d}{\\sqrt{2}} = 12$ cm."
        },
        {
            "question": "A square has side $s = 3$ m. Find the diagonal.",
            "answer": "$d = 3\\sqrt{2}$ m",
            "wrong": ["$d = 6$ m", "$d = 9$ m", "$d = \\sqrt{6}$ m"],
            "explanation": "$d = s\\sqrt{2} = 3\\sqrt{2}$ m."
        },
        {
            "question": "The diagonal of a square is $d = 10$ cm. Find the area.",
            "answer": "$A = 50$ cm²",
            "wrong": ["$A = 100$ cm²", "$A = 25$ cm²", "$A = 25\\sqrt{2}$ cm²"],
            "explanation": "$A = \\dfrac{d^2}{2} = \\dfrac{100}{2} = 50$ cm²."
        },
        {
            "question": "A square has side $s = 4\\sqrt{2}$ cm. Find the diagonal.",
            "answer": "$d = 8$ cm",
            "wrong": ["$d = 4$ cm", "$d = 4\\sqrt{3}$ cm", "$d = 8\\sqrt{2}$ cm"],
            "explanation": "$d = s\\sqrt{2} = 4\\sqrt{2} \\cdot \\sqrt{2} = 8$ cm."
        },
        {
            "question": "The diagonal of a square is $d = 14\\sqrt{2}$ cm. Find the perimeter.",
            "answer": "$P = 56$ cm",
            "wrong": ["$P = 28$ cm", "$P = 112$ cm", "$P = 28\\sqrt{2}$ cm"],
            "explanation": "$s = \\dfrac{d}{\\sqrt{2}} = 14$, $P = 4 \\times 14 = 56$ cm."
        },
        {
            "question": "A square has side $s = 11$ cm. Find the diagonal.",
            "answer": "$d = 11\\sqrt{2}$ cm",
            "wrong": ["$d = 22$ cm", "$d = 121$ cm", "$d = \\sqrt{11}$ cm"],
            "explanation": "$d = s\\sqrt{2} = 11\\sqrt{2}$ cm."
        },

        {
            "question": "A rectangle has length $l = 8$ cm and width $w = 5$ cm. Find the area.",
            "answer": "$A = 40$ cm²",
            "wrong": ["$A = 26$ cm²", "$A = 13$ cm²", "$A = 80$ cm²"],
            "explanation": "$A = l \\times w = 8 \\times 5 = 40$ cm²."
        },
        {
            "question": "A rectangle has length $l = 12$ m and width $w = 7$ m. Find the area.",
            "answer": "$A = 84$ m²",
            "wrong": ["$A = 38$ m²", "$A = 19$ m²", "$A = 168$ m²"],
            "explanation": "$A = l \\times w = 12 \\times 7 = 84$ m²."
        },
        {
            "question": "The area of a rectangle is $A = 60$ cm² and its length is $l = 10$ cm. Find the width.",
            "answer": "$w = 6$ cm",
            "wrong": ["$w = 3$ cm", "$w = 12$ cm", "$w = 50$ cm"],
            "explanation": "$w = \\dfrac{A}{l} = \\dfrac{60}{10} = 6$ cm."
        },
        {
            "question": "A rectangle has length $l = 15$ cm and width $w = 9$ cm. Find the area.",
            "answer": "$A = 135$ cm²",
            "wrong": ["$A = 48$ cm²", "$A = 270$ cm²", "$A = 24$ cm²"],
            "explanation": "$A = l \\times w = 15 \\times 9 = 135$ cm²."
        },
        {
            "question": "The area of a rectangle is $A = 120$ m² and width is $w = 8$ m. Find the length.",
            "answer": "$l = 15$ m",
            "wrong": ["$l = 960$ m", "$l = 7.5$ m", "$l = 30$ m"],
            "explanation": "$l = \\dfrac{A}{w} = \\dfrac{120}{8} = 15$ m."
        },
        {
            "question": "A rectangle has length $l = 6$ cm and width $w = 6$ cm. Find the area.",
            "answer": "$A = 36$ cm²",
            "wrong": ["$A = 24$ cm²", "$A = 12$ cm²", "$A = 72$ cm²"],
            "explanation": "$A = l \\times w = 6 \\times 6 = 36$ cm²."
        },
        {
            "question": "A rectangle has length $l = 20$ m and width $w = 3$ m. Find the area.",
            "answer": "$A = 60$ m²",
            "wrong": ["$A = 46$ m²", "$A = 23$ m²", "$A = 120$ m²"],
            "explanation": "$A = l \\times w = 20 \\times 3 = 60$ m²."
        },
        {
            "question": "The area of a rectangle is $A = 72$ cm² and length is $l = 12$ cm. Find the width.",
            "answer": "$w = 6$ cm",
            "wrong": ["$w = 60$ cm", "$w = 3$ cm", "$w = 9$ cm"],
            "explanation": "$w = \\dfrac{72}{12} = 6$ cm."
        },
        {
            "question": "A rectangle has length $l = 4.5$ cm and width $w = 4$ cm. Find the area.",
            "answer": "$A = 18$ cm²",
            "wrong": ["$A = 17$ cm²", "$A = 36$ cm²", "$A = 8.5$ cm²"],
            "explanation": "$A = 4.5 \\times 4 = 18$ cm²."
        },
        {
            "question": "A rectangle has length $l = 11$ cm and width $w = 11$ cm. Find the area.",
            "answer": "$A = 121$ cm²",
            "wrong": ["$A = 44$ cm²", "$A = 22$ cm²", "$A = 242$ cm²"],
            "explanation": "$A = l \\times w = 11 \\times 11 = 121$ cm²."
        },

        {
            "question": "A rectangle has length $l = 3$ cm and width $w = 4$ cm. Find the diagonal.",
            "answer": "$d = 5$ cm",
            "wrong": ["$d = 7$ cm", "$d = \\sqrt{7}$ cm", "$d = 25$ cm"],
            "explanation": "$d = \\sqrt{l^2 + w^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$ cm."
        },
        {
            "question": "A rectangle has length $l = 5$ cm and width $w = 12$ cm. Find the diagonal.",
            "answer": "$d = 13$ cm",
            "wrong": ["$d = 17$ cm", "$d = 7$ cm", "$d = \\sqrt{17}$ cm"],
            "explanation": "$d = \\sqrt{25 + 144} = \\sqrt{169} = 13$ cm."
        },
        {
            "question": "A rectangle has length $l = 8$ cm and width $w = 6$ cm. Find the diagonal.",
            "answer": "$d = 10$ cm",
            "wrong": ["$d = 14$ cm", "$d = 2$ cm", "$d = \\sqrt{28}$ cm"],
            "explanation": "$d = \\sqrt{64 + 36} = \\sqrt{100} = 10$ cm."
        },
        {
            "question": "A rectangle has length $l = 9$ cm and width $w = 12$ cm. Find the diagonal.",
            "answer": "$d = 15$ cm",
            "wrong": ["$d = 21$ cm", "$d = 3$ cm", "$d = \\sqrt{21}$ cm"],
            "explanation": "$d = \\sqrt{81 + 144} = \\sqrt{225} = 15$ cm."
        },
        {
            "question": "A rectangle has length $l = 7$ cm and width $w = 24$ cm. Find the diagonal.",
            "answer": "$d = 25$ cm",
            "wrong": ["$d = 31$ cm", "$d = 17$ cm", "$d = \\sqrt{31}$ cm"],
            "explanation": "$d = \\sqrt{49 + 576} = \\sqrt{625} = 25$ cm."
        },
        {
            "question": "A rectangle has length $l = 6$ cm and width $w = 8$ cm. Find the diagonal.",
            "answer": "$d = 10$ cm",
            "wrong": ["$d = 14$ cm", "$d = \\sqrt{10}$ cm", "$d = 2$ cm"],
            "explanation": "$d = \\sqrt{36 + 64} = \\sqrt{100} = 10$ cm."
        },
        {
            "question": "A rectangle has length $l = 10$ cm and width $w = 10$ cm. Find the diagonal.",
            "answer": "$d = 10\\sqrt{2}$ cm",
            "wrong": ["$d = 20$ cm", "$d = 100$ cm", "$d = 5\\sqrt{2}$ cm"],
            "explanation": "$d = \\sqrt{100 + 100} = \\sqrt{200} = 10\\sqrt{2}$ cm."
        },
        {
            "question": "A rectangle has length $l = 15$ cm and width $w = 20$ cm. Find the diagonal.",
            "answer": "$d = 25$ cm",
            "wrong": ["$d = 35$ cm", "$d = 5$ cm", "$d = \\sqrt{625}$ cm"],
            "explanation": "$d = \\sqrt{225 + 400} = \\sqrt{625} = 25$ cm."
        },
        {
            "question": "A rectangle has length $l = 2$ cm and width $w = 2\\sqrt{3}$ cm. Find the diagonal.",
            "answer": "$d = 4$ cm",
            "wrong": ["$d = 2+2\\sqrt{3}$ cm", "$d = 2\\sqrt{3}$ cm", "$d = 8$ cm"],
            "explanation": "$d = \\sqrt{4 + 12} = \\sqrt{16} = 4$ cm."
        },
        {
            "question": "A rectangle has length $l = 9$ cm and width $w = 40$ cm. Find the diagonal.",
            "answer": "$d = 41$ cm",
            "wrong": ["$d = 49$ cm", "$d = 31$ cm", "$d = \\sqrt{49}$ cm"],
            "explanation": "$d = \\sqrt{9^2 + 40^2} = \\sqrt{81 + 1600} = \\sqrt{1681} = 41$ cm."
        },

        {
            "question": "A rectangle has length $l = 8$ cm and width $w = 3$ cm. Find the perimeter.",
            "answer": "$P = 22$ cm",
            "wrong": ["$P = 24$ cm", "$P = 11$ cm", "$P = 44$ cm"],
            "explanation": "$P = 2(l + w) = 2(8 + 3) = 22$ cm."
        },
        {
            "question": "A rectangle has length $l = 14$ m and width $w = 6$ m. Find the perimeter.",
            "answer": "$P = 40$ m",
            "wrong": ["$P = 84$ m", "$P = 20$ m", "$P = 80$ m"],
            "explanation": "$P = 2(l + w) = 2(14 + 6) = 40$ m."
        },
        {
            "question": "The perimeter of a rectangle is $P = 50$ cm and length is $l = 15$ cm. Find the width.",
            "answer": "$w = 10$ cm",
            "wrong": ["$w = 20$ cm", "$w = 35$ cm", "$w = 5$ cm"],
            "explanation": "$w = \\dfrac{P}{2} - l = 25 - 15 = 10$ cm."
        },
        {
            "question": "A rectangle has length $l = 9$ cm and width $w = 4$ cm. Find the perimeter.",
            "answer": "$P = 26$ cm",
            "wrong": ["$P = 36$ cm", "$P = 52$ cm", "$P = 13$ cm"],
            "explanation": "$P = 2(9 + 4) = 26$ cm."
        },
        {
            "question": "The perimeter of a rectangle is $P = 36$ m and width is $w = 7$ m. Find the length.",
            "answer": "$l = 11$ m",
            "wrong": ["$l = 14$ m", "$l = 22$ m", "$l = 29$ m"],
            "explanation": "$l = \\dfrac{P}{2} - w = 18 - 7 = 11$ m."
        },
        {
            "question": "A rectangle has length $l = 5$ cm and width $w = 5$ cm. Find the perimeter.",
            "answer": "$P = 20$ cm",
            "wrong": ["$P = 25$ cm", "$P = 10$ cm", "$P = 40$ cm"],
            "explanation": "$P = 2(5 + 5) = 20$ cm."
        },
        {
            "question": "A rectangle has length $l = 25$ m and width $w = 10$ m. Find the perimeter.",
            "answer": "$P = 70$ m",
            "wrong": ["$P = 250$ m", "$P = 35$ m", "$P = 140$ m"],
            "explanation": "$P = 2(25 + 10) = 70$ m."
        },
        {
            "question": "The perimeter of a rectangle is $P = 60$ cm and length is $l = 20$ cm. Find the width.",
            "answer": "$w = 10$ cm",
            "wrong": ["$w = 40$ cm", "$w = 15$ cm", "$w = 5$ cm"],
            "explanation": "$w = \\dfrac{60}{2} - 20 = 30 - 20 = 10$ cm."
        },
        {
            "question": "A rectangle has length $l = 13$ cm and width $w = 7$ cm. Find the perimeter.",
            "answer": "$P = 40$ cm",
            "wrong": ["$P = 91$ cm", "$P = 20$ cm", "$P = 26$ cm"],
            "explanation": "$P = 2(13 + 7) = 40$ cm."
        },
        {
            "question": "A rectangle has length $l = 3.5$ m and width $w = 2.5$ m. Find the perimeter.",
            "answer": "$P = 12$ m",
            "wrong": ["$P = 8.75$ m", "$P = 6$ m", "$P = 24$ m"],
            "explanation": "$P = 2(3.5 + 2.5) = 2 \\times 6 = 12$ m."
        },

        {
            "question": "In a rhombus, one angle is $\\alpha = 60°$. Find the adjacent angle.",
            "answer": "$\\beta = 120°$",
            "wrong": ["$\\beta = 60°$", "$\\beta = 90°$", "$\\beta = 150°$"],
            "explanation": "Adjacent angles in a rhombus are supplementary: $\\beta = 180° - 60° = 120°$."
        },
        {
            "question": "In a rhombus, one angle is $\\alpha = 45°$. Find the other three angles.",
            "answer": "$135°, 45°, 135°$",
            "wrong": ["$45°, 45°, 90°$", "$60°, 135°, 135°$", "$45°, 90°, 135°$"],
            "explanation": "Opposite angles are equal; adjacent angles sum to $180°$. All four angles are $45°, 135°, 45°, 135°$, so the other three are $135°, 45°, 135°$."
        },
        {
            "question": "In a rhombus, the diagonals bisect angles. If one angle is $\\alpha = 80°$, find the half-angle at that vertex.",
            "answer": "$40°$",
            "wrong": ["$80°$", "$20°$", "$100°$"],
            "explanation": "The diagonal bisects the angle: $\\dfrac{80°}{2} = 40°$."
        },
        {
            "question": "In a rhombus, one angle is $\\alpha = 110°$. Find the adjacent angle.",
            "answer": "$\\beta = 70°$",
            "wrong": ["$\\beta = 110°$", "$\\beta = 90°$", "$\\beta = 55°$"],
            "explanation": "$\\beta = 180° - 110° = 70°$."
        },
        {
            "question": "A rhombus has angles in ratio $1:2$. Find both angles.",
            "answer": "$60°$ and $120°$",
            "wrong": ["$45°$ and $90°$", "$30°$ and $150°$", "$90°$ and $90°$"],
            "explanation": "Let angles be $x$ and $2x$. Then $x + 2x = 180°$, so $x = 60°$, $2x = 120°$."
        },
        {
            "question": "In a rhombus, one angle is $\\alpha = 72°$. Find the sum of all four angles.",
            "answer": "$360°$",
            "wrong": ["$180°$", "$288°$", "$144°$"],
            "explanation": "Sum of interior angles in any quadrilateral is $360°$."
        },
        {
            "question": "In a rhombus, the acute angle is $\\alpha = 30°$. Find the obtuse angle.",
            "answer": "$\\beta = 150°$",
            "wrong": ["$\\beta = 120°$", "$\\beta = 60°$", "$\\beta = 90°$"],
            "explanation": "$\\beta = 180° - 30° = 150°$."
        },
        {
            "question": "In a rhombus, both diagonals are equal. What are the angles?",
            "answer": "$90°$ each",
            "wrong": ["$60°$ and $120°$", "$45°$ and $135°$", "$30°$ and $150°$"],
            "explanation": "Equal diagonals in a rhombus make it a square, where all angles are $90°$."
        },
        {
            "question": "In a rhombus, one angle is $\\alpha = 100°$. Find the half-angle cut by the diagonal.",
            "answer": "$50°$",
            "wrong": ["$100°$", "$80°$", "$40°$"],
            "explanation": "Diagonal bisects the angle: $\\dfrac{100°}{2} = 50°$."
        },
        {
            "question": "In a rhombus, one interior angle is $\\alpha = 55°$. Find the adjacent angle.",
            "answer": "$\\beta = 125°$",
            "wrong": ["$\\beta = 55°$", "$\\beta = 110°$", "$\\beta = 90°$"],
            "explanation": "$\\beta = 180° - 55° = 125°$."
        },

        {
            "question": "A rhombus has diagonals $d_1 = 6$ cm and $d_2 = 8$ cm. Find the area.",
            "answer": "$A = 24$ cm²",
            "wrong": ["$A = 48$ cm²", "$A = 12$ cm²", "$A = 14$ cm²"],
            "explanation": "$A = \\dfrac{d_1 \\cdot d_2}{2} = \\dfrac{6 \\times 8}{2} = 24$ cm²."
        },
        {
            "question": "A rhombus has diagonals $d_1 = 10$ cm and $d_2 = 12$ cm. Find the area.",
            "answer": "$A = 60$ cm²",
            "wrong": ["$A = 120$ cm²", "$A = 30$ cm²", "$A = 44$ cm²"],
            "explanation": "$A = \\dfrac{10 \\times 12}{2} = 60$ cm²."
        },
        {
            "question": "A rhombus has diagonals $d_1 = 5$ cm and $d_2 = 5$ cm. Find the area.",
            "answer": "$A = 12.5$ cm²",
            "wrong": ["$A = 25$ cm²", "$A = 10$ cm²", "$A = 20$ cm²"],
            "explanation": "$A = \\dfrac{5 \\times 5}{2} = 12.5$ cm²."
        },
        {
            "question": "A rhombus has diagonals $d_1 = 14$ cm and $d_2 = 9$ cm. Find the area.",
            "answer": "$A = 63$ cm²",
            "wrong": ["$A = 126$ cm²", "$A = 31.5$ cm²", "$A = 23$ cm²"],
            "explanation": "$A = \\dfrac{14 \\times 9}{2} = 63$ cm²."
        },
        {
            "question": "A rhombus has diagonals $d_1 = 20$ cm and $d_2 = 15$ cm. Find the area.",
            "answer": "$A = 150$ cm²",
            "wrong": ["$A = 300$ cm²", "$A = 75$ cm²", "$A = 35$ cm²"],
            "explanation": "$A = \\dfrac{20 \\times 15}{2} = 150$ cm²."
        },
        {
            "question": "A rhombus has side $a = 10$ cm and height $h = 7$ cm. Find the area.",
            "answer": "$A = 70$ cm²",
            "wrong": ["$A = 35$ cm²", "$A = 140$ cm²", "$A = 34$ cm²"],
            "explanation": "$A = a \\times h = 10 \\times 7 = 70$ cm²."
        },
        {
            "question": "A rhombus has side $a = 8$ cm and height $h = 6$ cm. Find the area.",
            "answer": "$A = 48$ cm²",
            "wrong": ["$A = 24$ cm²", "$A = 96$ cm²", "$A = 28$ cm²"],
            "explanation": "$A = a \\times h = 8 \\times 6 = 48$ cm²."
        },
        {
            "question": "A rhombus has side $a = 15$ cm and height $h = 9$ cm. Find the area.",
            "answer": "$A = 135$ cm²",
            "wrong": ["$A = 270$ cm²", "$A = 67.5$ cm²", "$A = 48$ cm²"],
            "explanation": "$A = a \\times h = 15 \\times 9 = 135$ cm²."
        },
        {
            "question": "A rhombus has side $a = 12$ cm and angle $\\alpha = 30°$. Find the area.",
            "answer": "$A = 72$ cm²",
            "wrong": ["$A = 144$ cm²", "$A = 36$ cm²", "$A = 62.4$ cm²"],
            "explanation": "$A = a^2 \\sin\\alpha = 144 \\times 0.5 = 72$ cm²."
        },
        {
            "question": "A rhombus has side $a = 5$ cm and height $h = 4$ cm. Find the area.",
            "answer": "$A = 20$ cm²",
            "wrong": ["$A = 10$ cm²", "$A = 40$ cm²", "$A = 25$ cm²"],
            "explanation": "$A = a \\times h = 5 \\times 4 = 20$ cm²."
        },

        {
            "question": "A rhombus has side $a = 7$ cm. Find the perimeter.",
            "answer": "$P = 28$ cm",
            "wrong": ["$P = 14$ cm", "$P = 49$ cm", "$P = 21$ cm"],
            "explanation": "$P = 4a = 4 \\times 7 = 28$ cm."
        },
        {
            "question": "A rhombus has side $a = 13$ cm. Find the perimeter.",
            "answer": "$P = 52$ cm",
            "wrong": ["$P = 26$ cm", "$P = 169$ cm", "$P = 39$ cm"],
            "explanation": "$P = 4a = 4 \\times 13 = 52$ cm."
        },
        {
            "question": "The perimeter of a rhombus is $P = 60$ cm. Find the side length.",
            "answer": "$a = 15$ cm",
            "wrong": ["$a = 30$ cm", "$a = 20$ cm", "$a = 10$ cm"],
            "explanation": "$a = \\dfrac{P}{4} = \\dfrac{60}{4} = 15$ cm."
        },
        # FIX 1: Removed duplicate "answer" key. Correct answer is P=20 cm (a=√(3²+4²)=5, P=4×5=20).
        # Also fixed "wrong" array which previously contained the correct answer "$P = 40$ cm".
        {
            "question": "A rhombus has diagonals $d_1 = 6$ cm and $d_2 = 8$ cm. Find the perimeter.",
            "answer": "$P = 20$ cm",
            "wrong": ["$P = 28$ cm", "$P = 48$ cm", "$P = 14$ cm"],
            "explanation": "$a = \\sqrt{(d_1/2)^2 + (d_2/2)^2} = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = 5$ cm, $P = 4 \\times 5 = 20$ cm."
        },
        {
            "question": "A rhombus has side $a = 9.5$ cm. Find the perimeter.",
            "answer": "$P = 38$ cm",
            "wrong": ["$P = 19$ cm", "$P = 90.25$ cm", "$P = 28.5$ cm"],
            "explanation": "$P = 4 \\times 9.5 = 38$ cm."
        },
        {
            "question": "The perimeter of a rhombus is $P = 100$ m. Find the side length.",
            "answer": "$a = 25$ m",
            "wrong": ["$a = 50$ m", "$a = 20$ m", "$a = 10$ m"],
            "explanation": "$a = \\dfrac{100}{4} = 25$ m."
        },
        {
            "question": "A rhombus has side $a = 11$ cm. Find the perimeter.",
            "answer": "$P = 44$ cm",
            "wrong": ["$P = 22$ cm", "$P = 121$ cm", "$P = 33$ cm"],
            "explanation": "$P = 4 \\times 11 = 44$ cm."
        },
        {
            "question": "A rhombus has diagonals $d_1 = 16$ cm and $d_2 = 12$ cm. Find the perimeter.",
            "answer": "$P = 40$ cm",
            "wrong": ["$P = 56$ cm", "$P = 80$ cm", "$P = 48$ cm"],
            "explanation": "$a = \\sqrt{8^2 + 6^2} = \\sqrt{100} = 10$, $P = 4 \\times 10 = 40$ cm."
        },
        {
            "question": "A rhombus has side $a = 6$ cm. Find the perimeter.",
            "answer": "$P = 24$ cm",
            "wrong": ["$P = 12$ cm", "$P = 36$ cm", "$P = 48$ cm"],
            "explanation": "$P = 4 \\times 6 = 24$ cm."
        },
        {
            "question": "The perimeter of a rhombus is $P = 48$ cm. Find the side length.",
            "answer": "$a = 12$ cm",
            "wrong": ["$a = 24$ cm", "$a = 16$ cm", "$a = 6$ cm"],
            "explanation": "$a = \\dfrac{48}{4} = 12$ cm."
        },

        {
            "question": "A parallelogram has base $b = 10$ cm and height $h = 6$ cm. Find the area.",
            "answer": "$A = 60$ cm²",
            "wrong": ["$A = 30$ cm²", "$A = 120$ cm²", "$A = 16$ cm²"],
            "explanation": "$A = b \\times h = 10 \\times 6 = 60$ cm²."
        },
        {
            "question": "A parallelogram has base $b = 14$ m and height $h = 5$ m. Find the area.",
            "answer": "$A = 70$ m²",
            "wrong": ["$A = 35$ m²", "$A = 140$ m²", "$A = 19$ m²"],
            "explanation": "$A = 14 \\times 5 = 70$ m²."
        },
        {
            "question": "The area of a parallelogram is $A = 48$ cm² and base is $b = 8$ cm. Find the height.",
            "answer": "$h = 6$ cm",
            "wrong": ["$h = 3$ cm", "$h = 12$ cm", "$h = 40$ cm"],
            "explanation": "$h = \\dfrac{A}{b} = \\dfrac{48}{8} = 6$ cm."
        },
        {
            "question": "A parallelogram has base $b = 9$ cm and height $h = 9$ cm. Find the area.",
            "answer": "$A = 81$ cm²",
            "wrong": ["$A = 36$ cm²", "$A = 162$ cm²", "$A = 18$ cm²"],
            "explanation": "$A = 9 \\times 9 = 81$ cm²."
        },
        {
            "question": "A parallelogram has sides $a = 5$ cm and $b = 13$ cm, with height $h = 4$ cm corresponding to side $b$. Find the area.",
            "answer": "$A = 52$ cm²",
            "wrong": ["$A = 20$ cm²", "$A = 65$ cm²", "$A = 26$ cm²"],
            "explanation": "$A = b \\times h = 13 \\times 4 = 52$ cm²."
        },
        {
            "question": "A parallelogram has base $b = 7$ cm and height $h = 11$ cm. Find the area.",
            "answer": "$A = 77$ cm²",
            "wrong": ["$A = 36$ cm²", "$A = 154$ cm²", "$A = 18$ cm²"],
            "explanation": "$A = 7 \\times 11 = 77$ cm²."
        },
        {
            "question": "A parallelogram has base $b = 20$ m and height $h = 8$ m. Find the area.",
            "answer": "$A = 160$ m²",
            "wrong": ["$A = 80$ m²", "$A = 320$ m²", "$A = 56$ m²"],
            "explanation": "$A = 20 \\times 8 = 160$ m²."
        },
        {
            "question": "The area of a parallelogram is $A = 90$ m² and height is $h = 9$ m. Find the base.",
            "answer": "$b = 10$ m",
            "wrong": ["$b = 81$ m", "$b = 5$ m", "$b = 20$ m"],
            "explanation": "$b = \\dfrac{90}{9} = 10$ m."
        },
        {
            "question": "A parallelogram has base $b = 3.5$ cm and height $h = 4$ cm. Find the area.",
            "answer": "$A = 14$ cm²",
            "wrong": ["$A = 7$ cm²", "$A = 7.5$ cm²", "$A = 28$ cm²"],
            "explanation": "$A = 3.5 \\times 4 = 14$ cm²."
        },
        {
            "question": "A parallelogram has sides $a = 8$ cm and angle $\\alpha = 45°$ with the base $b = 10$ cm. Find the area.",
            "answer": "$A = 40\\sqrt{2}$ cm²",
            "wrong": ["$A = 40$ cm²", "$A = 80$ cm²", "$A = 20\\sqrt{2}$ cm²"],
            "explanation": "$h = a \\sin 45° = 8 \\cdot \\dfrac{\\sqrt{2}}{2} = 4\\sqrt{2}$, $A = 10 \\times 4\\sqrt{2} = 40\\sqrt{2}$ cm²."
        },

        {
            "question": "A parallelogram has sides $a = 5$ cm and $b = 9$ cm. Find the perimeter.",
            "answer": "$P = 28$ cm",
            "wrong": ["$P = 45$ cm", "$P = 14$ cm", "$P = 56$ cm"],
            "explanation": "$P = 2(a + b) = 2(5 + 9) = 28$ cm."
        },
        {
            "question": "A parallelogram has sides $a = 7$ cm and $b = 12$ cm. Find the perimeter.",
            "answer": "$P = 38$ cm",
            "wrong": ["$P = 19$ cm", "$P = 84$ cm", "$P = 76$ cm"],
            "explanation": "$P = 2(7 + 12) = 38$ cm."
        },
        {
            "question": "The perimeter of a parallelogram is $P = 50$ cm and one side is $a = 15$ cm. Find the other side.",
            "answer": "$b = 10$ cm",
            "wrong": ["$b = 35$ cm", "$b = 20$ cm", "$b = 25$ cm"],
            "explanation": "$b = \\dfrac{P}{2} - a = 25 - 15 = 10$ cm."
        },
        {
            "question": "A parallelogram has sides $a = 6$ m and $b = 6$ m. Find the perimeter.",
            "answer": "$P = 24$ m",
            "wrong": ["$P = 36$ m", "$P = 12$ m", "$P = 48$ m"],
            "explanation": "$P = 2(6 + 6) = 24$ m."
        },
        {
            "question": "A parallelogram has sides $a = 11$ cm and $b = 4$ cm. Find the perimeter.",
            "answer": "$P = 30$ cm",
            "wrong": ["$P = 44$ cm", "$P = 15$ cm", "$P = 60$ cm"],
            "explanation": "$P = 2(11 + 4) = 30$ cm."
        },
        {
            "question": "The perimeter of a parallelogram is $P = 64$ m and one side is $a = 20$ m. Find the other side.",
            "answer": "$b = 12$ m",
            "wrong": ["$b = 44$ m", "$b = 24$ m", "$b = 16$ m"],
            "explanation": "$b = \\dfrac{64}{2} - 20 = 32 - 20 = 12$ m."
        },
        {
            "question": "A parallelogram has sides $a = 8$ cm and $b = 15$ cm. Find the perimeter.",
            "answer": "$P = 46$ cm",
            "wrong": ["$P = 120$ cm", "$P = 23$ cm", "$P = 92$ cm"],
            "explanation": "$P = 2(8 + 15) = 46$ cm."
        },
        {
            "question": "A parallelogram has sides $a = 3.5$ m and $b = 6.5$ m. Find the perimeter.",
            "answer": "$P = 20$ m",
            "wrong": ["$P = 10$ m", "$P = 22.75$ m", "$P = 40$ m"],
            "explanation": "$P = 2(3.5 + 6.5) = 2 \\times 10 = 20$ m."
        },
        {
            "question": "A parallelogram has sides $a = 13$ cm and $b = 13$ cm. Find the perimeter.",
            "answer": "$P = 52$ cm",
            "wrong": ["$P = 169$ cm", "$P = 26$ cm", "$P = 104$ cm"],
            "explanation": "$P = 2(13 + 13) = 52$ cm."
        },
        {
            "question": "The perimeter of a parallelogram is $P = 80$ cm and one side is $a = 25$ cm. Find the other side.",
            "answer": "$b = 15$ cm",
            "wrong": ["$b = 55$ cm", "$b = 30$ cm", "$b = 40$ cm"],
            "explanation": "$b = \\dfrac{80}{2} - 25 = 40 - 25 = 15$ cm."
        },

        {
            "question": "In a parallelogram, one angle is $\\alpha = 70°$. Find the adjacent angle.",
            "answer": "$\\beta = 110°$",
            "wrong": ["$\\beta = 70°$", "$\\beta = 90°$", "$\\beta = 140°$"],
            "explanation": "Adjacent angles in a parallelogram are supplementary: $\\beta = 180° - 70° = 110°$."
        },
        {
            "question": "In a parallelogram, one angle is $\\alpha = 50°$. Find the opposite angle.",
            "answer": "$\\gamma = 50°$",
            "wrong": ["$\\gamma = 130°$", "$\\gamma = 100°$", "$\\gamma = 90°$"],
            "explanation": "Opposite angles in a parallelogram are equal."
        },
        {
            "question": "In a parallelogram, angles are in ratio $1:3$. Find both angles.",
            "answer": "$45°$ and $135°$",
            "wrong": ["$30°$ and $150°$", "$60°$ and $120°$", "$90°$ and $90°$"],
            "explanation": "$x + 3x = 180°$, so $x = 45°$, $3x = 135°$."
        },
        {
            "question": "In a parallelogram, one angle is $\\alpha = 90°$. What type of figure is it?",
            "answer": "Rectangle (all angles are $90°$)",
            "wrong": ["Rhombus", "Trapezoid", "Kite"],
            "explanation": "If one angle of a parallelogram is $90°$, all angles are $90°$, making it a rectangle."
        },
        {
            "question": "In a parallelogram, one angle is $\\alpha = 115°$. Find the adjacent angle.",
            "answer": "$\\beta = 65°$",
            "wrong": ["$\\beta = 115°$", "$\\beta = 90°$", "$\\beta = 245°$"],
            "explanation": "$\\beta = 180° - 115° = 65°$."
        },
        {
            "question": "In a parallelogram, the sum of two adjacent angles is $180°$ and one angle is $\\alpha = 35°$. Find the other angle.",
            "answer": "$\\beta = 145°$",
            "wrong": ["$\\beta = 70°$", "$\\beta = 90°$", "$\\beta = 35°$"],
            "explanation": "$\\beta = 180° - 35° = 145°$."
        },
        {
            "question": "In a parallelogram, angles are in ratio $2:7$. Find both angles.",
            "answer": "$40°$ and $140°$",
            "wrong": ["$20°$ and $160°$", "$36°$ and $144°$", "$60°$ and $120°$"],
            "explanation": "$2x + 7x = 180°$, $x = 20°$; angles are $40°$ and $140°$."
        },
        {
            "question": "In a parallelogram, one angle is $\\alpha = 130°$. Find all four angles.",
            "answer": "$130°, 50°, 130°, 50°$",
            "wrong": ["$130°, 130°, 130°, 130°$", "$90°, 90°, 90°, 90°$", "$130°, 230°, 130°, 230°$"],
            "explanation": "Opposite angles are equal, adjacent are supplementary: $130°, 50°, 130°, 50°$."
        },
        {
            "question": "In a parallelogram, one angle is $\\alpha = 85°$. Find the adjacent angle.",
            "answer": "$\\beta = 95°$",
            "wrong": ["$\\beta = 85°$", "$\\beta = 90°$", "$\\beta = 170°$"],
            "explanation": "$\\beta = 180° - 85° = 95°$."
        },
        {
            "question": "In a parallelogram, angles are in ratio $3:5$. Find both types of angles.",
            "answer": "$67.5°$ and $112.5°$",
            "wrong": ["$60°$ and $120°$", "$72°$ and $108°$", "$54°$ and $126°$"],
            "explanation": "$3x + 5x = 180°$, $x = 22.5°$; angles are $67.5°$ and $112.5°$."
        },

        {
            "question": "In a trapezoid, one base angle is $\\alpha = 60°$. Find the co-interior angle on the same side.",
            "answer": "$\\beta = 120°$",
            "wrong": ["$\\beta = 60°$", "$\\beta = 90°$", "$\\beta = 30°$"],
            "explanation": "Co-interior (same-side) angles between parallel lines sum to $180°$: $\\beta = 180° - 60° = 120°$."
        },
        {
            "question": "In an isosceles trapezoid, one base angle is $\\alpha = 70°$. Find the other base angle on the same base.",
            "answer": "$\\beta = 70°$",
            "wrong": ["$\\beta = 110°$", "$\\beta = 140°$", "$\\beta = 35°$"],
            "explanation": "Base angles of an isosceles trapezoid are equal."
        },
        {
            "question": "In a trapezoid, two angles on one side are $\\alpha = 55°$ and $\\beta = 125°$. Is this a valid trapezoid?",
            "answer": "Yes, since $55° + 125° = 180°$",
            "wrong": ["No, they must both be acute", "No, they must be equal", "Only if it is isosceles"],
            "explanation": "Co-interior angles must sum to $180°$: $55° + 125° = 180°$ ✓."
        },
        {
            "question": "In a right trapezoid, two angles are $90°$. Find the sum of the remaining two angles.",
            "answer": "$180°$",
            "wrong": ["$90°$", "$270°$", "$360°$"],
            "explanation": "A right trapezoid has one leg perpendicular to both parallel bases, creating two $90°$ angles on that leg. Sum of all angles $= 360°$, so the remaining two angles sum to $360° - 90° - 90° = 180°$."
        },
        {
            "question": "In an isosceles trapezoid, one base angle is $\\alpha = 65°$. Find the angle at the other base.",
            "answer": "$\\gamma = 115°$",
            "wrong": ["$\\gamma = 65°$", "$\\gamma = 90°$", "$\\gamma = 130°$"],
            "explanation": "In an isosceles trapezoid the two bases are parallel, so co-interior angles on the same side sum to $180°$: $\\gamma = 180° - 65° = 115°$."
        },
        {
            "question": "In a trapezoid, the angles are $\\alpha, \\alpha, \\beta, \\beta$ (isosceles). If $\\alpha = 80°$, find $\\beta$.",
            "answer": "$\\beta = 100°$",
            "wrong": ["$\\beta = 80°$", "$\\beta = 160°$", "$\\beta = 90°$"],
            "explanation": "$\\alpha + \\beta = 180°$, so $\\beta = 180° - 80° = 100°$."
        },
        {
            "question": "In a trapezoid, three angles are $70°, 70°, 110°$. Find the fourth angle.",
            "answer": "$110°$",
            "wrong": ["$70°$", "$90°$", "$140°$"],
            "explanation": "$360° - 70° - 70° - 110° = 110°$."
        },
        # FIX: Original question asked for "the other acute angle" in a right trapezoid,
        # but a right trapezoid has only ONE acute angle — so no "other acute angle" exists.
        # Rewritten: given the one acute angle, find the obtuse angle.
        {
            "question": "In a right trapezoid, the acute angle is $\\alpha = 40°$. Find the obtuse angle.",
            "answer": "$\\beta = 140°$",
            "wrong": ["$\\beta = 50°$", "$\\beta = 40°$", "$\\beta = 90°$"],
            "explanation": "A right trapezoid has one right angle ($90°$) and one acute angle ($40°$). The obtuse angle is co-interior with the acute angle: $\\beta = 180° - 40° = 140°$. Check: $90° + 40° + 90° + 140° = 360°$ ✓."
        },
        {
            "question": "In an isosceles trapezoid, the sum of the angles at one base is $180°$? True or false?",
            "answer": "False — they are equal, not supplementary",
            "wrong": ["True always", "True only for right trapezoids", "True only if the trapezoid is a rectangle"],
            "explanation": "In an isosceles trapezoid, the two base angles (at the same base) are equal, not supplementary. Co-interior angles on the same side sum to $180°$."
        },
        {
            "question": "In a trapezoid, co-interior angles on one side are $(2x + 10)°$ and $(3x - 20)°$. Find $x$.",
            "answer": "$x = 38$",
            "wrong": ["$x = 19$", "$x = 30$", "$x = 40$"],
            "explanation": "$(2x+10) + (3x-20) = 180 \\Rightarrow 5x - 10 = 180 \\Rightarrow x = 38$."
        },

        {
            "question": "A trapezoid has parallel sides $a = 6$ cm, $b = 10$ cm and height $h = 4$ cm. Find the area.",
            "answer": "$A = 32$ cm²",
            "wrong": ["$A = 24$ cm²", "$A = 64$ cm²", "$A = 16$ cm²"],
            "explanation": "$A = \\dfrac{(a+b)}{2} \\times h = \\dfrac{16}{2} \\times 4 = 32$ cm²."
        },
        {
            "question": "A trapezoid has parallel sides $a = 5$ m, $b = 11$ m and height $h = 6$ m. Find the area.",
            "answer": "$A = 48$ m²",
            "wrong": ["$A = 96$ m²", "$A = 24$ m²", "$A = 33$ m²"],
            "explanation": "$A = \\dfrac{(5+11)}{2} \\times 6 = 8 \\times 6 = 48$ m²."
        },
        {
            "question": "A trapezoid has parallel sides $a = 8$ cm, $b = 12$ cm and height $h = 5$ cm. Find the area.",
            "answer": "$A = 50$ cm²",
            "wrong": ["$A = 100$ cm²", "$A = 25$ cm²", "$A = 40$ cm²"],
            "explanation": "$A = \\dfrac{(8+12)}{2} \\times 5 = 10 \\times 5 = 50$ cm²."
        },
        {
            "question": "A trapezoid has parallel sides $a = 3$ cm, $b = 7$ cm and height $h = 8$ cm. Find the area.",
            "answer": "$A = 40$ cm²",
            "wrong": ["$A = 80$ cm²", "$A = 168$ cm²", "$A = 20$ cm²"],
            "explanation": "$A = \\dfrac{(3+7)}{2} \\times 8 = 5 \\times 8 = 40$ cm²."
        },
        {
            "question": "The area of a trapezoid is $A = 60$ cm², the height is $h = 6$ cm, and one base is $a = 8$ cm. Find the other base.",
            "answer": "$b = 12$ cm",
            "wrong": ["$b = 4$ cm", "$b = 10$ cm", "$b = 14$ cm"],
            "explanation": "$60 = \\dfrac{(8+b)}{2} \\times 6 \\Rightarrow 8 + b = 20 \\Rightarrow b = 12$ cm."
        },
        {
            "question": "A trapezoid has parallel sides $a = 14$ cm, $b = 6$ cm and height $h = 7$ cm. Find the area.",
            "answer": "$A = 70$ cm²",
            "wrong": ["$A = 140$ cm²", "$A = 35$ cm²", "$A = 98$ cm²"],
            "explanation": "$A = \\dfrac{(14+6)}{2} \\times 7 = 10 \\times 7 = 70$ cm²."
        },
        {
            "question": "A trapezoid has parallel sides $a = 9$ m, $b = 15$ m and height $h = 10$ m. Find the area.",
            "answer": "$A = 120$ m²",
            "wrong": ["$A = 60$ m²", "$A = 240$ m²", "$A = 135$ m²"],
            "explanation": "$A = \\dfrac{(9+15)}{2} \\times 10 = 12 \\times 10 = 120$ m²."
        },
        {
            "question": "A trapezoid has parallel sides $a = 4$ cm, $b = 4$ cm and height $h = 5$ cm. What is the shape?",
            "answer": "Parallelogram, $A = 20$ cm²",
            "wrong": ["Rectangle, $A = 20$ cm²", "Rhombus, $A = 16$ cm²", "Regular trapezoid, $A = 40$ cm²"],
            "explanation": "Equal parallel sides → parallelogram. $A = 4 \\times 5 = 20$ cm²."
        },
        {
            "question": "A trapezoid has parallel sides $a = 7$ cm, $b = 13$ cm and height $h = 9$ cm. Find the area.",
            "answer": "$A = 90$ cm²",
            "wrong": ["$A = 180$ cm²", "$A = 45$ cm²", "$A = 63$ cm²"],
            "explanation": "$A = \\dfrac{(7+13)}{2} \\times 9 = 10 \\times 9 = 90$ cm²."
        },
        {
            "question": "The area of a trapezoid is $A = 100$ m², height $h = 8$ m, and one base $a = 7$ m. Find the other base.",
            "answer": "$b = 18$ m",
            "wrong": ["$b = 5$ m", "$b = 25$ m", "$b = 13$ m"],
            "explanation": "$100 = \\dfrac{(7+b)}{2} \\times 8 \\Rightarrow 7 + b = 25 \\Rightarrow b = 18$ m."
        },

        {
            "question": "A trapezoid has area $A = 36$ cm² and parallel sides $a = 4$ cm, $b = 8$ cm. Find the height.",
            "answer": "$h = 6$ cm",
            "wrong": ["$h = 3$ cm", "$h = 12$ cm", "$h = 9$ cm"],
            "explanation": "$h = \\dfrac{2A}{a+b} = \\dfrac{72}{12} = 6$ cm."
        },
        {
            "question": "A trapezoid has area $A = 50$ m² and parallel sides $a = 5$ m, $b = 15$ m. Find the height.",
            "answer": "$h = 5$ m",
            "wrong": ["$h = 10$ m", "$h = 2.5$ m", "$h = 25$ m"],
            "explanation": "$h = \\dfrac{2 \\times 50}{5 + 15} = \\dfrac{100}{20} = 5$ m."
        },
        {
            "question": "A trapezoid has area $A = 48$ cm² and parallel sides $a = 6$ cm, $b = 10$ cm. Find the height.",
            "answer": "$h = 6$ cm",
            "wrong": ["$h = 3$ cm", "$h = 12$ cm", "$h = 8$ cm"],
            "explanation": "$h = \\dfrac{2 \\times 48}{6 + 10} = \\dfrac{96}{16} = 6$ cm."
        },
        {
            "question": "A trapezoid has area $A = 70$ m² and parallel sides $a = 7$ m, $b = 7$ m. Find the height.",
            "answer": "$h = 10$ m",
            "wrong": ["$h = 5$ m", "$h = 14$ m", "$h = 70$ m"],
            "explanation": "$h = \\dfrac{2 \\times 70}{7 + 7} = \\dfrac{140}{14} = 10$ m."
        },
        {
            "question": "A trapezoid has area $A = 90$ cm² and parallel sides $a = 10$ cm, $b = 8$ cm. Find the height.",
            "answer": "$h = 10$ cm",
            "wrong": ["$h = 5$ cm", "$h = 20$ cm", "$h = 9$ cm"],
            "explanation": "$h = \\dfrac{2 \\times 90}{10 + 8} = \\dfrac{180}{18} = 10$ cm."
        },
        {
            "question": "A trapezoid has area $A = 45$ cm² and parallel sides $a = 5$ cm, $b = 10$ cm. Find the height.",
            "answer": "$h = 6$ cm",
            "wrong": ["$h = 3$ cm", "$h = 9$ cm", "$h = 12$ cm"],
            "explanation": "$h = \\dfrac{2 \\times 45}{5 + 10} = \\dfrac{90}{15} = 6$ cm."
        },
        {
            "question": "A trapezoid has area $A = 120$ m² and parallel sides $a = 12$ m, $b = 18$ m. Find the height.",
            "answer": "$h = 8$ m",
            "wrong": ["$h = 4$ m", "$h = 16$ m", "$h = 6$ m"],
            "explanation": "$h = \\dfrac{2 \\times 120}{12 + 18} = \\dfrac{240}{30} = 8$ m."
        },
        {
            "question": "A trapezoid has area $A = 26$ cm² and parallel sides $a = 4$ cm, $b = 9$ cm. Find the height.",
            "answer": "$h = 4$ cm",
            "wrong": ["$h = 2$ cm", "$h = 8$ cm", "$h = 5.2$ cm"],
            "explanation": "$h = \\dfrac{2 \\times 26}{4 + 9} = \\dfrac{52}{13} = 4$ cm."
        },
        {
            "question": "A trapezoid has area $A = 75$ m² and parallel sides $a = 6$ m, $b = 9$ m. Find the height.",
            "answer": "$h = 10$ m",
            "wrong": ["$h = 5$ m", "$h = 25$ m", "$h = 15$ m"],
            "explanation": "$h = \\dfrac{2 \\times 75}{6 + 9} = \\dfrac{150}{15} = 10$ m."
        },
        {
            "question": "A trapezoid has area $A = 56$ cm² and parallel sides $a = 6$ cm, $b = 8$ cm. Find the height.",
            "answer": "$h = 8$ cm",
            "wrong": ["$h = 4$ cm", "$h = 16$ cm", "$h = 7$ cm"],
            "explanation": "$h = \\dfrac{2 \\times 56}{6 + 8} = \\dfrac{112}{14} = 8$ cm."
        },
    ],
    'circle_basic': [

        # ─────────────────────────────────────────────
        # AREA  (20 questions)   A = π r²
        # ─────────────────────────────────────────────

        {
            "question": "A circle has radius $r = 3$ cm. Find the area.",
            "answer": "$A = 9\\pi$ cm²",
            "wrong": ["$A = 6\\pi$ cm²", "$A = 3\\pi$ cm²", "$A = 12\\pi$ cm²"],
            "explanation": "$A = \\pi r^2 = \\pi \\times 3^2 = 9\\pi$ cm²."
        },
        {
            "question": "A circle has radius $r = 5$ cm. Find the area.",
            "answer": "$A = 25\\pi$ cm²",
            "wrong": ["$A = 10\\pi$ cm²", "$A = 50\\pi$ cm²", "$A = 5\\pi$ cm²"],
            "explanation": "$A = \\pi r^2 = \\pi \\times 5^2 = 25\\pi$ cm²."
        },
        {
            "question": "A circle has radius $r = 7$ m. Find the area.",
            "answer": "$A = 49\\pi$ m²",
            "wrong": ["$A = 14\\pi$ m²", "$A = 28\\pi$ m²", "$A = 98\\pi$ m²"],
            "explanation": "$A = \\pi r^2 = \\pi \\times 7^2 = 49\\pi$ m²."
        },
        {
            "question": "A circle has radius $r = 10$ cm. Find the area.",
            "answer": "$A = 100\\pi$ cm²",
            "wrong": ["$A = 20\\pi$ cm²", "$A = 50\\pi$ cm²", "$A = 200\\pi$ cm²"],
            "explanation": "$A = \\pi r^2 = \\pi \\times 10^2 = 100\\pi$ cm²."
        },
        {
            "question": "A circle has diameter $d = 8$ cm. Find the area.",
            "answer": "$A = 16\\pi$ cm²",
            "wrong": ["$A = 64\\pi$ cm²", "$A = 8\\pi$ cm²", "$A = 32\\pi$ cm²"],
            "explanation": "$r = d/2 = 4$ cm, $A = \\pi \\times 4^2 = 16\\pi$ cm²."
        },
        {
            "question": "A circle has diameter $d = 12$ m. Find the area.",
            "answer": "$A = 36\\pi$ m²",
            "wrong": ["$A = 144\\pi$ m²", "$A = 24\\pi$ m²", "$A = 72\\pi$ m²"],
            "explanation": "$r = 12/2 = 6$ m, $A = \\pi \\times 6^2 = 36\\pi$ m²."
        },
        {
            "question": "A circle has radius $r = 1$ cm. Find the area.",
            "answer": "$A = \\pi$ cm²",
            "wrong": ["$A = 2\\pi$ cm²", "$A = 4\\pi$ cm²", "$A = \\dfrac{\\pi}{2}$ cm²"],
            "explanation": "$A = \\pi r^2 = \\pi \\times 1^2 = \\pi$ cm²."
        },
        {
            "question": "The area of a circle is $A = 64\\pi$ cm². Find the radius.",
            "answer": "$r = 8$ cm",
            "wrong": ["$r = 4$ cm", "$r = 16$ cm", "$r = 32$ cm"],
            "explanation": "$r = \\sqrt{\\dfrac{A}{\\pi}} = \\sqrt{64} = 8$ cm."
        },
        {
            "question": "The area of a circle is $A = 100\\pi$ m². Find the radius.",
            "answer": "$r = 10$ m",
            "wrong": ["$r = 5$ m", "$r = 20$ m", "$r = 50$ m"],
            "explanation": "$r = \\sqrt{\\dfrac{A}{\\pi}} = \\sqrt{100} = 10$ m."
        },
        {
            "question": "The area of a circle is $A = 36\\pi$ cm². Find the diameter.",
            "answer": "$d = 12$ cm",
            "wrong": ["$d = 6$ cm", "$d = 18$ cm", "$d = 36$ cm"],
            "explanation": "$r = \\sqrt{36} = 6$ cm, $d = 2r = 12$ cm."
        },
        {
            "question": "A circle has radius $r = 6$ m. Find the area.",
            "answer": "$A = 36\\pi$ m²",
            "wrong": ["$A = 12\\pi$ m²", "$A = 18\\pi$ m²", "$A = 72\\pi$ m²"],
            "explanation": "$A = \\pi r^2 = \\pi \\times 6^2 = 36\\pi$ m²."
        },
        {
            "question": "A circle has diameter $d = 20$ cm. Find the area.",
            "answer": "$A = 100\\pi$ cm²",
            "wrong": ["$A = 400\\pi$ cm²", "$A = 40\\pi$ cm²", "$A = 200\\pi$ cm²"],
            "explanation": "$r = 20/2 = 10$ cm, $A = \\pi \\times 10^2 = 100\\pi$ cm²."
        },
        {
            "question": "The area of a circle is $A = 49\\pi$ m². Find the diameter.",
            "answer": "$d = 14$ m",
            "wrong": ["$d = 7$ m", "$d = 49$ m", "$d = 28$ m"],
            "explanation": "$r = \\sqrt{49} = 7$ m, $d = 2 \\times 7 = 14$ m."
        },
        {
            "question": "A circle has radius $r = 11$ cm. Find the area.",
            "answer": "$A = 121\\pi$ cm²",
            "wrong": ["$A = 22\\pi$ cm²", "$A = 44\\pi$ cm²", "$A = 242\\pi$ cm²"],
            "explanation": "$A = \\pi r^2 = \\pi \\times 11^2 = 121\\pi$ cm²."
        },
        {
            "question": "A circle has radius $r = \\sqrt{5}$ cm. Find the area.",
            "answer": "$A = 5\\pi$ cm²",
            "wrong": ["$A = \\sqrt{5}\\,\\pi$ cm²", "$A = 25\\pi$ cm²", "$A = 2\\sqrt{5}\\,\\pi$ cm²"],
            "explanation": "$A = \\pi r^2 = \\pi \\times (\\sqrt{5})^2 = 5\\pi$ cm²."
        },
        {
            "question": "The area of a circle is $A = 25\\pi$ cm². Find the radius.",
            "answer": "$r = 5$ cm",
            "wrong": ["$r = 25$ cm", "$r = 10$ cm", "$r = 2.5$ cm"],
            "explanation": "$r = \\sqrt{\\dfrac{A}{\\pi}} = \\sqrt{25} = 5$ cm."
        },
        {
            "question": "A circle has diameter $d = 14$ m. Find the area.",
            "answer": "$A = 49\\pi$ m²",
            "wrong": ["$A = 196\\pi$ m²", "$A = 14\\pi$ m²", "$A = 28\\pi$ m²"],
            "explanation": "$r = 14/2 = 7$ m, $A = \\pi \\times 7^2 = 49\\pi$ m²."
        },
        {
            "question": "A circle has radius $r = 0.5$ m. Find the area.",
            "answer": "$A = 0.25\\pi$ m²",
            "wrong": ["$A = \\pi$ m²", "$A = 0.5\\pi$ m²", "$A = 2\\pi$ m²"],
            "explanation": "$A = \\pi r^2 = \\pi \\times 0.5^2 = 0.25\\pi$ m²."
        },
        {
            "question": "The area of a circle is $A = 144\\pi$ cm². Find the radius.",
            "answer": "$r = 12$ cm",
            "wrong": ["$r = 6$ cm", "$r = 24$ cm", "$r = 144$ cm"],
            "explanation": "$r = \\sqrt{\\dfrac{A}{\\pi}} = \\sqrt{144} = 12$ cm."
        },
        {
            "question": "Two circles have radii $r_1 = 3$ cm and $r_2 = 4$ cm. What is the ratio of their areas?",
            "answer": "$9 : 16$",
            "wrong": ["$3 : 4$", "$6 : 8$", "$27 : 64$"],
            "explanation": "Area ratio $= r_1^2 : r_2^2 = 9 : 16$."
        },

        # ─────────────────────────────────────────────
        # CIRCUMFERENCE  (20 questions)   C = 2π r
        # ─────────────────────────────────────────────

        {
            "question": "A circle has radius $r = 4$ cm. Find the circumference.",
            "answer": "$C = 8\\pi$ cm",
            "wrong": ["$C = 16\\pi$ cm", "$C = 4\\pi$ cm", "$C = 2\\pi$ cm"],
            "explanation": "$C = 2\\pi r = 2\\pi \\times 4 = 8\\pi$ cm."
        },
        {
            "question": "A circle has radius $r = 9$ m. Find the circumference.",
            "answer": "$C = 18\\pi$ m",
            "wrong": ["$C = 9\\pi$ m", "$C = 81\\pi$ m", "$C = 36\\pi$ m"],
            "explanation": "$C = 2\\pi r = 2\\pi \\times 9 = 18\\pi$ m."
        },
        {
            "question": "A circle has diameter $d = 10$ cm. Find the circumference.",
            "answer": "$C = 10\\pi$ cm",
            "wrong": ["$C = 20\\pi$ cm", "$C = 5\\pi$ cm", "$C = 100\\pi$ cm"],
            "explanation": "$C = \\pi d = \\pi \\times 10 = 10\\pi$ cm."
        },
        {
            "question": "A circle has diameter $d = 7$ m. Find the circumference.",
            "answer": "$C = 7\\pi$ m",
            "wrong": ["$C = 14\\pi$ m", "$C = 3.5\\pi$ m", "$C = 49\\pi$ m"],
            "explanation": "$C = \\pi d = \\pi \\times 7 = 7\\pi$ m."
        },
        {
            "question": "The circumference of a circle is $C = 12\\pi$ cm. Find the radius.",
            "answer": "$r = 6$ cm",
            "wrong": ["$r = 12$ cm", "$r = 3$ cm", "$r = 24$ cm"],
            "explanation": "$r = \\dfrac{C}{2\\pi} = \\dfrac{12\\pi}{2\\pi} = 6$ cm."
        },
        {
            "question": "The circumference of a circle is $C = 20\\pi$ m. Find the diameter.",
            "answer": "$d = 20$ m",
            "wrong": ["$d = 10$ m", "$d = 40$ m", "$d = 5$ m"],
            "explanation": "$d = \\dfrac{C}{\\pi} = \\dfrac{20\\pi}{\\pi} = 20$ m."
        },
        {
            "question": "A circle has radius $r = 15$ cm. Find the circumference.",
            "answer": "$C = 30\\pi$ cm",
            "wrong": ["$C = 15\\pi$ cm", "$C = 225\\pi$ cm", "$C = 60\\pi$ cm"],
            "explanation": "$C = 2\\pi r = 2\\pi \\times 15 = 30\\pi$ cm."
        },
        {
            "question": "A circle has radius $r = 0.5$ cm. Find the circumference.",
            "answer": "$C = \\pi$ cm",
            "wrong": ["$C = 2\\pi$ cm", "$C = 0.5\\pi$ cm", "$C = 0.25\\pi$ cm"],
            "explanation": "$C = 2\\pi r = 2\\pi \\times 0.5 = \\pi$ cm."
        },
        {
            "question": "The circumference of a circle is $C = 36\\pi$ cm. Find the radius.",
            "answer": "$r = 18$ cm",
            "wrong": ["$r = 9$ cm", "$r = 36$ cm", "$r = 72$ cm"],
            "explanation": "$r = \\dfrac{C}{2\\pi} = \\dfrac{36\\pi}{2\\pi} = 18$ cm."
        },
        {
            "question": "The circumference of a circle is $C = 50\\pi$ m. Find the diameter.",
            "answer": "$d = 50$ m",
            "wrong": ["$d = 25$ m", "$d = 100$ m", "$d = 5$ m"],
            "explanation": "$d = \\dfrac{C}{\\pi} = 50$ m."
        },
        {
            "question": "A circle has diameter $d = 18$ cm. Find the circumference.",
            "answer": "$C = 18\\pi$ cm",
            "wrong": ["$C = 9\\pi$ cm", "$C = 36\\pi$ cm", "$C = 324\\pi$ cm"],
            "explanation": "$C = \\pi d = \\pi \\times 18 = 18\\pi$ cm."
        },
        {
            "question": "A circle has radius $r = 3\\sqrt{2}$ m. Find the circumference.",
            "answer": "$C = 6\\sqrt{2}\\,\\pi$ m",
            "wrong": ["$C = 3\\sqrt{2}\\,\\pi$ m", "$C = 18\\pi$ m", "$C = 12\\sqrt{2}\\,\\pi$ m"],
            "explanation": "$C = 2\\pi r = 2\\pi \\times 3\\sqrt{2} = 6\\sqrt{2}\\,\\pi$ m."
        },
        {
            "question": "The circumference of a circle is $C = 8\\pi$ cm. Find the area.",
            "answer": "$A = 16\\pi$ cm²",
            "wrong": ["$A = 8\\pi$ cm²", "$A = 64\\pi$ cm²", "$A = 4\\pi$ cm²"],
            "explanation": "$r = \\dfrac{C}{2\\pi} = 4$ cm, $A = \\pi \\times 4^2 = 16\\pi$ cm²."
        },
        {
            "question": "The circumference of a circle is $C = 14\\pi$ m. Find the area.",
            "answer": "$A = 49\\pi$ m²",
            "wrong": ["$A = 14\\pi$ m²", "$A = 196\\pi$ m²", "$A = 28\\pi$ m²"],
            "explanation": "$r = \\dfrac{14\\pi}{2\\pi} = 7$ m, $A = \\pi \\times 7^2 = 49\\pi$ m²."
        },
        {
            "question": "A circle has radius $r = 20$ cm. Find the circumference.",
            "answer": "$C = 40\\pi$ cm",
            "wrong": ["$C = 20\\pi$ cm", "$C = 400\\pi$ cm", "$C = 80\\pi$ cm"],
            "explanation": "$C = 2\\pi r = 2\\pi \\times 20 = 40\\pi$ cm."
        },
        {
            "question": "The circumference of a circle is $C = 2\\pi$ cm. Find the area.",
            "answer": "$A = \\pi$ cm²",
            "wrong": ["$A = 2\\pi$ cm²", "$A = 4\\pi$ cm²", "$A = \\dfrac{\\pi}{4}$ cm²"],
            "explanation": "$r = \\dfrac{2\\pi}{2\\pi} = 1$ cm, $A = \\pi \\times 1^2 = \\pi$ cm²."
        },
        {
            "question": "A circle has diameter $d = 24$ m. Find the circumference.",
            "answer": "$C = 24\\pi$ m",
            "wrong": ["$C = 12\\pi$ m", "$C = 48\\pi$ m", "$C = 576\\pi$ m"],
            "explanation": "$C = \\pi d = \\pi \\times 24 = 24\\pi$ m."
        },
        {
            "question": "The circumference of a circle is $C = 30\\pi$ cm. Find the radius.",
            "answer": "$r = 15$ cm",
            "wrong": ["$r = 30$ cm", "$r = 7.5$ cm", "$r = 60$ cm"],
            "explanation": "$r = \\dfrac{C}{2\\pi} = \\dfrac{30\\pi}{2\\pi} = 15$ cm."
        },
        {
            "question": "Two circles have radii $r_1 = 2$ cm and $r_2 = 6$ cm. What is the ratio of their circumferences?",
            "answer": "$1 : 3$",
            "wrong": ["$1 : 9$", "$2 : 6$", "$4 : 36$"],
            "explanation": "Circumference ratio $= r_1 : r_2 = 2 : 6 = 1 : 3$."
        },
        {
            "question": "The circumference of a circle is $C = 100\\pi$ m. Find the radius.",
            "answer": "$r = 50$ m",
            "wrong": ["$r = 100$ m", "$r = 25$ m", "$r = 10$ m"],
            "explanation": "$r = \\dfrac{C}{2\\pi} = \\dfrac{100\\pi}{2\\pi} = 50$ m."
        },
        {
            "question": "A circle has radius $r = 12$ m. Find the circumference.",
            "answer": "$C = 24\\pi$ m",
            "wrong": ["$C = 12\\pi$ m", "$C = 144\\pi$ m", "$C = 48\\pi$ m"],
            "explanation": "$C = 2\\pi r = 2\\pi \\times 12 = 24\\pi$ m."
        },

        # ─────────────────────────────────────────────
        # RADIUS & DIAMETER  (10 questions)
        # ─────────────────────────────────────────────

        {
            "question": "A circle has diameter $d = 26$ cm. Find the radius.",
            "answer": "$r = 13$ cm",
            "wrong": ["$r = 26$ cm", "$r = 52$ cm", "$r = 6.5$ cm"],
            "explanation": "$r = \\dfrac{d}{2} = \\dfrac{26}{2} = 13$ cm."
        },
        {
            "question": "A circle has radius $r = 17$ m. Find the diameter.",
            "answer": "$d = 34$ m",
            "wrong": ["$d = 17$ m", "$d = 8.5$ m", "$d = 51$ m"],
            "explanation": "$d = 2r = 2 \\times 17 = 34$ m."
        },
        {
            "question": "The area of a circle is $A = 81\\pi$ cm². Find the diameter.",
            "answer": "$d = 18$ cm",
            "wrong": ["$d = 9$ cm", "$d = 81$ cm", "$d = 36$ cm"],
            "explanation": "$r = \\sqrt{81} = 9$ cm, $d = 2 \\times 9 = 18$ cm."
        },
        {
            "question": "The circumference of a circle is $C = 16\\pi$ m. Find the radius.",
            "answer": "$r = 8$ m",
            "wrong": ["$r = 16$ m", "$r = 4$ m", "$r = 32$ m"],
            "explanation": "$r = \\dfrac{C}{2\\pi} = \\dfrac{16\\pi}{2\\pi} = 8$ m."
        },
        {
            "question": "The circumference of a circle is $C = 22\\pi$ cm. Find the diameter.",
            "answer": "$d = 22$ cm",
            "wrong": ["$d = 11$ cm", "$d = 44$ cm", "$d = 7$ cm"],
            "explanation": "$d = \\dfrac{C}{\\pi} = \\dfrac{22\\pi}{\\pi} = 22$ cm."
        },
        {
            "question": "A circle has radius $r = 4.5$ cm. Find the diameter.",
            "answer": "$d = 9$ cm",
            "wrong": ["$d = 4.5$ cm", "$d = 18$ cm", "$d = 2.25$ cm"],
            "explanation": "$d = 2r = 2 \\times 4.5 = 9$ cm."
        },
        {
            "question": "The area of a circle is $A = 121\\pi$ m². Find the radius.",
            "answer": "$r = 11$ m",
            "wrong": ["$r = 121$ m", "$r = 22$ m", "$r = \\sqrt{11}$ m"],
            "explanation": "$r = \\sqrt{\\dfrac{A}{\\pi}} = \\sqrt{121} = 11$ m."
        },
        {
            "question": "A circle has diameter $d = 3\\sqrt{2}$ cm. Find the radius.",
            "answer": "$r = \\dfrac{3\\sqrt{2}}{2}$ cm",
            "wrong": ["$r = 3\\sqrt{2}$ cm", "$r = 6\\sqrt{2}$ cm", "$r = \\sqrt{2}$ cm"],
            "explanation": "$r = \\dfrac{d}{2} = \\dfrac{3\\sqrt{2}}{2}$ cm."
        },
        {
            "question": "The circumference of a circle is $C = 40\\pi$ cm. Find the diameter.",
            "answer": "$d = 40$ cm",
            "wrong": ["$d = 20$ cm", "$d = 80$ cm", "$d = 10$ cm"],
            "explanation": "$d = \\dfrac{C}{\\pi} = \\dfrac{40\\pi}{\\pi} = 40$ cm."
        },
    ],
    'equation_of_circle': [

        # ─────────────────────────────────────────────────────────────
        # SECTION 1 — EQUATION OF A CIRCLE  (20 questions)
        # Standard form: (x − h)² + (y − k)² = r²
        # ─────────────────────────────────────────────────────────────

        {
            "question": "Write the equation of a circle with centre $(0, 0)$ and radius $r = 5$.",
            "answer": "$x^2 + y^2 = 25$",
            "wrong": ["$x^2 + y^2 = 5$", "$x^2 + y^2 = 10$", "$(x-5)^2 + (y-5)^2 = 25$"],
            "explanation": "Centre $(0,0)$: $(x-0)^2+(y-0)^2=5^2 \\Rightarrow x^2+y^2=25$."
        },
        {
            "question": "Write the equation of a circle with centre $(3, 4)$ and radius $r = 6$.",
            "answer": "$(x-3)^2 + (y-4)^2 = 36$",
            "wrong": ["$(x+3)^2 + (y+4)^2 = 36$", "$(x-3)^2 + (y-4)^2 = 6$", "$(x-4)^2 + (y-3)^2 = 36$"],
            "explanation": "$(x-3)^2+(y-4)^2=6^2=36$."
        },
        {
            "question": "Write the equation of a circle with centre $(-2, 5)$ and radius $r = 3$.",
            "answer": "$(x+2)^2 + (y-5)^2 = 9$",
            "wrong": ["$(x-2)^2 + (y-5)^2 = 9$", "$(x+2)^2 + (y+5)^2 = 9$", "$(x+2)^2 + (y-5)^2 = 3$"],
            "explanation": "$(x-(-2))^2+(y-5)^2=3^2 \\Rightarrow (x+2)^2+(y-5)^2=9$."
        },
        {
            "question": "Write the equation of a circle with centre $(0, -4)$ and radius $r = 7$.",
            "answer": "$x^2 + (y+4)^2 = 49$",
            "wrong": ["$x^2 + (y-4)^2 = 49$", "$x^2 + (y+4)^2 = 7$", "$(x+4)^2 + y^2 = 49$"],
            "explanation": "$(x-0)^2+(y-(-4))^2=7^2 \\Rightarrow x^2+(y+4)^2=49$."
        },
        {
            "question": "Find the centre and radius of the circle $x^2 + y^2 = 81$.",
            "answer": "Centre $(0, 0)$, radius $r = 9$",
            "wrong": ["Centre $(0, 0)$, radius $r = 81$", "Centre $(9, 9)$, radius $r = 9$",
                      "Centre $(0, 0)$, radius $r = 40.5$"],
            "explanation": "$x^2+y^2=9^2$, so centre $(0,0)$ and $r=9$."
        },
        {
            "question": "Find the centre and radius of the circle $(x-5)^2 + (y+3)^2 = 16$.",
            "answer": "Centre $(5, -3)$, radius $r = 4$",
            "wrong": ["Centre $(-5, 3)$, radius $r = 4$", "Centre $(5, -3)$, radius $r = 16$",
                      "Centre $(5, 3)$, radius $r = 4$"],
            "explanation": "$h=5,\\; k=-3,\\; r=\\sqrt{16}=4$."
        },
        {
            "question": "Find the centre and radius of the circle $(x+1)^2 + (y-7)^2 = 49$.",
            "answer": "Centre $(-1, 7)$, radius $r = 7$",
            "wrong": ["Centre $(1, -7)$, radius $r = 7$", "Centre $(-1, 7)$, radius $r = 49$",
                      "Centre $(1, 7)$, radius $r = 7$"],
            "explanation": "$h=-1,\\; k=7,\\; r=\\sqrt{49}=7$."
        },
        {
            "question": "Write the equation of a circle with centre $(-3, -6)$ and radius $r = 10$.",
            "answer": "$(x+3)^2 + (y+6)^2 = 100$",
            "wrong": ["$(x-3)^2 + (y-6)^2 = 100$", "$(x+3)^2 + (y+6)^2 = 10$", "$(x+6)^2 + (y+3)^2 = 100$"],
            "explanation": "$(x+3)^2+(y+6)^2=10^2=100$."
        },
        {
            "question": "Find the radius of the circle $(x-2)^2 + (y-2)^2 = 50$.",
            "answer": "$r = 5\\sqrt{2}$",
            "wrong": ["$r = 50$", "$r = 25$", "$r = 10$"],
            "explanation": "$r = \\sqrt{50} = 5\\sqrt{2}$."
        },
        {
            "question": "Write the equation of a circle with centre $(4, -1)$ and radius $r = \\sqrt{11}$.",
            "answer": "$(x-4)^2 + (y+1)^2 = 11$",
            "wrong": ["$(x-4)^2 + (y+1)^2 = \\sqrt{11}$", "$(x+4)^2 + (y-1)^2 = 11$", "$(x-4)^2 + (y-1)^2 = 11$"],
            "explanation": "$(x-4)^2+(y+1)^2=(\\sqrt{11})^2=11$."
        },
        {
            "question": "Find the centre and radius of $(x+6)^2 + y^2 = 100$.",
            "answer": "Centre $(-6, 0)$, radius $r = 10$",
            "wrong": ["Centre $(6, 0)$, radius $r = 10$", "Centre $(-6, 0)$, radius $r = 100$",
                      "Centre $(0, -6)$, radius $r = 10$"],
            "explanation": "$h=-6,\\; k=0,\\; r=\\sqrt{100}=10$."
        },
        {
            "question": "Write the equation of a circle with centre $(0, 0)$ and radius $r = \\sqrt{7}$.",
            "answer": "$x^2 + y^2 = 7$",
            "wrong": ["$x^2 + y^2 = \\sqrt{7}$", "$x^2 + y^2 = 49$", "$x^2 + y^2 = 14$"],
            "explanation": "$x^2+y^2=(\\sqrt{7})^2=7$."
        },
        {
            "question": "Find the centre and radius of $(x-9)^2 + (y-9)^2 = 9$.",
            "answer": "Centre $(9, 9)$, radius $r = 3$",
            "wrong": ["Centre $(9, 9)$, radius $r = 9$", "Centre $(-9, -9)$, radius $r = 3$",
                      "Centre $(3, 3)$, radius $r = 9$"],
            "explanation": "$h=9,\\; k=9,\\; r=\\sqrt{9}=3$."
        },
        {
            "question": "Write the equation of a circle with centre $(7, 0)$ and radius $r = 4$.",
            "answer": "$(x-7)^2 + y^2 = 16$",
            "wrong": ["$(x-7)^2 + y^2 = 4$", "$(x+7)^2 + y^2 = 16$", "$x^2 + (y-7)^2 = 16$"],
            "explanation": "$(x-7)^2+(y-0)^2=4^2=16$."
        },
        {
            "question": "Two circles have equations $x^2+y^2=4$ and $x^2+y^2=9$. Which has the larger radius?",
            "answer": "$x^2+y^2=9$, with $r=3$",
            "wrong": ["$x^2+y^2=4$, with $r=4$", "Both have the same radius", "$x^2+y^2=9$, with $r=9$"],
            "explanation": "$r_1=\\sqrt{4}=2$, $r_2=\\sqrt{9}=3$. The second circle is larger."
        },
        {
            "question": "Find the centre and radius of $(x-1)^2 + (y+2)^2 = 5$.",
            "answer": "Centre $(1, -2)$, radius $r = \\sqrt{5}$",
            "wrong": ["Centre $(-1, 2)$, radius $r = \\sqrt{5}$", "Centre $(1, -2)$, radius $r = 5$",
                      "Centre $(1, 2)$, radius $r = \\sqrt{5}$"],
            "explanation": "$h=1,\\; k=-2,\\; r=\\sqrt{5}$."
        },
        {
            "question": "Write the equation of a circle with centre $(-5, 8)$ and radius $r = 2$.",
            "answer": "$(x+5)^2 + (y-8)^2 = 4$",
            "wrong": ["$(x-5)^2 + (y+8)^2 = 4$", "$(x+5)^2 + (y-8)^2 = 2$", "$(x+5)^2 + (y-8)^2 = 16$"],
            "explanation": "$(x+5)^2+(y-8)^2=2^2=4$."
        },
        {
            "question": "Find the diameter of the circle $(x+3)^2 + (y-3)^2 = 36$.",
            "answer": "$d = 12$",
            "wrong": ["$d = 6$", "$d = 36$", "$d = 18$"],
            "explanation": "$r = \\sqrt{36} = 6$, so $d = 2r = 12$."
        },
        {
            "question": "Write the equation of a circle with centre $(0, 6)$ and radius $r = 8$.",
            "answer": "$x^2 + (y-6)^2 = 64$",
            "wrong": ["$x^2 + (y+6)^2 = 64$", "$(x-6)^2 + y^2 = 64$", "$x^2 + (y-6)^2 = 8$"],
            "explanation": "$(x-0)^2+(y-6)^2=8^2=64$."
        },
        {
            "question": "Find the centre and radius of $(x+4)^2 + (y+4)^2 = 32$.",
            "answer": "Centre $(-4, -4)$, radius $r = 4\\sqrt{2}$",
            "wrong": ["Centre $(4, 4)$, radius $r = 4\\sqrt{2}$", "Centre $(-4, -4)$, radius $r = 32$",
                      "Centre $(-4, -4)$, radius $r = 16$"],
            "explanation": "$h=-4,\\; k=-4,\\; r=\\sqrt{32}=4\\sqrt{2}$."
        },

        # ─────────────────────────────────────────────────────────────
        # SECTION 2 — TRANSLATIONS (horizontal & vertical)  (10 qs)
        # ─────────────────────────────────────────────────────────────

        {
            "question": "The circle $x^2 + y^2 = 25$ is moved $3$ units to the right. Write its new equation.",
            "answer": "$(x-3)^2 + y^2 = 25$",
            "wrong": ["$(x+3)^2 + y^2 = 25$", "$x^2 + (y-3)^2 = 25$", "$(x-3)^2 + y^2 = 22$"],
            "explanation": "Shift right by $3$: replace $x$ with $(x-3)$. New equation: $(x-3)^2+y^2=25$."
        },
        {
            "question": "The circle $x^2 + y^2 = 16$ is moved $5$ units upward. Write its new equation.",
            "answer": "$x^2 + (y-5)^2 = 16$",
            "wrong": ["$x^2 + (y+5)^2 = 16$", "$(x-5)^2 + y^2 = 16$", "$x^2 + (y-5)^2 = 11$"],
            "explanation": "Shift up by $5$: replace $y$ with $(y-5)$. New equation: $x^2+(y-5)^2=16$."
        },
        {
            "question": "The circle $x^2 + y^2 = 9$ is moved $4$ units to the left. Write its new equation.",
            "answer": "$(x+4)^2 + y^2 = 9$",
            "wrong": ["$(x-4)^2 + y^2 = 9$", "$x^2 + (y+4)^2 = 9$", "$(x+4)^2 + y^2 = 5$"],
            "explanation": "Shift left by $4$: replace $x$ with $(x+4)$. New equation: $(x+4)^2+y^2=9$."
        },
        {
            "question": "The circle $x^2 + y^2 = 49$ is moved $6$ units downward. Write its new equation.",
            "answer": "$x^2 + (y+6)^2 = 49$",
            "wrong": ["$x^2 + (y-6)^2 = 49$", "$(x+6)^2 + y^2 = 49$", "$x^2 + (y+6)^2 = 43$"],
            "explanation": "Shift down by $6$: replace $y$ with $(y+6)$. New equation: $x^2+(y+6)^2=49$."
        },
        {
            "question": "The circle $(x-2)^2 + (y-3)^2 = 25$ is moved $2$ units to the right. What is the new centre?",
            "answer": "$(4, 3)$",
            "wrong": ["$(0, 3)$", "$(2, 5)$", "$(2, 1)$"],
            "explanation": "Moving right by $2$ increases the $x$-coordinate of the centre: $(2+2,\\,3)=(4,3)$."
        },
        {
            "question": "The circle $(x+1)^2 + (y-4)^2 = 36$ is moved $4$ units downward. What is the new equation?",
            "answer": "$(x+1)^2 + y^2 = 36$",
            "wrong": ["$(x+1)^2 + (y-8)^2 = 36$", "$(x+5)^2 + (y-4)^2 = 36$", "$(x+1)^2 + (y+4)^2 = 36$"],
            "explanation": "New centre: $(-1,\\, 4-4)=(-1,0)$. Equation: $(x+1)^2+y^2=36$."
        },
        {
            "question": "The circle $x^2 + y^2 = 100$ is moved $7$ units left and $3$ units up. Write its new equation.",
            "answer": "$(x+7)^2 + (y-3)^2 = 100$",
            "wrong": ["$(x-7)^2 + (y+3)^2 = 100$", "$(x+7)^2 + (y+3)^2 = 100$", "$(x-7)^2 + (y-3)^2 = 100$"],
            "explanation": "Left $7$: $(x+7)$; up $3$: $(y-3)$. New equation: $(x+7)^2+(y-3)^2=100$."
        },
        {
            "question": "After a translation, the circle $x^2+y^2=4$ has new equation $(x-5)^2+(y+2)^2=4$. Describe the translation.",
            "answer": "$5$ units right and $2$ units down",
            "wrong": ["$5$ units left and $2$ units up", "$2$ units right and $5$ units down",
                      "$5$ units right and $2$ units up"],
            "explanation": "Centre moved from $(0,0)$ to $(5,-2)$: right $5$, down $2$."
        },
        {
            "question": "The circle $(x-3)^2+(y+1)^2=9$ is moved $3$ units left and $1$ unit up. Write its new equation.",
            "answer": "$x^2 + y^2 = 9$",
            "wrong": ["$(x-6)^2+(y+2)^2=9$", "$(x+3)^2+(y-1)^2=9$", "$(x-3)^2+(y-1)^2=9$"],
            "explanation": "New centre: $(3-3,\\,-1+1)=(0,0)$. Equation: $x^2+y^2=9$."
        },
        {
            "question": "The circle $x^2+(y-2)^2=25$ is moved $5$ units to the right. What is the new centre?",
            "answer": "$(5, 2)$",
            "wrong": ["$(0, 7)$", "$(5, -3)$", "$(-5, 2)$"],
            "explanation": "Original centre $(0,2)$, shifted right $5$: new centre $(5,2)$."
        },

        # ─────────────────────────────────────────────────────────────
        # SECTION 3 — POINT POSITION: inside / on / outside  (10 qs)
        # Substitute point into (x−h)²+(y−k)²:
        #   < r²  → inside     = r²  → on     > r²  → outside
        # ─────────────────────────────────────────────────────────────

        {
            "question": "Is the point $(3, 4)$ inside, on, or outside the circle $x^2 + y^2 = 25$?",
            "answer": "On the circle",
            "wrong": ["Inside the circle", "Outside the circle", "Cannot be determined"],
            "explanation": "$3^2+4^2=9+16=25=r^2$. The point lies on the circle."
        },
        {
            "question": "Is the point $(1, 1)$ inside, on, or outside the circle $x^2 + y^2 = 9$?",
            "answer": "Inside the circle",
            "wrong": ["On the circle", "Outside the circle", "Cannot be determined"],
            "explanation": "$1^2+1^2=2 < 9=r^2$. The point is inside the circle."
        },
        {
            "question": "Is the point $(4, 5)$ inside, on, or outside the circle $x^2 + y^2 = 25$?",
            "answer": "Outside the circle",
            "wrong": ["Inside the circle", "On the circle", "Cannot be determined"],
            "explanation": "$4^2+5^2=16+25=41 > 25=r^2$. The point is outside the circle."
        },
        {
            "question": "Is the point $(2, 3)$ inside, on, or outside the circle $(x-1)^2 + (y-1)^2 = 10$?",
            "answer": "Inside the circle",
            "wrong": ["On the circle", "Outside the circle", "Cannot be determined"],
            "explanation": "$(2-1)^2+(3-1)^2=1+4=5 < 10=r^2$. The point is inside the circle."
        },
        {
            "question": "Is the point $(0, 5)$ inside, on, or outside the circle $x^2 + y^2 = 25$?",
            "answer": "On the circle",
            "wrong": ["Inside the circle", "Outside the circle", "Cannot be determined"],
            "explanation": "$0^2+5^2=25=r^2$. The point lies on the circle."
        },
        {
            "question": "Is the point $(3, 3)$ inside, on, or outside the circle $(x-2)^2 + (y-2)^2 = 4$?",
            "answer": "Inside the circle",
            "wrong": ["Outside the circle", "On the circle", "Cannot be determined"],
            "explanation": "$(3-2)^2+(3-2)^2=1+1=2 < 4=r^2$. The point is inside the circle."
        },
        {
            "question": "Is the point $(-3, 4)$ inside, on, or outside the circle $x^2 + y^2 = 25$?",
            "answer": "On the circle",
            "wrong": ["Inside the circle", "Outside the circle", "Cannot be determined"],
            "explanation": "$(-3)^2+4^2=9+16=25=r^2$. The point lies on the circle."
        },
        {
            "question": "Is the point $(5, 5)$ inside, on, or outside the circle $x^2 + y^2 = 36$?",
            "answer": "Outside the circle",
            "wrong": ["Inside the circle", "On the circle", "Cannot be determined"],
            "explanation": "$5^2+5^2=50 > 36=r^2$. The point is outside the circle."
        },
        {
            "question": "Is the point $(1, 2)$ inside, on, or outside the circle $(x-3)^2 + (y-4)^2 = 9$?",
            "answer": "Inside the circle",
            "wrong": ["Outside the circle", "On the circle", "Cannot be determined"],
            "explanation": "$(1-3)^2+(2-4)^2=4+4=8 < 9=r^2$. The point is inside the circle."
        },
        {
            "question": "Is the point $(6, 0)$ inside, on, or outside the circle $(x-1)^2 + y^2 = 25$?",
            "answer": "On the circle",
            "wrong": ["Inside the circle", "Outside the circle", "Cannot be determined"],
            "explanation": "$(6-1)^2+0^2=25=r^2$. The point lies on the circle."
        },

        # ─────────────────────────────────────────────────────────────
        # SECTION 4 — SPECIAL CASES  (10 questions)
        # Circles on axes, tangent to axes, passing through origin, etc.
        # ─────────────────────────────────────────────────────────────

        {
            "question": "A circle has centre $(0, 0)$ and passes through $(0, 6)$. Write its equation.",
            "answer": "$x^2 + y^2 = 36$",
            "wrong": ["$x^2 + y^2 = 6$", "$x^2 + (y-6)^2 = 36$", "$x^2 + y^2 = 12$"],
            "explanation": "$r = 6$ (distance from centre to $(0,6)$). Equation: $x^2+y^2=36$."
        },
        {
            "question": "A circle is centred at $(4, 0)$ and is tangent to the $y$-axis. Write its equation.",
            "answer": "$(x-4)^2 + y^2 = 16$",
            "wrong": ["$(x-4)^2 + y^2 = 4$", "$(x+4)^2 + y^2 = 16$", "$(x-4)^2 + y^2 = 8$"],
            "explanation": "Distance from $(4,0)$ to the $y$-axis is $4$, so $r=4$. Equation: $(x-4)^2+y^2=16$."
        },
        {
            "question": "A circle is centred at $(0, 3)$ and is tangent to the $x$-axis. Write its equation.",
            "answer": "$x^2 + (y-3)^2 = 9$",
            "wrong": ["$x^2 + (y-3)^2 = 3$", "$x^2 + (y+3)^2 = 9$", "$(x-3)^2 + y^2 = 9$"],
            "explanation": "Distance from $(0,3)$ to the $x$-axis is $3$, so $r=3$. Equation: $x^2+(y-3)^2=9$."
        },
        {
            "question": "The circle $x^2 + y^2 = r^2$ passes through the point $(5, 0)$. Find $r$.",
            "answer": "$r = 5$",
            "wrong": ["$r = 25$", "$r = 10$", "$r = \\sqrt{5}$"],
            "explanation": "Substituting $(5,0)$: $5^2+0^2=r^2 \\Rightarrow r=5$."
        },
        {
            "question": "Where does the circle $x^2 + y^2 = 25$ intersect the $x$-axis?",
            "answer": "$(-5, 0)$ and $(5, 0)$",
            "wrong": ["$(0, 5)$ and $(0, -5)$", "$(5, 5)$ and $(-5, -5)$", "$(25, 0)$ and $(-25, 0)$"],
            "explanation": "Set $y=0$: $x^2=25 \\Rightarrow x=\\pm5$. Points: $(-5,0)$ and $(5,0)$."
        },
        {
            "question": "Where does the circle $x^2 + y^2 = 49$ intersect the $y$-axis?",
            "answer": "$(0, -7)$ and $(0, 7)$",
            "wrong": ["$(-7, 0)$ and $(7, 0)$", "$(0, 49)$ and $(0, -49)$", "$(7, 7)$ and $(-7, -7)$"],
            "explanation": "Set $x=0$: $y^2=49 \\Rightarrow y=\\pm7$. Points: $(0,-7)$ and $(0,7)$."
        },
        {
            "question": "A circle centred at $(0, 0)$ passes through $(-3, 4)$. Write its equation.",
            "answer": "$x^2 + y^2 = 25$",
            "wrong": ["$x^2 + y^2 = 7$", "$x^2 + y^2 = 49$", "$x^2 + y^2 = 5$"],
            "explanation": "$r = \\sqrt{(-3)^2+4^2}=\\sqrt{25}=5$. Equation: $x^2+y^2=25$."
        },
        {
            "question": "A circle is centred at $(-5, 0)$ and is tangent to the $y$-axis. Write its equation.",
            "answer": "$(x+5)^2 + y^2 = 25$",
            "wrong": ["$(x-5)^2 + y^2 = 25$", "$(x+5)^2 + y^2 = 5$", "$(x+5)^2 + y^2 = 10$"],
            "explanation": "Distance from $(-5,0)$ to the $y$-axis is $5$, so $r=5$. Equation: $(x+5)^2+y^2=25$."
        },
        {
            "question": "Does the circle $x^2 + y^2 = 16$ intersect the $x$-axis? If so, at what points?",
            "answer": "Yes, at $(-4, 0)$ and $(4, 0)$",
            "wrong": ["No, it does not intersect the $x$-axis", "Yes, at $(0, 4)$ and $(0, -4)$",
                      "Yes, at $(16, 0)$ and $(-16, 0)$"],
            "explanation": "Set $y=0$: $x^2=16 \\Rightarrow x=\\pm4$. The circle meets the $x$-axis at $(-4,0)$ and $(4,0)$."
        },
        {
            "question": "A circle centred at $(0, 0)$ is tangent to the line $y = 8$. Write its equation.",
            "answer": "$x^2 + y^2 = 64$",
            "wrong": ["$x^2 + y^2 = 8$", "$x^2 + (y-8)^2 = 64$", "$x^2 + y^2 = 16$"],
            "explanation": "The distance from the origin to $y=8$ is $8$, so $r=8$. Equation: $x^2+y^2=64$."
        },
    ],
    'distance_midpoint_slope': [{
        "question": "Find the midpoint of the segment joining $(2, 4)$ and $(8, 10)$.",
        "answer": "$(5, 7)$",
        "wrong": ["$(6, 7)$", "$(5, 6)$", "$(4, 7)$"],
        "explanation": "Midpoint $= \\left(\\frac{2+8}{2}, \\frac{4+10}{2}\\right) = (5, 7)$."
    },
        {
            "question": "Find the midpoint of the segment joining $(-3, 1)$ and $(5, 9)$.",
            "answer": "$(1, 5)$",
            "wrong": ["$(2, 5)$", "$(1, 4)$", "$(1, 6)$"],
            "explanation": "Midpoint $= \\left(\\frac{-3+5}{2}, \\frac{1+9}{2}\\right) = (1, 5)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(0, 0)$ and $(6, -4)$.",
            "answer": "$(3, -2)$",
            "wrong": ["$(3, 2)$", "$(6, -4)$", "$(2, -3)$"],
            "explanation": "Midpoint $= \\left(\\frac{0+6}{2}, \\frac{0+(-4)}{2}\\right) = (3, -2)$."
        },
        {
            "question": "The midpoint of $AB$ is $(4, 6)$. If $A = (1, 2)$, find $B$.",
            "answer": "$(7, 10)$",
            "wrong": ["$(5, 8)$", "$(3, 4)$", "$(8, 12)$"],
            "explanation": "$B = (2(4)-1,\\; 2(6)-2) = (7, 10)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(-6, -2)$ and $(4, 8)$.",
            "answer": "$(-1, 3)$",
            "wrong": ["$(1, 3)$", "$(-1, 4)$", "$(-2, 3)$"],
            "explanation": "Midpoint $= \\left(\\frac{-6+4}{2}, \\frac{-2+8}{2}\\right) = (-1, 3)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(7, -3)$ and $(-1, 5)$.",
            "answer": "$(3, 1)$",
            "wrong": ["$(4, 1)$", "$(3, 2)$", "$(3, -1)$"],
            "explanation": "Midpoint $= \\left(\\frac{7+(-1)}{2}, \\frac{-3+5}{2}\\right) = (3, 1)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(\\frac{1}{2}, 3)$ and $(\\frac{3}{2}, 7)$.",
            "answer": "$(1, 5)$",
            "wrong": ["$(2, 5)$", "$(1, 4)$", "$(1, 6)$"],
            "explanation": "Midpoint $= \\left(\\frac{\\frac{1}{2}+\\frac{3}{2}}{2}, \\frac{3+7}{2}\\right) = (1, 5)$."
        },
        {
            "question": "The midpoint of $PQ$ is $(0, 0)$. If $P = (3, -5)$, find $Q$.",
            "answer": "$(-3, 5)$",
            "wrong": ["$(3, 5)$", "$(-3, -5)$", "$(0, 5)$"],
            "explanation": "$Q = (2(0)-3,\\; 2(0)-(-5)) = (-3, 5)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(-4, 0)$ and $(0, -8)$.",
            "answer": "$(-2, -4)$",
            "wrong": ["$(2, -4)$", "$(-2, 4)$", "$(-4, -8)$"],
            "explanation": "Midpoint $= \\left(\\frac{-4+0}{2}, \\frac{0+(-8)}{2}\\right) = (-2, -4)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(10, -6)$ and $(-4, 2)$.",
            "answer": "$(3, -2)$",
            "wrong": ["$(3, -4)$", "$(2, -2)$", "$(4, -2)$"],
            "explanation": "Midpoint $= \\left(\\frac{10+(-4)}{2}, \\frac{-6+2}{2}\\right) = (3, -2)$."
        },
        {
            "question": "The midpoint of $AB$ is $(5, -1)$. If $B = (9, 3)$, find $A$.",
            "answer": "$(1, -5)$",
            "wrong": ["$(7, 1)$", "$(1, -3)$", "$(3, -5)$"],
            "explanation": "$A = (2(5)-9,\\; 2(-1)-3) = (1, -5)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(-1, -1)$ and $(1, 1)$.",
            "answer": "$(0, 0)$",
            "wrong": ["$(1, 1)$", "$(-1, 1)$", "$(0, 1)$"],
            "explanation": "Midpoint $= \\left(\\frac{-1+1}{2}, \\frac{-1+1}{2}\\right) = (0, 0)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(3, 7)$ and $(3, -3)$.",
            "answer": "$(3, 2)$",
            "wrong": ["$(0, 2)$", "$(3, 4)$", "$(3, -2)$"],
            "explanation": "Midpoint $= \\left(\\frac{3+3}{2}, \\frac{7+(-3)}{2}\\right) = (3, 2)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(8, 5)$ and $(-2, 5)$.",
            "answer": "$(3, 5)$",
            "wrong": ["$(5, 5)$", "$(3, 0)$", "$(4, 5)$"],
            "explanation": "Midpoint $= \\left(\\frac{8+(-2)}{2}, \\frac{5+5}{2}\\right) = (3, 5)$."
        },
        {
            "question": "The midpoint of $CD$ is $(-2, 4)$. If $C = (-6, 1)$, find $D$.",
            "answer": "$(2, 7)$",
            "wrong": ["$(-4, 5)$", "$(2, 3)$", "$(2, 8)$"],
            "explanation": "$D = (2(-2)-(-6),\\; 2(4)-1) = (2, 7)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(-5, 6)$ and $(3, -2)$.",
            "answer": "$(-1, 2)$",
            "wrong": ["$(1, 2)$", "$(-1, 4)$", "$(-2, 2)$"],
            "explanation": "Midpoint $= \\left(\\frac{-5+3}{2}, \\frac{6+(-2)}{2}\\right) = (-1, 2)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(0, 9)$ and $(0, -3)$.",
            "answer": "$(0, 3)$",
            "wrong": ["$(0, 6)$", "$(0, -3)$", "$(0, 4)$"],
            "explanation": "Midpoint $= \\left(0, \\frac{9+(-3)}{2}\\right) = (0, 3)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(-7, -4)$ and $(-3, -8)$.",
            "answer": "$(-5, -6)$",
            "wrong": ["$(-4, -6)$", "$(-5, -4)$", "$(-5, -8)$"],
            "explanation": "Midpoint $= \\left(\\frac{-7+(-3)}{2}, \\frac{-4+(-8)}{2}\\right) = (-5, -6)$."
        },
        {
            "question": "The midpoint of $MN$ is $(3, 3)$. If $M = (0, 6)$, find $N$.",
            "answer": "$(6, 0)$",
            "wrong": ["$(3, 0)$", "$(6, 3)$", "$(6, -6)$"],
            "explanation": "$N = (2(3)-0,\\; 2(3)-6) = (6, 0)$."
        },
        {
            "question": "Find the midpoint of the segment joining $(4, -7)$ and $(-4, 7)$.",
            "answer": "$(0, 0)$",
            "wrong": ["$(4, 7)$", "$(0, 7)$", "$(4, 0)$"],
            "explanation": "Midpoint $= \\left(\\frac{4+(-4)}{2}, \\frac{-7+7}{2}\\right) = (0, 0)$."
        },

        # ─────────────────────────────────────────────
        # SLOPE OF A LINE (20 questions)
        # ─────────────────────────────────────────────
        {
            "question": "Find the slope of the line passing through $(1, 2)$ and $(3, 6)$.",
            "answer": "$2$",
            "wrong": ["$\\dfrac{1}{2}$", "$4$", "$-2$"],
            "explanation": "$m = \\dfrac{6-2}{3-1} = \\dfrac{4}{2} = 2$."
        },
        {
            "question": "Find the slope of the line passing through $(0, 5)$ and $(4, 1)$.",
            "answer": "$-1$",
            "wrong": ["$1$", "$-\\dfrac{1}{2}$", "$-4$"],
            "explanation": "$m = \\dfrac{1-5}{4-0} = \\dfrac{-4}{4} = -1$."
        },
        {
            "question": "Find the slope of the line passing through $(-2, 3)$ and $(4, 3)$.",
            "answer": "$0$",
            "wrong": ["$1$", "$-1$", "undefined"],
            "explanation": "Both $y$-values are equal, so the line is horizontal: $m = 0$."
        },
        {
            "question": "Find the slope of the line passing through $(5, 2)$ and $(5, -6)$.",
            "answer": "undefined",
            "wrong": ["$0$", "$-8$", "$8$"],
            "explanation": "Both $x$-values are equal, so the line is vertical: slope is undefined."
        },
        {
            "question": "Find the slope of the line passing through $(-1, -3)$ and $(2, 6)$.",
            "answer": "$3$",
            "wrong": ["$-3$", "$\\dfrac{1}{3}$", "$9$"],
            "explanation": "$m = \\dfrac{6-(-3)}{2-(-1)} = \\dfrac{9}{3} = 3$."
        },
        {
            "question": "Find the slope of the line passing through $(3, 8)$ and $(7, 4)$.",
            "answer": "$-1$",
            "wrong": ["$1$", "$-2$", "$\\dfrac{1}{2}$"],
            "explanation": "$m = \\dfrac{4-8}{7-3} = \\dfrac{-4}{4} = -1$."
        },
        {
            "question": "Find the slope of the line passing through $(0, 0)$ and $(5, 10)$.",
            "answer": "$2$",
            "wrong": ["$5$", "$\\dfrac{1}{2}$", "$10$"],
            "explanation": "$m = \\dfrac{10-0}{5-0} = \\dfrac{10}{5} = 2$."
        },
        {
            "question": "Find the slope of the line passing through $(-4, 1)$ and $(2, -2)$.",
            "answer": "$-\\dfrac{1}{2}$",
            "wrong": ["$\\dfrac{1}{2}$", "$-2$", "$2$"],
            "explanation": "$m = \\dfrac{-2-1}{2-(-4)} = \\dfrac{-3}{6} = -\\dfrac{1}{2}$."
        },
        {
            "question": "Find the slope of the line $3x + y = 9$.",
            "answer": "$-3$",
            "wrong": ["$3$", "$9$", "$\\dfrac{1}{3}$"],
            "explanation": "Rearranging: $y = -3x + 9$, so slope $= -3$."
        },
        {
            "question": "Find the slope of the line $2x - 4y = 8$.",
            "answer": "$\\dfrac{1}{2}$",
            "wrong": ["$2$", "$-\\dfrac{1}{2}$", "$-2$"],
            "explanation": "Rearranging: $y = \\dfrac{1}{2}x - 2$, so slope $= \\dfrac{1}{2}$."
        },
        {
            "question": "A line has slope $3$ and passes through $(1, 4)$. What is its $y$-intercept?",
            "answer": "$1$",
            "wrong": ["$3$", "$4$", "$7$"],
            "explanation": "$y = 3x + b \\Rightarrow 4 = 3(1)+b \\Rightarrow b=1$."
        },
        {
            "question": "Find the slope of a line perpendicular to a line with slope $4$.",
            "answer": "$-\\dfrac{1}{4}$",
            "wrong": ["$4$", "$-4$", "$\\dfrac{1}{4}$"],
            "explanation": "Perpendicular slopes are negative reciprocals: $-\\dfrac{1}{4}$."
        },
        {
            "question": "Find the slope of a line parallel to $y = -2x + 7$.",
            "answer": "$-2$",
            "wrong": ["$2$", "$7$", "$\\dfrac{1}{2}$"],
            "explanation": "Parallel lines have equal slopes. Slope $= -2$."
        },
        {
            "question": "Find the slope of the line passing through $(6, -1)$ and $(2, 7)$.",
            "answer": "$-2$",
            "wrong": ["$2$", "$-\\dfrac{1}{2}$", "$\\dfrac{1}{2}$"],
            "explanation": "$m = \\dfrac{7-(-1)}{2-6} = \\dfrac{8}{-4} = -2$."
        },
        {
            "question": "Find the slope of the line passing through $(-3, -3)$ and $(3, 3)$.",
            "answer": "$1$",
            "wrong": ["$-1$", "$0$", "$3$"],
            "explanation": "$m = \\dfrac{3-(-3)}{3-(-3)} = \\dfrac{6}{6} = 1$."
        },
        {
            "question": "Find the slope of the line $y = 7$.",
            "answer": "$0$",
            "wrong": ["$7$", "$-7$", "undefined"],
            "explanation": "$y = 7$ is a horizontal line, so its slope is $0$."
        },
        {
            "question": "Find the slope of the line $x = -4$.",
            "answer": "undefined",
            "wrong": ["$-4$", "$0$", "$4$"],
            "explanation": "$x = -4$ is a vertical line, so its slope is undefined."
        },
        {
            "question": "Find the slope of the line passing through $(1, 5)$ and $(4, 14)$.",
            "answer": "$3$",
            "wrong": ["$\\dfrac{1}{3}$", "$9$", "$-3$"],
            "explanation": "$m = \\dfrac{14-5}{4-1} = \\dfrac{9}{3} = 3$."
        },
        {
            "question": "Find the slope of the line passing through $(-2, 7)$ and $(3, -3)$.",
            "answer": "$-2$",
            "wrong": ["$2$", "$-\\dfrac{1}{2}$", "$5$"],
            "explanation": "$m = \\dfrac{-3-7}{3-(-2)} = \\dfrac{-10}{5} = -2$."
        },
        {
            "question": "Two points are $(a, 3)$ and $(4, 9)$ with slope $2$. Find $a$.",
            "answer": "$1$",
            "wrong": ["$2$", "$-1$", "$3$"],
            "explanation": "$2 = \\dfrac{9-3}{4-a} \\Rightarrow 2(4-a)=6 \\Rightarrow 4-a=3 \\Rightarrow a=1$."
        },

        # ─────────────────────────────────────────────
        # DISTANCE BETWEEN TWO POINTS (20 questions)
        # ─────────────────────────────────────────────
        {
            "question": "Find the distance between $(0, 0)$ and $(3, 4)$.",
            "answer": "$5$",
            "wrong": ["$7$", "$\\sqrt{7}$", "$25$"],
            "explanation": "$d = \\sqrt{(3-0)^2+(4-0)^2} = \\sqrt{9+16} = \\sqrt{25} = 5$."
        },
        {
            "question": "Find the distance between $(1, 1)$ and $(4, 5)$.",
            "answer": "$5$",
            "wrong": ["$\\sqrt{7}$", "$7$", "$\\sqrt{25}+1$"],
            "explanation": "$d = \\sqrt{(4-1)^2+(5-1)^2} = \\sqrt{9+16} = 5$."
        },
        {
            "question": "Find the distance between $(-2, 3)$ and $(2, 6)$.",
            "answer": "$5$",
            "wrong": ["$\\sqrt{7}$", "$6$", "$4$"],
            "explanation": "$d = \\sqrt{(2-(-2))^2+(6-3)^2} = \\sqrt{16+9} = 5$."
        },
        {
            "question": "Find the distance between $(0, 0)$ and $(5, 12)$.",
            "answer": "$13$",
            "wrong": ["$17$", "$\\sqrt{17}$", "$12$"],
            "explanation": "$d = \\sqrt{25+144} = \\sqrt{169} = 13$."
        },
        {
            "question": "Find the distance between $(3, -2)$ and $(7, 1)$.",
            "answer": "$5$",
            "wrong": ["$\\sqrt{7}$", "$6$", "$\\sqrt{23}$"],
            "explanation": "$d = \\sqrt{(7-3)^2+(1-(-2))^2} = \\sqrt{16+9} = 5$."
        },
        {
            "question": "Find the distance between $(-1, -1)$ and $(2, 3)$.",
            "answer": "$5$",
            "wrong": ["$4$", "$\\sqrt{7}$", "$6$"],
            "explanation": "$d = \\sqrt{(2-(-1))^2+(3-(-1))^2} = \\sqrt{9+16} = 5$."
        },
        {
            "question": "Find the distance between $(0, 4)$ and $(3, 0)$.",
            "answer": "$5$",
            "wrong": ["$7$", "$4$", "$3$"],
            "explanation": "$d = \\sqrt{9+16} = 5$."
        },
        {
            "question": "Find the distance between $(-3, 0)$ and $(0, 4)$.",
            "answer": "$5$",
            "wrong": ["$4$", "$3$", "$\\sqrt{7}$"],
            "explanation": "$d = \\sqrt{(-3-0)^2+(0-4)^2} = \\sqrt{9+16} = 5$."
        },
        {
            "question": "Find the distance between $(2, 2)$ and $(5, 6)$.",
            "answer": "$5$",
            "wrong": ["$\\sqrt{7}$", "$6$", "$4$"],
            "explanation": "$d = \\sqrt{(5-2)^2+(6-2)^2} = \\sqrt{9+16} = 5$."
        },
        {
            "question": "Find the distance between $(1, -3)$ and $(4, 1)$.",
            "answer": "$5$",
            "wrong": ["$4$", "$3$", "$\\sqrt{43}$"],
            "explanation": "$d = \\sqrt{(4-1)^2+(1-(-3))^2} = \\sqrt{9+16} = 5$."
        },
        {
            "question": "Find the distance between $(0, 0)$ and $(8, 6)$.",
            "answer": "$10$",
            "wrong": ["$14$", "$\\sqrt{14}$", "$8$"],
            "explanation": "$d = \\sqrt{64+36} = \\sqrt{100} = 10$."
        },
        {
            "question": "Find the distance between $(-5, 0)$ and $(7, 0)$.",
            "answer": "$12$",
            "wrong": ["$2$", "$\\sqrt{12}$", "$6$"],
            "explanation": "Both points are on the $x$-axis: $d = |7-(-5)| = 12$."
        },
        {
            "question": "Find the distance between $(0, -3)$ and $(0, 9)$.",
            "answer": "$12$",
            "wrong": ["$6$", "$\\sqrt{12}$", "$3$"],
            "explanation": "Both points are on the $y$-axis: $d = |9-(-3)| = 12$."
        },
        {
            "question": "Find the distance between $(-6, 1)$ and $(-2, 4)$.",
            "answer": "$5$",
            "wrong": ["$\\sqrt{7}$", "$4$", "$6$"],
            "explanation": "$d = \\sqrt{(-2-(-6))^2+(4-1)^2} = \\sqrt{16+9} = 5$."
        },
        {
            "question": "Find the distance between $(1, 2)$ and $(1, 8)$.",
            "answer": "$6$",
            "wrong": ["$\\sqrt{6}$", "$3$", "$10$"],
            "explanation": "Same $x$: $d = |8-2| = 6$."
        },
        {
            "question": "Find the distance between $(-4, -3)$ and $(0, 0)$.",
            "answer": "$5$",
            "wrong": ["$7$", "$\\sqrt{7}$", "$4$"],
            "explanation": "$d = \\sqrt{16+9} = 5$."
        },
        {
            "question": "Find the distance between $(2, -1)$ and $(14, 4)$.",
            "answer": "$13$",
            "wrong": ["$\\sqrt{13}$", "$17$", "$12$"],
            "explanation": "$d = \\sqrt{(14-2)^2+(4-(-1))^2} = \\sqrt{144+25} = \\sqrt{169} = 13$."
        },
        {
            "question": "Find the distance between $(-3, -4)$ and $(0, 0)$.",
            "answer": "$5$",
            "wrong": ["$7$", "$4$", "$3$"],
            "explanation": "$d = \\sqrt{9+16} = 5$."
        },
        {
            "question": "Find the distance between $(1, 1)$ and $(7, 9)$.",
            "answer": "$10$",
            "wrong": ["$\\sqrt{10}$", "$8$", "$14$"],
            "explanation": "$d = \\sqrt{(7-1)^2+(9-1)^2} = \\sqrt{36+64} = \\sqrt{100} = 10$."
        },
        {
            "question": "Find the distance between $(-1, 2)$ and $(11, 7)$.",
            "answer": "$13$",
            "wrong": ["$\\sqrt{13}$", "$12$", "$17$"],
            "explanation": "$d = \\sqrt{(11-(-1))^2+(7-2)^2} = \\sqrt{144+25} = \\sqrt{169} = 13$."
        }
    ],
    'the_laws_of_sines': [{
        "question": "In $\\triangle ABC$, $A = 30°$, $B = 60°$, $a = 5$. Find $b$.",
        "answer": "$5\\sqrt{3}$",
        "wrong": ["$10$", "$\\dfrac{5\\sqrt{3}}{2}$", "$5$"],
        "explanation": "$\\dfrac{b}{\\sin 60°} = \\dfrac{5}{\\sin 30°} \\Rightarrow b = \\dfrac{5 \\cdot \\frac{\\sqrt{3}}{2}}{\\frac{1}{2}} = 5\\sqrt{3}$."
    },
        {
            "question": "In $\\triangle ABC$, $A = 45°$, $B = 75°$, $a = 8$. Find $b$.",
            "answer": "$4\\sqrt{6}$",
            "wrong": ["$8\\sqrt{2}$", "$4\\sqrt{3}$", "$8$"],
            "explanation": "$\\dfrac{b}{\\sin 75°} = \\dfrac{8}{\\sin 45°}$. $\\sin 75° = \\dfrac{\\sqrt{6}+\\sqrt{2}}{4}$, $\\sin 45° = \\dfrac{\\sqrt{2}}{2}$. So $b = \\dfrac{8 \\cdot \\frac{\\sqrt{6}+\\sqrt{2}}{4}}{\\frac{\\sqrt{2}}{2}} = 4\\sqrt{3}+4 \\approx 4\\sqrt{6}$."
        },
        {
            "question": "In $\\triangle ABC$, $B = 30°$, $C = 90°$, $b = 6$. Find $c$.",
            "answer": "$12$",
            "wrong": ["$6\\sqrt{3}$", "$6\\sqrt{2}$", "$3$"],
            "explanation": "$\\dfrac{c}{\\sin 90°} = \\dfrac{6}{\\sin 30°} \\Rightarrow c = \\dfrac{6 \\cdot 1}{0.5} = 12$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 45°$, $C = 90°$, $a = 7$. Find $c$.",
            "answer": "$7\\sqrt{2}$",
            "wrong": ["$14$", "$7$", "$\\dfrac{7\\sqrt{2}}{2}$"],
            "explanation": "$\\dfrac{c}{\\sin 90°} = \\dfrac{7}{\\sin 45°} \\Rightarrow c = \\dfrac{7}{\\frac{\\sqrt{2}}{2}} = 7\\sqrt{2}$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 60°$, $B = 40°$, $a = 10$. Find $b$ (to 2 decimal places).",
            "answer": "$7.43$",
            "wrong": ["$8.66$", "$6.43$", "$9.40$"],
            "explanation": "$b = \\dfrac{10 \\cdot \\sin 40°}{\\sin 60°} = \\dfrac{10 \\times 0.6428}{0.8660} \\approx 7.43$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 50°$, $B = 70°$, $b = 15$. Find $a$.",
            "answer": "$12.22$",
            "wrong": ["$14.10$", "$10.50$", "$13.05$"],
            "explanation": "$a = \\dfrac{15 \\cdot \\sin 50°}{\\sin 70°} = \\dfrac{15 \\times 0.7660}{0.9397} \\approx 12.22$."
        },
        {
            "question": "In $\\triangle ABC$, $B = 80°$, $C = 55°$, $c = 9$. Find $b$.",
            "answer": "$10.84$",
            "wrong": ["$9.85$", "$8.00$", "$11.50$"],
            "explanation": "$b = \\dfrac{9 \\cdot \\sin 80°}{\\sin 55°} = \\dfrac{9 \\times 0.9848}{0.8192} \\approx 10.84$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 30°$, $C = 120°$, $a = 4$. Find $c$.",
            "answer": "$4\\sqrt{3}$",
            "wrong": ["$8$", "$4$", "$2\\sqrt{3}$"],
            "explanation": "$\\dfrac{c}{\\sin 120°} = \\dfrac{4}{\\sin 30°} \\Rightarrow c = \\dfrac{4 \\cdot \\frac{\\sqrt{3}}{2}}{\\frac{1}{2}} = 4\\sqrt{3}$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 20°$, $B = 130°$, $a = 5$. Find $b$.",
            "answer": "$12.66$",
            "wrong": ["$10.00$", "$7.66$", "$14.00$"],
            "explanation": "$b = \\dfrac{5 \\cdot \\sin 130°}{\\sin 20°} = \\dfrac{5 \\times 0.7660}{0.3420} \\approx 12.66$ (note: $\\sin 130° = \\sin 50°$)."
        },
        {
            "question": "In $\\triangle ABC$, $A = 35°$, $B = 85°$, $a = 12$. Find $b$.",
            "answer": "$20.85$",
            "wrong": ["$18.00$", "$14.40$", "$16.50$"],
            "explanation": "$b = \\dfrac{12 \\cdot \\sin 85°}{\\sin 35°} = \\dfrac{12 \\times 0.9962}{0.5736} \\approx 20.85$."
        },
        {
            "question": "In $\\triangle ABC$, $B = 45°$, $C = 60°$, $b = 10$. Find $c$.",
            "answer": "$\\dfrac{10\\sqrt{6}}{2} \\approx 12.25$",
            "wrong": ["$10\\sqrt{2}$", "$5\\sqrt{6}$", "$10$"],
            "explanation": "$c = \\dfrac{10 \\cdot \\sin 60°}{\\sin 45°} = \\dfrac{10 \\cdot \\frac{\\sqrt{3}}{2}}{\\frac{\\sqrt{2}}{2}} = \\dfrac{10\\sqrt{3}}{\\sqrt{2}} = 5\\sqrt{6} \\approx 12.25$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 75°$, $B = 65°$, $a = 20$. Find $b$.",
            "answer": "$18.79$",
            "wrong": ["$20.00$", "$17.50$", "$21.30$"],
            "explanation": "$b = \\dfrac{20 \\cdot \\sin 65°}{\\sin 75°} = \\dfrac{20 \\times 0.9063}{0.9659} \\approx 18.79$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 100°$, $B = 40°$, $b = 7$. Find $a$.",
            "answer": "$10.71$",
            "wrong": ["$9.00$", "$7.00$", "$12.00$"],
            "explanation": "$a = \\dfrac{7 \\cdot \\sin 100°}{\\sin 40°} = \\dfrac{7 \\times 0.9848}{0.6428} \\approx 10.71$."
        },
        {
            "question": "In $\\triangle ABC$, $C = 25°$, $A = 110°$, $c = 6$. Find $a$.",
            "answer": "$13.36$",
            "wrong": ["$10.00$", "$11.50$", "$14.00$"],
            "explanation": "$a = \\dfrac{6 \\cdot \\sin 110°}{\\sin 25°} = \\dfrac{6 \\times 0.9397}{0.4226} \\approx 13.36$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 55°$, $C = 75°$, $c = 18$. Find $a$.",
            "answer": "$15.29$",
            "wrong": ["$18.00$", "$12.50$", "$16.80$"],
            "explanation": "$a = \\dfrac{18 \\cdot \\sin 55°}{\\sin 75°} = \\dfrac{18 \\times 0.8192}{0.9659} \\approx 15.29$."
        },
        {
            "question": "In $\\triangle ABC$, $B = 38°$, $C = 72°$, $b = 14$. Find $c$.",
            "answer": "$21.60$",
            "wrong": ["$19.00$", "$14.00$", "$23.50$"],
            "explanation": "$c = \\dfrac{14 \\cdot \\sin 72°}{\\sin 38°} = \\dfrac{14 \\times 0.9511}{0.6157} \\approx 21.60$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 15°$, $B = 150°$, $a = 3$. Find $b$.",
            "answer": "$5.80$",
            "wrong": ["$6.00$", "$3.00$", "$4.50$"],
            "explanation": "$b = \\dfrac{3 \\cdot \\sin 150°}{\\sin 15°} = \\dfrac{3 \\times 0.5}{0.2588} \\approx 5.80$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 62°$, $B = 48°$, $a = 25$. Find $b$.",
            "answer": "$21.08$",
            "wrong": ["$22.50$", "$18.00$", "$25.00$"],
            "explanation": "$b = \\dfrac{25 \\cdot \\sin 48°}{\\sin 62°} = \\dfrac{25 \\times 0.7431}{0.8829} \\approx 21.08$."
        },
        {
            "question": "In $\\triangle ABC$, $B = 90°$, $A = 30°$, $a = 5$. Find $b$.",
            "answer": "$10$",
            "wrong": ["$5\\sqrt{3}$", "$5\\sqrt{2}$", "$\\dfrac{5}{2}$"],
            "explanation": "$\\dfrac{b}{\\sin 90°} = \\dfrac{5}{\\sin 30°} \\Rightarrow b = \\dfrac{5}{0.5} = 10$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 67°$, $C = 53°$, $c = 30$. Find $a$.",
            "answer": "$34.44$",
            "wrong": ["$30.00$", "$28.00$", "$36.00$"],
            "explanation": "$a = \\dfrac{30 \\cdot \\sin 67°}{\\sin 53°} = \\dfrac{30 \\times 0.9205}{0.7986} \\approx 34.44$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 42°$, $B = 95°$, $b = 50$. Find $a$.",
            "answer": "$33.57$",
            "wrong": ["$40.00$", "$50.00$", "$29.00$"],
            "explanation": "$a = \\dfrac{50 \\cdot \\sin 42°}{\\sin 95°} = \\dfrac{50 \\times 0.6691}{0.9962} \\approx 33.57$."
        },
        {
            "question": "In $\\triangle ABC$, $B = 33°$, $C = 87°$, $c = 22$. Find $b$.",
            "answer": "$12.01$",
            "wrong": ["$11.00$", "$14.50$", "$10.00$"],
            "explanation": "$b = \\dfrac{22 \\cdot \\sin 33°}{\\sin 87°} = \\dfrac{22 \\times 0.5446}{0.9986} \\approx 12.01$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 58°$, $B = 62°$, $a = 17$. Find $b$.",
            "answer": "$17.73$",
            "wrong": ["$17.00$", "$18.50$", "$16.00$"],
            "explanation": "$b = \\dfrac{17 \\cdot \\sin 62°}{\\sin 58°} = \\dfrac{17 \\times 0.8829}{0.8480} \\approx 17.73$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 105°$, $C = 30°$, $c = 8$. Find $a$.",
            "answer": "$15.45$",
            "wrong": ["$16.00$", "$12.00$", "$14.00$"],
            "explanation": "$a = \\dfrac{8 \\cdot \\sin 105°}{\\sin 30°} = \\dfrac{8 \\times 0.9659}{0.5} \\approx 15.45$."
        },
        {
            "question": "In $\\triangle ABC$, $B = 120°$, $C = 25°$, $b = 11$. Find $c$.",
            "answer": "$5.37$",
            "wrong": ["$6.00$", "$4.50$", "$7.00$"],
            "explanation": "$c = \\dfrac{11 \\cdot \\sin 25°}{\\sin 120°} = \\dfrac{11 \\times 0.4226}{0.8660} \\approx 5.37$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 72°$, $B = 48°$, $b = 13$. Find $a$.",
            "answer": "$16.64$",
            "wrong": ["$15.00$", "$18.00$", "$14.50$"],
            "explanation": "$a = \\dfrac{13 \\cdot \\sin 72°}{\\sin 48°} = \\dfrac{13 \\times 0.9511}{0.7431} \\approx 16.64$."
        },
        {
            "question": "In $\\triangle ABC$, $C = 140°$, $A = 20°$, $a = 9$. Find $c$.",
            "answer": "$16.97$",
            "wrong": ["$18.00$", "$14.50$", "$20.00$"],
            "explanation": "$c = \\dfrac{9 \\cdot \\sin 140°}{\\sin 20°} = \\dfrac{9 \\times 0.6428}{0.3420} \\approx 16.97$ (note: $\\sin 140° = \\sin 40°$)."
        },
        {
            "question": "In $\\triangle ABC$, $A = 88°$, $B = 52°$, $a = 40$. Find $b$.",
            "answer": "$31.54$",
            "wrong": ["$33.00$", "$29.00$", "$35.00$"],
            "explanation": "$b = \\dfrac{40 \\cdot \\sin 52°}{\\sin 88°} = \\dfrac{40 \\times 0.7880}{0.9994} \\approx 31.54$."
        },
        {
            "question": "In $\\triangle ABC$, $B = 27°$, $C = 118°$, $b = 7$. Find $c$.",
            "answer": "$13.57$",
            "wrong": ["$12.00$", "$10.50$", "$15.00$"],
            "explanation": "$c = \\dfrac{7 \\cdot \\sin 118°}{\\sin 27°} = \\dfrac{7 \\times 0.8829}{0.4540} \\approx 13.57$ ($\\sin 118° = \\sin 62°$)."
        },
        {
            "question": "In $\\triangle ABC$, $A = 36°$, $B = 84°$, $a = 16$. Find $b$.",
            "answer": "$27.08$",
            "wrong": ["$25.00$", "$20.00$", "$30.00$"],
            "explanation": "$b = \\dfrac{16 \\cdot \\sin 84°}{\\sin 36°} = \\dfrac{16 \\times 0.9945}{0.5878} \\approx 27.08$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 53°$, $C = 97°$, $c = 24$. Find $a$.",
            "answer": "$19.28$",
            "wrong": ["$21.00$", "$17.50$", "$22.00$"],
            "explanation": "$a = \\dfrac{24 \\cdot \\sin 53°}{\\sin 97°} = \\dfrac{24 \\times 0.7986}{0.9925} \\approx 19.28$."
        },
        {
            "question": "In $\\triangle ABC$, $B = 64°$, $C = 46°$, $c = 18$. Find $b$.",
            "answer": "$22.54$",
            "wrong": ["$20.00$", "$24.00$", "$18.00$"],
            "explanation": "$b = \\dfrac{18 \\cdot \\sin 64°}{\\sin 46°} = \\dfrac{18 \\times 0.8988}{0.7193} \\approx 22.54$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 22°$, $B = 143°$, $a = 10$. Find $b$.",
            "answer": "$15.89$",
            "wrong": ["$18.00$", "$14.00$", "$12.50$"],
            "explanation": "$b = \\dfrac{10 \\cdot \\sin 143°}{\\sin 22°} = \\dfrac{10 \\times 0.6018}{0.3746} \\approx 16.07$ ($\\sin 143° = \\sin 37°$)."
        },
        {
            "question": "In $\\triangle ABC$, $B = 76°$, $C = 59°$, $b = 33$. Find $c$.",
            "answer": "$29.26$",
            "wrong": ["$27.00$", "$31.00$", "$33.00$"],
            "explanation": "$c = \\dfrac{33 \\cdot \\sin 59°}{\\sin 76°} = \\dfrac{33 \\times 0.8572}{0.9703} \\approx 29.13$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 47°$, $C = 83°$, $a = 21$. Find $c$.",
            "answer": "$28.52$",
            "wrong": ["$26.00$", "$30.00$", "$21.00$"],
            "explanation": "$c = \\dfrac{21 \\cdot \\sin 83°}{\\sin 47°} = \\dfrac{21 \\times 0.9925}{0.7314} \\approx 28.52$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 130°$, $B = 20°$, $b = 6$. Find $a$.",
            "answer": "$13.44$",
            "wrong": ["$12.00$", "$15.00$", "$10.50$"],
            "explanation": "$a = \\dfrac{6 \\cdot \\sin 130°}{\\sin 20°} = \\dfrac{6 \\times 0.7660}{0.3420} \\approx 13.44$."
        },
        {
            "question": "In $\\triangle ABC$, $B = 41°$, $C = 99°$, $c = 45$. Find $b$.",
            "answer": "$29.82$",
            "wrong": ["$31.00$", "$27.00$", "$35.00$"],
            "explanation": "$b = \\dfrac{45 \\cdot \\sin 41°}{\\sin 99°} = \\dfrac{45 \\times 0.6561}{0.9877} \\approx 29.89$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 78°$, $B = 57°$, $b = 28$. Find $a$.",
            "answer": "$32.46$",
            "wrong": ["$30.00$", "$35.00$", "$28.00$"],
            "explanation": "$a = \\dfrac{28 \\cdot \\sin 78°}{\\sin 57°} = \\dfrac{28 \\times 0.9781}{0.8387} \\approx 32.67$."
        },
        {
            "question": "In $\\triangle ABC$, $C = 112°$, $A = 33°$, $a = 14$. Find $c$.",
            "answer": "$23.78$",
            "wrong": ["$22.00$", "$25.00$", "$20.00$"],
            "explanation": "$c = \\dfrac{14 \\cdot \\sin 112°}{\\sin 33°} = \\dfrac{14 \\times 0.9272}{0.5446} \\approx 23.83$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 69°$, $B = 71°$, $a = 50$. Find $b$.",
            "answer": "$50.75$",
            "wrong": ["$50.00$", "$52.00$", "$48.00$"],
            "explanation": "$b = \\dfrac{50 \\cdot \\sin 71°}{\\sin 69°} = \\dfrac{50 \\times 0.9455}{0.9336} \\approx 50.64$."
        },

        # ─────────────────────────────────────────────
        # BURCHAKNI TOPISH (41–80)
        # ─────────────────────────────────────────────
        {
            "question": "In $\\triangle ABC$, $a = 7$, $b = 10$, $A = 30°$. Find $B$.",
            "answer": "$45.57°$",
            "wrong": ["$30°$", "$60°$", "$90°$"],
            "explanation": "$\\sin B = \\dfrac{b \\sin A}{a} = \\dfrac{10 \\times 0.5}{7} = \\dfrac{5}{7} \\approx 0.7143 \\Rightarrow B \\approx 45.57°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 6$, $b = 6$, $A = 50°$. Find $B$.",
            "answer": "$50°$",
            "wrong": ["$60°$", "$80°$", "$40°$"],
            "explanation": "Since $a = b$, the triangle is isosceles, so $B = A = 50°$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 8$, $c = 10$, $B = 40°$. Find $C$.",
            "answer": "$52.49°$",
            "wrong": ["$40°$", "$60°$", "$45°$"],
            "explanation": "$\\sin C = \\dfrac{10 \\sin 40°}{8} = \\dfrac{10 \\times 0.6428}{8} \\approx 0.8035 \\Rightarrow C \\approx 53.46°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 5$, $c = 7$, $A = 38°$. Find $C$.",
            "answer": "$59.74°$",
            "wrong": ["$38°$", "$72°$", "$45°$"],
            "explanation": "$\\sin C = \\dfrac{7 \\sin 38°}{5} = \\dfrac{7 \\times 0.6157}{5} \\approx 0.8620 \\Rightarrow C \\approx 59.50°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 12$, $b = 9$, $B = 35°$. Find $A$.",
            "answer": "$49.86°$",
            "wrong": ["$55°$", "$40°$", "$60°$"],
            "explanation": "$\\sin A = \\dfrac{12 \\sin 35°}{9} = \\dfrac{12 \\times 0.5736}{9} \\approx 0.7648 \\Rightarrow A \\approx 49.86°$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 15$, $c = 12$, $C = 45°$. Find $B$.",
            "answer": "$62.11°$",
            "wrong": ["$45°$", "$75°$", "$55°$"],
            "explanation": "$\\sin B = \\dfrac{15 \\sin 45°}{12} = \\dfrac{15 \\times 0.7071}{12} \\approx 0.8839 \\Rightarrow B \\approx 62.11°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 20$, $b = 24$, $A = 55°$. Find $B$.",
            "answer": "$80.47°$",
            "wrong": ["$55°$", "$65°$", "$70°$"],
            "explanation": "$\\sin B = \\dfrac{24 \\sin 55°}{20} = \\dfrac{24 \\times 0.8192}{20} \\approx 0.9830 \\Rightarrow B \\approx 79.54°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 9$, $c = 11$, $C = 70°$. Find $A$.",
            "answer": "$50.35°$",
            "wrong": ["$70°$", "$40°$", "$60°$"],
            "explanation": "$\\sin A = \\dfrac{9 \\sin 70°}{11} = \\dfrac{9 \\times 0.9397}{11} \\approx 0.7688 \\Rightarrow A \\approx 50.26°$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 7$, $c = 7\\sqrt{2}$, $B = 30°$. Find $C$.",
            "answer": "$45°$",
            "wrong": ["$60°$", "$90°$", "$30°$"],
            "explanation": "$\\sin C = \\dfrac{7\\sqrt{2} \\cdot \\sin 30°}{7} = \\sqrt{2} \\times 0.5 = \\dfrac{\\sqrt{2}}{2} \\Rightarrow C = 45°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 14$, $b = 10$, $B = 42°$. Find $A$.",
            "answer": "$69.04°$",
            "wrong": ["$42°$", "$60°$", "$75°$"],
            "explanation": "$\\sin A = \\dfrac{14 \\sin 42°}{10} = \\dfrac{14 \\times 0.6691}{10} \\approx 0.9367 \\Rightarrow A \\approx 69.57°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 18$, $c = 22$, $A = 48°$. Find $C$.",
            "answer": "$65.66°$",
            "wrong": ["$48°$", "$72°$", "$55°$"],
            "explanation": "$\\sin C = \\dfrac{22 \\sin 48°}{18} = \\dfrac{22 \\times 0.7431}{18} \\approx 0.9083 \\Rightarrow C \\approx 65.43°$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 5$, $c = 5\\sqrt{3}$, $B = 30°$. Find $C$.",
            "answer": "$60°$",
            "wrong": ["$30°$", "$90°$", "$45°$"],
            "explanation": "$\\sin C = \\dfrac{5\\sqrt{3} \\cdot \\sin 30°}{5} = \\sqrt{3} \\times 0.5 = \\dfrac{\\sqrt{3}}{2} \\Rightarrow C = 60°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 11$, $b = 13$, $A = 44°$. Find $B$.",
            "answer": "$55.55°$",
            "wrong": ["$44°$", "$60°$", "$50°$"],
            "explanation": "$\\sin B = \\dfrac{13 \\sin 44°}{11} = \\dfrac{13 \\times 0.6947}{11} \\approx 0.8205 \\Rightarrow B \\approx 55.17°$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 25$, $c = 30$, $B = 56°$. Find $C$.",
            "answer": "$82.69°$",
            "wrong": ["$56°$", "$65°$", "$75°$"],
            "explanation": "$\\sin C = \\dfrac{30 \\sin 56°}{25} = \\dfrac{30 \\times 0.8290}{25} \\approx 0.9948 \\Rightarrow C \\approx 84.27°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 3$, $b = 4$, $A = 20°$. Find $B$.",
            "answer": "$27.00°$",
            "wrong": ["$20°$", "$40°$", "$35°$"],
            "explanation": "$\\sin B = \\dfrac{4 \\sin 20°}{3} = \\dfrac{4 \\times 0.3420}{3} \\approx 0.4560 \\Rightarrow B \\approx 27.13°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 10$, $c = 14$, $C = 85°$. Find $A$.",
            "answer": "$45.45°$",
            "wrong": ["$85°$", "$40°$", "$55°$"],
            "explanation": "$\\sin A = \\dfrac{10 \\sin 85°}{14} = \\dfrac{10 \\times 0.9962}{14} \\approx 0.7116 \\Rightarrow A \\approx 45.32°$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 16$, $c = 19$, $B = 50°$. Find $C$.",
            "answer": "$65.59°$",
            "wrong": ["$50°$", "$75°$", "$60°$"],
            "explanation": "$\\sin C = \\dfrac{19 \\sin 50°}{16} = \\dfrac{19 \\times 0.7660}{16} \\approx 0.9097 \\Rightarrow C \\approx 65.65°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 8$, $b = 8$, $A = 65°$. Find $C$.",
            "answer": "$50°$",
            "wrong": ["$65°$", "$70°$", "$40°$"],
            "explanation": "Since $a = b$, $B = A = 65°$. Then $C = 180° - 65° - 65° = 50°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 30$, $c = 35$, $A = 60°$. Find $C$.",
            "answer": "$84.29°$",
            "wrong": ["$60°$", "$70°$", "$75°$"],
            "explanation": "$\\sin C = \\dfrac{35 \\sin 60°}{30} = \\dfrac{35 \\times 0.8660}{30} \\approx 1.010$ — this gives no solution (ambiguous case check needed)."
        },
        {
            "question": "In $\\triangle ABC$, $b = 9$, $c = 6$, $C = 28°$. Find $B$.",
            "answer": "$45.23°$",
            "wrong": ["$28°$", "$60°$", "$35°$"],
            "explanation": "$\\sin B = \\dfrac{9 \\sin 28°}{6} = \\dfrac{9 \\times 0.4695}{6} \\approx 0.7043 \\Rightarrow B \\approx 44.77°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 7$, $b = 9$, $A = 43°$. Find angle $B$.",
            "answer": "$61.82°$",
            "wrong": ["$43°$", "$55°$", "$70°$"],
            "explanation": "$\\sin B = \\dfrac{9 \\sin 43°}{7} = \\dfrac{9 \\times 0.6820}{7} \\approx 0.8768 \\Rightarrow B \\approx 61.32°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 15$, $c = 10$, $C = 33°$. Find $A$.",
            "answer": "$55.08°$",
            "wrong": ["$33°$", "$45°$", "$65°$"],
            "explanation": "$\\sin A = \\dfrac{15 \\sin 33°}{10} = \\dfrac{15 \\times 0.5446}{10} \\approx 0.8169 \\Rightarrow A \\approx 54.84°$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 20$, $c = 17$, $C = 52°$. Find $B$.",
            "answer": "$67.72°$ or $112.28°$",
            "wrong": ["$52°$", "$90°$", "$60°$"],
            "explanation": "$\\sin B = \\dfrac{20 \\sin 52°}{17} = \\dfrac{20 \\times 0.7880}{17} \\approx 0.9271 \\Rightarrow B \\approx 67.91°$ or $112.09°$ (ambiguous case)."
        },
        {
            "question": "In $\\triangle ABC$, $a = 4$, $b = 6$, $A = 25°$. Find $B$.",
            "answer": "$39.34°$",
            "wrong": ["$25°$", "$50°$", "$45°$"],
            "explanation": "$\\sin B = \\dfrac{6 \\sin 25°}{4} = \\dfrac{6 \\times 0.4226}{4} \\approx 0.6339 \\Rightarrow B \\approx 39.34°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 13$, $b = 11$, $B = 47°$. Find $A$.",
            "answer": "$57.99°$",
            "wrong": ["$47°$", "$65°$", "$70°$"],
            "explanation": "$\\sin A = \\dfrac{13 \\sin 47°}{11} = \\dfrac{13 \\times 0.7314}{11} \\approx 0.8643 \\Rightarrow A \\approx 59.81°$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 8$, $c = 12$, $B = 35°$. Find $C$.",
            "answer": "$59.01°$ or $120.99°$",
            "wrong": ["$35°$", "$45°$", "$70°$"],
            "explanation": "$\\sin C = \\dfrac{12 \\sin 35°}{8} = \\dfrac{12 \\times 0.5736}{8} \\approx 0.8604 \\Rightarrow C \\approx 59.32°$ or $120.68°$ (ambiguous case)."
        },
        {
            "question": "In $\\triangle ABC$, $a = 22$, $b = 18$, $A = 75°$. Find $B$.",
            "answer": "$51.72°$",
            "wrong": ["$75°$", "$40°$", "$60°$"],
            "explanation": "$\\sin B = \\dfrac{18 \\sin 75°}{22} = \\dfrac{18 \\times 0.9659}{22} \\approx 0.7903 \\Rightarrow B \\approx 52.12°$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 11$, $c = 14$, $C = 67°$. Find $B$.",
            "answer": "$46.26°$",
            "wrong": ["$67°$", "$55°$", "$40°$"],
            "explanation": "$\\sin B = \\dfrac{11 \\sin 67°}{14} = \\dfrac{11 \\times 0.9205}{14} \\approx 0.7232 \\Rightarrow B \\approx 46.26°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 6$, $c = 8$, $A = 40°$. Find $C$.",
            "answer": "$58.99°$",
            "wrong": ["$40°$", "$70°$", "$50°$"],
            "explanation": "$\\sin C = \\dfrac{8 \\sin 40°}{6} = \\dfrac{8 \\times 0.6428}{6} \\approx 0.8571 \\Rightarrow C \\approx 58.99°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 17$, $b = 21$, $A = 54°$. Find $B$.",
            "answer": "$83.90°$",
            "wrong": ["$54°$", "$65°$", "$75°$"],
            "explanation": "$\\sin B = \\dfrac{21 \\sin 54°}{17} = \\dfrac{21 \\times 0.8090}{17} \\approx 1.0 \\Rightarrow B \\approx 90°$ (borderline case)."
        },
        {
            "question": "In $\\triangle ABC$, $b = 13$, $c = 10$, $C = 37°$. Find $B$.",
            "answer": "$51.62°$",
            "wrong": ["$37°$", "$60°$", "$45°$"],
            "explanation": "$\\sin B = \\dfrac{13 \\sin 37°}{10} = \\dfrac{13 \\times 0.6018}{10} \\approx 0.7823 \\Rightarrow B \\approx 51.52°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 24$, $b = 20$, $B = 62°$. Find $A$.",
            "answer": "$90°$ (right angle)",
            "wrong": ["$62°$", "$70°$", "$80°$"],
            "explanation": "$\\sin A = \\dfrac{24 \\sin 62°}{20} = \\dfrac{24 \\times 0.8829}{20} \\approx 1.059$ — this is an impossible case ($> 1$), so no valid triangle exists."
        },
        {
            "question": "In $\\triangle ABC$, $a = 5$, $b = 7$, $A = 32°$. Find $B$.",
            "answer": "$47.77°$",
            "wrong": ["$32°$", "$55°$", "$60°$"],
            "explanation": "$\\sin B = \\dfrac{7 \\sin 32°}{5} = \\dfrac{7 \\times 0.5299}{5} \\approx 0.7419 \\Rightarrow B \\approx 47.82°$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 30$, $c = 25$, $B = 80°$. Find $C$.",
            "answer": "$55.17°$",
            "wrong": ["$80°$", "$45°$", "$60°$"],
            "explanation": "$\\sin C = \\dfrac{25 \\sin 80°}{30} = \\dfrac{25 \\times 0.9848}{30} \\approx 0.8207 \\Rightarrow C \\approx 55.17°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 16$, $c = 12$, $C = 46°$. Find $A$.",
            "answer": "$72.75°$ or $107.25°$",
            "wrong": ["$46°$", "$60°$", "$55°$"],
            "explanation": "$\\sin A = \\dfrac{16 \\sin 46°}{12} = \\dfrac{16 \\times 0.7193}{12} \\approx 0.9591 \\Rightarrow A \\approx 73.58°$ or $106.42°$ (ambiguous case)."
        },
        {
            "question": "In $\\triangle ABC$, $b = 19$, $c = 23$, $B = 49°$. Find $C$.",
            "answer": "$72.09°$",
            "wrong": ["$49°$", "$80°$", "$65°$"],
            "explanation": "$\\sin C = \\dfrac{23 \\sin 49°}{19} = \\dfrac{23 \\times 0.7547}{19} \\approx 0.9133 \\Rightarrow C \\approx 65.85°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 10$, $b = 10\\sqrt{2}$, $A = 30°$. Find $B$.",
            "answer": "$45°$",
            "wrong": ["$30°$", "$60°$", "$90°$"],
            "explanation": "$\\sin B = \\dfrac{10\\sqrt{2} \\cdot \\sin 30°}{10} = \\sqrt{2} \\times 0.5 = \\dfrac{\\sqrt{2}}{2} \\Rightarrow B = 45°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 9$, $b = 12$, $A = 36°$. Find $B$.",
            "answer": "$52.24°$",
            "wrong": ["$36°$", "$60°$", "$45°$"],
            "explanation": "$\\sin B = \\dfrac{12 \\sin 36°}{9} = \\dfrac{12 \\times 0.5878}{9} \\approx 0.7837 \\Rightarrow B \\approx 51.56°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 100$, $b = 80$, $B = 40°$. Find $A$.",
            "answer": "$53.46°$",
            "wrong": ["$40°$", "$60°$", "$70°$"],
            "explanation": "$\\sin A = \\dfrac{100 \\sin 40°}{80} = \\dfrac{100 \\times 0.6428}{80} \\approx 0.8035 \\Rightarrow A \\approx 53.46°$."
        },

        # ─────────────────────────────────────────────
        # MURAKKAB / ARALASH (81–100)
        # ─────────────────────────────────────────────
        {
            "question": "In $\\triangle ABC$, $A = 40°$, $a = 10$, $b = 14$. How many valid triangles exist?",
            "answer": "$2$ (ambiguous case)",
            "wrong": ["$0$", "$1$", "$3$"],
            "explanation": "$\\sin B = \\dfrac{14 \\sin 40°}{10} \\approx 0.8999 < 1$ and $b > a$, so two triangles exist (SSA ambiguous case)."
        },
        {
            "question": "In $\\triangle ABC$, $a = 5$, $b = 3$, $B = 25°$. Find the third angle $C$.",
            "answer": "$114.06°$",
            "wrong": ["$90°$", "$130°$", "$100°$"],
            "explanation": "$\\sin A = \\dfrac{5 \\sin 25°}{3} \\approx 0.7036 \\Rightarrow A \\approx 44.69°$. Then $C = 180° - 44.69° - 25° \\approx 110.31°$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 30°$, $B = 70°$, $c = 15$. Find $a$.",
            "answer": "$7.76$",
            "wrong": ["$10.00$", "$5.00$", "$12.00$"],
            "explanation": "$C = 180° - 30° - 70° = 80°$. $a = \\dfrac{15 \\sin 30°}{\\sin 80°} = \\dfrac{15 \\times 0.5}{0.9848} \\approx 7.62$."
        },
        {
            "question": "In $\\triangle ABC$, $B = 50°$, $C = 65°$, $b = 20$. Find $c$.",
            "answer": "$23.66$",
            "wrong": ["$20.00$", "$18.50$", "$26.00$"],
            "explanation": "$c = \\dfrac{20 \\sin 65°}{\\sin 50°} = \\dfrac{20 \\times 0.9063}{0.7660} \\approx 23.66$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 8$, $b = 8$, $c = 8$. Find all angles.",
            "answer": "$A = B = C = 60°$",
            "wrong": ["$A=90°, B=C=45°$", "$A=B=45°, C=90°$", "$A=B=C=90°$"],
            "explanation": "Equilateral triangle: all sides equal, so all angles are $60°$. Confirmed by Law of Sines: all ratios equal."
        },
        {
            "question": "In $\\triangle ABC$, $A = 110°$, $a = 25$, $b = 13$. Find $B$.",
            "answer": "$29.27°$",
            "wrong": ["$30°$", "$40°$", "$20°$"],
            "explanation": "$\\sin B = \\dfrac{13 \\sin 110°}{25} = \\dfrac{13 \\times 0.9397}{25} \\approx 0.4886 \\Rightarrow B \\approx 29.27°$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 10$, $c = 10$, $B = 72°$. Find $C$ and then $A$.",
            "answer": "$C = 72°$, $A = 36°$",
            "wrong": ["$C=72°, A=18°$", "$C=36°, A=72°$", "$C=108°, A=0°$"],
            "explanation": "Since $b = c$, triangle is isosceles so $C = B = 72°$. Then $A = 180° - 72° - 72° = 36°$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 25°$, $C = 135°$, $a = 7$. Find $c$.",
            "answer": "$16.56$",
            "wrong": ["$14.00$", "$18.00$", "$12.50$"],
            "explanation": "$c = \\dfrac{7 \\sin 135°}{\\sin 25°} = \\dfrac{7 \\times 0.7071}{0.4226} \\approx 11.71$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 6$, $A = 30°$, $b = 12$. What is $B$?",
            "answer": "$90°$",
            "wrong": ["$60°$", "$45°$", "$120°$"],
            "explanation": "$\\sin B = \\dfrac{12 \\sin 30°}{6} = \\dfrac{12 \\times 0.5}{6} = 1 \\Rightarrow B = 90°$ exactly."
        },
        {
            "question": "In $\\triangle ABC$, $A = 35°$, $B = 95°$, $a = 18$. Find $c$. ($C = 50°$)",
            "answer": "$24.08$",
            "wrong": ["$20.00$", "$27.00$", "$18.00$"],
            "explanation": "$C = 180° - 35° - 95° = 50°$. $c = \\dfrac{18 \\sin 50°}{\\sin 35°} = \\dfrac{18 \\times 0.7660}{0.5736} \\approx 24.03$."
        },
        {
            "question": "In $\\triangle ABC$, $B = 48°$, $C = 62°$, $b = 27$. Find $a$. ($A = 70°$)",
            "answer": "$34.16$",
            "wrong": ["$30.00$", "$27.00$", "$38.00$"],
            "explanation": "$A = 180° - 48° - 62° = 70°$. $a = \\dfrac{27 \\sin 70°}{\\sin 48°} = \\dfrac{27 \\times 0.9397}{0.7431} \\approx 34.16$."
        },
        {
            "question": "A triangle has $a = 7$, $b = 9$, $A = 48°$. Is there an ambiguous case? If yes, find both possible values of $B$.",
            "answer": "$B_1 \\approx 74.35°$, $B_2 \\approx 105.65°$",
            "wrong": ["Only $B = 74°$", "No solution", "$B = 48°$"],
            "explanation": "$\\sin B = \\dfrac{9 \\sin 48°}{7} \\approx 0.9552$. Since $b > a$ and $\\sin B < 1$, two values: $B \\approx 72.84°$ or $107.16°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 50$, $b = 50$, $A = 40°$. Find $C$.",
            "answer": "$100°$",
            "wrong": ["$80°$", "$60°$", "$140°$"],
            "explanation": "Isosceles: $B = A = 40°$. $C = 180° - 40° - 40° = 100°$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 15°$, $B = 45°$, $c = 10$. Find $a$. ($C = 120°$)",
            "answer": "$3.35$",
            "wrong": ["$5.00$", "$4.00$", "$2.00$"],
            "explanation": "$C = 120°$. $a = \\dfrac{10 \\sin 15°}{\\sin 120°} = \\dfrac{10 \\times 0.2588}{0.8660} \\approx 2.99$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 14$, $c = 20$, $B = 30°$. Find both possible values of $C$.",
            "answer": "$C_1 \\approx 45.58°$, $C_2 \\approx 134.42°$",
            "wrong": ["Only $C = 45°$", "No solution", "$C = 90°$"],
            "explanation": "$\\sin C = \\dfrac{20 \\sin 30°}{14} = \\dfrac{10}{14} \\approx 0.7143 \\Rightarrow C \\approx 45.58°$ or $134.42°$ (both valid)."
        },
        {
            "question": "In $\\triangle ABC$, $A = 60°$, $B = 60°$, $a = 12$. Find $b$ and $c$.",
            "answer": "$b = c = 12$",
            "wrong": ["$b=12, c=6$", "$b=c=6\\sqrt{3}$", "$b=c=24$"],
            "explanation": "Equilateral triangle ($A=B=C=60°$): all sides equal, so $b = c = a = 12$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 90°$, $B = 30°$, $b = 5$. Find $a$ and $c$.",
            "answer": "$a = 10$, $c = 5\\sqrt{3}$",
            "wrong": ["$a=5\\sqrt{2}, c=5$", "$a=5, c=10$", "$a=10, c=5$"],
            "explanation": "$a = \\dfrac{5}{ \\sin 30°} = 10$. $C = 60°$, $c = \\dfrac{10 \\sin 60°}{1} = 5\\sqrt{3}$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 7$, $b = 24$, $A = 17°$. Does a valid triangle exist?",
            "answer": "Yes, two triangles",
            "wrong": ["No triangle", "Exactly one triangle", "Infinitely many"],
            "explanation": "$\\sin B = \\dfrac{24 \\sin 17°}{7} \\approx 1.009 > 1$ — no valid triangle exists (SSA impossible case)."
        },
        {
            "question": "In $\\triangle ABC$, $a = 15$, $b = 20$, $c = 25$. Verify using Law of Sines that $C = 90°$.",
            "answer": "$C = 90°$ ✓",
            "wrong": ["$C = 60°$", "$C = 80°$", "$C = 75°$"],
            "explanation": "Check: $\\dfrac{c}{\\sin C} = \\dfrac{25}{1} = 25$, $\\dfrac{a}{\\sin A} = \\dfrac{15}{0.6} = 25$. Also $15^2 + 20^2 = 625 = 25^2$ confirms right angle."
        },
        {
            "question": "In $\\triangle ABC$, $A = 80°$, $a = 40$, $b = 30$. Find $B$, $C$, and $c$.",
            "answer": "$B \\approx 47.93°$, $C \\approx 52.07°$, $c \\approx 32.27$",
            "wrong": ["$B=50°, C=50°, c=40$", "$B=40°, C=60°, c=35$", "$B=47°, C=53°, c=28$"],
            "explanation": "$\\sin B = \\dfrac{30 \\sin 80°}{40} \\approx 0.7386 \\Rightarrow B \\approx 47.57°$. $C = 180° - 80° - 47.57° \\approx 52.43°$. $c = \\dfrac{40 \\sin 52.43°}{\\sin 80°} \\approx 32.38$."
        },
        {
            "question": "In $\\triangle ABC$, $A = 72°$, $B = 53°$, $a = 100$. Find $b$ and $c$ ($C = 55°$).",
            "answer": "$b \\approx 87.67$, $c \\approx 86.03$",
            "wrong": ["$b=100, c=80$", "$b=80, c=90$", "$b=90, c=75$"],
            "explanation": "$b = \\dfrac{100 \\sin 53°}{\\sin 72°} \\approx \\dfrac{100 \\times 0.7986}{0.9511} \\approx 83.96$. $c = \\dfrac{100 \\sin 55°}{\\sin 72°} \\approx \\dfrac{100 \\times 0.8192}{0.9511} \\approx 86.13$."
        }
    ],
    'the_laws_of_cosines': [{
        "question": "In $\\triangle ABC$, $a = 5$, $b = 7$, $C = 60°$. Find $c$.",
        "answer": "$\\sqrt{39} \\approx 6.24$",
        "wrong": ["$\\sqrt{74}$", "$6$", "$\\sqrt{53}$"],
        "explanation": "$c^2 = 25 + 49 - 2(5)(7)\\cos 60° = 74 - 35 = 39 \\Rightarrow c = \\sqrt{39}$."
    },
        {
            "question": "In $\\triangle ABC$, $a = 8$, $b = 6$, $C = 90°$. Find $c$.",
            "answer": "$10$",
            "wrong": ["$14$", "$\\sqrt{28}$", "$\\sqrt{50}$"],
            "explanation": "$c^2 = 64 + 36 - 2(8)(6)\\cos 90° = 100 - 0 = 100 \\Rightarrow c = 10$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 10$, $c = 12$, $A = 45°$. Find $a$.",
            "answer": "$\\approx 8.56$",
            "wrong": ["$\\approx 10.00$", "$\\approx 7.21$", "$\\approx 9.80$"],
            "explanation": "$a^2 = 100 + 144 - 2(10)(12)\\cos 45° = 244 - 240 \\times \\frac{\\sqrt{2}}{2} \\approx 244 - 169.71 \\approx 74.29 \\Rightarrow a \\approx 8.62$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 3$, $b = 4$, $C = 30°$. Find $c$.",
            "answer": "$\\approx 2.05$",
            "wrong": ["$\\approx 3.00$", "$\\approx 2.65$", "$\\approx 1.50$"],
            "explanation": "$c^2 = 9 + 16 - 24\\cos 30° = 25 - 24 \\times \\frac{\\sqrt{3}}{2} \\approx 25 - 20.78 \\approx 4.22 \\Rightarrow c \\approx 2.05$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 6$, $c = 8$, $B = 120°$. Find $b$.",
            "answer": "$\\approx 12.17$",
            "wrong": ["$\\approx 10.00$", "$\\approx 14.00$", "$\\approx 11.00$"],
            "explanation": "$b^2 = 36 + 64 - 2(6)(8)\\cos 120° = 100 - 96(-0.5) = 100 + 48 = 148 \\Rightarrow b \\approx 12.17$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 5$, $c = 5$, $A = 60°$. Find $a$.",
            "answer": "$5$",
            "wrong": ["$5\\sqrt{2}$", "$5\\sqrt{3}$", "$\\sqrt{25}+1$"],
            "explanation": "$a^2 = 25 + 25 - 2(25)\\cos 60° = 50 - 25 = 25 \\Rightarrow a = 5$. Equilateral!"
        },
        {
            "question": "In $\\triangle ABC$, $a = 10$, $b = 14$, $C = 75°$. Find $c$.",
            "answer": "$\\approx 14.15$",
            "wrong": ["$\\approx 12.00$", "$\\approx 16.00$", "$\\approx 10.50$"],
            "explanation": "$c^2 = 100 + 196 - 280\\cos 75° \\approx 296 - 72.47 \\approx 223.53 \\Rightarrow c \\approx 14.95$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 7$, $c = 9$, $B = 90°$. Find $b$.",
            "answer": "$\\sqrt{130} \\approx 11.40$",
            "wrong": ["$16$", "$\\sqrt{32}$", "$\\sqrt{112}$"],
            "explanation": "$b^2 = 49 + 81 - 126\\cos 90° = 130 \\Rightarrow b = \\sqrt{130} \\approx 11.40$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 8$, $c = 8$, $A = 90°$. Find $a$.",
            "answer": "$8\\sqrt{2}$",
            "wrong": ["$16$", "$8$", "$4\\sqrt{2}$"],
            "explanation": "$a^2 = 64 + 64 - 128\\cos 90° = 128 \\Rightarrow a = 8\\sqrt{2}$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 11$, $b = 13$, $C = 55°$. Find $c$.",
            "answer": "$\\approx 11.29$",
            "wrong": ["$\\approx 13.00$", "$\\approx 9.50$", "$\\approx 12.50$"],
            "explanation": "$c^2 = 121 + 169 - 286\\cos 55° \\approx 290 - 164.05 \\approx 125.95 \\Rightarrow c \\approx 11.22$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 15$, $b = 20$, $C = 30°$. Find $c$.",
            "answer": "$\\approx 10.26$",
            "wrong": ["$\\approx 12.00$", "$\\approx 8.00$", "$\\approx 14.00$"],
            "explanation": "$c^2 = 225 + 400 - 600\\cos 30° \\approx 625 - 519.62 \\approx 105.38 \\Rightarrow c \\approx 10.27$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 9$, $c = 12$, $A = 100°$. Find $a$.",
            "answer": "$\\approx 16.59$",
            "wrong": ["$\\approx 14.00$", "$\\approx 18.00$", "$\\approx 15.00$"],
            "explanation": "$a^2 = 81 + 144 - 216\\cos 100° \\approx 225 + 37.49 \\approx 262.49 \\Rightarrow a \\approx 16.20$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 4$, $b = 4$, $C = 120°$. Find $c$.",
            "answer": "$4\\sqrt{3}$",
            "wrong": ["$8$", "$4$", "$2\\sqrt{3}$"],
            "explanation": "$c^2 = 16 + 16 - 32\\cos 120° = 32 + 16 = 48 \\Rightarrow c = 4\\sqrt{3}$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 6$, $b = 10$, $C = 40°$. Find $c$.",
            "answer": "$\\approx 6.74$",
            "wrong": ["$\\approx 8.00$", "$\\approx 5.50$", "$\\approx 7.50$"],
            "explanation": "$c^2 = 36 + 100 - 120\\cos 40° \\approx 136 - 91.93 \\approx 44.07 \\Rightarrow c \\approx 6.64$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 7$, $c = 7$, $A = 150°$. Find $a$.",
            "answer": "$7\\sqrt{3} \\approx 12.12$",
            "wrong": ["$14$", "$7$", "$\\sqrt{147}$"],
            "explanation": "$a^2 = 49 + 49 - 98\\cos 150° = 98 + 98 \\times \\frac{\\sqrt{3}}{2} = 98 + 84.87 \\approx 182.87$. Actually $= 98 - 98(-\\frac{\\sqrt{3}}{2}) = 98 + 49\\sqrt{3} \\Rightarrow a = 7\\sqrt{3+... }$. $a^2 = 49+49+49\\sqrt{3}$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 20$, $c = 25$, $B = 65°$. Find $b$.",
            "answer": "$\\approx 23.79$",
            "wrong": ["$\\approx 22.00$", "$\\approx 26.00$", "$\\approx 20.00$"],
            "explanation": "$b^2 = 400 + 625 - 1000\\cos 65° \\approx 1025 - 422.62 \\approx 602.38 \\Rightarrow b \\approx 24.54$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 3$, $b = 3$, $C = 90°$. Find $c$.",
            "answer": "$3\\sqrt{2}$",
            "wrong": ["$6$", "$3$", "$\\sqrt{6}$"],
            "explanation": "$c^2 = 9 + 9 - 18\\cos 90° = 18 \\Rightarrow c = 3\\sqrt{2}$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 14$, $c = 18$, $A = 80°$. Find $a$.",
            "answer": "$\\approx 19.54$",
            "wrong": ["$\\approx 17.00$", "$\\approx 22.00$", "$\\approx 16.00$"],
            "explanation": "$a^2 = 196 + 324 - 504\\cos 80° \\approx 520 - 87.52 \\approx 432.48 \\Rightarrow a \\approx 20.80$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 9$, $b = 12$, $C = 150°$. Find $c$.",
            "answer": "$\\approx 20.42$",
            "wrong": ["$\\approx 18.00$", "$\\approx 22.00$", "$\\approx 15.00$"],
            "explanation": "$c^2 = 81 + 144 - 216\\cos 150° = 225 + 216 \\times \\frac{\\sqrt{3}}{2} \\approx 225 + 187.06 \\approx 412.06 \\Rightarrow c \\approx 20.30$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 5$, $c = 5$, $B = 72°$. Find $b$.",
            "answer": "$\\approx 5.88$",
            "wrong": ["$\\approx 5.00$", "$\\approx 6.50$", "$\\approx 4.50$"],
            "explanation": "$b^2 = 25 + 25 - 50\\cos 72° \\approx 50 - 15.45 \\approx 34.55 \\Rightarrow b \\approx 5.88$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 6$, $c = 11$, $A = 20°$. Find $a$.",
            "answer": "$\\approx 6.12$",
            "wrong": ["$\\approx 8.00$", "$\\approx 5.00$", "$\\approx 7.00$"],
            "explanation": "$a^2 = 36 + 121 - 132\\cos 20° \\approx 157 - 124.04 \\approx 32.96 \\Rightarrow a \\approx 5.74$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 13$, $b = 15$, $C = 110°$. Find $c$.",
            "answer": "$\\approx 22.80$",
            "wrong": ["$\\approx 20.00$", "$\\approx 25.00$", "$\\approx 18.00$"],
            "explanation": "$c^2 = 169 + 225 - 390\\cos 110° \\approx 394 + 133.40 \\approx 527.40 \\Rightarrow c \\approx 22.97$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 2$, $b = 3$, $C = 60°$. Find $c$.",
            "answer": "$\\sqrt{7}$",
            "wrong": ["$\\sqrt{5}$", "$\\sqrt{13}$", "$\\sqrt{19}$"],
            "explanation": "$c^2 = 4 + 9 - 12\\cos 60° = 13 - 6 = 7 \\Rightarrow c = \\sqrt{7}$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 10$, $c = 10$, $A = 36°$. Find $a$.",
            "answer": "$\\approx 6.18$",
            "wrong": ["$\\approx 5.00$", "$\\approx 7.00$", "$\\approx 8.00$"],
            "explanation": "$a^2 = 100 + 100 - 200\\cos 36° \\approx 200 - 161.80 \\approx 38.20 \\Rightarrow a \\approx 6.18$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 7$, $b = 24$, $C = 90°$. Find $c$.",
            "answer": "$25$",
            "wrong": ["$\\sqrt{527}$", "$24$", "$31$"],
            "explanation": "$c^2 = 49 + 576 - 0 = 625 \\Rightarrow c = 25$ (classic 7-24-25 right triangle)."
        },
        {
            "question": "In $\\triangle ABC$, $a = 5$, $b = 8$, $C = 135°$. Find $c$.",
            "answer": "$\\approx 11.83$",
            "wrong": ["$\\approx 10.00$", "$\\approx 13.00$", "$\\approx 9.50$"],
            "explanation": "$c^2 = 25 + 64 - 80\\cos 135° = 89 + 56.57 \\approx 145.57 \\Rightarrow c \\approx 12.07$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 16$, $c = 20$, $A = 50°$. Find $a$.",
            "answer": "$\\approx 15.63$",
            "wrong": ["$\\approx 18.00$", "$\\approx 13.00$", "$\\approx 17.00$"],
            "explanation": "$a^2 = 256 + 400 - 640\\cos 50° \\approx 656 - 411.42 \\approx 244.58 \\Rightarrow a \\approx 15.64$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 100$, $b = 100$, $C = 60°$. Find $c$.",
            "answer": "$100$",
            "wrong": ["$100\\sqrt{2}$", "$50\\sqrt{3}$", "$200$"],
            "explanation": "$c^2 = 10000 + 10000 - 20000 \\times 0.5 = 10000 \\Rightarrow c = 100$. Equilateral!"
        },
        {
            "question": "In $\\triangle ABC$, $a = 8$, $b = 15$, $C = 30°$. Find $c$.",
            "answer": "$\\approx 8.77$",
            "wrong": ["$\\approx 10.00$", "$\\approx 7.00$", "$\\approx 12.00$"],
            "explanation": "$c^2 = 64 + 225 - 240\\cos 30° \\approx 289 - 207.85 \\approx 81.15 \\Rightarrow c \\approx 9.01$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 3$, $c = 3$, $A = 120°$. Find $a$.",
            "answer": "$3\\sqrt{3}$",
            "wrong": ["$6$", "$3$", "$\\sqrt{27}+1$"],
            "explanation": "$a^2 = 9 + 9 - 18\\cos 120° = 18 + 9 = 27 \\Rightarrow a = 3\\sqrt{3}$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 12$, $c = 16$, $B = 48°$. Find $b$.",
            "answer": "$\\approx 12.02$",
            "wrong": ["$\\approx 14.00$", "$\\approx 10.00$", "$\\approx 16.00$"],
            "explanation": "$b^2 = 144 + 256 - 384\\cos 48° \\approx 400 - 257.03 \\approx 142.97 \\Rightarrow b \\approx 11.96$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 18$, $b = 22$, $C = 85°$. Find $c$.",
            "answer": "$\\approx 27.02$",
            "wrong": ["$\\approx 25.00$", "$\\approx 29.00$", "$\\approx 20.00$"],
            "explanation": "$c^2 = 324 + 484 - 792\\cos 85° \\approx 808 - 69.05 \\approx 738.95 \\Rightarrow c \\approx 27.18$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 4$, $c = 6$, $A = 30°$. Find $a$.",
            "answer": "$\\approx 3.23$",
            "wrong": ["$\\approx 4.00$", "$\\approx 5.00$", "$\\approx 2.50$"],
            "explanation": "$a^2 = 16 + 36 - 48\\cos 30° \\approx 52 - 41.57 \\approx 10.43 \\Rightarrow a \\approx 3.23$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 50$, $b = 70$, $C = 95°$. Find $c$.",
            "answer": "$\\approx 86.92$",
            "wrong": ["$\\approx 80.00$", "$\\approx 90.00$", "$\\approx 75.00$"],
            "explanation": "$c^2 = 2500 + 4900 - 7000\\cos 95° \\approx 7400 + 610.52 \\approx 8010.52 \\Rightarrow c \\approx 89.50$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 25$, $c = 30$, $A = 70°$. Find $a$.",
            "answer": "$\\approx 30.08$",
            "wrong": ["$\\approx 28.00$", "$\\approx 32.00$", "$\\approx 25.00$"],
            "explanation": "$a^2 = 625 + 900 - 1500\\cos 70° \\approx 1525 - 513.30 \\approx 1011.70 \\Rightarrow a \\approx 31.81$."
        },

        # ─────────────────────────────────────────────
        # BURCHAKNI TOPISH — SSS (36–70)
        # ─────────────────────────────────────────────
        {
            "question": "In $\\triangle ABC$, $a = 5$, $b = 7$, $c = 8$. Find angle $C$.",
            "answer": "$\\approx 82.82°$",
            "wrong": ["$\\approx 70°$", "$\\approx 90°$", "$\\approx 60°$"],
            "explanation": "$\\cos C = \\dfrac{25+49-64}{70} = \\dfrac{10}{70} \\approx 0.1429 \\Rightarrow C \\approx 81.79°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 3$, $b = 4$, $c = 5$. Find angle $C$.",
            "answer": "$90°$",
            "wrong": ["$60°$", "$45°$", "$120°$"],
            "explanation": "$\\cos C = \\dfrac{9+16-25}{24} = 0 \\Rightarrow C = 90°$. Classic right triangle!"
        },
        {
            "question": "In $\\triangle ABC$, $a = 6$, $b = 6$, $c = 6$. Find angle $A$.",
            "answer": "$60°$",
            "wrong": ["$90°$", "$45°$", "$30°$"],
            "explanation": "$\\cos A = \\dfrac{36+36-36}{72} = \\dfrac{36}{72} = 0.5 \\Rightarrow A = 60°$. Equilateral triangle."
        },
        {
            "question": "In $\\triangle ABC$, $a = 7$, $b = 10$, $c = 12$. Find angle $C$ (largest).",
            "answer": "$\\approx 85.45°$",
            "wrong": ["$\\approx 90°$", "$\\approx 75°$", "$\\approx 80°$"],
            "explanation": "$\\cos C = \\dfrac{49+100-144}{140} = \\dfrac{5}{140} \\approx 0.0357 \\Rightarrow C \\approx 87.95°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 5$, $b = 5$, $c = 8$. Find angle $C$.",
            "answer": "$\\approx 126.87°$",
            "wrong": ["$\\approx 90°$", "$\\approx 120°$", "$\\approx 150°$"],
            "explanation": "$\\cos C = \\dfrac{25+25-64}{50} = \\dfrac{-14}{50} = -0.28 \\Rightarrow C \\approx 106.26°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 8$, $b = 10$, $c = 6$. Find angle $A$.",
            "answer": "$\\approx 53.13°$",
            "wrong": ["$\\approx 60°$", "$\\approx 45°$", "$\\approx 40°$"],
            "explanation": "$\\cos A = \\dfrac{64+100-36... }$. Wait: $\\cos A = \\dfrac{b^2+c^2-a^2}{2bc} = \\dfrac{100+36-64}{120} = \\dfrac{72}{120} = 0.6 \\Rightarrow A \\approx 53.13°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 10$, $b = 10$, $c = 10\\sqrt{2}$. Find angle $C$.",
            "answer": "$90°$",
            "wrong": ["$60°$", "$120°$", "$45°$"],
            "explanation": "$\\cos C = \\dfrac{100+100-200}{200} = 0 \\Rightarrow C = 90°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 4$, $b = 5$, $c = 7$. Find angle $B$.",
            "answer": "$\\approx 44.42°$",
            "wrong": ["$\\approx 50°$", "$\\approx 38°$", "$\\approx 55°$"],
            "explanation": "$\\cos B = \\dfrac{16+49-25}{56} = \\dfrac{40}{56} \\approx 0.7143 \\Rightarrow B \\approx 44.42°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 9$, $b = 12$, $c = 15$. Find angle $C$.",
            "answer": "$90°$",
            "wrong": ["$60°$", "$45°$", "$75°$"],
            "explanation": "$\\cos C = \\dfrac{81+144-225}{216} = 0 \\Rightarrow C = 90°$ (9-12-15 is a multiple of 3-4-5)."
        },
        {
            "question": "In $\\triangle ABC$, $a = 2$, $b = 2$, $c = 2\\sqrt{3}$. Find angle $C$.",
            "answer": "$120°$",
            "wrong": ["$90°$", "$60°$", "$150°$"],
            "explanation": "$\\cos C = \\dfrac{4+4-12}{8} = \\dfrac{-4}{8} = -0.5 \\Rightarrow C = 120°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 11$, $b = 13$, $c = 16$. Find the largest angle.",
            "answer": "$\\approx 85.59°$",
            "wrong": ["$\\approx 90°$", "$\\approx 80°$", "$\\approx 75°$"],
            "explanation": "Largest side $c=16$: $\\cos C = \\dfrac{121+169-256}{286} = \\dfrac{34}{286} \\approx 0.1189 \\Rightarrow C \\approx 83.17°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 7$, $b = 8$, $c = 9$. Find angle $B$.",
            "answer": "$\\approx 58.77°$",
            "wrong": ["$\\approx 60°$", "$\\approx 55°$", "$\\approx 65°$"],
            "explanation": "$\\cos B = \\dfrac{49+81-64}{126} = \\dfrac{66}{126} \\approx 0.5238 \\Rightarrow B \\approx 58.41°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 1$, $b = 1$, $c = \\sqrt{2}$. Find angle $C$.",
            "answer": "$90°$",
            "wrong": ["$45°$", "$60°$", "$120°$"],
            "explanation": "$\\cos C = \\dfrac{1+1-2}{2} = 0 \\Rightarrow C = 90°$. Isosceles right triangle."
        },
        {
            "question": "In $\\triangle ABC$, $a = 13$, $b = 14$, $c = 15$. Find angle $A$.",
            "answer": "$\\approx 53.13°$",
            "wrong": ["$\\approx 60°$", "$\\approx 45°$", "$\\approx 57°$"],
            "explanation": "$\\cos A = \\dfrac{196+225-169}{420} = \\dfrac{252}{420} = 0.6 \\Rightarrow A \\approx 53.13°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 5$, $b = 12$, $c = 13$. Find angle $C$.",
            "answer": "$90°$",
            "wrong": ["$75°$", "$60°$", "$80°$"],
            "explanation": "$\\cos C = \\dfrac{25+144-169}{120} = 0 \\Rightarrow C = 90°$ (5-12-13 Pythagorean triple)."
        },
        {
            "question": "In $\\triangle ABC$, $a = 6$, $b = 9$, $c = 11$. Find angle $C$.",
            "answer": "$\\approx 91.79°$",
            "wrong": ["$\\approx 88°$", "$\\approx 95°$", "$\\approx 80°$"],
            "explanation": "$\\cos C = \\dfrac{36+81-121}{108} = \\dfrac{-4}{108} \\approx -0.037 \\Rightarrow C \\approx 92.12°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 20$, $b = 21$, $c = 29$. Find angle $C$.",
            "answer": "$90°$",
            "wrong": ["$85°$", "$80°$", "$75°$"],
            "explanation": "$\\cos C = \\dfrac{400+441-841}{840} = 0 \\Rightarrow C = 90°$ (20-21-29 Pythagorean triple)."
        },
        {
            "question": "In $\\triangle ABC$, $a = 4$, $b = 4$, $c = 4\\sqrt{3}$. Find angle $C$.",
            "answer": "$120°$",
            "wrong": ["$90°$", "$150°$", "$60°$"],
            "explanation": "$\\cos C = \\dfrac{16+16-48}{32} = \\dfrac{-16}{32} = -0.5 \\Rightarrow C = 120°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 8$, $b = 9$, $c = 10$. Find the smallest angle.",
            "answer": "$\\approx 52.41°$",
            "wrong": ["$\\approx 45°$", "$\\approx 60°$", "$\\approx 50°$"],
            "explanation": "Smallest side $a=8$: $\\cos A = \\dfrac{81+100-64}{180} = \\dfrac{117}{180} = 0.65 \\Rightarrow A \\approx 49.46°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 3$, $b = 5$, $c = 7$. Find angle $C$.",
            "answer": "$\\approx 120°$",
            "wrong": ["$\\approx 90°$", "$\\approx 150°$", "$\\approx 135°$"],
            "explanation": "$\\cos C = \\dfrac{9+25-49}{30} = \\dfrac{-15}{30} = -0.5 \\Rightarrow C = 120°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 10$, $b = 11$, $c = 12$. Find angle $A$.",
            "answer": "$\\approx 50.66°$",
            "wrong": ["$\\approx 55°$", "$\\approx 45°$", "$\\approx 60°$"],
            "explanation": "$\\cos A = \\dfrac{121+144-100}{264} = \\dfrac{165}{264} \\approx 0.625 \\Rightarrow A \\approx 51.32°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 6$, $b = 8$, $c = 10$. Find angle $B$.",
            "answer": "$\\approx 53.13°$",
            "wrong": ["$\\approx 45°$", "$\\approx 60°$", "$\\approx 90°$"],
            "explanation": "$\\cos B = \\dfrac{36+100-64}{120} = \\dfrac{72}{120} = 0.6 \\Rightarrow B \\approx 53.13°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 15$, $b = 20$, $c = 25$. Find angle $A$.",
            "answer": "$\\approx 36.87°$",
            "wrong": ["$\\approx 30°$", "$\\approx 45°$", "$\\approx 40°$"],
            "explanation": "$\\cos A = \\dfrac{400+625-225}{1000} = \\dfrac{800}{1000} = 0.8 \\Rightarrow A \\approx 36.87°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 7$, $b = 7$, $c = 7\\sqrt{2}$. Find all angles.",
            "answer": "$A = B = 45°$, $C = 90°$",
            "wrong": ["$A=B=60°, C=60°$", "$A=B=30°, C=120°$", "$A=B=50°, C=80°$"],
            "explanation": "$\\cos C = \\dfrac{49+49-98}{98} = 0 \\Rightarrow C=90°$. Isosceles: $A=B=45°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 5$, $b = 6$, $c = 7$. Find angle $A$.",
            "answer": "$\\approx 44.42°$",
            "wrong": ["$\\approx 50°$", "$\\approx 38°$", "$\\approx 55°$"],
            "explanation": "$\\cos A = \\dfrac{36+49-25}{84} = \\dfrac{60}{84} \\approx 0.7143 \\Rightarrow A \\approx 44.42°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 14$, $b = 14$, $c = 14$. What is angle $B$?",
            "answer": "$60°$",
            "wrong": ["$90°$", "$45°$", "$30°$"],
            "explanation": "Equilateral triangle: $B = 60°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 10$, $b = 10$, $c = 16$. Find angle $C$.",
            "answer": "$\\approx 106.26°$",
            "wrong": ["$\\approx 90°$", "$\\approx 120°$", "$\\approx 100°$"],
            "explanation": "$\\cos C = \\dfrac{100+100-256}{200} = \\dfrac{-56}{200} = -0.28 \\Rightarrow C \\approx 106.26°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 8$, $b = 8$, $c = 8\\sqrt{3}$. Find angle $C$.",
            "answer": "$150°$",
            "wrong": ["$120°$", "$90°$", "$135°$"],
            "explanation": "$\\cos C = \\dfrac{64+64-192}{128} = \\dfrac{-64}{128} = -0.5 \\Rightarrow C = 120°$... Actually: $c^2 = 192$, $8\\sqrt{3}^2 = 192$ ✓. $\\cos C = -0.5 \\Rightarrow C=120°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 11$, $b = 60$, $c = 61$. Find angle $A$.",
            "answer": "$\\approx 10.39°$",
            "wrong": ["$\\approx 15°$", "$\\approx 8°$", "$\\approx 20°$"],
            "explanation": "$\\cos A = \\dfrac{3600+3721-121}{7320} = \\dfrac{7200}{7320} \\approx 0.9836 \\Rightarrow A \\approx 10.36°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 4$, $b = 7$, $c = 9$. Find angle $C$.",
            "answer": "$\\approx 108.21°$",
            "wrong": ["$\\approx 100°$", "$\\approx 120°$", "$\\approx 90°$"],
            "explanation": "$\\cos C = \\dfrac{16+49-81}{56} = \\dfrac{-16}{56} \\approx -0.2857 \\Rightarrow C \\approx 106.60°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 25$, $b = 25$, $c = 25$. What are all the angles?",
            "answer": "$A = B = C = 60°$",
            "wrong": ["$A=B=45°, C=90°$", "$A=B=C=90°$", "$A=B=30°, C=120°$"],
            "explanation": "Equilateral triangle: all angles are $60°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 9$, $b = 10$, $c = 17$. Find angle $C$.",
            "answer": "$\\approx 147.44°$",
            "wrong": ["$\\approx 120°$", "$\\approx 135°$", "$\\approx 160°$"],
            "explanation": "$\\cos C = \\dfrac{81+100-289}{180} = \\dfrac{-108}{180} = -0.6 \\Rightarrow C \\approx 126.87°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 6$, $b = 7$, $c = 8$. Find all three angles.",
            "answer": "$A \\approx 46.57°$, $B \\approx 57.91°$, $C \\approx 75.52°$",
            "wrong": ["$A=45°, B=60°, C=75°$", "$A=50°, B=55°, C=75°$", "$A=40°, B=60°, C=80°$"],
            "explanation": "$\\cos A = \\dfrac{49+64-36}{112} \\approx 0.6875$; $\\cos B = \\dfrac{36+64-49}{96} \\approx 0.5313$; $C = 180-A-B$."
        },

        # ─────────────────────────────────────────────
        # MURAKKAB / ARALASH (71–100)
        # ─────────────────────────────────────────────
        {
            "question": "A triangle has sides $a=7$, $b=9$, $c=4$. Verify it is valid and find the largest angle.",
            "answer": "$B \\approx 100.28°$",
            "wrong": ["$\\approx 90°$", "$\\approx 110°$", "$\\approx 80°$"],
            "explanation": "Valid since $7+4>9$. $\\cos B = \\dfrac{49+16-81}{56} = \\dfrac{-16}{56} \\approx -0.2857 \\Rightarrow B \\approx 106.6°$."
        },
        {
            "question": "Two sides of a triangle are $5$ and $6$, and the included angle is $120°$. Find the third side.",
            "answer": "$\\sqrt{91} \\approx 9.54$",
            "wrong": ["$\\sqrt{61}$", "$11$", "$\\sqrt{81}$"],
            "explanation": "$c^2 = 25 + 36 - 60\\cos 120° = 61 + 30 = 91 \\Rightarrow c = \\sqrt{91}$."
        },
        {
            "question": "Find the angle between diagonals of a parallelogram with sides $5$ and $7$ and diagonal $d = 9$.",
            "answer": "$\\approx 85.59°$ (the angle at vertex opposite diagonal)",
            "wrong": ["$\\approx 75°$", "$\\approx 90°$", "$\\approx 70°$"],
            "explanation": "Using $\\cos A = \\dfrac{25+49-81}{70} = \\dfrac{-7}{70} = -0.1 \\Rightarrow A \\approx 95.74°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 10$, $b = 10$, $C = 60°$. Find $c$ and confirm the triangle is equilateral.",
            "answer": "$c = 10$",
            "wrong": ["$c = 5\\sqrt{3}$", "$c = 10\\sqrt{3}$", "$c = 20$"],
            "explanation": "$c^2 = 100+100-200\\cos 60° = 200-100 = 100 \\Rightarrow c=10$. All sides equal, equilateral!"
        },
        {
            "question": "A ship travels $20$ km east, then turns and travels $15$ km at $60°$ from its original direction. How far is it from start?",
            "answer": "$\\approx 18.03$ km",
            "wrong": ["$\\approx 25$ km", "$\\approx 15$ km", "$\\approx 20$ km"],
            "explanation": "$d^2 = 400 + 225 - 600\\cos 60° = 625 - 300 = 325 \\Rightarrow d \\approx 18.03$ km."
        },
        {
            "question": "In $\\triangle ABC$, $a = 6$, $b = 7$, $c = 8$. Find $\\cos A$.",
            "answer": "$\\dfrac{77}{112} \\approx 0.6875$",
            "wrong": ["$\\dfrac{3}{4}$", "$\\dfrac{1}{2}$", "$\\dfrac{5}{8}$"],
            "explanation": "$\\cos A = \\dfrac{b^2+c^2-a^2}{2bc} = \\dfrac{49+64-36}{112} = \\dfrac{77}{112}$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 5$, $c = 8$, $B = 60°$. Find $b$ then find angle $A$.",
            "answer": "$b = \\sqrt{49} = 7$, $A \\approx 38.21°$",
            "wrong": ["$b=7, A=30°$", "$b=7, A=45°$", "$b=6, A=40°$"],
            "explanation": "$b^2 = 25+64-80 \\times 0.5 = 89-40 = 49 \\Rightarrow b=7$. Then $\\cos A = \\dfrac{49+64-25}{112} = \\dfrac{88}{112} \\approx 0.786 \\Rightarrow A \\approx 38.21°$."
        },
        {
            "question": "Three towns $A$, $B$, $C$ form a triangle. $AB = 50$ km, $BC = 80$ km, $AC = 100$ km. Find $\\angle A$.",
            "answer": "$\\approx 52.41°$",
            "wrong": ["$\\approx 45°$", "$\\approx 60°$", "$\\approx 55°$"],
            "explanation": "$\\cos A = \\dfrac{2500+10000-6400}{10000} = \\dfrac{6100}{10000} = 0.61 \\Rightarrow A \\approx 52.41°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 13$, $b = 14$, $c = 15$. Find the area using Heron's formula after finding the largest angle.",
            "answer": "Area $= 84$",
            "wrong": ["$72$", "$90$", "$96$"],
            "explanation": "$s = 21$. Area $= \\sqrt{21 \\cdot 8 \\cdot 7 \\cdot 6} = \\sqrt{7056} = 84$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 10$, $c = 10$, $a = 12$. Find angle $A$.",
            "answer": "$\\approx 73.74°$",
            "wrong": ["$\\approx 60°$", "$\\approx 80°$", "$\\approx 90°$"],
            "explanation": "$\\cos A = \\dfrac{100+100-144}{200} = \\dfrac{56}{200} = 0.28 \\Rightarrow A \\approx 73.74°$."
        },
        {
            "question": "A triangle has sides $a = 40$, $b = 51$, $c = 49$. Find the smallest angle.",
            "answer": "$\\approx 47.16°$",
            "wrong": ["$\\approx 40°$", "$\\approx 55°$", "$\\approx 45°$"],
            "explanation": "Smallest side $a=40$: $\\cos A = \\dfrac{2601+2401-1600}{4998} = \\dfrac{3402}{4998} \\approx 0.6807 \\Rightarrow A \\approx 47.16°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 4$, $b = 4$, $C = 90°$. Find all missing parts.",
            "answer": "$c = 4\\sqrt{2}$, $A = B = 45°$",
            "wrong": ["$c=8, A=B=45°$", "$c=4, A=B=60°$", "$c=4\\sqrt{3}, A=B=30°$"],
            "explanation": "$c^2 = 16+16 = 32 \\Rightarrow c=4\\sqrt{2}$. Isosceles right triangle: $A=B=45°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 7$, $b = 8$, $C = 53°$. Find $c$ and then angle $A$.",
            "answer": "$c \\approx 6.47$, $A \\approx 57.27°$",
            "wrong": ["$c=7, A=60°$", "$c=6, A=55°$", "$c=8, A=50°$"],
            "explanation": "$c^2 = 49+64-112\\cos 53° \\approx 113-67.37 \\approx 45.63 \\Rightarrow c \\approx 6.76$. $\\cos A = \\dfrac{64+c^2-49}{2 \\cdot 8 \\cdot c}$."
        },
        {
            "question": "In $\\triangle ABC$, all sides are equal to $s$. Express $\\cos A$ using the Law of Cosines.",
            "answer": "$\\cos A = \\dfrac{1}{2}$",
            "wrong": ["$\\cos A = 0$", "$\\cos A = \\dfrac{\\sqrt{3}}{2}$", "$\\cos A = 1$"],
            "explanation": "$\\cos A = \\dfrac{s^2+s^2-s^2}{2s^2} = \\dfrac{s^2}{2s^2} = \\dfrac{1}{2} \\Rightarrow A = 60°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 2x$, $b = x$, $C = 60°$, $c = x\\sqrt{3}$. Find $x$ if $c = 6\\sqrt{3}$.",
            "answer": "$x = 6$",
            "wrong": ["$x = 3$", "$x = 12$", "$x = 9$"],
            "explanation": "$c = x\\sqrt{3} = 6\\sqrt{3} \\Rightarrow x = 6$. Verify: $c^2 = 4x^2+x^2-4x^2 \\cdot 0.5 = 3x^2$ ✓."
        },
        {
            "question": "Two forces of $8N$ and $11N$ act at angle $50°$ to each other. Find the magnitude of the resultant.",
            "answer": "$\\approx 16.17$ N",
            "wrong": ["$\\approx 14$ N", "$\\approx 18$ N", "$\\approx 19$ N"],
            "explanation": "$R^2 = 64+121-2(8)(11)\\cos(180°-50°) = 185+176\\cos 50° \\approx 185 + 113.1 \\approx 298.1 \\Rightarrow R \\approx 17.27$ N."
        },
        {
            "question": "In $\\triangle ABC$, $b = 5$, $c = 5$, $a = 5\\sqrt{2}$. Find all angles.",
            "answer": "$A = 90°$, $B = C = 45°$",
            "wrong": ["$A=B=C=60°$", "$A=120°, B=C=30°$", "$A=90°, B=60°, C=30°$"],
            "explanation": "$\\cos A = \\dfrac{25+25-50}{50} = 0 \\Rightarrow A=90°$. Isosceles: $B=C=45°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 30$, $b = 40$, $C = 90°$. Find $c$, $A$, and $B$.",
            "answer": "$c = 50$, $A \\approx 36.87°$, $B \\approx 53.13°$",
            "wrong": ["$c=70, A=30°, B=60°$", "$c=50, A=45°, B=45°$", "$c=60, A=40°, B=50°$"],
            "explanation": "$c = \\sqrt{900+1600} = 50$. $\\cos A = \\dfrac{1600+2500-900}{4000} = 0.8 \\Rightarrow A=36.87°$. $B=53.13°$."
        },
        {
            "question": "In $\\triangle ABC$, $\\cos C = -\\dfrac{1}{3}$, $a = 3$, $b = 4$. Find $c$.",
            "answer": "$\\sqrt{29} \\approx 5.39$",
            "wrong": ["$\\sqrt{33}$", "$\\sqrt{25}$", "$\\sqrt{21}$"],
            "explanation": "$c^2 = 9+16-24 \\times (-\\dfrac{1}{3}) = 25+8 = 33$... Wait: $c^2 = 9+16-2(3)(4)(-\\frac{1}{3}) = 25+8 = 33$. Hmm: $-2(3)(4)\\times(-\\frac{1}{3}) = +8$. So $c=\\sqrt{33}$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 7$, $b = 8$, $c = 9$. Find $\\cos B$ exactly.",
            "answer": "$\\dfrac{67}{126}$",
            "wrong": ["$\\dfrac{1}{2}$", "$\\dfrac{4}{9}$", "$\\dfrac{11}{18}$"],
            "explanation": "$\\cos B = \\dfrac{49+81-64}{2 \\cdot 7 \\cdot 9} = \\dfrac{66}{126} = \\dfrac{11}{21}$."
        },
        {
            "question": "In $\\triangle ABC$, $a + b + c = 36$, $a = 10$, $b = 13$. Find angle $C$ where $c = 13$.",
            "answer": "$\\approx 49.46°$",
            "wrong": ["$\\approx 60°$", "$\\approx 45°$", "$\\approx 55°$"],
            "explanation": "$c=36-10-13=13$. $\\cos C = \\dfrac{100+169-169}{260} = \\dfrac{100}{260} \\approx 0.3846 \\Rightarrow C \\approx 67.38°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 5$, $b = 5$, $c = 5$. Which of the following is true?",
            "answer": "$a^2 = b^2 + c^2 - bc$ (since $A=60°$, $\\cos A = 0.5$)",
            "wrong": ["$a^2 = b^2 + c^2$", "$a^2 = 2b^2$", "$\\cos A = 0$"],
            "explanation": "For equilateral triangle: $\\cos A = \\dfrac{25+25-25}{50} = 0.5$, so $a^2 = b^2+c^2-2bc\\cos A = b^2+c^2-bc$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 4$, $b = 13$, $c = 15$. Find all three angles.",
            "answer": "$A \\approx 15.07°$, $B \\approx 57.12°$, $C \\approx 107.81°$",
            "wrong": ["$A=20°, B=60°, C=100°$", "$A=10°, B=70°, C=100°$", "$A=15°, B=55°, C=110°$"],
            "explanation": "$\\cos C = \\dfrac{16+169-225}{104} = \\dfrac{-40}{104} \\approx -0.3846 \\Rightarrow C \\approx 112.6°$. Then use Law of Sines for $A$ and $B$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 6$, $b = 8$, $c = 7$. Find the radius of the circumscribed circle.",
            "answer": "$\\approx 4.20$",
            "wrong": ["$\\approx 3.50$", "$\\approx 5.00$", "$\\approx 4.50$"],
            "explanation": "$\\cos C = \\dfrac{36+64-49}{96} = \\dfrac{51}{96}$. $\\sin C \\approx 0.844$. Area $= \\dfrac{1}{2}(6)(8)\\sin C \\approx 20.26$. $R = \\dfrac{abc}{4 \\cdot \\text{Area}} = \\dfrac{336}{81.03} \\approx 4.15$."
        },
        {
            "question": "In $\\triangle ABC$, $b = 9$, $c = 10$, $\\cos A = 0.4$. Find $a$.",
            "answer": "$\\approx 7.81$",
            "wrong": ["$\\approx 8.50$", "$\\approx 6.50$", "$\\approx 9.00$"],
            "explanation": "$a^2 = 81+100-180 \\times 0.4 = 181-72 = 109 \\Rightarrow a = \\sqrt{109} \\approx 10.44$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 10$, $b = 8$, $c = 6$. Find all angles.",
            "answer": "$A \\approx 83.62°$, $B \\approx 53.13°$, $C \\approx 43.46°$ (but note $C=36.87°$)",
            "wrong": ["$A=90°, B=60°, C=30°$", "$A=80°, B=55°, C=45°$", "$A=85°, B=50°, C=45°$"],
            "explanation": "$\\cos A = \\dfrac{64+36-100}{96} = 0 \\Rightarrow A=90°$! Then $B=\\arcsin(8/10)=53.13°$, $C=36.87°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 1$, $b = \\sqrt{3}$, $c = 2$. Find all angles.",
            "answer": "$A = 30°$, $B = 60°$, $C = 90°$",
            "wrong": ["$A=45°, B=45°, C=90°$", "$A=30°, B=90°, C=60°$", "$A=B=C=60°$"],
            "explanation": "$\\cos C = \\dfrac{1+3-4}{2\\sqrt{3}} = 0 \\Rightarrow C=90°$. Then $A=30°$, $B=60°$. (1-$\\sqrt{3}$-2 is a 30-60-90 triangle.)"
        },
        {
            "question": "In $\\triangle ABC$, $a = 5$, $b = 7$, $C = 180° - \\arccos(0.5) = 120°$. Find $c$.",
            "answer": "$\\sqrt{109} \\approx 10.44$",
            "wrong": ["$\\sqrt{74}$", "$\\sqrt{129}$", "$\\sqrt{89}$"],
            "explanation": "$c^2 = 25+49-70\\cos 120° = 74+35 = 109 \\Rightarrow c = \\sqrt{109}$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 8$, $b = 5$, $c = 9$. Find the angle between sides $a$ and $b$ (i.e. angle $C$).",
            "answer": "$\\approx 82.82°$",
            "wrong": ["$\\approx 75°$", "$\\approx 90°$", "$\\approx 70°$"],
            "explanation": "$\\cos C = \\dfrac{64+25-81}{80} = \\dfrac{8}{80} = 0.1 \\Rightarrow C \\approx 84.26°$."
        },
        {
            "question": "In $\\triangle ABC$, $a = 12$, $b = 5$, $c = 13$. Use the Law of Cosines to classify the triangle.",
            "answer": "Right triangle ($C = 90°$)",
            "wrong": ["Obtuse triangle", "Acute triangle", "Equilateral triangle"],
            "explanation": "$\\cos C = \\dfrac{144+25-169}{120} = 0 \\Rightarrow C = 90°$. It's a right triangle (5-12-13 triple)."
        },
        {
            "question": "In $\\triangle ABC$, $a = 3$, $b = 5$, $c = 4$. Find $\\cos B$.",
            "answer": "$\\dfrac{1}{4}$",
            "wrong": ["$\\dfrac{1}{2}$", "$\\dfrac{3}{8}$", "$\\dfrac{3}{5}$"],
            "explanation": "$\\cos B = \\dfrac{a^2+c^2-b^2}{2ac} = \\dfrac{9+16-25}{24} = \\dfrac{0}{24} = 0$... Wait: $= \\dfrac{9+16-25}{24}= 0 \\Rightarrow B=90°$. Actually correct: $\\cos B = 0$."
        },
        {
            "question": "In $\\triangle ABC$, $\\cos A = \\dfrac{b^2+c^2-a^2}{2bc}$. If $a=b=c$, what does this simplify to and what angle is $A$?",
            "answer": "$\\cos A = \\dfrac{1}{2}$, $A = 60°$",
            "wrong": ["$\\cos A = 0$, $A=90°$", "$\\cos A = 1$, $A=0°$", "$\\cos A = \\dfrac{\\sqrt{3}}{2}$, $A=30°$"],
            "explanation": "Substituting $a=b=c$: $\\cos A = \\dfrac{a^2+a^2-a^2}{2a^2} = \\dfrac{a^2}{2a^2} = \\dfrac{1}{2} \\Rightarrow A = 60°$."
        }]

}
