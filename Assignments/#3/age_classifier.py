def age_classifier(age):
    '''
    The age_classifier function takes one parameter (person's age) 
    and determines whether the person is an infant, a child, 
    a teenager, or an adult.
    '''

    # checks whether an input is an integer, if not return an errror and ends execution 
    try:
        age = int(age)
    except:
        print("INVALID INPUT")
        print("Please enter you age as an integer")
        exit()


    if age < 0:      # impossible, so returns an error 
        print("At this moment of human evolution, you cannot exist before you were born.") 
        print("Please input a positive integer.")

    if age <= 1:                     # he/she is an infant 
        return "You are an infant"

    elif age > 1 and age < 13:       # he/she is a child
        return "You are a child"
                                    
    elif age >= 13 and age < 20:    # he/she is a teenager 
        return "You are a teenager"
                                    
    else:
        return "You are an adult"   # he/she is an adult 
    
     

age_input = input("Please enter your age: ")
age_class = age_classifier(age_input)
print(age_class)