'''
Exercise 2: Fibonacci Sequence Generator
Write a Python script to print the first 
N
 terms of the Fibonacci sequence, where 
N
 is provided by the user.

Fibonacci sequence: 
0, 1, 1, 2, 3, 5, 8, 13, 21,…
Sample Input: N = 6
Sample Output: 0, 1, 1, 2, 3, 5

'''

def main():
    N = int(input("N: "))
    a, b = 0, 1
    cnt = 0
    while cnt<N:
        print(a, end=" ")
        a, b = b, a+b
        cnt += 1

main()