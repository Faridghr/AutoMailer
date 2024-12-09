from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QPushButton, QLabel, QLineEdit,
    QTextEdit, QFileDialog, QWidget, QFormLayout, QTabWidget, QMessageBox
)
from PyQt5.QtCore import Qt
from csv_handler import CSVHandler
from email_handler import EmailHandler

class EmailSenderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoMailer - Email Sender")
        self.resize(800, 600)

        # Handlers
        self.csv_handler = CSVHandler(self)
        self.email_handler = EmailHandler(self)

        # UI Components
        self.init_ui()

    def init_ui(self):
        # UI Components
        self.csv_label = QLabel("No CSV file uploaded")
        self.csv_label.setAlignment(Qt.AlignCenter)
        self.csv_label.setStyleSheet("font-size: 16px; color: #333333; padding: 10px;")
        
        self.upload_button = QPushButton("Upload CSV")
        self.upload_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 14px; padding: 10px; border-radius: 5px;")
        
        self.columns_label = QLabel("Available Columns (Use {column_name} to insert dynamically in Email Body):")
        self.columns_label.setStyleSheet("font-size: 14px; color: #333333; padding: 10px;")
        
        self.columns_text = QTextEdit()
        self.columns_text.setReadOnly(True)
        self.columns_text.setStyleSheet("font-size: 14px; padding: 10px; background-color: white; border: 1px solid #ccc; border-radius: 5px;")

        self.subject_input = QLineEdit()
        self.subject_input.setStyleSheet("font-size: 14px; padding: 10px; border-radius: 5px; background-color: white; border: 1px solid #ccc;")
        
        self.body_input = QTextEdit()
        self.body_input.setStyleSheet("font-size: 14px; padding: 10px; background-color: white; border: 1px solid #ccc; border-radius: 5px;")
        self.body_input.setFixedHeight(300)
        
        self.start_row_input = QLineEdit()
        self.start_row_input.setPlaceholderText("Start Row (x)")
        self.start_row_input.setStyleSheet("font-size: 14px; padding: 10px; border-radius: 5px; background-color: white; border: 1px solid #ccc;")

        self.end_row_input = QLineEdit()
        self.end_row_input.setPlaceholderText("End Row (y)")
        self.end_row_input.setStyleSheet("font-size: 14px; padding: 10px; border-radius: 5px; background-color: white; border: 1px solid #ccc;")

        # New instruction label
        self.dynamic_instruction_label = QLabel("Use {column_name} in the email body to dynamically insert values from the CSV.")
        self.dynamic_instruction_label.setAlignment(Qt.AlignCenter)
        self.dynamic_instruction_label.setStyleSheet("font-size: 14px; color: #555555; padding: 10px; font-style: italic;")

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 16px; color: #333333; padding: 10px;")

        self.send_button = QPushButton("Send Emails")
        self.send_button.setStyleSheet("background-color: #2196F3; color: white; font-size: 14px; padding: 10px; border-radius: 5px;")

        self.recipient_email_input = QLineEdit()
        self.recipient_email_input.setPlaceholderText("Recipient Email Column Name")
        self.recipient_email_input.setStyleSheet("font-size: 14px; padding: 10px; border-radius: 5px; background-color: white; border: 1px solid #ccc;")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Your Email Address")
        self.email_input.setStyleSheet("font-size: 14px; padding: 10px; border-radius: 5px; background-color: white; border: 1px solid #ccc;")
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Your Email App Password")
        self.password_input.setStyleSheet("font-size: 14px; padding: 10px; border-radius: 5px; background-color: white; border: 1px solid #ccc;")
        self.password_input.setEchoMode(QLineEdit.Password)
        
        self.save_credentials_button = QPushButton("Save Credentials")
        self.save_credentials_button.setStyleSheet("background-color: #FFC107; color: white; font-size: 14px; padding: 10px; border-radius: 5px;")
        
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("font-size: 14px; padding: 10px; background-color: #f5f5f5;")

        csv_layout = QVBoxLayout()
        form_layout = QFormLayout()
        
        form_layout.addRow(self.csv_label)
        form_layout.addRow(self.upload_button)
        form_layout.addRow(self.columns_label)
        form_layout.addRow(self.columns_text)
        form_layout.addRow("Recipient Email Column:", self.recipient_email_input)
        form_layout.addRow("Subject:", self.subject_input)
        form_layout.addRow("Email Body:", self.body_input)
        form_layout.addRow("Send Emails From Row:", self.start_row_input)
        form_layout.addRow("To Row:", self.end_row_input)
        form_layout.addRow(self.dynamic_instruction_label)  # Add the dynamic instruction label
        form_layout.addRow(self.send_button)
        form_layout.addRow(self.status_label)
        csv_layout.addLayout(form_layout)

        csv_tab = QWidget()
        csv_tab.setLayout(csv_layout)
        self.tab_widget.addTab(csv_tab, "Send Emails")
        
        credentials_layout = QVBoxLayout()
        credentials_layout.addWidget(self.email_input)
        credentials_layout.addWidget(self.password_input)
        credentials_layout.addWidget(self.save_credentials_button)

        # Add an empty widget at the end to push the widgets to the left
        empty_widget = QWidget()
        credentials_layout.addWidget(empty_widget, 1)

        credentials_tab = QWidget()
        credentials_tab.setLayout(credentials_layout)
        self.tab_widget.addTab(credentials_tab, "Email Credentials")
        
        self.setCentralWidget(self.tab_widget)

        # Connect signals
        self.upload_button.clicked.connect(self.csv_handler.upload_csv)
        self.send_button.clicked.connect(self.email_handler.send_emails)
        self.save_credentials_button.clicked.connect(self.email_handler.save_credentials)
