# Ask user for input and output file names
input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

# Read input file and remove duplicate lines
with open(input_file, 'r') as f:
    lines = f.readlines()
    unique_lines = list(set(lines))

# Write unique lines to output file
with open(output_file, 'w') as f:
    f.writelines(unique_lines)

print("Done! Unique lines saved to", output_file)
