import time
import random
from functools import wraps
def record_time (func):
    @wraps(func)
    def wrap (*args, **kwargs):
        start = time.time()
        result =  func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result
    return wrap


@record_time
def downLoad ():
    print('下载开始..')
    time.sleep(random.random() * 6)
    print('下载结束')

@record_time
def upload ():
    print('上传开始..')
    time.sleep(random.random() * 6)
    print('上传结束')
downLoad.__wrapped__()
upload()