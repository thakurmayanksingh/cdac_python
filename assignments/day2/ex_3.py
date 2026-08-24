"""
Exercise 3: Tuple Operations
Given a tuple of numbers: numbers = (10, 20, 30, 40, 50, 60, 70, 80)

Print the element at index 3.
Print the last element of the tuple.
Slice the tuple to get elements from index 2 to 5 (inclusive).
Check if the value 30 exists in the tuple.
"""

def main():
    numbers = (10, 20, 30, 40, 50, 60, 70, 80)
    print(f"Element at index 3: {numbers[3]}")
    print(f"The Last element of the tuple: {numbers[-1]}")
    print(f"Sliced value of the tuple to get elements from index 2 to 5 (inclusive): {numbers[2:6]}")
    print("Yes" if 30 in numbers else "Not Present")

main()