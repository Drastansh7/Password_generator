import string
import secrets

def password_generator(pwd_len):
    try:
        lower_elems = string.ascii_lowercase
        upper_elems = string.ascii_uppercase
        digit_elems = string.digits
        special_elems = string.punctuation

        elems_lst = []
        elems_lst.extend(list(lower_elems))
        elems_lst.extend(list(upper_elems))
        elems_lst.extend(list(digit_elems))
        elems_lst.extend(list(special_elems))

        res = []
        for i in range(pwd_len):
            res.append(secrets.choice(elems_lst))
        return "".join(res)

    except Exception as e:
        return f"Error occurred: {e} "

if __name__ == '__main__':
    try:
        pwd_len = int(input("How long would you like your password to be: "))
        password = password_generator(pwd_len)
        print("Your password is:", password)
    except ValueError:
        print("Kindly enter a valid number for the length of the password.")






