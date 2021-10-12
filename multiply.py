from os import error

def multiply_list(input_list):

	'''The multiple_list take inpt_list as a parameter
	   this function will multiple all of the elements in the list
        '''Using try except to catch any errors and return False
   
    try:
        output = 1
        for number in input_list:
            output = output * number
        return output
    except error:
        return False
