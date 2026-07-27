# 📊 Sorting Algorithm Visualizer

A Python-based application that visually demonstrates how different sorting algorithms work using animated bar charts. This project helps understand the internal working of sorting algorithms by displaying each intermediate step during the sorting process.

## 🚀 Features

- Visualizes sorting algorithms in real time.
- Randomly generates an unsorted array.
- User can choose the sorting algorithm.
- Smooth animation using Matplotlib.
- Step-by-step visualization implemented using Python generators.

## 🛠️ Technologies Used

- Python 3.x
- Matplotlib
- Random Module

---

## 📂 Project Structure

```
Sorting-Algorithm-Visualizer/
│
├── algorithms.py      # Sorting algorithm implementations
├── vizualizer.py      # Visualization using Matplotlib
├── main.py            # Main driver program
└── README.md
```

---

## 📌 Implemented Algorithms

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Sorting-Algorithm-Visualizer.git
```

### 2. Navigate to the project

```bash
cd Sorting-Algorithm-Visualizer
```

### 3. Install dependencies

```bash
pip install matplotlib
```

---

## ▶️ Running the Project

Execute the main file.

```bash
python main.py
```

You will be prompted to enter:

```
Enter array size:
```

Then choose the sorting algorithm:

```
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
```

A visualization window will open displaying the sorting process.

---

## 📸 Working

1. User enters the desired array size.
2. A random array is generated.
3. User selects a sorting algorithm.
4. The selected algorithm sorts the array.
5. Every intermediate state is animated using Matplotlib.

---

## 💡 How It Works

Each sorting algorithm is implemented as a **Python Generator**.

Instead of returning the sorted array directly, the algorithm yields the array after every important modification.

Example:

```python
yield a
```

Matplotlib's `FuncAnimation` consumes these yielded states and updates the heights of the bars to create a smooth animation.

---

## 📈 Time Complexities

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |

---

## 🎯 Learning Objectives

This project helps understand:

- Sorting algorithm logic
- Time complexity comparison
- Python generators (`yield`)
- Data visualization with Matplotlib
- Animation using `FuncAnimation`
- Modular programming in Python

---

## 🔮 Future Enhancements

- Adjustable animation speed.
- Pause and Resume functionality.
- Color comparison between sorted and unsorted elements.
- Add Heap Sort.
- Add Counting Sort.
- Add Radix Sort.
- Compare two algorithms simultaneously.
- GUI using Tkinter or PyQt.
- Display real-time statistics (comparisons and swaps).

---

## 👨‍💻 Author

**Sidhant Sahni**

If you found this project helpful, feel free to ⭐ the repository.
