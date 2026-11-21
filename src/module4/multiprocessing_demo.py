import multiprocessing
import time

def task1():
    for i in range(5):
        print("Task 1 - Iteration", i +1)
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2 - Iteration", i +1)
        time.sleep(1)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = task1)
    p2 = multiprocessing.Process(target = task2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Both tasks completed.")