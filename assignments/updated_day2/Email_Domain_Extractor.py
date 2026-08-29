"""
Exercise 3: Email Domain Extractor
Write a program that prompts the user to enter an email address string. Extract the domain name (the part after the @) and print it. If the string is not a valid email (does not contain exactly one @), print "Invalid Email".

Sample Input: "vinod@vinod.co"
Sample Output: "vinod.co"
Sample Input: "vinod.co"
Sample Output: "Invalid Email"
"""

def main():
    inp = input("Sample Input: ")
    if inp.find("@") != -1:
        idx = inp.index("@")
        print(f"Sample Output: {inp[idx+1:]}")
    else:
        print("Invalid Email")

if __name__ == "__main__":
    main()