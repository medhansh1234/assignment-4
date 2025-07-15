#writing to file
file1 = open("output.txt", 'w')

text = input("Enter text to write to the file :")
file1.write(text+'\n')
print("Data succesfully written to output.txt")

file1.close()

#appending to file

file2 = open("output.txt", 'a')
append_text = input("Enter additional text to append:")
file2.write(append_text)
print("Data succesfully appended.")

file2.close()

# reading file

file3 = open("output.txt", 'r')

print("Final content of output.txt:")
reading_file = file3.read()
print(reading_file)

file3.close()

