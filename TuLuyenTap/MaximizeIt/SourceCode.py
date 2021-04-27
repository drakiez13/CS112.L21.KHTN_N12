def binh_phuong_mod(l,m):
    _l = []
    for _ in l:
        _l.append((_**2)%m)
    return _l

k,m=map(int,input().split())
l=[]

for _ in range(k):
    l.append(list(map(int,input().split())))
    l[_]=binh_phuong_mod(l[_][1:], m)
    
import itertools

max_yeah = -1

for t in itertools.product(*l):
    _ = sum(t) % m
    if _ > max_yeah:
        max_yeah = _

print(max_yeah)
