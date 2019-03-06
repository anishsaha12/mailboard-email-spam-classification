import email
import imaplib

# class EmailReader:

    # def __init__(self, contact):                #to login contact
    #     self.contact = contact
    #     # Logging in to the inbox
    #     self.mail = imaplib.IMAP4_SSL('imap.gmail.com',port=993)
    #     self.mail.login(self.contact['id'], self.contact['password'])
    #     self.mail.select("inbox") # connect to inbox.

    #     result, data = self.mail.uid('search', None, "ALL") # search and return uids instead
    #     self.email_uids = data[0].split()

    # def get_decoded_email_body(self, message_body):
    #     """ Decode email body.
    #     Detect character set if the header is not set.
    #     We try to get text/plain, but if there is not one then fallback to text/html.
    #     :param message_body: Raw 7-bit message body input e.g. from imaplib. Double encoded in quoted-printable and latin-1
    #     :return: Message body as unicode string
    #     """

    #     msg = email.message_from_string(message_body.decode('utf8'))

    #     text = ""
    #     if msg.is_multipart():
    #         html = None
    #         for part in msg.walk():

    #             # print ("%s, %s" % (part.get_content_type(), part.get_content_charset()))

    #             if part.get_content_charset() is None:
    #                 # We cannot know the character set, so return decoded "something"
    #                 text = part.get_payload(decode=True)
    #                 continue

    #             charset = part.get_content_charset()

    #             if part.get_content_type() == 'text/plain':
    #                 text = str(part.get_payload(decode=True), str(charset), "ignore").encode('utf8', 'replace')

    #             if part.get_content_type() == 'text/html':
    #                 html = str(part.get_payload(decode=True), str(charset), "ignore").encode('utf8', 'replace')

    #         if text is not None:
    #             return text.strip()
    #         else:
    #             return html.strip()
    #     else:
    #         text = str(msg.get_payload(decode=True), msg.get_content_charset(), 'ignore').encode('utf8', 'replace')
    #         return text.strip()

    # def get_email(self, index =-1):             #default gets latest email
    #     mail = self.mail
    #     email_uid = self.email_uids[index]
    #     # print("UIDs",self.email_uids)
    #     result, data = mail.uid('fetch', email_uid, '(RFC822)')
    #     raw_email = data[0][1]

    #     # print(raw_email.decode('utf8'))
    #     email_message = email.message_from_string(raw_email.decode('utf8') )

    #     email_obj = dict()
    #     from_contact = dict()
    #     email_from = email.utils.parseaddr(email_message['From'])   # for parsing "FirstName LastName" <email@domain.com>
    #     from_contact['name']= email_from[0]
    #     from_contact['id']= email_from[1]
    #     email_obj['from'] = from_contact
    #     email_obj['to'] = email_message['To'].split(',')
    #     if email_message['Cc']:
    #         email_obj['cc'] = email_message['Cc'].split(',')
    #     else:
    #         email_obj['cc'] = []
    #     email_obj['date'] = email_message['Date']
    #     # email_obj['content-type'] = email_message['Content-Type']
    #     # email_obj['mime-version'] = email_message['MIME-Version']
    #     email_obj['subject'] = email_message['Subject']
    #     email_obj['body'] = self.get_decoded_email_body(raw_email)

    #     return email_obj

    # def all_emails(self):
    #     emails = []
    #     for i in range(len(self.email_uids)):
    #         emails.append(self.get_email(i))

    #     return emails

class EmailReader:

    def __init__(self, contact):                #to login contact
        self.contact = contact
        # Logging in to the inbox
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com',port=993)
        self.mail.login(self.contact['id'], self.contact['password'])
        self.mail.select("inbox") # connect to inbox.

        result, data = self.mail.uid('search', None, "ALL") # search and return uids instead
        self.email_uids = data[0].split()

    def get_decoded_email_body(self, message_body):
        """ Decode email body.
        Detect character set if the header is not set.
        We try to get text/plain, but if there is not one then fallback to text/html.
        :param message_body: Raw 7-bit message body input e.g. from imaplib. Double encoded in quoted-printable and latin-1
        :return: Message body as unicode string
        """

        msg = email.message_from_string(message_body.decode('utf8'))

        text = ""
        if msg.is_multipart():
            html = None
            for part in msg.walk():

                # print ("%s, %s" % (part.get_content_type(), part.get_content_charset()))

                if part.get_content_charset() is None:
                    # We cannot know the character set, so return decoded "something"
                    text = part.get_payload(decode=True)
                    continue

                charset = part.get_content_charset()

                if part.get_content_type() == 'text/plain':
                    text = str(part.get_payload(decode=True), str(charset), "ignore").encode('utf8', 'replace')

                if part.get_content_type() == 'text/html':
                    html = str(part.get_payload(decode=True), str(charset), "ignore").encode('utf8', 'replace')

            if text is not None:
                return text.strip()
            else:
                return html.strip()
        else:
            text = str(msg.get_payload(decode=True), msg.get_content_charset(), 'ignore').encode('utf8', 'replace')
            return text.strip()

    def get_new_emails(self, latest_uid):             #default gets latest email
        index = self.email_uids.index(str(latest_uid).encode('ASCII'))
        email_uids_new = self.email_uids[(index+1):]

        emails = []
        for email_uid in email_uids_new:
            ema = self.get_email(email_uid)
            emails.append(ema)

        return emails

    def get_email(self, email_uid):             #default gets latest email
        mail = self.mail
        result, data = mail.uid('fetch', email_uid, '(RFC822)')
        raw_email = data[0][1]

        email_obj = dict()

        try:
            email_message = email.message_from_string(raw_email.decode('utf8') )
            from_contact = dict()
            email_from = email.utils.parseaddr(email_message['From'])   # for parsing "FirstName LastName" <email@domain.com>
            from_contact['name']= email_from[0]
            from_contact['id']= email_from[1]
            email_obj['from'] = from_contact
            email_obj['to'] = email_message['To'].split(',')
            if email_message['Cc']:
                email_obj['cc'] = email_message['Cc'].split(',')
            else:
                email_obj['cc'] = []
            email_obj['date'] = email_message['Date']
            # email_obj['content-type'] = email_message['Content-Type']
            # email_obj['mime-version'] = email_message['MIME-Version']
            email_obj['subject'] = email_message['Subject']
            email_obj['body'] = self.get_decoded_email_body(raw_email)
        except:
            pass

        return email_obj

    def all_emails(self):
        emails = []
        for i in range(len(self.email_uids)):
            emails.append(self.get_email(i))

        return emails


contact = { 'name':'Anish Saha',
            'id': 'anishsaha12@gmail.com',
            'password': 'ani99001161'}

my_email = EmailReader(contact)
print('\n\n\n',my_email.get_new_emails(7341))