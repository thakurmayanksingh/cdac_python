"""
Exercise 4: Reverse a String using Slicing
Write a function that accepts a string input from the user and returns the reversed string using sequence slicing.

Sample Input: "CDAC Pune"
Sample Output: "enuP CADC"
"""

def main():
    inp = input("Sample Input: ")
    print(inp[::-1])

main()