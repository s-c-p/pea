from pdb import set_trace as st

def dirty_prime_gen(seed1, seed2):
    x = (seed1 + seed2) // 6
    if x % 2 == 0:
        k = x // 2
    else:
        k = x // 2 + 1
        yield 6*k + 1
    k += 1
    while True:
        yield 6*k - 1
        yield 6*k + 1
        k += 1

def trngl_num_gen():
    n = 1
    while True:
        yield (n*(n+1))//2
        n += 1

def num_is_trngl(num):
    d = (8*num + 1)**0.5
    if int(d) == d:
        return (d - 1)//2
    return False

def is_prime(test, known):
    for x in known:
        if x > test:
            return False
        if test % x == 0:
            return False
    return True

def prime_list(lim, known=None):
    if known == None:
        known = [2, 3, 5, 7]
    dp = dirty_prime_gen(known[-2], known[-1])
    while len(known) < lim:
        sp = next(dp)
        if is_prime(sp, known):
            known.append(sp)
    return known

def prime_factorize(num, known_primes):
    pf = dict()
    for p in known_primes:
        if p > num:
            break
        n = num
        times = int()
        while n % p == 0:
            n /= p
            times += 1
        pf[p] = times
    return {k:v for k, v in pf.items() if v != 0}

def the_func(dct):
    # (12, 504, {2: 3, 3: 2, 7: 1}),
    # 504 = 2*2*2 * 3*3 * 7
    # 504 = product of 6 distinct prime numbers - a, b, c, d, e, f
    # ans = a * b * c * d**2 * e**2 * f**6
    chars = "abcdefghijklmnopqrstuvwxyz"
    grp_size = sum(dct.values())
    pph = list(chars[:grp_size]) # primeNum place holder
    i = int()
    raw_eqn = list()
    for pwr, reps in dct.items():
        for _ in range(reps):
            cpph = pph[i]
            frag = "%s**%d" % (cpph, pwr-1)
            raw_eqn.append(frag)
            i += 1
    code = "def x(%s): return %s" % (", ".join(pph), "*".join(raw_eqn))
    st()
    return grp_size, eval(code)

def find_least_f_num(min, max):
    ans = list()
    knp = prime_list(max) # misuse but okay
    for num in range(min, max+1):
        fzn = prime_factorize(num, knp)
        nf = sum(fzn.values())
        ans.append((nf, num, fzn))
    return sorted(ans, key=lambda x: x[0])
    return ans

from pprint import pprint as pp
research = find_least_f_num(501, 600)
pp(research)
exit()
# (512, 576, 540, 567, 600)


from itertools import product

def get_trngl_num_with_n_factors(n):
    knp = prime_list(n) # misuse but ok
    pf = prime_factorize(n, knp)
    grp_size, functor = the_func(pf)
    knp = knp[:grp_size*2]
    for group in product(knp, grp_size):
        x = functor(group)
        if num_is_trngl(x):
            print(x)
            break
    return

#get_trngl_num_with_n_factors(504)



