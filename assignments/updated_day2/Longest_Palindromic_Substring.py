"""
Exercise 9: Longest Palindromic Substring
Write a program that prompts the user to enter a text string and finds the longest substring within it that reads the same forward and backward. If there are multiple palindromic substrings of the same maximum length, print any one of them.
               01234
Sample Input: "babad"
Sample Output: "bab" (or "aba")
Sample Input: "cbbd"
Sample Output: "bb"
"""

def palindrome(st):
    return st == st[::-1]

def main():
    
    inp = input("Sample Input: ")
    max_len = 0
    ans = ''

    for i in range(len(inp)):
        for j in range(i+1, len(inp)):
            if palindrome(inp[i:j+1]) and max_len < len(inp[i:j+1]):
                max_len = len(inp[i:j+1])
                ans = inp[i:j+1]

    print(f"Sample Output: {ans}")

if __name__ == "__main__":
    main()