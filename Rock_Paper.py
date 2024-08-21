import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLabel,
    QLineEdit, QPushButton, QListWidget, QInputDialog, QMessageBox, QHBoxLayout
)
from PyQt5.QtCore import Qt

class ContactManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.contacts = [
            {'name': 'Alice Smith', 'phone': '123-456-7890', 'email': 'alice@example.com', 'address': '123 Maple St, Springfield'},
            {'name': 'Bob Johnson', 'phone': '987-654-3210', 'email': 'bob@example.com', 'address': '456 Oak St, Springfield'}
        ]

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contact Manager')
        self.setGeometry(200, 200, 600, 400)

        # Layout setup
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Contact List
        self.contact_list_widget = QListWidget()
        self.contact_list_widget.itemClicked.connect(self.display_contact_details)
        self.update_contact_list()
        main_layout.addWidget(self.contact_list_widget)

        # Buttons
        button_layout = QHBoxLayout()

        add_button = QPushButton('Add Contact')
        add_button.clicked.connect(self.add_contact)
        button_layout.addWidget(add_button)

        update_button = QPushButton('Update Contact')
        update_button.clicked.connect(self.update_contact)
        button_layout.addWidget(update_button)

        delete_button = QPushButton('Delete Contact')
        delete_button.clicked.connect(self.delete_contact)
        button_layout.addWidget(delete_button)

        search_button = QPushButton('Search Contact')
        search_button.clicked.connect(self.search_contact)
        button_layout.addWidget(search_button)

        main_layout.addLayout(button_layout)

        # Contact Details
        self.details_label = QLabel()
        main_layout.addWidget(self.details_label)

        self.setCentralWidget(central_widget)

    def update_contact_list(self):
        self.contact_list_widget.clear()
        for contact in self.contacts:
            self.contact_list_widget.addItem(f"{contact['name']} - {contact['phone']}")

    def display_contact_details(self):
        selected_contact = self.contact_list_widget.currentRow()
        contact = self.contacts[selected_contact]
        details = f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"
        self.details_label.setText(details)

    def add_contact(self):
        name, ok = QInputDialog.getText(self, 'Add Contact', 'Enter name:')
        if ok and name:
            phone, ok = QInputDialog.getText(self, 'Add Contact', 'Enter phone number:')
            if ok and phone:
                email, ok = QInputDialog.getText(self, 'Add Contact', 'Enter email:')
                if ok and email:
                    address, ok = QInputDialog.getText(self, 'Add Contact', 'Enter address:')
                    if ok and address:
                        self.contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
                        self.update_contact_list()

    def update_contact(self):
        selected_contact = self.contact_list_widget.currentRow()
        if selected_contact >= 0:
            contact = self.contacts[selected_contact]
            name, ok = QInputDialog.getText(self, 'Update Contact', 'Update name:', QLineEdit.Normal, contact['name'])
            if ok and name:
                phone, ok = QInputDialog.getText(self, 'Update Contact', 'Update phone number:', QLineEdit.Normal, contact['phone'])
                if ok and phone:
                    email, ok = QInputDialog.getText(self, 'Update Contact', 'Update email:', QLineEdit.Normal, contact['email'])
                    if ok and email:
                        address, ok = QInputDialog.getText(self, 'Update Contact', 'Update address:', QLineEdit.Normal, contact['address'])
                        if ok and address:
                            self.contacts[selected_contact] = {'name': name, 'phone': phone, 'email': email, 'address': address}
                            self.update_contact_list()

    def delete_contact(self):
        selected_contact = self.contact_list_widget.currentRow()
        if selected_contact >= 0:
            reply = QMessageBox.question(self, 'Delete Contact', 'Are you sure you want to delete this contact?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                del self.contacts[selected_contact]
                self.update_contact_list()
                self.details_label.clear()

    def search_contact(self):
        search_term, ok = QInputDialog.getText(self, 'Search Contact', 'Enter name or phone number:')
        if ok and search_term:
            for contact in self.contacts:
                if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                    details = f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"
                    self.details_label.setText(details)
                    break
            else:
                QMessageBox.information(self, 'Search Result', 'No contact found.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactManager()
    window.show()
    sys.exit(app.exec_())
