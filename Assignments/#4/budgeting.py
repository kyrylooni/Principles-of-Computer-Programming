def budget_calculator():
    '''
    The budget_calculator function calculates the total spending based on the expenses and 
    salary and then decides wheter the user is under the budget or above the budget
    '''

    # if an salary input is anything different from float than produce an error message  
    try:
        salary = float(input(f"Enter your montly salary in dollars: "))
    except:
        print("INVALID INPUT")
        print("Please enter a numeric value")
        exit()

    total_spending = 0
    print("Input 0 for an expense prompt to finish an execution")

    # while you make some money, ask for the expeses you have
    while salary != 0:
        # if an expense input is anything different from float than produce an error message  
        try:
            expense = float(input("Enter your montly expense in dollars: "))
        except:
            print("INVALID INPUT")
            print("Please enter a numeric value")
            continue
            
        #if the next inputed expense is zero than you are done with execution 
        if expense == 0 :
            print("Done calculating.")
            break 
        # accumulation pattern; at the begining total_spending = 0
        # with each itteration (expense) add it to the total 
        total_spending = total_spending + expense

    # if you are making more than you spend, you are under the budget
    if salary >= total_spending:
        print("You are under the budget ;)") 
    # otherwise if you spend more than you make, you are over the budget 
    else:
        print("You are over the budget!")
    print(f"Your total spendings are: ${total_spending:.2f}")

# function invocation
budget_calculator()
