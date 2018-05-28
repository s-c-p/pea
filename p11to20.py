from pdb import set_trace as db

def br():
    print("-"*79)

# ----------------------------------------------------------------------------

def prod(lst):
    ans = 1
    for n in lst:
        ans *= n
    return ans

def get_surroundings(center, matrix):
    ans    = list()
    x, y = center
    x_lim, y_lim = len(matrix), len(matrix[0])
    px_feasible = x + 3 <  x_lim
    nx_feasible = x - 3 >= 0
    py_feasible = y + 3 <  y_lim
    ny_feasible = y - 3 >= 0
    if px_feasible:
        px = [matrix[x][y], matrix[x+1][y], matrix[x+2][y], matrix[x+3][y]]
        ans.append(px)
    if nx_feasible:
        nx = [matrix[x][y], matrix[x-1][y], matrix[x-2][y], matrix[x-3][y]]
        ans.append(nx)
    if py_feasible:
        py = [matrix[x][y], matrix[x][y+1], matrix[x][y+2], matrix[x][y+3]]
        ans.append(py)
    if ny_feasible:
        ny = [matrix[x][y], matrix[x][y-1], matrix[x][y-2], matrix[x][y-3]]
        ans.append(ny)
    if px_feasible and py_feasible:
        pxpy = [matrix[x][y], matrix[x+1][y+1], matrix[x+2][y+2], matrix[x+3][y+3]]
        ans.append(pxpy)
    if nx_feasible and py_feasible:
        nxpy = [matrix[x][y], matrix[x-1][y+1], matrix[x-2][y+2], matrix[x-3][y+3]]
        ans.append(nxpy)
    if nx_feasible and ny_feasible:
        nxny = [matrix[x][y], matrix[x-1][y-1], matrix[x-2][y-2], matrix[x-3][y-3]]
        ans.append(nxny)
    if px_feasible and ny_feasible:
        pxny = [matrix[x][y], matrix[x+1][y-1], matrix[x+2][y-2], matrix[x+3][y-3]]
        ans.append(pxny)
    return ans


def prob11():
    given = [
        [ 8,  2, 22, 97, 38, 15,  0, 40,  0, 75,  4,  5,  7, 78, 52, 12, 50, 77, 91,  8],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48,  4, 56, 62,  0],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30,  3, 49, 13, 36, 65],
        [52, 70, 95, 23,  4, 60, 11, 42, 69, 24, 68, 56,  1, 32, 56, 71, 37,  2, 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99,  3, 45,  2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68,  2, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21],
        [24, 55, 58,  5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23,  9, 75,  0, 76, 44, 20, 45, 35, 14,  0, 61, 33, 97, 34, 31, 33, 95],
        [78, 17, 53, 28, 22, 75, 31, 67, 15, 94,  3, 80,  4, 62, 16, 14,  9, 53, 56, 92],
        [16, 39,  5, 42, 96, 35, 31, 47, 55, 58, 88, 24,  0, 17, 54, 24, 36, 29, 85, 57],
        [86, 56,  0, 48, 35, 71, 89,  7,  5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68,  5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,  4, 89, 55, 40],
        [ 4, 52,  8, 83, 97, 35, 99, 16,  7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72,  3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
        [ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74,  4, 36, 16],
        [20, 73, 35, 29, 78, 31, 90,  1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,  5, 54],
        [ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52,  1, 89, 19, 67, 48]
    ]
    known_max = 0
    for i in range(len(given)):
        for j in range(len(given[i])):
            pos = (i, j)
            nbrs = get_surroundings(pos, given)
            this_max = max(map(prod, nbrs))
            known_max = max(known_max, this_max)
    return known_max

# print(prob11())
br()

# ----------------------------------------------------------------------------

def dirty_fast_prime_gen(seed=None):
    if seed:
        k = 1
        while True:
            
    yield 2
    yield 3
    k = 1
    while True:
        yield 6*k - 1
        yield 6*k + 1
        k += 1
    return

