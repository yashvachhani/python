import time
import concurrent.futures

start  = time.perf_counter()

def do_something(second):
    print(f'sleeping {second} sec')
    time.sleep(second)
    return f'done slepping....{second}'

'''
# create threadpool exicuter
with concurrent.futures.ThreadPoolExecutor() as executor:
    # creates theads takes function and argument as a perameter
    f1 = executor.submit(do_something,1)
    f2 = executor.submit(do_something,3)
    print(f1.result())
    print(f2.result())
'''

# create multipal threadpool exicuter in loop
with concurrent.futures.ThreadPoolExecutor() as executor:
    # creates theads takes function and argument as a perameter
    secs =[5,4,3,2,1]
    result = [executor.submit(do_something,sec) for sec in secs ]
    
    for f in concurrent.futures.as_completed(result):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {finish-start} secondss')