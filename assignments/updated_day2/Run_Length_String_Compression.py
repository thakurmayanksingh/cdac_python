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
    if not inp or len(inp)<2:
        print(f"Sample Output: {inp}")
        return

    comp_str = ""
    cnt = 1
    i, j = 0, 1

    while j<len(inp):
        if inp[i] == inp[j]:
            cnt += 1
            j += 1
        else:
            comp_str += inp[i] + str(cnt)
            i = j
            j += 1
            cnt = 1
        if j == len(inp):
            comp_str += inp[i] + str(cnt)

    if len(comp_str)<len(inp):
        print(f"Sample Output: {comp_str}")
        return

    print(f"Sample Output: {inp}")

if __name__ == "__main__":
    main()