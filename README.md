Simple email sending cli-tool, for testing purpose
==================================================

Usage:
------

    python mail.py -h

```
usage: mail.py [-h] [--host HOST] [--port PORT] --login LOGIN --password
               PASSWORD [--sender SENDER] [--to TO] --subject SUBJECT --text
               TEXT [--html HTML] [--tls] [--no-tls] [--debuglevel DEBUGLEVEL]

Send email throw specified SMTP server.

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           SMTP host (default: beta.debugmail.io)
  --port PORT           SMTP port (default: 9025)
  --login LOGIN         Auth login (default: None)
  --password PASSWORD   Auth password (default: None)
  --sender SENDER       Sender email address (default: john.doe@example.org)
  --to TO               Receiver email address (default: jane.doe@example.org)
  --subject SUBJECT     Email subject (default: None)
  --text TEXT           Email body (plain text) (default: None)
  --html HTML           Email body (html) (default: )
  --tls                 Use TLS (default: True)
  --no-tls              Not use TLS (default: True)
  --debuglevel DEBUGLEVEL
                        Debug level (default: 0)
```

Usage example:
--------------

```
python mail.py --host="debugmail.info" --login="john.doe@example.org" --password="very secret" --subject="Test subject" --text="Test message" --html="<h1>Wow, so electronic, very mail</h1>"
```