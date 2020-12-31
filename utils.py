
def input_user(text):
    """ This input check is empty or not """
    input_user_var = input(f'{text}: ')
    if input_user_var == '':
        input_user(text)

    return input_user_var