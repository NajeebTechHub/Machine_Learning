# it's a higher order function cause recieve func as input 

import functools as ft
a = ft.reduce(lambda x,y:x+y,[1,3,5,7,7])
print(a)

min = ft.reduce(lambda x,y:x if x<y else y,[56,78,90,56,45,33,21])
print(min)