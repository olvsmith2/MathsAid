#Validation for integer limit inputs. Use "%S", "%d","%P" and int as perameters
def Int_validate(inp, action, string, Max_length):
    Max_length = int(Max_length)
    #Checks input number is less than the given amout of digits digits
    if len(string) > Max_length and string[0] != "-":
        return False
    elif len(string) > Max_length + 1:
        return False
    #Lets them enter negative numbers
    if len(string) == 1 and inp == "-":
        return True
    #Checks if the action is to delete characters
    if action == "0":
        return True
    #Checks for null input
    if inp == "":
        return True
    #Checks if the input is a digit    
    if inp.isdigit():
        return True
    #Returns invalid input of the input doesnt meet the above criteria
    else:
        return False

#Validation for a decimal input + pi input. Use "%S", "%d","%P" and int as perameters
def Decimal_validate_with_pi(inp, action, string, Max_length):
    Max_length = int(Max_length)
    #Sets the number as no a decimal 
    Decimal = False
    #Checks the input for a decimal
    for i in string:
        if i == ".":
            Decimal = True
    #Checks input number of digits is less than the given amout of digits
    #Check is there is no decimal point or - sign
    if len(string) > Max_length and string[0] != "-" and Decimal == False:
        return False
    #Check is there is a decimal point but no - sign
    elif len(string) > Max_length + 1 and Decimal == True and string[0] != "-" :
        return False
    #Check is there is no decimal point but is a - sign
    elif len(string) > Max_length + 1 and Decimal == False and string[0] == "-" :
        return False
    #Check is there is a decimal point and a - sign
    elif len(string) > Max_length + 2 and Decimal == False and string[0] == "-" :
        return False

    #Lets them enter negative numbers
    if len(string) == 1 and inp == "-":
        return True
    #Checks if the action is to delete characters
    if action == "0":
        return True
    #Checks for null input
    if inp == "":
        return True
    #Checks if the input is a digit    
    if inp.isdigit():
        return True
    #Checks for the input pi
    if inp == "p" or inp == "i":
        return True
    #Checks if the input is a decimal point    
    if inp == ".":
        return True
    #Returns invalid input of the input doesnt meet the above criteria
    else:
        return False

#Validation for a decimal input. Use "%S", "%d","%P" and int as perameters
def Decimal_validate(inp, action, string, Max_length):
    Max_length = int(Max_length)
    #Sets the number as no a decimal 
    Decimal = False
    #Checks the input for a decimal
    for i in string:
        if i == ".":
            Decimal = True
    #Checks input number of digits is less than the given amout of digits
    #Check is there is no decimal point or - sign
    if len(string) > Max_length and string[0] != "-" and Decimal == False:
        return False
    #Check is there is a decimal point but no - sign
    elif len(string) > Max_length + 1 and Decimal == True and string[0] != "-" :
        return False
    #Check is there is no decimal point but is a - sign
    elif len(string) > Max_length + 1 and Decimal == False and string[0] == "-" :
        return False
    #Check is there is a decimal point and a - sign
    elif len(string) > Max_length + 2 and Decimal == False and string[0] == "-" :
        return False

    #Lets them enter negative numbers
    if len(string) == 1 and inp == "-":
        return True
    #Checks if the action is to delete characters
    if action == "0":
        return True
    #Checks for null input
    if inp == "":
        return True
    #Checks if the input is a digit    
    if inp.isdigit():
        return True
    #Checks if the input is a decimal point    
    if inp == ".":
        return True
    #Returns invalid input of the input doesnt meet the above criteria
    else:
        return False

#Validation function for entery box. Use "%S", "%d" and list as perameters
def Function_validate(inp, action, Valid_characters):
    #Checks if the action is to delete characters
    if action == "0":
        return True
    #Checks for null input
    if inp == "":
        return True        
    #Checks if the input is a digit    
    if inp.isdigit():
        return True
    #Checks if the input is in the list of valid characters
    elif inp in Valid_characters:
        return True
    #Returns invalid input of the input doesnt meet the above criteria
    else:
        return False

#Edits the input string to a format which SymPy can turn into a function
def Python_formular_formator(string):
    if len(string) > 1:     
        #Creates an empty string to store the formatted string
        updated_string = ""
        #For loop that goes through each index of the string
        for index in range(1, len(string)):
            #Makes a variable to hold the current character for the loop
            character = string[index]
            #Makes a variable to hold the previous character for the loop
            previous_character = string[index - 1]
            #Adds the previous character to the updated string
            updated_string = updated_string + previous_character

            #Adds a multiply sign between two sets of brackets
            if character == "(" and previous_character == ")":
                updated_string = updated_string + "*"

            #Adds a multiply sign between trig functions and x's
            if character == "s" and previous_character == "x":
                updated_string = updated_string + "*"
            if character == "c" and previous_character == "x":
                updated_string = updated_string + "*"
            if character == "t" and previous_character == "x":
                updated_string = updated_string + "*"

            #Adds a multiply sign between trig functions and numbers
            if character == "s" and previous_character.isdigit():
                updated_string = updated_string + "*"
            if character == "c" and previous_character.isdigit():
                updated_string = updated_string + "*"
            if character == "t" and previous_character.isdigit():
                updated_string = updated_string + "*"

            #Adds a multiply sign between exponential functions and numbers
            if character == "e" and previous_character.isdigit():
                updated_string = updated_string + "*"
            if character == "l" and previous_character.isdigit():
                updated_string = updated_string + "*"

            #Adds a multiply sign between x's and x's
            if character == "x" and previous_character == "x":
                updated_string = updated_string + "*"
            if previous_character == "x" and character == "x":
                updated_string = updated_string + "*"
            
            #Adds a multiply sign between digits and x's
            if character == "x" and previous_character.isdigit():
                updated_string = updated_string + "*"
            if previous_character == "x" and character.isdigit():
                updated_string = updated_string + "*"
            
            #Adds a multiply sign between digits and a set of brackets
            if character == "(" and previous_character.isdigit():
                updated_string = updated_string + "*"
            if previous_character == ")" and character.isdigit():
                updated_string = updated_string + "*"
            
            #Adds a multiply sign between x's and a set of brackets
            if previous_character == ")" and character == "x":
                updated_string = updated_string + "*"
            if character == "(" and previous_character == "x":
                updated_string = updated_string + "*"

        updated_string = updated_string + character
        return updated_string
    else:
        return string

#Validates limit inputs
def Limit_validate(Upper, Lower):
    return True
    #Checks numbers were entered
    try:
        Upper = float(Upper)
        Lower = float(Lower)
        #Checks the lower limit is smaller than the upper limit
        if Lower < Upper:
            return True
        else:
            return False
    except:
        return False