import random
random.seed(10)
print(random.random())
random.seed(10)
print(random.random())
random.seed(12)
print(random.random())
random.seed(10)
print(random.random())

xx = 13
print(xx)


def test_1(xx):
    xx += 2
    print(xx)
    for i in range(1, xx):
        print(i)




#
# if __name__ == '__main__':
#     print(__name__)
#     # test_1(3)
#     test_seed(5)
