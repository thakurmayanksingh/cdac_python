"""
Exercise 2: Reversed Uppercased String
Write a program that takes a string input from the user, reverses the string, converts the entire reversed string to uppercase, and prints the result.

Sample Input: "Bangalore"
Sample Output: "EROLAGNAB"
"""

def main():
    inp = input("Sample Input: ")
    print(f"Sample Output: {inp[::-1].upper()}")

if __name__ == "__main__":
    main()