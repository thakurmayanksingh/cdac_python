"""
Exercise 8: Score to Grade Converter
Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F
"""

def main():
    score = int(input("Enter Score(0 - 100): "))
    if score>=90 and score <=100:
        print("A")
    elif score>=80 and score <=89:
        print("B")
    elif score>=70 and score <=79:
        print("C")
    elif score>=60 and score <=69:
        print("D")
    elif score<60:
        print("F")
    else:
        print("Not a Valid Input.. Enter Value between 0 to 100 only.")  

main()