import os

from labs.lab8.tkContacts import contact_list_from_path, ContactsGUI, Contact
from labs.lab8.contacts import contactlistdata

contacts_file = 'contacts.txt'

if __name__ == '__main__':

    if os.path.exists(contacts_file):
        print("'" + contacts_file + "' exists! Loading values from it...")
        contactlist = contact_list_from_path(contacts_file)
    else:
        print(f"'{contacts_file}' doesn't exist. Using default data.")
        contactlist = contactlistdata
    contacts = ContactsGUI(contactlist, contacts_file)

    contacts.root.mainloop()
