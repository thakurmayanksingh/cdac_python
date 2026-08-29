"""
Exercise 10: Run-Length String Compression
Write a program that prompts the user to enter a text string and compresses it using run-length encoding (listing character counts next to each repeated character). If the compressed string is not smaller in size than the original string, print the original string.

Sample Input: "aabcccccaaa"
Sample Output: "a2b1c5a3"
Sample Input: "abcd"
Sample Output: "abcd" (since "a1b1c1d1" is longer than "abcd")

"""

def main():
    inp = input("Sample Input: ")
    mp = {}
    for char in inp:
        if char in mp:
            mp[char] += 1
        else:
            mp[char] = 1
    comp_str = ""
    for item in mp:
        comp_str = comp_str + item + str(mp[item])
    print(comp_str)

if __name__ == "__main__":
    main()