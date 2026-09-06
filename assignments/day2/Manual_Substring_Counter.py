"""
Exercise 7: Manual Substring Counter
Write a program that prompts the user to enter a main text string and a substring.
Count how many times the substring appears in the main string without using Python's built-in .count() method.

Sample Input: (User inputs main string "banana" and substring "an")
Sample Output: 2

"""

def main():
    inp = input("Input String: ")
    sub = input("Substring: ")
    window = len(sub)
    cnt = 0
    i, j = 0, window
    while j <= len(inp):
        if inp[i:j]==sub:
            cnt += 1
            i += 1
            j += 1
        else:
            i += 1
            j += 1
    print(cnt)

if __name__ == "__main__":
    main()