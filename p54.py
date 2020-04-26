from numpy.random import uniform


def binomial_rv(n, p):
    count = 0
    for i in range(n):
        u = uniform()
    if u < p:
        count = count + 1  # Or count += 1
    return count


mmm = binomial_rv(10, 0.5)
print(mmm)
