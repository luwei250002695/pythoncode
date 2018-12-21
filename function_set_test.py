# x = set('runoob')
# y = set('google77')
x = set(['runoob','AAA'])
y = set(['google',7])
print(x, y)
print(x & y)  #交集为空，set()
# print(x + y)  #set不能相加
print(x | y)  #X + Y,交集
print(x - y)  #只显示X
print(len(x))

list1 = [2, 3, 4, 5, 5, 5, 9, 8]
list2 = [2, 13, 14, 15, 5, 5, 91, 8]
list1 += list2
list1.sort()
list1 = set(list1)  #list去重