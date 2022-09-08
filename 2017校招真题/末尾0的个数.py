x = int(input())

### Ver 01
n = 1
for i in range(1, x + 1):
    n *= i
n = str(n)[::-1]
count = 0
for i in n:
    if i != '0':
        break
    count += 1
print("count=", count, "\n")


### Ver 02
n2 = 1
for i in range(1, x + 1):
    n2 *= i

count2 = 0
while (n2%10==0):
    n2 = n2 // 10
    count2 += 1

print("count2=", count2)