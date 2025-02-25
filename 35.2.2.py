import time
import requests
import threading

def getting_url_1_thread():
    print('Выполняется 1 поток..')
    urls = ['https://www.dota2.com/home', 'https://kinogo.biz/?hash=eatvtb', 'https://t.me/telegram']
    start = time.time()
    for url in urls:
        requests.get(url)


def getting_url_2_thread():
    print('Выполняется 2 поток..')
    urls = ['https://av.by/profile/bookmarks/cars', 'https://www.youtube.com/', 'https://chatgptchatapp.com/']
    start = time.time()
    for url in urls:
        requests.get(url)

start = time.time()

thread_1 = threading.Thread(target=getting_url_1_thread)
thread_2 = threading.Thread(target=getting_url_2_thread)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

end = time.time()

print(f'Выполнилось за {end - start} секунд')