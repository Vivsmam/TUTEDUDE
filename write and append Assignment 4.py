# Step 1: Write user input to output.txt
write_data = input("Enter data to write to the file: ")

with open("output.txt", "w") as file:
    file.write(write_data + "\n")

# Step 2: Append additional data to the file
append_data = input("Enter additional data to append to the file: ")

with open("output.txt", "a") as file:
    file.write(append_data + "\n")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
try:
    with open("output.txt", "r") as file:
        for index, line in enumerate(file, start=1):
            print(f"Line {index}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")
