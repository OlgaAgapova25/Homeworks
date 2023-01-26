last_names = []
first_names = []
middle_names = []
phone_numbers = []
def write_data(last_name, first_name, mid_name, phone_number):
    last_names.append(last_name)
    first_names.append(first_name)
    middle_names.append(mid_name)
    phone_numbers.append(phone_number)
def import_data(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            input = str(line)
    input = input.split(',')
    for i in range(0,len(input),4):
        last_names.append(input[i])
    for i in range(1,len(input),4):
        first_names.append(input[i])
    for i in range(2,len(input),4):
        middle_names.append(input[i])
    for i in range(3,len(input),4):
        phone_numbers.append(input[i])
def get_data(last_name):
    indexes = [i for i, el in enumerate(last_names) if el == last_name]
    fn_search = [first_names[i] for i in indexes]
    mn_search = [middle_names[i] for i in indexes]
    ph_search = [phone_numbers[i] for i in indexes]
    for i in indexes:
        print(last_name)
        print(first_names[i])
        print(middle_names[i])
        print(phone_numbers[i])
        print()
    return fn_search, mn_search, ph_search
def export_data(last_name):
    first_names, mid_names, phone_numbers = get_data(last_name)
    with open('file.txt', 'a') as file:
        for i in range(len(first_names)):
            file.write(f'{last_name}\n')
            file.write(f'{first_names[i]}\n')
            file.write(f'{mid_names[i]}\n')
            file.write(f'{phone_numbers[i]}\n')
            file.write(f'\n')