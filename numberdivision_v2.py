def divide(num1,num2):
    # Verify input 1 is in numeric form
    if type(num1) != int and float:
        # Input is not numeric, return error to user
        return 'Error - Input1 is not a number'
    
    # Verify input 2 is in numeric form
    elif type(num2) != int and float:
        # Input is not numeric, return error to user
        return 'Error - Input2 is not a number'
        
    # Check if the denominator number is greater than 0
    if (num2 == 0):
        # Denominator is 0, return error to user
        return 'Error - You cannot divide by 0. Please choose an appropriate denominator'
    
    # Perform the devision
    divide_res = num1/num2;
    
    # Return completed equasion to user 
    return "{0}/{1} = {2}".format(num1,num2,divide_res)