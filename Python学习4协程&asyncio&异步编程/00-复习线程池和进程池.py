# 线程池导入
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading

#
# def f(n):
#     time.sleep(2)
#     # print(n)
#     # print("进程(%s) %s的平方: %s" % (os.getpid(), n, n*n))
#     # print(threading.current_thread().getName(), n, n * n)
#     return n * n
#
#
# # 创建一个线程池或者进程池
# pool = ThreadPoolExecutor(max_workers=5)
# # pool = ProcessPoolExecutor(max_workers=5)
# ret_list = []
# for i in range(10):
#     # 异步提交任务,f函数名称或者方法名称,i给f函数的参数
#     ret = pool.submit(f, i)
#     print(ret)
#     # print(ret.result())
#     ret_list.append(ret)
#
# # 锁定线程池,不让新任务再提交进来了.轻易不用
# # pool.shutdown()
# for i in ret_list:
#     print(i.result())


# 本人比较推荐第二种方式
# 线程池的另一种使用方式
from multiprocessing.dummy import Pool as ThreadPool
# from multiprocessing import Pool
import time


def func1(n):
    time.sleep(2)
    print(n)


n_list = [i for i in range(10)]

# 基于线程池处理任务
pool = ThreadPool(4)
pool.map(func1, n_list)
pool.close()
pool.join()
# 基于进程池处理任务
# if __name__ == '__main__':
#     pool = Pool(processes=4)
#     pool.map(func1, n_list)
