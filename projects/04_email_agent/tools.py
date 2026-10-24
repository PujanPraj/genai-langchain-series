### Sending Email Agent - send_email


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from langchain.tools import tool

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "puzpraz123@gmail.com"
password = "----"


def send_email(to: str, subject: str, body: str):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        print("Connecting to server...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        server.login(sender_email, password)
        print("Login successful! Sending email...")

        server.sendmail(sender_email, to, message.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        server.quit()


@tool
def send_email_tool(to: str, subject: str, body: str):
    """
    Send Email to any email address by providing the correct email address, subject and body.
    Args:
        to - email address of recipent
        subject - email subject in one line
        body - email body in plane text
    """
    send_email(to, subject, body)
    return "Email sent successfully..."


ALL_TOOLS = [send_email_tool]
