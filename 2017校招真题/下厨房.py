# 第一个问题就是输入的问题，没说输入多少行
# 第二个问题就是去掉重复字符的问题

_repeat = 0
x = []

rep_time = int(input("How many lines to input:"))

# while (_repeat<rep_time):
#     try:
#         m = input().split()
#         x.extend(m)
#     except:
#         print(len(set(x)))
#         break
#     _repeat+=1

while (_repeat<rep_time):
    x.extend(input().split())
    _repeat+=1

print(list(set(x)))