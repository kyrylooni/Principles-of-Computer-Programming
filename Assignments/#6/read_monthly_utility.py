# This program displays the records that are
# in the monthly_bill_details.txt file.

def main():

    # 2) Open a file for reading via (with open(<file name>) as <file object>) structure which will automatically close and save the file at the end of execution.
    with open("monthly_bill_details.txt", "r") as f_open:

        # 3) readlines() method reads all of the lines and creates a list of values from each line 
        values = f_open.readlines()

        # 4) set up month counter 
        month = 1
        # 5) for each value number in a loop
        for value in values:
            # 6) strip the newline character 
            value = value.rstrip("\n")
            # 7) Display result
            print(f"For month #{month} your bill is ${value}")
            # 8) increment 1 mounth for each iteration 
            month += 1

# invoke main function as a standalone function  
if __name__ == "__main__":
    # 1) invoke main 
    main()