'''
可以保存值,還可以進行描述
'''
person = {'name': '張三', 'age': 18, 'math': 95, 'chinese': 93,
          'english': 95, 'gym': 93, 'height': 180, 'weight': 150}

'''
字典的注意事項
1.key不能重複不然後一個key會覆蓋前一個
2.value可以是任意數據類型

'''

person = {
    'name': '張三',
    'age': 20,
    'age': 100,
    'isPass': True,
    'hobbies': ['sing', 'jump', 'basketball'],
    4: 'good',  # key只要是不可變數聚類型都可以
    ('yes', 'no'): 100,
    # ['ok', 'no']: 'hi'  # 會報錯,list是可變的

}

print(person)


''''
字典的增刪改查
1.字典的數據保存是無順序的,不能通過下標獲取
'''
person = {
    'name': 'sam',
    'age': 100,
    'addr': '襄陽'

}

# 使用key獲取對應value
print(person['name'])

# 需求:獲取一個不存在的key時,不報錯,如果這個key不存在就使用默認值(默認返回None)
print(person.get('gender'))  # none
print(person.get('gender', 'female'))  # 使用默認給定值female

print(person)  # get不會往裡面加東西

# 使用key可以修改對應的value
person['name'] = 'lili'

# 增加可以直接寫
person['gender'] = 'female'

print(person)

# 刪除
x = person.pop('name')  # return執行結果是value
print(x)

result = person.popitem()  # 會return 給你刪掉的元素

del person['addr']

print(person)

print(result)

person.clear()  # 把字典清空


# update方法的使用
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9]

nums1.extend(nums2)
print(nums1)

person2 = {
    'name': 'yuyu', 'age': 22
}
person3 = {
    'addr': 'Jp', 'height': 180
}

person2.update(person3)

# x= person2+person3   字典不支持加法只能用update的

print(person2)

words1 = ('jello', 'good')
words2 = ('123', 'wwww')
print(words1+words2)  # 不改變原本的tuple就可以用

'''
字典的遍歷方式
'''
person = {'name': '張三', 'age': 18,  'height': 180}

for x in person:  # 像是foreach用法
    print(x, '=', person[x])


# 獲取所有key再來遍歷key獲取value

print(person.keys())
for k in person.keys():
    print(k, person[k])


# 獲取所有value>>沒有key
for v in person.values():
    print(v)

# 把列表的數據變成tuple
print(person.items())

for item in person.items():
    print(item[0], '=', item[1])

for k, v in person.items():
    print(k, '=', v)


# 把字典內KEY跟value換位置

dic = {
    "a": 100, "b": 200, "c": 300
}

dic2 = {}

for k, v in dic.items():
    dic2[v] = k

print(dic2)


# 字典推導式

dic = {v: k for k, v in dic.items()}
