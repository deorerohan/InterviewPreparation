x = int(input()) + 1
y = int(input()) + 1
z = int(input()) + 1
n = int(input())

output = list()


def UsingForLoop(x, y, z, n):
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if i + j + k == n:
                    continue
                output.append([i, j, k])

    print(output)


def UsingComprehension(x, y, z, n):
    output = [
        [i, j, k]
        for k in range(z)
        for j in range(y)
        for i in range(x)
        if i + j + k != n
    ]
    # if i+j+k != n
    print(output)


UsingComprehension(x, y, z, n)
