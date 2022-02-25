# 內置類 list tuple set
import json as js
nums = [9, 8, 4, 3, 2, 1]

a = tuple(nums)  # 轉換成tuple

print(a)

u = set(a)

print(u)

# 如果用dic去轉會變只剩key值
z = list({'yuyu': 'ioio', 'age': 18})

# eval>>可以執行字符串裡面的代碼
a = 'input("請輸入用戶名")'

print(eval(a))

# json使用

person = {'name': '張三', 'age': 18, 'math': 95, 'chinese': 93,
          'english': 95, 'gym': 93, 'height': 180, 'weight': 150}

m = js.dumps(person)

print(m)

print(type(m))

n = '{"name": "李四", "age": 100, "math": 95, "chinese": 93,"english": 95, "gym": 93, "height": 180, "weight": 150}'

p = eval(n)

# 將json轉換成為字典
cc = js.loads(n)
print(type(cc))

# json裡面的陣列只有list跟tuple可以直接轉換
print(js.dumps(['hi', 'ww', 'wewewe', 'aaaa']))
print(js.dumps(('hi', 'ww', 'wewewe', 'aaaa')))
