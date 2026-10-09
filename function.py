def count (a, b):
    return a + b*2

print(count(a=3, b=4))

def nunCount (*a):
    total = 0
    for ar in a:
        if type(ar) == int or type(ar) == float:
            total = total + ar
    return total    
print(nunCount(1, 22, '你好啊', [100, '不是']))

def fn1 (*a, **b):
    print(a)
    print(b)
fn1('0', 'vv', name='1')   
