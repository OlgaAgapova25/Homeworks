def get_value():
    last_name = str(input("Enter the last name: "))
    first_name = str(input("Enter the first name: "))
    mid_name = str(input("Enter the middle name: "))
    phone_number = str(input("Enter the phone number: "))
    return last_name, first_name, mid_name, phone_number

def view_data():
    last_name = str(input("Enter the last name of a person you're searching: "))
    return last_name

def import_data():
    file_name = str(input("Enter the name of the file you'd like to get data from: "))
    return file_name