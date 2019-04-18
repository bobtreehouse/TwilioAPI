# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:14:27 2019

@author: bobtr
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:44:12 2019

@author: bobtr
"""

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from credentials import (account_sid, auth_token, recipient0, recipient1, recipient2, recipient3, recipient4, recipient5, recipient6, recipient7, recipient8, recipient9, recipient10, recipient11, recipient12, recipient13, recipient14, recipient15, recipient16, recipient17, recipient18, recipient19, recipient20, recipient21, recipient22, recipient23, recipient24, recipient25, recipient26, recipient27, recipient28, recipient29, recipient30, recipient31, recipient32, recipient33, recipient34, recipient35, recipient36, recipient37, 
recipient38, recipient39, recipient40, recipient41, recipient42, recipient43, recipient44, recipient45, recipient46, recipient47, recipient48, recipient49, recipient50, recipient51, recipient52, recipient53, recipient54, recipient55, recipient56, recipient57, my_twilio)

# Your Account Sid and Auth Token from twilio.com/console

client = Client(account_sid, auth_token)

my_msg = '**Reminder: APOLOGIES if you received previous auto-text stating practice was on. NO wrestling practice tonight nor next thurs (4/18 & 4/25). We resume Thursday (5/2). Bob Trieste 917-806-6333. ENJOY THE BREAK !!'

message = client.messages.create(to=recipient0, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient1, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient2, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient3, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient4, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient5, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient6, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient7, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient8, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient9, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient10, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient11, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient12, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient13, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient14, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient15, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient16, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient17, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient18, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient19, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient20, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient21, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient22, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient23, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient24, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient25, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient26, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient27, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient28, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient29, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient30, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient31, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient32, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient33, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient34, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient35, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient36, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient37, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient38, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient39, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient40, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient41, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient42, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient43, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient44, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient45, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient46, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient47, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient48, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient49, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient50, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient51, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient52, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient53, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient54, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient55, from_=my_twilio, body=my_msg)
print(message.sid)

message = client.messages.create(to=recipient56, from_=my_twilio, body=my_msg)
print(message.sid)
    
message = client.messages.create(to=recipient57, from_=my_twilio, body=my_msg)
print(message.sid)