def is_prime(num_to_check, known_primes):
    # thanks to Py's call-by-*; the list known_primes is passed by reference
    # assumes known_primes is sorted
    for x in known_primes:
        if num_to_check % x == 0:
            return False
    return True

def prime_gen(l):
    p_gen = dirty_fast_prime_gen()
    known_primes = list()
    known_primes.append(next(p_gen))
    known_primes.append(next(p_gen))
    while len(known_primes) < l:
        np = next(p_gen)
        if is_prime(np, known_primes):
            known_primes.append(np)
    return known_primes

def num_is_triangle(num):
    # k = num
    # k = n*(n+1) // 2
    # 0 = n^2 + n -2k
    # n = (-1 +- (1 + 8k)**0.5)/2
    k = num
    n1 = (-1 + (1 + 8*k)**0.5)/2
    # n2 = (-1 - (1 + 8*k)**0.5)/2 this will always be negative as k is always positive
    if int(n1) == n1:
        return int(n1)
    return False

# def prob12():
#     return 762409999177
#     import itertools
#     # 500 = 2*2 * 5*5*5
#     # 500 = product of 5 distinct prime numbers - a, b, c, d, e
#     # ans = a * b * c**4 * d**4 * e**4
#     #         && ans is a triangle number
#     lim = 10
#     while True:
#         known_primes = prime_gen(lim)
#         for g in itertools.permutations(known_primes, 5):
#             a, b, c, d, e = g
#             the_num = a * b * c**4 * d**4 * e**4
#             check = num_is_triangle(the_num)
#             if check:
#                 print(g)
#                 return check
#         lim += 5
#     return

# # print(prob12())

def prime_factorize(num, known_primes):
    if num in [0, 1]:
        return num
    if known_primes[-1] < num:
    ans = dict()
    num_backup = num
    for prime in known_primes:
        num = num_backup
        if prime > num:    # don't scan known primes greater than num itself
            break
        ans[prime] = 0    # init ans dict with prime as key holding 0 as value
        while True:
            quot = num / prime
            if int(quot) == quot:
                ans[prime] += 1
                num = int(quot)
            else:
                break
    return ans

import pprint
ans = prime_factorize(76576500, prime_gen(100))
pprint.pprint({k:v for k, v in ans.items() if v != 0})
print(f"number of factors -- {prod([f+1 for f in ans.values()])}")
print(sum(ans.values()))

def prob12():
    # return 762409999177
    import itertools
    # 504 = 2*2*2 * 3*3 * 7
    # 504 = product of 6 distinct prime numbers - a, b, c, d, e, f
    # ans = a * b * c * d**2 * e**2 * f**6
    #         && ans is a triangle number
    lim = 10
    while True:
        known_primes = prime_gen(lim)
        for g in itertools.permutations(known_primes, 6):
            a, b, c, d, e, f = g
            the_num = a * b * c * d**2 * e**2 * f**6
            check = num_is_triangle(the_num)
            if check:
                print(g)
                return check
        lim += 5
    return

# print(prob12())
http://code.jasonbhill.com/sage/project-euler-problem-12/
https://projecteuler.net/problem=12
https://github.com/nayuki/Project-Euler-solutions/blob/master/Answers.txt

# def prob12(lim):
#     p_gen = dirty_fast_prime_gen()
#     triangle_num = triangle_num_gen()
#     known_primes = list()
#     known_primes.append(next(p_gen))
#     known_primes.append(next(p_gen))
#     while True:
#         __ol = len(known_primes)
#         i = next(triangle_num)
#         while known_primes[-1] < i:    # before doing anything, make sure we know sufficient prime numbers
#             np = next(p_gen)
#             if is_prime(np, known_primes):
#                 known_primes.append(np)
#         if __ol != len(known_primes):
#             print(f"{len(known_primes)-__ol} primes found and added for i={i}")
#         __factors_of_i = prime_factorize(i, known_primes)
#         num_of_factors = prod([c+1 for c in __factors_of_i.values()])
#         if num_of_factors >= lim:
#             return i
#     return

# print(prob12(500))
