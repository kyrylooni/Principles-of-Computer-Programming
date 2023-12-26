def distance_traveled():

    '''
    the distance_traveled function computes total distance traveled by multiplying speed * time 
    '''

    #if speed and hours inputs are anything else than number produce an error message 
    try:
        speed = int(input("Enter the speed you traveled with: "))
        hours = int(input("Enter the number of hours you traveled: "))
    except:
        print("INVALID INPUT")
        print("Please input a numeric value.")
        exit()


    # tab hours from distance
    print("Hours\tDistance Traveled")
    print("-------------")


    # since counting starts from 0 the list produced is [0,1,2]
    # to match hours that starts with 1 (everything multiplied by 0 == 0), add +1 to the range function 
    # [0, 1, 2, 3]
    # range DOES NOT produce list itself, invoke list function in order to create a list object. 
    hrs = list(range(hours+1))

 
# for each hour in the list: [3, 2, 1, 0]
    for hour in hrs:
        # we do not multiply by 0, because there is no point, so we ommit it with a conditional 
        if hour > 0 and speed > 0:
            total_distance = speed * hour 
            print(f"{hour}\t{total_distance}")
    # since we invoke the function without passing any parameter, I decided to return the last distance value produced by function, even though we do not need to return anything in that case 
    # alternatively we can accumulate the result into a list of distances by invoking .append() method on a newly created list object, or return None 
    #return total_distance

distance_traveled()
