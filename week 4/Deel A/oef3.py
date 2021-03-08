import os

import multiprocessing
import threading

import time

from multiprocessing import Process

NUM_WORKERS = 4


# versie 1
def worker():
    """ Do nothing, wait for a timer to expire """
    print(f"PID: {os.getpid()}, Process Name: {multiprocessing.current_process().name}, Thread Name: {threading.current_thread().name}")
    time.sleep(1)

# versie 2
# def worker():
#     """ Do some computations """
#     print(f"PID: {os.getpid()}, Process Name: {multiprocessing.current_process().name}, Thread Name: {threading.current_thread().name}")
#     x = 0
#     while x < 10000000:
#         x += 1

if (__name__ == '__main__'):
    # ## Run tasks serially
    start_time = time.time()
    for x in range(NUM_WORKERS):
        worker()
    end_time = time.time()
    print(f"Serial time={end_time - start_time:.2f} sec\n")

    # Run tasks using threads
    start_time = time.time()
    threads = []
    # create all threads
    for i in range(NUM_WORKERS):
        thread = threading.Thread(target=worker)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Threads time={end_time - start_time:.2f} sec\n")

    # # Run tasks using processes
    start_time = time.time()
    processes = []
    # create all processes
    for i in range(NUM_WORKERS):
        process = Process(target=worker)
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes
    for process in processes:
        process.join()

    end_time = time.time()
    print(f"Parallel time={end_time - start_time:.2f} sec\n")
