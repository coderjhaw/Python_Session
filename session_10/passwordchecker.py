


def checkPassword(password):
    # CRITERIA FOR STRONG PASSWORD
        # 1. contains at least 10 characters
        # 2. contains uppercase letter
        # 3. contains lowercase letter
        # 4. contains number
        # 5. has a special character (!@#$%^&*)
    
    isStrongPassword = False
    # 1. FIRST BASIS FOR PASSWORD STRENGTH IS CHECK THE PASSWORD LENGTH
    # HERE I set minimum password length of 8
    if len(password) < 10:
        return "Password should be at least 10 characters long"

    # 2. NEXT IF PASSWORD HAS AN UPPERCASE LETTER
    hasUppercase = False
    for char in password:
        if char.isupper():
            hasUppercase = True
            break
    # WARNING IF PASSWORD DOESN'T HAVE AN UPPERCASE
    # if not hasUppercase:
    #     return "Password must have an upper case letter!"

    # 3. NEXT IF PASSWORD HAS A LOWERCASE LETTER
    hasLowercase = False
    for char in password:
        if char.islower():
            hasLowercase = True
            break
    # WARNING IF PASSWORD DOESN'T HAVE A LOWERCASE 
    # if not hasLowercase:
    #     return "Password must have a lower case letter!"

    # 4. THEN CHECK IF PASSWORD HAS A NUMBER
    hasNumber = False
    for char in password:
        if char.isdigit():
            hasNumber = True
            break
    # WARNING IF PASSWORD DOESN'T HAVE A NUMBER
    # if not hasNumber:
    #     return "Password should contain at least one digit number."
        
    # 5. LASTLY IF PASSWORD HAS A SPECIAL CHARACTERS OR SYMBOLS
    symbols = "!@#$%^&*(),.?\":{}|<>"
    hasSymbol = False
    for char in password:
        if char in symbols:
            hasSymbol = True
            break
    # WARNING IF PASSWORD DOESN'T HAVE AT LEAST 1 SPECIAL CHARACTER
    # if not hasSymbol:
    #     return "Password should include special character or symbol like !@#$%^&*("
    

    if hasLowercase and hasNumber and hasUppercase and hasSymbol:
        isStrongPassword = True
    else:
        isStrongPassword = False
    
    return isStrongPassword

    
