import copy


class T1:
    name = 't1'

t1 = T1()
t2 = copy.deepcopy(t1)
t2.name = 't2'
print(type(t2), t2.name)
print(type(t1), t1.name)