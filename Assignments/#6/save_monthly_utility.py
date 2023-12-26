# This program gets mounthly exppenses data from the user and 
# saves it as records in the monthly_bill_details.txt

def main():
    # 2) ask for number of months 
    # 3) check to see if the user input is a float 
    # if yes, proceed further, if not return a value error 
    try:
        num_months = int(input("Enter a number of months you would like to save your data from: "))
    except ValueError as err:
        print(err)
        # Display error message
        print("Please enter a whole number")
        exit()

    # 4) Open a file for writing via (with open(<file name>) as <file object>) structure which will automatically close and save the file at the end of execution.
    with open("monthly_bill_details.txt", "w") as f_open:

        # 5) if passed value is possitive and not 0; 
        # 6) iterated over a counted loop in range number of months, adding 1 on each iteration 
        # else return error 
        if num_months > 0 and num_months != 0:
            for count in range(1, num_months+1):
                # 7) Display  message
                print(f"Enter data for a bill in month #{count}")

                # 8) ask for an amount on the bill
                # 9) check to see if the user input is a float
                # # if yes, proceed further, if not return a value error 
                try:
                    bill_info = float(input("Enter an ammount on the bill in dollars: "))
                except ValueError as err:
                    print(err)
                    # Display the error message 
                    print("Please enter an amount as a number")

                # 10) if the amount is greater than and not equal to 0 
                # 11) write the value to the file
                # else display error message 
                if bill_info > 0 and bill_info != 0:
                    f_open.write(f"{bill_info:.2f}\n")
                else:
                    print("Please enter a positive number")

                # 12) Print blank line
                print()
            # 13) Display the message after the last iteration has been completed and value has been saved
            print("Your monthly bill information has been saved in monthly_bill_details.txt")
        else:
            print("ERROR")
            print("Please provide a value greater than and not equal to 0")


# invoke main function as a standalone function  
if __name__ == "__main__":
    # 1) invoke main 
    main()