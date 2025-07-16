import threading
def cpu_bound_task():
   count =0
   for _ in range(10**7):
      count += 1
thread1 = threading.Thread(target=cpu_bound_task)
thread2 = threading.Thread(target=cpu_bound_task)
thread1.start()
thread2.start()
thread1.join()
thread2.join()