import os

from labs.lab8.tkContacts import ContactsGUI, Contact, ContactsGUISQLite

contacts_file = 'contacts.db'

if __name__ == '__main__':
    contacts_gui = ContactsGUISQLite(contacts_file)

    contacts_gui.root.mainloop()
