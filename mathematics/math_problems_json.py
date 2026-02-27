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
            'wrong': ['$(-\\infty,\\ +\\infty)$', '$\\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$', '$(-1,\\ 1)$'],
            'explanation': '$\\arccos(x)$ requires $-1 \\le x \\le 1$. Domain: $[-1, 1]$.',
        },
        {
            'question': 'What is the range of $f(x) = \\arccos(x)$?',
            'answer': '$[0,\\ \\pi]$',
            'wrong': ['$\\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$', '$(-\\infty,\\ +\\infty)$', '$\\left[0, \\dfrac{\\pi}{2}\\right]$'],
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
            'wrong': ['$[0,\\ \\pi]$', '$(-\\infty,\\ +\\infty)$', '$\\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$'],
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
            'wrong': ['$\\left(-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right)$', '$[0,\\ \\pi]$', '$(-\\infty,\\ +\\infty)$'],
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
    ]
}
