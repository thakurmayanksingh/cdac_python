"""
Exercise 11: Group Anagrams
Write a program that starts with a list of strings defined at the top of your script (e.g., words = ["eat", "tea", "tan", "ate", "nat", "bat"]) and groups the anagrams (words formed by rearranging letters) together. Print the final grouped list of lists.

Hardcoded Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Sample Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

"""

def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans = []

    for word in words:
        is_found = False
        for group in ans:
            if sorted(word) == sorted(group[0]):
                group.append(word)
                is_found = True
                break
        if is_found == False:
            ans.append([word])
    
    print(ans)


if __name__ == "__main__":  main()