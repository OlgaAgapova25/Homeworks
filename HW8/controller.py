import db_model
import UI

def new_contact():
    last_name, first_name, mid_name, phone_number, department = UI.get_value()
    db_model.write_data(last_name, first_name, mid_name, phone_number, department)
    db_model.export_data(last_name)
def get_contact():
    last_name = UI.view_data()
    first_names, middle_names, phones, dptmnts = db_model.get_data(last_name)
    print(list(zip(first_names, middle_names, phones, dptmnts)))

def export_contacts():
    last_name = UI.view_data()
    db_model.export_data(last_name)

def import_contacts():
    db_model.import_data()