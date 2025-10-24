x = lambda x : x%2==0

print(x(10))

List = [1,2,3,4,5]

map_result = map(lambda num : num*num,List)
print(list(map_result))

filter_result = filter(lambda num : num>3,List)
print(list(filter_result))

import functools
result_reduce = functools.reduce(lambda x,y:x+y,List)
print(result_reduce)