from datetime import datetime
import math
import sys

start_time = datetime.now()

DIRECTORY_PATH_POWER = "/Users/kolesnikova/Documents/otus/3.Power/test."
DIRECTORY_PATH_FIBO = "/Users/kolesnikova/Documents/otus/4.Fibo/test."
DIRECTORY_PATH_PRIMES = "/Users/kolesnikova/Documents/otus/5.Primes/test."

# 01. +1 байт. Реализовать итеративный O(N) алгоритм возведения числа в степень.
def iterrative_method(N, power):
    res = 1
    for i in range(0, power):
        res *= N
    return res


# 11. +1 байт. Реализовать алгоритм возведения в степень через домножение O(N/2+LogN) = O(N).
def multiplication_method(N, power):
    res = 1
    res_prom = N
    res_prom2 = 1
    d = 2
    while d < power:
        res_prom *= res_prom
        d *= 2
    if d == power:
        return res_prom * res_prom
    if power - int(d / 2) >= 0:
        for k in range(0, power - int(d / 2)):
            res_prom2 *= N
        res = res_prom * res_prom2
    return res


# 12. +1 байт. Реализовать алгоритм возведения в степень через двоичное разложение показателя степени O(2LogN) = O(LogN).
def logN_method(N, power):
    res = 1
    d = N
    while (power > 1):
        if (power % 2 == 1):
            res *= d
        d *= d
        power = int(power / 2)
    if (power > 0):
        res *= d
    return (res)


# 02. +1 байт. Реализовать рекурсивный O(2^N) и итеративный O(N) алгоритмы поиска чисел Фибоначчи.
def fibo1(N: int):
    if N <= 1:
        return N
    else:
        return (fibo1(N - 1) + fibo1(N - 2))


# итеративный O(N) алгоритмы поиска чисел Фибоначчи.
def fibo2(N: int):
    f1 = 1
    f2 = 2
    for i in range(3, N):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f2


# 13. +1 байт. Реализовать алгоритм поиска чисел Фибоначчи по формуле золотого сечения

def fibo3(N: int):
    psi = (1 + math.sqrt(5)) / 2
    f = int(logN_method(psi, N) / math.sqrt(5) + 0.5)
    return f


# 14. +1 байт. Написать класс умножения матриц, реализовать алгоритм возведения матрицы в степень через двоичное разложение показателя степени,
# реализовать алгоритм поиска чисел Фибоначчи O(LogN) через умножение матриц, используя созданный класс.
class matrix(object):
    """операции с матрицами"""

    def multiply(m1, m2):
        m = [[0, 0], [0, 0]]
        m[0][0] = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
        m[0][1] = m1[0][0] * m2[1][0] + m1[0][1] * m2[1][1]
        m[1][0] = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
        m[1][1] = m1[1][0] * m2[1][0] + m1[1][1] * m2[1][1]
        return m

    def logN_method(m, power):
        res = [[1, 0], [0, 1]]
        d = m
        while (power > 1):
            if (power % 2 == 1):
                res = matrix.multiply(res, d)
            d = matrix.multiply(d, d)
            power = int(power / 2)
        if (power > 0):
            res = matrix.multiply(res, d)
        return (res)


def matrix_fib(N: int):
    base = [[1, 1], [1, 0]]  # 1-1-1-0
    res = matrix.logN_method(base, N)
    return res[0][1]


# 03. +1 байт. Реализовать алгоритм поиска количества простых чисел через перебор делителей, O(N^2).
def cntPrime(N):
    cnt = 0
    for i in range(2, N + 1):
        if (isPrime(i)):
            cnt += 1
    return cnt


def isPrime(N):
    if (N == 2): return True
    if (N % 2 == 0): return False
    s = int(math.sqrt(N))
    for i in range(3, s + 1, 2):
        if (N % i == 0):
            return False
    return True


# 15. +1 байт. Реализовать алгоритм поиска простых чисел с оптимизациями поиска и делением только на простые числа, O(N * Sqrt(N) / Ln (N)).

def cntPrime2(N):
    cnt = 0
    primes = [2]
    cnt += 1
    if N > 2:
        for i in range(3, N + 1):
            if (isPrime2(i, primes)):
                # print(primes)
                cnt += 1
                primes.append(i)
    else:
        cnt = int(N/2)
    return cnt


def isPrime2(N, primes):
    s = int(math.sqrt(N))
    i = 0
    while primes[i] <= s:
        if (N % primes[i] == 0):
            return False
        i += 1
    return True


