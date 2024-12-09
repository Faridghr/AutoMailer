# AutoMailer

## Introduction
Welcome to AutoMailer Application! This app is a powerful, easy-to-use application designed to streamline the process of sending personalized emails to multiple recipients based on data stored in a CSV file. Whether you're sending newsletters, invitations, or any other type of mass email, this app makes it easy to send emails in bulk with personalized content for each recipient.

## Features
- **CSV Upload:** Upload a CSV file containing your recipient data (e.g., names, email addresses, or other personalized fields).
- **Personalization:** Customize the email content using the data in the CSV file to send personalized messages.
- **Progress Tracking:** Track the progress of your email sending with an easy-to-understand progress bar.
- **Error Handling:** The app will alert you if any issues arise, such as missing data or failed email deliveries.
- **SMTP Integration:** The app integrates with Gmail’s SMTP server for sending emails.

## Step-by-Step Usage Guide

### 1. Start the Application:
Open the application. You should see a simple, user-friendly interface with fields for uploading your CSV file, setting email subject/body, and configuring other settings.

### 2. Upload Your CSV File:
Click the **"Upload CSV"** button to load your data file. This CSV file should contain at least one column with the email addresses of the recipients.
**Important:** Ensure that the CSV file has a header row and that it includes a column for email addresses. You’ll need to specify the name of this column when setting up the email sending process.

### 3. Configure Email Settings:
- **Recipient Column:** Enter the name of the column in your CSV file that contains the recipients' email addresses. The app will use this column to send emails.
- **Email Subject:** Enter the subject of the email you want to send to all recipients.
- **Email Body:** Write the body of the email in the provided text box. You can use placeholders (such as `{Name}`, `{Address}`, etc.) from your CSV data to personalize the email content for each recipient. For example, if your CSV has a column called "Name", you can use `{Name}` in the email body, and the app will replace it with the recipient's name.

### 4. Set Email Range:
- **Start Row:** Specify the starting row in the CSV file from which you want to begin sending emails (typically after the header). If you want to start from the first recipient, leave this at 0.
- **End Row:** Specify the last row for sending emails. If you want to send emails to all recipients in the file, leave this blank or set it to the last row of your CSV.

### 5. Enter Sender Email Credentials:
- **Sender Email:** Enter your Gmail email address that will be used to send the emails.
- **Sender Password:** Enter the password for your Gmail account. This is required to authenticate and send emails through Gmail’s SMTP server.

**Note:** Make sure to use an app-specific password for Gmail if two-factor authentication is enabled.

### 6. Send Emails:
After setting everything up, click the **"Send Emails"** button to start sending emails. The app will process the CSV file row by row, sending personalized emails to each recipient.
During the process, you’ll see a progress bar indicating how many emails have been sent. Once completed, a success message will appear, confirming the number of emails successfully sent.

### 7. Track and Handle Errors:
If the app encounters any issues (e.g., invalid email address, missing required fields), it will notify you through error messages. If an email fails to send, the app will continue sending the remaining emails, and you’ll receive a detailed error message.

### 8. Finish:
Once all emails have been sent, you’ll receive a confirmation message with the total number of successful emails. You can then close the application or upload another CSV file to send more emails.

## Best Practices
- **Ensure Data Accuracy:** Before uploading your CSV file, double-check that all email addresses are valid and that the column names match the ones you input into the app (especially for the recipient email column).
- **Use Placeholders Wisely:** Make sure your CSV file contains the necessary data to replace the placeholders you’ve used in the email body (e.g., `{Name}`, `{City}`).
- **Test with a Small List:** For the first run, try sending emails to a small group (e.g., 3–5) to ensure everything is set up correctly.

## Troubleshooting

- **Error Message:** If you encounter issues with sending emails, check the error message for details. Common issues include missing columns in the CSV file or incorrect email credentials.
- **SMTP Issues:** If the app can't connect to the email server, ensure that your internet connection is stable and that you've entered the correct email settings (especially the sender email and password).

## Security and Privacy
Your email credentials are required to send emails through your Gmail account. The application does **not** store or share your email credentials. However, make sure to use **app-specific passwords** for Gmail for added security.

## Conclusion
This app is a powerful tool for managing mass email campaigns, newsletters, and personalized email communication, simplifying the process while giving you full control over your email content. Happy emailing!
