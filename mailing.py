import smtplib
import imghdr
from email.message import EmailMessage
import os

PASSWORD = os.getenv("PASSWORD")  #PLease provide your own gmail id password by activating two step verification and add app password there to generate one.
SENDER = "vigneshbaskar2024@gmail.com"
RECEIVER = "vigneshbaskar2024@gmail.com"

def send_email(image_path):
    print("process started")
    message = EmailMessage()
    message['Subject'] = "New person has been showed up!"
    message['From'] = SENDER
    message['To'] = RECEIVER
    message.set_content("Hey, we just saw a new person!!!!!!")

    with open(image_path, "rb") as file: #Context mangers
        content = file.read()
    message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.send_message(message)
    gmail.quit()
    print("ended")

if __name__ == "__main__":
    send_email(image_path="images/192.png")
