def roman_numerals(number):
    
    try:
        number = int(number)
    except:
        print("INVALID INPUT")
        print("Please enter an intager")
        exit()

    roman_nums = { 1 : "I", 2 : "II", 3 : "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8:"VIII", 9: "IX", 10: "X" }
    
    for key, value, in roman_nums.items():
        if key == number:
            #print("----KEY:", key, "NUMBER:", number, "----")
            return value   
    return "INPUT IS OUT OF RANGE"
  

number_inpt = input("Enter a number (in range from 1 to 10): ")
numbs = roman_numerals(number_inpt)
print(numbs)