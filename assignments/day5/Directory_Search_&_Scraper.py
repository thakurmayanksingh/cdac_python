"""
Assignment 3: Corporate Directory Search & Scraper
Scenario
You are writing a parser to extract formatted employee phone records from unstructured text files.
Employee phone numbers are formatted in multiple ways across the directory.

Problem Description
Write a function scrape_directory_phones(directory_text) that extracts phone records from text and 
returns a structured list of dictionaries.

The function must detect phone numbers matching any of the following three formats:
AAA-PPP-LLLL (e.g., 123-456-7890)
(AAA) PPP-LLLL (e.g., (123) 456-7890)
AAAPPPLLLL (10 consecutive digits, e.g., 1234567890) where AAA represents the area code (3 digits), 
PPP represents the prefix (3 digits), and LLLL represents the line number (4 digits).
Design a single compiled RegEx pattern to parse all three formats using capture groups.
For each match found in directory_text, build a dictionary with the following keys:
"area_code": String containing the extracted 3 area code digits.
"prefix": String containing the extracted 3 prefix digits.
"line_number": String containing the extracted 4 line number digits.
"formatted": A normalized phone string in the format "(AAA) PPP-LLLL".
Return a list of these dictionaries. If no phone numbers are found, return an empty list.
"""
import re

def scrape_directory_phones(directory_text):
    pattern = re.compile(r'(?:\((\d{3})\)\s|(\d{3})-|(\d{3}))(\d{3})-?(\d{4})')
    out = []
    for i in re.finditer(pattern, directory_text):
        mp = {}
        x = i.groups()
        print(x)
        area = [int(i) for i in x[:3] if i is not None]
        area = area[0]
        prefix = x[3]
        line_num = x[4]

        mp["Area"] = area
        mp["Prefix"] = prefix
        mp["line_number"] = line_num
        mp["formatted"] = f"({area}) {prefix}-{line_num}"
        out.append(mp)
    print(out)


def main():
    directory = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."
    scrape_directory_phones(directory)
    

if __name__ == ("__main__"):
    main()   