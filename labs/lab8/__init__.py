import os

from labs.lab7.tkContacts import loadListFromFile, Contacts

contacts_file = 'contacts.txt'

if __name__ == '__main__':

    if os.path.exists(contacts_file):
        print("'" + contacts_file + "' exists! Loading values from it...")
        contactlist = loadListFromFile(contacts_file)

    contacts = Contacts(contactlist, contacts_file)

    contacts.root.mainloop()
