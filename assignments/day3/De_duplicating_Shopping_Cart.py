"""
Exercise 8: De-duplicating Shopping Cart

Scenario: An online shopping cart has duplicate items due to double-clicks: 
["apple", "banana", "apple", "orange", "banana", "banana"].
 Write a program that processes the list and removes all duplicate items, but keeps the first occurrence of each item in 
 its original order. Print the cleaned cart.

Hardcoded Input: cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
Sample Output: ['apple', 'banana', 'orange']
"""

def main():
    cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
    mp = {}
    i = 0
    while i<len(cart):
        item = cart[i]
        if item in mp:
            cart.pop(i)
            continue
        else:
            mp[item] = 1
        i += 1
    print(cart)

if __name__ == "__main__":
    main()