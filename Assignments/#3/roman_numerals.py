def roman_numerals(number):
    '''
    The roman_numerals function takes one parameter (number) within 
    a range from 0 to 10 and returns Roman numeral version of that number.
    '''
    # checks whether an input is an integer, if not return an errror and ends execution 
    try:
        number = int(number)
    except:
        print("INVALID INPUT")
        print("Please enter an intager")
        exit()

    if number == 1:
        return "I" 
    elif number == 2:
        return "II"
    elif number == 3:
        return "III"
    elif number == 4:
        return "IV"
    elif number == 5:
        return "V"
    elif number == 6:
        return "VI"
    elif number == 7:
        return "VII"
    elif number == 8:
        return "VIII"
    elif number == 9:
        return "IX"
    elif number == 10:
        return "X"
    else:
        return "INVALID INPUT"


number_inpt = input("Enter a number (in range from 1 to 10): ")
rom_nums = roman_numerals(number_inpt)
print(rom_nums)