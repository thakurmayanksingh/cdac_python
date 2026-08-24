"""
Exercise 7: Star Padding Layout formatter
Write a program that center-aligns a user-supplied text string inside a fixed block of 30 asterisks (*).

Sample Input: "Python"
Sample Output: "************Python************"

"""

def main():
    inp = input("Sample Input: ")
    n = 30 - len(inp)
    m = n//2
    print('*'*m, inp, '*'*m)

main()