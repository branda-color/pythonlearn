a = 100

x = 'hello'

world = 'yaya'


def test():
    x = 'hello222'
    print('x={}'.format(x))

    a = 10
    print('內部a = {}'.format(a))

    global world

    world = 'OK'

    '''
    globalst查看全局變量
    localst查看局部變量
    '''

    print('locals = {},globals={}'.format(locals(), globals()))


test()


print('外部a = {}'.format(a))
print('外部world = {}'.format(world))


'''
只有函數可以切割變量
if裡面還是全局變量
'''
if 3 > 2:
    m = 'hi'
