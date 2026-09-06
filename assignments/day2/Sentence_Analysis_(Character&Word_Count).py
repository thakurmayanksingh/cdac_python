"""
Exercise 1: Sentence Analysis (Character & Word Count)
Write a Python program that prompts the user to enter a sentence. The program must count and display:

The total number of characters (including spaces and punctuation).
The total number of words.
Sample Input: "Learning Python is fun!"
Sample Output:
Total Characters: 23
Total Words: 4
"""
def main():
    inp = input("Sample Input: ")
    print("Sample Output:")
    print(f"Total Characters: {len(inp)}")
    print(f"Total Words: {len(inp.split())}")

if __name__ == "__main__":
    main()