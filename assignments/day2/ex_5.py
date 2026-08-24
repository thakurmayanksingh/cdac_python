"""
Exercise 5: Vowel and Consonant Counter
Write a program that accepts a string and counts the total number of vowels and consonants inside it.

Sample Input: "Python programming"
Sample Output: Vowels: 4, Consonants: 13
"""

def main():
    inp = input("Sample Input: ")
    v = 0
    c = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in inp.replace(" ", ""):
        if char in vowels:
            v += 1
        else:
            c += 1
    print(f"Vowels: {v}, Consonants: {c}")


main()