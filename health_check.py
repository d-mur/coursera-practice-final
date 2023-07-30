#!/usr/bin/env python3
import os
import psutil
from socket import gethostbyname
import emails


failures = []

if psutil.cpu_percent() > 80.0:
  failures.append('Error - CPU usage is over 80%')

if psutil.disk_usage("/").percent > 100.0-20:
  failures.append('Error - Available disk space is less than 20%')

if psutil.virtual_memory().available / 1024 / 1024 < 500.0:
  failures.append('Error - Available memory is less than 500MB')

try:
  ip =  gethostbyname('localhost')
  if ip  != '127.0.0.1':
    failures.append('Error - localhost cannot be resolved to 127.0.0.1')
except Error:
  failures.append('Error - localhost cannot be resolved to 127.0.0.1')

sender = "automation@example.com"
recipient = os.getlogin()
body = "Please check your system and resolve the issue as soon as possible"
for subject in failures:
  message = emails.generate_email(sender, recipient, subject, body)
  emails.send_email(message)
