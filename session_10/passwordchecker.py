


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
    
    # 3. NEXT IF PASSWORD HAS A LOWERCASE LETTER
    hasLowercase = False
    for char in password:
        if char.islower():
            hasLowercase = True
            break
   

    # 4. THEN CHECK IF PASSWORD HAS A NUMBER
    hasNumber = False
    for char in password:
        if char.isdigit():
            hasNumber = True
            break
    
        
    # 5. LASTLY IF PASSWORD HAS A SPECIAL CHARACTERS OR SYMBOLS
    symbols = "!@#$%^&*(),.?\":{}|<>"
    hasSymbol = False
    for char in password:
        if char in symbols:
            hasSymbol = True
            break
    
    

    if hasLowercase and hasNumber and hasUppercase and hasSymbol:
        isStrongPassword = True
    else:
        isStrongPassword = False
    
    return isStrongPassword

    
