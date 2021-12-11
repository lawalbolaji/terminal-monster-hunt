from utils.printPause import print_pause


def valid_input(prompt, options, duration = 2):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause((f'"{option}" is invalid. '
                        'Please enter a valid option!'), duration)
