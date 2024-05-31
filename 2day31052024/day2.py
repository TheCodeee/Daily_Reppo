list = [12, 3, 7, 8, 13, 23]
target = 25

for l in list:
    for m in list:
        if m + l == target:
            break
    if m + l == target:
        print("target achived = ", target)
        break
