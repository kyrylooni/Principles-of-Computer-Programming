# This program gets employee data from the user and 
# saves it as records in the employee.txt


def main():
  
    # 2) Get the number of employee records to create. 
    num_emps = int(input("How many employee records do you want to create? ")) 

    # 3) Open a file for writing via (with open(<file name>) as <file object>) structure which will automatically close and save the file at the end of execution.
    with open("employees.txt", "w") as emp_file:

    # 4) Get each employee's data and write it to the file. 
        for count in range(1, num_emps+1):
            # 5) Get the data for an employee
            print(f"Enter data for employee #{count}")
            name = input("Name: ")
            id_num = input("ID number: ")
            dept = input("Department: ")

            # 6) Write the data as a record to the file.
            emp_file.write(f"{name}\n")
            emp_file.write(f"{id_num}\n")
            emp_file.write(f"{dept}\n")

            # 7) Display a blank line.
            print()
        
        print("Employee records written to employees.txt. ")


# invoke main function as a standalone function  
if __name__ == "__main__":
    # 1) Invoke main
    main()