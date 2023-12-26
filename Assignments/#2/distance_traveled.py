def distance_traveled(time):
    '''
    The distance_traveled function takes one parameter (time) and returns
    total distance traveled if the speed is 70 mph. 
    '''

    #checks to see if the input value is an intager, assuming that time is a whole number.
    #if not intager, stop an execution. 
    try:
        time = int(time)
    except:
        print("INVALID INPUT")
        print("Plese provide an intager for the function invocation")
        exit()

    SPEED = 70

    #calculates total distance traveled
    total_distance = SPEED * time
    return total_distance


print("Total distance traveled in 6 hours:", distance_traveled(6), "miles")
print("Total distance traveled in 10 hours:", distance_traveled(10), "miles")
print("Total distance traveled in 15 hours:", distance_traveled(15), "miles")

