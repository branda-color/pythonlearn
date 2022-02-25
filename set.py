'''
不重複的無序,數據集合{}或set來表示
{}:兩種意思>>字典/集合
{}若裡面放單個值就是集合
如果有重複的數據就會被去除
沒有查詢方法!!因為它是無序的
'''
from unicodedata import name


x = {'hello', 'good', 1}

names = {'yuyu', 'wewe', 'rere', 'yuyu'}

print(names)

# 添加一個元素
names.add('lili')

print(names)

# 清空集合
# names.clear()
# 空集合的表示方式是set() ////如果{}是表示空字典

# 刪除隨機集合元素
# names.pop()
print(names)

# 指定刪除集合元素
names.remove('yuyu')

print(names)

# 將多個集合合併生成一個新的集合
a = names.union({'ruru', 'erer'})

print(a)

# update是用舊的去合併

names.update(['aa', 'bb'])

print(names)


first = {'lili', 'yuyu', 'rere'}
second = {'one', 'two', 'three'}
third = {'qqq', 'aaa', 'xxxx', 'yuyu'}

# 可以用減法來計算差集
print(third - first)
# 可以用減法來計算交集
print(first & third)

# 可以求聯集
print(first | third)

# 聯集那塊扣掉交集(不同的就出現相同的不要)
print(first ^ third)


# 型別互相轉換
nums = [5, 8, 9, 7, 1, 1, 1, 1, 2, 2, 2, 4, 5, 8, 9]
x = set(nums)
y = list(x)

y.sort()

print(y)
