
#postal code validation
def postal_code_validation():
    max_attempts = 5
    for attempt in range(max_attempts):
        postal_code = input('Enter your postal code: ')
        if postal_code.isdigit():
            return postal_code  
        else:
            print('Please enter a valid postal code.')
    print('Exceeded maximum attempts. Exiting.')
    exit()
    return None 

#mobile number validation
def mobile_number_validation():    
    max_attempts = 5
    for attempt in range(max_attempts):
        mobile_number = input('Enter your mobile number: ')
        if(mobile_number.isdigit()):
            return mobile_number
        else:
            print('Please enter a valid mobile number!')
    print('Exceeded maximum attempts. Exiting.')
    exit()
    return None 


#input - password validation---------------------------------------------------------------------------
def containsLetterAndNumber(input_password):
    return any(char.isalpha() for char in input_password) and any(char.isdigit() for char in input_password)

def containsBlankSpace(input_password):
    return ' ' in input_password

def containsSpecialCharacter(input_password):
    special_characters = "!@#$%^&*()-_+=[]{}|:;<>,.?/"
    return any(char in special_characters for char in input_password)

def correctPW(passWord):
    while True:
        if len(passWord) < 6 or len(passWord) > 12:
            print("\nSorry! Your password is invalid.")
            print("It must be between 6 and 12 characters in length.")
        elif not containsLetterAndNumber(passWord):
            print("\nSorry! Your password is invalid.")
            print("It must contain at least one alphabetical character and one numerical digit.")
        elif containsBlankSpace(passWord):
            print("\nSorry! Your password is invalid.")
            print("It shouldn't have any blank space in it.")
        elif not containsSpecialCharacter(passWord):
            print("\nSorry! Your password is invalid.")
            print("It must contain at least one special character.")
        else:
            print("Your password is valid!")
            return passWord

        passWord = input("\nEnter new password: ")
