items = ["apple", "banana", "orange", "apple", "mango"]

for i in range(len(items)):
    f = 0
    for j in range(i + 1, len(items)):
        if items[i] == items[j]:
            print(items[i])
            f = 1
            break
    if f == 1:
        break