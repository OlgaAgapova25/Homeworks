last_names = []
first_names = []
middle_names = []
phone_numbers = []
departments = []
def write_data(last_name, first_name, mid_name, phone_number, department):
    last_names.append(last_name)
    first_names.append(first_name)
    middle_names.append(mid_name)
    phone_numbers.append(phone_number)
    departments.append(department)
def import_data():
    file = open('new_contacts_file.txt', 'r')
    for line in file:
        input = str(line)
    new_file = open('file.txt', 'a')
    new_file.write(input)
    new_file.close()
    input = input.split(',')
    for i in range(0,len(input),5):
        last_names.append(input[i])
    for i in range(1,len(input),5):
        first_names.append(input[i])
    for i in range(2,len(input),5):
        middle_names.append(input[i])
    for i in range(3,len(input),5):
        phone_numbers.append(input[i])
    for i in range(4,len(input),5):
        departments.append(input[i])
    file.close()
def get_data(last_name):
    input = ''
    with open('file.txt','r') as file:
        for line in file:
            input = str(line)
    input = input.split(',')
    for i in range(0, len(input), 5):
        last_names.append(input[i])
    for i in range(1, len(input), 5):
        first_names.append(input[i])
    for i in range(2, len(input), 5):
        middle_names.append(input[i])
    for i in range(3, len(input), 5):
        phone_numbers.append(input[i])
    for i in range(4, len(input), 5):
        departments.append(input[i])
    indexes = [i for i, el in enumerate(last_names) if el == last_name]
    fn_search = [first_names[i] for i in indexes]
    mn_search = [middle_names[i] for i in indexes]
    ph_search = [phone_numbers[i] for i in indexes]
    dpt_search = [departments[i] for i in indexes]
    return fn_search, mn_search, ph_search, dpt_search
def export_data(last_name):
    first_names, mid_names, phone_numbers, departments = get_data(last_name)
    with open('file.txt', 'a') as file:
        for i in range(len(first_names)):
            file.write(f'{last_name},{first_names[i]},{mid_names[i]},{phone_numbers[i]},{departments[i]},')