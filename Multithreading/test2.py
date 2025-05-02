import threading
import time

done = False

def worker(text):
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        print(f"{text}:{counter}")

t1 = threading.Thread(target=worker,daemon=True,args=("ACB",))
t2 = threading.Thread(target=worker,daemon=True,args=("XYZ",))

t1.start()
t2.start()

#if joint not start any execution until this 2 finishes
t1.join()
t2.join()


input('Press Enter to quit!')
done = True 
