'''
函數介紹
多行代碼打包成一個整體
使用def關鍵字來聲明函數
'''


def tell_story(place, person1, person2):
    # place = '廟'
    # person1 = '老和尚'
    # person2 = '小和尚'
    print('從前有做河')
    print('河邊有座'+place)
    print('廟裡有個'+person1)
    print('還有一個'+person2)
    print(person1+'再給'+person2+'講故事')


tell_story('道觀', '老道', '道童')
tell_story(place='小河', person2='老道', person1='道童')  # 變量賦值不用按照順序

'''
返回值就是執行結果,並不是所有函數都要有返回值
如果一個函數枚有返回值那他的返回值就是None
'''


def add(a: int, b: int):
    """
    相加
    """
    c = a+b

    return c


result = add(1, 2)

print(result**2)


help(add)

y = add('hello', 'ass')

print(y)


def test1():
    print('test1開始')
    print('test1end')


def test2():
    print('test2start')
    test1()
    print('test2end')


test2()


def sum(n, m):
    x = 0
    for i in range(n, m):
        x += i
    return x


q = sum(0, 101)

print(q)


def test(a, b):
    x = a//b
    y = a % b
    # return [x, y]
    # return {'x': x, 'y': y}
    return x, y


print(test(13, 5))
