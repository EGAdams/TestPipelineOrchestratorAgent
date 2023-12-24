class MessageSender:
    def __init__(self):
        self.messages = []

    def send(self, to, subject, content):
        message = {
            "to": to,
            "subject": subject,
            "content": content
        }
        self.messages.append( message )