import traceback



class message_request:
    def toDict(self):
        d = {
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "message_type": self.message_type,
            "GID": self.GID,
        }
        return d

    def recieve_message(self, json):
        return "here are your messages: bla bla bla"
        # try:
        #     if not json.has_key("commodity"):
        #         return "No commodity"
        #
        #     if not MarketState.commodities.has_key(json["commodity"]):
        #         return "Bad commodity"
        #
        #     self.commodity = int(json["commodity"])
        #     return RequestOperations.processReq(self)
        # except Exception as e:
        #     print(traceback.print_exc())
        #     return str(e)

    def send_message(self, json):
        return "thanks for your message. here is the message ID: blabla"
        # try:
        #     if not json.has_key("id"):
        #         return "No query id"
        #     self.id = int(json["id"])
        #
        #     return RequestOperations.processReq(self)
        # except Exception as e:
        #     print(traceback.print_exc())
        #     return str(e)

    requestTypes = {"send": send_message, "receive": recieve_message}

    def loadFromJson(self, json):
        try:
            if not "user_name" in json:
                return "No user name"
            if not "first_name" in json:
                return "No first name"
            if not "last_name" in json:
                return "No last name"
            if not "GID" in json:
                return "No group id"
            if not "message_type" in json:
                return "No message type"

            user_name = json["user_name"]#.encode("utf8")
            first_name = json["first_name"]#.encode("utf8")
            last_name = json["last_name"]#.encode("utf8")
            GID = json["GID"]#.encode("utf8")
            message_type = json["message_type"]#.encode("utf8")

            if message_type not in self.requestTypes:
                print(message_type)
                return "Bad request type"

            self.user_name = user_name
            self.first_name = first_name
            self.last_name = last_name
            self.GID = GID
            self.message_type= message_type

            # userTimings[self.user].append(time.time())
            # userTimings[self.user] = userTimings[self.user][-20:]
            # if userTimings[self.user][-1] - userTimings[self.user][0] < 10:
            #     print("Penalty for user %s" % (self.user))
            #     MarketState.semaphore.release()
            #     time.sleep(120)
            #     MarketState.semaphore.acquire()
            #
            # if not json.has_key("type"):
            #     return "No type key"

            # self.type = json["type"].encode("utf8")

            print("User %s, first name %s, last name %s, gid %s Request %s" % (self.user_name,self.first_name,self.last_name,self.GID, self.message_type))



            resp = self.requestTypes[self.message_type](self, json)
            # if nonce is not None:
            #     cipher = ""  # pkcs.new(public_key_object)
            #     resp = "".join(map(lambda i: cipher.encrypt(resp[i:i + 64]), range(0, len(resp), 64)))
            #     return resp.encode('base64')
            # else:
            #     return resp
            return resp
        except Exception as e:
            print(traceback.print_exc())
            return str(e)


#MarketState.activeQueries = {}  # pickle.load(open("active_queries.pkl",'r'))