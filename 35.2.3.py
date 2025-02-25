import requests
import time
import multiprocessing

def processes(url):
    return requests.get(url)

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        urls = ['https://av.by/profile/bookmarks/cars', 'https://www.youtube.com/', 'https://chatgptchatapp.com/']
        print('Начали выполнять..')
        start = time.time()
        results = pool.map(processes, urls)
        
    end = time.time()
    print('Последовательные результаты:', results)
    print('Время выполнения в сек:', end - start)