"""
Exercise 3: The Cargo Train Scanner
Scenario: A train has wagons carrying different resources: ["coal", "iron", "gold", "coal", "timber", "coal"]. 
The train conductor wants to inspect the cargo. Write a program that prompts the user to enter a resource type (e.g., "coal" or "gold").

Print the total number of wagons carrying that resource (using .count()).
If the resource is on the train, print the index of the very first wagon carrying it (using .index()). 
If it is not found, print "Resource not found on train!".

Sample Input: "coal"
Sample Output:
Number of coal wagons: 3
First coal wagon is at index: 0
Sample Input: "oil"
Sample Output: "Resource not found on train!"
"""
def main():
    resources = ["coal", "iron", "gold", "coal", "timber", "coal"]
    n = input("Enter a Resource Type: ")
    if n in resources:
        print(f"Number of coal wagons: {resources.count(n)}",)
        print(f"Number of coal wagons: {resources.index(n)}",)
    else:
        print("Resource not found on train!")



print("="*110)
main()