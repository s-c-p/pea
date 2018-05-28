import pdb

def br():
    print("-"*79)

def _prime_filter(num_list):
    working_list = num_list[:]
    # assumes num_list is sorted 0 -> largest
    #             first element is non zero
    for a_suspect in working_list:
        if a_suspect == 0:
            continue
            # skip num's which have already been determined to be composite
        for i, a_number in enumerate(working_list):
            if a_number == a_suspect:
                continue
                # don't scan primes themselves
            if a_number < a_suspect:
                continue
                # no sense in finding 5 (smaller) % 10 (larger)
            if a_number % a_suspect == 0:
                working_list[i] = 0
                # now we know this number is composite
    return list(filter(None, working_list))

# ----------------------------------------------------------------------------

def ero_sieve(till):
    numbers = list(range(2, till+1))
    return _prime_filter(numbers)

# ans = ero_sieve(200)
# print(len(ans))
# print(ans)
br()

# ----------------------------------------------------------------------------

def table_gen(x, lim):
    i = int()
    while True:
        i += x
        if i >= lim:
            break
        yield i

def prob1(till):
    gen3 = table_gen(3, till)
    gen5 = table_gen(5, till)
    gen15= table_gen(15, till)
    ans = sum(gen3) + sum(gen5) - sum(gen15)
    return ans

# print(prob1(1000))
br()

# ----------------------------------------------------------------------------

def fib_gen(till):
    a = 0
    b = 1
    while True:
        ans = a + b
        if ans >= till:
            break
        yield ans
        a = b
        b = ans

def prob2(till):
    nums = filter(lambda x: x % 2 == 0, fib_gen(till))
    return sum(nums)

# print(prob2(4*10**6))
br()

# ----------------------------------------------------------------------------

def lower_prime_factors(of):
    till = int(of**0.5)
    factors = list()
    for i in range(2, till):
        if of % i == 0:
            factors.append(i)
    # for x in factors:
    #     factors.append(of//x)
    return _prime_filter(factors)

prob3 = lambda x: max(lower_prime_factors(x))

# print(prob3(600851475143))
br()

# ----------------------------------------------------------------------------

def is_palin(num):
    x = str(num)
    if x == x[::-1]:
        return True
    return False

def find_factors(num):
    center = int(num**0.5)
    good_factors = list()
    # focus on finding biggest ones greater than 99
    for sus in range(center, 99, -1):
        if num % sus == 0:
            good_factors.append(sus)
    for x in good_factors:
        if num / x < 100:
            good_factors.remove(x)
            # cuz both factors should be three digit
    return good_factors

def prob4():
    ans = 0
    for num in range(999*999, 99, -1):
        if not is_palin(num):
            continue
        if len(find_factors(num)) >= 1:
            ans = num
            break
    return ans

# print(prob4())
br()

# ----------------------------------------------------------------------------

def prime_factors(of):
    number = of
    factors = list()
    # number = root(10) == 3.something; then we'd miss 5. So scan till `of`
    for i in range(2, number):
        if number % i == 0:
            factors.append(i)
    return _prime_filter(factors)

def prime_factorize(num):
    p_factors = prime_factors(num)
    if len(p_factors) == 0:        return { num : 1 }
    test_factor = p_factors.pop()
    ans = { test_factor : 0 }
    while True:
        quot, rem = divmod(num, test_factor)
        if rem == 0:
            num = num / test_factor
            ans[test_factor] += 1
        else:
            test_factor = p_factors.pop()
            ans[test_factor] = 0
        if num == 1:
            break
    return ans

def prob5(lim):
    def _digest(lod):
        ans = 1
        for k, v in lod.items():
            for _ in range(v):
                ans *= k
        return ans
    # ans = prod_of_all primes^greatest_power
    ans = dict()
    temp = list()
    for a_num in range(2, lim):
        p_i = prime_factorize(a_num)
        temp.append(p_i)
    for pfd in temp:
        for k, v in pfd.items():
            try:
                ans[k]
            except KeyError:
                ans[k] = v
            else:
                ans[k] = max(ans[k], v)
    return _digest(ans)

# print(prob5(20))
br()

# ----------------------------------------------------------------------------

def prob6(till):
    num_squares = (x**2 for x in range(till))
    return sum(range(till))**2 - sum(num_squares)

# print(prob6(20))
br()

# ----------------------------------------------------------------------------

def dirty_fast_prime_gen():
    yield 2
    yield 3
    k = 1
    while True:
        yield 6*k - 1
        yield 6*k + 1
        k += 1

def prob7(n_th):
    known = list()
    gutter = dirty_fast_prime_gen()
    known.append(next(gutter))
    known.append(next(gutter))
    while True:
        if len(known) >= n_th:
            break
        possible = next(gutter)
        is_prime = True
        for p in known:
            if possible % p == 0:
                is_prime = False
                break
        if is_prime:
            known.append(possible)
    return known[-1]

# print(prob7(10001))
br()

# ----------------------------------------------------------------------------

def prod(x):
    ans = 1
    digits = map(int, list(x))
    for d in digits:
        ans *= d
    return ans

def readN(src, n):
    for i, char in enumerate(src):
        # assert char == src[i]
        selection = src[i:i+n]
        if len(selection) < n:
            break
        yield selection

def prob8(g_size):
    NUMBER = "\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450\
    "
    curr_max = int()
    for num_str in readN(NUMBER, g_size):
        if '0' in num_str:
            continue
        curr_max = max(curr_max, prod(num_str))
    return curr_max

# print(prob8(13))
br()

# ----------------------------------------------------------------------------

def prob9():
    # for i in range(1, 998+1):
    #     for j in range(1, 998+1):
    #         a = i
    #         b = j
    #         c = 1000 - a - b
    #         if a**2 + b**2 == c**2:
    #             return (a, b, c)
    # a = m^2 - n^2
    # b = 2 * m * n
    # c = m^2 + n^2
    for m in range(1, 998+1):
        m_squared = m**2
        for n in range(1, 998+1):
            n_squared = n**2
            
            if m_squared <= n_squared:
                continue # cuz a can't be 0 or negative
            a = m_squared - n_squared
            b = 2*m*n
            c = m_squared + n_squared
            if a + b + c == 1000:
                print(a, b, c)
                return a*b*c

    return 31875000

# print(prob9())
br()

# ----------------------------------------------------------------------------

def prob10(lim):
    known = list()
    gutter = dirty_fast_prime_gen()
    known.append(next(gutter))
    known.append(next(gutter))
    l = int()
    while True:
        if known[-1] >= lim:
            if known[-1] > lim:
                known.pop()
            break

        possible = next(gutter)
        is_prime = True
        for p in known:
            if possible % p == 0:
                is_prime = False
                break
        if is_prime:
            known.append(possible)

        l += 1
        if l % 1000 == 0:
            print(l//1000, len(known))
    return sum(known)

# TODO: print(prob10(2*10**6))

