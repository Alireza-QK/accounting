from src.constants import OPTION_CHOICE


def choice_option(choice):

    print(list(OPTION_CHOICE.keys()))

    if choice in list(OPTION_CHOICE.keys()):
        print('yes')
    else:
        print('Invalid choice')
