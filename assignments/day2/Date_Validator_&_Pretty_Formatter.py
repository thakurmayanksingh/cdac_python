"""
Exercise 12: Date Validator & Pretty Formatter
Write a program that prompts the user to enter a date string in the format "DD/MM/YYYY".

Warning

Do not use any built-in date/time library functions (such as the datetime or time modules) to format or validate the dates.
 You must parse and split the string manually, and use a custom tuple of month names for the pretty output if needed.

Your program must:

Verify if the date is valid. To be valid:
The month must be between 1 and 12 inclusive.
The day must be valid for that specific month 
(e.g., April, June, September, November have 30 days; others have 31 days).
For February, the day must be at most 29 in a leap year 
(divisible by 4, except for centuries not divisible by 400) and at most 28 in standard years.
If the date is valid, use a tuple of month names 
("January", "February", ...) to format and print the date in a long-form readable layout: "MonthName DD, YYYY".
If the date is invalid, print "Invalid Date".
Sample Input: "26/08/2026"
Sample Output: "August 26, 2026"
Sample Input: "29/02/2026" (2026 is not a leap year)
Sample Output: "Invalid Date"
Sample Input: "31/04/2026" (April only has 30 days)
Sample Output: "Invalid Date"
"""


def main():
    m = (input("Enter the Date in (DD/MM/YYYY) format: "))
    out = list(map(int, m.split("/")))
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    x = ""
    date, mon, year = out
    mo = month[mon - 1]
    if year < 1:
        print("Invalid value for Year")
        return
    
    if mon < 1 or mon > 12:
        print("Invalid value for Month")
        return

    if date < 1 or date > 31:
        print("Invalid value for Date")

    if mon == 2: 
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            if date > 29:
                print("Invalid Date")
                print(f"{m} ({year} is a leap year but {mon} will have maximum of 29 days)")
                return
        else:
            if date > 28:
                print("Invalid Date")
                print(f"{m} ({year} is not a leap year)")
                return
    elif mon in (4, 6, 9, 11):
        if date > 30:
            print("Invalid Date")
            print(f"{m} ({mon} will have maximum of 30 days)")
            return
    else:
        if date > 31:
            print("Invalid Date")
            print(f"{m} ({mon} will have maximum of 30 days)")
            return 

    x += mo + " " + str(date) + ", " + str(year)
    print(x)


if __name__ == "__main__":
    main()