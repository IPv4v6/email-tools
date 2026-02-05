#!/usr/bin/env python3

"""
IMAP folder lister

This script connects to an IMAP server and lists all folders.
"""

import argparse
import imaplib
import codecs

a = argparse.ArgumentParser()
a.add_argument('-s', '--server', required=True)
a.add_argument('-P', '--port', type=int, default=993, help='the server port (default: %(default)s)')
a.add_argument('-u', '--username', required=True)
a.add_argument('-p', '--password', required=True)

args = a.parse_args()

i = imaplib.IMAP4_SSL(host=args.server)
i.login(args.username, args.password)

ret, data = i.list()
for folder in data:
	# see RFC 3501 Mailbox International Naming Convention
	folder_rep = folder.replace(b'&', b'+').replace(b',', b'/')
	folder_dec = codecs.decode(folder_rep, 'utf-7')
	folder_spl = folder_dec.split(' "/" ')[-1]
	print(folder_spl)

i.logout()
