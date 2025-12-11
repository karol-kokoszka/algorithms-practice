# Algorithms Practice

This project is designed for practicing various algorithms, including sorting and searching techniques. It provides implementations of common algorithms and includes unit tests to ensure their correctness.

## Project Structure

```
algorithms-practice/
├── src/
│   ├── __init__.py
│   ├── sorting.py
│   ├── searching.py
│   └── utils.py
├── tests/
│   ├── test_sorting.py
│   ├── test_searching.py
│   └── test_utils.py
├── requirements.txt
└── README.md
```

## Algorithms Implemented

### Sorting Algorithms
- **Bubble Sort**: A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- **Quick Sort**: An efficient sorting algorithm that uses a divide-and-conquer approach to sort elements.
- **Merge Sort**: A stable sorting algorithm that divides the list into halves, sorts them, and then merges them back together.

### Searching Algorithms
- **Linear Search**: A straightforward search algorithm that checks each element in the list until the desired element is found.
- **Binary Search**: An efficient search algorithm that finds the position of a target value within a sorted array.

## Utilities
- **Swap**: A utility function to swap two elements in a list.
- **Generate Random List**: A utility function to create a list of random integers for testing purposes.

## Running Tests

To run the tests for this project, ensure you have the necessary dependencies installed. You can install them using:

```
pip install -r requirements.txt
```

Then, you can run the tests using your preferred testing framework. For example, if you are using pytest, you can run:

```
pytest tests/
```

## Usage

You can import the algorithms from the `src` package in your Python scripts. For example:

```python
from src.sorting import bubble_sort
from src.searching import binary_search
```

Feel free to explore and modify the algorithms as you practice!