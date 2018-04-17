import os
import sqlite3
from tkinter import *


class Contact:
    @staticmethod
    def from_line(line: str):
        lines = line.split(',')

        name = ','.join(lines[:-1])  # all but last
        phone = lines[-1]  # last

        contact = Contact(name, phone)
        return contact

    def as_sqlite_values(self):
        return rf''' '{self.name}', '{self.phone}' '''

    def __init__(self, name: str, phone: str):
        name = name.strip()
        phone = phone.strip()

        self.name: str = name
        self.phone: str = phone

    def __str__(self):
        return f"{self.name}, {self.phone}"

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    def __iter__(self):
        yield self.name
        yield self.phone


default_contact_list = [
    ('Siemens, Harper', '323-4149'),
    ('Smith, Patti', '239-1212'),
    ('Jackson, Janet', '313-1352'),
    ('Manfredi, Ralph', '872-2221'),
    ('Thompson, Bobby', '365-2622'),
    ('James, Lebron', '457-6223'),
    ('Ziegler, Zig', '667-1101'),
    ('Robbins, Tony', '329-2310')
]

default_contact_list = [Contact(name, phone) for (name, phone) in default_contact_list]


class ContactsGUI:
    def selection(self):
        print("At %s of %d" % (self.select.curselection(), len(self.contacts)))
        return int(self.select.curselection()[0])

    def get_name(self):
        return self.nameVar.get()

    def get_phone(self):
        return self.phoneVar.get()

    def get_contact_from_fields(self):
        return Contact(self.get_name(), self.get_phone())

    def get_selected(self):
        return self.contacts[self.selection()]

    def add_contact(self):
        self.contacts.append(self.get_contact_from_fields())
        self.set_list()

    def update_selected_contact(self):
        self.contacts[self.selection()] = self.get_contact_from_fields()
        self.set_list()

    def delete_selected_contact(self):
        del self.contacts[self.selection()]
        self.set_list()

    def load_selected_contact(self):
        name, phone = self.contacts[self.selection()]
        self.nameVar.set(name)
        self.phoneVar.set(phone)

    def __init__(self, path):
        self.path = path
        self.load_from_disk()

        self.root = Tk()

        self.root.winfo_toplevel().title("My Contact List")

        self.framebuttons = Frame(self.root)
        self.framebuttons.pack(fill=BOTH, expand=YES)

        Label(self.framebuttons, text="Name:").grid(row=0, column=0, sticky=N)
        self.nameVar = StringVar()
        self.name = Entry(self.framebuttons, textvariable=self.nameVar)
        self.name.grid(row=0, column=1, sticky=W)

        Label(self.framebuttons, text="Phone:").grid(row=1, column=0, sticky=N)
        self.phoneVar = StringVar()
        self.phone = Entry(self.framebuttons, textvariable=self.phoneVar)
        self.phone.grid(row=1, column=1, sticky=N)

        self.framebuttons = Frame(self.root)  # add a row of buttons
        self.framebuttons.pack()
        self.btn_add = Button(self.framebuttons, text=" Add  ", command=self.add_contact)
        self.btn_update = Button(self.framebuttons, text="Update", command=self.update_selected_contact)
        self.btn_delete = Button(self.framebuttons, text="Delete", command=self.delete_selected_contact)
        self.btn_load = Button(self.framebuttons, text=" Load ", command=self.load_selected_contact)
        self.btn_save = Button(self.framebuttons, text=" Save ", command=self.set_list)

        self.btn_add.pack(side=LEFT)
        self.btn_update.pack(side=LEFT)
        self.btn_delete.pack(side=LEFT)
        self.btn_load.pack(side=LEFT)
        self.btn_save.pack(side=LEFT)

        self.framebuttons = Frame(self.root)  # allow for selection of names
        self.framebuttons.pack()
        self.scroll = Scrollbar(self.framebuttons, orient=VERTICAL)
        self.select = Listbox(self.framebuttons, yscrollcommand=self.scroll.set, height=7)
        self.scroll.config(command=self.select.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.select.pack(side=LEFT, fill=BOTH)

        self.set_list()

    def set_list(self):
        """Resets displayed list from self.contacts."""
        self.contacts.sort()
        self.select.delete(0, END)

        for contact in self.contacts:
            self.select.insert(END, contact.name)

        self.save_to_disk()

    def load_default_contacts(self):
        self.contacts = default_contact_list

    def create_blank_file(self):
        with open(self.path, 'w') as f:
            pass

    def create_default_file(self):
        self.load_default_contacts()
        self.save_to_disk()

    def save_to_disk(self):
        self.save_to_file()

    def load_from_disk(self):
        self.load_from_file()

    def load_from_file(self):
        self.contacts = ContactsGUI.load_from_file_s(self.path)

    @staticmethod
    def load_from_file_s(path) -> list:
        ret = []
        with open(path, 'r') as f:
            for line in f:
                line = line.replace('\r', '').replace('\n', '')
                contact = Contact.from_line(line)
                ret.append(contact)
        return ret

    def save_to_file(self):
        with open(self.path, 'w') as f:
            print("Writing list to file at '" + self.path + "'.")

            for contact in self.contacts:
                line = str(contact)
                f.write(line + '\n')


class ContactsGUISQLite(ContactsGUI):
    contacts_table_name = 'contacts'

    def create_default_tables(self):
        with sqlite3.connect(self.path) as conn:
            c = conn.cursor()

            sql = f"""CREATE TABLE {self.contacts_table_name} (
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT
);"""

            print(sql)

            c.execute(sql)

    def save_to_sqlite(self):
        conn = sqlite3.connect(self.path)

        c = conn.cursor()

        for contact in self.contacts:
            sql = f'INSERT INTO {self.contacts_table_name} VALUES()'

            print(sql)

            c.execute(sql)

        conn.close()

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

        conn = sqlite3.connect(self.path)

        c = conn.cursor()

        print(conn)
        print(c)

        conn.close()

    def save_to_disk(self):
        self.save_to_sqlite()

    def load_from_disk(self):
        self.load_from_sqlite()
