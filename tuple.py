'''
tuple和list相同,都可以用來保存多個數據
不同的是tuple不能變動
'''
words = ['hello', 'yes', 'hi', 'goods']  # list

nums = (9, 4, 3, 1, 7, 6, 9, 9, 9)  # tuple

'''
和列表依樣也是一個有序的存數據容器,也可以通過下標來獲取元素
'''
# nums[3] = 40  # 會報錯,他不能修改

print(nums.index(7))

print(nums.count(9))


# 特殊情況,如何表示只有一個元素的tuple??

ages = (18)  # 是一個整數不是tuple
ages = (18,)  # 是tuple

print(type(ages))

# list轉成tuple??

print(tuple(words))

# tuple轉成list??

print(list(nums))

heights = ("189", "174", "170")
print('*'.join(heights))  # join要string才可以用
x = "".join(('h', 'e', 'l', 'l', 'o'))  # join結果會是string

print(type(x))

# tuple可以遍歷

for i in nums:
    print(i)
