import smtplib


class NotificationManager:
    def __init__(self):
        self.MY_EMAIL = "flight.deals.sg@gmail.com"
        self.PASSWORD = "bggknpfpcykobnuz"

    def notify(self, message, email_list):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=self.MY_EMAIL, password=self.PASSWORD)
        for email in email_list:
            connection.sendmail(from_addr=self.MY_EMAIL, to_addrs=email, msg=f"Subject:Flight Deal found\n\n{message}")
