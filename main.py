import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Sorting Algorithms

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            yield a


def selection_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]
        yield a


def insertion_sort(arr):
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
            yield a

        a[j+1] = key
        yield a


# Merge Sort Generator
def merge_sort(arr):

    def merge_sort_recursive(a, l, r):
        if r - l <= 1:
            return

        mid = (l + r) // 2

        yield from merge_sort_recursive(a, l, mid)
        yield from merge_sort_recursive(a, mid, r)

        left = a[l:mid]
        right = a[mid:r]

        i = j = 0
        k = l

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1

            k += 1
            yield a

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
            yield a

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
            yield a

    a = arr.copy()
    yield from merge_sort_recursive(a, 0, len(a))


# Quick Sort Generator
def quick_sort(arr):

    def quick_sort_recursive(a, low, high):
        if low >= high:
            return

        pivot = a[high]
        i = low

        for j in range(low, high):

            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
                yield a

        a[i], a[high] = a[high], a[i]
        yield a

        yield from quick_sort_recursive(a, low, i-1)
        yield from quick_sort_recursive(a, i+1, high)

    a = arr.copy()
    yield from quick_sort_recursive(a, 0, len(a)-1)


# User Input

size = int(input("Enter array size: "))

print("\nChoose Sorting Algorithm")
print("1. Bubble Sort")
print("2. Selection Sort")
print("3. Insertion Sort")
print("4. Merge Sort")
print("5. Quick Sort")

choice = int(input("Enter choice: "))

data = list(range(1, size+1))
random.shuffle(data)

# Algorithm Selection

if choice == 1:
    generator = bubble_sort(data)
    title = "Bubble Sort"

elif choice == 2:
    generator = selection_sort(data)
    title = "Selection Sort"

elif choice == 3:
    generator = insertion_sort(data)
    title = "Insertion Sort"

elif choice == 4:
    generator = merge_sort(data)
    title = "Merge Sort"

elif choice == 5:
    generator = quick_sort(data)
    title = "Quick Sort"

else:
    print("Invalid Choice")
    exit()

#Visualization 

fig, ax = plt.subplots()

bars = ax.bar(range(len(data)), data)

ax.set_title(title)
ax.set_xlim(0, size)
ax.set_ylim(0, int(size*1.1))

def update(arr):
    for bar, val in zip(bars, arr):
        bar.set_height(val)

ani = animation.FuncAnimation(
    fig,
    update,
    frames=generator,
    interval=50,
    repeat=False
)

plt.show()