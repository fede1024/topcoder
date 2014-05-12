# Given a set of numbers and a result, find an equation that gives that number
# as result.

from __future__ import division

def get_num(n):
    if type(n) == list:
        return n[0]
    return n


def find_eq(numbers, res):
    if len(numbers) == 1:
        if get_num(numbers[0]) == res:
            return numbers[0]
        return None

    for i in xrange(len(numbers)):
        for j in xrange(i+1, len(numbers)):
            v1 = numbers[i]
            n1 = get_num(v1)
            v2 = numbers[j]
            n2 = get_num(v2)

            numbers = numbers[:i] + numbers[i+1:j] + numbers[j+1:]

            sol = find_eq(numbers + [[n1 + n2, '+', v1, v2]], res) or \
                  find_eq(numbers + [[n1 - n2, '-', v1, v2]], res) or \
                  find_eq(numbers + [[n2 - n1, '-', v2, v1]], res) or \
                  find_eq(numbers + [[n1 * n2, '*', v1, v2]], res) or \
                  (find_eq(numbers + [[n1 / n2, '/', v1, v2]], res) if n2 != 0 else None) or \
                  (find_eq(numbers + [[n2 / n1, '/', v2, v1]], res) if n1 != 0 else None)

            if sol:
                return sol

            numbers = numbers[:i] + [v1] + numbers[i:j-1] + [v2] + numbers[j-1:]

    return None

def render_formula(f, level_zero = True):
    if type(f) != list:
        return str(f)

    res = render_formula(f[2], False) + " " + f[1] + " " + render_formula(f[3], False)

    if f[1] == '+' or f[1] == '-' and not level_zero:
        return "(%s)"%(res)

    return res

def find_equation(numbers, result):
    f = find_eq(numbers, result)

    if f:
        print result, "=", render_formula(f)
    else:
        print "No solution found."

find_equation([3, 4, 2, 3, -1], 35)
# 35 = (3 + 4) * (-1 + 2 * 3)

find_equation([3, 10, 4, 2, 3, -1], 91)
# 91 = (3 + 10) * (3 * (4 - 2) - -1)

find_equation([1, 3, 4, 2, 3], -33)
# -33 = (1 - 4) * (2 + 3 * 3)

find_equation([1, 3, 4, 20, -2], 81)
# 81 = (4 * 20 + -2 / (1 - 3))

