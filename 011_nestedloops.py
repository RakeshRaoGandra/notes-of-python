i = 2
while i < 20:
    print(i)
    i = i * 2
print("End", i)





count = 0
for i in range(1, 5):
    for j in range(1, 5):
        if i + j == 5:
            print(i, j)
            count = count + 1
print("Count:", count)

for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()