import controller

def main():
    choice = int(input("Enter the option you need:\n"
                       "1 To add a contact\n"
                       "2 To find contacts of a person\n"
                       "3 To export contacts: "))
    if choice == 1:
        controller.new_contact()
    elif choice == 2:
        controller.get_contact()
    elif choice == 3:
        controller.export_contacts()

if __name__ == "__main__":
    main()