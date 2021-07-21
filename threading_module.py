import time
import threading

start  = time.perf_counter()

def do_something(second):
    print(f'sleeping {second} sec')
    time.sleep(second)
    print('done slepping....')

# create thread and assiend task and pass argumant as args
t1 = threading.Thread(target = do_something,args=[5])
t2 = threading.Thread(target = do_something,args=[2])

# start the threads
t1.start()
t2.start()

# this is optional 
# join the flow of program ( this is make sure thread is exicuted before exicuting further program)
t1.join()
t2.join()

# use loop and handel multipal threads
threads = []

for _ in range(10):
    t = threading.Thread(target=do_something,args=[4])
    t.start()
    threads.append(t)

for i in threads:
    i.join()

finish = time.perf_counter()

print(f'Finished in {finish-start} secondss')