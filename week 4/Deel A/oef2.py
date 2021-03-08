import threading
import logging
from queue import Queue
from threading import Thread

import requests


def check_website(address):
    """
    check if a website is down, if so, notify the owner
    """
    try:
        print(f"Check address by {threading.current_thread()}: {address}")
        ping_website(address)
    except ValueError:
        # simulation
        logging.info(f"Notifying the owner of {address} website")
        time.sleep(0.5)


def ping_website(address, timeout=20):
    """
    Check if a website is down (the status_code >= 400 or if the timeout expires)

    Throw a Exception if any of the website down conditions are met
    """
    try:
        response = requests.head(address, timeout=timeout)
        if response.status_code >= 400:
            logging.warning(f"Website {address} returned status_code={response.status_code}")
            raise ValueError()
    except requests.exceptions.RequestException:
        logging.warning(f"Timeout expired for website {address}")
        raise ValueError()


WEBSITE_LIST = [
    'http://howest.be',
    'http://airbnb.com',
    'http://instagram.com',
    'http://snapchat.com',
    'http://youtube.com',
    'http://baidu.com',
    'http://yahoo.com',
    'http://live.com',
    'http://envato.com',
    'http://amazon.co.uk',
    'http://amazon.com',
    'http://facebook.com',
    'http://google.com',
    'http://google.fr',
    'http://google.es',
    'http://google.co.uk',
    'http://internet.org',
    'http://gmail.com',
    'http://stackoverflow.com',
    'http://github.com',
    'http://heroku.com',
    'http://really-cool-available-domain.com',
    'http://djangoproject.com',
    'http://rubyonrails.org',
    'http://basecamp.com',
    'http://trello.com',
    'http://yiiframework.com',
    'http://shopify.com',
    'http://another-really-interesting-domain.co',
    'http://linkedin.com',
    'http://yandex.ru',
    'http://netflix.com',
    'http://wordpress.com',
    'http://bing.com',
]

# Serial
import time


# logging.basicConfig(level=logging.WARNING)
# start_time = time.time()
# for address in WEBSITE_LIST:
#     check_website(address)
# end_time = time.time()
# print(f"Time for serial approach: {end_time - start_time:.2f} sec")


# Threading - Labo

class MyThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        global q
        lock.acquire()
        while not q.empty():
            site = q.get()
            lock.release()
            check_website(site)
            lock.acquire()
        lock.release()


THREAD_COUNT = 4
lock = threading.Lock()
q = Queue()
[q.put(i) for i in WEBSITE_LIST]

logging.basicConfig(level=logging.WARNING)
start_time = time.time()

# lege container voor de threads vast te houden
threads = [None for i in range(THREAD_COUNT)]
for i in range(THREAD_COUNT):
    threads[i] = MyThread(i)
    threads[i].start()

for thr in threads:
    thr.join()

end_time = time.time()
print(f"Time for Parallel approach: {end_time - start_time:.2f} sec")
