"""
Exercise 5: Custom Title Case Formatter
Write a program that accepts a string input from the user and outputs it in Title Case (capitalizing the first letter of each word and lowercasing the remaining letters). Do not use Python's built-in .title() method.

Sample Input: "WELCOME TO BANGALORE CITY"
Sample Output: "Welcome To Bangalore City"
"""

def main():
    inp = input("Sample Input: ")
    new_list = inp.split()
    for idx in range(len(new_list)):
        new_list[idx] = new_list[idx].lower()
        new_list[idx] = new_list[idx][0].upper() + new_list[idx][1:]
    print(f"Sample Output: {' '.join(new_list)}")

if __name__ == "__main__":
    main()