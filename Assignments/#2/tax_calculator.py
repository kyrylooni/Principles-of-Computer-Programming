def calculate_tax(price):
    '''
    The calculate_tax function taskes one parameter (price) as a float 
    and returns total sale amount in dollars.
    '''

#checks to see if the input is a float, if not return an error messages and stops execution
    try:
        price_float = float(price)
    except:
        print("INVALID INPUT")
        print("Please enter a numeric value")
        exit()

    # (2 decimal places)
    print(f"The amount of purchase: ${price_float:.2f}")
    
    STATE_SALES_TAX_RATE = 0.05
    COUNTY_SALES_TAX_RATE = 0.025
    
    #computes the state sales tax (2 decimal places)
    state_sales_tax = price_float * STATE_SALES_TAX_RATE
    print(f"State sales tax: ${state_sales_tax:.2f}")

    #computes the county tax (2 decimal places)
    county_sales_tax = price_float * COUNTY_SALES_TAX_RATE
    print(f"County sales tax: ${county_sales_tax:.2f}")

    #computes the total sales tax (2 decimal places)
    total_sales_tax = state_sales_tax + county_sales_tax
    print(f"Total sales tax: ${total_sales_tax:.2f} ")

    print("------------------------------------------")

    #total sales amount (2 decimal places)
    total_sale_amount = price_float + total_sales_tax
    return f"{total_sale_amount:.2f}"



price_inpt = input("Enter the amount of a purchase in dollars: ")
print('The total amount of the sale: $' + calculate_tax(price_inpt))
