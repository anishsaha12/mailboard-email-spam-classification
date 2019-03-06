import email
import imaplib

def get_new_mail(last_uid = 7344, host= "imap.gmail.com", port=993, login="anishsaha12@gmail.com", password="ani99001161"):
    print('hi')
    # connect
    mail_server = imaplib.IMAP4_SSL(host, port)

    # authenticate
    mail_server.login(login, password)

    # issue the search command of the form "SEARCH UID 42:"
    command = "SEARCH UID "+str(last_uid)+":"
    mail_server.select(mailbox='INBOX')
    result, data = mail_server.uid(command=command) # gives all uids from last_uid to latest in INBOX
    messages = data[0].split()
    print(messages)

    # yield mails
    for message_uid in messages:
        # SEARCH command always returns at least the most
        # recent message, even if it has already been synced
        if int(message_uid) > last_uid:
            result, msg = mail_server.uid('fetch', message_uid, '(RFC822)') # return a tuple with status as first and msg as second
            print (int(message_uid), email.message_from_string(msg[0][1].decode('utf-8')))

get_new_mail()