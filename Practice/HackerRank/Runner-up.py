if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    sortedList = list(set(arr))
    sortedList.sort()
    print(sortedList[-2])
