i = 2
while i <= 1000:
    if i % 2 != 0:
        i = i - 1
    else:
        i = i * i
        i = i + 1
        print(i)