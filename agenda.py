AGENDA = {}

def show_contacts():
    for contact in AGENDA:
        get_contact(contact)
        print('----------------------------')

def get_contact(contact):
    print("Name:", contact)
    print("Tel:", AGENDA[contact][Tel])
    print("Email:", AGENDA[contact][Email])
    print("Adress:", AGENDA[contact][Adress])

def add_contact(contact, tel, email, adress):
    AGENDA[contact] = {
        'Tel': tel,
        'Email': email,
        'Adress': adress,
    }
    print('>>>The conctact {} has been added sucessfully<<'.format(contact))


def edit_contact(contact, key, value):
    if key == 'Tel':
        AGENDA[contact] = {
            'Tel': value
        }
    if key == 'Email':
        AGENDA[contact] = {
            'Email': value
        }
    if key == 'Adress'
        AGENDA[contact] = {
           'Adress': value
       }
    print('>>>The conctact {} has been edited sucessfully<<'.format(contact))

def delete_contact(contact):
    AGENDA.pop(contact)
    print('>>>The conctact {} has been deleted sucessfully<<'.format(contact))

def print_menu ():
    print('---------------------------------------')
    print('1 - Show all contacts')
    print('2 - Search contact')
    print('3 - Add contact')
    print('4 - Edit contact')
    print('5 - Delete contact')
    print('0 - Exit the program')
    print('---------------------------------------')

print_menu()
option = input('Choose a option: ')


while True:
    if option == '1':
        show_contacts()
    elif option == '2':
        contact = input('Type the contact name')
        get_contact(contact)
    elif option == '3':
        contact = input('Type the contact name')
        tel = input('Type the contact telephone')
        email = input('Type the contact email')
        adress = input('Type the contact adress')
        add_contact(contact, tel, email, adress)
    elif option == '4':
        contact = input('Type the contact name that you wanna edit')
        key = input('What field do you wanna edit?')
        value = input('What will be the new value for the field?')
        edit_contact(contact, key, value)
    elif option == '5':
        contact = input('Type the contact name that you wanna delete')
        delete_contact(contact)
    elif option == '0':
        break
    else:
        print('Invalid option')