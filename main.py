import smtplib

# GMAIL.COM
class Mail:
    def __init__(self, mail='matolpydev@gmail.com'):
        self.mail = mail

    def send_email(self, message="Hi! It's message from the python code!"):
        sender = "matolpydev@gmail.com"
        password = "csszpkcslndaiita"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        try:
            server.login(user=sender, password=password)
            server.sendmail(from_addr=sender, to_addrs=self.mail, msg=message)
            sent_result = "The message was sent successfully!"
        except Exception as _ex:
            sent_result = f"{_ex}\nCheck your login or password, please!"
        print(sent_result)

        return sent_result


if __name__ == '__main__':
    mail_object = Mail()
    mail_object.send_email()
