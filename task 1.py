try :
    file_name = "sample.txt"
    file1 = open(file_name, 'r')

    read_file = file1.readlines()
    print("Reading file content :")

    first_line = read_file[0]
    second_line = read_file[1]


    print("Line 1 :", first_line)
    print("Line 2 :", second_line)


    file1.close()

except FileNotFoundError:
    print("Error: The file" , file_name,  "was not found. ")
