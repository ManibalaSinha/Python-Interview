#parse and evaluate a mathematical expression string in python
import operator
import re

def evaluate_expression(expr):
    tokens = re.findall(r'\d+\.?\d*|[()+\-*/]', expr) #\d+ match digit, \.? match decimal, \d* more digit, \- minus
    
    def parse(tokens):
        def get_number_or_expr():
            token = tokens.pop(0)
            if token == '(': #If token is (: it's a sub-expression, recursively evaluate it.
                val = parse(tokens)
                tokens.pop(0)  # remove ')'
                return val
            return float(token)

        def get_term():
            val = get_number_or_expr()
            while tokens and tokens[0] in ('*', '/'):
                op = tokens.pop(0)
                next_val = get_number_or_expr()
                val = ops[op](val, next_val)
            return val

        val = get_term()
        while tokens and tokens[0] in ('+', '-'):
            op = tokens.pop(0)
            next_val = get_term()
            val = ops[op](val, next_val)
        return val

    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    return parse(tokens)
print(evaluate_expression("3 + 5 * 2"))  
