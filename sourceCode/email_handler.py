import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PyQt5.QtWidgets import QMessageBox


class EmailHandler:
    def __init__(self, parent):
        self.parent = parent
        self.sender_email = ""
        self.sender_password = ""

    def save_credentials(self):
        self.sender_email = self.parent.email_input.text()
        self.sender_password = self.parent.password_input.text()

        if not self.sender_email or not self.sender_password:
            QMessageBox.critical(self.parent, "Error", "Please provide both email and password.")
        else:
            QMessageBox.information(self.parent, "Success", "Credentials saved successfully!")

    def send_emails(self):
        if self.parent.csv_handler.csv_data is None or self.parent.csv_handler.csv_data.empty:
            QMessageBox.critical(self.parent, "Error", "Please upload a CSV file first.")
            return
        
        recipient_column = self.parent.recipient_email_input.text()
        if recipient_column not in self.parent.csv_handler.csv_data.columns:
            QMessageBox.critical(self.parent, "Error", f"Recipient email column '{recipient_column}' does not exist.")
            return

        subject = self.parent.subject_input.text()
        body_template = self.parent.body_input.toPlainText()

        # Ensure subject is provided
        if not subject.strip():
            QMessageBox.critical(self.parent, "Error", "Email subject cannot be empty.")
            return

        # Ensure email body is provided
        if not body_template.strip():
            QMessageBox.critical(self.parent, "Error", "Email body cannot be empty.")
            return

        # Extract and validate input rows
        try:
            start_row = int(self.parent.start_row_input.text()) if self.parent.start_row_input.text() else 0
            end_row = int(self.parent.end_row_input.text()) if self.parent.end_row_input.text() else len(self.parent.csv_handler.csv_data)
        except ValueError:
            QMessageBox.critical(self.parent, "Error", "Please enter valid integers for row inputs.")
            return
        
        # Validate row ranges
        total_emails = end_row - start_row
        if total_emails <= 0:
            QMessageBox.critical(self.parent, "Error", "Invalid row range selected.")
            return
        
        # Validate row ranges
        csv_length = len(self.parent.csv_handler.csv_data)
        if not (0 <= start_row < csv_length) or not (0 < end_row <= csv_length) or start_row >= end_row:
            QMessageBox.critical(self.parent, "Error", "Invalid row range selected.")
            return

        self.parent.status_label.setText(f"Sending emails to {total_emails} recipients...")

        
        # Create SMTP session
        try:
            if self.sender_email and self.sender_password:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(self.sender_email, self.sender_password)

                for idx, row in self.parent.csv_handler.csv_data.iloc[start_row:end_row].iterrows():
                    try:
                        recipient_email = row[recipient_column]
                        email_body = body_template.format(**row)

                        message = MIMEMultipart()
                        message['From'] = self.sender_email
                        message['To'] = recipient_email
                        message['Subject'] = subject
                        message.attach(MIMEText(email_body, 'plain'))

                        server.sendmail(self.sender_email, recipient_email, message.as_string())

                        # Update progress (optional: add progress bar in UI)
                        progress = int(((idx - start_row + 1) / total_emails) * 100)
                        self.parent.status_label.setText(f"Progress: {progress}% ({idx + 1}/{total_emails})")

                    except Exception as e:
                        QMessageBox.warning(self.parent, "Warning", f"Failed to send email to {recipient_email}: {e}")

                server.quit()
                QMessageBox.information(self.parent, "Success", f"Successfully sent emails to {total_emails} recipients.")
            else:
                QMessageBox.critical(self.parent, "Error", "Save email credentials first.")
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Failed to send emails: {str(e)}")
