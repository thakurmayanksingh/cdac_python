"""
Exercise 2: Character Frequency Counter
Write a Python program to count the number of occurrences of each character in a given string. Store the output in a clean, readable format.

Sample Input: "hello"
Sample Output:
h: 1
e: 1
l: 2
o: 1
"""
def main():
    inp = input("Enter String: ")
    mp = {}
    for char in inp:
        if char in mp:
            mp[char] += 1
        else:
            mp[char] = 1
    for item in mp:
        print(f"{item}: {mp[item]}")

main()