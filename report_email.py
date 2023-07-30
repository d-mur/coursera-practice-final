#!/usr/bin/env python3
import os
import reports
from datetime import date
import emails


if __name__ == "__main__":
  attachment = r'/tmp/processed.pdf'
  title = 'Processed Update on ' + date.today().strftime("%B %d, %Y")
  paragraph = ''

  path_to_descr = 'supplier-data/descriptions/'
  for file in sorted(os.listdir(path_to_descr)):
    if file[-4:].lower() == '.txt':
      with open(path_to_descr+file, 'r') as f:
        lines = f.readlines()
        paragraph += f'name: {lines[0]}<br/>'
        paragraph += f'weight: {lines[1]}<br/>'
        paragraph += '<br/>'

  reports.generate_report(attachment, title, paragraph)

  sender = "automation@example.com"
  recipient = os.getlogin()
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = r"/tmp/processed.pdf"
  message = emails.generate_email(sender, recipient, subject, body, attachment)
  emails.send_email(message)
