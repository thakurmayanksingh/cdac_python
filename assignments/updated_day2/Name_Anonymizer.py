"""
Exercise 8: Name Anonymizer
Write a program that prompts the user to enter a full name (first name, middle name, last name) and anonymizes it. 
The output should print the initials of the first and middle names followed by the full last name. 
If the name consists of only a single word, print it as-is.

Sample Input: "Vinod Kumar Kayartaya"
Sample Output: "V. K. Kayartaya"
Sample Input: "Bangalore"
Sample Output: "Bangalore"
"""

def main():
    inp = input("Sample Input: ")
    if len(inp) == 1:
        print(inp)
    inp_list = inp.split()
    for i in range(2):
        if i<len(inp_list)-1:
            inp_list[i] = inp_list[i][0].upper() + '.'
    print(" ".join(inp_list))


if __name__ == "__main__":
    main()