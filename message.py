import json
import time
import traceback
import uuid


class message():
	def __init__(self,user_name, message_content, message_date, group_id):
		self.user_name=user_name
		self.message_content=message_content
		self.message_date = message_date
		self.group_id = group_id
		self.guid = str(uuid.uuid4())
		self.server_time = int(time.time() * 1000)

	def __str__ (self):
		return f"{self.user_name}, {self.message_content}, {self.message_date}, {self.group_id}, {self.guid},{self.server_time}"

	def to_dict(self):
		try:
			return {"userName": self.user_name, "messageGuid": self.guid, "groupID": self.group_id, "msgDate": self.server_time,
			 "messageContent": self.message_content}
		except Exception as e:
			print(traceback.print_exc())
			return str(e)

	def to_json(self):
		return json.dumps(self.to_dict)