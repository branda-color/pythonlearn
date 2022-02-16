'''
有一個列表names = ['jack', 'yuyu', 'toto', 'tete']
再讓用戶輸入一個姓名,如果這個姓名在列表裡存在提示用戶姓名已存在
如果不存在就新增
'''
names = ['jack', 'yuyu', 'toto', 'tete']

yuyu = 'yuyu'

# in是一個運算符
# is是 == 的意思

print(yuyu in names)

username = input('請輸入用戶名:')

if username in names:
    print('用戶名已存在')
else:
    names.append(username)
print(names)

# 另一種寫法(for else語句>>for執行完if都沒有跳else)
for name in names:
    if username == name:
        print('用戶已存在')
        break
else:
    names.append(username)
print(names)


# 統計列表裡元素出現次數最多的元素
# 冒泡排序優化
nums = [6, 5, 3, 1, 8, 7, 2, 4]

count = 0
j = 0
'''
第一次沒有多比較
第二次j=1多比較了1次
第三次j=2多比較了2次
'''
while j < len(nums)-1:
    flag = True  # 每一趟都沒有交換
    i = 0
    while i < len(nums)-1-j:
        count += 1
        if nums[i] > nums[i+1]:
            # 只要交換了flag就不成立
            flag = False
            nums[i], nums[i+1] = nums[i+1], nums[i]
        i += 1
    if flag:
        break
    j += 1
print(nums)
print('比較了%d次' % count)

# 求列表裡最大數
num = [3, 1, 9, 8, 0, 7, 2, 5]

# num.sort()
x = num[0]
i = 0
for num1 in num:
    i += 1
    if num1 > x:
        x = num1
        index = i-1
print('發現最大值是:%d.%d' % (x, index))

# 刪除列表空字符串
words = ['hello', '', '', 'good', 'bad', 'ok', '']

# for word in words:
#     if word == '':
#         words.remove(word)
# print(words)

# i = 0
# while i < len(words):
#     if words[i] == '':
#         words.remove(words[i])
#         i -= 1
#     i += 1
# print(words)

words2 = []
for word in words:
    if word != '':
        words2.append(word)
words = words2
print(words)
