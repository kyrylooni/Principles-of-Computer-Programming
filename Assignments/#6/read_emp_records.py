# This program displays the records that are
# in the employees.txt file.

def main():
    
    # 2) Open a file for reading via (with open(<file name>) as <file object>) structure which will automatically close and save the file at the end of execution.
    with open("employees.txt", 'r') as emp_file:

        # 3) Read the first line from the file, which is 
        # the name field of the first record
        name = emp_file.readline()
        
        # 4) If a field was read, continue processing 
        while name != "":
            # 5) Read the ID number field.
            id_num = emp_file.readline()

            # 6) Read the department field
            dept = emp_file.readline()

            # 7) Strip the newlines from fields.
            name = name.rstrip('\n')
            id_num = id_num.rstrip('\n')
            dept = dept.rstrip('\n')

            # 8) Display the record
            print(f"Name: {name}")
            print(f"ID: {id_num}")
            print(f"Dept: {dept}")
            print()

            # 9) Read the name field of the next record.
            name = emp_file.readline()
        
# invoke main function as a standalone function  
if __name__ == "__main__":
    # 1) invoke main 
    main()