t1 = ('1', '2', '3')
t2 = ('骆昊', 45, True, '四川成都')
print(type(t1))
print(type(t2))
print(len(t1))
print(t1[1])
print(t2[-2])
print(t2[:3])
print(type((1,)))
t3 =  'a', 'c', 'vv', 'ck'
w1,*w2,w3 = t3
print(type(t3))
print(type(w1))
print(w1)
print(w2)
print(type(w2))
a, *b, c = 'hello'
print(a, b, c)
import timeit

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

infos = ('骆昊', 45, True, '四川成都')
print(infos[1])
print(type(list(infos)))

frts = ['apple', 'banana', 'orange']
frts[1] = 'new'
print(frts)
print(type(tuple(frts)))