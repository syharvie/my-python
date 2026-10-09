set1 = {1,2,2,3,3,44}
print(set1)
set2 = [1,2,2,3,3,44]
print(set(set2))
print(set('hello'))
print({num for num in range(1, 20) if num % 3 == 0})
set3 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
for el in set3:
    print(el)
set4 = {1, 999, 20001, 'Swift'}    
set4.add(100)
set4.add(18650)
print(set4)
set4.discard(999)
print(set4 & set3)
print(set4 | set3)
print(set4 - set3)
print(set3.isdisjoint(set4))

set5 = frozenset({'s', 'v', 'p'})