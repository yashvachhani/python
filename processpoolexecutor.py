import time
import concurrent.futures
start  = time.perf_counter()

def do_something(second):
    print(f'sleeping {second} sec')
    time.sleep(second)
    return f'done slepping....{second}'
'''
# for one and manule
with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(do_something,1)
    f2 = executor.submit(do_something,1)
    print(f1.result())
    print(f2.result())

# in loop
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5 ,4, 3, 2, 1]
    result = [executor.submit(do_something,sec) for sec in secs]

    for f in concurrent.futures.as_completed(result):
        print(f.result())
'''
# in map
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5 ,4, 3, 2, 1]
    results = executor.map(do_something,secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {finish-start} secondss')