import os
import sqlite3
from pprint import pprint

from tkContacts import ContactsGUI, Contact


class ContactsGUISQLite(ContactsGUI):
    contacts_table_name = 'contacts'

    def create_default_tables(self):
        with sqlite3.connect(self.path) as conn:
            c = conn.cursor()

            sql = f"CREATE TABLE {self.contacts_table_name} (" \
                  f"    contact_id INTEGER PRIMARY KEY AUTOINCREMENT," \
                  f"    name TEXT," \
                  f"    phone TEXT" \
                  f");"

            print(sql)

            c.execute(sql)

    def save_to_sqlite(self):

        with sqlite3.connect(self.path) as conn:
            c = conn.cursor()

            sql = f"DELETE FROM {self.contacts_table_name};"
            print(sql)
            c.execute(sql)  # delete all

            print(f"Saving to {self.path}!")

            for contact in self.contacts:
                contact: Contact
                sql = f'INSERT INTO {self.contacts_table_name}(name, phone) VALUES(' + \
                      contact.as_sqlite_values() + \
                      f');'

                print(sql)

                c.execute(sql)

    def load_from_sqlite(self):
        path = os.path.abspath(self.path)

        if not os.path.isfile(path):  # create blank file if file DNE
            print(f"File '{self.path}' DNE. Creating blank file.")

            self.create_blank_file()
            self.create_default_tables()
            self.load_default_contacts()
            self.save_to_disk()
            return

        print(f"SQLite DB '{self.path}' exists!")

        with sqlite3.connect(self.path) as conn:
            c = conn.cursor()

            sql = f"SELECT name, phone FROM {self.contacts_table_name};"
            print(sql)
            c.execute(sql)

            results = c.fetchall()
            pprint(results)

            for result in results:
                contact = Contact(result[0], result[1])
                self.contacts.append(contact)

    def save_to_disk(self):
        self.save_to_sqlite()

    def load_from_disk(self):
        self.load_from_sqlite()
