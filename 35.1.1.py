import math
import time

def calculate_sqrt_sum(x):
    summa = 0.0
    for i in range(1, x+1):
        summa += math.sqrt(i)
    return summa

def main():
    numbers = [23232, 13123, 1234, 65754, 43343]
    results = []
    start = time.time()
    for number in numbers:
        results.append(calculate_sqrt_sum(number))
    end = time.time()
    print('Последовательные результаты:', results)
    print('Время выполнения в сек:', end - start)

if __name__ == '__main__':
    main()