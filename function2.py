# 生成随机验证码
import random
import string

ALL_CHARS = string.digits + string.ascii_letters

def generate_code (*, code_len = 4):
    """
    生产指定长度的验证码
    Args:
        code_len (int, optional): _description_. Defaults to 4.
    Returns:
        _type_: _description_
    """    
    return ''.join(random.choices(ALL_CHARS, k=code_len))
print(generate_code(code_len=10))


def calc(fnc, *a, **b):
    items = list(a) + list(b.values())
    print(a)
    total = 0
    print(items)
    for el in items:
        if type(el) in [int, float]:
            total = fnc(total, el)
    print(total)        
    return total  

def add (a, b):
    return a + b
def mul (a, b):
    return a * b
calc(add, 1, 2, 'k', name=123)
calc(mul, 1, 2, 'k', name=123)

