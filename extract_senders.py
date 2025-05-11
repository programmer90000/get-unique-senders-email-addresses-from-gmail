import mailbox
from email.utils import parseaddr

# Path to your MBOX file (adjust if needed)
mbox_file = 'all_mail.mbox'

# Open the mailbox
mbox = mailbox.mbox(mbox_file)

# Set to collect unique sender emails
unique_senders = set()

for message in mbox:
    if message['From'] is None:
        continue  # skip if 'From' is missing
    name, email = parseaddr(message['From'])
    if email:
        unique_senders.add(email.lower())  # normalize to lowercase

# Save to a file
with open('unique_senders.txt', 'w') as f:
    for sender in sorted(unique_senders):
        f.write(sender + '\n')

print(f'Extracted {len(unique_senders)} unique sender email addresses.')
