def main():
    # 3) invoke get_property_tax function 
    # 4) jump to get_property_tax function 
    get_property_tax()


def get_assesment_value():
    '''
    get_asssesment_value function calculates property assesment value based on 
    current county tax and property_value provided by the user
    '''
    # 8) set up a constant 
    COUNTY_TAX_RATE = 0.06

    # 9) prompt the user for input
    # 10) check to see if input is valid 
    # if it is proceed further
    # if not, display an error mesage and exit the program 
    try:
        property_value = float(input(f"Enter your property value in dollars: "))
    except:
        print("INVALID INPUT")
        print("Please provide a numeric value")
        exit()
    # 11) if number of fat grams is a positive number and it is not zero 
    if property_value > 0 and property_value != 0:
        # 12) calculate assesment value of the property by multiplying property_value and county tax rate. 
        assesment_value = property_value * COUNTY_TAX_RATE
        # 13) return a resulted value to a function invocation 
        return assesment_value
    else:
         # 14) if previous conditions are false; print error 
        print("Enter a non-zero or positive number")
        exit()
        # 15) back to get_property_tax function 

def get_property_tax():
    '''
    get_property_tax function calculates total property tax based on current property tax and 
    property assesment value 
    '''
    # 5) set up constant for property in cents
    # will use this value later for calculating property tax for each $100
    PROPERTY_TAX_IN_CENTS = 0.82
    
    # 6) invoke get_assesment_value and return the resulted value back to assesment_value variable
    # 7) jump to get_assesment_value function 
    assesment_value = get_assesment_value()
    # 16) calculate tax for property by multiplying assesment value and property tax in cents devided 100
    # because the property tax is then 82 cents for each $100 of the assessment value.
    tax_for_peoperty = assesment_value  * (PROPERTY_TAX_IN_CENTS/100)
    # 17) calculate total property tax by adding assessment value and specific tax for propery 
    total_propery_tax = assesment_value + tax_for_peoperty
    # 18) display the resulted value in dollars 
    print(f"Your total property tax is: ${total_propery_tax:,}")
    # 19) back to main function 

# 1) invoke main 
# 2) jump to main function 
main()  
# end of the program 




