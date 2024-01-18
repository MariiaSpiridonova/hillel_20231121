symbols = '!"£$%^&*()_+`:;@""|{}[]#~?/.,<>'


def password_checker(function):
    def wrapper():
        password = function()
        if password is not None:
            if not any(char.isdigit() for char in password):
                print("Please use at least 1 digit")
                wrapper()
            elif not any(char.isalpha() for char in password):
                print("Please use at least 1 letter")
                wrapper()
            elif not any(char in symbols for char in password):
                print("Please use at least 1 special symbol")
                wrapper()
            elif len(password) < 8:
                print("Password should consist of min 8 characters")
                wrapper()
            else:
                print(f"Password {password} meets the requirements")

        else:
            print("Please check requirements and try again")
            wrapper()

    return wrapper()


@password_checker
def input_password():
    password = input(
        "Password should consist of min 8 characters and contain "
        "at least 1 letter, 1 digit and 1 special symbol. "
        "No spaces or TAB allowed. \nPlease enter the password >>> "
    )
    if not password or any(char.isspace() for char in password):
        print("Password could not be empty. No spaces or TAB allowed")
        return None
    else:
        return password

#
# input_password()
