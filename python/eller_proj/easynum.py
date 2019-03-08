list = []
i = 1
while len(list)!=10000:
    if i == 1:
        list.append(i)
        i+=1
        continue
    if i > 1:
        q = 0
        for x in range(1,i):
            if i % x == 0:
                q+=1
        if q == 0:
            list.append(i)
            print(len(list))
            continue
        else:
            continue


print(list[len(list)-1])