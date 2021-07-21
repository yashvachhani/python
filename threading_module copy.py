import time
import multiprocessing
start  = time.perf_counter()

def do_something(second):
    print(f'sleeping {second} sec')
    time.sleep(second)
    print('done slepping....')

'''
# for manual
p1 = multiprocessing.Process(target=do_something,args=[2])
p2 = multiprocessing.Process(target=do_something,args=[2])

p1.start()
p2.start()

p1.join()
p2.join()
'''


# in loop
processes=[]
for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1.3])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finished in {finish-start} secondss')