# 存五個人的年齡算平均值
#  利用列表:有序的集合
#  創建list>>格式:格式名 = [列表選項1,列表選項2......,列表選項n]

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


# list裡面的元素可以是不同類型的
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
