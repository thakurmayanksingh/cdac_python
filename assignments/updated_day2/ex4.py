"""
Write a program that prompts the user to enter a string and counts:

The individual frequency of each vowel (a, e, i, o, u), case-insensitively.
The total count of all consonants.
Sample Input: "Vinod Kumar Kayartaya"
Sample Output:
Vowel Frequencies:
a: 4
e: 0
i: 1
o: 1
u: 1
Total Consonants: 12
"""

def main():
    inp = input("Sample Input: ")
    mp = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    con = 0
    for char in inp:
        if char.lower() in ('a', 'e', 'i', 'o', 'u'):
            mp[char] += 1
        else:
            if char.isalpha():
                con += 1
    print("Sample Output:")
    print("Vowel Frequencies: ")
    for item in mp:
        print(f"{item}: {mp[item]}")
    print(f"Total Consonants: {con}")

if __name__ == "__main__":
    main()