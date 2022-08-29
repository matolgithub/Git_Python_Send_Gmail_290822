import smtplib
from email.mime.text import MIMEText


# GMAIL.COM
# class Mail:
#     def __init__(self, mail='8888888888888@gmail.com'):
#         self.mail = mail
#
#     def send_email(self, message="Hi! It's message from the python code!"):
#         sender = "8888888888888@gmail.com"
#         password = "888888888888888888"
#
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#
#         try:
#             server.login(user=sender, password=password)
#             server.sendmail(from_addr=sender, to_addrs=self.mail, msg=message)
#             sent_result = "The message was sent successfully!"
#         except Exception as _ex:
#             sent_result = f"{_ex}\nCheck your login or password, please!"
#         print(sent_result)
#
#         return sent_result

class Mail:
    def __init__(self, mail='00000000000000@mail.ru'):
        self.mail = mail

    def send_email(self, message="Hi! It's message from the python code!\nПривет, май френд!"):
        sender = "000000000000000000000@mail.ru"
        password = "4000000000000000000"

        server = smtplib.SMTP("smtp.mail.ru", 587)
        server.starttls()

        try:
            server.login(user=sender, password=password)
            msg = MIMEText(message)
            msg['Subject'] = "Вот тебе и тема письма на русском языке, сэр!"
            server.sendmail(sender, self.mail, msg.as_string())
            # server.sendmail(sender, self.mail, f"Subject: Test!!!!!!!\n{message}")
            sent_result = "The message was sent successfully!"
        except Exception as _ex:
            sent_result = f"{_ex}\nCheck your login or password, please!"
        print(sent_result)

        return sent_result


if __name__ == '__main__':
    mail_object = Mail()
    mail_object.send_email()
