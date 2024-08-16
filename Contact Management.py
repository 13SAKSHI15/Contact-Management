import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize the main window
root = tk.Tk()
root.title("Contact Management System")

# Initialize the contacts dictionary
contacts = {}

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter contact name:")
    if name:
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        update_contact_list()

# Function to update the contact list display
def update_contact_list():
    listbox.delete(0, tk.END)
    for name, info in contacts.items():
        listbox.insert(tk.END, f"{name}: {info['phone']}")

# Function to view contact details
def view_contact():
    selected = listbox.get(tk.ACTIVE)
    if selected:
        name = selected.split(":")[0]
        contact = contacts.get(name)
        if contact:
            messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")

# Function to update a contact
def update_contact():
    selected = listbox.get(tk.ACTIVE)
    if selected:
        name = selected.split(":")[0]
        if name in contacts:
            phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=contacts[name]["phone"])
            email = simpledialog.askstring("Input", "Enter new email:", initialvalue=contacts[name]["email"])
            address = simpledialog.askstring("Input", "Enter new address:", initialvalue=contacts[name]["address"])
            contacts[name] = {"phone": phone, "email": email, "address": address}
            update_contact_list()

# Function to delete a contact
def delete_contact():
    selected = listbox.get(tk.ACTIVE)
    if selected:
        name = selected.split(":")[0]
        if name in contacts:
            del contacts[name]
            update_contact_list()

# Function to search for a contact
def search_contact():
    search_term = simpledialog.askstring("Search", "Enter name or phone number:")
    if search_term:
        found = False
        for name, info in contacts.items():
            if search_term.lower() in name.lower() or search_term in info['phone']:
                messagebox.showinfo("Search Result", f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
                found = True
                break
        if not found:
            messagebox.showinfo("Search Result", "No contact found")

# Create GUI elements
frame = tk.Frame(root)
frame.pack(pady=10)

add_button = tk.Button(frame, text="Add Contact", command=add_contact)
add_button.pack(side=tk.LEFT, padx=5)

view_button = tk.Button(frame, text="View Contact", command=view_contact)
view_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(frame, text="Update Contact", command=update_contact)
update_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(frame, text="Delete Contact", command=delete_contact)
delete_button.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(frame, text="Search Contact", command=search_contact)
search_button.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

update_contact_list()

# Run the application
root.mainloop()