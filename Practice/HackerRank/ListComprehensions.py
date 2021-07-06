x=int(input())+1
y=int(input())+1
z=int(input())+1
n=int(input())

output = list()

for i in range(x):
    for j in range(y):
        for k in range(z):
            if i + j + k == n:
                continue
            output.append([i,j,k])

print(output)

