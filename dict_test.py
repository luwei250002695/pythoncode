dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

for key in dict.keys():   # 遍历key
    print(key)
for velue in dict.values():    # 遍历
    print(velue)
for k, v in dict.items():   # 遍历key，value
    print(k,':',v)
# print(dict['Name'], dict['Age'])
# print(len(dict), dict, type(dict))
str2 = str(dict)              # 字典转为字符串 '{'Name': 'Runoob', 'Age': 7, 'Class': 'First'}'

num1 = int(input('请输入：'))   # 斐波那契
j = 0
a, b = 0, 1
while b <= num1:
    print(b, end=',')
    a, b = b, a + b
    j += 1
    # dict.update(b = j)  # b是不改变的
    dict[b] = j
print(dict)
num2 = int(input('请输入：'))
print(dict[num2])

# while 1:
#     num2 = int(input('请输入：'))
#     if type(num2) == int:
#         print(dict[num2])

