import tkinter as tk
from tkinter import messagebox
import csv

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open("contacts.csv", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    self.contacts.append(row)
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open("contacts.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.contacts)

    def add_contact(self, name, phone, email):
        self.contacts.append([name, phone, email])
        self.save_contacts()

    def delete_contact(self, index):
        del self.contacts[index]
        self.save_contacts()

    def edit_contact(self, index, name, phone, email):
        self.contacts[index] = [name, phone, email]
        self.save_contacts()

    def get_contacts(self):
        return self.contacts

class ContactManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        
        self.contact_manager = ContactManager()

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.contact_listbox = tk.Listbox(self.root, width=50)
        self.contact_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.populate_contact_listbox()

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=0, padx=5, pady=5)

        self.edit_button = tk.Button(self.root, text="Edit Contact", command=self.edit_contact)
        self.edit_button.grid(row=5, column=1, padx=5, pady=5)

    def populate_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contact_manager.get_contacts():
            self.contact_listbox.insert(tk.END, contact[0])

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            self.contact_manager.add_contact(name, phone, email)
            self.populate_contact_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Please fill in all fields.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.contact_manager.delete_contact(index)
            self.populate_contact_listbox()
        else:
            messagebox.showwarning("Error", "Please select a contact to delete.")

    def edit_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            if name and phone and email:
                self.contact_manager.edit_contact(index, name, phone, email)
                self.populate_contact_listbox()
                self.clear_entries()
            else:
                messagebox.showwarning("Error", "Please fill in all fields.")
        else:
            messagebox.showwarning("Error", "Please select a contact to edit.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerGUI(root)
    root.mainloop()
