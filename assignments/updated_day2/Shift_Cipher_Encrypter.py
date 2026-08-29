"""
Exercise 6: Shift Cipher Encrypter
Write a program that prompts the user for a text string and a shift integer, 
and encrypts the text using a Caesar cipher. It should shift each alphabetical character in the
 string by the specified shift number down the alphabet. Maintain uppercase and lowercase characters, 
 and leave spaces or punctuation marks completely unchanged.

Sample Input: (User inputs string "Vinod" and shift 3)
Sample Output: "Ylqrg"
"""

def main():
    inp = input("Sample Input: ")
    shift = int(input("Shift: "))
    ans_str = ''
    for char in inp:
        if char.isalpha():
            asc = ord(char)
            shifted = asc+shift
            if char.islower():
                if shifted > 122:
                    dif = abs(shifted-122)
                    ans_shift = dif%26
                    ans_str = ans_str+chr(ord('a') + ans_shift-1)
                else:
                    ans_str = ans_str + chr(shifted)
            if char.isupper():
                if shifted > 90:
                    dif = abs(shifted-90)
                    ans_shift = dif%26
                    ans_str = ans_str+chr(ord('A') + ans_shift-1)
                else:
                    ans_str = ans_str + chr(shifted)
        else:
            ans_str += char

    print(ans_str)


if __name__ == "__main__":
    main()