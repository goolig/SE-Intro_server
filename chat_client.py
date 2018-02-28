import json
import string
import urllib
import pickle
import argparse
import sys
import time
import random
import traceback
import os
import urllib.parse
import urllib.request

def make_req(data):
    url = 'http://127.0.0.1:80'
    # values = {'name': 'Michael Foord',
    #           'location': 'Northampton',
    #           'language': 'Python'}

    print(data)
    data = json.dumps(data)
    data = data.encode('utf8')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    return the_page


def send_message(user_name,first_name,last_name, gid, message_text):
    req = {
        "user_name": user_name,
		"first_name":first_name, "last_name":last_name, "GID":gid, "message_text":message_text, "message_type":"send"
	}
    return make_req(req)

def random_string(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

user_name = random_string(7)
first_name =random_string(5)
last_name = random_string(4)
gid = random_string(3)

while True:
    try:
        send_message(user_name,first_name,last_name,gid,random_string(random.randint(1,10)))
    except Exception as e:
        print(traceback.print_exc())
        exit()
    time.sleep(random.randint(1,10))

