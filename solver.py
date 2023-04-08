def insertion(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        j = i-1
        while j>=0 and arr[j]>value:
            # print(i)
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = value
        print(arr)
    print(arr)


def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
        print(arr)
    print(arr)
def heap(arr):
    print("heap")


def merge(arr):
    print("merge")


def quick(arr):
    print("quick")


def print_(arr):
    print(arr)


def end(a):
    print("koniec")


def interactive(a):
    command = input().split()
    functions = [print_, insertion, bubble, heap, merge, quick, end]
    if command:
        functions[int(command[0])](a)


first = input().split()
array = list(map(float, first[2:]))
print(array)

while True:
    try:
        interactive(array)
    except EOFError:
        break
# insertion([5, 4, 6, 1])