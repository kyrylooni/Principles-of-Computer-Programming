def main():
    # 2) invoke get_fat_calories function
    # jump to get_fat_calories function  
    get_fat_calories()
    # 9) invoke get_carbohydrate_calories function 
    # jump to the get_carbohydrate_calories function
    get_carbohydrate_calories()

def get_fat_calories():
    '''
    get_fat_calories function calculates the number of fat calories person consumes per day 
    '''

    # 3) ask user for input of fat grams 
    # 4) check to see if the input is valid 
    # if it is proceed further
    # if not, display an error mesage and exit the program 
    try:
        fat_grams = float(input("Enter a number of fat grams: "))
    except:
        print("INVALID INPUT")
        print("Please provide a numeric value")
        exit()

    # 5) if number of fat grams is a positive number and it is not zero 
    if fat_grams > 0 and fat_grams != 0:
        # 6) multiply fat calories by 9 (according to the formula)
        fat_calories = fat_grams * 9
        # 7) print result 
        print(f"You consume {int(fat_calories)} fat calories in a day")
    else:
        # 8) if previous conditions are false; print error 
        print("Enter a non-zero or positive number")
        # back to main function 
        

def get_carbohydrate_calories():
    '''
    get_carbohydrate_calories function calculates the number of carbohydrate calories person consumes per day 
    '''
    # 9) ask user for a number of carb grams 
    # 10) check to see if input is valid 
    # if it is proceed further
    # if not, display an error mesage and exit the program 
    try:
        carb_grams = float(input("Enter a number of carbohydrate grams: "))
    except:
        print("INVALID INPUT")
        print("Please provide a numeric value")
        exit()
    
    # 11) if number of carb grams is a positive number and it is not zero 
    if carb_grams > 0 and carb_grams != 0:
        # 12) multiply carb grams by 4 (according to the formula)
        carb_calories = carb_grams * 4
        # 13) print result 
        print(f"You consume {int(carb_calories)} carb calories in a day")
    else:
        # 14) if previous conditions are false; print error 
        print("Enter a non-zero or positive number")
        # back to main function 
       
# 1) invoke main function 
# jump to main function
main()
# end of the program 