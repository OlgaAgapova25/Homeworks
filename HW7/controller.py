import db_model
import UI

def new_contact():
    last_name, first_name, mid_name, phone_number = UI.get_value()
    db_model.write_data(last_name, first_name, mid_name, phone_number)
def get_contact():
    last_name = UI.view_data()
    contacts = db_model.get_data(last_name)

def export_contacts():
    last_name = UI.view_data()
    db_model.export_data(last_name)

def import_contacts():
    file_name = UI.import_data()
    db_model.import_data(file_name)