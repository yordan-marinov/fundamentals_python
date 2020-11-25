import re

text = input()

regex = r"( )([a-z0-9]+[a-z0-9._-]+)@([a-zA-Z0-9-]+)\.([a-zA-Z0-9.]+)\b"

emails = re.finditer(regex, text)

[
    print(email.group(0))
    for email in emails
]