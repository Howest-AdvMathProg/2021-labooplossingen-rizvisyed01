import threading
import time
import logging
from random import randrange
from threading import Thread

THREAD_AMOUNT = 2
RANDOM_AMOUNT = 20
dict = {}
lock = threading.Lock()

logging.basicConfig(level=logging.INFO)


def generateRandom(num):
    name = "Thread-" + str(num)
    lock.acquire()
    dict[name] = []
    lock.release()
    for rndIndex in range(RANDOM_AMOUNT):
        rnd = randrange(0, 1000, 1)
        while rnd in dict[name]:
            rnd = randrange(0, 1000, 1)
        logging.info("I am %s Adding %s", name, rnd)
        lock.acquire()
        dict[name].append(rnd)
        lock.release()
        time.sleep(randrange(0, 2, 1))


if __name__ == "__main__":
    threads = [None] * THREAD_AMOUNT
    for i in range(THREAD_AMOUNT):
        threads[i] = Thread(target=generateRandom, args=(i,))
        threads[i].start()

    for thr in threads:
        thr.join()

    logging.info("All threads done!")
    for key in dict:
        print("Values: " + key)
        print(dict[key])
