# 存五個人的年齡算平均值
#  利用列表:有序的集合
#  創建list>>格式:格式名 = [列表選項1,列表選項2......,列表選項n]

import copy
import random
list1 = []

print(list1)


list2 = [18, 19, 20, 21, 22]

index = 0
sum = 0

# 不要超過三層
while index < 5:
    sum += list2[index]

    index += 1
    # if index == 5:
print("平均年齡%d" % (sum/5))


# list裡面的元素可以是不同類型的(但一般使用上會存相同的型態)
# 注意不要越界(下標超出可表示範圍)
list3 = [1, 2, 3, "a", "b", "h"]
print(list3)

# list元素取值>>格式:列表名[下標]
list4 = [1, 2, 3, 4, 5]
print(list4[2])

# 替換

list4[2] = 300
print(list4)


# list的操作:

# list組合
list5 = [1, 2, 3]
list6 = [4, 5, 6]

list7 = list5+list6

print(list7)

# list重複
list8 = [1, 2, 3]

print(list8*3)

# 判斷元素是否在list中
list9 = [1, 2, 3, 4, 5]
print(3 in list9)
print(6 in list9)

# 列表擷取
list10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list10[2:6])
print(list10[3:])
print(list10[:5])

# 二維list
list11 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list11[1][1])

# 列表方法
# append>>在列表裡面增加"元素"
list12 = [1, 2, 3, 4, 5]
list12.append(6)
list12.append([7, 8, 9])
print(list12)


# 追加方式不一樣(在末尾一次性追加另一個列表的多個值)
list13 = [1, 2, 3, 4, 5]
list13.extend([6, 7, 8])
print(list13)

# 不覆蓋原數據,原數據向後順延
list14 = [1, 2, 3, 4, 5]
list14.insert(1, 100)
list14.insert(0, [2, 2, 3])
print(list14)


# pop(x = list(-1))
# 移除列表中指定下標處的元素(默認移除最後一個)
list15 = [1, 2, 3, 4, 5]
print(list15[-1])
list15.pop()
list15.pop(2)
print(list15.pop(1))
print(list15)

# 移除列表中某個元素(第一個匹配的結果)
list16 = [1, 2, 3, 4, 5, 6]
list16.remove(4)
print(list16)


# 清除列表所有元素
list17 = [1, 2, 3, 45]
list17.clear()
print(list17)


# 從列表中找出某值的下標
list18 = [1, 2, 3, 4, 5, 3, 4, 5, 6]
index18 = list18.index(3)
# 後面兩個參數表示範圍
index19 = list18.index(3, 3, 6)

print(index19)
print(index18)


# 裡面有幾個元素
list20 = [1, 2, 3, 4, 5]
print(len(list20))


# 獲取最大值
list21 = [1, 2, 3, 4, 5]
print(max(list21))
# 獲取最小值
print(min(list21))

# 查看列表中所出現的次數
list23 = [2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
print(list23.count(2))

num24 = 0

while num24 < list23.count(2):
    list23.remove(2)
    num24 += 1
print(list23)


# 倒敘陣列內的值
list25 = [2, 1, 3, 4, 5]
list25.reverse()
print(list25)

# 排序
list26 = [6, 4, 8, 1, 2]
list26.sort()
print(list26)

# 淺拷貝(因為底層的變數是存在暫存區>>暫存區內在存記憶體的地址)
list27 = [1, 2, 3, 4, 5]
list28 = list27

list28[1] = 200

print(list27, list28)


# 深拷貝(暫存區存的地址是不同的記憶體地址)
list29 = [1, 2, 3, 4, 5]
list30 = list29.copy()

list30[1] = 200
# 印出記憶體的地址
print(id(list30), id(list29))

print(list29, list30)

list31 = list((1, 2, 3, 4))
print(list31)


# 切片是一個淺拷貝

names1 = ['張三', '李四', '王武', '捷克']
names2 = names1[::]

names1[0] = 'jeery'
print(names2)


# 列表嵌套

nums = [1, 2, [100, 200, 500], 3, 4, 5]
'''
一個學校有10個老師,三個辦公室,等待工作分配
tips:房間隨機把老師塞進去
'''
teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j']
rooms = [[], [], []]

for teacher in teachers:
    room = random.choice(rooms)
    room.append(teacher)
print(rooms)

# 列表推導式(使用簡單語法實現創建列表)

list32 = [i for i in range(10)]

print(list32)

list33 = [i for i in range(10) if i % 2 == 0]

print(list33)


# 淺拷貝vs.深拷貝

words = ['hello', 'good', [100, 200, 300], 'yes', 'ho', 'ok']

'''
淺拷貝不會拷貝內層列表,要完全拷貝不同的要用深拷貝
'''


words1 = words.copy()

words2 = copy.deepcopy(words)

words[0] = '你好'

print(words1)

words[2][0] = 1

print(words1)

print(words2)
