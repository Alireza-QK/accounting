from os import system, name
from db import check_exsist, create
from utils import input_user


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def show_text():
    print('Choice option: ', end='\n')
    print('Option 1: Create new user')
    print('Option 2: Login')
    print('*' * 40)

show_text()


isTrue = False
while isTrue is not True:
    option = input_user('Which option: ')

    if option == '1':
        first_name = input_user('Enter fitst name: ')
        last_name = input_user('Enter last name: ')
        username = input_user('Enter username: ')
        password = input_user('Enter password: ')
        age = input_user('Enter age: ')
        email = input_user('Enter email: ')
        phone = input_user('Enter phone: ')
        check_user = check_exsist('user', username=username)
        if check_user is not True:
            res = create('User',
                first_name=first_name, last_name=last_name,username=username,password=password,
                age=age,email=email,phone_number=phone
            )
            if res:
                isTrue = True
                clear()
                show_text()
        else:
            isTrue = True
        isTrue = False

    elif option == '2':
        print('login')
        clear()
        show_text()




