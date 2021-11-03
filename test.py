# n = 4 
# f = open('result.txt', 'w')

# for i in range(n, 2*n): 
#     current_string = ' '*(2*n-1) * i + '\n'
#     import pdb; pdb.set_trace()
#     f.write(current_string)
# f.close()


# import requests

# print(requests.get('https://www.youtube.com/').tex


# d = {}
# import time 
# import requests
# def benshmark(iter=10):
#     def dekorator(func): 
#         def wrapper(*args, **kwargs):
#             print('до функции') 
#             start = time.time()
#             result = func()
#             func_name = func.__qualname__
#             d.update (
#                 {
#                     func_name: d.get(func_name, 0) + 1
#                 }
#             )
#             import pdb; pdb.set_trace()
#             # for i in range(10):
#             #     result = func(*args, **kwargs)
#             finish = time.time()
#             print('После функции')
#             print(f'Вермя выполнения функции:{(finish-start)/iter}')
#             return result 
#         return wrapper
#     return dekorator   

# @benshmark(iter=5)
# def hallo(name='worold'):
#     print(f'Hallo,{name}')
#     # requastest get('https://www.youtube.com/')
#     time.sleep(0.5)

# @benshmark(iter=5)
# def name():
#     print(12435467)

# hallo('art')
# name()

# hallo('art')
# name()

# print(d)


# def countdown(n): 
#     print('Start working ')
#     while n>0:
#         yield n
#         n -= 1 
        
# timer = countdown(10)
# for t in timer:
#     print(t)

# list =['a', 'b', 'c', 'f', 'm']
# gen = (x for x in list)

# print(type(gen))

# for x in gen:
#     print(x)

def check_logs(patch=None):
    f = open(patch, 'r')
    for i, l in enumerate(f):
        if 'ERROR' in l:
            yield i+1 
    f.close() 

logger = check_logs('new.txt')
for log in logger:
    if log > 10:
        break 
    print(log) 
    
