'''
Exercise 3: Prime Number Checker
Write a program that checks whether a positive integer entered by the user is a prime number.

Logic: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
Sample Input: 17
Sample Output: 17 is a prime number.

'''

def main():
    num = int(input("Enter Number: "))
    if num != 1:
        cnt = 0
        for i in range(2, num//2+1): # for i in range(2, int(num**0.5))
            if (num%i == 0):
                cnt += 1
                break
        if cnt != 0:
            print("Not Prime!")
        else:
            print("Prime!")
    else:
        print("1 is neither prime nor composite, it is a natural number.")

main()