# In section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementations,
# from page 41, was the most efficient, but we noted that it did not yield the
# factors in increasing order. Modify the generator so that it reports factors
# in increasing order, while maintaining its general performance advantages.

def factors(n):
    k = 1
    largeFactors = []
    while k * k < n:
        if n % k == 0:
            yield k
            largeFactors.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for factor in reversed(largeFactors):
        yield factor

number = 100
for factor in factors(number):
    print(factor)
