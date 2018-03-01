import threading
from message import message

semaphore = threading.Semaphore()
messages = []

def add_message(user_name, message_content, message_date, group_id):
	m = message(user_name, message_content, message_date, group_id)
	messages.append(m)
	return m.guid