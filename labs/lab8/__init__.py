import os

from tkContactsSQLite import ContactsGUISQLite

contacts_file = 'contacts.db'

if __name__ == '__main__':
    contacts_gui = ContactsGUISQLite(contacts_file)

    contacts_gui.root.mainloop()
