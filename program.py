calculation_to_units = 24
name_of_units = 'hours'



def days_to_units(number_of_days):
    return f'In {number_of_days} days are {calculation_to_units *number_of_days}{name_of_units}'


def validate_and_execute():
    try:
        user_input_number = int(user_input_number_list)
        if user_input_number < 0:
            print("Is a negativ number, please use a valid number")
        if user_input_number == 0 :
            print("User input is 0 and is invalid")
        elif user_input_number > 0:
            print(days_to_units(user_input_number))
    except ValueError:
        print("Is not a number, please insert a number")


user_input = ''
while user_input.lower() != "exit":
    user_input = input("Insert the number of days you want to convert in hours:\n") 
    for user_input_number_list in user_input.split(","):
        validate_and_execute()
