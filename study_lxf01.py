# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:33:18 2017

@author: sunjingjing
"""

#name = input()
#print('hello',name)

#name = input('pleae input you name:')
#print('hello',name)

#L1 = ['Hello', 'World', 18, 'Apple', None]
#L2 = [x.lower() for x in L1 if isinstance(x, (str))]
#print(L2)

#列表生成式
#L1 =['Hello', 'World', 18, 'Apple', None]
#L2 = [x for x in L1 if isinstance(x,(str)) ]
#print(L2)

#生成器
##list
#L1 = [v*v for v in range(10)]
#print(L1)
##generator
#L2 = (v for v in range(10))
##print(L2)
#for n in L2:
#    print(n)

#斐波拉契数列
def fib(max):
    n,a,b=0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'done'

fib(4)

#list,tuple,dict,set,str等iterable --迭代对象
#一类是generator，包括生成器和带yield的generator function ---迭代器
