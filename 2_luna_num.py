inp = input()

summ = 0
for i in range(len(inp)):
    current_num = int(inp[i])
    if i % 2 == 0:
        current_num *= 2
        if current_num > 9:
            current_num -= 9
    summ += current_num
print(-summ % 10)
