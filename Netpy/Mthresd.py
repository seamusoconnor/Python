import time
import threading

def calc_square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print ('Square ' + str(n*n))

def calc_cube(numbers):
    for n in numbers:
        print ('cube ' + str(n*n*n))

if __name__ == "__main__":
    arr = [2,3,8,9]
    start_time = time.time()
    time.sleep(0.2)

    t1 = threading.Thread(target=calc_square, args=(arr,))
    t2 = threading.Thread(target=calc_cube, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    elapsed_time = time.time() - start_time
    print (elapsed_time)