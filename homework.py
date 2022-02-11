# 第一題
num = 100
while num <= 999:
    a = num % 10
    b = num // 10 % 10
    c = num // 100
    if num == a**3 + b**3 + c**3:
        print(num)

        # python沒有++
    num += 1

# 找出最大值+第二最大值
# while大於10才會停止(也就是input一次接收一個數字最大到9)

listNum = []
num = 0
while num < 5:
    var = int(input())

    listNum.append(var)
    num += 1
print(listNum)

listNum.sort()
count = listNum.count(listNum[len(listNum)-1])

c = 0
while c < count:
    listNum.pop()
    c += 1
print(listNum[len(listNum)-1])
