import random
from algorithms import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
)
from vizualizer import visualize

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

visualize(data, generator, title, size)