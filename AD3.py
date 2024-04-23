# Select the file name and the search term
file_name = input("Enter the file name")
search_text = input("Enter a search term")

# Check the file for the search term line by line
import os
import re

try:
    with open(file_name, "r") as f:
        for line in f:
            match = re.search(search_text, line)
            if match:
                print(f"The file name you entered is {file_name}")
                print(f"search text: {search_text}")
                print(f"The search text, {search_text}, was found")
                break
        else:
            print(f"The search text, {search_text}, not found")
except FileNotFoundError:
    print(f"Error: the file, {file_name}, not found")