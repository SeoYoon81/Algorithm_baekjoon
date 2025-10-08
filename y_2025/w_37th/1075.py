n = int(input())
f = int(input())
now = ((n//100) * 100)%f
for i in range(f):
    if (now + i)%f == 0:
        answer = i
        break

if i < 10:
    print('0'+str(i))
else:
    print(i)