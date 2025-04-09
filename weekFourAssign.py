# File Read & Write Challenge: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

try:
    inputFileName1 = input("Enter the name of the first input file:\n(If your file is in another directory, enter the full path, e.g.: C:\\Users\\user\\Documents\\input.txt)\n")
    with open(inputFileName1, "r") as inputFile1:
        content1 = inputFile1.read()

    inputFileName2 = input("Enter the name of the second input file:\n")
    with open(inputFileName2, "r") as inputFile2:
        content2 = inputFile2.read()

    mergedContent = content1 + "\n" + content2
    with open("outputFile.txt", "w") as outputFile:
        outputFile.write(mergedContent)

    print("The contents of the two input files have been merged into outputFile.txt.")

except FileNotFoundError:
    print("File not found. Please check the filename or path and try again.")

except Exception as e:
    print(f"An error occurred: {e}")
