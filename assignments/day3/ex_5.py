"""
Exercise 5: The Spy's Word Reverser
Scenario: A secret agent wants to send an encrypted message. 
The encryption rule is simple: reverse every word in the sentence, but keep the order of words unchanged.

Write a program that prompts the user for a sentence, splits it, 
uses a list comprehension to reverse the letters of each word, and joins them back together.

Sample Input: "Meet me at midnight"
Sample Output: "teeM em ta thgindim"
"""
def main():
    inp = input("Enter input: ")
    inp_list = inp.split()
    for i in range(len(inp_list)):
        ele = inp_list[i]
        inp_list[i] = ele[::-1]
    inp = " ".join(inp_list)
    print(inp)    


print("="*110)
main()