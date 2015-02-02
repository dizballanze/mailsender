Simple email sending cli-tool, for testing purposes
===================================================

Features:
---------

 -  HTML and/or TXT content.
 -  TLS support.
 -  Multiple attachments.
 -  Flood - send same mail multiple times through one connection.


Usage:
------

    python mail.py -h

```
usage: mail.py [-h] [--host HOST] [--port PORT] --login LOGIN --password
               PASSWORD [--sender SENDER] [--to TO] --subject SUBJECT --text
               TEXT [--html HTML] [--tls] [--no-tls] [--debuglevel DEBUGLEVEL]
               [--attachments ATTACHMENTS] [--flood FLOOD]

Send email through specified SMTP server.

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
  --attachments ATTACHMENTS
                        One or few files to attach (default: None)
  --flood FLOOD         Count of messages send (through one connection)
                        (default: 1)
```

Usage example:
--------------

```
python mail.py --host="debugmail.io" --login="john.doe@example.org" --password="very secret" --subject="Test subject" --text="Test message" --html="<h1>Wow, so electronic, very mail</h1>"
```

with attachments:

```
python mail.py --login="john.doe@gmail.com" --password="123123" --port="25" --host="debugmail.io" --text="Text content" --html="<h1>HTML content</h1>" --subject="test" --attachments="/tmp/attachment1.txt" --attachments="/tmp/attachment2.txt"
```

License
-------

The MIT License (MIT)

Copyright (c) 2015 Yuri Shikanov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.