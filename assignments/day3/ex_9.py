"""
Exercise 9: The Josephus Elimination Game

Scenario: A group of N soldiers (numbered 1 to N) stand in a circle. Starting from the first soldier, every K-th soldier is 
eliminated from the circle. The count continues with the next remaining soldier, moving clockwise. 
This process repeats until only one soldier remains. Write a program that prompts the user to enter N (number of soldiers) and 
K (elimination interval). Simulate the game using a list and print the order of eliminations and the final survivor.

Sample Input: N = 5, K = 2

Sample Output:

Soldier circle initialized: [1, 2, 3, 4, 5]
Eliminated soldier: 2 (Remaining: [1, 3, 4, 5])
Eliminated soldier: 4 (Remaining: [1, 3, 5])
Eliminated soldier: 1 (Remaining: [3, 5])
Eliminated soldier: 5 (Remaining: [3])
The sole survivor is: 3

"""

def  main():
    n = int(input("N = "))
    k = int(input("K = "))
    soldiers = [x for x in range(1, n+1)]
    cnt = 1
    i = 0
    while len(soldiers)>1:
        if cnt == k:
            soldiers.pop(i)
            cnt = 1
        else:
            cnt += 1
            i += 1
            if i>len(soldiers)-1:
                i = i%len(soldiers)
    print(f"The sole survivor is: {soldiers[0]}")


if __name__ == "__main__":
    main()