random = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

i = 0
while i< len(random):
    if random[i]%3 ==0:
        print(random[i])
        i += 1
    else:
        i += 1