import argparse
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(host=None, port=None, login=None, password=None, sender=None,
              to=None,subject=None, text=None, html=None, debuglevel=2):
    """ Send email """

    # Compose mail headers
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to

    # Compose mail body
    text_part = MIMEText(text, 'plain')
    msg.attach(text_part)
    if len(html):
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

    # Connect and authenticate
    smtp = SMTP()
    smtp.set_debuglevel(debuglevel)
    smtp.connect(host, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(login, password)

    try:
    	smtp.sendmail(sender, to, msg.as_string())
    finally:
    	smtp.close()
        print "Done."


parser = argparse.ArgumentParser(
    description='Send email throw specified SMTP server.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--host", required=False, default="beta.debugmail.io", help="SMTP host")
parser.add_argument("--port", required=False, type=int, default=9025, help="SMTP port")
parser.add_argument("--login", required=True, help="Auth login")
parser.add_argument("--password", required=True, help="Auth password")
parser.add_argument("--sender", required=False, default="john.doe@example.org", help="Sender email address")
parser.add_argument("--to", required=False, default="jane.doe@example.org", help="Receiver email address")
parser.add_argument("--subject", required=True, help="Email subject")
parser.add_argument("--text", required=True, help="Email body (plain text)")
parser.add_argument("--html", required=False, default="", help="Email body (html)")
parser.add_argument("--debuglevel", required=False, type=int, default=0)

args = parser.parse_args()
kwargs = args.__dict__
send_mail(**kwargs)