"""
Exercise 1: Palindrome Checker
Write a function that checks whether a given string is a palindrome (reads the same forward and backward, ignoring spaces and letter case).

Sample Input: "A man a plan a canal Panama"
Sample Output: True
"""
def main():
    s = input("Enter String: ")
    n = s.replace(" ", "").lower()
    i = 0
    j = len(n)-1
    while i<=j:
        if n[i] != n[j]:
            print(f"'{s}' is not a palindrome!")
            return
        i += 1
        j -= 1
    print(f"'{s}' is a palindrome!")

main()