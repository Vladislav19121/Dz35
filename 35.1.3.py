import math
import time
import multiprocessing


def calculate_sqrt_sum(number):
    summa = 0.0
    for i in range(1, number+1):
        summa += math.sqrt(i)
    return summa 

def main():
    numbers = [23232, 1312, 12345, 6575, 4334]
    results = [None]*len(numbers)
    threads = []
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_sqrt_sum, numbers)
    end = time.time()
    print('Последовательные результаты:', results)
    print('Время выполнения в сек:', end - start)

if __name__ == '__main__':
    main()