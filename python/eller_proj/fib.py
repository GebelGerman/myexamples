list  = [1,1]
while True:
    q = list[len(list)-1] + list[len(list)-2]
    if q < 4000000:
        list.append(q)
    else:
        break
sum=0
for i in list:
    if i%2==0:
        sum+=i

print(sum)