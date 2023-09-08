import imaplib
import email
from datetime import datetime, timedelta

# Email account details
IMAP_SERVER = 'imap.gmail.com'
USERNAME = 'joseph.r.heath@gmail.com'
PASSWORD = 'Tr@shpand@81!'

# Time period to retrieve senders from
start_date = datetime.now() - timedelta(days=7)  # Change as needed
end_date = datetime.now()  # Change as needed

# Connect to the email server
imap = imaplib.IMAP4_SSL(IMAP_SERVER)
imap.login(USERNAME, PASSWORD)
imap.select('INBOX')

# Search for emails within the specified date range
search_criteria = f'(SINCE {start_date.strftime("%d-%b-%Y")}) (BEFORE {end_date.strftime("%d-%b-%Y")})'
status, data = imap.search(None, search_criteria)

senders = set()  # Store unique senders

# Iterate over the retrieved email IDs
for num in data[0].split():
    status, email_data = imap.fetch(num, '(RFC822)')
    raw_email = email_data[0][1]
    email_message = email.message_from_bytes(raw_email)

    sender = email_message['From']
    senders.add(sender)

# Print the list of senders
for sender in senders:
    print(sender)

# Close the connection to the email server
imap.close()
imap.logout()