# 16. +1 байт. Реализовать алгоритм "Решето Эратосфена" для быстрого поиска простых чисел O(N Log Log N).
def eratosthen(N):
    primes = []
    for i in range(N + 1):
        primes.append(i)
    primes[1] = 0
    i = 2
    while i <= N:
        if primes[i] != 0:
            j = i + i
            while j <= N:
                # это число составное, поэтому заменяем его нулем
                primes[j] = 0
                # переходим к следующему числу, которое кратно i (оно на i больше)
                j = j + i
        i += 1
    primes2 = set(primes)
    return len(primes2) - 1


# 17. +1 байт. Решето Эратосфена с оптимизацией памяти, используя битовую матрицу, сохраняя по 32 значения в одном int, хранить биты только для нечётных чисел.
# не реализовано

# 18. +1 байт. Решето Эратосфена со сложностью O(n), см. дополнительный материал.

def eratosthen2(N):
    if N > 2:
        lp = [0] * (N+1)
        pr = []
        for i in range(2, N+1):
            if lp[i] == 0:
                lp[i] = i
                pr.append(i)
            for j in pr:
                if (j > lp[i]) | (j * i > N):
                    break
                else:
                    lp[j * i] = j
        cnt = len(set(pr))
    else:
        cnt = int(N / 2)
    return cnt


# ТЕСТИРОВАНИЕ
def test_power(i):
    with open(DIRECTORY_PATH_POWER + str(i) + '.in') as f:
        d = f.readlines()
        power = int(d[1])
        N = float(d[0])
    with open(DIRECTORY_PATH_POWER + str(i) + '.out') as f:
        out = f.readline()

    print("метод 01")
    start_time = datetime.now()
    res = iterrative_method(N, power)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)
    if abs(float(res) - float(out)) < 0.0000000001:
        print("test ok")
    else:
        print("test not ok")

    print("метод 11")
    start_time = datetime.now()
    res2 = multiplication_method(N, power)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)

    if abs(float(res2) - float(out)) < 0.0000000001:
        print("test ok")
    else:
        print("test not ok")

    print("метод 12")
    start_time = datetime.now()
    res3 = logN_method(N, power)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)

    if abs(float(res3) - float(out)) < 0.0000000001:
        print("test ok")
    else:
        print("test not ok")

def test_fibo(i):
    with open(DIRECTORY_PATH_FIBO + str(i) + '.in') as f:
        N = int(f.readline())

    with open(DIRECTORY_PATH_FIBO + str(i) + '.out') as f:
        out = f.readline()

    print("метод 02-1")
    start_time = datetime.now()
    res = fibo1(N)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)
    if int(res) == int(out):
        print("test ok")
    else:
        print("test not ok")

    print("метод 02-2")
    start_time = datetime.now()
    res2 = fibo2(N)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)

    if int(res2) == int(out):
        print("test ok")
    else:
        print("test not ok")

    print("метод 13")
    start_time = datetime.now()
    res3 = fibo3(N)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)

    if int(res3) == int(out):
        print("test ok")
    else:
        print("test not ok")

    print("метод 14")
    start_time = datetime.now()
    res4 = matrix_fib(N)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)

    if int(res4) == int(out):
        print("test ok")
    else:
        print("test not ok")



def test_primes(i):
    with open(DIRECTORY_PATH_PRIMES + str(i) + '.in') as f:
        N = int(f.readline())

    with open(DIRECTORY_PATH_PRIMES + str(i) + '.out') as f:
        out = f.readline()

    print("метод 03")
    start_time = datetime.now()
    res = cntPrime(N)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)
    if int(res) == int(out):
        print("test ok")
    else:
        print("test not ok")

    print("метод 15")
    start_time = datetime.now()
    res2 = cntPrime2(N)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)

    if int(res2) == int(out):
        print("test ok")
    else:
        print("test not ok")

    print("метод 16")
    start_time = datetime.now()
    res3 = eratosthen(N)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)

    if int(res3) == int(out):
        print("test ok")
    else:
        print("test not ok")

    print("метод 18")
    start_time = datetime.now()
    res4 = eratosthen2(N)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)

    if int(res4) == int(out):
        print("test ok")
    else:
        print("test not ok")



# проверяем  возведение числа в степень
for i in range(0, 10):
    test_power(i)

# проверяем поиск чисел Фибоначчи
for i in range(0, 10):
    test_fibo(i)

# проверяем поиск простых чисел
for i in range(0, 10):
    print(i)
    test_primes(i)
