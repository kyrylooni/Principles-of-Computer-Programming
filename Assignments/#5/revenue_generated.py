# The author of this project is aware of other possible ways to create the following program.
# However, in this case, he chose to use dictionary mechanics, since it is an efficient way to access key/value pairs though value lookups based on keys
# which will satisfy the requirements of this program more than enough.

# The author is always open to further recomendations/councerns in regards to his programs :)


# 1) set up constant choices as global variables for reusibility purposes
TIER_1_CHOICE = 1
TIER_2_CHOICE = 2
TIER_3_CHOICE = 3 
BOX_OFFICE_CHOICE = 4
QUIT_CHOICE = 5


# 2) create a dictionary that contains tiers as keys and their number choices as values 

# set it up as a global variable in case of value lookup request for multiple functions

tiers = {"Tier 1":TIER_1_CHOICE, "Tier 2":TIER_2_CHOICE, "Tier 3":TIER_3_CHOICE, "Box Office Tier": BOX_OFFICE_CHOICE}

# 3) create a list of dictionary keys in order to use it for value lookup  
t_keys = list(tiers.keys()) 

# 4) check to see in case a name input is a number; 
# Also global variable since will be used both for intro and outro
try:
    name = input(str("Please enter your name: "))
except:
    print("INVALID INPUT")
    print("Please enter a string")
    exit()

# main function serves as a base for function invocation of each other function in the program 
def main():
    # 6) set up a control variable in for a number choice
    choice = 0
   
    # 7) Invoke intro function 
    # jump to the intro function
    intro()

    # 9) while the number is not 5, do not exit the problem; continue 
    while choice != QUIT_CHOICE:
        # 10) invoke menu function
        # jump to the menu function 
        menu()

        # 12) if choice is not a number, output an error and ask again 
        try:
            choice = int(input("Enter a tier you are interested in or quit the program: "))
        except:
            print("Please input a number to make a choice from one of the options below")
            continue

        # 13) if choice is 1 elif 2 elif 3 elif 4 elif 0 else invalid input 
        if choice == TIER_1_CHOICE:
            # invoke get_tiers_sales function 
            # jump to get_tiers_sales function
            get_tiers_sales(TIER_1_CHOICE)
        elif choice == TIER_2_CHOICE:
             # invoke get_tiers_sales function 
             # jump to get_tiers_sales function
            get_tiers_sales(TIER_2_CHOICE)
        elif choice == TIER_3_CHOICE:
             # invoke get_tiers_sales function 
             # jump to get_tiers_sales function
            get_tiers_sales(TIER_3_CHOICE)
             # invoke get_tiers_sales function 
             # jump to get_tiers_sales function
        elif choice == BOX_OFFICE_CHOICE:
             # invoke get_tiers_sales function 
             # jump to get_tiers_sales function
            get_tiers_sales(BOX_OFFICE_CHOICE)
        elif choice == QUIT_CHOICE:
            print("We are done here.")
            print("Exiting the program....")
        else:
            print("Please enter value (1-5)")
    
    # 30) invoke goodbye
    goodbye()
    # end of the program.

        
def intro():
    '''
    intro function welcomes the user with previously inputted name
    '''

    # 8) print a welcome message including a name input from the user
    
    print(f"Welcome {name} to Disney University basketball games revenue calculator!")
     # back to the main function

 
def menu():
    '''
    menu function prints out different tieir choices to navigate or quit the problem if user would like to do so
    '''
    # 11) print menu choices
    print("    MAIN MENU")
    print("1) TIER 1 SALES")
    print("2) TIER 2 SALES")
    print("3) TIER 3 SALES")
    print("4) BOX OFFICE SALES")
    print("5) QUIT")
    # back to the main function 

def get_tiers_sales(tier_input):
    '''
    get_tiers_function takes on parameter (tier_input) as a number choice for a specific tier and conducts a value lookup from tier prices dictionary based on provided key
    if the number is a key in tiers_prices it saves a price associated with that key into a variable and then calculates a total income based on a number of tickets sold
    '''
    
    # 14) create a tier prices dictionary with tier choices as keys and prices as valuues
    tiers_prices = {TIER_1_CHOICE:50, TIER_2_CHOICE:30, TIER_3_CHOICE:10, BOX_OFFICE_CHOICE:200}
    # 15) create a list of tiers_price keys
    prices_keys = list(tiers_prices.keys())

    # 16) create a dictionary of seats availabler per each teir with tier choices as keys and seats available as values 
    seats_available_per_tier = {TIER_1_CHOICE:200, TIER_2_CHOICE:400, TIER_3_CHOICE:600, BOX_OFFICE_CHOICE:50}

    # 17) check to see if a passed tier value is in keys
    if tier_input in prices_keys:
        
        # 18) look up each specific value that is associated with a key in t_keys dictionary
        # conducting this lookup in order display each tier for an passed number respectively 
        # since passed value starts with 1, and list itteration starts with 0 (-1) from passed value in order to match a value of the key in the t_keys dictionary  
        tier = t_keys[tier_input-1]
        
        # 19) look up number of seats associated with requested tier
        num_seat = seats_available_per_tier[tier_input]
        
        # 20) look up price for a requested tier 
        price = tiers_prices[tier_input]

        # 21)  assign tickets sold variable to None type 
        # None type serves as a placeholder and does not carry any type of the value 
        # until gets assign to an intager later 
        tickets_sold = None

        # 22) while tickets sold is None type.  
        while tickets_sold is None:
            # 23) check to see if tickets_sold input is valid integer 
            # if not print an error message and prompt again  
            # if yes, proceed further  
            try:
                # here we assign tickets_sold to an intager if passed value is itself an intager, so it is not None anymore 
                tickets_sold = int(input(f"How many tickets were sold for {tier} ({num_seat} seats available): "))
            except:
            # 24) print error message 
            # here it means that inputed value is not an iteger, therefore still None type; thus, repeat an itteration. 
                print("INVALID INPUT")
                print("Please enter a whole number")
               
        # 25) if the number of tickets sold is greater than and is not 0, and the number of tickets sold is less then or equal to the number of seats for a tier 
        # 26) accumulate total_income from sale by price * tickets sold for a requested tier 
        if tickets_sold > 0 and tickets_sold != 0 and tickets_sold <= num_seat:
            total_income = price * tickets_sold     
            # 27) print total income based on tier requested               
            print(f"For {tier} total income is: ${total_income:,}")
            # 28) if the number of tickets sold is greater than number of seats per tier 
            # print value limit error
        elif tickets_sold > num_seat:
            print("ERROR")
            print(f"You have reached the limit of {num_seat} seats for this tier!")
            # 29) else the user have inputed the negative number 
            # print a negative number error
        else:
            print("ERROR")
            print("Please input non-negative number or not 0")
        # back to main 
        
            
def goodbye():
   '''
    goodbye function produce a closing messssage at the end of the program execution.
   '''

  # 31) print goodbye message
   print(f"Thank you {name} for being our customer")
   print("Goodbye!")

# 5) invoke main function 
main()