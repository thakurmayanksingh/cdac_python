"""
Exercise 6: Grading on a Curve
Scenario: A professor wants to adjust exam grades. Prompt the user to enter a list of space-separated test scores. Convert them to a list of integers. Using a single list comprehension with conditionals, apply the following curve rules:

If a score is below 50, add 10 points.
If a score is 50 or higher, add 5 points.
The maximum possible score is capped at 100 (e.g., a score of 98 becomes 100, not 103). Print the original and the curved grades.
Sample Input: "45 88 30 98 50"
Sample Output:
Original: [45, 88, 30, 98, 50]
Curved: [55, 93, 40, 100, 55]
"""

def main():
    inp = input("Sample Input: ")
    inp_list = inp.split()
    inp_list = [int(a) for a in inp_list.copy()]
    ans_list = [(x+10 if x<50 else x+5 if x+5<=100 else 100) for x in inp_list]
    print(ans_list)


if __name__ == "__main__":
    main()