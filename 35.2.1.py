import time
import requests

def getting_url():
    urls = ['https://www.dota2.com/home', 'https://kinogo.biz/?hash=eatvtb', 'https://t.me/telegram']
    start = time.time()
    for url in urls:
        requests.get(url)

    end = time.time()
    print(f'Выполнилось за {end - start} секунд')

getting_url()