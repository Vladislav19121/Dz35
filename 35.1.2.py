import math
import time
import threading
def calculate_sqrt_sum(x, results, index):
    summa = 0.0
    for i in range(1, x+1):
        summa += math.sqrt(i)
    results[index] = summa

def main():
    numbers = [2323, 13123, 1234, 6575, 433434]
    results = [None]*len(numbers)
    threads = []
    start = time.time()
    for i,n in enumerate(numbers):
        thread = threading.Thread(target = calculate_sqrt_sum, args=(n, results, i))
        threads.append(thread)
        thread.start()
        for thread in threads:
            thread.join()

    end = time.time()
    print('Последовательные результаты:', results)
    print('Время выполнения в сек:', end - start)
    print(f'{threads}')

if __name__ == '__main__':
    main()


