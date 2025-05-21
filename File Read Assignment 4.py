# Program to read and print all lines from sample.txt with line numbers

try:
    with open("sample.txt", "r") as file:
        for index, line in enumerate(file, start=1):
            print(f"Line {index}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
