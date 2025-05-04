from collections import Counter
from math import factorial

def decomp(n):
    def prime_factors(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                yield i
        if n > 1:
            yield n

    total = Counter()
    for i in range(2, n+1):
        total += Counter(prime_factors(i))

    return ' * '.join(f'{k}^{v}' if v > 1 else str(k) for k, v in sorted(total.items()))
